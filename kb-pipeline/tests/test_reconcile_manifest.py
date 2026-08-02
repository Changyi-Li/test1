"""清单驱动全量对账引擎单元测试（票 #16，AC1–AC5）。"""
from __future__ import annotations

import json
import sys
import urllib.error
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import pipeline as P
import sync_config
import sync_engine
import sync_manifest
import sync_state


SITEMAP_URL = "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/sitemap.xml"

EN_URLS = [
    ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
     "Accounting/AccrualAccounting/AccrualAccounting.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
     "UserGuide/GettingStarted/GettingStarted.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
     "UserGuide/GettingStarted/MobileClient.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
     "UserGuide/GettingStarted/MonitorBI.htm"),
]

ZH_OK = {
    ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
     "Accounting/AccrualAccounting/AccrualAccounting.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
     "UserGuide/GettingStarted/GettingStarted.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
     "UserGuide/GettingStarted/WebClient.htm"),
}

FIXTURE_HTML = """<html><head><title>Topic</title></head>
<body><div id="contentBody"><h1>Topic</h1>
<p>Welcome to Monitor ERP G5.</p>
<h2>Overview</h2><p>First part.</p>
<h2>Next steps</h2><p>Second part.</p>
</div></body></html>"""


def sitemap_xml(urls: list[str]) -> str:
    entries = []
    for url in urls:
        path = url.split("help.monitorerp.cn/", 1)[1]
        loc = ("https://help.monitorerp.com/"
               + path.replace("/en-us/Content/Topics/",
                              "/en-us/Content/Content/Topics/", 1))
        entries.append(f"<url><loc>{loc}</loc></url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            + "".join(entries) + "</urlset>")


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
    def __init__(self, sitemap: str | None, en_ok=None, zh_ok=None,
                 fail_head=(), fail_status: int = 404):
        self.sitemap = sitemap
        self.en_ok = set(en_ok) if en_ok is not None else set(EN_URLS)
        self.zh_ok = set(zh_ok) if zh_ok is not None else set()
        self.fail_head = set(fail_head)
        self.fail_status = fail_status
        self.calls: dict[str, list[str]] = {"get": [], "head": []}

    def get(self, url, headers, timeout=30):
        self.calls["get"].append(url)
        if url == SITEMAP_URL:
            if self.sitemap is None:
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
            return FakeResponse(self.sitemap.encode("utf-8"),
                                etag='"sitemap"')
        if url in self.en_ok or url in self.zh_ok:
            return FakeResponse(FIXTURE_HTML.encode("utf-8"), etag='"en"')
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)

    def head(self, url, headers, timeout=30):
        self.calls["head"].append(url)
        if url in self.fail_head:
            raise urllib.error.HTTPError(url, self.fail_status, "Not Found", {}, None)
        if "/en-us/" in url:
            ok = url in self.en_ok
        else:
            ok = url in self.zh_ok
        if ok:
            return FakeResponse(etag='"h"')
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)


@pytest.fixture
def engine_root(tmp_path, monkeypatch):
    monkeypatch.setattr(sync_engine, "ROOT", tmp_path)
    return tmp_path


@pytest.fixture
def cfg():
    return replace(sync_config.load_sync_config(),
                   renames={"UserGuide/GettingStarted/MobileClient": "WebClient.htm"})


@pytest.fixture
def round_network(monkeypatch):
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS[:3]), zh_ok=ZH_OK)
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    return net


def _jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in
            path.read_text(encoding="utf-8").splitlines() if line.strip()]


