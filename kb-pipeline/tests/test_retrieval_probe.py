"""检索实测探针单元测试（导入工具，接缝 7 的纯函数部分）。"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import retrieval_probe

FIXTURE = """| # | 中文问题 | 预期主题（en） | 预期主题（zh，如有） | 关键事实点 |
| --- | --- | --- | --- | --- |
| 1 | 我刚开始接触 Monitor ERP，应该从哪里了解系统？ | UserGuide/GettingStarted/GettingStarted | 同路径 zh | 面向新用户 |
| 5 | Monitor Mobile 叫什么？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | 重命名 |
| 11 | Monitor BI 是什么？ | UserGuide/GettingStarted/MonitorBI | — | zh 404 |
"""


def test_parse_questions_skips_header_and_resolves_shorthand():
    questions = retrieval_probe.parse_questions(FIXTURE)
    assert [q["number"] for q in questions] == [1, 5, 11]
    assert questions[0]["question"].startswith("我刚开始接触")
    assert questions[0]["expected_en"] == "UserGuide/GettingStarted/GettingStarted"
    # 「同路径 zh」解析为与 en 相同的路径
    assert questions[0]["expected_zh"] == "UserGuide/GettingStarted/GettingStarted"
    assert questions[1]["expected_zh"] == "UserGuide/GettingStarted/WebClient"
    assert questions[2]["expected_zh"] is None


def test_hit_expected_uses_full_path_and_language():
    en = [{"full_path": "UserGuide/GettingStarted/GettingStarted",
           "language": "en-us"}]
    zh = [{"full_path": "UserGuide/GettingStarted/GettingStarted",
           "language": "zh-cn"}]
    # en 期望必须由 en-us 文档满足
    assert retrieval_probe.hit_expected(
        en, "UserGuide/GettingStarted/GettingStarted", "en-us")
    assert not retrieval_probe.hit_expected(
        zh, "UserGuide/GettingStarted/GettingStarted", "en-us")
    # zh 期望由 zh-cn 文档满足
    assert retrieval_probe.hit_expected(
        zh, "UserGuide/GettingStarted/GettingStarted", "zh-cn")
    assert not retrieval_probe.hit_expected(
        en, "UserGuide/GettingStarted/GettingStarted", "zh-cn")
    assert not retrieval_probe.hit_expected(
        en, "UserGuide/GettingStarted/MonitorBI", "en-us")
    assert retrieval_probe.hit_expected(en, None, "en-us")


def test_full_path_strips_language_prefix():
    data = retrieval_probe.load_topic_map()
    meta = data["en-us_UserGuide_GettingStarted_GettingStarted.md"]
    topic_id = meta["id"]
    assert topic_id.split("/", 1)[1] == \
        "UserGuide/GettingStarted/GettingStarted"


def test_load_topic_map_real_metadata():
    topic_map = retrieval_probe.load_topic_map()
    assert "en-us_UserGuide_GettingStarted_GettingStarted.md" in topic_map
    assert (topic_map["en-us_UserGuide_GettingStarted_GettingStarted.md"]
            ["topic_path"] == "UserGuide/GettingStarted")
