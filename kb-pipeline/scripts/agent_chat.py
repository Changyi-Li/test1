"""RAGFlow agent（工作流）对话与引用渲染 —— 把 agent 嵌进自己的页面。

背景: RAGFlow 自带聊天页把检索命中的所有来源文档渲染成回答底部的一列文件卡片
（前端组件 ReferenceDocumentList），没有单独隐藏它的开关（只有「显示引用」总开关，
关掉则文中引用也没了）。本模块绕开自带聊天页，直接调 agent 对话 API，只取正文与
引用数据，由自己渲染: 正文里的 [ID:N] 引用标记做成可点击（悬停/点击看对应 chunk），
底部不渲染文件列表。机制经 v0.26.4 源码核对 + 本机实测验证。

端点（v0.26.4）:
  GET  /api/v1/agents?page=0&page_size=100   -> data.canvas[]（id/title/canvas_category）
  POST /api/v1/agents/chat/completions       裸 OpenAI 格式（非 {code,data} 包装）
    body: {"agent_id", "openai-compatible": true,
           "messages": [{"role":"user","content":...}], "stream": false}
    choices[0].message.content    回答正文（含 [ID:N] 标记）
    choices[0].message.reference  引用: {"chunks":{cid:chunk},"doc_aggs":{...}}
                                 或直接 {cid:chunk}，两种都要兼容
  引用编号: kb_prompt 用 "ID: {hash_str2int(chunk_id,500)}"，add_reference 的 dict key
            同值 -> 正文 [ID:N] 直接查 chunks[str(N)]。

用法（后端集成）:
  from agent_chat import AgentChatClient, render_answer_page, build_payload
  client = AgentChatClient(cfg.base_url, api_key)
  answer = client.converse(agent_id, "怎么创建组件呢")
  html = render_answer_page(answer.content, answer.chunks,
                            question="怎么创建组件呢")   # 自包含整页（含渲染 JS）
  # 或把 build_payload(...) 的 JSON 交给自己的前端，用页面里的同一套渲染逻辑

用法（演示 CLI，需 RAGFLOW_API_KEY）:
  py scripts/agent_chat.py --agent-id <id> "怎么创建组件呢"
  写同目录 agent-chat-preview.html 并打开；底部浮条切换 inline/tooltip/popover 三种引用渲染。
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import webbrowser
from dataclasses import dataclass, field
from pathlib import Path
from urllib import error, request

from ragflow_api import RagflowError

urlopen = request.urlopen  # 测试可 monkeypatch

PAGE_SIZE = 100  # v0.26.4 上限，传大报错 "page_size must be <= 100"
CITE_RE = re.compile(r"\[(?:ID\s*:\s*)?(\d+)\]")
DEFAULT_TIMEOUT = 300
DEFAULT_OUT = Path(__file__).resolve().parent / "agent-chat-preview.html"


@dataclass
class Chunk:
    """单个引用 chunk 的渲染字段（从 v0.26.4 各种 chunk 形状归一而来）。"""
    content: str
    doc_name: str = ""
    url: str = ""
    similarity: float | None = None


@dataclass
class AgentAnswer:
    content: str
    chunks: dict[str, Chunk] = field(default_factory=dict)
    session_id: str = ""
    agent_id: str = ""


# --------------------------------------------------------------------------- 客户端
def _normalize_reference(reference: object) -> dict[str, Chunk]:
    """把 v0.26.4 两种 reference 形状归一成 {cid: Chunk}。

    openai 模式是 {"chunks":{cid:chunk},"doc_aggs":{...}} 或直接 {cid:chunk}；
    常规模式是 {"chunks":{...},"doc_aggs":{...}}。chunk 字段也两种键都要兼容。
    """
    if isinstance(reference, dict) and "chunks" in reference:
        raw_chunks = reference["chunks"] or {}
    else:
        raw_chunks = reference or {}
    if not isinstance(raw_chunks, dict):
        raw_chunks = {}
    chunks: dict[str, Chunk] = {}
    for cid, ck in raw_chunks.items():
        if not isinstance(ck, dict):
            continue
        chunks[str(cid)] = Chunk(
            content=ck.get("content_with_weight") or ck.get("content") or "",
            doc_name=ck.get("docnm_kwd") or ck.get("document_name") or "",
            url=ck.get("url") or "",
            similarity=ck.get("similarity"),
        )
    return chunks


class AgentChatClient:
    """RAGFlow agent 对话客户端（薄 HTTP，零第三方依赖）。

    agent 两个端点独立于导入工具（converse 响应是裸 OpenAI 格式，没有 {code,data}
    包装），故不复用 RagflowClient，单独实现；错误统一抛 RagflowError。
    """

    def __init__(self, base_url: str, api_key: str,
                 timeout: int = DEFAULT_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def _request(self, method: str, path: str,
                 body: object | None = None) -> dict:
        url = f"{self.base_url}{path}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            payload = json.dumps(body).encode("utf-8")
        req = request.Request(url, data=payload, headers=headers, method=method)
        try:
            with urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read().decode("utf-8")
        except error.HTTPError as exc:
            raise RagflowError(f"HTTP {exc.code} {method} {path}: {exc.reason}")
        except error.URLError as exc:
            raise RagflowError(f"网络错误 {method} {path}: {exc.reason}")
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RagflowError(f"RAGFlow 响应不是 JSON（{method} {path}）: {exc}")
        if isinstance(data, dict) and data.get("code") not in (None, 0):
            raise RagflowError(
                f"RAGFlow 返回 code={data.get('code')}: {data.get('message')}"
                f"（{method} {path}）")
        return data

    def list_agents(self, title: str | None = None) -> list[dict]:
        """列出 API key 可见的 agent；title 按标题子串过滤。"""
        data = self._request("GET",
                             f"/api/v1/agents?page=0&page_size={PAGE_SIZE}")
        canvas = (data.get("data") or {}).get("canvas") or []
        agents = [c for c in canvas if isinstance(c, dict)]
        if title:
            agents = [a for a in agents if title in (a.get("title") or "")]
        return agents

    def resolve_agent(self, agent_id: str | None = None,
                      title: str | None = None) -> dict:
        """按 id 或标题子串选 agent；不提供时取第一个。"""
        agents = self.list_agents()
        if not agents:
            raise RagflowError("该 API key 下没有任何 agent")
        if agent_id:
            for a in agents:
                if a.get("id") == agent_id:
                    return a
            raise RagflowError(f"找不到 agent id={agent_id}（现有: "
                               f"{', '.join(a.get('title', '?') for a in agents)}）")
        if title:
            matches = [a for a in agents if title in (a.get("title") or "")]
            if matches:
                return matches[0]
            raise RagflowError(f"没有标题含 {title!r} 的 agent。现有: "
                               f"{', '.join(a.get('title', '?') for a in agents)}")
        return agents[0]

    def converse(self, agent_id: str, question: str,
                 session_id: str | None = None) -> AgentAnswer:
        """发一条消息（openai-compatible 模式），返回回答正文 + 引用 chunks。

        该模式无会话记忆，适合一次性查询；聊天机器人请用 converse_session()。
        """
        body: dict = {
            "agent_id": agent_id,
            "openai-compatible": True,
            "messages": [{"role": "user", "content": question}],
            "stream": False,
        }
        if session_id:
            body["session_id"] = session_id
        resp = self._request("POST", "/api/v1/agents/chat/completions",
                             body=body)
        message = ((resp.get("choices") or [{}])[0].get("message") or {})
        return AgentAnswer(
            content=message.get("content") or "",
            chunks=_normalize_reference(message.get("reference")),
            session_id=str(resp.get("id") or ""),
            agent_id=agent_id,
        )

    def converse_session(self, agent_id: str, question: str,
                         session_id: str | None = None) -> AgentAnswer:
        """多轮会话（常规模式）：会话消息在 RAGFlow 侧累积，支持追问上下文。

        请求是 {"agent_id","query","session_id"?}，不带 openai-compatible；
        响应 {code, data:{session_id, data:{content, reference}}}。
        每次返回的 answer.session_id 传给下一次调用即可续会话；不带则开新会话。
        """
        body: dict = {"agent_id": agent_id, "query": question, "stream": False}
        if session_id:
            body["session_id"] = session_id
        resp = self._request("POST", "/api/v1/agents/chat/completions",
                             body=body)
        data = resp.get("data") or {}
        inner = data.get("data") or {}
        return AgentAnswer(
            content=inner.get("content") or "",
            chunks=_normalize_reference(inner.get("reference")),
            session_id=str(data.get("session_id") or ""),
            agent_id=agent_id,
        )

    def converse_stream(self, agent_id: str, question: str,
                        session_id: str | None = None):
        """流式（SSE）多轮会话；yield 每个事件 dict（含 session_id/reference）。

        RAGFlow 常规模式 stream=true 返回 SSE 行: data: {event, data:{content,
        reference}, session_id}，以 data: [DONE] 结束。content 增量靠 message
        事件累积，reference 在 message_end 事件里，session_id 每条事件都有。
        """
        body: dict = {"agent_id": agent_id, "query": question, "stream": True}
        if session_id:
            body["session_id"] = session_id
        url = f"{self.base_url}/api/v1/agents/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}",
                   "Content-Type": "application/json"}
        req = request.Request(url, data=json.dumps(body).encode("utf-8"),
                              headers=headers, method="POST")
        try:
            with urlopen(req, timeout=self.timeout) as resp:
                for raw in resp:
                    line = raw.decode("utf-8").strip()
                    if not line.startswith("data:"):
                        continue
                    payload = line[5:].strip()
                    if payload == "[DONE]":
                        return
                    try:
                        yield json.loads(payload)
                    except json.JSONDecodeError:
                        continue
        except error.HTTPError as exc:
            raise RagflowError(f"HTTP {exc.code} POST /agents/chat/completions:"
                               f" {exc.reason}")
        except error.URLError as exc:
            raise RagflowError(f"网络错误 POST /agents/chat/completions:"
                               f" {exc.reason}")


# --------------------------------------------------------------------------- 解析
def parse_citations(content: str) -> list[tuple[str, str]]:
    """返回 [(原标记, 引用编号)]，按出现顺序去重。"""
    seen: list[tuple[str, str]] = []
    for m in CITE_RE.finditer(content):
        idx = m.group(1)
        if idx not in [s[1] for s in seen]:
            seen.append((m.group(0), idx))
    return seen


def chunk_to_dict(chunk: Chunk) -> dict:
    return {"content": chunk.content, "doc_name": chunk.doc_name,
            "url": chunk.url, "similarity": chunk.similarity}


def build_payload(content: str, chunks: dict[str, Chunk], *,
                  question: str = "", agent_title: str = "",
                  agent_id: str = "") -> dict:
    """给前端渲染用的 JSON payload（content + chunks，无文件列表）。"""
    ordered = sorted(chunks.items(), key=lambda kv: (int(kv[0])
                                                     if kv[0].isdigit() else 0))
    return {
        "agent": {"id": agent_id, "title": agent_title},
        "question": question,
        "content": content,
        "chunks": {cid: chunk_to_dict(c) for cid, c in ordered},
    }


# --------------------------------------------------------------------------- 渲染
HTML_TEMPLATE = r"""<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>Agent 回答 · 引用渲染</title>
<style>
  body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;color:#1f2328;
       background:#f6f8fa;padding-bottom:80px;}
  .wrap{max-width:760px;margin:24px auto;background:#fff;border:1px solid #d0d7de;
        border-radius:10px;padding:28px 32px;}
  h1{font-size:18px;margin:0 0 4px;}
  .sub{color:#656d76;font-size:13px;margin:0 0 18px;}
  .q{background:#eff7ff;border:1px solid #c8e1ff;border-radius:8px;padding:10px 14px;
     margin:0 0 16px;font-size:14px;}
  .q b{color:#0550ae;}
  .md h1,.md h2,.md h3{line-height:1.3;}
  .md h2{font-size:18px;border-bottom:1px solid #d8dee4;padding-bottom:4px;}
  .md p{line-height:1.75;font-size:15px;margin:10px 0;}
  .md li{line-height:1.7;font-size:15px;}
  .md pre{background:#f6f8fa;border:1px solid #d0d7de;border-radius:6px;
          padding:12px;overflow:auto;font-size:13px;}
  .md code{background:#f6f8fa;border-radius:4px;padding:1px 5px;font-size:13px;}
  .md pre code{background:none;padding:0;}
  .md blockquote{border-left:4px solid #d0d7de;color:#57606a;margin:10px 0;padding:2px 12px;}
  .md table{border-collapse:collapse;}
  .md th,.md td{border:1px solid #d0d7de;padding:6px 10px;}
  .md img{max-width:100%;}
  /* 引用 */
  .cite{display:inline-block;min-width:1.1em;text-align:center;margin:0 1px;
        font-size:11px;line-height:1.4;color:#fff;background:#0969da;
        border-radius:3px;padding:0 3px;cursor:pointer;vertical-align:super;
        font-style:normal;font-weight:600;user-select:none;}
  .cite:hover{background:#054da6;}
  .cite-missing{background:#cf222e;}
  /* tooltip / popover / inline 共用卡片 */
  .cite-card{position:absolute;z-index:10;max-width:360px;max-height:280px;overflow:auto;
             background:#fff;border:1px solid #d0d7de;border-radius:8px;
             box-shadow:0 6px 24px rgba(31,35,40,.18);padding:10px 12px;font-size:13px;
             line-height:1.6;}
  .cite-card .h{font-weight:600;color:#0550ae;margin-bottom:6px;font-size:12px;
                border-bottom:1px solid #eaeef2;padding-bottom:5px;display:flex;
                justify-content:space-between;gap:10px;}
  .cite-card .c{white-space:pre-wrap;word-break:break-word;}
  .cite-card .u{color:#0969da;text-decoration:none;font-size:12px;}
  .chunk-expand{margin:10px 0 10px 26px;border-left:3px solid #0969da;
                background:#f3f8ff;border-radius:0 8px 8px 0;padding:10px 14px;
                font-size:13px;line-height:1.6;}
  .chunk-expand .h{font-weight:600;color:#0550ae;margin-bottom:6px;}
  .chunk-expand .c{white-space:pre-wrap;word-break:break-word;}
  .state{border-top:1px solid #eaeef2;margin-top:22px;padding-top:12px;
         color:#656d76;font-size:12.5px;line-height:1.7;}
  .state b{color:#1f2328;}
  .warn{background:#fff8c5;border:1px solid #eed888;border-radius:8px;padding:10px 14px;
        font-size:13.5px;margin-top:14px;color:#5a4b00;}
  #bar{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid #d0d7de;
       padding:10px 20px;display:flex;align-items:center;gap:8px;font-size:13px;z-index:20;}
  #bar button{border:1px solid #d0d7de;background:#fff;border-radius:6px;padding:6px 12px;
              cursor:pointer;font-size:13px;}
  #bar button.on{background:#0969da;border-color:#0969da;color:#fff;}
</style>
</head>
<body>
<div class="wrap">
  <h1>Agent 回答 · 引用渲染</h1>
  <p class="sub">正文 [ID:N] 可点击查看 chunk；<b>底部不渲染文件列表</b>。底部浮条切换渲染变体。</p>
  <div class="q"><b>Q:</b> <span id="question"></span></div>
  <div class="md" id="answer"></div>
  <div class="warn" id="warn" style="display:none"></div>
  <div class="state" id="state"></div>
</div>
<div id="bar">
  <span>引用渲染：</span>
  <button data-v="inline" class="on">inline · 点击展开</button>
  <button data-v="tooltip">tooltip · 悬停</button>
  <button data-v="popover">popover · 点击</button>
  <span id="modeDesc" style="color:#656d76;margin-left:10px"></span>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
const CITE_RE = /\[(?:ID\s*:\s*)?(\d+)\]/g;
let MODE = new URLSearchParams(location.search).get('variant') || 'inline';

// ---- 最小 markdown 渲染（够用即可）----
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function inline(md){
  let s = esc(md);
  s = s.replace(/`([^`]+)`/g,(m,c)=>'<code>'+c+'</code>');
  s = s.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
  s = s.replace(/\*([^*]+)\*/g,'<em>$1</em>');
  s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2" target="_blank">$1</a>');
  return s;
}
function renderMarkdown(md){
  md = md.replace(CITE_RE,(m,n)=>'\x01'+n+'\x02');
  const lines = md.split('\n');
  const out = []; let i = 0; let code = null; let curList = null;
  const flushList = ()=>{ if(curList && curList.items.length){ out.push('<'+curList.tag+'>'+curList.items.map(x=>'<li>'+x+'</li>').join('')+'</'+curList.tag+'>'); } curList=null; };
  const block = h=>{ flushList(); out.push(h); };
  while(i<lines.length){
    const line = lines[i];
    const fence = line.match(/^```(\w*)\s*$/);
    if(fence){ if(code===null){code=[];} else{ block('<pre class="code"><code>'+code.join('\n')+'</code></pre>'); code=null; } i++; continue; }
    if(code!==null){ code.push(esc(line)); i++; continue; }
    if(line.trim()===''){ flushList(); i++; continue; }
    let m = line.match(/^(#{1,6})\s+(.*)$/);
    if(m){ const lvl=m[1].length; block('<h'+lvl+'>'+inline(m[2])+'</h'+lvl+'>'); i++; continue; }
    if(/^\s*([-*_])\s*\1\s*\1+\s*$/.test(line)){ block('<hr>'); i++; continue; }
    let u = line.match(/^\s*[-*+]\s+(.*)$/);
    if(u){ if(curList && curList.tag!=='ul'){ flushList(); } curList=curList||{tag:'ul',items:[]}; curList.items.push(inline(u[1])); i++; continue; }
    let o = line.match(/^\s*\d+[.)]\s+(.*)$/);
    if(o){ if(curList && curList.tag!=='ol'){ flushList(); } curList=curList||{tag:'ol',items:[]}; curList.items.push(inline(o[1])); i++; continue; }
    let bq = line.match(/^\s*>\s?(.*)$/);
    if(bq){ const qs=[bq[1]]; while(i+1<lines.length && /^\s*>/.test(lines[i+1])){ qs.push(lines[i+1].replace(/^\s*>\s?/,'')); i++; } block('<blockquote>'+qs.map(q=>inline(q)).join('<br>')+'</blockquote>'); i++; continue; }
    const para=[line];
    while(i+1<lines.length){
      const nxt=lines[i+1];
      if(nxt.trim()===''||/^```/.test(nxt)||/^#{1,6}\s/.test(nxt)||/^\s*([-*+>]|\d+[.)])\s/.test(nxt)) break;
      para.push(nxt); i++;
    }
    block('<p>'+para.map(p=>inline(p)).join('<br>')+'</p>');
    i++;
  }
  flushList();
  if(code!==null){ out.push('<pre class="code"><code>'+code.join('\n')+'</code></pre>'); }
  return out.join('\n').replace(/\x01(\d+)\x02/g,(m,n)=>citeSup(n));
}
function citeSup(n){
  const hit = DATA.chunks && DATA.chunks[n];
  return '<sup class="cite'+(hit?'':' cite-missing')+'" data-idx="'+esc(n)+'">'+esc(n)+'</sup>';
}

// ---- 三种变体交互 ----
function chunkBody(idx){
  const c = DATA.chunks && DATA.chunks[idx];
  if(!c) return '<div class="h">引用 '+idx+' <span style="color:#cf222e">未匹配到 reference</span></div><div class="c">(reference 里没有这个编号)</div>';
  const name = c.doc_name ? esc(c.doc_name) : '(无文档名)';
  const url = c.url ? ' <a class="u" href="'+esc(c.url)+'" target="_blank">源页面 ↗</a>' : '';
  return '<div class="h">'+name+' <span>#'+esc(idx)+(c.similarity!=null?' · '+Number(c.similarity).toFixed(3):'')+'</span></div>'+
         '<div class="c">'+esc(c.content)+'</div>'+url;
}
let tipEl=null, popEl=null, openPop=null;
function removeCard(){  // 只清 tooltip/popover 浮层，不动 inline 展开框
  if(tipEl){ tipEl.remove(); tipEl=null; }
  if(popEl){ popEl.remove(); popEl=null; openPop=null; }
}
function clearInline(){ document.querySelectorAll('.chunk-expand').forEach(e=>e.remove()); }
function showTip(el,idx){
  removeCard();
  tipEl=document.createElement('div'); tipEl.className='cite-card';
  tipEl.innerHTML=chunkBody(idx); document.body.appendChild(tipEl);
  const move=e=>{ const r=tipEl.getBoundingClientRect(); let x=e.clientX+14, y=e.clientY+14;
    if(x+r.width>innerWidth) x=e.clientX-14-r.width; if(y+r.height>innerHeight) y=e.clientY-14-r.height;
    tipEl.style.left=x+'px'; tipEl.style.top=y+'px'; };
  const leave=()=>{ tipEl.remove(); tipEl=null; el.removeEventListener('mousemove',move); };
  el.addEventListener('mousemove',move); el.addEventListener('mouseleave',leave,{once:true});
  move({clientX:el.getBoundingClientRect().right, clientY:el.getBoundingClientRect().top});
}
function showPop(el,idx){
  if(openPop===el){ removeCard(); return; }
  removeCard();
  openPop=el; popEl=document.createElement('div'); popEl.className='cite-card';
  popEl.innerHTML=chunkBody(idx); document.body.appendChild(popEl);
  const r=el.getBoundingClientRect(); popEl.style.left=r.left+'px'; popEl.style.top=(r.bottom+6)+'px';
}
function toggleInline(el,idx){
  const block = el.closest('p,li,h2,h3,h4,h5,h6,blockquote,pre,td') || el;
  const old = block.nextElementSibling;
  if(old && old.classList && old.classList.contains('chunk-expand')){ old.remove(); return; }
  removeCard(); clearInline();  // 只保留当前这一个展开
  const box=document.createElement('div'); box.className='chunk-expand';
  box.innerHTML=chunkBody(idx);
  block.insertAdjacentElement('afterend',box);
}
function bind(mode){
  removeCard(); clearInline();
  const answerEl = document.getElementById('answer');
  answerEl.innerHTML = renderMarkdown(DATA.content);
  answerEl.querySelectorAll('.cite').forEach(el=>{
    const idx = el.dataset.idx;
    el.style.cursor = mode==='tooltip' ? 'default' : 'pointer';
    if(mode==='tooltip'){
      el.addEventListener('mouseenter',()=>showTip(el,idx));
    } else if(mode==='popover'){
      el.addEventListener('click',ev=>{ ev.stopPropagation(); showPop(el,idx); });
    } else {
      el.addEventListener('click',ev=>{ ev.stopPropagation(); toggleInline(el,idx); });
    }
  });
}
document.addEventListener('click',e=>{ if(!e.target.closest('.cite-card')) removeCard(); });

// ---- 渲染 ----
document.getElementById('question').textContent = DATA.question;
const ans = renderMarkdown(DATA.content);
document.getElementById('answer').innerHTML = ans;
const markers=[...DATA.content.matchAll(CITE_RE)];
const found=[...new Set(markers.map(m=>m[1]))];
const missing=found.filter(n=>!(DATA.chunks&&DATA.chunks[n]));
const agent=DATA.agent||{};
document.getElementById('state').innerHTML =
  '<b>Agent:</b> '+esc(agent.title||'')+' <span style="color:#8c959f">('+esc(agent.id||'')+')</span><br>'+
  '<b>正文引用标记:</b> '+found.length+' 个（'+found.map(n=>'#'+n).join(', ')+'）　'+
  '<b>reference 块:</b> '+(DATA.chunks?Object.keys(DATA.chunks).length:0)+'　'+
  '<b>未匹配:</b> '+(missing.length?missing.join(','):'无');
if(!found.length){
  document.getElementById('warn').style.display='block';
  document.getElementById('warn').textContent='⚠ 回答正文里没有 [ID:N] 引用标记——说明工作流里 LLM 没有按引用提示输出标记（渲染没问题，是工作流/提示词的事）。reference 里有块但正文没标记，UI 也就无可点击处。';
} else if(missing.length){
  document.getElementById('warn').style.display='block';
  document.getElementById('warn').textContent='⚠ 有 '+missing.length+' 个标记在 reference 里找不到对应块（'+missing.join(', ')+'），可能标记编号是枚举序号而 reference 键是哈希，或跨了多个检索节点。';
}
const desc={tooltip:'悬停引用数字查看 chunk 内容',popover:'点击引用固定气泡查看',inline:'点击引用在其所在段落下方原地展开'};
document.getElementById('modeDesc').textContent='当前：'+desc[MODE];
document.querySelectorAll('#bar button').forEach(b=>{
  b.classList.toggle('on', b.dataset.v===MODE);
  b.addEventListener('click',()=>{ MODE=b.dataset.v; bind(MODE); removeCard();
    document.querySelectorAll('#bar button').forEach(x=>x.classList.toggle('on',x===b));
    document.getElementById('modeDesc').textContent='当前：'+desc[MODE];
    history.replaceState(null,'','?variant='+MODE); });
});
bind(MODE);
</script>
</body>
</html>
"""


def render_answer_page(content: str, chunks: dict[str, Chunk], *,
                       question: str = "", agent_title: str = "",
                       agent_id: str = "") -> str:
    """生成自包含 HTML 整页：正文 [ID:N] 可点击，底部不渲染文件列表。

    数据以 JSON 嵌进页面，交互由内嵌 JS 完成（inline 点击展开为默认变体）。
    后端集成若不想用整页，可改调 build_payload() 拿 JSON 交给自己前端渲染。
    """
    payload = build_payload(content, chunks, question=question,
                            agent_title=agent_title, agent_id=agent_id)
    data_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return HTML_TEMPLATE.replace("__DATA__", data_json)


# --------------------------------------------------------------------------- CLI
def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="agent_chat.py",
        description="RAGFlow agent 对话与引用渲染（正文 [ID:N] 可点击，不渲染文件列表）")
    ap.add_argument("question", nargs="?", metavar="问题",
                    help="要问的问题（省略则进入交互模式）")
    ap.add_argument("--api-key", metavar="KEY",
                    help="RAGFlow API key（默认读 RAGFLOW_API_KEY）")
    ap.add_argument("--config", metavar="PATH",
                    help="覆盖配置路径（默认 config/ragflow.json，取 base_url）")
    ap.add_argument("--agent-id", metavar="ID", help="指定 agent id")
    ap.add_argument("--agent-title", metavar="TITLE", default="Monitor",
                    help="按标题子串选 agent（默认 Monitor）")
    ap.add_argument("--output", metavar="PATH",
                    help=f"HTML 输出路径（默认 {DEFAULT_OUT}）")
    ap.add_argument("--no-open", action="store_true",
                    help="不自动打开浏览器")
    ap.add_argument("--interactive", action="store_true",
                    help="交互式连续提问（每轮独立，无会话记忆）")
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                    help=f"HTTP 超时秒数（默认 {DEFAULT_TIMEOUT}）")
    return ap


def _surface(answer: AgentAnswer, agent: dict, out_path: Path) -> None:
    """把状态打到 stdout，方便集成时核对标记命中情况。"""
    citations = parse_citations(answer.content)
    found = [idx for _, idx in citations]
    missing = [n for n in found if n not in answer.chunks]
    print("\n== Agent ==")
    print(f"  {agent.get('title')}  ({agent.get('id')})")
    print("== 回答正文（原文，含引用标记）==")
    print(f"  {answer.content}\n")
    print("== 引用解析 ==")
    print(f"  标记: {len(found)} 个 -> {found}")
    print(f"  reference 块: {len(answer.chunks)} 个 -> "
          f"{sorted(answer.chunks, key=int)}")
    print(f"  未匹配: {missing or '无'}")
    if not found:
        print("  !! 正文无 [ID:N] 标记：工作流 LLM 没按引用提示输出标记，"
              "与渲染无关，需查工作流")
    print(f"== 输出 ==")
    print(f"  {out_path}")
    for cid, ck in sorted(answer.chunks.items(), key=lambda kv: int(kv[0])):
        sim = f"{ck.similarity:.3f}" if ck.similarity is not None else "-"
        print(f"  chunk[{cid}] sim={sim} doc={ck.doc_name or '(无)'}")


def run_one(client: AgentChatClient, ns, question: str) -> None:
    agent = client.resolve_agent(ns.agent_id, ns.agent_title)
    answer = client.converse(agent["id"], question)
    out_path = Path(ns.output) if ns.output else DEFAULT_OUT
    out_path.write_text(
        render_answer_page(answer.content, answer.chunks,
                           question=question,
                           agent_title=agent.get("title", ""),
                           agent_id=agent.get("id", "")),
        encoding="utf-8")
    _surface(answer, agent, out_path)
    if not ns.no_open:
        try:
            webbrowser.open(out_path.as_uri())
        except Exception:
            pass  # 演示用，打不开就算了


def main(argv=None) -> int:
    ap = build_parser()
    ns = ap.parse_args(argv)
    api_key = (ns.api_key or os.environ.get("RAGFLOW_API_KEY", "")).strip()
    if not api_key:
        print("错误: 未提供 RAGFlow API key"
              "（--api-key 或设置环境变量 RAGFLOW_API_KEY）", file=sys.stderr)
        return 1
    try:
        import ragflow_config
        cfg = ragflow_config.load_ragflow_config(ns.config)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1
    client = AgentChatClient(cfg.base_url, api_key, timeout=ns.timeout)

    if ns.interactive:
        print("交互模式：输入问题回车（Ctrl+C 或空行退出），每轮独立无记忆")
        while True:
            try:
                question = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if not question:
                break
            try:
                run_one(client, ns, question)
            except RagflowError as exc:
                print(f"错误: {exc}", file=sys.stderr)
        return 0

    if not ns.question:
        ap.error("需要问题参数，或用 --interactive")
    try:
        run_one(client, ns, ns.question)
    except RagflowError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
