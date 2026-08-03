"""kb-pipeline 共享库：抓取、清洗、元数据、分块、自检（按主题清单参数化）。

清洗管线复用了 research/html-conversion/scripts/compare.py 的 custom_convert
（BS4 + #contentBody 提取），并补充：图片相对路径解析为绝对 URL。

站点、主题路径与主题清单由 Manifest 传入，同一个共享库既可驱动试点
（pilot_manifest()）也可驱动生产清单（后续票由 sitemap 生成）。
"""
from __future__ import annotations

import hashlib
import pathlib
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import timezone
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup


@dataclass(frozen=True)
class Manifest:
    """一次同步的主题清单：站点、主题路径、主题列表与抓取参数。"""
    site: str
    topic_path: str
    source: str
    topics: tuple[dict, ...]
    zh_probes: tuple[str, ...]
    headers: dict[str, str]
    fetch_sleep: float = 1.0


def pilot_manifest() -> Manifest:
    """试点清单：与历史硬编码行为完全一致（URL/UA/间隔/主题）。"""
    return PILOT_MANIFEST


PILOT_MANIFEST = Manifest(
    site="https://help.monitorerp.cn/CN-MONITOR_G5",
    topic_path="UserGuide/GettingStarted",
    source="help.monitorerp.cn",
    topics=(
        {"lang": "en-us", "page": "GettingStarted.htm", "zh_page": "GettingStarted.htm"},
        {"lang": "en-us", "page": "MobileClient.htm", "zh_page": "WebClient.htm"},
        {"lang": "en-us", "page": "MonitorBI.htm", "zh_page": "MonitorBI.htm"},
    ),
    zh_probes=("GettingStarted.htm", "WebClient.htm", "MobileClient.htm", "MonitorBI.htm"),
    headers={"User-Agent": "MonitorERP-KB-Pilot/0.1 (https://github.com/Changyi-Li/test1)"},
    fetch_sleep=1.0,  # 无 robots.txt，自约束 1–2 req/s
)

# ---------- schema（规格 §4.1/§4.2，试点与生产共用） ----------

EXPECTED_FIELDS_META = {
    "id", "title", "url", "source", "version", "language", "topic_path",
    "quality", "lastmod", "etag", "content_hash", "images", "paired_topic_id",
}
EXPECTED_FIELDS_CHUNK = {
    "chunk_id", "topic_id", "order", "title", "heading_path", "content",
    "language", "quality", "url", "topic_path", "images", "paired_chunk_id",
    "char_count", "token_estimate",
}

NOISE_PATTERNS = [
    r"Powered by MadCap",
    r"Online help for version",
    r"Skip to",
    r"Cookies",
    r"data-mc-",
    r"You are here",
]
CALLOUT_CLASSES = re.compile(r"note|warning|tip|important|alert|caution", re.I)

# 转换质量第 3 项（无截断/乱码）的乱码签名：UTF-8 字节流被按 Latin-1 解码时的
# 典型产物（Ã©=é、â€œ="、Â\xa0=不换行空格），正常 UTF-8 内容不会命中。
MOJIBAKE_PATTERNS = [
    re.compile(r"Ã[\x80-\xbf]"),
    re.compile(r"Â[\xa0\x80-\xbf]"),
    re.compile(r"â€[\x80-\xbf]"),
]


def garbled_markdown_problems(md: str) -> list[str]:
    """检查清洗后 Markdown 的截断/乱码信号（规格 §6 转换质量第 3 项）。

    乱码：U+FFFD 替换字符、UTF-8 被按 Latin-1 解码的典型签名、控制字符；
    截断：代码围栏不平衡、文档结尾出现未闭合的链接/图片。返回问题清单，空=通过。
    """
    problems: list[str] = []
    if "�" in md:
        problems.append("含 U+FFFD 替换字符（解码失败）")
    for pat in MOJIBAKE_PATTERNS:
        if pat.search(md):
            problems.append("疑似乱码签名（UTF-8 被按 Latin-1 解码）")
    ctrl = sorted({c for c in md if ord(c) < 32 and c not in "\n\r\t"})
    if ctrl:
        problems.append(f"含控制字符 {''.join(ctrl)[:5]!r}")
    if md.count("```") % 2:
        problems.append("代码围栏不平衡（``` 为奇数）")
    if re.search(r"!?\[[^\]]*\]\([^)]*$", md, re.M):
        problems.append("文档结尾存在未闭合的链接/图片")
    return problems


