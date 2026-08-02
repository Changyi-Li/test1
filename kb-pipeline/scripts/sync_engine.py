"""单 URL 全量对账引擎（票 #15，垂直切片）。

`--mode reconcile --url <主题 URL>` 的单页端到端：抓取（配置 UA + 限速）→
清洗 → 元数据 → 分块 → 机器自检。原始 HTML 与响应头写入 data/raw/
（gitignore，不入库）；清洗 Markdown、13 字段元数据、14 字段分块与自检结果
写入 data/ 入库产物；同步状态写入 state/sync-state.jsonl（gitignore）。

重复运行幂等：元数据按 id、分块按 topic_id 覆盖更新，其他主题的既有产物保留。
镜像配对（paired_topic_id）属于清单驱动对账（后续票），本引擎不做镜像扫描。
"""
from __future__ import annotations

import json
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import pipeline as P
import sync_config
import sync_state

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE_REL = "state/sync-state.jsonl"

LANGS = ("en-us", "zh-cn")
_TOPIC_URL_RE = re.compile(
    r"^/(.+?)/(en-us|zh-cn)/Content/Topics/(.+)/([^/]+\.htm)$"
)


def state_path() -> Path:
    return ROOT / STATE_FILE_REL


def headers_path() -> Path:
    return ROOT / "data" / "raw" / "headers.json"


def clean_dir() -> Path:
    return ROOT / "data" / "clean"


def meta_path() -> Path:
    return ROOT / "data" / "metadata.jsonl"


def chunks_path() -> Path:
    return ROOT / "data" / "chunks.jsonl"


def check_path() -> Path:
    return ROOT / "data" / "selfcheck-results.txt"


@dataclass(frozen=True)
class TopicTarget:
    """从单个主题 URL 推导出的抓取/入库定位信息。"""
    url: str
    site: str
    source: str
    language: str
    topic_path: str
    page: str
    topic_id: str


def parse_topic_url(url: str) -> TopicTarget:
    """从主题 URL 推导站点/语言/主题路径/页面；非法 URL 抛 ValueError。"""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError(f"主题 URL 必须是 http(s) 绝对 URL，得到 {url!r}")
    m = _TOPIC_URL_RE.match(parsed.path)
    if m is None:
        raise ValueError(
            "主题 URL 必须形如 <站点>/<语言>/Content/Topics/<主题路径>/<页面>.htm，"
            f"得到 {url!r}"
        )
    site_segment, language, topic_path, page = m.groups()
    return TopicTarget(
        url=url,
        site=f"{parsed.scheme}://{parsed.netloc}/{site_segment}",
        source=parsed.netloc,
        language=language,
        topic_path=topic_path,
        page=page,
        topic_id=f"{language}/{topic_path}/{Path(page).stem}",
    )


def _pace(rate: float) -> None:
    """抓取后按 1/rate 秒间隔限速（试点自约束 1–2 req/s 口径的参数化）。"""
    time.sleep(1.0 / rate)


def _fetch(target: TopicTarget, user_agent: str, timeout: int = 30):
    """按配置 UA 抓取单页；返回 (原始字节或 None, 响应头信息)。"""
    manifest = P.Manifest(
        site=target.site,
        topic_path=target.topic_path,
        source=target.source,
        topics=(),
        zh_probes=(),
        headers={"User-Agent": user_agent},
        fetch_sleep=0.0,
    )
    headers_rec: dict = {}
    raw = P.probe(manifest, target.url, headers_rec, timeout=timeout)
    return raw, headers_rec.get(target.url, {})


def _load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: JSONL 行不是合法 JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line_no}: JSONL 行必须是对象")
        rows.append(row)
    return rows


def _save_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
        encoding="utf-8",
    )


def _load_headers() -> dict:
    path = headers_path()
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _save_headers(headers: dict) -> None:
    path = headers_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(headers, ensure_ascii=False, indent=2), encoding="utf-8")


def build_metadata(target: TopicTarget, info: dict, md: str, raw_html: str) -> dict:
    """13 字段元数据行（规格 §4.1）；单 URL 模式 paired_topic_id 为 null。"""
    return {
        "id": target.topic_id,
        "title": P.extract_title(md, raw_html),
        "url": target.url,
        "source": target.source,
        "version": P.extract_version(raw_html),
        "language": target.language,
        "topic_path": target.topic_path,
        "quality": "canonical" if target.language == "en-us" else "reference",
        "lastmod": info.get("lastmod"),
        "etag": info.get("etag"),
        "content_hash": P.sha256_hex(md),
        "images": re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md),
        "paired_topic_id": None,
    }


