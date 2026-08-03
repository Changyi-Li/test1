"""全量对账质量门单元测试（票 #20，AC1–AC5）。

覆盖：图片 URL 去重后全量验证（broken_image 例外与 revive）、机器检查 100%
（M1 字段集合/M2 id 唯一）、转换质量 7 项逐页（含无截断/乱码）、按模块抽查
模板（check_dataset_sampled / sample_pages_per_module）、门禁失败非零退出并
给出失败清单，以及 run_sync --mode check CLI 能力。
"""
from __future__ import annotations

import json
import re
import sys
import urllib.error
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import pipeline as P
import run_sync
import sync_config
import sync_engine
import sync_manifest


SITEMAP_URL = "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/sitemap.xml"
IMAGE_URL = "https://help.monitorerp.cn/CN-MONITOR_G5/Images/diagram.png"

EN_URLS = [
    ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
     "Accounting/AccrualAccounting/AccrualAccounting.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
     "UserGuide/GettingStarted/GettingStarted.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
     "UserGuide/GettingStarted/MobileClient.htm"),
]

ZH_OK = {
    ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
     "Accounting/AccrualAccounting/AccrualAccounting.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
     "UserGuide/GettingStarted/GettingStarted.htm"),
    ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
     "UserGuide/GettingStarted/WebClient.htm"),
}

IMAGE_HTML = """<html><head><title>Topic</title></head>
<body><div id="contentBody"><h1>Topic</h1>
<p>Welcome to Monitor ERP G5.</p>
<img src="https://help.monitorerp.cn/CN-MONITOR_G5/Images/diagram.png" alt="diagram"/>
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
                 fail_head=(), fail_status: int = 404,
                 broken_images=(), ok_images=()):
        self.sitemap = sitemap
        self.en_ok = set(en_ok) if en_ok is not None else set(EN_URLS)
        self.zh_ok = set(zh_ok) if zh_ok is not None else set()
        self.fail_head = set(fail_head)
        self.fail_status = fail_status
        self.broken_images = set(broken_images)
        self.ok_images = set(ok_images)
        self.calls: dict[str, list[str]] = {"get": [], "head": []}

    def get(self, url, headers, timeout=30):
        self.calls["get"].append(url)
        if url == SITEMAP_URL:
            if self.sitemap is None:
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
            return FakeResponse(self.sitemap.encode("utf-8"), etag='"sitemap"')
        if url in self.en_ok or url in self.zh_ok:
            return FakeResponse(IMAGE_HTML.encode("utf-8"), etag='"en"')
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)

    def head(self, url, headers, timeout=30):
        self.calls["head"].append(url)
        if url in self.fail_head:
            raise urllib.error.HTTPError(url, self.fail_status, "Not Found", {}, None)
        if url in self.broken_images:
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
        if url in self.ok_images:
            return FakeResponse(etag='"img"')
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
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=ZH_OK,
                      ok_images={IMAGE_URL})
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
    """写入一条可通过 M/C 自检的主题产物（raw/clean/meta/chunks）。"""
    md = P.clean_markdown(IMAGE_HTML, url)
    clean_dir = root / "data" / "clean"
    clean_dir.mkdir(parents=True, exist_ok=True)
    clean_file = clean_dir / (topic_id.replace("/", "_") + ".md")
    clean_file.write_text(md, encoding="utf-8")
    raw_dir = root / "data" / "raw" / language
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / (topic_id.replace("/", "_") + ".htm")).write_bytes(
        IMAGE_HTML.encode("utf-8"))
    images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md)
    meta = {
        "id": topic_id, "title": "Topic", "url": url,
        "source": "help.monitorerp.cn", "version": "25.8",
        "language": language,
        "topic_path": "/".join(topic_id.split("/")[1:-1]),
        "quality": quality, "lastmod": "2026-05-21T08:18:54Z",
        "etag": '"seed"', "content_hash": P.sha256_hex(md), "images": images,
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
            "images": re.findall(r"!\[[^\]]*\]\(([^)]+)\)", chunk["content"]),
            "paired_chunk_id": None,
            "char_count": len(chunk["content"]),
            "token_estimate": P.est_tokens(chunk["content"]),
        })
    chunk_rows.sort(key=lambda c: (c["topic_id"], c["order"]))
    chunks_path.write_text(
        "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunk_rows),
        encoding="utf-8")


def _seed_module_pages(root: Path, module: str, count: int) -> list[str]:
    """在指定模块内生成 count 个可通过自检的 en 主题，返回 topic_id 列表。"""
    ids = []
    for i in range(count):
        name = f"Topic{i:02d}"
        tid = f"en-us/{module}/ModulePage/{name}"
        url = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
               f"{module}/ModulePage/{name}.htm")
        _seed_topic(root, tid, url, "en-us", "canonical")
        ids.append(tid)
    return ids


def test_raw_keyed_by_topic_id_avoids_page_name_collision(engine_root):
    """data/raw 按 topic_id 编码文件名落盘，同名页互不覆盖（票 #26 回归）。"""
    url_a = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
             "Stock/Alpha/bSettings.htm")
    url_b = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
             "Stock/Beta/bSettings.htm")
    _seed_topic(engine_root, "en-us/Stock/Alpha/bSettings", url_a,
                "en-us", "canonical")
    _seed_topic(engine_root, "en-us/Stock/Beta/bSettings", url_b,
                "en-us", "canonical")
    ra = (engine_root / "data" / "raw" / "en-us" /
          "en-us_Stock_Alpha_bSettings.htm")
    rb = (engine_root / "data" / "raw" / "en-us" /
          "en-us_Stock_Beta_bSettings.htm")
    assert ra.exists() and rb.exists()
    assert not (engine_root / "data" / "raw" / "en-us" /
                "bSettings.htm").exists()


