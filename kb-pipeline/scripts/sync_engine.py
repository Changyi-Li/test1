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

失败恢复与停止条件（票 #19）：所有 GET/HEAD 遇 429/5xx 按配置指数退避重试
（base×2^n 封顶 max_seconds，config/sync.json 的 backoff）。每轮跟踪连续失败与
错误率：连续失败 ≥ 配置阈值或单轮错误率 > 配置阈值时停止本轮、非零退出，并把
失败 URL 与原因写进 state/sync-error-report.jsonl 供恢复排查；每条结果即时落盘，
任何中断（含阈值停止）后续跑从同步状态恢复，不重复已完成工作。
"""
from __future__ import annotations

import json
import math
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from email.utils import format_datetime
from pathlib import Path
from typing import Callable, TypeVar
from urllib.parse import urlparse

import pipeline as P
import sync_config
import sync_manifest
import sync_state

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE_REL = "state/sync-state.jsonl"
ERROR_REPORT_REL = "state/sync-error-report.jsonl"

LANGS = ("en-us", "zh-cn")
_TOPIC_URL_RE = re.compile(
    r"^/(.+?)/(en-us|zh-cn)/Content/Topics/(.+)/([^/]+\.htm)$"
)

# 429/5xx 视为服务器侧瞬时可重试错误（规格 §5.4）；其余状态不重试。
RETRYABLE_STATUSES = frozenset({429, 500, 502, 503, 504})


def state_path() -> Path:
    return ROOT / STATE_FILE_REL


def error_report_path() -> Path:
    return ROOT / ERROR_REPORT_REL


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


def sample_check_path() -> Path:
    return ROOT / "data" / "selfcheck-sample-results.txt"


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


@dataclass(frozen=True)
class TopicResult:
    """process_topic 的结果（票 #19）：status=ok 时 meta/chunks/info 为有效产物。

    - ok：抓取→清洗→元数据→分块全部完成，产物已入库。
    - deleted：200→404/410 删除事件或墓碑保持，墓碑/例外已写，不算失败。
    - error：运行时失败（网络/429/5xx/自检未过），reason 供错误报告。
    """
    status: str
    meta: dict = field(default_factory=dict)
    chunks: list[dict] = field(default_factory=list)
    info: dict = field(default_factory=dict)
    reason: str | None = None


@dataclass
class RoundFailures:
    """单轮失败跟踪（规格 §5.5，票 #19）：连续失败与错误率停止判定 + 失败清单。

    attempt_ok / attempt_failed 逐条更新（attempts 分母含成功/失败/删除事件）；
    consecutive_stop 在每次失败后立即检查，rate_stop 在阶段边界/轮末检查。
    records 供错误报告（失败 URL 与原因，供恢复排查）。
    """
    attempts: int = 0
    failures: int = 0
    consecutive: int = 0
    records: list[dict] = field(default_factory=list)

    def attempt_ok(self) -> None:
        self.attempts += 1
        self.consecutive = 0

    def attempt_failed(self, url: str, reason: str) -> None:
        self.attempts += 1
        self.failures += 1
        self.consecutive += 1
        self.records.append({
            "url": url,
            "reason": reason,
            "at": sync_state.utc_now_iso(),
        })

    def consecutive_stop(self, cfg: sync_config.SyncConfig) -> str | None:
        threshold = cfg.stop_conditions.consecutive_failures
        if self.consecutive >= threshold:
            return f"连续失败 {self.consecutive} 次 ≥ {threshold}，停止本轮"
        return None

    def rate_stop(self, cfg: sync_config.SyncConfig) -> str | None:
        threshold = cfg.stop_conditions.error_rate_percent / 100.0
        if self.attempts and self.failures / self.attempts > threshold:
            pct = self.failures / self.attempts * 100.0
            return (f"单轮错误率 {pct:.1f}% > "
                    f"{cfg.stop_conditions.error_rate_percent}%，停止本轮")
        return None

    def consume(self, result: TopicResult, cfg: sync_config.SyncConfig,
                url: str) -> str | None:
        """按 process_topic 结果更新失败跟踪；连续失败达阈值返回停止原因，否则 None。

        error → 记失败；ok / deleted → 记成功（删除事件不算失败）。调用方仍需按
        result.status 决定跳过（error/deleted）或 mark_ok（ok）。
        """
        if result.status == "error":
            self.attempt_failed(url, result.reason or "抓取失败")
            return self.consecutive_stop(cfg)
        self.attempt_ok()
        return None


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


def _en_topic_path(url: str) -> str:
    """从 en 主题 URL 提取主题路径（Content/Topics/ 后、页面文件前的目录部分）。

    例如 `.../Content/Topics/UserGuide/GettingStarted/GettingStarted.htm` →
    `UserGuide/GettingStarted`。用于 --topic-path 前缀限定对账范围（票 #21）。
    """
    rel = sync_manifest.en_topic_rel_path(url)
    return rel.rsplit("/", 1)[0]


def _pace(rate: float) -> None:
    """抓取后按 1/rate 秒间隔限速（试点自约束 1–2 req/s 口径的参数化）。"""
    time.sleep(1.0 / rate)


# ---------- 429/5xx 指数退避（规格 §5.4，票 #19） ----------

def _backoff_delay(attempt: int, backoff: sync_config.BackoffConfig) -> float:
    """第 attempt 次重试前的退避延迟：base×2^attempt，封顶 max_seconds。"""
    return min(backoff.base_seconds * (2 ** attempt), backoff.max_seconds)


def _retriable(status: object) -> bool:
    """429/5xx 视为可重试；网络异常（字符串状态）与其余状态码不重试。"""
    return isinstance(status, int) and status in RETRYABLE_STATUSES


def _can_retry(attempt: int, backoff: sync_config.BackoffConfig) -> bool:
    """下一跳退避延迟仍低于上限才继续重试（1s→2s→4s…封顶 max_seconds）。"""
    return _backoff_delay(attempt, backoff) < backoff.max_seconds


def _status_reason(status: object) -> str:
    """把抓取返回的 status（HTTP 状态码或 ERROR 字符串）转成错误报告用的原因。"""
    if isinstance(status, int):
        return f"HTTP {status}"
    return str(status)


_T = TypeVar("_T")


def _retry_probe(probe: Callable[[], tuple[_T, dict]],
                 backoff: sync_config.BackoffConfig) -> tuple[_T, dict]:
    """执行返回 (result, info) 的探测；429/5xx 按配置指数退避重试。

    返回最后一次探测的 (result, info)；退避延迟 base×2^n 封顶 max_seconds，
    下一跳延迟已达上限时放弃重试（1s→2s→4s…上限 60s，规格 §5.4）。
    """
    attempt = 0
    while True:
        result, info = probe()
        status = info.get("status")
        if not _retriable(status) or not _can_retry(attempt, backoff):
            return result, info
        time.sleep(_backoff_delay(attempt, backoff))
        attempt += 1


def _write_error_report(failures: list[dict], stopped: str, total: int) -> Path:
    """写错误报告：失败 URL 与原因逐行 JSONL + summary 行；覆盖上次报告。"""
    path = error_report_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        json.dumps({"type": "failure", **f}, ensure_ascii=False)
        for f in failures
    ]
    lines.append(json.dumps({
        "type": "summary",
        "stopped": stopped,
        "failed": len(failures),
        "total": total,
        "at": sync_state.utc_now_iso(),
    }, ensure_ascii=False))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _stop_round(failures: list[dict], reason: str, total: int) -> int:
    """停止本轮：写错误报告、打印停止原因与报告路径、返回非零退出码。"""
    path = _write_error_report(failures, reason, total)
    print(f"错误: {reason}", file=sys.stderr)
    print(f"错误报告: {path.relative_to(ROOT)}（{len(failures)} 条失败）",
          file=sys.stderr)
    return 1


def _fetch(target: TopicTarget, cfg: sync_config.SyncConfig, headers_rec: dict,
           timeout: int = 30) -> tuple[bytes | None, dict]:
    """按配置 UA 抓取单页；429/5xx 按配置指数退避重试（票 #19）。

    响应头信息写入调用方共享的 headers_rec；重试期间每次探测都会刷新该记录，
    返回最后一次探测的结果与响应头信息。
    """
    manifest = P.Manifest(
        site=target.site,
        topic_path=target.topic_path,
        source=target.source,
        topics=(),
        zh_probes=(),
        headers={"User-Agent": cfg.user_agent},
        fetch_sleep=0.0,
    )

    def _probe_once() -> tuple[bytes | None, dict]:
        raw = P.probe(manifest, target.url, headers_rec, timeout=timeout)
        return raw, headers_rec.get(target.url, {})

    return _retry_probe(_probe_once, cfg.backoff)


def _probe_head_with_backoff(manifest: P.Manifest, url: str, headers_rec: dict,
                             backoff: sync_config.BackoffConfig) -> dict:
    """HEAD 探测；429/5xx 指数退避重试（票 #19）。返回最后一次探测的 info。"""
    _result, info = _retry_probe(
        lambda: (None, P.probe_head(manifest, url, headers_rec)), backoff)
    return info