def topic_url(manifest: Manifest, lang: str, page: str) -> str:
    return f"{manifest.site}/{lang}/Content/Topics/{manifest.topic_path}/{page}"


def topic_id(manifest: Manifest, lang: str, page: str) -> str:
    return f"{lang}/{manifest.topic_path}/{pathlib.Path(page).stem}"


def est_tokens(text: str) -> int:
    """cl100k_base 近似：CJK 每字约 1 token，其余按 ~4 字符/token。仅监控用。"""
    cjk = sum(1 for c in text if "\u4e00" <= c <= "\u9fff")
    other = len(text) - cjk
    return int(cjk + other / 4 + 0.5)


def normalize_heading_text(text: str | None) -> str:
    """标题文本比较用归一化：去掉全部空白（raw 侧 get_text 会在上标 sup 周围
    插入空白，如 'm 3 '，与清洗器的 'm3' 等价；Q2 比较前两侧统一去空白）。"""
    return re.sub(r"\s+", "", text or "")


# ---------- 抓取 ----------

def _head(url: str, headers: dict, timeout: int = 30):
    req = urllib.request.Request(url, headers=headers, method="HEAD")
    return urllib.request.urlopen(req, timeout=timeout)

def _open(url: str, headers: dict, timeout: int = 30):
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req, timeout=timeout)


def probe(manifest: Manifest, url: str, headers_rec: dict, timeout: int = 30):
    """探测 URL；200 返回字节，否则返回 None 并记录状态。"""
    info: dict[str, object] = {"url": url, "status": None, "final_url": None, "lastmod": None, "etag": None}
    try:
        with _open(url, manifest.headers, timeout) as resp:
            info["status"] = resp.status
            info["final_url"] = resp.geturl()
            info["lastmod"] = _iso_lastmod(resp.headers.get("Last-Modified"))
            info["etag"] = resp.headers.get("ETag")
            headers_rec[url] = info
            return resp.read()
    except urllib.error.HTTPError as exc:
        info["status"] = exc.code
        headers_rec[url] = info
        return None
    except Exception as exc:  # 网络错误也算失败，记入 headers
        info["status"] = f"ERROR: {exc}"
        headers_rec[url] = info
        return None


def _iso_lastmod(value):
    if not value:
        return None
    try:
        dt = parsedate_to_datetime(value)
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return value


def probe_head(manifest: Manifest, url: str, headers_rec: dict, timeout: int = 30):
    """HEAD 探测 URL；返回信息记录（status/final_url/lastmod/etag），不读 body。"""
    info: dict[str, object] = {
        "url": url, "status": None, "final_url": None, "lastmod": None, "etag": None,
    }
    try:
        with _head(url, manifest.headers, timeout) as resp:
            info["status"] = resp.status
            info["final_url"] = resp.geturl()
            info["lastmod"] = _iso_lastmod(resp.headers.get("Last-Modified"))
            info["etag"] = resp.headers.get("ETag")
            headers_rec[url] = info
            return info
    except urllib.error.HTTPError as exc:
        info["status"] = exc.code
        headers_rec[url] = info
        return info
    except Exception as exc:  # 网络错误也算失败，记入 headers
        info["status"] = f"ERROR: {exc}"
        headers_rec[url] = info
        return info

# ---------- 清洗（复用 custom_convert，图片 URL 绝对化） ----------

