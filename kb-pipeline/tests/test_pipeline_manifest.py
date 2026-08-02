"""共享库按主题清单参数化的单元测试（票 #14，AC2）。"""
from __future__ import annotations

import sys
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pipeline as P


def test_topic_url_and_id_follow_manifest():
    m = P.Manifest(
        site="https://example.test/ROOT",
        topic_path="Prod/Topics",
        source="example.test",
        topics=(),
        zh_probes=(),
        headers={"User-Agent": "Prod-Bot/1.0"},
        fetch_sleep=0.5,
    )
    assert P.topic_url(m, "en-us", "Page.htm") == (
        "https://example.test/ROOT/en-us/Content/Topics/Prod/Topics/Page.htm"
    )
    assert P.topic_id(m, "zh-cn", "Page.htm") == "zh-cn/Prod/Topics/Page"


def test_pilot_manifest_preserves_pilot_behavior():
    m = P.pilot_manifest()
    assert P.topic_url(m, "en-us", "GettingStarted.htm") == (
        "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
        "UserGuide/GettingStarted/GettingStarted.htm"
    )
    assert P.topic_id(m, "en-us", "GettingStarted.htm") == (
        "en-us/UserGuide/GettingStarted/GettingStarted"
    )
    assert m.source == "help.monitorerp.cn"
    assert m.topic_path == "UserGuide/GettingStarted"
    assert m.fetch_sleep == 1.0
    assert m.headers["User-Agent"].startswith("MonitorERP-KB-Pilot")
    assert [t["page"] for t in m.topics] == [
        "GettingStarted.htm", "MobileClient.htm", "MonitorBI.htm",
    ]
    assert list(m.zh_probes) == [
        "GettingStarted.htm", "WebClient.htm", "MobileClient.htm", "MonitorBI.htm",
    ]

class _FakeHeadResponse:
    status = 200
    headers = {"Last-Modified": "Thu, 21 May 2026 08:18:54 GMT", "ETag": '"h1"'}

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def geturl(self):
        return "https://help.monitorerp.cn/final"

    def read(self):
        raise AssertionError("HEAD 请求不应读取 body")


def test_probe_head_records_200_headers_without_body(monkeypatch):
    called = []

    def fake_head(url, headers, timeout=30):
        called.append(url)
        return _FakeHeadResponse()

    monkeypatch.setattr(P, "_head", fake_head)
    manifest = P.Manifest(
        site="https://example.test/ROOT",
        topic_path="Prod/Topics",
        source="example.test",
        topics=(),
        zh_probes=(),
        headers={"User-Agent": "Prod-Bot/1.0"},
        fetch_sleep=0.5,
    )
    url = "https://help.monitorerp.cn/x.htm"
    headers_rec: dict = {}
    info = P.probe_head(manifest, url, headers_rec)

    assert info["status"] == 200
    assert info["etag"] == '"h1"'
    assert info["lastmod"] == "2026-05-21T08:18:54Z"
    assert info["final_url"] == "https://help.monitorerp.cn/final"
    assert headers_rec[url] is info
    assert called == [url]


def test_probe_head_records_404(monkeypatch):
    def fake_head(url, headers, timeout=30):
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)

    monkeypatch.setattr(P, "_head", fake_head)
    manifest = P.Manifest(
        site="https://example.test/ROOT",
        topic_path="Prod/Topics",
        source="example.test",
        topics=(),
        zh_probes=(),
        headers={"User-Agent": "Prod-Bot/1.0"},
        fetch_sleep=0.5,
    )
    url = "https://help.monitorerp.cn/missing.htm"
    headers_rec: dict = {}
    info = P.probe_head(manifest, url, headers_rec)

    assert info["status"] == 404
    assert headers_rec[url]["status"] == 404