# ---------- AC1 图片 URL 去重后全量验证，404 记 broken_image 例外 ----------

def test_reconcile_manifest_records_broken_image_exception(
        engine_root, cfg, monkeypatch):
    """图片 404 → broken_image 例外（detail 记所属主题），且去重后只 HEAD 一次。"""
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=ZH_OK,
                      broken_images={IMAGE_URL})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0)

    assert code == 0   # broken_image 是结构性例外，不失败
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    broken = [r for r in exc if r["type"] == "broken_image"]
    assert len(broken) == 1
    assert broken[0]["id"] == IMAGE_URL
    assert "被" in broken[0]["detail"]
    assert broken[0]["resolved"] is False
    # 去重：3 en + 3 zh 主题共用同一图片，只 HEAD 一次
    assert net.calls["head"].count(IMAGE_URL) == 1


def test_image_revival_resolves_broken_image_exception(
        engine_root, cfg, monkeypatch):
    """上次 404 的图片这次 200 → 既有 broken_image 例外 resolved。"""
    sync_engine.upsert_exception({
        "id": IMAGE_URL, "type": "broken_image", "detail": "曾失效",
        "discovered_at": "2026-08-01T00:00:00Z", "resolved": False,
    })
    net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=ZH_OK,
                      ok_images={IMAGE_URL})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    code = sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0)

    assert code == 0
    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    broken = [r for r in exc if r["type"] == "broken_image"
              and r["id"] == IMAGE_URL]
    assert len(broken) == 1
    assert broken[0]["resolved"] is True


def _run_reconcile_with_image(engine_root, cfg, monkeypatch, status: str):
    """用指定图片状态跑一次 limit=3 对账；status 为 'ok' 或 'broken'。"""
    if status == "ok":
        net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=ZH_OK,
                          ok_images={IMAGE_URL})
    else:
        net = FakeNetwork(sitemap=sitemap_xml(EN_URLS), zh_ok=ZH_OK,
                          broken_images={IMAGE_URL})
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    return sync_engine.reconcile_manifest(limit=3, cfg=cfg, rate=5.0)


def test_image_rebreak_reopens_broken_image_exception(engine_root, cfg,
                                                      monkeypatch):
    """broken→revive→broken：例外重新标回 resolved:False（不残留在 resolved）。"""
    _run_reconcile_with_image(engine_root, cfg, monkeypatch, "broken")
    _run_reconcile_with_image(engine_root, cfg, monkeypatch, "ok")
    _run_reconcile_with_image(engine_root, cfg, monkeypatch, "broken")

    exc = _jsonl(engine_root / "data" / "exceptions.jsonl")
    broken = [r for r in exc if r["type"] == "broken_image"
              and r["id"] == IMAGE_URL]
    assert len(broken) == 1
    assert broken[0]["resolved"] is False