def inline_md(el, base_url):
    out = []
    for child in el.children:
        if getattr(child, "name", None) is None:
            out.append(child.string or "")
            continue
        name = child.name.lower()
        if name == "br":
            out.append("\n")
        elif name == "img":
            cls = " ".join(child.get("class", [])) or ""
            if "MCDropDown_Image_Icon" in cls or "MCHelpControl_Image_Icon" in cls:
                continue
            alt = child.get("alt", "") or ""
            src = child.get("src", "") or ""
            out.append(f"![{alt}]({urljoin(base_url, src)})")
        elif name == "a":
            href = child.get("href", "") or ""
            if href and not href.startswith("#") and not href.startswith("javascript:"):
                inner = inline_md(child, base_url)
                if inner:
                    out.append(f"[{inner}]({href})")
                    continue
            txt = re.sub(r"\s+", " ", child.get_text(" ", strip=True))
            if txt and href and not href.startswith("#") and not href.startswith("javascript:"):
                out.append(f"[{txt}]({href})")
            elif txt:
                out.append(txt)
        elif name == "code":
            out.append("`" + (child.get_text() or "") + "`")
        elif name in ("span", "strong", "em", "b", "i", "u", "sup", "sub", "font"):
            out.append(inline_md(child, base_url))
        else:
            inner = inline_md(child, base_url)
            if inner:
                out.append(inner)
            else:
                out.append(re.sub(r"\s+", " ", child.get_text(" ", strip=True)))
    text = "".join(out)
    return re.sub(r"[ \t]+", " ", text).strip()


def table_md(table, base_url):
    rows = []
    for tr in table.find_all("tr"):
        cells = [inline_md(c, base_url) or " " for c in tr.find_all(["th", "td"])]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |"]
    lines.append("|" + "---|" * ncols)
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


_BLOCK_TAGS = {
    "p", "ul", "ol", "table", "pre", "blockquote", "dl",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "div", "section", "article", "figure", "main",
}


def _li_has_block(li) -> bool:
    return any(getattr(c, "name", None) and c.name.lower() in _BLOCK_TAGS
               for c in li.children)


def _inline_only(el, base_url: str) -> str:
    """渲染元素的直接内联子内容，跳过块级子元素（块级交给 walk 顶层展开）。"""
    out = []
    for child in el.children:
        if getattr(child, "name", None) is None:
            out.append(child.string or "")
            continue
        if child.name.lower() in _BLOCK_TAGS:
            continue
        out.append(inline_md(child, base_url))
    return "".join(out)


def clean_markdown(raw_html: str, base_url: str) -> str:
    soup = BeautifulSoup(raw_html, "lxml")
    body = soup.select_one("#contentBody") or soup.select_one(".body-container") or soup.body
    lines = []

    def walk(el):
        for child in el.children:
            if getattr(child, "name", None) is None:
                continue
            name = child.name.lower()
            if name in ("script", "style", "nav", "header", "footer", "aside"):
                continue
            if re.search(r"breadcrumb|nocontent", " ".join(child.get("class", [])) or "", re.I):
                continue
            if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = int(name[1])
                txt = inline_md(child, base_url) or " "
                lines.append("\n" + "#" * level + " " + txt)
            elif name == "p":
                t = inline_md(child, base_url)
                if re.match(r"^You are here:$", t):
                    continue
                if t:
                    cls = " ".join(child.get("class", [])) or ""
                    if CALLOUT_CLASSES.search(cls):
                        lines.append("> " + t)
                    else:
                        lines.append(t)
            elif name == "ul":
                for li in child.find_all("li", recursive=False):
                    if _li_has_block(li):
                        head = _inline_only(li, base_url)
                        if head:
                            lines.append("- " + head)
                        walk(li)
                    else:
                        t = inline_md(li, base_url)
                        if t:
                            lines.append("- " + t)
            elif name == "ol":
                for i, li in enumerate(child.find_all("li", recursive=False), 1):
                    if _li_has_block(li):
                        head = _inline_only(li, base_url)
                        if head:
                            lines.append(f"{i}. " + head)
                        walk(li)
                    else:
                        t = inline_md(li, base_url)
                        if t:
                            lines.append(f"{i}. " + t)
            elif name == "table":
                t = table_md(child, base_url)
                if t:
                    lines.append(t)
            elif name == "pre":
                lines.append("```\n" + (child.get_text() or "") + "\n```")
            elif name == "img":
                alt = child.get("alt", "") or ""
                src = child.get("src", "") or ""
                lines.append(f"![{alt}]({urljoin(base_url, src)})")
            elif name == "blockquote":
                t = inline_md(child, base_url)
                if t:
                    lines.append("> " + t)
            elif name in ("div", "section", "article", "figure", "span", "main", "a", "li"):
                cls = " ".join(child.get("class", [])) or ""
                if CALLOUT_CLASSES.search(cls):
                    t = inline_md(child, base_url)
                    if t:
                        lines.append("> " + t)
                else:
                    has_block = any(
                        getattr(c, "name", None)
                        and c.name.lower() in ("p", "ul", "ol", "table", "pre",
                                               "blockquote", "h1", "h2", "h3",
                                               "h4", "h5", "h6", "div",
                                               "section", "article", "figure",
                                               "main")
                        for c in child.children
                    )
                    if has_block:
                        walk(child)
                    else:
                        t = inline_md(child, base_url)
                        if t:
                            lines.append(t)
            elif name == "dl":
                for dt in child.find_all("dt", recursive=False):
                    lines.append("**" + inline_md(dt, base_url) + "**")
                for dd in child.find_all("dd", recursive=False):
                    t = inline_md(dd, base_url)
                    if t:
                        lines.append(": " + t)

    walk(body)
    text = "\n".join(x for x in lines if x)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_version(raw_html: str) -> str:
    m = re.search(r"(?:Online help for version|版本)\s*([\d.]+)", raw_html)
    return m.group(1) if m else "25.8"


