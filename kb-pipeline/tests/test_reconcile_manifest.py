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


def _seed_topic(root: Path, topic_id: str, url: str, language: str,
                quality: str, paired_topic_id: str | None = None) -> None:
    """写入一条可通过全量自检的主题产物（raw/clean/meta/chunks）。"""
    md = P.clean_markdown(FIXTURE_HTML, url)
    clean_dir = root / "data" / "clean"
    clean_dir.mkdir(parents=True, exist_ok=True)
    clean_file = clean_dir / (topic_id.replace("/", "_") + ".md")
    clean_file.write_text(md, encoding="utf-8")
    raw_dir = root / "data" / "raw" / language
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / (topic_id.replace("/", "_") + ".htm")).write_bytes(
        FIXTURE_HTML.encode("utf-8"))
    meta = {
        "id": topic_id, "title": "Topic", "url": url,
        "source": "help.monitorerp.cn", "version": "25.8",
        "language": language,
        "topic_path": "/".join(topic_id.split("/")[1:-1]),
        "quality": quality, "lastmod": "2026-05-21T08:18:54Z",
        "etag": '"seed"', "content_hash": P.sha256_hex(md), "images": [],
        "paired_topic_id": paired_topic_id,
    }
    meta_path = root / "data" / "metadata.jsonl"
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    rows = [r for r in _jsonl(meta_path) if r.get("id") != topic_id]
    rows.append(meta)
    rows.sort(key=lambda r: (r["language"], r["id"]))
    meta_path.write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
        encoding="utf-8")
    chunks_path = root / "data" / "chunks.jsonl"
    chunks_path.parent.mkdir(parents=True, exist_ok=True)
    chunk_rows = [c for c in _jsonl(chunks_path)
                  if c.get("topic_id") != topic_id]
    for order, chunk in enumerate(P.chunk_markdown(md)):
        chunk_rows.append({
            "chunk_id": f"{topic_id}::{order}", "topic_id": topic_id,
            "order": order, "title": meta["title"],
            "heading_path": [p["text"] for p in chunk["path"]],
            "content": chunk["content"], "language": language,
            "quality": quality, "url": url, "topic_path": meta["topic_path"],
            "images": [], "paired_chunk_id": None,
            "char_count": len(chunk["content"]),
            "token_estimate": P.est_tokens(chunk["content"]),
        })
    chunk_rows.sort(key=lambda c: (c["topic_id"], c["order"]))
    chunks_path.write_text(
        "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunk_rows),
        encoding="utf-8")


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
    _seed_topic(engine_root, "en-us/Area/Module/Topic0", gone,
                "en-us", "canonical")

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
    # 数据集不残留墓碑页旧产物
    assert not (engine_root / "data" / "clean" /
                "en-us_Area_Module_Topic0.md").exists()
    assert "en-us/Area/Module/Topic0" not in {
        r["id"] for r in _jsonl(engine_root / "data" / "metadata.jsonl")}
    assert all(c["topic_id"] != "en-us/Area/Module/Topic0"
               for c in _jsonl(engine_root / "data" / "chunks.jsonl"))


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
    monkeypatch.setattr(sync_engine.time, "sleep", lambda s: None)
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
    monkeypatch.setattr(sync_engine.time, "sleep", lambda s: None)

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