def test_verify_images_dedups_across_dataset(engine_root, cfg, monkeypatch):
    """多个主题引用同一图片 URL → verify_images 只验证一次。"""
    _seed_topic(engine_root, "en-us/Accounting/AccrualAccounting/AccrualAccounting",
                ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
                 "Accounting/AccrualAccounting/AccrualAccounting.htm"),
                "en-us", "canonical")
    _seed_topic(engine_root, "zh-cn/Accounting/AccrualAccounting/AccrualAccounting",
                ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
                 "Accounting/AccrualAccounting/AccrualAccounting.htm"),
                "zh-cn", "reference")
    net = FakeNetwork(sitemap=None, ok_images={IMAGE_URL})
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)

    broken, stop = sync_engine.verify_images(cfg, rate=5.0, headers_rec={},
                                             round_f=sync_engine.RoundFailures())

    assert broken == [] and stop is None
    assert net.calls["head"].count(IMAGE_URL) == 1   # 去重：2 主题 1 个 URL


# ---------- AC2 机器检查 100%（M1 字段集合 / M2 id 唯一） ----------

def _valid_meta_row(topic_id: str, url: str, language: str, quality: str) -> dict:
    return {
        "id": topic_id, "title": "Topic", "url": url,
        "source": "help.monitorerp.cn", "version": "25.8", "language": language,
        "topic_path": "/".join(topic_id.split("/")[1:-1]),
        "quality": quality, "lastmod": "2026-05-21T08:18:54Z",
        "etag": '"seed"', "content_hash": "0" * 64, "images": [],
        "paired_topic_id": None,
    }


def test_machine_check_rejects_duplicate_id(engine_root):
    rows = [
        _valid_meta_row("en-us/UserGuide/GettingStarted/GettingStarted",
                        "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm",
                        "en-us", "canonical"),
        _valid_meta_row("en-us/UserGuide/GettingStarted/GettingStarted",
                        "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/UserGuide/GettingStarted/MobileClient.htm",
                        "en-us", "canonical"),
    ]
    log = sync_engine._machine_check(rows, [], [], {})
    assert log.ok is False
    assert any("M2" in f for f in log.failures)


def test_machine_check_accepts_parens_in_topic_id(engine_root):
    """真实文件名含括号（tWarnings(intotal)）应通过 M2 id 格式（票 #27 回归）。"""
    row = _valid_meta_row(
        "en-us/Stock/Valuation/WIPValue/tWarnings(intotal)",
        "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/Stock/Valuation/WIPValue/tWarnings(intotal).htm",
        "en-us", "canonical")
    log = sync_engine._machine_check([row], [], [], {})
    assert not any("M2" in f for f in log.failures)


def test_machine_check_rejects_unknown_field(engine_root):
    row = _valid_meta_row("en-us/UserGuide/GettingStarted/GettingStarted",
                          "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm",
                          "en-us", "canonical")
    row["extra"] = "surprise"
    log = sync_engine._machine_check([row], [], [], {})
    assert log.ok is False
    assert any("M1" in f for f in log.failures)


def _valid_chunk_row(topic_id: str, url: str, content: str,
                     token_estimate: int, language: str = "en-us",
                     order: int = 0) -> dict:
    quality = "canonical" if language == "en-us" else "reference"
    return {
        "chunk_id": f"{topic_id}::{order}", "topic_id": topic_id, "order": order,
        "title": "Topic", "heading_path": ["Topic"], "content": content,
        "language": language, "quality": quality, "url": url,
        "topic_path": "/".join(topic_id.split("/")[1:-1]),
        "images": [], "paired_chunk_id": None,
        "char_count": len(content), "token_estimate": token_estimate,
    }


def test_machine_check_c8_allows_atomic_oversize_chunk(engine_root):
    """超上限但无空行切分点的原子块（表格）通过 C8（票 #28 原子块例外）。"""
    tid = "en-us/Stock/Parts/PartPrices"
    url = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
           "Stock/Parts/PartPrices.htm")
    meta = _valid_meta_row(tid, url, "en-us", "canonical")
    atomic = _valid_chunk_row(
        tid, url, "| A | B |\n|---|---|\n" + "| x | y |\n" * 200, 2500)
    log = sync_engine._machine_check([meta], [atomic], [], {})
    assert not any("C8" in f for f in log.failures)