def test_reconcile_manifest_runs_full_pipeline_with_mirrors(
        engine_root, round_network, cfg, monkeypatch):
    paced = []
    monkeypatch.setattr(sync_engine, "_pace", paced.append)

    code = sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0)

    assert code == 0
    # 限速生效：每个网络请求后按 1/rate 等待
    assert len(paced) == (len(round_network.calls["get"])
                          + len(round_network.calls["head"]))
    # sitemap 下载与修复生效（只处理 Topics/*.htm）
    assert round_network.calls["get"][0] == SITEMAP_URL
    # en 保真层 + zh 参考层入库，配对双向正确
    meta = {r["id"]: r for r in _jsonl(engine_root / "data" / "metadata.jsonl")}
    assert set(meta) == {
        "en-us/Accounting/AccrualAccounting/AccrualAccounting",
        "en-us/UserGuide/GettingStarted/GettingStarted",
        "en-us/UserGuide/GettingStarted/MobileClient",
        "zh-cn/Accounting/AccrualAccounting/AccrualAccounting",
        "zh-cn/UserGuide/GettingStarted/GettingStarted",
        "zh-cn/UserGuide/GettingStarted/WebClient",
    }
    assert meta["en-us/Accounting/AccrualAccounting/AccrualAccounting"]["quality"] == "canonical"
    assert meta["zh-cn/Accounting/AccrualAccounting/AccrualAccounting"]["quality"] == "reference"
    assert meta["en-us/UserGuide/GettingStarted/MobileClient"]["paired_topic_id"] == (
        "zh-cn/UserGuide/GettingStarted/WebClient")
    assert meta["zh-cn/UserGuide/GettingStarted/WebClient"]["paired_topic_id"] == (
        "en-us/UserGuide/GettingStarted/MobileClient")
    assert meta["en-us/UserGuide/GettingStarted/GettingStarted"]["paired_topic_id"] == (
        "zh-cn/UserGuide/GettingStarted/GettingStarted")
    # 重命名例外写入例外表
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    renamed = [r for r in exc if r["type"] == "renamed"]
    assert len(renamed) == 1
    assert renamed[0]["id"] == "zh-cn/UserGuide/GettingStarted/MobileClient"
    assert "WebClient" in renamed[0]["detail"]
    # 分块镜像配对：zh 全部命中，en 为 null
    chunks = _jsonl(engine_root / "data" / "chunks.jsonl")
    assert all(c["paired_chunk_id"] for c in chunks if c["language"] == "zh-cn")
    assert all(c["paired_chunk_id"] is None for c in chunks
               if c["language"] == "en-us")
    for c in chunks:
        if c["language"] == "zh-cn":
            assert c["paired_chunk_id"].split("::", 1)[0] == (
                meta[c["topic_id"]]["paired_topic_id"])
    # 自检 ALL PASS，配对检查不再 SKIP
    check_txt = (engine_root / "data" / "selfcheck-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: ALL PASS" in check_txt
    assert "[SKIP]" not in check_txt
    assert "[PASS] M9" in check_txt
    assert "[PASS] C9" in check_txt
    # 同步状态：en 3 + zh 3 全部 ok；未翻译 zh 页不写状态
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    assert len(state) == 6
    assert all(r["status"] == "ok" for r in state)


def test_reconcile_manifest_limit_scopes_round(engine_root, monkeypatch, cfg):
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=set())
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(limit=2, cfg=cfg, rate=5.0)

    assert code == 0
    meta = _jsonl(engine_root / "data" / "metadata.jsonl")
    assert len(meta) == 2
    assert {r["id"] for r in meta} == {
        "en-us/Accounting/AccrualAccounting/AccrualAccounting",
        "en-us/UserGuide/GettingStarted/GettingStarted",
    }
    exc = {r["id"] for r in _jsonl(engine_root / "data" / "exceptions.jsonl")
           if r["type"] == "untranslated"}
    assert exc == {
        "zh-cn/Accounting/AccrualAccounting/AccrualAccounting",
        "zh-cn/UserGuide/GettingStarted/GettingStarted",
    }


def test_reconcile_manifest_writes_untranslated_exception(
        engine_root, monkeypatch, cfg):
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=set())
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(limit=4, cfg=cfg, rate=5.0)

    assert code == 0
    meta = {r["id"]: r for r in _jsonl(engine_root / "data" / "metadata.jsonl")}
    assert meta["en-us/UserGuide/GettingStarted/MonitorBI"]["paired_topic_id"] is None
    assert "zh-cn/UserGuide/GettingStarted/MonitorBI" not in meta
    exc = {r["id"] for r in _jsonl(engine_root / "data" / "exceptions.jsonl")
           if r["type"] == "untranslated"}
    assert "zh-cn/UserGuide/GettingStarted/MonitorBI" in exc
    # 未翻译 zh 404 不写同步状态（结构性例外，非运行时错误）
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    zh_monitor_bi = ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
                     "UserGuide/GettingStarted/MonitorBI.htm")
    assert all(r["url"] != zh_monitor_bi for r in state)


def test_reconcile_manifest_aborts_when_sitemap_unavailable(
        engine_root, monkeypatch, cfg, capsys):
    net = FakeNetwork(sitemap=None)
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0)

    assert code == 1
    assert "sitemap" in capsys.readouterr().err.lower()
    assert net.calls["head"] == []
    assert not (engine_root / "data" / "metadata.jsonl").exists()
    assert not (engine_root / "state" / "sync-state.jsonl").exists()


def test_reconcile_manifest_aborts_when_en_head_mismatch_over_ten_percent(
        engine_root, monkeypatch, cfg, capsys):
    urls = [(f"https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
             f"Area/Module/Topic{i}.htm") for i in range(12)]
    net = FakeNetwork(sitemap=sitemap_xml(urls), en_ok=urls[:10],
                      fail_head=urls[10:12])
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(limit=None, cfg=cfg, rate=5.0)

    assert code == 1
    assert "> 10.0%" in capsys.readouterr().err
    assert not (engine_root / "data" / "metadata.jsonl").exists()
    assert len([u for u in net.calls["get"] if u != SITEMAP_URL]) == 0