def _download_sitemap_with_backoff(cfg: sync_config.SyncConfig) -> tuple[bytes | None, dict]:
    """下载 en sitemap；429/5xx 指数退避重试（票 #19）。返回 (raw, info)。"""
    return _retry_probe(lambda: sync_manifest.download_sitemap(cfg.user_agent),
                        cfg.backoff)


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
    """按 (id, type) 幂等覆盖写入例外表；保留首次发现时间，resolved 以本轮为准。

    重跑全量对账时同一结构例外不再刷新 discovered_at，保证重跑产物逐字节一致
    （resolved 同值时输出不变）；条件重新出现（如图片 broken→revive→broken）
    时 resolved 回到 False，反映当前状态。
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
        topic_id.replace("/", "_") + ".htm")
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


class _CheckLog:
    """自检输出收集器：report 记录 PASS/FAIL 行并聚合 ok；failures 供失败清单。"""

    def __init__(self) -> None:
        self.lines: list[str] = []
        self.failures: list[str] = []
        self.skips: int = 0
        self.ok = True

    def report(self, name: str, passed: bool, detail: str = "") -> None:
        self.ok = self.ok and passed
        line = f"[{'PASS' if passed else 'FAIL'}] {name}" \
            + (f" — {detail}" if detail else "")
        self.lines.append(line)
        if not passed:
            self.failures.append(line)

    def skip(self, name: str) -> None:
        self.lines.append(f"[SKIP] {name}")
        self.skips += 1


def _print_failures(failures: list[str]) -> None:
    """门禁失败清单输出到 stderr（票 #20 AC5：失败即给清单）。"""
    if not failures:
        return
    print(f"自检失败清单（{len(failures)} 项）:", file=sys.stderr)
    for line in failures:
        print(f"  {line}", file=sys.stderr)


