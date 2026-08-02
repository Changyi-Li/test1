"""共享库按主题清单参数化的单元测试（票 #14，AC2）。"""
from __future__ import annotations

import sys
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
