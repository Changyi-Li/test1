"""同步引擎：增量同步（票 #17）、单 URL 对账（票 #15）与清单驱动全量对账（票 #16）。

`--mode incremental [--dry-run]`：基于同步状态对已知主题发起条件请求
（ETag 优先 If-None-Match，Last-Modified 兜底 If-Modified-Since），
304/指纹一致不重写任何产物、状态保持；变化页只对该主题 GET 全文并即时落盘，
中断后可从断点续跑，重跑幂等。

`--mode reconcile --url <主题 URL>`：单页端到端（抓取→清洗→元数据→分块→自检），
镜像配对检查标记 SKIP。

`--mode reconcile [--limit N]`：从 en-us sitemap 生成权威 en 清单（修复规则、
Topics/*.htm 过滤、规范化去重、HEAD 可达性校验），同轮扫描 zh 同路径镜像
（含已知重命名映射），对样本主题走完整管道，把未翻译/重命名/删除例外写进
例外表，最后跑全量数据集自检（M1–M10/C1–C10，含镜像配对）。

原始 HTML 与响应头写入 data/raw/（gitignore，不入库）；清洗 Markdown、13 字段
元数据、14 字段分块、例外表与自检结果写入 data/ 入库产物；同步状态写入
state/sync-state.jsonl（gitignore）。重复运行幂等。

删除检测（票 #18）：曾 ok 的页面 200→404 或从 sitemap 消失时，同步状态留墓碑
（deleted_at + 最后指纹）、例外表记 deleted，并清除该页数据集旧产物与镜像配对；
页面重现时墓碑清除、例外 resolved、重新入库。全量对账与增量同步两种模式均覆盖。
"""
from __future__ import annotations

import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import urlparse

import pipeline as P
import sync_config
import sync_manifest
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


def exceptions_path() -> Path:
    return ROOT / "data" / "exceptions.jsonl"


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


@dataclass(frozen=True)
class MirrorResult:
    """一个 en 主题的 zh 镜像扫描结果。"""
    en_url: str
    en_id: str
    zh_url: str | None      # 解析后的 zh 页面 URL（同路径或重命名），None=无镜像
    zh_id: str | None
    kind: str               # paired | renamed | untranslated


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


def _topic_id_of_url(url: str) -> str:
    m = _TOPIC_URL_RE.match(urlparse(url).path)
    if m is None:
        raise ValueError(f"不是主题 URL: {url!r}")
    _site, language, topic_path, page = m.groups()
    return f"{language}/{topic_path}/{Path(page).stem}"


def _pace(rate: float) -> None:
    """抓取后按 1/rate 秒间隔限速（试点自约束 1–2 req/s 口径的参数化）。"""
    time.sleep(1.0 / rate)


def _fetch(target: TopicTarget, user_agent: str, headers_rec: dict,
           timeout: int = 30):
    """按配置 UA 抓取单页；响应头信息写入调用方共享的 headers_rec。"""
    manifest = P.Manifest(
        site=target.site,
        topic_path=target.topic_path,
        source=target.source,
        topics=(),
        zh_probes=(),
        headers={"User-Agent": user_agent},
        fetch_sleep=0.0,
    )
    raw = P.probe(manifest, target.url, headers_rec, timeout=timeout)
    return raw, headers_rec.get(target.url, {})


def _headers_manifest(user_agent: str,
                       extra_headers: dict[str, str] | None = None) -> P.Manifest:
    """只携带 UA（及可选条件请求头）的抓取参数（HEAD 探测用，站点字段不参与请求）。"""
    headers = {"User-Agent": user_agent}
    if extra_headers:
        headers.update(extra_headers)
    return P.Manifest(
        site="",
        topic_path="",
        source="",
        topics=(),
        zh_probes=(),
        headers=headers,
        fetch_sleep=0.0,
    )


def _http_if_modified_since(lastmod: str) -> str:
    """状态里的 ISO 时间 → HTTP 条件请求头需要的 IMF-fixdate（GMT）。"""
    try:
        dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
    except ValueError:
        return lastmod
    return format_datetime(dt, usegmt=True)


def _conditional_headers(record: dict | None) -> dict[str, str]:
    """按同步状态构造条件请求头：ETag 优先，Last-Modified 兜底。"""
    if record is None:
        return {}
    etag = record.get("etag")
    if etag:
        return {"If-None-Match": str(etag)}
    lastmod = record.get("lastmod")
    if lastmod:
        return {"If-Modified-Since": _http_if_modified_since(str(lastmod))}
    return {}


def _is_unchanged(info: dict, record: dict | None) -> bool:
    """304 或 HEAD 指纹与状态一致 → 未变化（ETag 优先，Last-Modified 兜底）。"""
    if info.get("status") == 304:
        return True
    if record is None or info.get("status") != 200:
        return False
    etag = info.get("etag")
    if etag is not None and record.get("etag") is not None:
        return etag == record.get("etag")
    lastmod = info.get("lastmod")
    return (lastmod is not None and record.get("lastmod") is not None
            and lastmod == record.get("lastmod"))


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


