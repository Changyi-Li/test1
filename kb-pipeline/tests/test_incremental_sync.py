"""增量同步引擎单元测试（票 #17，AC1–AC5）。"""
from __future__ import annotations

import json
import sys
import urllib.error
from datetime import datetime
from email.utils import format_datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import pipeline as P
import sync_config
import sync_engine
import sync_state


URL_A = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
         "UserGuide/GettingStarted/GettingStarted.htm")
URL_B = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
         "UserGuide/GettingStarted/MobileClient.htm")
URL_C = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
         "UserGuide/GettingStarted/MonitorBI.htm")

def _http_date(iso: str) -> str:
    """测试侧把 ISO lastmod 转成 If-Modified-Since 使用的 IMF-fixdate。"""
    return format_datetime(datetime.fromisoformat(iso.replace("Z", "+00:00")),
                           usegmt=True)


FIXTURE_HTML = """<html><head><title>Topic</title></head>
<body><div id="contentBody"><h1>Topic</h1>
<p>Welcome to Monitor ERP G5.</p>
<h2>Overview</h2><p>First part.</p>
<h2>Next steps</h2><p>Second part.</p>
</div></body></html>"""


class FakeResponse:
    status = 200

    def __init__(self, body: bytes = b"",
                 lastmod: str = "2026-05-21T08:18:54Z",
                 etag: str = '"test-etag"'):
        self._body = body
        self.headers = {"Last-Modified": lastmod, "ETag": etag}

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def geturl(self):
        return "https://help.monitorerp.cn/final"

    def read(self):
        return self._body


class FakeNetwork:
    """按 URL 提供当前服务器指纹；条件请求命中则 304。

    fingerprints: {url: (etag, lastmod)}。interrupt_after 用于模拟中断：
    第 N 个请求后抛 KeyboardInterrupt。
    """

    def __init__(self, fingerprints: dict[str, tuple[str, str]],
                 bodies: dict[str, str] | None = None,
                 interrupt_after: int | None = None,
                 fail_status: int = 404):
        self.fingerprints = fingerprints
        self.bodies = bodies or {url: FIXTURE_HTML for url in fingerprints}
        self.interrupt_after = interrupt_after
        self.fail_status = fail_status
        self.calls: dict[str, list[str]] = {"head": [], "get": []}
        self.requests: list[tuple[str, str, dict]] = []
        self._count = 0

    def _maybe_interrupt(self):
        self._count += 1
        if self.interrupt_after is not None and self._count > self.interrupt_after:
            raise KeyboardInterrupt

    def head(self, url, headers, timeout=30):
        self.calls["head"].append(url)
        self.requests.append(("HEAD", url, dict(headers)))
        self._maybe_interrupt()
        if url not in self.fingerprints:
            raise urllib.error.HTTPError(url, self.fail_status, "Not Found", {}, None)
        etag, lastmod = self.fingerprints[url]
        if headers.get("If-None-Match") == etag:
            raise urllib.error.HTTPError(url, 304, "Not Modified", {}, None)
        if lastmod and headers.get("If-Modified-Since") == _http_date(lastmod):
            raise urllib.error.HTTPError(url, 304, "Not Modified", {}, None)
        return FakeResponse(etag=etag, lastmod=lastmod)

    def get(self, url, headers, timeout=30):
        self.calls["get"].append(url)
        self.requests.append(("GET", url, dict(headers)))
        self._maybe_interrupt()
        if url not in self.fingerprints:
            raise urllib.error.HTTPError(url, self.fail_status, "Not Found", {}, None)
        etag, lastmod = self.fingerprints[url]
        return FakeResponse(self.bodies[url].encode("utf-8"),
                            etag=etag, lastmod=lastmod)


@pytest.fixture
def engine_root(tmp_path, monkeypatch):
    monkeypatch.setattr(sync_engine, "ROOT", tmp_path)
    return tmp_path


@pytest.fixture
def cfg():
    return sync_config.load_sync_config()


