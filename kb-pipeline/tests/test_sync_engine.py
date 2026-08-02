"""单 URL 全量对账引擎单元测试（票 #15，AC1–AC5）。"""
from __future__ import annotations

import json
import sys
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import pipeline as P
import run_sync
import sync_config
import sync_engine
import sync_state


URL = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
       "UserGuide/GettingStarted/GettingStarted.htm")
ZH_URL = ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
          "UserGuide/GettingStarted/GettingStarted.htm")

FIXTURE_HTML = """<html><head><title>Getting started</title></head>
<body><div id="contentBody"><h1>Getting started</h1>
<p>Welcome to Monitor ERP G5.</p>
<h2>Overview</h2><p>First part.</p>
<h2>Next steps</h2><p>Second part.</p>
<div class="note"><p>Remember to save.</p></div>
</div></body></html>"""


class FakeResponse:
    status = 200

    def __init__(self, body: bytes, lastmod: str = "2026-05-21T08:18:54Z",
                 etag: str = '"test-etag"'):
        self._body = body
        self.headers = {"Last-Modified": lastmod, "ETag": etag}

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def geturl(self) -> str:
        return URL

    def read(self) -> bytes:
        return self._body


@pytest.fixture
def engine_root(tmp_path, monkeypatch):
    """把引擎产物路径重定向到临时目录。"""
    monkeypatch.setattr(sync_engine, "ROOT", tmp_path)
    return tmp_path


@pytest.fixture
def fake_network(monkeypatch):
    """替换 pipeline._open：返回夹具页面并记录请求 UA。"""
    captured = {"headers": None, "calls": 0}

    def fake_open(url, headers, timeout=30):
        captured["headers"] = headers
        captured["calls"] += 1
        return FakeResponse(FIXTURE_HTML.encode("utf-8"))

    monkeypatch.setattr(P, "_open", fake_open)
    return captured


def test_parse_topic_url_derives_language_path_and_id():
    target = sync_engine.parse_topic_url(URL)
    assert target.language == "en-us"
    assert target.topic_path == "UserGuide/GettingStarted"
    assert target.page == "GettingStarted.htm"
    assert target.topic_id == "en-us/UserGuide/GettingStarted/GettingStarted"
    assert target.site == "https://help.monitorerp.cn/CN-MONITOR_G5"
    assert target.source == "help.monitorerp.cn"

    zh = sync_engine.parse_topic_url(ZH_URL)
    assert zh.language == "zh-cn"
    assert zh.topic_id == "zh-cn/UserGuide/GettingStarted/GettingStarted"


def test_parse_topic_url_rejects_invalid_urls():
    for bad in ("not-a-url", "https://example.test/no/topics/here.htm",
                "https://example.test/en-us/Content/Topics/NoPage"):
        with pytest.raises(ValueError):
            sync_engine.parse_topic_url(bad)


def test_pace_sleeps_one_over_rate(monkeypatch):
    slept = []
    monkeypatch.setattr(sync_engine.time, "sleep", slept.append)
    sync_engine._pace(5.0)
    assert slept == [0.2]


