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
    let buf='', content='', chunks={}, started=false;
    const show = ()=>{ mdEl.textContent = stripThink(content); scrollBottom(); };
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
        if(d.start_to_think){ content += '<think>'; }
        if(d.content){ content += d.content; started=true; }
        if(d.end_to_think){ content += '</think>'; }
        if(d.reference && d.reference.chunks) chunks = d.reference.chunks;
        if(started) show();
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
  h.innerHTML='<div class="big">💬</div><div>问 Monitor ERP Assistant 点什么</div>';
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