def _emit_gate(machine: _CheckLog, conversion: _CheckLog, path: Path) -> bool:
    """把机器检查 + 转换质量结果合并写盘并打印失败清单；返回是否全部通过。"""
    lines = machine.lines + conversion.lines
    ok = machine.ok and conversion.ok
    lines.append(f"\nRESULT: {'ALL PASS' if ok else 'HAS FAILURES'}\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    _print_failures(machine.failures + conversion.failures)
    return ok


def selfcheck_single(meta: dict, chunks: list[dict]) -> bool:
    """单页机器自检：元数据完整性 + 分块完整性；配对检查标记 SKIP。

    任一检查失败 → 写自检结果文件、stderr 打印失败清单并返回 False。
    """
    log = _CheckLog()
    report = log.report

    topic_id = meta["id"]
    language = meta["language"]
    id_re = re.compile(rf"^({'|'.join(LANGS)})/(?:[A-Za-z0-9_()-]+/)*[A-Za-z0-9_()-]+$")

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
    log.skip("M9 镜像配对（单 URL 对账不做镜像扫描，清单驱动票覆盖）")

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
    report("C8 token_estimate 为正整数且 ≤ 1200 硬上限（原子块例外）",
           all(isinstance(c["token_estimate"], int)
               and (0 < c["token_estimate"] <= 1200
                    or not _has_split_point(c["content"]))
               for c in chunks))
    log.skip("C9 中文块镜像配对（单 URL 对账不做镜像扫描，清单驱动票覆盖）")
    report("C10 块 images 与内容内图片一致",
           all(c["images"] == re.findall(r"!\[[^\]]*\]\(([^)]+)\)", c["content"])
               for c in chunks))

    log.lines.append(f"\nRESULT: {'ALL PASS' if log.ok else 'HAS FAILURES'}\n")
    path = check_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(log.lines), encoding="utf-8")
    _print_failures(log.failures)
    return log.ok


def _has_split_point(content: str) -> bool:
    """块内容是否有可切分点（空行）。原子块（表格/列表/提示框，无空行）按规格
    §4.2「原子保留/不切断」允许超过 ~1200 硬上限；有切分点却仍超上限才判 FAIL。"""
    return bool(re.search(r"\n\s*\n", content or ""))


def _machine_check(meta_rows: list[dict], chunk_rows: list[dict],
                   exc_rows: list[dict],
                   expected_pairs: dict[str, str | None]) -> _CheckLog:
    """机器检查 100%（规格 §6 第 2 条）：M1–M10 元数据完整性 + C1–C10 分块完整性。

    expected_pairs 为本轮镜像扫描得到的 {topic_id: paired_topic_id 或 None}；
    抽查模式传 {} 时只校验数据内部一致性（互逆/悬空/同语言），不比对扫描结果。
    """
    log = _CheckLog()
    report = log.report
    ids = {r["id"] for r in meta_rows}
    id_re = re.compile(rf"^({'|'.join(LANGS)})/(?:[A-Za-z0-9_()-]+/)*[A-Za-z0-9_()-]+$")
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
               or not (0 < c["token_estimate"] <= 1200)
               and _has_split_point(c["content"])]
    report("C8 token_estimate 为正整数且 ≤ 1200 硬上限（原子块例外）",
           not tk_fail, f"bad={tk_fail}")
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
    return log


