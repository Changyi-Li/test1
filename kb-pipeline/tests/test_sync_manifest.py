"""sitemap → en 清单与 zh 镜像推导单元测试（票 #16，AC1/AC3）。"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import sync_manifest as SM


SITEMAP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Content/Topics/Accounting/AccrualAccounting/AccrualAccounting.htm</loc></url>
  <url><loc>https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Content/Topics/Accounting/AccrualAccounting/AccrualAccountingList/bSettings.htm</loc></url>
  <url><loc>https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Content/Home.htm</loc></url>
  <url><loc>https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Content/Resources/Images/logo.png</loc></url>
  <url><loc>https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm</loc></url>
  <url><loc>https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm</loc></url>
  <url><loc>https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm#section</loc></url>
</urlset>
"""


def test_fix_sitemap_url_replaces_host_and_removes_double_content():
    assert SM.fix_sitemap_url(
        "https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Content/Topics/A/B.htm"
    ) == "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/A/B.htm"
    # 已是单层 Content 的 URL 只换主机，不再改路径
    assert SM.fix_sitemap_url(
        "https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Topics/A/B.htm"
    ) == "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/A/B.htm"


def test_build_en_manifest_filters_dedupes_and_normalizes():
    urls = SM.build_en_manifest(SITEMAP_XML)
    assert urls == [
        "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
        "Accounting/AccrualAccounting/AccrualAccounting.htm",
        "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
        "Accounting/AccrualAccounting/AccrualAccountingList/bSettings.htm",
        "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
        "UserGuide/GettingStarted/GettingStarted.htm",
    ]


def test_zh_url_for_replaces_language_segment():
    en = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
          "UserGuide/GettingStarted/GettingStarted.htm")
    assert SM.zh_url_for(en) == (
        "https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
        "UserGuide/GettingStarted/GettingStarted.htm"
    )


def test_en_topic_rel_path_and_renamed_page_resolution():
    en = ("https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/"
          "UserGuide/GettingStarted/MobileClient.htm")
    assert SM.en_topic_rel_path(en) == "UserGuide/GettingStarted/MobileClient"
    zh = SM.zh_url_for(en)
    assert SM.zh_url_for_page(zh, "WebClient.htm") == (
        "https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/"
        "UserGuide/GettingStarted/WebClient.htm"
    )