def extract_title(md: str, raw_html: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.M)
    if m:
        return m.group(1).strip()
    soup = BeautifulSoup(raw_html, "lxml")
    t = soup.find("title")
    return (t.get_text(strip=True) if t else "") or ""


def raw_body_stats(raw_html: str):
    """统计 #contentBody 内的标题/链接/图片/提示框/表格/代码，供质量代理检查。"""
    soup = BeautifulSoup(raw_html, "lxml")
    body: Any = soup.select_one("#contentBody") or soup.select_one(".body-container") or soup.body
    headings = []
    for h in body.find_all(re.compile(r"^h[1-6]$")):
        headings.append((int(h.name[1]), re.sub(r"\s+", " ", h.get_text(" ", strip=True))))
    links = [a.get("href", "") for a in body.find_all("a")
             if a.get("href") and not a.get("href", "").startswith("#")
             and not a.get("href", "").startswith("javascript:")]
    images = [img.get("src", "") for img in body.find_all("img")
              if img.get("src")
              and "MCDropDown_Image_Icon" not in " ".join(img.get("class", []))
              and "MCHelpControl_Image_Icon" not in " ".join(img.get("class", []))]
    callouts = [el for el in body.find_all(["p", "div"])
                if CALLOUT_CLASSES.search(" ".join(el.get("class", [])) or "")]
    tables = len(body.find_all("table"))
    pre = len(body.find_all("pre"))
    codes = len(body.find_all("code"))
    return {"headings": headings, "links": links, "images": images,
            "callouts": len(callouts), "tables": tables, "pre": pre, "code": codes}


def _count_md_tables(md: str) -> int:
    """统计 Markdown 表格**块**数（连续的 | 起始行算一个表格）。

    旧的按行计数把表格的每一行都当一张表，与 raw_body_stats 的
    `<table>` 元素计数对不上（一张 6 行表 → raw=1 md=6）。"""
    count = 0
    in_table = False
    for ln in md.splitlines():
        if ln.lstrip().startswith("|"):
            if not in_table:
                count += 1
                in_table = True
        else:
            in_table = False
    return count


def md_stats(md: str):
    heading_lines = [(len(m.group(1)), m.group(2).strip())
                     for m in re.finditer(r"^(#{1,6})\s+(.+)$", md, re.M)]
    # 正文链接只统计 [text](url)，(?<!!) 排除图片语法 ![alt](url)
    links = re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", md)
    images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md)
    return {"headings": heading_lines, "links": links, "images": images,
            "blockquote_lines": len(re.findall(r"^>\s?", md, re.M)),
            "tables": _count_md_tables(md),
            "code_fences": len(re.findall(r"^```", md, re.M))}


# ---------- 分块 ----------