def _conversion_check(meta_rows: list[dict],
                      sampled: set[str] | None = None,
                      skip_without_raw: bool = False) -> _CheckLog:
    """转换质量逐页 7 项（规格 §6 第 3 条）：无残留/标题一致/无截断乱码/链接数/
    图片绝对 URL/提示框转 blockquote/表格代码原子保留。sampled=None 时全量逐页。

    skip_without_raw=True 时缺失 data/raw 的页面标 SKIP 而非 FAIL（raw 不入库，
    供抽查模板在 fresh clone 上不假失败；对账自检保持 FAIL 以拦截产物不一致）。
    """
    log = _CheckLog()
    report = log.report
    log.lines.append("--- 转换质量代理（逐页） ---" if sampled is None
                     else f"--- 转换质量代理（按模块抽样 {len(sampled)} 页） ---")
    for r in meta_rows:
        if sampled is not None and r["id"] not in sampled:
            continue
        tid = r["id"]
        raw_file = ROOT / "data" / "raw" / r["language"] / (
            tid.replace("/", "_") + ".htm")
        if not raw_file.exists():
            if skip_without_raw:
                log.skip(f"Q1[{tid}] 原始 HTML 缺失（data/raw 不入库）"
                         "— 跳过转换质量校验")
            else:
                report(f"Q1[{tid}] 原始 HTML 存在", False, "data/raw 缺失")
            continue
        raw_html = raw_file.read_bytes().decode("utf-8", errors="replace")
        md = (clean_dir() / (tid.replace("/", "_") + ".md")).read_text(
            encoding="utf-8")
        rb = P.raw_body_stats(raw_html)
        ms = P.md_stats(md)
        noise = [p for p in P.NOISE_PATTERNS if re.search(p, md, re.I)]
        report(f"Q1[{tid}] 无导航/页脚/版本/脚本残留", not noise,
               f"found={noise}")
        rh = [(lv, txt) for lv, txt in rb["headings"]]
        mh = ms["headings"]
        hdiff = []
        for k in range(max(len(rh), len(mh))):
            a = rh[k] if k < len(rh) else None
            b = mh[k] if k < len(mh) else None
            same = (a is not None and b is not None and a[0] == b[0]
                    and P.normalize_heading_text(a[1])
                    == P.normalize_heading_text(b[1]))
            if not same:
                hdiff.append(f"#{k}: raw={a} md={b}")
        report(f"Q2[{tid}] 标题层级/文本一致", not hdiff, "; ".join(hdiff[:4]))
        garbled = P.garbled_markdown_problems(md)
        report(f"Q3[{tid}] 无截断/乱码", not garbled, "; ".join(garbled[:4]))
        report(f"Q4[{tid}] 正文链接数量一致",
               len(rb["links"]) == len(ms["links"]),
               f"raw={len(rb['links'])} md={len(ms['links'])}")
        img_abs = all(x.startswith("http") for x in ms["images"])
        report(f"Q5[{tid}] 图片数量一致且绝对 URL",
               len(rb["images"]) == len(ms["images"]) and img_abs,
               f"raw={len(rb['images'])} md={len(ms['images'])} abs={img_abs}")
        report(f"Q6[{tid}] 提示框转 blockquote",
               rb["callouts"] == ms["blockquote_lines"],
               f"raw_callouts={rb['callouts']} md_blockquotes={ms['blockquote_lines']}")
        report(f"Q7[{tid}] 表格/代码计数一致",
               rb["tables"] == ms["tables"]
               and rb["pre"] == ms["code_fences"] // 2,
               f"tables raw={rb['tables']} md={ms['tables']}; "
               f"pre raw={rb['pre']} fences={ms['code_fences']}")
    return log


def selfcheck_dataset(expected_pairs: dict[str, str | None]) -> bool:
    """全量数据集自检（规格 §6）：机器检查 100%（M1–M10/C1–C10）+ 转换质量
    Q1–Q7 逐页全检。任一门禁失败 → 写自检文件、stderr 打印失败清单并返回 False。"""
    meta_rows = _load_jsonl(meta_path())
    chunk_rows = _load_jsonl(chunks_path())
    exc_rows = _load_exceptions()
    machine = _machine_check(meta_rows, chunk_rows, exc_rows, expected_pairs)
    conversion = _conversion_check(meta_rows)
    return _emit_gate(machine, conversion, check_path())


def _module_of(row: dict) -> str:
    """主题所属模块：topic_path 首段，缺失时按 "root"。"""
    return (row.get("topic_path") or "").split("/")[0] or "root"


def sample_pages_per_module(meta_rows: list[dict],
                            check_cfg: sync_config.CheckConfig) -> set[str]:
    """按模块抽样：每模块 ≥max(ceil(页数×percent%), min_pages) 页，不足该数全取；
    按 id 排序取前 N，保证确定性（规格 §6 全站抽查模板）。"""
    by_module: dict[str, list[str]] = {}
    for r in meta_rows:
        by_module.setdefault(_module_of(r), []).append(r["id"])
    sampled: set[str] = set()
    for module in sorted(by_module):
        ids = by_module[module]
        sample_size = max(
            math.ceil(len(ids) * check_cfg.sample_min_percent / 100.0),
            check_cfg.sample_min_pages)
        sampled.update(sorted(ids)[:sample_size])
    return sampled


