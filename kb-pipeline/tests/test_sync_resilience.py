"""失败恢复与停止条件引擎单元测试（票 #19，AC1–AC4）。

覆盖：429/5xx 指数退避（读配置、封顶后放弃）、连续失败停止、单轮错误率停止、
错误报告（失败 URL 与原因）、阈值停止后续跑从状态恢复。
"""
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

URL_A = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
         "UserGuide/GettingStarted/GettingStarted.htm")
URL_B = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
         "UserGuide/GettingStarted/MobileClient.htm")
URL_C = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
         "UserGuide/GettingStarted/MonitorBI.htm")


def _topic_url(i: int) -> str:
    return (f"https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
            f"Area/Module/Topic{i}.htm")


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


FIXTURE_HTML = """<html><head><title>Topic</title></head>
<body><div id="contentBody"><h1>Topic</h1>
<p>Welcome to Monitor ERP G5.</p>
<h2>Overview</h2><p>First part.</p>
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
        return URL_A

    def read(self):
        return self._body


class FlakyNetwork:
    """增量场景网络：HEAD/GET 失败按 URL 提供状态序列，耗尽后成功。

    head_fails / get_fails：{url: [status, ...]} 依次抛出的 HTTP 状态；
    unchanged：{url: etag}，HEAD 条件请求命中该 etag 时返回 304。
    """

    def __init__(self, head_fails=None, get_fails=None, unchanged=None):
        self.head_fails = {k: list(v) for k, v in (head_fails or {}).items()}
        self.get_fails = {k: list(v) for k, v in (get_fails or {}).items()}
        self.unchanged = unchanged or {}
        self.calls: dict[str, list[str]] = {"head": [], "get": []}
        self.sleeps: list[float] = []

    def _fail_next(self, seq):
        return seq.pop(0) if seq else None

    def head(self, url, headers, timeout=30):
        self.calls["head"].append(url)
        status = self._fail_next(self.head_fails.get(url, []))
        if status is not None:
            raise urllib.error.HTTPError(url, status, "Fail", {}, None)
        if headers.get("If-None-Match") == self.unchanged.get(url):
            raise urllib.error.HTTPError(url, 304, "Not Modified", {}, None)
        return FakeResponse(etag=self.unchanged.get(url) or '"server"')

    def get(self, url, headers, timeout=30):
        self.calls["get"].append(url)
        status = self._fail_next(self.get_fails.get(url, []))
        if status is not None:
            raise urllib.error.HTTPError(url, status, "Fail", {}, None)
        return FakeResponse(FIXTURE_HTML.encode("utf-8"), etag='"server"')


class ReconcileNetwork:
    """全量对账场景网络：sitemap/en/zh HEAD + 主题 GET；get_fails 提供 GET 失败序列。"""

    def __init__(self, sitemap: str, en_ok, zh_ok=(), get_fails=None,
                 head_fails=None):
        self.sitemap = sitemap
        self.en_ok = set(en_ok)
        self.zh_ok = set(zh_ok)
        self.get_fails = {k: list(v) for k, v in (get_fails or {}).items()}
        self.head_fails = {k: list(v) for k, v in (head_fails or {}).items()}
        self.calls: dict[str, list[str]] = {"head": [], "get": []}
        self.sleeps: list[float] = []

    def _error(self, url, status):
        raise urllib.error.HTTPError(url, status, "Fail", {}, None)

    def get(self, url, headers, timeout=30):
        self.calls["get"].append(url)
        if self.get_fails.get(url):
            return self._error(url, self.get_fails[url].pop(0))
        if url == SITEMAP_URL:
            return FakeResponse(self.sitemap.encode("utf-8"), etag='"sitemap"')
        if url in self.en_ok or url in self.zh_ok:
            return FakeResponse(FIXTURE_HTML.encode("utf-8"), etag='"en"')
        return self._error(url, 404)

    def head(self, url, headers, timeout=30):
        self.calls["head"].append(url)
        if self.head_fails.get(url):
            return self._error(url, self.head_fails[url].pop(0))
        ok = url in self.en_ok if "/en-us/" in url else url in self.zh_ok
        if ok:
            return FakeResponse(etag='"h"')
        return self._error(url, 404)


@pytest.fixture
def engine_root(tmp_path, monkeypatch):
    monkeypatch.setattr(sync_engine, "ROOT", tmp_path)
    return tmp_path


@pytest.fixture
def cfg():
    return sync_config.load_sync_config()


def _patch_net(monkeypatch, net):
    """接入网络替身并记录 backoff 退避延迟（time.sleep 由 net.sleeps 记录）。"""
    monkeypatch.setattr(P, "_open", net.get)
    monkeypatch.setattr(P, "_head", net.head)
    monkeypatch.setattr(sync_engine, "_pace", lambda rate: None)
    monkeypatch.setattr(sync_engine.time, "sleep", net.sleeps.append)


def _seed_state(root: Path, records: list[dict]) -> sync_state.SyncState:
    st = sync_state.SyncState(root / "state" / "sync-state.jsonl")
    st.load()
    for fields in records:
        st.record(**fields)
    return st


def _ok_record(url: str, i: int) -> dict:
    return {
        "url": url, "language": "en-us", "etag": f'"{i}"',
        "lastmod": "2026-05-21T08:18:54Z", "content_hash": "0" * 64,
        "status": "ok", "last_ok_at": "2026-08-02T00:00:00Z",
    }


def _jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in
            path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _report(root: Path) -> list[dict]:
    return _jsonl(root / "state" / "sync-error-report.jsonl")


def _failures(root: Path) -> list[dict]:
    return [r for r in _report(root) if r.get("type") == "failure"]


def _summary(root: Path) -> dict:
    return next(r for r in _report(root) if r.get("type") == "summary")


def test_incremental_head_429_backoff_then_unchanged(engine_root, cfg,
                                                     monkeypatch):
    """AC1：条件 HEAD 429 按 1s→2s 退避重试后 304，不触发 GET、产物与状态不变。"""
    net = FlakyNetwork(head_fails={URL_A: [429, 429]}, unchanged={URL_A: '"0"'})
    _patch_net(monkeypatch, net)
    _seed_state(engine_root, [_ok_record(URL_A, 0)])

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert net.calls["head"] == [URL_A, URL_A, URL_A]
    assert net.sleeps == [1.0, 2.0]          # base=1：1s → 2s
    assert net.calls["get"] == []
    assert _jsonl(engine_root / "state" / "sync-state.jsonl")[0]["status"] == "ok"


def test_backoff_reads_config_base_and_cap(engine_root, cfg, monkeypatch):
    """AC1：退避延迟读配置（base=2,max=10 → 2s→4s）。"""
    cfg2 = replace(cfg, backoff=sync_config.BackoffConfig(base_seconds=2,
                                                          max_seconds=10))
    net = FlakyNetwork(head_fails={URL_A: [429, 429]}, unchanged={URL_A: '"0"'})
    _patch_net(monkeypatch, net)
    _seed_state(engine_root, [_ok_record(URL_A, 0)])

    code = sync_engine.incremental_sync(None, None, cfg2, rate=2.0)

    assert code == 0
    assert net.sleeps == [2.0, 4.0]


def test_incremental_get_500_backoff_then_success(engine_root, cfg, monkeypatch):
    """AC1：变化页 GET 500 按 1s→2s 退避重试后成功，状态与产物正常入库。"""
    net = FlakyNetwork(get_fails={URL_A: [500, 500]})
    _patch_net(monkeypatch, net)
    _seed_state(engine_root, [_ok_record(URL_A, 0)])

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert net.calls["get"] == [URL_A, URL_A, URL_A]
    assert net.sleeps == [1.0, 2.0]
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    assert state[0]["status"] == "ok"
    assert (engine_root / "data" / "clean" /
            "en-us_UserGuide_GettingStarted_GettingStarted.md").exists()


def test_backoff_gives_up_after_cap_and_marks_error(engine_root, cfg, monkeypatch):
    """AC1：退避延迟到 max 上限仍失败 → 放弃重试、记 error；单 URL 100% 错误率停止。"""
    net = FlakyNetwork(head_fails={URL_A: [429] * 10})
    _patch_net(monkeypatch, net)
    _seed_state(engine_root, [_ok_record(URL_A, 0)])

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 1
    assert net.calls["head"] == [URL_A] * 7        # 初试 + 6 次退避重试
    assert net.sleeps == [1.0, 2.0, 4.0, 8.0, 16.0, 32.0]  # 封顶 60，下一跳 60 不再重试
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    assert state[0]["status"] == "error"


def test_incremental_consecutive_failure_stop_then_resume(
        engine_root, cfg, monkeypatch, capsys):
    """AC2/AC4：连续失败达阈值 → 停止、非零退出、报告含失败 URL；续跑从状态恢复。"""
    cfg2 = replace(cfg, stop_conditions=sync_config.StopConditions(
        consecutive_failures=2, error_rate_percent=10))
    net = FlakyNetwork(head_fails={URL_A: [500] * 10, URL_B: [500] * 10})
    _patch_net(monkeypatch, net)
    _seed_state(engine_root, [_ok_record(URL_A, 0), _ok_record(URL_B, 1),
                              _ok_record(URL_C, 2)])

    code = sync_engine.incremental_sync(None, None, cfg2, rate=2.0)

    assert code == 1
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    by_url = {r["url"]: r for r in state}
    assert by_url[URL_A]["status"] == "error"
    assert by_url[URL_B]["status"] == "error"
    assert by_url[URL_C]["status"] == "ok"         # 停止在 B，C 未触达
    assert [r["url"] for r in _failures(engine_root)] == [URL_A, URL_B]
    assert all("HTTP 500" in r["reason"] for r in _failures(engine_root))
    assert _summary(engine_root)["stopped"].startswith("连续失败")
    assert "连续失败" in capsys.readouterr().err

    # 续跑：网络恢复，A/B/C 全部重新入库，之前已完成状态不重复抓取
    net.head_fails = {}
    net.get_fails = {}
    code2 = sync_engine.incremental_sync(None, None, cfg2, rate=2.0)

    assert code2 == 0
    state = _jsonl(engine_root / "state" / "sync-state.jsonl")
    assert all(r["status"] == "ok" for r in state)
    assert len(net.calls["get"]) >= 3


def test_incremental_error_rate_stop_writes_report(engine_root, cfg,
                                                   monkeypatch, capsys):
    """AC2/AC3：单轮错误率 >10%（2/11=18.2%）→ 停止、非零退出、报告含 URL+原因。"""
    urls = [URL_A, URL_B] + [_topic_url(i) for i in range(9)]   # 11 条
    net = FlakyNetwork(head_fails={URL_A: [500] * 10, URL_B: [500] * 10},
                       unchanged={u: f'"{i}"' for i, u in enumerate(urls)})
    _patch_net(monkeypatch, net)
    _seed_state(engine_root, [_ok_record(u, i) for i, u in enumerate(urls)])

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 1
    err = capsys.readouterr().err
    assert "> 10.0%" in err
    assert {r["url"] for r in _failures(engine_root)} == {URL_A, URL_B}
    assert all("HTTP 500" in r["reason"] for r in _failures(engine_root))
    summary = _summary(engine_root)
    assert summary["failed"] == 2
    assert summary["total"] == 11


def test_incremental_normal_completion_writes_report_with_failures(
        engine_root, cfg, monkeypatch):
    """AC3：错误率 ≤10% 的轮正常结束也写报告（失败 URL 供恢复排查），但退出码 0。"""
    urls = [URL_A] + [_topic_url(i) for i in range(9)]          # 10 条，1 失败 = 10%
    net = FlakyNetwork(head_fails={URL_A: [500] * 10},
                       unchanged={u: f'"{i}"' for i, u in enumerate(urls)})
    _patch_net(monkeypatch, net)
    _seed_state(engine_root, [_ok_record(u, i) for i, u in enumerate(urls)])

    code = sync_engine.incremental_sync(None, None, cfg, rate=2.0)

    assert code == 0
    assert len(_failures(engine_root)) == 1
    assert _failures(engine_root)[0]["url"] == URL_A
    assert _summary(engine_root)["stopped"] == "completed"


def test_reconcile_sitemap_429_backoff_then_success(engine_root, cfg,
                                                    monkeypatch):
    """AC1：全量对账 sitemap 下载 429 按配置退避重试后成功。"""
    urls = [_topic_url(0)]
    net = ReconcileNetwork(sitemap=sitemap_xml(urls), en_ok=urls,
                           zh_ok=set(), get_fails={SITEMAP_URL: [429]})
    _patch_net(monkeypatch, net)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)

    code = sync_engine.reconcile_manifest(limit=1, cfg=cfg, rate=5.0)

    assert code == 0
    assert net.sleeps == [1.0]
    meta = _jsonl(engine_root / "data" / "metadata.jsonl")
    assert len(meta) == 1


def test_reconcile_head_phase_consecutive_failures_stop_writes_report(
        engine_root, cfg, monkeypatch, capsys):
    """AC2/AC3：en HEAD 探测阶段连续失败达阈值 → 停止、非零退出、报告含失败 URL。"""
    urls = [_topic_url(i) for i in range(6)]
    net = ReconcileNetwork(sitemap=sitemap_xml(urls), en_ok=urls[5:],
                           zh_ok=set(),
                           head_fails={u: [500] * 10 for u in urls[:5]})
    _patch_net(monkeypatch, net)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)

    code = sync_engine.reconcile_manifest(limit=None, cfg=cfg, rate=5.0)

    assert code == 1
    assert {r["url"] for r in _failures(engine_root)} == set(urls[:5])
    assert all("HTTP 500" in r["reason"] for r in _failures(engine_root))
    assert "连续失败" in capsys.readouterr().err
    assert not (engine_root / "data" / "metadata.jsonl").exists()


def test_reconcile_pipeline_consecutive_failures_stop_writes_report(
        engine_root, cfg, monkeypatch, capsys):
    """AC2/AC3：完整管道连续 GET 失败达阈值 → 停止、非零退出、报告含失败 URL。"""
    cfg2 = replace(cfg, stop_conditions=sync_config.StopConditions(
        consecutive_failures=2, error_rate_percent=10))
    urls = [_topic_url(i) for i in range(4)]
    net = ReconcileNetwork(sitemap=sitemap_xml(urls), en_ok=urls, zh_ok=set(),
                           get_fails={urls[0]: [500] * 10, urls[1]: [500] * 10})
    _patch_net(monkeypatch, net)
    monkeypatch.setattr(sync_manifest, "SITEMAP_URL", SITEMAP_URL)

    code = sync_engine.reconcile_manifest(limit=4, cfg=cfg2, rate=5.0)

    assert code == 1
    assert {r["url"] for r in _failures(engine_root)} == {urls[0], urls[1]}
    assert all("HTTP 500" in r["reason"] for r in _failures(engine_root))
    assert "连续失败" in capsys.readouterr().err
    # en 主题 2 个失败即停，后 2 个与 zh 镜像未处理
    meta = _jsonl(engine_root / "data" / "metadata.jsonl")
    assert len(meta) == 0