def _merge_headers(headers_rec: dict) -> None:
    headers = _load_headers()
    headers.update(headers_rec)
    _save_headers(headers)


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


def _load_exceptions() -> list[dict]:
    return _load_jsonl(exceptions_path())


def _save_exceptions(rows: list[dict]) -> None:
    _save_jsonl(exceptions_path(), rows)


def upsert_exception(row: dict) -> None:
    """按 (id, type) 幂等覆盖写入例外表；保留首次发现时间与既有 resolved 状态。

    重跑全量对账时同一结构例外不再刷新 discovered_at，保证重跑产物逐字节一致；
    其他既有例外（如试点首版两条）原样保留。
    """
    rows = _load_exceptions()
    existing = next(
        (r for r in rows
         if r.get("id") == row.get("id") and r.get("type") == row.get("type")),
        None,
    )
    if existing is not None:
        row = {
            **row,
            "discovered_at": existing.get("discovered_at", row.get("discovered_at")),
            "resolved": existing.get("resolved", row.get("resolved")),
        }
        rows = [r for r in rows if r is not existing]
    rows.append(row)
    rows.sort(key=lambda r: (r["type"], r["id"]))
    _save_exceptions(rows)


def _resolve_exception(topic_id: str, kind: str) -> None:
    """页面重现/镜像恢复时把进行中的结构例外标记 resolved（无变化不写盘）。"""
    rows = _load_exceptions()
    changed = False
    for row in rows:
        if (row.get("id") == topic_id and row.get("type") == kind
                and not row.get("resolved")):
            row["resolved"] = True
            changed = True
    if changed:
        _save_exceptions(rows)


def _remove_topic_artifacts(topic_id: str) -> None:
    """从数据集中清除该主题全部旧产物，并解除指向它的镜像配对。"""
    clean_file = clean_dir() / (topic_id.replace("/", "_") + ".md")
    if clean_file.exists():
        clean_file.unlink()
    raw_file = ROOT / "data" / "raw" / topic_id.split("/", 1)[0] / (
        topic_id.rsplit("/", 1)[-1] + ".htm")
    if raw_file.exists():
        raw_file.unlink()

    meta_rows = _load_jsonl(meta_path())
    kept: list[dict] = []
    changed = False
    for row in meta_rows:
        if row.get("id") == topic_id:
            changed = True
            continue
        if row.get("paired_topic_id") == topic_id:
            row["paired_topic_id"] = None
            changed = True
        kept.append(row)
    if changed:
        _save_jsonl(meta_path(), kept)

    chunk_rows = _load_jsonl(chunks_path())
    kept_chunks: list[dict] = []
    chunk_changed = False
    unpaired = {r["id"] for r in kept if r.get("paired_topic_id") is None}
    for chunk in chunk_rows:
        if chunk.get("topic_id") == topic_id:
            chunk_changed = True
            continue
        if chunk.get("language") == "en-us":
            if chunk.get("paired_chunk_id") is not None:
                chunk["paired_chunk_id"] = None
                chunk_changed = True
        elif (chunk.get("topic_id") in unpaired
              and chunk.get("paired_chunk_id") is not None):
            chunk["paired_chunk_id"] = None
            chunk_changed = True
        kept_chunks.append(chunk)
    if chunk_changed:
        _save_jsonl(chunks_path(), kept_chunks)


def _delete_topic(url: str, language: str | None,
                  state: sync_state.SyncState, detail: str) -> None:
    """200→404 或从清单消失：状态留墓碑（deleted_at + 最后指纹）、
    例外表记 deleted、清除该主题数据集产物并解除对方配对。同一事件幂等。"""
    try:
        topic_id = _topic_id_of_url(url)
    except ValueError:
        topic_id = None
    prev = state.get(url)
    was_deleted = prev is not None and prev.get("status") == "deleted"
    state.mark_deleted(url, language=language)
    print(f"== 已删除: {url}（墓碑：deleted_at + 最后指纹）")
    if topic_id is None:
        return
    _remove_topic_artifacts(topic_id)
    rows = _load_exceptions()
    has_open = any(r.get("id") == topic_id and r.get("type") == "deleted"
                   and not r.get("resolved") for r in rows)
    if was_deleted and has_open:
        return  # 同一删除事件仍在进行：保留首次 discovered_at，产物逐字节一致
    rows = [r for r in rows
            if not (r.get("id") == topic_id and r.get("type") == "deleted")]
    rows.append({
        "id": topic_id,
        "type": "deleted",
        "detail": detail,
        "discovered_at": sync_state.utc_now_iso(),
        "resolved": False,
    })
    rows.sort(key=lambda r: (r["type"], r["id"]))
    _save_exceptions(rows)


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