def test_reconcile_single_url_runs_full_pipeline(engine_root, fake_network,
                                                 monkeypatch, capsys):
    paced = []
    monkeypatch.setattr(sync_engine, "_pace", paced.append)
    cfg = sync_config.load_sync_config()

    code = sync_engine.reconcile_single_url(URL, cfg, rate=5.0)

    assert code == 0
    # 限速生效：抓取后按 1/rate 间隔等待
    assert paced == [5.0]
    # UA 生效：请求头携带配置 UA
    assert fake_network["headers"] == {"User-Agent": cfg.user_agent}
    # 原始 HTML 落盘（不入库目录 data/raw/）
    raw_file = engine_root / "data" / "raw" / "en-us" / "GettingStarted.htm"
    assert raw_file.read_bytes() == FIXTURE_HTML.encode("utf-8")
    headers = json.loads((engine_root / "data" / "raw" / "headers.json").read_text(
        encoding="utf-8"))
    assert headers[URL]["status"] == 200
    assert headers[URL]["etag"] == '"test-etag"'
    assert headers[URL]["lastmod"] == "2026-05-21T08:18:54Z"
    # 清洗 Markdown 入库
    clean_file = engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")
    md = clean_file.read_text(encoding="utf-8")
    assert "# Getting started" in md
    assert "Welcome to Monitor ERP G5." in md
    # 13 字段元数据入库
    meta_rows = [json.loads(line) for line in
                 (engine_root / "data" / "metadata.jsonl").read_text(
                     encoding="utf-8").splitlines() if line.strip()]
    assert len(meta_rows) == 1
    meta = meta_rows[0]
    assert set(meta) == P.EXPECTED_FIELDS_META
    assert meta["id"] == "en-us/UserGuide/GettingStarted/GettingStarted"
    assert meta["quality"] == "canonical"
    assert meta["content_hash"] == P.sha256_hex(md)
    assert meta["paired_topic_id"] is None
    # 14 字段分块入库
    chunks = [json.loads(line) for line in
              (engine_root / "data" / "chunks.jsonl").read_text(
                  encoding="utf-8").splitlines() if line.strip()]
    assert len(chunks) == 3
    assert all(set(c) == P.EXPECTED_FIELDS_CHUNK for c in chunks)
    assert [c["order"] for c in chunks] == [0, 1, 2]
    assert all(c["paired_chunk_id"] is None for c in chunks)
    # 同步状态 ok 记录（ETag/Last-Modified/content_hash）
    state_rows = [json.loads(line) for line in
                  (engine_root / "state" / "sync-state.jsonl").read_text(
                      encoding="utf-8").splitlines()]
    assert len(state_rows) == 1
    state = state_rows[0]
    assert state["status"] == "ok"
    assert state["url"] == URL
    assert state["etag"] == '"test-etag"'
    assert state["lastmod"] == "2026-05-21T08:18:54Z"
    assert state["content_hash"] == meta["content_hash"]
    # 自检结果全部 PASS
    check_txt = (engine_root / "data" / "selfcheck-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: ALL PASS" in check_txt
    assert "FAIL" not in check_txt


def test_reconcile_single_url_is_idempotent(engine_root, fake_network,
                                            monkeypatch):
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    cfg = sync_config.load_sync_config()

    sync_engine.reconcile_single_url(URL, cfg, rate=5.0)
    first_hash = (engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")).read_text(
            encoding="utf-8")
    code = sync_engine.reconcile_single_url(URL, cfg, rate=5.0)

    assert code == 0
    meta_lines = [line for line in
                  (engine_root / "data" / "metadata.jsonl").read_text(
                      encoding="utf-8").splitlines() if line.strip()]
    assert len(meta_lines) == 1
    chunk_lines = [line for line in
                   (engine_root / "data" / "chunks.jsonl").read_text(
                       encoding="utf-8").splitlines() if line.strip()]
    assert len(chunk_lines) == 3
    state_lines = (engine_root / "state" / "sync-state.jsonl").read_text(
        encoding="utf-8").splitlines()
    assert len(state_lines) == 1
    headers = json.loads((engine_root / "data" / "raw" / "headers.json").read_text(
        encoding="utf-8"))
    assert list(headers) == [URL]
    second_hash = (engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")).read_text(
            encoding="utf-8")
    assert first_hash == second_hash


def test_reconcile_preserves_other_topics(engine_root, fake_network,
                                          monkeypatch):
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    cfg = sync_config.load_sync_config()
    other_meta = {
        "id": "zh-cn/UserGuide/GettingStarted/MonitorBI",
        "title": "Monitor BI", "url": ZH_URL.replace("GettingStarted", "MonitorBI"),
        "source": "help.monitorerp.cn", "version": "25.8",
        "language": "zh-cn", "topic_path": "UserGuide/GettingStarted",
        "quality": "reference", "lastmod": "2026-05-21T08:22:34Z",
        "etag": '"other"', "content_hash": "deadbeef", "images": [],
        "paired_topic_id": None,
    }
    other_chunk = {
        "chunk_id": other_meta["id"] + "::0", "topic_id": other_meta["id"],
        "order": 0, "title": other_meta["title"], "heading_path": ["Monitor BI"],
        "content": "# Monitor BI", "language": "zh-cn", "quality": "reference",
        "url": other_meta["url"], "topic_path": other_meta["topic_path"],
        "images": [], "paired_chunk_id": None, "char_count": 13,
        "token_estimate": 10,
    }
    meta_path = engine_root / "data" / "metadata.jsonl"
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(other_meta, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    chunks_path = engine_root / "data" / "chunks.jsonl"
    chunks_path.write_text(json.dumps(other_chunk, ensure_ascii=False) + "\n",
                           encoding="utf-8")

    sync_engine.reconcile_single_url(URL, cfg, rate=5.0)

    meta_rows = [json.loads(line) for line in
                 meta_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(meta_rows) == 2
    ids = [r["id"] for r in meta_rows]
    assert ids.count("en-us/UserGuide/GettingStarted/GettingStarted") == 1
    assert other_meta["id"] in ids
    chunk_rows = [json.loads(line) for line in
                  chunks_path.read_text(encoding="utf-8").splitlines()
                  if line.strip()]
    assert len(chunk_rows) == 4
    assert sum(1 for c in chunk_rows
               if c["topic_id"] == "en-us/UserGuide/GettingStarted/GettingStarted") == 3
    assert sum(1 for c in chunk_rows if c["topic_id"] == other_meta["id"]) == 1


def test_reconcile_http_error_marks_state_error_and_returns_nonzero(
        engine_root, monkeypatch):
    def fake_open(url, headers, timeout=30):
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)

    monkeypatch.setattr(P, "_open", fake_open)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    cfg = sync_config.load_sync_config()

    code = sync_engine.reconcile_single_url(URL, cfg, rate=5.0)

    assert code == 1
    state_rows = [json.loads(line) for line in
                  (engine_root / "state" / "sync-state.jsonl").read_text(
                      encoding="utf-8").splitlines()]
    assert len(state_rows) == 1
    assert state_rows[0]["status"] == "error"
    assert state_rows[0]["url"] == URL
    assert not (engine_root / "data" / "metadata.jsonl").exists()
    assert not (engine_root / "data" / "chunks.jsonl").exists()


def test_reconcile_invalid_url_returns_nonzero_without_state(engine_root):
    cfg = sync_config.load_sync_config()
    code = sync_engine.reconcile_single_url("not-a-url", cfg, rate=5.0)
    assert code == 1
    assert not (engine_root / "state" / "sync-state.jsonl").exists()


def test_selfcheck_reports_failure_on_hash_mismatch(engine_root):
    meta = {
        "id": "en-us/UserGuide/GettingStarted/GettingStarted",
        "title": "Getting started", "url": URL, "source": "help.monitorerp.cn",
        "version": "25.8", "language": "en-us",
        "topic_path": "UserGuide/GettingStarted", "quality": "canonical",
        "lastmod": "2026-05-21T08:18:54Z", "etag": '"test-etag"',
        "content_hash": "0" * 64, "images": [], "paired_topic_id": None,
    }
    chunks = []
    clean_dir = engine_root / "data" / "clean"
    clean_dir.mkdir(parents=True, exist_ok=True)
    (clean_dir / "en-us_UserGuide_GettingStarted_GettingStarted.md").write_text(
        "# Getting started\n\nWelcome.\n", encoding="utf-8")

    ok = sync_engine.selfcheck_single(meta, chunks)

    assert ok is False
    check_txt = (engine_root / "data" / "selfcheck-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: HAS FAILURES" in check_txt
    assert "[FAIL] M8" in check_txt


def test_main_reconcile_url_delegates_to_engine(monkeypatch, capsys):
    calls = []

    def fake_engine(url, cfg, rate):
        calls.append((url, cfg, rate))
        return 7

    monkeypatch.setattr(run_sync.sync_engine, "reconcile_single_url", fake_engine)
    code = run_sync.main(["--mode", "reconcile", "--url", URL, "--rate", "5"])
    assert code == 7
    assert len(calls) == 1
    url, cfg, rate = calls[0]
    assert url == URL
    assert isinstance(cfg, sync_config.SyncConfig)
    assert rate == 5.0


def test_main_reconcile_url_dry_run_stays_plan_only(monkeypatch, capsys):
    def fake_engine(url, cfg, rate):
        raise AssertionError("dry-run 不应执行对账")

    monkeypatch.setattr(run_sync.sync_engine, "reconcile_single_url", fake_engine)
    code = run_sync.main(["--mode", "reconcile", "--url", URL, "--dry-run"])
    assert code == 0
    out = capsys.readouterr().out
    assert URL in out
    assert "dry-run" in out.lower()



def test_reconcile_preserves_existing_pairing(engine_root, fake_network,
                                              monkeypatch):
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    cfg = sync_config.load_sync_config()
    meta_path = engine_root / "data" / "metadata.jsonl"
    chunks_path = engine_root / "data" / "chunks.jsonl"

    sync_engine.reconcile_single_url(URL, cfg, rate=5.0)
    meta_rows = [json.loads(line) for line in
                 meta_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    meta_rows[0]["paired_topic_id"] = "zh-cn/UserGuide/GettingStarted/GettingStarted"
    meta_path.write_text(json.dumps(meta_rows[0], ensure_ascii=False) + "\n",
                         encoding="utf-8")
    chunks = [json.loads(line) for line in
              chunks_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    chunks[0]["paired_chunk_id"] = "zh-cn/UserGuide/GettingStarted/GettingStarted::0"
    chunks_path.write_text(
        "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks),
        encoding="utf-8")

    code = sync_engine.reconcile_single_url(URL, cfg, rate=5.0)

    assert code == 0
    meta_rows = [json.loads(line) for line in
                 meta_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert meta_rows[0]["paired_topic_id"] == (
        "zh-cn/UserGuide/GettingStarted/GettingStarted")
    chunks = [json.loads(line) for line in
              chunks_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert chunks[0]["paired_chunk_id"] == (
        "zh-cn/UserGuide/GettingStarted/GettingStarted::0")

def test_reconcile_selfcheck_failure_marks_state_error(engine_root, fake_network,
                                                       monkeypatch):
    """自检未通过时不得写 ok 状态，产物保留供人工检查。"""
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    monkeypatch.setattr(sync_engine, "selfcheck_single", lambda meta, chunks: False)
    cfg = sync_config.load_sync_config()

    code = sync_engine.reconcile_single_url(URL, cfg, rate=5.0)

    assert code == 1
    state_rows = [json.loads(line) for line in
                  (engine_root / "state" / "sync-state.jsonl").read_text(
                      encoding="utf-8").splitlines()]
    assert len(state_rows) == 1
    assert state_rows[0]["status"] == "error"
    assert state_rows[0]["url"] == URL
    assert state_rows[0]["content_hash"]
    assert (engine_root / "data" / "metadata.jsonl").exists()
    assert (engine_root / "data" / "chunks.jsonl").exists()


def test_selfcheck_rejects_zero_chunks(engine_root):
    """空页（0 分块）不能通过分块完整性自检。"""
    clean_txt = "# Getting started\n\nWelcome.\n"
    meta = {
        "id": "en-us/UserGuide/GettingStarted/GettingStarted",
        "title": "Getting started", "url": URL, "source": "help.monitorerp.cn",
        "version": "25.8", "language": "en-us",
        "topic_path": "UserGuide/GettingStarted", "quality": "canonical",
        "lastmod": "2026-05-21T08:18:54Z", "etag": '"test-etag"',
        "content_hash": P.sha256_hex(clean_txt), "images": [],
        "paired_topic_id": None,
    }
    clean_dir = engine_root / "data" / "clean"
    clean_dir.mkdir(parents=True, exist_ok=True)
    (clean_dir / "en-us_UserGuide_GettingStarted_GettingStarted.md").write_text(
        clean_txt, encoding="utf-8")

    ok = sync_engine.selfcheck_single(meta, [])

    assert ok is False
    check_txt = (engine_root / "data" / "selfcheck-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: HAS FAILURES" in check_txt
    assert "[FAIL] C0" in check_txt



def test_reconcile_known_url_404_tombstones_and_returns_nonzero(
        engine_root, monkeypatch):
    """AC(#18)：--url 对账中已知页 404 → 墓碑 + deleted 例外，旧产物清除。"""
    def fake_open(url, headers, timeout=30):
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)

    monkeypatch.setattr(P, "_open", fake_open)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    cfg = sync_config.load_sync_config()
    state = sync_state.SyncState(engine_root / "state" / "sync-state.jsonl")
    state.load()
    state.mark_ok(URL, language="en-us", etag='"old"', content_hash="0" * 64)
    clean_file = engine_root / "data" / "clean" / (
        "en-us_UserGuide_GettingStarted_GettingStarted.md")
    clean_file.parent.mkdir(parents=True, exist_ok=True)
    clean_file.write_text("# Topic\n\nWelcome.\n", encoding="utf-8")
    meta_path = engine_root / "data" / "metadata.jsonl"
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps({
        "id": "en-us/UserGuide/GettingStarted/GettingStarted",
        "title": "Topic", "url": URL, "source": "help.monitorerp.cn",
        "version": "25.8", "language": "en-us",
        "topic_path": "UserGuide/GettingStarted", "quality": "canonical",
        "lastmod": "2026-05-21T08:18:54Z", "etag": '"old"',
        "content_hash": "0" * 64, "images": [], "paired_topic_id": None,
    }, ensure_ascii=False) + "\n", encoding="utf-8")

    code = sync_engine.reconcile_single_url(URL, cfg, rate=5.0)

    assert code == 1
    state_rows = [json.loads(line) for line in
                  (engine_root / "state" / "sync-state.jsonl").read_text(
                      encoding="utf-8").splitlines() if line.strip()]
    assert len(state_rows) == 1
    row = state_rows[0]
    assert row["status"] == "deleted"
    assert row["deleted_at"]
    assert row["etag"] == '"old"'           # 墓碑保留最后指纹
    exc = [json.loads(line) for line in
           (engine_root / "data" / "exceptions.jsonl").read_text(
               encoding="utf-8").splitlines() if line.strip()]
    assert exc[0]["type"] == "deleted"
    assert exc[0]["id"] == "en-us/UserGuide/GettingStarted/GettingStarted"
    assert not clean_file.exists()
    meta_lines = []
    if (engine_root / "data" / "metadata.jsonl").exists():
        meta_lines = [json.loads(x) for x in (engine_root / "data" / "metadata.jsonl")
                      .read_text(encoding="utf-8").splitlines() if x.strip()]
    assert meta_lines == []
    chunk_lines = []
    if (engine_root / "data" / "chunks.jsonl").exists():
        chunk_lines = [json.loads(x) for x in (engine_root / "data" / "chunks.jsonl")
                       .read_text(encoding="utf-8").splitlines() if x.strip()]
    assert chunk_lines == []