def _jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in
            path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _seed_state(root: Path, records: list[dict]) -> sync_state.SyncState:
    st = sync_state.SyncState(root / "state" / "sync-state.jsonl")
    st.load()
    for fields in records:
        st.record(**fields)
    return st


def test_incremental_unchanged_304_rewrites_nothing(engine_root, cfg,
                                                    monkeypatch, capsys):
    """AC1：状态指纹与服务器一致 → 条件 HEAD 返回 304，产物与状态原样保持。"""
    etag = '"en-v1"'
    lastmod = "2026-05-21T08:18:54Z"
    net = FakeNetwork({URL_A: (etag, lastmod)})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    _seed_state(engine_root, [{
        "url": URL_A, "language": "en-us", "etag": etag, "lastmod": lastmod,
        "content_hash": "0" * 64, "status": "ok",
        "last_ok_at": "2026-08-02T00:00:00Z",
    }])
    clean_file = engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")
    clean_file.parent.mkdir(parents=True, exist_ok=True)
    clean_file.write_text("# Topic\n\nWelcome.\n", encoding="utf-8")
    meta_path = engine_root / "data" / "metadata.jsonl"
    meta_path.write_text(
        json.dumps({
            "id": "en-us/UserGuide/GettingStarted/GettingStarted",
            "title": "Topic", "url": URL_A, "source": "help.monitorerp.cn",
            "version": "25.8", "language": "en-us",
            "topic_path": "UserGuide/GettingStarted", "quality": "canonical",
            "lastmod": lastmod, "etag": etag, "content_hash": "0" * 64,
            "images": [], "paired_topic_id": None,
        }, ensure_ascii=False) + "\n", encoding="utf-8")
    state_path = engine_root / "state" / "sync-state.jsonl"
    before = {
        "clean": clean_file.read_bytes(),
        "meta": meta_path.read_bytes(),
        "state": state_path.read_bytes(),
    }

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert net.calls["get"] == []
    assert net.requests[0][0] == "HEAD"
    assert net.requests[0][2]["If-None-Match"] == etag
    assert clean_file.read_bytes() == before["clean"]
    assert meta_path.read_bytes() == before["meta"]
    assert state_path.read_bytes() == before["state"]
    assert not (engine_root / "data" / "raw" / "headers.json").exists()
    assert URL_A in capsys.readouterr().out


def test_incremental_changed_page_updates_artifacts_and_hash(
        engine_root, cfg, monkeypatch):
    """AC2：变化页条件 HEAD 200 → 只对该主题 GET，产物与 content_hash 更新一致。"""
    net = FakeNetwork({URL_A: ('"en-v2"', "2026-06-01T00:00:00Z")})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [{
        "url": URL_A, "language": "en-us", "etag": '"en-v1"',
        "lastmod": "2026-05-21T08:18:54Z", "content_hash": "0" * 64,
        "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z",
    }])

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert net.calls["get"] == [URL_A]
    assert net.requests[0][2]["If-None-Match"] == '"en-v1"'
    clean_file = engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")
    md = clean_file.read_text(encoding="utf-8")
    assert "Welcome to Monitor ERP G5." in md
    meta = _jsonl(engine_root / "data" / "metadata.jsonl")
    assert len(meta) == 1
    assert meta[0]["content_hash"] == P.sha256_hex(md)
    assert meta[0]["etag"] == '"en-v2"'
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    assert len(state) == 1
    assert state[0]["status"] == "ok"
    assert state[0]["etag"] == '"en-v2"'
    assert state[0]["lastmod"] == "2026-06-01T00:00:00Z"
    assert state[0]["content_hash"] == meta[0]["content_hash"]