def selfcheck_dataset(expected_pairs: dict[str, str | None]) -> bool:
    """全量数据集自检（规格 §6）：M1–M10 + C1–C10 + Q1–Q6 转换质量代理。

    expected_pairs：本轮镜像扫描得到的 {topic_id: paired_topic_id 或 None}，
    用于校验配对与例外覆盖。
    """
    meta_rows = _load_jsonl(meta_path())
    chunk_rows = _load_jsonl(chunks_path())
    exc_rows = _load_exceptions()
    ids = {r["id"] for r in meta_rows}
    lines: list[str] = []
    ok = True

    def report(name: str, passed: bool, detail: str = "") -> None:
        nonlocal ok
        ok = ok and passed
        lines.append(f"[{'PASS' if passed else 'FAIL'}] {name}"
                     + (f" — {detail}" if detail else ""))

    id_re = re.compile(rf"^({'|'.join(LANGS)})/(?:[A-Za-z0-9_-]+/)*[A-Za-z0-9_-]+$")
    url_re = re.compile(
        r"^https?://[^/]+(?:/[^/]+)?/(en-us|zh-cn)/Content/Topics/.+\.htm$")

    # ---- 元数据完整性 ----
    report("M1 元数据字段集合 = 13 字段",
           all(set(r) == P.EXPECTED_FIELDS_META for r in meta_rows),
           f"{len(meta_rows)} rows")
    dups = [r["id"] for r in meta_rows
            if sum(1 for x in meta_rows if x["id"] == r["id"]) > 1]
    report("M2 id 唯一且符合稳定格式",
           not dups and all(re.fullmatch(id_re, r["id"]) for r in meta_rows),
           f"dup={dups}")
    report("M3 url 规范且与 language 一致",
           all(re.fullmatch(url_re, r["url"])
               and ("/" + r["language"] + "/Content/Topics/") in r["url"]
               for r in meta_rows))
    report("M4 language 枚举且与 id 前缀一致",
           all(r["language"] in LANGS
               and r["id"].startswith(r["language"] + "/") for r in meta_rows))
    report("M5 quality 枚举（en→canonical, zh→reference）",
           all((r["language"] == "en-us" and r["quality"] == "canonical")
               or (r["language"] == "zh-cn" and r["quality"] == "reference")
               for r in meta_rows))
    report("M6 version/lastmod/etag 非空且 lastmod 为 ISO8601 UTC",
           all(r["version"] and r["etag"] and r["lastmod"]
               and re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
                                r["lastmod"] or "")
               for r in meta_rows))
    report("M7 images 为绝对 URL 数组",
           all(isinstance(r["images"], list)
               and all(str(x).startswith("http") for x in r["images"])
               for r in meta_rows))
    hash_fail = []
    for r in meta_rows:
        cf = clean_dir() / (r["id"].replace("/", "_") + ".md")
        if not cf.exists() or P.sha256_hex(
                cf.read_text(encoding="utf-8")) != r["content_hash"]:
            hash_fail.append(r["id"])
    report("M8 content_hash 重算一致", not hash_fail, f"mismatch={hash_fail}")

    pair_fail: list[str] = []
    by_id = {r["id"]: r for r in meta_rows}
    for r in meta_rows:
        p = r.get("paired_topic_id")
        if p is not None:
            partner = by_id.get(p)
            if partner is None:
                pair_fail.append(f"{r['id']}->悬空 {p}")
            else:
                if partner.get("paired_topic_id") != r["id"]:
                    pair_fail.append(f"{r['id']}->{p} 非互逆")
                if partner["language"] == r["language"]:
                    pair_fail.append(f"{r['id']}->{p} 同语言配对")
        if r["id"] in expected_pairs and expected_pairs[r["id"]] != p:
            pair_fail.append(f"{r['id']}: 期望 {expected_pairs[r['id']]} 实际 {p}")
    report("M9 镜像配对互逆且与镜像扫描一致", not pair_fail,
           "; ".join(pair_fail[:8]))

    exc_keys = {(e["id"], e["type"]) for e in exc_rows}
    missing_exc = []
    for tid, expected_partner in expected_pairs.items():
        if expected_partner is None and tid.startswith("en-us/"):
            zh_id = "zh-cn/" + tid.split("/", 1)[1]
            if (zh_id, "untranslated") not in exc_keys:
                missing_exc.append(f"{zh_id} 缺 untranslated 例外")
    report("M10 缺失镜像的 en 主题有 untranslated 例外",
           not missing_exc, "; ".join(missing_exc))

    # ---- 分块完整性 ----
    report("C1 分块字段集合 = 14 字段",
           all(set(c) == P.EXPECTED_FIELDS_CHUNK for c in chunk_rows),
           f"{len(chunk_rows)} rows")
    cid_fail = [c["chunk_id"] for c in chunk_rows
                if c["chunk_id"] != f"{c['topic_id']}::{c['order']}"
                or c["topic_id"] not in ids]
    report("C2 chunk_id 格式与 topic_id 引用", not cid_fail, f"bad={cid_fail}")
    order_fail = []
    by_topic: dict[str, list[int]] = {}
    for c in chunk_rows:
        by_topic.setdefault(c["topic_id"], []).append(c["order"])
    for tid, orders in by_topic.items():
        if sorted(orders) != list(range(len(orders))):
            order_fail.append(tid)
    report("C3 order 每主题 0 起连续", not order_fail, f"bad={order_fail}")
    report("C4 heading_path 非空字符串列表",
           all(isinstance(c["heading_path"], list) and c["heading_path"]
               and all(isinstance(x, str) and x for x in c["heading_path"])
               for c in chunk_rows))
    report("C5 content 非空", all(bool(c["content"]) for c in chunk_rows))
    cc_fail = [c["chunk_id"] for c in chunk_rows
               if c["char_count"] != len(c["content"])]
    report("C6 char_count 与内容一致", not cc_fail, f"bad={cc_fail}")
    ctx_fail = []
    for c in chunk_rows:
        mrow = by_id.get(c["topic_id"])
        if mrow is None or not (c["language"] == mrow["language"]
                                and c["quality"] == mrow["quality"]
                                and c["url"] == mrow["url"]
                                and c["topic_path"] == mrow["topic_path"]):
            ctx_fail.append(c["chunk_id"])
    report("C7 块上下文字段与主题清单一致", not ctx_fail, f"bad={ctx_fail}")
    tk_fail = [c["chunk_id"] for c in chunk_rows
               if not isinstance(c["token_estimate"], int)
               or not (0 < c["token_estimate"] <= 1200)]
    report("C8 token_estimate 为正整数且 ≤ 1200 硬上限", not tk_fail,
           f"bad={tk_fail}")
    en_chunk_ids = {c["chunk_id"] for c in chunk_rows if c["language"] == "en-us"}
    pair_fail2: list[str] = []
    for c in chunk_rows:
        if c["language"] == "en-us":
            if c["paired_chunk_id"] is not None:
                pair_fail2.append(f"en {c['chunk_id']} 不应有配对")
            continue
        pair_id = by_id.get(c["topic_id"], {}).get("paired_topic_id")
        if pair_id is None:
            if c["paired_chunk_id"] is not None:
                pair_fail2.append(f"{c['chunk_id']} 无主题配对却有分块配对")
            continue
        if c["paired_chunk_id"] is None:
            pair_fail2.append(f"{c['chunk_id']} 缺配对")
            continue
        if c["paired_chunk_id"] not in en_chunk_ids:
            pair_fail2.append(f"{c['chunk_id']}->{c['paired_chunk_id']} 悬空")
        if c["paired_chunk_id"].rsplit("::", 1)[0] != pair_id:
            pair_fail2.append(f"{c['chunk_id']}->{c['paired_chunk_id']} 主题不一致")
    for tid, expected_partner in expected_pairs.items():
        if expected_partner is None or not tid.startswith("zh-cn/"):
            continue
        if any(c["paired_chunk_id"] is None
               for c in chunk_rows if c["topic_id"] == tid):
            pair_fail2.append(f"{tid} 分块配对未全部命中")
    report("C9 中文块 paired_chunk_id 引用真实英文块（英文块为 null）",
           not pair_fail2, "; ".join(pair_fail2[:8]))
    img_fail = [c["chunk_id"] for c in chunk_rows
                if c["images"] != re.findall(r"!\[[^\]]*\]\(([^)]+)\)",
                                             c["content"])]
    report("C10 块 images 与内容内图片一致", not img_fail, f"bad={img_fail}")

    # ---- 转换质量代理（逐页） ----
    report("--- 转换质量代理（逐页） ---", True)
    for r in meta_rows:
        raw_file = ROOT / "data" / "raw" / r["language"] / (
            r["id"].rsplit("/", 1)[-1] + ".htm")
        if not raw_file.exists():
            report(f"Q1[{r['id']}] 原始 HTML 存在", False, "data/raw 缺失")
            continue
        raw_html = raw_file.read_bytes().decode("utf-8", errors="replace")
        md = (clean_dir() / (r["id"].replace("/", "_") + ".md")).read_text(
            encoding="utf-8")
        rb = P.raw_body_stats(raw_html)
        ms = P.md_stats(md)
        noise = [p for p in P.NOISE_PATTERNS if re.search(p, md, re.I)]
        report(f"Q1[{r['id']}] 无导航/页脚/版本/脚本残留", not noise,
               f"found={noise}")
        rh = [(lv, txt) for lv, txt in rb["headings"]]
        mh = ms["headings"]
        hdiff = []
        for k in range(max(len(rh), len(mh))):
            a = rh[k] if k < len(rh) else None
            b = mh[k] if k < len(mh) else None
            if a != b:
                hdiff.append(f"#{k}: raw={a} md={b}")
        report(f"Q2[{r['id']}] 标题层级/文本一致", not hdiff, "; ".join(hdiff[:4]))
        report(f"Q3[{r['id']}] 正文链接数量一致",
               len(rb["links"]) == len(ms["links"]),
               f"raw={len(rb['links'])} md={len(ms['links'])}")
        img_abs = all(x.startswith("http") for x in ms["images"])
        report(f"Q4[{r['id']}] 图片数量一致且绝对 URL",
               len(rb["images"]) == len(ms["images"]) and img_abs,
               f"raw={len(rb['images'])} md={len(ms['images'])} abs={img_abs}")
        report(f"Q5[{r['id']}] 提示框转 blockquote",
               rb["callouts"] == ms["blockquote_lines"],
               f"raw_callouts={rb['callouts']} md_blockquotes={ms['blockquote_lines']}")
        report(f"Q6[{r['id']}] 表格/代码计数一致",
               rb["tables"] == ms["tables"]
               and rb["pre"] == ms["code_fences"] // 2,
               f"tables raw={rb['tables']} md={ms['tables']}; "
               f"pre raw={rb['pre']} fences={ms['code_fences']}")

    lines.append(f"\nRESULT: {'ALL PASS' if ok else 'HAS FAILURES'}\n")
    path = check_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return ok