def test_machine_check_c8_rejects_splitable_oversize_chunk(engine_root):
    """有可切分点（空行）却仍超上限的块判 C8 FAIL。"""
    tid = "en-us/Stock/Parts/PartPrices"
    url = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
           "Stock/Parts/PartPrices.htm")
    meta = _valid_meta_row(tid, url, "en-us", "canonical")
    splitable = _valid_chunk_row(
        tid, url, "Para one\n\nPara two\n\n" + "word " * 1000, 2500)
    log = sync_engine._machine_check([meta], [splitable], [], {})
    assert any("C8" in f for f in log.failures)


def test_machine_check_c9_allows_non_isomorphic_unmatched_chunks(
        engine_root):
    """非同构页：zh 翻译缺 h4 导致部分块匹配不上 → 允许 None（票 #32 决策）。"""
    en_tid = "en-us/Stock/Calculation/CalculateMeanPrice/bSettings"
    zh_tid = "zh-cn/Stock/Calculation/CalculateMeanPrice/bSettings"
    en_url = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
              "Stock/Calculation/CalculateMeanPrice/bSettings.htm")
    zh_url = ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
              "Stock/Calculation/CalculateMeanPrice/bSettings.htm")
    en_meta = _valid_meta_row(en_tid, en_url, "en-us", "canonical")
    zh_meta = _valid_meta_row(zh_tid, zh_url, "zh-cn", "reference")
    en_meta["paired_topic_id"] = zh_tid
    zh_meta["paired_topic_id"] = en_tid
    chunks = [
        _valid_chunk_row(en_tid, en_url, "c0", 100, order=0),
        _valid_chunk_row(en_tid, en_url, "c1", 100, order=1),
        _valid_chunk_row(zh_tid, zh_url, "z0", 100, language="zh-cn", order=0),
        _valid_chunk_row(zh_tid, zh_url, "z1", 100, language="zh-cn", order=1),
    ]
    chunks[2]["paired_chunk_id"] = f"{en_tid}::0"
    expected = {zh_tid: en_tid, en_tid: zh_tid}
    log = sync_engine._machine_check([en_meta, zh_meta], chunks, [], expected)
    assert not any("C9" in f for f in log.failures)


def test_machine_check_c9_rejects_totally_unpaired_topic(engine_root):
    """配对步骤完全缺失（所有 zh 块都 None）仍判 C9 FAIL。"""
    en_tid = "en-us/Stock/Calculation/CalculateMeanPrice/bSettings"
    zh_tid = "zh-cn/Stock/Calculation/CalculateMeanPrice/bSettings"
    en_url = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
              "Stock/Calculation/CalculateMeanPrice/bSettings.htm")
    zh_url = ("https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
              "Stock/Calculation/CalculateMeanPrice/bSettings.htm")
    en_meta = _valid_meta_row(en_tid, en_url, "en-us", "canonical")
    zh_meta = _valid_meta_row(zh_tid, zh_url, "zh-cn", "reference")
    en_meta["paired_topic_id"] = zh_tid
    zh_meta["paired_topic_id"] = en_tid
    chunks = [
        _valid_chunk_row(en_tid, en_url, "c0", 100, order=0),
        _valid_chunk_row(zh_tid, zh_url, "z0", 100, language="zh-cn", order=0),
        _valid_chunk_row(zh_tid, zh_url, "z1", 100, language="zh-cn", order=1),
    ]
    expected = {zh_tid: en_tid, en_tid: zh_tid}
    log = sync_engine._machine_check([en_meta, zh_meta], chunks, [], expected)
    assert any("C9" in f for f in log.failures)


# ---------- AC3 转换质量逐页 7 项（含无截断/乱码） ----------

def test_garbled_markdown_problems_detects_signals():
    assert P.garbled_markdown_problems("# OK\n\ntext.\n") == []
    assert len(P.garbled_markdown_problems("# T\n\n��\n")) == 1
    assert len(P.garbled_markdown_problems("# T\n\ncafÃ©\n")) == 1
    assert len(P.garbled_markdown_problems("# T\n\n```\nunclosed\n")) == 1
    assert len(P.garbled_markdown_problems("# T\n\nsee [a](https://x.com")) == 1
    assert len(P.garbled_markdown_problems("# T\n\nctrl \x07\n")) == 1