def test_incremental_get_only_changed_topics(engine_root, cfg, monkeypatch):
    """AC2：混合清单中只对变化主题发起 GET，未变化主题产物保持。"""
    etag_a = '"a-v1"'
    etag_b = '"b-v1"'
    net = FakeNetwork({
        URL_A: (etag_a, "2026-05-21T08:18:54Z"),
        URL_B: ('"b-v2"', "2026-06-02T00:00:00Z"),
    })
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [
        {"url": URL_A, "language": "en-us", "etag": etag_a,
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "a" * 64,
         "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z"},
        {"url": URL_B, "language": "en-us", "etag": etag_b,
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "b" * 64,
         "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z"},
    ])
    clean_a = engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")
    clean_a.parent.mkdir(parents=True, exist_ok=True)
    clean_a.write_text("# Topic A\n\nKeep me.\n", encoding="utf-8")
    before_a = clean_a.read_bytes()
    meta_path = engine_root / "data" / "metadata.jsonl"
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_a = {
        "id": "en-us/UserGuide/GettingStarted/GettingStarted",
        "title": "Topic A", "url": URL_A, "source": "help.monitorerp.cn",
        "version": "25.8", "language": "en-us",
        "topic_path": "UserGuide/GettingStarted", "quality": "canonical",
        "lastmod": "2026-05-21T08:18:54Z", "etag": etag_a,
        "content_hash": "a" * 64, "images": [], "paired_topic_id": None,
    }
    meta_path.write_text(json.dumps(meta_a, ensure_ascii=False) + "\n",
                         encoding="utf-8")

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert net.calls["get"] == [URL_B]
    assert clean_a.read_bytes() == before_a
    clean_b = engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_MobileClient.md")
    assert clean_b.exists()
    meta = _jsonl(meta_path)
    assert {r["id"] for r in meta} == {
        "en-us/UserGuide/GettingStarted/GettingStarted",
        "en-us/UserGuide/GettingStarted/MobileClient",
    }
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    by_url = {r["url"]: r for r in state}
    assert by_url[URL_A]["etag"] == etag_a
    assert by_url[URL_B]["etag"] == '"b-v2"'
    assert by_url[URL_B]["content_hash"] == P.sha256_hex(
        clean_b.read_text(encoding="utf-8"))


