"""PROTOTYPE（throwaway）— RAGFlow agent 聊天机器人（本地网页）。

起一个本地 HTTP 服务，浏览器打开就能像聊天机器人一样自己提问
（类似 chat.deepseek.com）:

  RAGFLOW_API_KEY=xxx py scripts/agent_chat_server.py [--port 8000]
      [--agent-id <id>] [--agent-title Monitor]

页面特性:
- 底部输入框提问，Enter 发送；回答正文里的 [ID:N] 引用可点击
  （默认 inline 点击展开 chunk，可切 tooltip/popover）
- 多轮会话: 用 RAGFlow 常规模式（converse_session），追问带上下文
- 回答正文里的 <think>…</think> 推理块会被剥掉，不显示
- 右上「新对话」开新会话

设计: RAGFlow API key 只存服务端（env RAGFLOW_API_KEY 或 --api-key），
页面不接触 key；真实集成时把这个薄服务换成你的后端，页面侧用同样的渲染 JS。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from agent_chat import AgentChatClient, RagflowError, chunk_to_dict

PAGE = r"""<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Monitor ERP Assistant</title>
<style>
  :root{--blue:#0969da;--blue-h:#054da6;--bg:#f6f8fa;--line:#d0d7de;
        --ink:#1f2328;--sub:#656d76;--user:#d7e7ff;}
  *{box-sizing:border-box;}
  html,body{height:100%;}
  body{margin:0;font-family:system-ui,-apple-system,"Segoe UI","Microsoft YaHei",sans-serif;
       background:var(--bg);color:var(--ink);display:flex;flex-direction:column;}
  header{display:flex;align-items:center;justify-content:space-between;gap:12px;
         padding:10px 20px;background:#fff;border-bottom:1px solid var(--line);
         position:sticky;top:0;z-index:5;}
  .brand{display:flex;align-items:center;gap:10px;font-weight:600;font-size:15px;}
  .brand .dot{width:9px;height:9px;border-radius:50%;background:#3fb950;}
  .head-actions{display:flex;align-items:center;gap:10px;}
  #newChat{border:1px solid var(--line);background:#fff;border-radius:8px;padding:5px 12px;
           cursor:pointer;font-size:13px;color:var(--ink);}
  #newChat:hover{background:#f3f4f6;}
  main{flex:1;overflow-y:auto;padding:24px 16px;display:flex;flex-direction:column;}
  .thread{max-width:760px;width:100%;margin:0 auto;display:flex;flex-direction:column;gap:18px;flex:1;}
  .msg{display:flex;flex-direction:column;max-width:88%;}
  .msg.user{align-self:flex-end;align-items:flex-end;}
  .msg.bot{align-self:flex-start;}
  .bubble{padding:10px 14px;border-radius:12px;font-size:14.5px;line-height:1.7;
          overflow-wrap:break-word;}
  .msg.user .bubble{background:var(--user);border:1px solid #c3d9f5;
                    border-bottom-right-radius:3px;}
  .msg.bot .bubble{background:#fff;border:1px solid var(--line);
                   border-bottom-left-radius:3px;width:100%;}
  .md h1,.md h2,.md h3{margin:8px 0 6px;line-height:1.3;}
  .md h2{font-size:17px;border-bottom:1px solid #eaeef2;padding-bottom:3px;}
  .md p{margin:7px 0;}
  .md ul,.md ol{margin:6px 0;padding-left:22px;}
  .md li{margin:2px 0;}
  .md pre{background:#f6f8fa;border:1px solid var(--line);border-radius:6px;padding:10px;
          overflow:auto;font-size:13px;margin:8px 0;}
  .md code{background:#f6f8fa;border-radius:4px;padding:1px 4px;font-size:13px;}
  .md pre code{background:none;padding:0;}
  .md blockquote{border-left:4px solid var(--line);color:#57606a;margin:8px 0;
                 padding:2px 12px;}
  .md table{border-collapse:collapse;}
  .md th,.md td{border:1px solid var(--line);padding:5px 9px;}
  .md img{max-width:100%;}
  /* 引用 */
  .cite{display:inline-block;min-width:1.1em;text-align:center;margin:0 1px;
        font-size:10.5px;line-height:1.4;color:#fff;background:var(--blue);
        border-radius:3px;padding:0 3px;cursor:pointer;vertical-align:super;
        font-style:normal;font-weight:600;user-select:none;}
  .cite:hover{background:var(--blue-h);}
  .cite-missing{background:#cf222e;}
  .cite-card{position:fixed;z-index:30;max-width:380px;max-height:300px;overflow:auto;
             background:#fff;border:1px solid var(--line);border-radius:8px;
             box-shadow:0 6px 24px rgba(31,35,40,.18);padding:10px 12px;font-size:13px;
             line-height:1.6;}
  .cite-card .h{font-weight:600;color:var(--blue);margin-bottom:6px;font-size:12px;
                border-bottom:1px solid #eaeef2;padding-bottom:5px;display:flex;
                justify-content:space-between;gap:10px;}
  .cite-card .c{white-space:pre-wrap;word-break:break-word;}
  .cite-card .u{color:var(--blue);text-decoration:none;font-size:12px;}
  .chunk-expand{margin:9px 0 9px 24px;border-left:3px solid var(--blue);
                background:#f3f8ff;border-radius:0 8px 8px 0;padding:9px 13px;
                font-size:13px;line-height:1.6;}
  .chunk-expand .h{font-weight:600;color:var(--blue);margin-bottom:5px;}
  .chunk-expand .c{white-space:pre-wrap;word-break:break-word;}
  /* 输入区 */
  footer{background:#fff;border-top:1px solid var(--line);padding:12px 16px 16px;
         position:sticky;bottom:0;}
  .input-box{max-width:760px;margin:0 auto;display:flex;gap:10px;align-items:flex-end;
             border:1px solid var(--line);border-radius:12px;background:#fff;
             padding:8px 8px 8px 14px;box-shadow:0 2px 8px rgba(31,35,40,.05);}
  textarea{flex:1;border:0;outline:0;resize:none;font-size:14.5px;line-height:1.6;
           font-family:inherit;max-height:160px;padding:6px 0;}
  #send{border:0;background:var(--blue);color:#fff;border-radius:9px;padding:9px 18px;
        cursor:pointer;font-size:14px;font-weight:600;}
  #send:disabled{background:#9bc1e8;cursor:not-allowed;}
  .typing{color:var(--sub);font-size:13px;padding:6px 2px;display:flex;gap:3px;}
  .typing .t{animation:blink 1.2s infinite;}
  .typing .t:nth-child(2){animation-delay:.2s;}
  .typing .t:nth-child(3){animation-delay:.4s;}
  @keyframes blink{0%,80%,100%{opacity:.2;}40%{opacity:1;}}
  .hint{margin:auto;text-align:center;color:var(--sub);font-size:13px;}
  .hint .big{font-size:26px;color:var(--ink);margin-bottom:10px;}
  .hint .big img{width:56px;height:56px;object-fit:contain;border-radius:10px;}
  /* 思考过程：默认收起，点击展开 */
  .think{margin:6px 0 10px;font-size:13px;}
  .think summary{cursor:pointer;color:var(--sub);user-select:none;padding:3px 2px;
                 list-style:none;display:inline-flex;align-items:center;gap:4px;}
  .think summary::before{content:'▸';font-size:11px;color:var(--sub);}
  .think[open] summary::before{content:'▾';}
  .think summary:hover{color:var(--blue);}
  .think-body{margin:6px 0 2px;padding:9px 12px;background:#f6f8fa;
              border:1px solid #eaeef2;border-radius:6px;color:#57606a;
              white-space:pre-wrap;word-break:break-word;font-size:12.5px;line-height:1.7;}
  .err{color:#cf222e;font-size:13px;margin-top:6px;}
</style>
</head>
<body>
<header>
  <div class="brand"><span class="dot"></span>__AGENT_TITLE__</div>
  <div class="head-actions">
    <button id="newChat">＋ 新对话</button>
  </div>
</header>
<main id="main"><div class="thread" id="thread"></div></main>
<footer>
  <div class="input-box">
    <textarea id="input" rows="1" placeholder="问点什么…（Enter 发送，Shift+Enter 换行）"></textarea>
    <button id="send">发送</button>
  </div>
</footer>
<script>
const AGENT_ID = '__AGENT_ID__';
let sessionId = null;

// ---- 最小 markdown + 引用渲染 ----
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function stripThink(c){ return c.replace(/<think>[\s\S]*?<\/think>/g, ''); }
function splitThink(content){
  // 把 <think>…</think> 块抽出来给折叠区，剩下的才是回答正文
  const thinking = [];
  const answer = content.replace(/<think>([\s\S]*?)<\/think>/g, (m, body)=>{ thinking.push(body); return ''; });
  return { thinking: thinking.join('\n\n'), answer };
}
function normalizeChunks(raw){
  // RAGFlow 原始 chunk 字段是 docnm_kwd/content_with_weight，归一到渲染用的字段
  const out = {};
  if(!raw) return out;
  for(const [cid, c] of Object.entries(raw)){
    if(!c || typeof c !== 'object') continue;
    out[cid] = {
      content: c.content_with_weight || c.content || '',
      doc_name: c.docnm_kwd || c.document_name || '',
      url: c.url || '',
      similarity: c.similarity,
    };
  }
  return out;
}
const CITE_RE = /\[(?:ID\s*:\s*)?(\d+)\]/g;
function inline(md){
  let s = esc(md);
  s = s.replace(/`([^`]+)`/g,(m,c)=>'<code>'+c+'</code>');
  s = s.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
  s = s.replace(/\*([^*]+)\*/g,'<em>$1</em>');
  s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2" target="_blank">$1</a>');
  return s;
}
function citeSup(n, chunks){
  const hit = chunks && chunks[n];
  return '<sup class="cite'+(hit?'':' cite-missing')+'" data-idx="'+esc(n)+'">'+esc(n)+'</sup>';
}
function renderMarkdown(md, chunks){
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
  return out.join('\n').replace(/\x01(\d+)\x02/g,(m,n)=>citeSup(n, chunks));
}

// ---- 引用交互（每轮回答的 chunks 独立）----
function chunkBody(idx, chunks){
  const c = chunks && chunks[idx];
  if(!c) return '<div class="h">引用 '+idx+' <span style="color:#cf222e">未匹配到 reference</span></div><div class="c">(reference 里没有这个编号)</div>';
  const name = c.doc_name ? esc(c.doc_name) : '(无文档名)';
  const url = c.url ? ' <a class="u" href="'+esc(c.url)+'" target="_blank">源页面 ↗</a>' : '';
  return '<div class="h">'+name+' <span>#'+esc(idx)+(c.similarity!=null?' · '+Number(c.similarity).toFixed(3):'')+'</span></div>'+
         '<div class="c">'+esc(c.content)+'</div>'+url;
}
function clearInline(){ document.querySelectorAll('.chunk-expand').forEach(e=>e.remove()); }
function toggleInline(el,chunks,idx){
  const block = el.closest('p,li,h2,h3,h4,h5,h6,blockquote,pre,td') || el;
  const old = block.nextElementSibling;
  if(old && old.classList && old.classList.contains('chunk-expand')){ old.remove(); return; }
  clearInline();
  const box=document.createElement('div'); box.className='chunk-expand';
  box.innerHTML=chunkBody(idx,chunks);
  block.insertAdjacentElement('afterend',box);
}
function bindCitations(container, chunks){
  container._chunks = chunks;
  container.querySelectorAll('.cite').forEach(el=>{
    const idx = el.dataset.idx;
    el.addEventListener('click', ev=>{ ev.stopPropagation(); toggleInline(el, chunks, idx); });
  });
}

// ---- 消息流 ----
const thread = document.getElementById('thread');
const input = document.getElementById('input');
const sendBtn = document.getElementById('send');
function scrollBottom(){ main.scrollTop = main.scrollHeight; }
function addUser(q){
  thread.querySelectorAll('.hint').forEach(el=>el.remove());
  const m=document.createElement('div'); m.className='msg user';
  m.innerHTML='<div class="bubble">'+esc(q)+'</div>'; thread.appendChild(m); scrollBottom();
}
function makeBubble(){
  const m=document.createElement('div'); m.className='msg bot';
  m.innerHTML='<div class="bubble"><div class="md"><span class="typing"><span class="t">●</span><span class="t">●</span><span class="t">●</span></span></div></div>';
  thread.appendChild(m); scrollBottom(); return m;
}
async function send(){
  const q = input.value.trim();
  if(!q || sendBtn.disabled) return;
  input.value=''; autoGrow();
  addUser(q);
  const bubble = makeBubble();
  const mdEl = bubble.querySelector('.md');
  sendBtn.disabled=true;
  try{
    const resp = await fetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({question:q, session_id:sessionId, stream:true})});
    if(!resp.ok || !resp.body){
      const data = await resp.json().catch(()=>({}));
      throw new Error(data.error || ('HTTP '+resp.status));
    }
    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    // 两个区域: 思考折叠块(默认收起，点击可看实时思考) + 回答实时区(带打字指示)
    const zone = document.createElement('div'); zone.className='answer-zone';
    zone.innerHTML='<span class="typing"><span class="t">●</span><span class="t">●</span><span class="t">●</span></span>';
    mdEl.appendChild(zone);
    let thinkEl=null, typingShown=true;
    const ensureThink = ()=>{
      if(!thinkEl){
        thinkEl=document.createElement('details'); thinkEl.className='think';
        thinkEl.innerHTML='<summary>💭 思考过程</summary><div class="think-body"></div>';
        mdEl.insertBefore(thinkEl, zone);
      }
      return thinkEl;
    };
    const showAnswer = (txt)=>{
      if(typingShown){ typingShown=false; zone.innerHTML=''; }
      zone.textContent = txt;
      scrollBottom();
    };
    let buf='', content='', answerLive='', chunks={}, inThinking=false;
    while(true){
      const {done, value} = await reader.read();
      if(done) break;
      buf += decoder.decode(value, {stream:true});
      let nl;
      while((nl=buf.indexOf('\n'))>=0){
        const line=buf.slice(0,nl).trim(); buf=buf.slice(nl+1);
        if(!line.startsWith('data:')) continue;
        const payload=line.slice(5).trim();
        if(payload==='[DONE]') continue;
        let ev; try{ ev=JSON.parse(payload); }catch{ continue; }
        if(ev.error) throw new Error(ev.error);
        if(ev.session_id) sessionId=ev.session_id;
        const d=ev.data||{};
        if(d.start_to_think){ inThinking=true; content+='<think>'; ensureThink(); }
        if(d.end_to_think){ inThinking=false; content+='</think>'; }
        if(d.content){
          content += d.content;
          if(inThinking){
            const tb = thinkEl ? thinkEl.querySelector('.think-body') : null;
            if(tb) tb.textContent += d.content;  // 思考折叠块里实时更新
          } else {
            answerLive += d.content;
            showAnswer(answerLive);
          }
        }
        if(d.reference && d.reference.chunks) chunks = normalizeChunks(d.reference.chunks);
      }
    }
    const { thinking, answer } = splitThink(content);
    let html = '';
    if(thinking.trim()) html += '<details class="think"><summary>💭 思考过程</summary><div class="think-body">'+esc(thinking.trim())+'</div></details>';
    html += renderMarkdown(answer, chunks);
    mdEl.innerHTML = html;
    bindCitations(bubble, chunks);
    scrollBottom();
  }catch(e){
    mdEl.parentElement.innerHTML='<div class="bubble err">⚠ '+esc(e.message||String(e))+'</div>';
    scrollBottom();
  }finally{ sendBtn.disabled=false; }
}
function autoGrow(){ input.style.height='auto'; input.style.height=Math.min(input.scrollHeight,160)+'px'; }
input.addEventListener('input',autoGrow);
input.addEventListener('keydown',e=>{ if(e.key==='Enter' && !e.shiftKey){ e.preventDefault(); send(); } });
sendBtn.addEventListener('click',send);

document.getElementById('newChat').addEventListener('click',()=>{
  sessionId=null; thread.innerHTML=''; input.focus();
  document.querySelectorAll('.chunk-expand').forEach(e=>e.remove());
  showHint();
});
function showHint(){
  const h=document.createElement('div'); h.className='hint';
  h.innerHTML='<div class="big"><img src="data:image/png;base64,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" alt=""></div><div>你好，我是 Monitor ERP 助手，有什么可以帮您？</div>';
  thread.appendChild(h);
}
showHint();
input.focus();
</script>
</body>
</html>
"""


class _Handler(BaseHTTPRequestHandler):
    server: "ChatServer"

    def log_message(self, fmt, *args):  # 安静点
        sys.stderr.write("%s\n" % (fmt % args))

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send_html(self.server.page)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path != "/api/chat":
            self._send_json({"error": "not found"}, 404)
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            question = (body.get("question") or "").strip()
            if not question:
                self._send_json({"error": "question 不能为空"}, 400)
                return
            if body.get("stream", False):
                self._proxy_stream(question, body.get("session_id"))
                return
            answer = self.server.client.converse_session(
                self.server.agent_id, question, body.get("session_id"))
            payload = {
                "answer": answer.content,
                "chunks": {cid: chunk_to_dict(c) for cid, c in answer.chunks.items()},
                "session_id": answer.session_id,
            }
            self._send_json(payload, 200)
        except RagflowError as exc:
            self._send_json({"error": str(exc)}, 502)
        except Exception as exc:
            self._send_json({"error": str(exc)}, 500)

    def _proxy_stream(self, question: str, session_id: str | None) -> None:
        """把 RAGFlow 的 SSE 转发给浏览器（边算边发，客户端断开就停）。

        必须关连接（close_connection=True）让响应有明确结束，否则浏览器 fetch
        的 reader.read() 永远等不到 done（keep-alive + 无 Content-Length 时
        响应体到连接关闭才算完）。
        """
        self.close_connection = True
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.flush()
        try:
            for ev in self.server.client.converse_stream(
                    self.server.agent_id, question, session_id):
                line = ("data: " + json.dumps(ev, ensure_ascii=False)
                        + "\n\n").encode("utf-8")
                try:
                    self.wfile.write(line)
                    self.wfile.flush()
                except (ConnectionAbortedError, BrokenPipeError):
                    return  # 浏览器断开（比如中途关页），停止转发
        except RagflowError as exc:
            try:
                self.wfile.write(("data: " + json.dumps(
                    {"error": str(exc)}, ensure_ascii=False) + "\n\n").encode("utf-8"))
                self.wfile.flush()
            except (ConnectionAbortedError, BrokenPipeError):
                pass
            return
        try:
            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()
        except (ConnectionAbortedError, BrokenPipeError):
            pass

    def _send_html(self, html: str):
        data = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, obj: dict, code: int):
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


class ChatServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, addr, page: str, client: AgentChatClient, agent_id: str):
        self.page = page
        self.client = client
        self.agent_id = agent_id
        super().__init__(addr, _Handler)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="agent_chat_server.py",
        description="PROTOTYPE — RAGFlow agent 聊天机器人（本地网页，可自己提问）")
    ap.add_argument("--port", type=int, default=8000, help="监听端口（默认 8000）")
    ap.add_argument("--host", default="127.0.0.1", help="监听地址（默认 127.0.0.1）")
    ap.add_argument("--api-key", metavar="KEY",
                    help="RAGFlow API key（默认读 RAGFLOW_API_KEY）")
    ap.add_argument("--config", metavar="PATH",
                    help="覆盖配置路径（默认 config/ragflow.json，取 base_url）")
    ap.add_argument("--agent-id", metavar="ID", help="指定 agent id")
    ap.add_argument("--agent-title", metavar="TITLE", default="Monitor",
                    help="按标题子串选 agent（默认 Monitor）")
    return ap


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
    try:
        client = AgentChatClient(cfg.base_url, api_key)
        agent = client.resolve_agent(ns.agent_id, ns.agent_title)
    except RagflowError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    page = PAGE.replace("__AGENT_TITLE__", agent.get("title", "Agent")) \
               .replace("__AGENT_ID__", agent.get("id", ""))
    server = ChatServer((ns.host, ns.port), page, client, agent["id"])
    print(f"== Agent: {agent.get('title')} ({agent.get('id')}) ==")
    print(f"打开 http://{ns.host}:{ns.port} 提问（Ctrl+C 退出）")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n退出")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