def _is_list_line(ln):
    s = ln.strip()
    return bool(re.match(r"^[-*]\s", s) or re.match(r"^\d+\.\s", s))


def _is_quote_line(ln):
    return ln.strip().startswith(">")


def split_oversize_unit(heading_line, body_lines, cap):
    """超过硬上限的单元：按空行分块后合并，避免切在列表/提示框中间。"""
    blocks = []
    cur = []
    in_fence = False
    for ln in body_lines:
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            cur.append(ln)
            continue
        if not in_fence and not ln.strip():
            if cur:
                blocks.append(cur)
                cur = []
            continue
        cur.append(ln)
    if cur:
        blocks.append(cur)

    merged = []
    for b in blocks:
        if merged and (_is_list_line(merged[-1][-1]) or _is_quote_line(merged[-1][-1])):
            merged[-1].append("")
            merged[-1].extend(b)
        else:
            merged.append(b)

    parts = []
    part = []
    for b in merged:
        if part and est_tokens("\n".join(part + [""] + b)) > cap:
            parts.append(part)
            part = []
        part.extend(b)
        part.append("")
    if part:
        parts.append(part)
    return [[heading_line] + p[:-1] for p in parts if p]


def chunk_markdown(md: str, cap: int = 1200):
    """按 h2 子树切块；h3 及更小标题跟随父 h2；超限先按 h3、再按段落二次切。"""
    lines = md.splitlines()
    heads = []
    for _i, _ln in enumerate(lines):
        _m = re.match(r"^(#{1,6})\s+(.+)$", _ln)
        if _m:
            heads.append((_i, len(_m.group(1)), _m.group(2).strip()))

    if not heads:
        return [{"path": [], "pos": (), "content": "\n".join(lines).strip()}]

    occurrence: dict[int, int] = {}

    def next_idx(level):
        occurrence[level] = occurrence.get(level, 0) + 1
        return occurrence[level] - 1

    units: list[dict[str, Any]] = []
    for k, (idx, level, text) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        body = lines[idx + 1:end]
        units.append({"level": level, "text": text, "idx": next_idx(level), "body": body})

    stack: list[dict[str, Any]] = []
    for u in units:
        while stack and stack[-1]["level"] >= u["level"]:
            stack.pop()
        u["path"] = stack + [{"level": u["level"], "text": u["text"], "idx": u["idx"]}]
        stack.append(u)

    prefix = lines[: heads[0][0]] if heads[0][0] > 0 else []
    have_h2 = any(u["level"] == 2 for u in units)

    chunks: list[dict[str, Any]] = []
    current: Any = None

    def close_current():
        nonlocal current
        if current is not None:
            content = "\n".join(current["content"]).strip()
            if content:
                chunks.append({"path": current["path"], "pos": current["pos"],
                               "content": content})
        current = None

    def start(u) -> dict[str, Any]:
        path = [{"level": p["level"], "text": p["text"]} for p in u["path"]]
        pos = tuple(p["idx"] for p in u["path"])
        return {"path": path, "pos": pos,
                "content": ["#" * u["level"] + " " + u["text"]]}

    for u in units:
        unit_text = "#" * u["level"] + " " + u["text"] + "\n" + "\n".join(u["body"])
        if current is None:
            current = start(u)
            if prefix:
                current["content"] = prefix + [""] + current["content"]
        elif u["level"] <= 2:
            close_current()
            current = start(u)
        else:
            if est_tokens("\n".join(current["content"] + [unit_text])) > cap:
                close_current()
                current = start(u)
            else:
                current["content"].append("#" * u["level"] + " " + u["text"])
        current["content"].extend(u["body"])

    close_current()

    final = []
    for c in chunks:
        if est_tokens(c["content"]) > cap and len(c["path"]) >= 1:
            head_line = "#" * c["path"][-1]["level"] + " " + c["path"][-1]["text"]
            body_lines = c["content"].splitlines()
            if body_lines and body_lines[0].startswith("#"):
                body_lines = body_lines[1:]
            for part in split_oversize_unit(head_line, body_lines, cap):
                final.append({"path": c["path"], "pos": c["pos"],
                              "content": "\n".join(part)})
        else:
            final.append(c)

    return final


