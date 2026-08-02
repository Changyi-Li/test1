"""sitemap → 权威 en 清单与 zh 镜像 URL 推导（规格 §5.1/§5.2，票 #16）。

每轮全量对账重新下载 en-us/sitemap.xml；条目需要修复（help.monitorerp.com →
help.monitorerp.cn、去掉 Content/Content/ 双写层），随后过滤 /Topics/*.htm、
规范化 URL 去重，得到权威 en 清单。zh 镜像由同路径替换语言段推导，
已知重命名映射（config/sync.json 的 renames）在同路径 404 时提供替代页面。
"""
from __future__ import annotations

import xml.etree.ElementTree as ET
from urllib.parse import urlsplit, urlunsplit

import pipeline as P

SITEMAP_URL = "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/sitemap.xml"

TOPIC_SEGMENT = "/Content/Topics/"


def fix_sitemap_url(url: str) -> str:
    """修复 sitemap 条目：主机换 help.monitorerp.cn，去掉 Content/Content/ 双写层。"""
    return url.replace("help.monitorerp.com", "help.monitorerp.cn") \
              .replace("/Content/Content/", "/Content/")


def normalize_url(url: str) -> str:
    """规范化：去 fragment/query/尾斜杠；主机小写（路径大小写原样保留）。"""
    parts = urlsplit(url)
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def _is_topic_url(url: str) -> bool:
    parsed = urlsplit(url)
    return parsed.path.endswith(".htm") and TOPIC_SEGMENT in parsed.path


def build_en_manifest(xml_text: str) -> list[str]:
    """sitemap XML → 修复/过滤/去重后的权威 en 主题 URL 列表（保持出现顺序）。"""
    root = ET.fromstring(xml_text)
    seen: set[str] = set()
    out: list[str] = []
    for el in root.iter():
        if el.tag.rsplit("}", 1)[-1] != "loc" or not el.text:
            continue
        fixed = fix_sitemap_url(el.text.strip())
        if not _is_topic_url(fixed):
            continue
        normalized = normalize_url(fixed)
        if normalized in seen:
            continue
        seen.add(normalized)
        out.append(normalized)
    return out


def zh_url_for(en_url: str) -> str:
    """同路径 zh 镜像 URL：语言段 en-us → zh-cn。"""
    return en_url.replace("/en-us/Content/Topics/", "/zh-cn/Content/Topics/", 1)


def zh_url_for_page(zh_url: str, page: str) -> str:
    """把 zh 同路径 URL 的页面文件名替换为重命名映射给出的 zh 页面。"""
    head, _sep, _old = zh_url.rpartition("/")
    return f"{head}/{page}"


def en_topic_rel_path(en_url: str) -> str:
    """Content/Topics/ 之后的相对主题路径（去语言前缀与 .htm）。"""
    after = urlsplit(en_url).path.split(TOPIC_SEGMENT, 1)[1]
    return after[:-4] if after.endswith(".htm") else after


def download_sitemap(user_agent: str, timeout: int = 30):
    """下载 en-us sitemap；返回 (原始字节或 None, 响应头信息)。"""
    manifest = P.Manifest(
        site="https://help.monitorerp.cn/CN-MONITOR_G5",
        topic_path="",
        source="help.monitorerp.cn",
        topics=(),
        zh_probes=(),
        headers={"User-Agent": user_agent},
        fetch_sleep=0.0,
    )
    headers_rec: dict = {}
    raw = P.probe(manifest, SITEMAP_URL, headers_rec, timeout=timeout)
    return raw, headers_rec.get(SITEMAP_URL, {})