def process_topic(target: TopicTarget, cfg: sync_config.SyncConfig, rate: float,
                  state: sync_state.SyncState, headers_rec: dict):
    """抓取→清洗→元数据→分块；成功返回 (meta, chunks, info)，失败返回 None。"""
    print(f"== 抓取: {target.url}")
    raw, info = _fetch(target, cfg.user_agent, headers_rec)
    _pace(rate)
    if raw is None:
        status = info.get("status")
        prev = state.get(target.url)
        if prev is not None and prev.get("status") == "deleted":
            print(f"错误: 墓碑页 {target.url} GET 失败（status={status}），"
                  "墓碑保持", file=sys.stderr)
            return None
        if prev is not None and (status == 404 or status == 410):
            _delete_topic(target.url, target.language, state,
                          f"{target.url} 现 {status}")
            return None
        state.mark_error(target.url, language=target.language)
        print(f"错误: 抓取失败（status={status}），同步状态已记 error",
              file=sys.stderr)
        return None

    raw_file = ROOT / "data" / "raw" / target.language / target.page
    raw_file.parent.mkdir(parents=True, exist_ok=True)
    raw_file.write_bytes(raw)
    print(f"  原始 HTML -> {raw_file.relative_to(ROOT)}")

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
    return meta, chunks, info