def check_dataset_sampled(cfg: sync_config.SyncConfig,
                          module: str | None = None) -> int:
    """抽查模板 CLI 能力（规格 §6，票 #20）：机器检查 100%，转换质量按模块抽样
    （每模块 ≥5% 且 ≥10 页，7 项全过）。只读当前 data/ 产物，不发网络请求。

    任一 M/C/Q 门禁失败 → 写 data/selfcheck-sample-results.txt、stderr 打印失败
    清单并返回非零退出码；全部通过返回 0。--module 限定单模块；data/raw 缺失的
    页面转换质量标 SKIP（raw 不入库，fresh clone 不假失败）。"""
    meta_rows = _load_jsonl(meta_path())
    if module is not None:
        filtered = [r for r in meta_rows if _module_of(r) == module]
        if not filtered:
            print(f"错误: 模块 {module!r} 无主题页（按 topic_path 首段匹配）",
                  file=sys.stderr)
            return 1
        meta_rows = filtered
    if not meta_rows:
        print("抽查: 数据集为空（先运行全量对账）", file=sys.stderr)
        return 1
    scope_ids = {r["id"] for r in meta_rows}
    chunk_rows = [c for c in _load_jsonl(chunks_path())
                  if c["topic_id"] in scope_ids]
    exc_rows = _load_exceptions()
    machine = _machine_check(meta_rows, chunk_rows, exc_rows, expected_pairs={})
    sampled = sample_pages_per_module(meta_rows, cfg.check)
    conversion = _conversion_check(meta_rows, sampled=sampled,
                                   skip_without_raw=True)
    ok = _emit_gate(machine, conversion, sample_check_path())
    note = ""
    if conversion.skips:
        note = f"，{conversion.skips} 页缺 data/raw 跳过转换质量"
    print(f"== 抽查: {'ALL PASS' if ok else 'HAS FAILURES'} "
          f"-> {sample_check_path().relative_to(ROOT)}"
          + (f"（转换质量抽样 {len(sampled)}/{len(meta_rows)} 页{note}）"
             if ok else ""))
    return 0 if ok else 1


def verify_images(cfg: sync_config.SyncConfig, rate: float,
                  headers_rec: dict,
                  round_f: RoundFailures) -> tuple[list[str], str | None]:
    """全量对账图片验证（规格 §5.2/§5.6，票 #20）：数据集内图片 URL 去重后全量
    HEAD 验证。200 通过并 resolve 既有 broken_image 例外；404/410 记 broken_image
    例外（detail 记所属主题）；其余状态按失败计入停止阈值（429/5xx 指数退避）。
    返回 (失效 URL 列表, 停止原因或 None)。"""
    meta_rows = _load_jsonl(meta_path())
    refs: dict[str, set[str]] = {}
    for r in meta_rows:
        for url in r.get("images", []):
            if isinstance(url, str) and url:
                refs.setdefault(url, set()).add(r["id"])
    image_urls = sorted(refs)
    if not image_urls:
        print("== 图片验证: 数据集无图片")
        return [], None
    manifest = _headers_manifest(cfg.user_agent)
    broken: list[str] = []
    for url in image_urls:
        hinfo = _probe_head_with_backoff(manifest, url, headers_rec, cfg.backoff)
        _pace(rate)
        status = hinfo.get("status")
        if status == 200:
            round_f.attempt_ok()
            _resolve_exception(url, "broken_image")
            continue
        if status == 404 or status == 410:
            # 404/410 与删除/未翻译判定口径一致（资源已不存在）→ broken_image 例外
            round_f.attempt_ok()   # 失效是结构性例外，不计失败
            upsert_exception({
                "id": url,
                "type": "broken_image",
                "detail": f"{url} {status}，被 {','.join(sorted(refs[url]))} 引用",
                "discovered_at": sync_state.utc_now_iso(),
                "resolved": False,
            })
            broken.append(url)
            continue
        round_f.attempt_failed(url, _status_reason(status))
        stop = round_f.consecutive_stop(cfg)
        if stop is not None:
            return broken, stop
    print(f"== 图片验证: 去重后 {len(image_urls)} 个 URL，"
          f"{len(broken)} 个失效（broken_image 例外）")
    return broken, None