def build_chunks(meta: dict, md: str) -> list[dict]:
    """14 字段分块行（规格 §4.2）；单 URL 模式不做镜像配对。"""
    rows = []
    for order, chunk in enumerate(P.chunk_markdown(md)):
        rows.append({
            "chunk_id": f"{meta['id']}::{order}",
            "topic_id": meta["id"],
            "order": order,
            "title": meta["title"],
            "heading_path": [p["text"] for p in chunk["path"]],
            "content": chunk["content"],
            "language": meta["language"],
            "quality": meta["quality"],
            "url": meta["url"],
            "topic_path": meta["topic_path"],
            "images": re.findall(r"!\[[^\]]*\]\(([^)]+)\)", chunk["content"]),
            "paired_chunk_id": None,
            "char_count": len(chunk["content"]),
            "token_estimate": P.est_tokens(chunk["content"]),
        })
    return rows


def upsert_metadata(meta: dict) -> None:
    """按 id 覆盖该主题的元数据行；保留其他主题的行与既有镜像配对。"""
    rows = _load_jsonl(meta_path())
    existing = next((r for r in rows if r.get("id") == meta["id"]), None)
    if existing is not None and existing.get("paired_topic_id") is not None:
        meta = {**meta, "paired_topic_id": existing["paired_topic_id"]}
    rows = [r for r in rows if r.get("id") != meta["id"]]
    rows.append(meta)
    rows.sort(key=lambda r: (r["language"], r["id"]))
    _save_jsonl(meta_path(), rows)


def upsert_chunks(topic_id: str, chunks: list[dict]) -> None:
    """按 topic_id 覆盖该主题的分块；内容未变的块沿用既有镜像配对。"""
    rows = _load_jsonl(chunks_path())
    old = [c for c in rows if c.get("topic_id") == topic_id]
    for chunk in chunks:
        same = next((o for o in old
                     if o.get("chunk_id") == chunk["chunk_id"]
                     and o.get("content") == chunk["content"]), None)
        if same is not None:
            chunk["paired_chunk_id"] = same.get("paired_chunk_id")
    rows = [c for c in rows if c.get("topic_id") != topic_id]
    rows.extend(chunks)
    rows.sort(key=lambda c: (c["topic_id"], c["order"]))
    _save_jsonl(chunks_path(), rows)


def _is_topic_url(url: str, language: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        return False
    return bool(re.search(rf"/{re.escape(language)}/Content/Topics/.+\.htm$",
                          parsed.path))


def selfcheck_single(meta: dict, chunks: list[dict]) -> bool:
    """单页机器自检：元数据完整性 + 分块完整性；配对检查标记 SKIP。"""
    lines: list[str] = []
    ok = True

    def report(name: str, passed: bool, detail: str = "") -> None:
        nonlocal ok
        ok = ok and passed
        lines.append(f"[{'PASS' if passed else 'FAIL'}] {name}"
                     + (f" — {detail}" if detail else ""))

    topic_id = meta["id"]
    language = meta["language"]
    id_re = re.compile(rf"^({'|'.join(LANGS)})/(?:[A-Za-z0-9_-]+/)*[A-Za-z0-9_-]+$")

    # ---- 元数据完整性 ----
    report("M1 元数据字段集合 = 13 字段", set(meta) == P.EXPECTED_FIELDS_META)
    report("M2 id 符合稳定格式", bool(id_re.fullmatch(topic_id)))
    report("M3 url 规范且与 language 一致", _is_topic_url(meta["url"], language))
    report("M4 language 枚举且与 id 前缀一致",
           language in LANGS and topic_id.startswith(language + "/"))
    report("M5 quality 枚举（en→canonical, zh→reference）",
           (language == "en-us" and meta["quality"] == "canonical")
           or (language == "zh-cn" and meta["quality"] == "reference"))
    lastmod = meta.get("lastmod")
    report("M6 version/lastmod/etag 非空且 lastmod 为 ISO8601 UTC",
           bool(meta.get("version")) and bool(meta.get("etag")) and bool(lastmod)
           and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
                                 lastmod or "")))
    images = meta.get("images")
    report("M7 images 为绝对 URL 数组",
           isinstance(images, list)
           and all(str(x).startswith("http") for x in images))
    clean_file = clean_dir() / (topic_id.replace("/", "_") + ".md")
    hash_ok = clean_file.exists() and P.sha256_hex(
        clean_file.read_text(encoding="utf-8")) == meta.get("content_hash")
    report("M8 content_hash 重算一致", hash_ok)
    lines.append("[SKIP] M9 镜像配对（单 URL 对账不做镜像扫描，清单驱动票覆盖）")

    # ---- 分块完整性 ----
    report("C0 至少一个分块（空页不能通过自检）", len(chunks) > 0)
    report("C1 分块字段集合 = 14 字段",
           all(set(c) == P.EXPECTED_FIELDS_CHUNK for c in chunks))
    report("C2 chunk_id 格式与 topic_id 引用",
           all(c["chunk_id"] == f"{c['topic_id']}::{c['order']}"
               and c["topic_id"] == topic_id for c in chunks))
    report("C3 order 0 起连续",
           [c["order"] for c in chunks] == list(range(len(chunks))))
    report("C4 heading_path 非空字符串列表",
           all(isinstance(c["heading_path"], list) and c["heading_path"]
               and all(isinstance(x, str) and x for x in c["heading_path"])
               for c in chunks))
    report("C5 content 非空", all(bool(c["content"]) for c in chunks))
    report("C6 char_count 与内容一致",
           all(c["char_count"] == len(c["content"]) for c in chunks))
    report("C7 块上下文字段与主题清单一致",
           all(c["language"] == language and c["quality"] == meta["quality"]
               and c["url"] == meta["url"] and c["topic_path"] == meta["topic_path"]
               for c in chunks))
    report("C8 token_estimate 为正整数且 ≤ 1200 硬上限",
           all(isinstance(c["token_estimate"], int)
               and 0 < c["token_estimate"] <= 1200 for c in chunks))
    lines.append("[SKIP] C9 中文块镜像配对（单 URL 对账不做镜像扫描，清单驱动票覆盖）")
    report("C10 块 images 与内容内图片一致",
           all(c["images"] == re.findall(r"!\[[^\]]*\]\(([^)]+)\)", c["content"])
               for c in chunks))

    lines.append(f"\nRESULT: {'ALL PASS' if ok else 'HAS FAILURES'}\n")
    path = check_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return ok