def test_incremental_interrupt_then_resume_skips_completed_items(
        engine_root, cfg, monkeypatch):
    """AC3：每条结果即时落盘；模拟中断后续跑不重复抓取已完成项。"""
    net = FakeNetwork({
        URL_A: ('"a-v2"', "2026-06-01T00:00:00Z"),
        URL_B: ('"b-v2"', "2026-06-02T00:00:00Z"),
        URL_C: ('"c-v2"', "2026-06-03T00:00:00Z"),
    }, interrupt_after=2)
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [
        {"url": URL_A, "language": "en-us", "etag": '"a-v1"',
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "a" * 64,
         "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z"},
        {"url": URL_B, "language": "en-us", "etag": '"b-v1"',
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "b" * 64,
         "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z"},
        {"url": URL_C, "language": "en-us", "etag": '"c-v1"',
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "c" * 64,
         "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z"},
    ])

    with pytest.raises(KeyboardInterrupt):
        sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    # 已完成的 A 即时落盘：状态 ok、指纹更新、产物存在
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    a_row = next(r for r in state if r["url"] == URL_A)
    assert a_row["status"] == "ok"
    assert a_row["etag"] == '"a-v2"'
    assert (engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")).exists()
    gets_after_first_run = len(net.calls["get"])
    assert gets_after_first_run == 1

    # 续跑：A 只发条件 HEAD（304），不重复 GET；B/C 补抓完成
    net.interrupt_after = None
    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    resumed_gets = net.calls["get"][gets_after_first_run:]
    assert resumed_gets == [URL_B, URL_C]
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    by_url = {r["url"]: r for r in state}
    assert all(by_url[u]["status"] == "ok" for u in (URL_A, URL_B, URL_C))
    assert by_url[URL_B]["etag"] == '"b-v2"'
    assert by_url[URL_C]["etag"] == '"c-v2"'
    assert (engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_MobileClient.md")).exists()
    assert (engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_MonitorBI.md")).exists()


def test_incremental_http_500_marks_state_error_and_stops_round(
        engine_root, cfg, monkeypatch, capsys):
    """票 #19：5xx 指数退避重试后仍失败 → 记 error，单轮错误率 100% → 停止、
    非零退出、写错误报告（失败 URL + 原因），不写产物、不发 GET。"""
    net = FakeNetwork({}, fail_status=500)
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    monkeypatch.setattr(sync_engine.time, "sleep", lambda s: None)
    _seed_state(engine_root, [{
        "url": URL_A, "language": "en-us", "etag": '"a-v1"',
        "lastmod": "2026-05-21T08:18:54Z", "content_hash": "a" * 64,
        "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z",
    }])

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 1
    assert net.calls["get"] == []
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    assert state[0]["status"] == "error"
    assert state[0]["etag"] == '"a-v1"'   # 保留最后已知指纹
    assert not (engine_root / "data" / "metadata.jsonl").exists()
    err = capsys.readouterr().err
    assert "500" in err
    assert "100.0% > 10.0%" in err
    report = _jsonl(engine_root / "state" / "sync-error-report.jsonl")
    assert any(r["type"] == "failure" and r["url"] == URL_A
               and "HTTP 500" in r["reason"] for r in report)
    assert any(r["type"] == "summary" and r["failed"] == 1 for r in report)


def test_incremental_dry_run_only_lists_would_fetch_urls(
        engine_root, cfg, monkeypatch, capsys):
    """AC4：--dry-run 只输出将抓取的 URL 清单，不写任何产物、不发 GET。"""
    etag_a = '"a-v1"'
    net = FakeNetwork({
        URL_A: (etag_a, "2026-05-21T08:18:54Z"),
        URL_B: ('"b-v2"', "2026-06-02T00:00:00Z"),
    })
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [
        {"url": URL_A, "language": "en-us", "etag": etag_a,
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "a" * 64,
         "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z"},
        {"url": URL_B, "language": "en-us", "etag": '"b-v1"',
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "b" * 64,
         "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z"},
    ])
    state_path = engine_root / "state" / "sync-state.jsonl"
    before_state = state_path.read_bytes()

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0,
                                        dry_run=True)

    assert code == 0
    assert net.calls["get"] == []
    out = capsys.readouterr().out
    fetch_lines = [ln for ln in out.splitlines() if ln.startswith("== 将抓取:")]
    assert fetch_lines == [f"== 将抓取: {URL_B}"]
    # 不写任何产物：状态、元数据、清洗产物、原始 HTML 与响应头均不落盘
    assert state_path.read_bytes() == before_state
    assert not (engine_root / "data" / "metadata.jsonl").exists()
    assert not (engine_root / "data" / "chunks.jsonl").exists()
    assert not (engine_root / "data" / "clean").exists()
    assert not (engine_root / "data" / "raw").exists()


def test_incremental_rerun_is_idempotent(engine_root, cfg, monkeypatch):
    """AC5：同一输入两次运行产物一致，第二次不再 GET。"""
    net = FakeNetwork({URL_A: ('"a-v1"', "2026-05-21T08:18:54Z")})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [{
        "url": URL_A, "language": "en-us", "etag": '"a-v0"',
        "lastmod": "2026-05-20T00:00:00Z", "content_hash": "0" * 64,
        "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z",
    }])

    assert sync_engine.incremental_sync(None, None, cfg, rate=2.0) == 0
    first = {
        "clean": (engine_root / "data" / "clean" / (
            "en-us_UserGuide_GettingStarted_GettingStarted.md")).read_bytes(),
        "meta": (engine_root / "data" / "metadata.jsonl").read_bytes(),
        "chunks": (engine_root / "data" / "chunks.jsonl").read_bytes(),
        "state": (engine_root / "state" / "sync-state.jsonl").read_bytes(),
    }
    gets_after_first = len(net.calls["get"])

    assert sync_engine.incremental_sync(None, None, cfg, rate=2.0) == 0

    assert (engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")).read_bytes() == first["clean"]
    assert (engine_root / "data" / "metadata.jsonl").read_bytes() == first["meta"]
    assert (engine_root / "data" / "chunks.jsonl").read_bytes() == first["chunks"]
    assert (engine_root / "state" / "sync-state.jsonl").read_bytes() == first["state"]
    assert net.calls["get"][gets_after_first:] == []


def test_incremental_empty_state_is_noop(engine_root, cfg, capsys):
    """新环境无状态文件 → 增量同步无事可做，提示先跑全量对账。"""
    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)
    assert code == 0
    assert "状态为空" in capsys.readouterr().out