def process_topic(target: TopicTarget, cfg: sync_config.SyncConfig, rate: float,
                  state: sync_state.SyncState, headers_rec: dict) -> TopicResult:
    """抓取→清洗→元数据→分块（429/5xx 指数退避）；返回 TopicResult。

    ok=产物入库；deleted=404/410 删除事件或墓碑保持（不算失败）；error=运行时
    失败，reason 供错误报告。删除/失败的状态与例外在该函数内即时落盘。
    """
    print(f"== 抓取: {target.url}")
    raw, info = _fetch(target, cfg, headers_rec)
    _pace(rate)
    if raw is None:
        status = info.get("status")
        prev = state.get(target.url)
        if prev is not None and prev.get("status") == "deleted":
            print(f"错误: 墓碑页 {target.url} GET 失败（status={status}），"
                  "墓碑保持", file=sys.stderr)
            return TopicResult("deleted")
        if prev is not None and (status == 404 or status == 410):
            _delete_topic(target.url, target.language, state,
                          f"{target.url} 现 {status}")
            return TopicResult("deleted")
        state.mark_error(target.url, language=target.language)
        print(f"错误: 抓取失败（status={status}），同步状态已记 error",
              file=sys.stderr)
        return TopicResult("error", reason=_status_reason(status))

    raw_file = ROOT / "data" / "raw" / target.language / (
        target.topic_id.replace("/", "_") + ".htm")
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
    return TopicResult("ok", meta=meta, chunks=chunks, info=info)