def reconcile_single_url(url: str, cfg: sync_config.SyncConfig, rate: float) -> int:
    """单主题 URL 端到端全量对账；返回进程退出码（0=成功且自检全 PASS）。"""
    try:
        target = parse_topic_url(url)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    state = sync_state.SyncState(state_path())
    state.load()
    headers_rec: dict = {}
    result = process_topic(target, cfg, rate, state, headers_rec)
    if result is None:
        return 1
    meta, chunks, info = result
    _merge_headers(headers_rec)
    print(f"  响应头 -> {headers_path().relative_to(ROOT)}")

    ok = selfcheck_single(meta, chunks)
    print(f"== 自检: {'ALL PASS' if ok else 'HAS FAILURES'} -> "
          f"{check_path().relative_to(ROOT)}")
    if ok:
        state.mark_ok(target.url, language=target.language,
                      etag=info.get("etag"), lastmod=info.get("lastmod"),
                      content_hash=meta["content_hash"])
        _resolve_exception(meta["id"], "deleted")
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


def _expected_pair_map(mirrors: dict[str, MirrorResult]) -> dict[str, str | None]:
    expected: dict[str, str | None] = {}
    for m in mirrors.values():
        expected[m.en_id] = m.zh_id
        if m.zh_id is not None:
            expected[m.zh_id] = m.en_id
    return expected


