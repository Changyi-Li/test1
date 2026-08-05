"""agent_chat 模块单元测试（fake urlopen，遵循 test_ragflow_api 风格）。"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import agent_chat
from agent_chat import AgentChatClient, Chunk, RagflowError


class FakeResponse:
    def __init__(self, payload: object):
        self._raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self):
        return self._raw


def _fake_urlopen(monkeypatch, handler):
    calls = []

    def fake(req, timeout=None):
        calls.append(req)
        return handler(req, timeout)

    monkeypatch.setattr(agent_chat, "urlopen", fake)
    return calls


def _client():
    return AgentChatClient("http://localhost:80", "test-key")


# --------------------------------------------------------------------------- list_agents
def test_list_agents_parses_canvas(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": {"canvas": [
            {"id": "a1", "title": "Monitor ERP assistant"},
            {"id": "a2", "title": "other"}], "total": 2}}))
    agents = _client().list_agents()
    assert [a["id"] for a in agents] == ["a1", "a2"]
    assert calls[0].full_url == "http://localhost:80/api/v1/agents?page=0&page_size=100"
    assert calls[0].get_header("Authorization") == "Bearer test-key"


def test_list_agents_filters_by_title(monkeypatch):
    _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": {"canvas": [
            {"id": "a1", "title": "Monitor ERP assistant"},
            {"id": "a2", "title": "other"}], "total": 2}}))
    agents = _client().list_agents(title="Monitor")
    assert [a["id"] for a in agents] == ["a1"]


def test_list_agents_error_on_nonzero_code(monkeypatch):
    _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 100, "message": "page_size must be <= 100"}))
    with pytest.raises(RagflowError) as exc:
        _client().list_agents()
    assert "code=100" in str(exc.value)


def test_resolve_agent_by_id_and_error(monkeypatch):
    _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": {"canvas": [{"id": "a1", "title": "Monitor"}],
                             "total": 1}}))
    assert _client().resolve_agent(agent_id="a1")["id"] == "a1"
    with pytest.raises(RagflowError) as exc:
        _client().resolve_agent(agent_id="nope")
    assert "找不到 agent id" in str(exc.value)


def test_resolve_agent_title_filter(monkeypatch):
    _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": {"canvas": [
            {"id": "a1", "title": "Monitor ERP assistant"},
            {"id": "a2", "title": "other"}], "total": 2}}))
    assert _client().resolve_agent(title="Monitor")["id"] == "a1"
    with pytest.raises(RagflowError) as exc:
        _client().resolve_agent(title="不存在")
    assert "没有标题含" in str(exc.value)


# --------------------------------------------------------------------------- converse
def test_converse_parses_wrapped_reference(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse({
        "id": "sess-1", "model": "a1",
        "choices": [{"index": 0, "message": {
            "role": "assistant",
            "content": "创建组件见 [ID:94] 和 [ID:201]。",
            "reference": {"chunks": {
                "94": {"content_with_weight": "组件登记是最基础的寄存器。",
                       "docnm_kwd": "zh-cn_Stock_Register.md",
                       "similarity": 0.912},
                "201": {"content": "留空自动编号。",
                        "document_name": "zh-cn_Stock_Register.md",
                        "similarity": 0.590},
            }, "doc_aggs": {"zh-cn_Stock_Register.md": {"count": 2}}},
        }}]}))
    answer = _client().converse("a1", "怎么创建组件呢")
    assert answer.content == "创建组件见 [ID:94] 和 [ID:201]。"
    assert answer.session_id == "sess-1"
    assert answer.agent_id == "a1"
    assert answer.chunks["94"].content == "组件登记是最基础的寄存器。"
    assert answer.chunks["94"].doc_name == "zh-cn_Stock_Register.md"
    assert answer.chunks["94"].similarity == 0.912
    # doc_aggs（文件列表）不进入渲染数据
    assert set(answer.chunks) == {"94", "201"}
    body = json.loads(calls[0].data.decode("utf-8"))
    assert body["agent_id"] == "a1"
    assert body["openai-compatible"] is True
    assert body["messages"] == [{"role": "user", "content": "怎么创建组件呢"}]
    assert body["stream"] is False


def test_converse_accepts_direct_reference_shape(monkeypatch):
    _fake_urlopen(monkeypatch, lambda req, t: FakeResponse({
        "choices": [{"message": {
            "content": "答案 [ID:7]。",
            "reference": {"7": {"content": "chunk 内容", "docnm_kwd": "b.md"}},
        }}]}))
    answer = _client().converse("a1", "q")
    assert answer.chunks["7"].doc_name == "b.md"


def test_converse_passes_session_id(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"id": "sess-2", "choices": [{"message": {"content": "x", "reference": {}}}]}))
    answer = _client().converse("a1", "q", session_id="sess-1")
    body = json.loads(calls[0].data.decode("utf-8"))
    assert body["session_id"] == "sess-1"
    assert answer.session_id == "sess-2"


def test_converse_http_error_raises(monkeypatch):
    def boom(req, timeout=None):
        raise __import__("urllib.error", fromlist=["HTTPError"])
    # 用 monkeypatch 让 urlopen 直接抛 HTTPError 不方便造响应体，改测 URLError
    _fake_urlopen(monkeypatch, lambda req, t: (_ for _ in ()).throw(
        __import__("urllib.error", fromlist=["URLError"]).URLError("boom")))
    with pytest.raises(RagflowError) as exc:
        _client().converse("a1", "q")
    assert "网络错误" in str(exc.value)


# --------------------------------------------------------------------------- 解析与渲染
def test_parse_citations_dedups_by_index():
    # 按引用编号去重: [ID:12] 之后 [12] 同编号被去掉
    found = agent_chat.parse_citations("见 [ID:12]、[12]、[ID: 3] 和 [ID:12] 再次")
    assert found == [("[ID:12]", "12"), ("[ID: 3]", "3")]


def test_parse_citations_none():
    assert agent_chat.parse_citations("没有引用的普通回答。") == []


def test_build_payload_orders_chunks_by_int_key():
    chunks = {"201": Chunk("b"), "94": Chunk("a"), "7": Chunk("c")}
    payload = agent_chat.build_payload("正文 [ID:7]", chunks,
                                       question="q", agent_title="Monitor")
    assert list(payload["chunks"]) == ["7", "94", "201"]
    assert payload["chunks"]["7"]["content"] == "c"
    assert payload["question"] == "q"
    assert payload["agent"]["title"] == "Monitor"


def test_render_answer_page_embeds_data_and_no_file_list():
    chunks = {"94": Chunk("组件登记", doc_name="a.md", similarity=0.9),
              "201": Chunk("自动编号", doc_name="a.md")}
    html = agent_chat.render_answer_page("创建组件见 [ID:94]。", chunks,
                                         question="怎么创建组件呢")
    assert "__DATA__" not in html
    # 嵌入 JSON 正确、含正文与 chunks
    data_script = html.split('<script id="data"', 1)[1]
    inner = data_script.split(">", 1)[1].split("</script>", 1)[0]
    payload = json.loads(inner)
    assert payload["content"] == "创建组件见 [ID:94]。"
    assert set(payload["chunks"]) == {"94", "201"}
    # 不渲染文件列表：页面里没有 doc_aggs、也没有把文档名列表塞进正文区
    assert "doc_aggs" not in html
    # 渲染 JS 在：有引用替换逻辑
    assert "renderMarkdown" in html
    assert "data-idx=" in html
    # 默认变体是 inline
    assert "|| 'inline'" in html