def reconcile_single_url(url: str, cfg: sync_config.SyncConfig, rate: float) -> int:
    """单主题 URL 端到端全量对账；返回进程退出码（0=成功且自检全 PASS）。

    运行时失败或自检未通过 → 写错误报告并非零退出（票 #19）；删除事件非零退出，
    但不写错误报告（已由墓碑/例外处理，非失败）。
    """
    try:
        target = parse_topic_url(url)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    state = sync_state.SyncState(state_path())
    state.load()
    headers_rec: dict = {}
    result = process_topic(target, cfg, rate, state, headers_rec)
    _merge_headers(headers_rec)
    if result.status == "error":
        failures = [{"url": target.url, "reason": result.reason or "抓取失败",
                     "at": sync_state.utc_now_iso()}]
        return _stop_round(failures, f"单 URL 对账失败: {target.url}", 1)
    if result.status == "deleted":
        print(f"== 对账: {target.url} 已删除（墓碑保持/删除事件），非零退出",
              file=sys.stderr)
        return 1
    meta, chunks, info = result.meta, result.chunks, result.info
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
        return 0
    state.mark_error(target.url, language=target.language,
                     etag=info.get("etag"), lastmod=info.get("lastmod"),
                     content_hash=meta["content_hash"])
    print("== 同步状态: error（自检未通过，产物保留供检查，不记 ok）",
          file=sys.stderr)
    failures = [{"url": target.url, "reason": "自检未通过",
                 "at": sync_state.utc_now_iso()}]
    return _stop_round(failures, f"单 URL 自检未通过: {target.url}", 1)


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
                       rate: float, topic_path: str | None = None) -> int:
    """清单驱动全量对账（规格 §5.1–§5.6，票 #16/#18/#19）。

    每轮：sitemap 下载/修复/过滤/去重 → en HEAD 可达性校验（>10% 失配即停）→
    删除检测（sitemap 消失与 200→404 → 墓碑 + deleted 例外 + 产物清除）→
    zh 同路径 HEAD 镜像扫描（含已知重命名映射）→ 样本主题完整管道 →
    例外表与同步状态 → 全量数据集自检。页面重现自动恢复：墓碑清除、例外
    resolved、重新入库。重复运行幂等。票 #19：所有 GET/HEAD 遇 429/5xx 指数
    退避重试；完整管道连续失败达阈值或单轮错误率超阈值 → 停止、非零退出、
    写错误报告（失败 URL 与原因）。

    topic_path 非 None 时（票 #21）：本轮范围限定为该主题路径前缀下的 en 主题
    （含其 zh 镜像），用于手动触发模块级全量对账；删除检测仍以完整 sitemap
    为准，范围外曾 ok 页面不被误标墓碑。与 --limit 可叠加（先按前缀过滤再取前 N）。
    """
    state = sync_state.SyncState(state_path())
    state.load()
    headers_rec: dict = {}

    print(f"== sitemap: {sync_manifest.SITEMAP_URL}")
    raw, info = _download_sitemap_with_backoff(cfg)
    _pace(rate)
    if raw is None:
        reason = (f"sitemap 下载失败（status={info.get('status')}），"
                  "停止本轮，不使用旧清单静默继续")
        failures = [{"url": sync_manifest.SITEMAP_URL, "reason": reason,
                     "at": sync_state.utc_now_iso()}]
        return _stop_round(failures, reason, 1)
    try:
        en_urls = sync_manifest.build_en_manifest(
            raw.decode("utf-8", errors="replace"))
    except ET.ParseError as exc:
        reason = f"sitemap 不是合法 XML（{exc}），停止本轮"
        failures = [{"url": sync_manifest.SITEMAP_URL, "reason": reason,
                     "at": sync_state.utc_now_iso()}]
        return _stop_round(failures, reason, 1)
    if not en_urls:
        reason = "sitemap 未解析出 Topics/*.htm 条目，停止本轮"
        return _stop_round([], reason, 0)
    scope = en_urls
    if topic_path is not None:
        scope = [u for u in en_urls if _en_topic_path(u).startswith(topic_path)]
    if limit is not None:
        scope = scope[:limit]
    scope_note = ""
    if topic_path is not None:
        scope_note += f"，--topic-path {topic_path} → 本轮 {len(scope)} 条"
    if limit is not None:
        scope_note += f"，--limit {limit} → 本轮 {len(scope)} 条"
    print(f"== en 清单: 修复/过滤/去重后 {len(en_urls)} 条{scope_note}")

    manifest = _headers_manifest(cfg.user_agent)
    round_f = RoundFailures()
    en_ok: list[str] = []
    en_failed: list[tuple[str, object]] = []
    for url in scope:
        hinfo = _probe_head_with_backoff(manifest, url, headers_rec, cfg.backoff)
        _pace(rate)
        status = hinfo.get("status")
        if status == 200:
            en_ok.append(url)
            round_f.attempt_ok()
        else:
            en_failed.append((url, status))
            if status == 404 or status == 410:
                round_f.attempt_ok()   # 删除候选：计入分母，不计失败
            else:
                round_f.attempt_failed(url, _status_reason(status))
                stop = round_f.consecutive_stop(cfg)
                if stop is not None:
                    return _stop_round(round_f.records, stop, round_f.attempts)
    failure_rate = len(en_failed) / len(scope)
    threshold = cfg.stop_conditions.error_rate_percent / 100.0
    if failure_rate > threshold:
        reason = (f"en 清单失配 {len(en_failed)}/{len(scope)} "
                  f"（{failure_rate:.1%} > {cfg.stop_conditions.error_rate_percent}%），"
                  "停止本轮并告警，不使用旧清单静默继续")
        for url, status in en_failed[:5]:
            print(f"  失配示例: {url} → {status}",
                  file=sys.stderr)
        failures = [
            {"url": u, "reason": _status_reason(s),
             "at": sync_state.utc_now_iso()}
            for u, s in en_failed
        ]
        return _stop_round(failures, reason, len(scope))
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
        hinfo = _probe_head_with_backoff(manifest, zh_url, headers_rec,
                                         cfg.backoff)
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
            round_f.attempt_failed(zh_url, _status_reason(status))
            stop = round_f.consecutive_stop(cfg)
            if stop is not None:
                _merge_headers(headers_rec)
                return _stop_round(round_f.records, stop, round_f.attempts)
            continue
        round_f.attempt_ok()   # 同路径 404/410：未翻译/重命名候选，计入分母不计失败
        zh_prev = state.get(zh_url)
        if zh_prev is not None and zh_prev.get("status") != "deleted":
            _delete_topic(zh_url, "zh-cn", state,
                          f"{zh_url} 现 {status}（zh 镜像消失）")
        renamed_page = cfg.renames.get(sync_manifest.en_topic_rel_path(url))
        if renamed_page:
            renamed_url = sync_manifest.zh_url_for_page(zh_url, renamed_page)
            hinfo2 = _probe_head_with_backoff(manifest, renamed_url, headers_rec,
                                              cfg.backoff)
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
                round_f.attempt_ok()
                continue
            if status2 != 404 and status2 != 410:
                state.mark_error(renamed_url, language="zh-cn")
                round_f.attempt_failed(renamed_url, _status_reason(status2))
                stop = round_f.consecutive_stop(cfg)
                if stop is not None:
                    _merge_headers(headers_rec)
                    return _stop_round(round_f.records, stop, round_f.attempts)
                continue
            round_f.attempt_ok()   # 重命名探测 404：仍按未翻译处理
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
    for url in en_ok:
        target = parse_topic_url(url)
        result = process_topic(target, cfg, rate, state, headers_rec)
        stop = round_f.consume(result, cfg, target.url)
        if stop is not None:
            _merge_headers(headers_rec)
            return _stop_round(round_f.records, stop, round_f.attempts)
        if result.status == "error" or result.status == "deleted":
            continue
        meta = result.meta
        fetched = result.info
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
        stop = round_f.consume(result, cfg, target.url)
        if stop is not None:
            _merge_headers(headers_rec)
            return _stop_round(round_f.records, stop, round_f.attempts)
        if result.status == "error" or result.status == "deleted":
            continue
        meta = result.meta
        fetched = result.info
        state.mark_ok(target.url, language=target.language,
                      etag=fetched.get("etag"), lastmod=fetched.get("lastmod"),
                      content_hash=meta["content_hash"])
        _resolve_exception(meta["id"], "deleted")

    # 图片验证（票 #20 AC1）：数据集图片 URL 去重后全量 HEAD，404 记 broken_image 例外
    _, img_stop = verify_images(cfg, rate, headers_rec, round_f)
    if img_stop is not None:
        _merge_headers(headers_rec)
        return _stop_round(round_f.records, img_stop, round_f.attempts)
    stop = round_f.rate_stop(cfg)
    if stop is not None:
        _merge_headers(headers_rec)
        return _stop_round(round_f.records, stop, round_f.attempts)

    apply_pairings(mirrors)
    _merge_headers(headers_rec)
    print(f"== 例外表: {len(_load_exceptions())} 条 -> "
          f"{exceptions_path().relative_to(ROOT)}")

    ok = selfcheck_dataset(_expected_pair_map(mirrors))
    print(f"== 自检: {'ALL PASS' if ok else 'HAS FAILURES'} -> "
          f"{check_path().relative_to(ROOT)}")
    # 正常结束也写报告（失败 0 条时为仅 summary），覆盖上一次报告，避免残留误导；
    # 自检未通过时 stopped 反映非零退出，避免报告与退出状态矛盾
    stopped = "completed" if ok else "数据集自检未通过"
    _write_error_report(round_f.records, stopped, round_f.attempts)
    return 0 if ok else 1