def test_selfcheck_dataset_reports_seven_conversion_checks(
        engine_root, round_network, cfg, monkeypatch):
    """逐页 7 项 Q 检查全部出现；乱码页在 Q3 失败。"""
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    sync_engine.reconcile_manifest(limit=1, cfg=cfg, rate=5.0)

    check_txt = (engine_root / "data" / "selfcheck-results.txt").read_text(
        encoding="utf-8")
    for q in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"):
        assert f"[PASS] {q}" in check_txt, f"missing {q}"
    assert "RESULT: ALL PASS" in check_txt


def _garbled_clean_file(engine_root: Path) -> Path:
    """limit=1 时清单首个 en 主题的清洗产物（写入 U+FFFD 以触发 Q3/M8 失败）。"""
    clean_file = (engine_root / "data" / "clean" /
                  "en-us_Accounting_AccrualAccounting_AccrualAccounting.md")
    clean_file.write_text(clean_file.read_text(encoding="utf-8") + "�",
                          encoding="utf-8")
    return clean_file


def test_selfcheck_dataset_fails_garbled_page(engine_root, round_network,
                                              cfg, monkeypatch):
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    sync_engine.reconcile_manifest(limit=1, cfg=cfg, rate=5.0)
    # 污染页面清洗产物：写入 U+FFFD，Q3 与 M8 都应失败
    _garbled_clean_file(engine_root)

    ok = sync_engine.selfcheck_dataset({})
    check_txt = (engine_root / "data" / "selfcheck-results.txt").read_text(
        encoding="utf-8")
    assert ok is False
    assert "[FAIL] Q3" in check_txt
    assert "[FAIL] M8" in check_txt
    assert "RESULT: HAS FAILURES" in check_txt


def test_selfcheck_dataset_prints_failure_list(engine_root, round_network,
                                               cfg, monkeypatch, capsys):
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    sync_engine.reconcile_manifest(limit=1, cfg=cfg, rate=5.0)
    _garbled_clean_file(engine_root)

    sync_engine.selfcheck_dataset({})

    err = capsys.readouterr().err
    assert "自检失败清单" in err
    assert "[FAIL] Q3" in err


# ---------- AC4 抽查模板（每模块 ≥5% 且 ≥10 页）作为 CLI 检查能力 ----------

def test_sample_pages_per_module_min_pages_floor():
    meta = [{"id": f"en-us/Mod{i}/T{t}", "topic_path": f"Mod{i}/T{t}"}
            for i in range(2) for t in range(3)]
    check_cfg = sync_config.CheckConfig(sample_min_percent=5, sample_min_pages=10)
    sampled = sync_engine.sample_pages_per_module(meta, check_cfg)
    assert sampled == {m["id"] for m in meta}   # 每模块 3 页 < 10 → 全取


def test_sample_pages_per_module_five_percent_floor():
    meta = [{"id": f"en-us/Mod0/T{t:02d}", "topic_path": f"Mod0/T{t:02d}"}
            for t in range(12)]
    check_cfg = sync_config.CheckConfig(sample_min_percent=5, sample_min_pages=10)
    sampled = sync_engine.sample_pages_per_module(meta, check_cfg)
    assert len(sampled) == 10                    # max(ceil(0.6), 10) → 10