def test_reconcile_manifest_sitemap_disappearance_tombstones_and_removes_artifacts(
        engine_root, round_network, cfg, monkeypatch):
    """AC1/AC2：曾 ok 的 en 页从 sitemap 消失 → 墓碑 + deleted 例外，产物与配对清除。"""
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    gone_en = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
               "Legacy/OldTopic/OldTopic.htm")
    gone_id = "en-us/Legacy/OldTopic/OldTopic"
    zh_url = ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
              "Legacy/OldTopic/OldTopic.htm")
    zh_id = "zh-cn/Legacy/OldTopic/OldTopic"
    _seed_topic(engine_root, gone_id, gone_en, "en-us", "canonical", zh_id)
    _seed_topic(engine_root, zh_id, zh_url, "zh-cn", "reference", gone_id)
    state = sync_state.SyncState(engine_root / "state" / "sync-state.jsonl")
    state.load()
    state.mark_ok(gone_en, language="en-us", etag='"old-en"',
                  content_hash="e" * 64)
    state.mark_ok(zh_url, language="zh-cn", etag='"old-zh"',
                  content_hash="z" * 64)

    code = sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0)

    assert code == 0
    rows = _jsonl(engine_root / "state" / "sync-state.jsonl")
    gone_row = next(r for r in rows if r["url"] == gone_en)
    assert gone_row["status"] == "deleted"
    assert gone_row["deleted_at"]
    assert gone_row["etag"] == '"old-en"'           # 墓碑保留最后指纹
    assert gone_row["content_hash"] == "e" * 64
    zh_row = next(r for r in rows if r["url"] == zh_url)
    assert zh_row["status"] == "ok"                 # 在线 zh 镜像不受影响
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    deleted = [r for r in exc if r["type"] == "deleted" and r["id"] == gone_id]
    assert len(deleted) == 1
    assert deleted[0]["resolved"] is False
    # 数据集不残留墓碑页旧产物
    assert not (engine_root / "data" / "clean" /
                "en-us_Legacy_OldTopic_OldTopic.md").exists()
    meta = _jsonl(engine_root / "data" / "metadata.jsonl")
    assert gone_id not in {r["id"] for r in meta}
    assert all(c["topic_id"] != gone_id
               for c in _jsonl(engine_root / "data" / "chunks.jsonl"))
    # 对方配对解除：zh 镜像保留，但不再指向已删除 en 页
    zh_meta = next(r for r in meta if r["id"] == zh_id)
    assert zh_meta["paired_topic_id"] is None
    assert all(c["paired_chunk_id"] is None
               for c in _jsonl(engine_root / "data" / "chunks.jsonl")
               if c["topic_id"] == zh_id)


def test_reconcile_manifest_zh_previously_ok_now_404_tombstones(
        engine_root, monkeypatch, cfg):
    """AC1/AC2：曾 ok 的 zh 镜像 404 → 墓碑 + deleted/untranslated 例外，产物清除。"""
    en_url = EN_URLS[0]
    en_id = "en-us/Accounting/AccrualAccounting/AccrualAccounting"
    zh_url = sync_manifest.zh_url_for(en_url)
    zh_id = "zh-cn/Accounting/AccrualAccounting/AccrualAccounting"
    _seed_topic(engine_root, zh_id, zh_url, "zh-cn", "reference", en_id)
    state = sync_state.SyncState(engine_root / "state" / "sync-state.jsonl")
    state.load()
    state.mark_ok(zh_url, language="zh-cn", etag='"old-zh"',
                  content_hash="z" * 64)
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=set())
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(limit=4, cfg=cfg, rate=5.0)

    assert code == 0
    rows = _jsonl(engine_root / "state" / "sync-state.jsonl")
    zh_row = next(r for r in rows if r["url"] == zh_url)
    assert zh_row["status"] == "deleted"
    assert zh_row["deleted_at"]
    assert zh_row["etag"] == '"old-zh"'
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    assert any(r["type"] == "deleted" and r["id"] == zh_id for r in exc)
    assert any(r["type"] == "untranslated" and r["id"] == zh_id for r in exc)
    meta = _jsonl(engine_root / "data" / "metadata.jsonl")
    assert zh_id not in {r["id"] for r in meta}
    en_meta = next(r for r in meta if r["id"] == en_id)
    assert en_meta["paired_topic_id"] is None
    assert not (engine_root / "data" / "clean" /
                "zh-cn_Accounting_AccrualAccounting_AccrualAccounting.md"
                ).exists()


def test_reconcile_manifest_revival_clears_tombstone_and_resolves_exception(
        engine_root, round_network, cfg, monkeypatch):
    """AC3：墓碑页重现 → mark_ok 清墓碑、deleted 例外 resolved、产物重新入库。"""
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    url = EN_URLS[0]
    tid = "en-us/Accounting/AccrualAccounting/AccrualAccounting"
    state = sync_state.SyncState(engine_root / "state" / "sync-state.jsonl")
    state.load()
    state.mark_deleted(url, language="en-us", deleted_at="2026-08-01T00:00:00Z",
                       etag='"old"', content_hash="0" * 64)
    sync_engine.upsert_exception({
        "id": tid, "type": "deleted", "detail": f"{url} 曾删除",
        "discovered_at": "2026-08-01T00:00:00Z", "resolved": False,
    })

    code = sync_engine.reconcile_manifest(limit=1, cfg=cfg, rate=5.0)

    assert code == 0
    rows = _jsonl(engine_root / "state" / "sync-state.jsonl")
    row = next(r for r in rows if r["url"] == url)
    assert row["status"] == "ok"
    assert row["deleted_at"] is None
    assert row["etag"] == '"en"'
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    deleted = next(r for r in exc if r["type"] == "deleted" and r["id"] == tid)
    assert deleted["resolved"] is True
    meta = {r["id"] for r in _jsonl(engine_root / "data" / "metadata.jsonl")}
    assert tid in meta
    assert (engine_root / "data" / "clean" /
            "en-us_Accounting_AccrualAccounting_AccrualAccounting.md").exists()