def test_incremental_lastmod_fallback_304(engine_root, cfg, monkeypatch):
    """无 ETag 时用 Last-Modified 兜底：If-Modified-Since 以 IMF-fixdate 发送。"""
    lastmod = "2026-05-21T08:18:54Z"
    net = FakeNetwork({URL_A: (None, lastmod)})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [{
        "url": URL_A, "language": "en-us", "etag": None, "lastmod": lastmod,
        "content_hash": "0" * 64, "status": "ok",
        "last_ok_at": "2026-08-02T00:00:00Z",
    }])
    state_path = engine_root / "state" / "sync-state.jsonl"
    before_state = state_path.read_bytes()

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert net.calls["get"] == []
    assert net.requests[0][2]["If-Modified-Since"] == (
        "Thu, 21 May 2026 08:18:54 GMT")
    assert state_path.read_bytes() == before_state


def test_incremental_skips_deleted_tombstones(engine_root, cfg, monkeypatch):
    """墓碑不重探：deleted 记录不进入条件请求，墓碑状态保持。"""
    etag_a = '"a-v1"'
    etag_b = '"b-v1"'
    deleted_at = "2026-08-01T12:00:00Z"
    net = FakeNetwork({URL_A: (etag_a, "2026-05-21T08:18:54Z")})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [
        {"url": URL_A, "language": "en-us", "etag": etag_a,
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "a" * 64,
         "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z"},
        {"url": URL_B, "language": "en-us", "etag": etag_b,
         "lastmod": "2026-05-21T08:18:54Z", "content_hash": "b" * 64,
         "status": "deleted", "last_ok_at": "2026-07-01T00:00:00Z",
         "deleted_at": deleted_at},
    ])
    state_path = engine_root / "state" / "sync-state.jsonl"
    before_state = state_path.read_bytes()

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert URL_B not in net.calls["head"]
    assert URL_B not in net.calls["get"]
    state = _jsonl(state_path)
    b_row = next(r for r in state if r["url"] == URL_B)
    assert b_row["status"] == "deleted"
    assert b_row["deleted_at"] == deleted_at
    assert state_path.read_bytes() == before_state


def test_incremental_invalid_url_is_clean_error(engine_root, cfg, monkeypatch,
                                                capsys):
    """非法主题 URL → 干净错误与非零退出，不写状态、不发请求。"""
    net = FakeNetwork({})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)

    code = sync_engine.incremental_sync(
        None, "https://example.com/not-a-topic", cfg, rate=2.0)

    assert code == 1
    assert net.requests == []
    assert not (engine_root / "state" / "sync-state.jsonl").exists()
    assert "错误" in capsys.readouterr().err