def test_check_sampled_all_pass_writes_sample_report(
        engine_root, cfg):
    _seed_module_pages(engine_root, "UserGuide", 12)

    code = sync_engine.check_dataset_sampled(cfg)

    assert code == 0
    sample_txt = (engine_root / "data" / "selfcheck-sample-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: ALL PASS" in sample_txt
    # 机器检查 100% + 转换质量只抽 10 页
    assert "--- 转换质量代理（按模块抽样 10 页） ---" in sample_txt
    assert "M1" in sample_txt and "C1" in sample_txt


def test_check_sampled_module_filter_only_audits_that_module(engine_root, cfg):
    """--module M 只审计该模块：其他模块的分块不得让 C2/C7 误失败。"""
    _seed_module_pages(engine_root, "Accounting", 2)
    _seed_module_pages(engine_root, "UserGuide", 12)

    code = sync_engine.check_dataset_sampled(cfg, module="Accounting")

    assert code == 0
    sample_txt = (engine_root / "data" / "selfcheck-sample-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: ALL PASS" in sample_txt
    assert "[FAIL]" not in sample_txt
    # 只抽样 Accounting 模块的 2 页（不涉及 UserGuide）
    assert "--- 转换质量代理（按模块抽样 2 页） ---" in sample_txt
    assert "en-us/UserGuide/ModulePage" not in sample_txt


def test_check_sampled_skips_conversion_without_raw(engine_root, cfg):
    """data/raw 不入库：fresh clone 缺 raw 时转换质量标 SKIP，不假失败。"""
    _seed_module_pages(engine_root, "UserGuide", 2)
    # 模拟 fresh clone：raw 目录不存在（gitignore，不入库）
    for raw_file in (engine_root / "data" / "raw").glob("**/*.htm"):
        raw_file.unlink()

    code = sync_engine.check_dataset_sampled(cfg)

    assert code == 0
    sample_txt = (engine_root / "data" / "selfcheck-sample-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: ALL PASS" in sample_txt
    assert "[SKIP] Q1" in sample_txt
    assert "跳过转换质量校验" in sample_txt


def test_check_sampled_gate_failure_exits_nonzero_with_list(
        engine_root, cfg, capsys):
    tid = _seed_module_pages(engine_root, "UserGuide", 12)[0]
    clean_file = (engine_root / "data" / "clean" /
                  (tid.replace("/", "_") + ".md"))
    clean_file.write_text(clean_file.read_text(encoding="utf-8") + "�",
                          encoding="utf-8")

    code = sync_engine.check_dataset_sampled(cfg)

    assert code == 1
    err = capsys.readouterr().err
    assert "自检失败清单" in err
    sample_txt = (engine_root / "data" / "selfcheck-sample-results.txt").read_text(
        encoding="utf-8")
    assert "RESULT: HAS FAILURES" in sample_txt
    assert "[FAIL] Q3" in sample_txt


def test_check_sampled_unknown_module_exits_nonzero(engine_root, cfg, capsys):
    _seed_module_pages(engine_root, "UserGuide", 2)
    code = sync_engine.check_dataset_sampled(cfg, module="NoSuchModule")
    assert code == 1
    assert "NoSuchModule" in capsys.readouterr().err


def test_check_sampled_empty_dataset_exits_nonzero(engine_root, cfg, capsys):
    code = sync_engine.check_dataset_sampled(cfg)
    assert code == 1
    assert "数据集为空" in capsys.readouterr().err


# ---------- AC5 CLI 抽查模板与失败清单 ----------

def test_parse_check_mode():
    ns = run_sync.parse_args(["--mode", "check"])
    assert ns.mode == "check"
    assert ns.module is None
    ns = run_sync.parse_args(["--mode", "check", "--module", "UserGuide"])
    assert ns.module == "UserGuide"


def test_check_mode_rejects_fetch_only_args(capsys):
    for argv in (["--mode", "check", "--url", "https://x.test/a.htm"],
                 ["--mode", "check", "--limit", "3"],
                 ["--mode", "check", "--rate", "2"],
                 ["--mode", "check", "--dry-run"]):
        with pytest.raises(SystemExit) as exc:
            run_sync.parse_args(argv)
        assert exc.value.code != 0
        assert "check" in capsys.readouterr().err


def test_main_check_delegates_to_sampled_engine(monkeypatch):
    calls = []

    def fake_check(cfg, module=None):
        calls.append(module)
        return 0

    monkeypatch.setattr(run_sync.sync_engine, "check_dataset_sampled", fake_check)
    code = run_sync.main(["--mode", "check", "--module", "UserGuide"])
    assert code == 0
    assert calls == ["UserGuide"]


def test_module_rejected_outside_check_mode(capsys):
    for argv in (["--mode", "incremental", "--module", "UserGuide"],
                 ["--mode", "reconcile", "--module", "UserGuide"]):
        with pytest.raises(SystemExit) as exc:
            run_sync.parse_args(argv)
        assert exc.value.code != 0
        assert "--module" in capsys.readouterr().err