def apply_pairings(mirrors: dict[str, MirrorResult]) -> None:
    """把本轮镜像扫描结果写回元数据 paired_topic_id 与分块 paired_chunk_id。

    中文块按标题位置路径单向映射英文同构块；匹配不上为 None（自检会拦截）。
    """
    expected = _expected_pair_map(mirrors)
    meta_rows = _load_jsonl(meta_path())
    changed = False
    for row in meta_rows:
        if row["id"] in expected and row.get("paired_topic_id") != expected[row["id"]]:
            row["paired_topic_id"] = expected[row["id"]]
            changed = True
    if changed:
        meta_rows.sort(key=lambda r: (r["language"], r["id"]))
        _save_jsonl(meta_path(), meta_rows)

    chunk_rows = _load_jsonl(chunks_path())
    pair_by_topic = {r["id"]: r.get("paired_topic_id") for r in meta_rows}
    pos_by_topic: dict[str, dict[str, tuple]] = {}
    for row in meta_rows:
        cf = clean_dir() / (row["id"].replace("/", "_") + ".md")
        if not cf.exists():
            continue
        md = cf.read_text(encoding="utf-8")
        positions: dict[str, tuple] = {}
        for order, c in enumerate(P.chunk_markdown(md)):
            positions[f"{row['id']}::{order}"] = c["pos"]
        pos_by_topic[row["id"]] = positions
    en_by_path: dict[tuple[str, ...], list[str]] = {}
    for c in chunk_rows:
        if c["language"] == "en-us":
            c["paired_chunk_id"] = None
            en_by_path.setdefault(tuple(c["heading_path"]), []).append(c["chunk_id"])
    for c in chunk_rows:
        if c["language"] != "zh-cn":
            continue
        partner = pair_by_topic.get(c["topic_id"])
        if partner is None:
            c["paired_chunk_id"] = None
            continue
        pos = pos_by_topic.get(c["topic_id"], {}).get(c["chunk_id"])
        matched = next(
            (cid for cid, p in pos_by_topic.get(partner, {}).items() if p == pos),
            None,
        )
        if matched is None:
            matched = en_by_path.get(tuple(c["heading_path"]), [None])[0]
        c["paired_chunk_id"] = matched
    chunk_rows.sort(key=lambda c: (c["topic_id"], c["order"]))
    _save_jsonl(chunks_path(), chunk_rows)