def test_reconcile_manifest_marks_deleted_for_previously_ok_en_404(
        engine_root, monkeypatch, cfg):
    urls = [(f"https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
             f"Area/Module/Topic{i}.htm") for i in range(20)]
    gone = urls[0]
    net = FakeNetwork(sitemap=sitemap_xml(urls), en_ok=urls[1:],
                      fail_head={gone})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    state = sync_state.SyncState(engine_root / "state" / "sync-state.jsonl")
    state.load()
    state.mark_ok(gone, language="en-us", etag='"old"',
                  content_hash="0" * 64)

    code = sync_engine.reconcile_manifest(limit=None, cfg=cfg, rate=5.0)

    assert code == 0
    rows = _jsonl(engine_root / "state" / "sync-state.jsonl")
    gone_row = next(r for r in rows if r["url"] == gone)
    assert gone_row["status"] == "deleted"
    assert gone_row["etag"] == '"old"'
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    deleted = [r for r in exc if r["type"] == "deleted"]
    assert len(deleted) == 1
    assert deleted[0]["id"] == "en-us/Area/Module/Topic0"


def test_reconcile_manifest_en_http_500_is_error_not_deleted(
        engine_root, monkeypatch, cfg):
    urls = [(f"https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
             f"Area/Module/Topic{i}.htm") for i in range(12)]
    down = urls[0]
    net = FakeNetwork(sitemap=sitemap_xml(urls), en_ok=urls,
                      fail_head={down}, fail_status=500)
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    state = sync_state.SyncState(engine_root / "state" / "sync-state.jsonl")
    state.load()
    state.mark_ok(down, language="en-us", etag='"old"',
                  content_hash="0" * 64)

    code = sync_engine.reconcile_manifest(limit=None, cfg=cfg, rate=5.0)

    assert code == 0
    rows = _jsonl(engine_root / "state" / "sync-state.jsonl")
    down_row = next(r for r in rows if r["url"] == down)
    assert down_row["status"] == "error"
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    assert not any(e["type"] == "deleted" for e in exc)


def test_reconcile_manifest_zh_http_500_is_error_not_untranslated(
        engine_root, monkeypatch, cfg):
    zh_down = ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
               "Accounting/AccrualAccounting/AccrualAccounting.htm")
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=set(),
                      fail_head={zh_down}, fail_status=500)
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(limit=4, cfg=cfg, rate=5.0)

    assert code == 0
    exc = {r["id"] for r in _jsonl(engine_root / "data" / "exceptions.jsonl")
           if r["type"] == "untranslated"}
    assert "zh-cn/Accounting/AccrualAccounting/AccrualAccounting" not in exc
    assert "zh-cn/UserGuide/GettingStarted/MonitorBI" in exc
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    zh_row = next(r for r in state if r["url"] == zh_down)
    assert zh_row["status"] == "error"
    meta = {r["id"]: r for r in _jsonl(engine_root / "data" / "metadata.jsonl")}
    assert meta["en-us/Accounting/AccrualAccounting/AccrualAccounting"][
        "paired_topic_id"] is None


def test_reconcile_manifest_rerun_is_idempotent(
        engine_root, round_network, cfg, monkeypatch):
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    assert sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0) == 0
    first_meta = (engine_root / "data" / "metadata.jsonl").read_text(
        encoding="utf-8")
    first_exc = (engine_root / "data" / "exceptions.jsonl").read_text(
        encoding="utf-8")
    first_chunks = (engine_root / "data" / "chunks.jsonl").read_text(
        encoding="utf-8")

    assert sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0) == 0

    assert (engine_root / "data" / "metadata.jsonl").read_text(
        encoding="utf-8") == first_meta
    assert (engine_root / "data" / "exceptions.jsonl").read_text(
        encoding="utf-8") == first_exc
    assert (engine_root / "data" / "chunks.jsonl").read_text(
        encoding="utf-8") == first_chunks
    assert len(_jsonl(engine_root / "state" / "sync-state.jsonl")) == 6


def test_reconcile_manifest_fails_when_pairing_missing(
        engine_root, round_network, cfg, monkeypatch):
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    monkeypatch.setattr(sync_engine, "apply_pairings", lambda mirrors: None)

    code = sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0)

    assert code == 1
    check_txt = (engine_root / "data" / "selfcheck-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: HAS FAILURES" in check_txt
    assert "[FAIL] C9" in check_txt