def test_reconcile_manifest_topic_path_scopes_round(engine_root, monkeypatch, cfg):
    """AC1：--topic-path 把本轮限定为主题路径前缀下的 en 主题及其 zh 镜像。"""
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=ZH_OK)
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(
        limit=None, cfg=cfg, rate=5.0, topic_path="UserGuide/GettingStarted")

    assert code == 0
    meta = {r["id"]: r for r in _jsonl(engine_root / "data" / "metadata.jsonl")}
    assert set(meta) == {
        "en-us/UserGuide/GettingStarted/GettingStarted",
        "en-us/UserGuide/GettingStarted/MobileClient",
        "en-us/UserGuide/GettingStarted/MonitorBI",
        "zh-cn/UserGuide/GettingStarted/GettingStarted",
        "zh-cn/UserGuide/GettingStarted/WebClient",
    }
    # 双语配对与重命名映射：en MobileClient ↔ zh WebClient；MonitorBI 未翻译
    assert meta["en-us/UserGuide/GettingStarted/MobileClient"][
        "paired_topic_id"] == "zh-cn/UserGuide/GettingStarted/WebClient"
    assert meta["zh-cn/UserGuide/GettingStarted/WebClient"][
        "paired_topic_id"] == "en-us/UserGuide/GettingStarted/MobileClient"
    assert meta["en-us/UserGuide/GettingStarted/MonitorBI"][
        "paired_topic_id"] is None
    # 中文分块全部命中真实英文块；英文块为 null
    chunks = _jsonl(engine_root / "data" / "chunks.jsonl")
    assert all(c["paired_chunk_id"] for c in chunks if c["language"] == "zh-cn")
    assert all(c["paired_chunk_id"] is None for c in chunks
               if c["language"] == "en-us")
    for c in chunks:
        if c["language"] == "zh-cn":
            assert c["paired_chunk_id"].split("::", 1)[0] == (
                meta[c["topic_id"]]["paired_topic_id"])
    # 未翻译/重命名例外
    exc = {r["id"]: r for r in _jsonl(engine_root / "data" / "exceptions.jsonl")}
    assert exc["zh-cn/UserGuide/GettingStarted/MonitorBI"]["type"] == "untranslated"
    assert exc["zh-cn/UserGuide/GettingStarted/MobileClient"]["type"] == "renamed"
    # 自检 ALL PASS，配对检查不 SKIP（M9/C9 全过）
    check_txt = (engine_root / "data" / "selfcheck-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: ALL PASS" in check_txt
    assert "[SKIP]" not in check_txt


def test_reconcile_manifest_topic_path_does_not_tombstone_out_of_scope(
        engine_root, monkeypatch, cfg):
    """AC1：--topic-path 缩小处理范围，但删除检测仍以完整 sitemap 为准，
    范围外曾 ok 页面不被误标墓碑（状态保持 ok、无 deleted 例外）。"""
    out_url = EN_URLS[0]  # Accounting/AccrualAccounting（范围外）
    state = sync_state.SyncState(engine_root / "state" / "sync-state.jsonl")
    state.load()
    state.mark_ok(out_url, language="en-us", etag='"old"',
                  content_hash="a" * 64)
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=ZH_OK)
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(
        limit=None, cfg=cfg, rate=5.0, topic_path="UserGuide/GettingStarted")

    assert code == 0
    state2 = sync_state.SyncState(engine_root / "state" / "sync-state.jsonl")
    state2.load()
    assert state2.get(out_url)["status"] == "ok"
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    assert not [r for r in exc if r["type"] == "deleted"]