def reconcile_manifest(limit: int | None, cfg: sync_config.SyncConfig,
                       rate: float) -> int:
    """清单驱动全量对账（规格 §5.1–§5.6，票 #16/#18）。

    每轮：sitemap 下载/修复/过滤/去重 → en HEAD 可达性校验（>10% 失配即停）→
    删除检测（sitemap 消失与 200→404 → 墓碑 + deleted 例外 + 产物清除）→
    zh 同路径 HEAD 镜像扫描（含已知重命名映射）→ 样本主题完整管道 →
    例外表与同步状态 → 全量数据集自检。页面重现自动恢复：墓碑清除、例外
    resolved、重新入库。重复运行幂等。
    """
    state = sync_state.SyncState(state_path())
    state.load()
    headers_rec: dict = {}

    print(f"== sitemap: {sync_manifest.SITEMAP_URL}")
    raw, info = sync_manifest.download_sitemap(cfg.user_agent)
    _pace(rate)
    if raw is None:
        print(f"错误: sitemap 下载失败（status={info.get('status')}），"
              "停止本轮，不使用旧清单静默继续", file=sys.stderr)
        return 1
    try:
        en_urls = sync_manifest.build_en_manifest(
            raw.decode("utf-8", errors="replace"))
    except ET.ParseError as exc:
        print(f"错误: sitemap 不是合法 XML（{exc}），停止本轮", file=sys.stderr)
        return 1
    if not en_urls:
        print("错误: sitemap 未解析出 Topics/*.htm 条目，停止本轮", file=sys.stderr)
        return 1
    scope = en_urls if limit is None else en_urls[:limit]
    print(f"== en 清单: 修复/过滤/去重后 {len(en_urls)} 条"
          + (f"，--limit {limit} → 本轮 {len(scope)} 条" if limit is not None
             else ""))

    manifest = _headers_manifest(cfg.user_agent)
    en_ok: list[str] = []
    en_failed: list[tuple[str, object]] = []
    for url in scope:
        hinfo = P.probe_head(manifest, url, headers_rec)
        _pace(rate)
        status = hinfo.get("status")
        if status == 200:
            en_ok.append(url)
        else:
            en_failed.append((url, status))
    failure_rate = len(en_failed) / len(scope)
    threshold = cfg.stop_conditions.error_rate_percent / 100.0
    if failure_rate > threshold:
        print(f"错误: en 清单失配 {len(en_failed)}/{len(scope)} "
              f"（{failure_rate:.1%} > {cfg.stop_conditions.error_rate_percent}%），"
              "停止本轮并告警，不使用旧清单静默继续", file=sys.stderr)
        for url, status in en_failed[:5]:
            print(f"  失配示例: {url} → {status}",
                  file=sys.stderr)
        return 1
    for url, status in en_failed:
        prev = state.get(url)
        if prev is not None and prev.get("status") == "deleted":
            continue  # 墓碑保持：不因探测失败改写状态
        if prev is not None and (status == 404 or status == 410):
            _delete_topic(url, "en-us", state,
                          f"{url} 现 {status}（sitemap 仍在清单中）")
        else:
            state.mark_error(url, language="en-us")
    print(f"== en HEAD 校验: {len(en_ok)}/{len(scope)} 可达"
          + (f"，{len(en_failed)} 个失配已记状态/例外" if en_failed else ""))

    manifest_normalized = {sync_manifest.normalize_url(u) for u in en_urls}
    disappeared = [
        u for u in sorted(state.urls())
        if (state.get(u) or {}).get("language") == "en-us"
        and (state.get(u) or {}).get("status") != "deleted"
        and sync_manifest.normalize_url(u) not in manifest_normalized
    ]
    for url in disappeared:
        _delete_topic(url, "en-us", state, f"{url} 已从 sitemap 消失")
    if disappeared:
        print(f"== 删除检测: {len(disappeared)} 个曾入库 en 页从 sitemap 消失，"
              "已留墓碑并清除产物")

    mirrors: dict[str, MirrorResult] = {}
    print(f"== zh 镜像扫描: {len(en_ok)} 个 en 主题同路径 HEAD")
    for url in en_ok:
        en_id = _topic_id_of_url(url)
        zh_url = sync_manifest.zh_url_for(url)
        hinfo = P.probe_head(manifest, zh_url, headers_rec)
        _pace(rate)
        status = hinfo.get("status")
        if status == 200:
            zh_id = _topic_id_of_url(zh_url)
            _resolve_exception(zh_id, "untranslated")
            _resolve_exception(zh_id, "renamed")
            mirrors[url] = MirrorResult(url, en_id, zh_url,
                                        _topic_id_of_url(zh_url), "paired")
            continue
        if status != 404 and status != 410:
            state.mark_error(zh_url, language="zh-cn")
            continue
        zh_prev = state.get(zh_url)
        if zh_prev is not None and zh_prev.get("status") != "deleted":
            _delete_topic(zh_url, "zh-cn", state,
                          f"{zh_url} 现 {status}（zh 镜像消失）")
        renamed_page = cfg.renames.get(sync_manifest.en_topic_rel_path(url))
        if renamed_page:
            renamed_url = sync_manifest.zh_url_for_page(zh_url, renamed_page)
            hinfo2 = P.probe_head(manifest, renamed_url, headers_rec)
            _pace(rate)
            status2 = hinfo2.get("status")
            if status2 == 200:
                mirrors[url] = MirrorResult(url, en_id, renamed_url,
                                            _topic_id_of_url(renamed_url),
                                            "renamed")
                _resolve_exception(_topic_id_of_url(zh_url), "untranslated")
                upsert_exception({
                    "id": _topic_id_of_url(zh_url),
                    "type": "renamed",
                    "detail": (f"zh 侧页面为 {renamed_page}："
                               f"{Path(url).stem} ↔ {Path(renamed_page).stem} "
                               "重命名映射"),
                    "discovered_at": sync_state.utc_now_iso(),
                    "resolved": False,
                })
                continue
            if status2 != 404 and status2 != 410:
                state.mark_error(renamed_url, language="zh-cn")
                continue
        mirrors[url] = MirrorResult(url, en_id, None, None, "untranslated")
        upsert_exception({
            "id": _topic_id_of_url(zh_url),
            "type": "untranslated",
            "detail": f"{zh_url} 404，英文主题无中文镜像",
            "discovered_at": sync_state.utc_now_iso(),
            "resolved": False,
        })

    zh_count = sum(1 for m in mirrors.values() if m.zh_url is not None)
    print(f"== zh 镜像: {zh_count} 个命中，"
          f"{sum(1 for m in mirrors.values() if m.kind == 'untranslated')} 未翻译，"
          f"{sum(1 for m in mirrors.values() if m.kind == 'renamed')} 重命名")

    print(f"== 完整管道: {len(en_ok)} en 主题 + {zh_count} zh 镜像")
    consecutive_failures = 0
    for url in en_ok:
        target = parse_topic_url(url)
        result = process_topic(target, cfg, rate, state, headers_rec)
        if result is None:
            consecutive_failures += 1
            if consecutive_failures >= cfg.stop_conditions.consecutive_failures:
                print("错误: 连续抓取失败达到阈值，停止本轮", file=sys.stderr)
                _merge_headers(headers_rec)
                return 1
            continue
        consecutive_failures = 0
        meta, _chunks, fetched = result
        state.mark_ok(target.url, language=target.language,
                      etag=fetched.get("etag"), lastmod=fetched.get("lastmod"),
                      content_hash=meta["content_hash"])
        _resolve_exception(meta["id"], "deleted")
    for url in en_ok:
        mirror = mirrors.get(url)
        if mirror is None or mirror.zh_url is None:
            continue
        target = parse_topic_url(mirror.zh_url)
        result = process_topic(target, cfg, rate, state, headers_rec)
        if result is None:
            consecutive_failures += 1
            if consecutive_failures >= cfg.stop_conditions.consecutive_failures:
                print("错误: 连续抓取失败达到阈值，停止本轮", file=sys.stderr)
                _merge_headers(headers_rec)
                return 1
            continue
        consecutive_failures = 0
        meta, _chunks, fetched = result
        state.mark_ok(target.url, language=target.language,
                      etag=fetched.get("etag"), lastmod=fetched.get("lastmod"),
                      content_hash=meta["content_hash"])
        _resolve_exception(meta["id"], "deleted")

    apply_pairings(mirrors)
    _merge_headers(headers_rec)
    print(f"== 例外表: {len(_load_exceptions())} 条 -> "
          f"{exceptions_path().relative_to(ROOT)}")

    ok = selfcheck_dataset(_expected_pair_map(mirrors))
    print(f"== 自检: {'ALL PASS' if ok else 'HAS FAILURES'} -> "
          f"{check_path().relative_to(ROOT)}")
    return 0 if ok else 1