def incremental_sync(limit: int | None, url: str | None,
                     cfg: sync_config.SyncConfig, rate: float,
                     dry_run: bool = False) -> int:
    """日常增量同步（票 #17/#18/#19）：基于同步状态对已知主题发起条件请求。

    未变化页（304 或指纹一致）不重写任何产物、状态保持；变化页 GET 全文。
    曾 ok 页面 404/410 → 墓碑 + deleted 例外 + 产物清除；已删除墓碑不重探，
    --url 显式指定时可重新入库（墓碑清除、例外 resolved）。每条结果即时落盘，
    中断后可从断点续跑。429/5xx 条件 HEAD 按配置指数退避重试；连续失败达阈值
    立即停止，轮末错误率超阈值也停止——停止均非零退出并写错误报告（票 #19）。
    dry_run 只输出将抓取的 URL 清单，不发 GET、不写任何产物。
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
    round_f = RoundFailures()
    for target_url in scope:
        record = state.get(target_url)
        info = _probe_head_with_backoff(
            _headers_manifest(cfg.user_agent, _conditional_headers(record)),
            target_url, headers_rec, cfg.backoff)
        _pace(rate)
        record_status = (record or {}).get("status")
        if info.get("status") == 304 and record_status == "deleted":
            # 墓碑页重现：内容未变（304）也要重新入库并清墓碑
            info = {**info, "status": 200}
        if _is_unchanged(info, record) and record_status != "deleted":
            unchanged += 1
            if not dry_run:
                round_f.attempt_ok()
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
                round_f.attempt_ok()  # 墓碑保持：本轮已处理（不重探），不计失败
                print(f"== 墓碑保持: {target_url} → {status}，不改写状态")
                continue
            if status == 404 or status == 410:
                _delete_topic(target_url, (record or {}).get("language"),
                              state, f"{target_url} 现 {status}")
                round_f.attempt_ok()  # 删除事件：本轮已处理，不计失败
                continue
            state.mark_error(target_url,
                             language=(record or {}).get("language"))
            round_f.attempt_failed(target_url, _status_reason(status))
            print(f"错误: {target_url} → {status}，同步状态已记 error",
                  file=sys.stderr)
            stop = round_f.consecutive_stop(cfg)
            if stop is not None:
                if fetched_any:
                    _merge_headers(headers_rec)
                return _stop_round(round_f.records, stop, round_f.attempts)
            continue
        changed += 1
        if dry_run:
            print(f"== 将抓取: {target_url}")
            continue
        fetched_any = True
        print(f"== 变化: {target_url}")
        target = parse_topic_url(target_url)
        result = process_topic(target, cfg, rate, state, headers_rec)
        stop = round_f.consume(result, cfg, target_url)
        if stop is not None:
            if fetched_any:
                _merge_headers(headers_rec)
            return _stop_round(round_f.records, stop, round_f.attempts)
        if result.status == "error":
            errors += 1
            continue
        if result.status == "deleted":
            continue  # 404/410 删除事件：本轮已处理（consume 已计成功）
        meta = result.meta
        fetched = result.info
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
        return 0
    stop = round_f.rate_stop(cfg)
    if stop is not None:
        return _stop_round(round_f.records, stop, round_f.attempts)
    # 正常结束也写报告（失败 0 条时为仅 summary），覆盖上一次报告，避免残留误导
    _write_error_report(round_f.records, "completed", round_f.attempts)
    print(f"== 增量同步完成: 未变化 {unchanged}，变化 {changed}"
          + (f"，错误 {errors}" if errors else ""))
    return 0