def test_incremental_404_tombstones_and_removes_artifacts(engine_root, cfg,
                                                          monkeypatch, capsys):
    """AC(#18)：曾 ok 的页面 404 → 状态墓碑 + deleted 例外，数据集旧产物清除。"""
    net = FakeNetwork({})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [{
        "url": URL_A, "language": "en-us", "etag": '"a-v1"',
        "lastmod": "2026-05-21T08:18:54Z", "content_hash": "a" * 64,
        "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z",
    }])
    clean_file = engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")
    clean_file.parent.mkdir(parents=True, exist_ok=True)
    clean_file.write_text("# Topic\n\nWelcome.\n", encoding="utf-8")
    meta_path = engine_root / "data" / "metadata.jsonl"
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps({
        "id": "en-us/UserGuide/GettingStarted/GettingStarted",
        "title": "Topic", "url": URL_A, "source": "help.monitorerp.cn",
        "version": "25.8", "language": "en-us",
        "topic_path": "UserGuide/GettingStarted", "quality": "canonical",
        "lastmod": "2026-05-21T08:18:54Z", "etag": '"a-v1"',
        "content_hash": "a" * 64, "images": [], "paired_topic_id": None,
    }, ensure_ascii=False) + "\n", encoding="utf-8")
    chunks_path = engine_root / "data" / "chunks.jsonl"
    chunks_path.write_text(json.dumps({
        "chunk_id": "en-us/UserGuide/GettingStarted/GettingStarted::0",
        "topic_id": "en-us/UserGuide/GettingStarted/GettingStarted",
        "order": 0, "title": "Topic", "heading_path": ["Topic"],
        "content": "# Topic\n\nWelcome.\n", "language": "en-us",
        "quality": "canonical", "url": URL_A,
        "topic_path": "UserGuide/GettingStarted", "images": [],
        "paired_chunk_id": None, "char_count": 18, "token_estimate": 6,
    }, ensure_ascii=False) + "\n", encoding="utf-8")

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert net.calls["get"] == []
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    row = next(r for r in state if r["url"] == URL_A)
    assert row["status"] == "deleted"
    assert row["deleted_at"]
    assert row["etag"] == '"a-v1"'          # 墓碑保留最后指纹
    assert row["content_hash"] == "a" * 64
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    deleted = [r for r in exc if r["type"] == "deleted"]
    assert len(deleted) == 1
    assert deleted[0]["id"] == "en-us/UserGuide/GettingStarted/GettingStarted"
    assert deleted[0]["resolved"] is False
    # 数据集不残留旧产物
    assert not clean_file.exists()
    assert _jsonl(meta_path) == []
    assert _jsonl(chunks_path) == []
    assert "已删除" in capsys.readouterr().out


def test_incremental_revives_tombstoned_page_via_explicit_url(
        engine_root, cfg, monkeypatch):
    """AC(#18)：--url 显式探测墓碑页；指纹未变（304）也重新入库并清墓碑。"""
    etag = '"a-v1"'
    lastmod = "2026-05-21T08:18:54Z"
    net = FakeNetwork({URL_A: (etag, lastmod)})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    _seed_state(engine_root, [{
        "url": URL_A, "language": "en-us", "etag": etag, "lastmod": lastmod,
        "content_hash": "a" * 64, "status": "deleted",
        "last_ok_at": "2026-07-01T00:00:00Z",
        "deleted_at": "2026-08-01T00:00:00Z",
    }])
    sync_engine.upsert_exception({
        "id": "en-us/UserGuide/GettingStarted/GettingStarted",
        "type": "deleted", "detail": f"{URL_A} 曾删除",
        "discovered_at": "2026-08-01T00:00:00Z", "resolved": False,
    })

    code = sync_engine.incremental_sync(None, URL_A, cfg, rate=2.0)

    assert code == 0
    assert net.calls["head"] == [URL_A]
    assert net.calls["get"] == [URL_A]      # 304 也不跳过：墓碑页需重新入库
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    row = next(r for r in state if r["url"] == URL_A)
    assert row["status"] == "ok"
    assert row["deleted_at"] is None
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    deleted = next(r for r in exc if r["type"] == "deleted")
    assert deleted["resolved"] is True
    clean_file = engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")
    assert clean_file.exists()
    meta = _jsonl(engine_root / "data" / "metadata.jsonl")
    assert meta[0]["id"] == "en-us/UserGuide/GettingStarted/GettingStarted"