def incremental_sync(limit: int | None, url: str | None,
                     cfg: sync_config.SyncConfig, rate: float,
                     dry_run: bool = False) -> int:
    """日常增量同步（票 #17/#18）：基于同步状态对已知主题发起条件请求。

    未变化页（304 或指纹一致）不重写任何产物、状态保持；变化页 GET 全文。
    曾 ok 页面 404/410 → 墓碑 + deleted 例外 + 产物清除；已删除墓碑不重探，
    --url 显式指定时可重新入库（墓碑清除、例外 resolved）。每条结果即时落盘，
    中断后可从断点续跑。dry_run 只输出将抓取的 URL 清单，不发 GET、不写任何产物。
    """
    state = sync_state.SyncState(state_path())
    state.load()
    if url is not None:
        try:
            parse_topic_url(url)
        except ValueError as exc:
            print(f"错误: {exc}", file=sys.stderr)
            return 1
        scope = [url]
    else:
        records = sorted(state.urls())
        active = [u for u in records
                  if (state.get(u) or {}).get("status") != "deleted"]
        scope = active[:limit] if limit is not None else active
    if not scope:
        print("增量同步: 同步状态为空或无活跃主题（先运行全量对账）")
        return 0

    headers_rec: dict = {}
    unchanged = 0
    changed = 0
    errors = 0
    fetched_any = False
    for target_url in scope:
        record = state.get(target_url)
        info = P.probe_head(
            _headers_manifest(cfg.user_agent, _conditional_headers(record)),
            target_url, headers_rec)
        _pace(rate)
        record_status = (record or {}).get("status")
        if info.get("status") == 304 and record_status == "deleted":
            # 墓碑页重现：内容未变（304）也要重新入库并清墓碑
            info = {**info, "status": 200}
        if _is_unchanged(info, record) and record_status != "deleted":
            unchanged += 1
            print(f"== 未变化: {target_url}")
            continue
        if info.get("status") != 200:
            errors += 1
            status = info.get("status")
            if dry_run:
                print(f"错误: {target_url} → {status}，dry-run 不记状态",
                      file=sys.stderr)
                continue
            if record_status == "deleted":
                print(f"== 墓碑保持: {target_url} → {status}，不改写状态")
                continue
            if status == 404 or status == 410:
                _delete_topic(target_url, (record or {}).get("language"),
                              state, f"{target_url} 现 {status}")
                continue
            state.mark_error(target_url,
                             language=(record or {}).get("language"))
            print(f"错误: {target_url} → {status}，同步状态已记 error",
                  file=sys.stderr)
            continue
        changed += 1
        if dry_run:
            print(f"== 将抓取: {target_url}")
            continue
        fetched_any = True
        print(f"== 变化: {target_url}")
        target = parse_topic_url(target_url)
        result = process_topic(target, cfg, rate, state, headers_rec)
        if result is None:
            errors += 1
            continue
        meta, _chunks, fetched = result
        state.mark_ok(target_url, language=target.language,
                      etag=fetched.get("etag"), lastmod=fetched.get("lastmod"),
                      content_hash=meta["content_hash"])
        _resolve_exception(meta["id"], "deleted")
        print(f"== 同步状态: ok（etag={fetched.get('etag')!r}, "
              f"content_hash={meta['content_hash'][:12]}…）")
    if fetched_any:
        _merge_headers(headers_rec)
        print(f"  响应头 -> {headers_path().relative_to(ROOT)}")
    if dry_run:
        print(f"== 增量同步预览: 将抓取 {changed}，未变化 {unchanged}"
              + (f"，错误 {errors}" if errors else ""))
    else:
        print(f"== 增量同步完成: 未变化 {unchanged}，变化 {changed}"
              + (f"，错误 {errors}" if errors else ""))
    return 0