def reconcile_single_url(url: str, cfg: sync_config.SyncConfig, rate: float) -> int:
    """单主题 URL 端到端全量对账；返回进程退出码（0=成功且自检全 PASS）。"""
    try:
        target = parse_topic_url(url)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    print(f"== 抓取: {target.url}")
    raw, info = _fetch(target, cfg.user_agent)
    _pace(rate)

    state = sync_state.SyncState(state_path())
    state.load()
    if raw is None:
        state.mark_error(target.url, language=target.language)
        print(f"错误: 抓取失败（status={info.get('status')}），同步状态已记 error",
              file=sys.stderr)
        return 1

    # 原始 HTML 与响应头落盘（data/raw/ 为 gitignore，不入库）
    raw_file = ROOT / "data" / "raw" / target.language / target.page
    raw_file.parent.mkdir(parents=True, exist_ok=True)
    raw_file.write_bytes(raw)
    headers = _load_headers()
    headers[target.url] = info
    _save_headers(headers)
    print(f"  原始 HTML -> {raw_file.relative_to(ROOT)}")
    print(f"  响应头 -> {headers_path().relative_to(ROOT)}")

    raw_html = raw.decode("utf-8", errors="replace")
    md = P.clean_markdown(raw_html, target.url)
    clean_file = clean_dir() / (target.topic_id.replace("/", "_") + ".md")
    clean_dir().mkdir(parents=True, exist_ok=True)
    clean_file.write_text(md, encoding="utf-8")
    print(f"== 清洗: {len(md)} 字符 -> {clean_file.relative_to(ROOT)}")

    meta = build_metadata(target, info, md, raw_html)
    upsert_metadata(meta)
    print(f"== 元数据: {meta['id']} -> {meta_path().relative_to(ROOT)}")

    chunks = build_chunks(meta, md)
    upsert_chunks(meta["id"], chunks)
    print(f"== 分块: {len(chunks)} 块 -> {chunks_path().relative_to(ROOT)}")

    ok = selfcheck_single(meta, chunks)
    print(f"== 自检: {'ALL PASS' if ok else 'HAS FAILURES'} -> "
          f"{check_path().relative_to(ROOT)}")

    if ok:
        state.mark_ok(target.url, language=target.language,
                      etag=info.get("etag"), lastmod=info.get("lastmod"),
                      content_hash=meta["content_hash"])
        print(f"== 同步状态: ok（etag={info.get('etag')!r}, "
              f"lastmod={info.get('lastmod')!r}, "
              f"content_hash={meta['content_hash'][:12]}…）")
    else:
        state.mark_error(target.url, language=target.language,
                         etag=info.get("etag"), lastmod=info.get("lastmod"),
                         content_hash=meta["content_hash"])
        print("== 同步状态: error（自检未通过，产物保留供检查，不记 ok）",
              file=sys.stderr)
    return 0 if ok else 1



