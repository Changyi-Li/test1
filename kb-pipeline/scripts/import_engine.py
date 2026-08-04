"""RAGFlow 导入引擎纯函数（导入工具，接缝 3/4/5）。

清单构建、对账规划、元数据构造、解析状态判定、导入状态读写。全部为无 IO
（除文件读写外）的纯逻辑，供 import_ragflow.py CLI 编排与单元测试使用。
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import pipeline as P

METADATA_REL = "data/metadata.jsonl"
CLEAN_DIR_REL = "data/clean"
IMPORT_STATE_REL = "state/ragflow-import.jsonl"


@dataclass(frozen=True)
class TopicManifest:
    """metadata.jsonl 中一条主题记录 + 其 clean 文件路径。"""
    topic_id: str
    title: str
    url: str
    source: str
    version: str
    language: str
    topic_path: str
    quality: str
    lastmod: str
    content_hash: str
    paired_topic_id: str
    clean_path: Path

    @property
    def doc_name(self) -> str:
        """RAGFlow 文档名 = clean 文件名（含 .md），与清单一一对应。"""
        return self.clean_path.name


@dataclass(frozen=True)
class DocRef:
    doc_name: str
    doc_id: str


@dataclass(frozen=True)
class ReconcilePlan:
    uploads: list[TopicManifest] = field(default_factory=list)
    rebuilds: list[TopicManifest] = field(default_factory=list)
    skips: list[TopicManifest] = field(default_factory=list)
    deletes: list[DocRef] = field(default_factory=list)

    @property
    def changes(self) -> int:
        """本轮需要写 RAGFlow 的动作数（不含 skip）。"""
        return len(self.uploads) + len(self.rebuilds) + len(self.deletes)


def load_manifest(metadata_path: Path | str, clean_dir: Path | str,
                  language: str | None = None,
                  module: str | None = None,
                  topic_path: str | None = None,
                  limit: int | None = None) -> list[TopicManifest]:
    """从 metadata.jsonl + clean/ 构建导入清单。

    逐条校验 clean 文件存在且 content_hash 重算一致（对齐数据集自检 M8 口径）；
    缺失或不一致直接抛 ValueError，拒绝导入不一致的数据集。
    过滤顺序：language → module（topic_path 首段）→ topic_path（前缀）→ limit。
    """
    clean_root = Path(clean_dir)
    rows: list[dict] = []
    with open(Path(metadata_path), encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))

    selected = rows
    if language is not None:
        selected = [r for r in selected if r.get("language") == language]
    if module is not None:
        selected = [r for r in selected
                    if r.get("topic_path", "").split("/", 1)[0] == module]
    if topic_path is not None:
        prefix = topic_path.rstrip("/")
        selected = [r for r in selected
                    if r.get("topic_path", "").startswith(prefix)]
    if limit is not None:
        selected = selected[:limit]

    manifest: list[TopicManifest] = []
    for r in selected:
        topic_id = str(r["id"])
        clean_path = clean_root / (topic_id.replace("/", "_") + ".md")
        if not clean_path.exists():
            rel = clean_path.relative_to(clean_root.parent.parent)
            raise ValueError(
                f"清单主题缺少 clean 文件: {topic_id}（{rel} 不存在）")
        current_hash = P.sha256_hex(clean_path.read_text(encoding="utf-8"))
        if current_hash != r.get("content_hash"):
            raise ValueError(
                f"清单主题 content_hash 与 clean 文件不一致: {topic_id}")
        manifest.append(TopicManifest(
            topic_id=topic_id,
            title=str(r.get("title", "")),
            url=str(r.get("url", "")),
            source=str(r.get("source", "")),
            version=str(r.get("version", "")),
            language=str(r.get("language", "")),
            topic_path=str(r.get("topic_path", "")),
            quality=str(r.get("quality", "")),
            lastmod=str(r.get("lastmod", "")),
            content_hash=str(r["content_hash"]),
            paired_topic_id=str(r.get("paired_topic_id") or ""),
            clean_path=clean_path,
        ))
    return manifest


def plan_reconcile(manifest: list[TopicManifest],
                   rf_docs: dict[str, dict],
                   state: dict[str, str]) -> ReconcilePlan:
    """对账规划（全量对账式）。

    - rf_docs: RAGFlow 现有文档 {doc_name: {"id": str, "run": str}}
    - state: 上次导入记录 {topic_id: content_hash}
    每主题：不存在→上传；存在且 hash 未变且 run=DONE→跳过；其余→删除重建
    （run 非 DONE 视为需重试——覆盖 --no-wait 后解析失败/未完成的情形）。
    清单外的 RAGFlow 文档→删除（消失主题/墓碑）。
    """
    plan = ReconcilePlan()
    manifest_names = {entry.doc_name for entry in manifest}
    for entry in manifest:
        rec = rf_docs.get(entry.doc_name)
        if rec is None:
            plan.uploads.append(entry)
            continue
        last_hash = state.get(entry.topic_id)
        if (last_hash is not None and last_hash == entry.content_hash
                and rec.get("run") == "DONE"):
            plan.skips.append(entry)
        else:
            plan.rebuilds.append(entry)
    for doc_name, rec in rf_docs.items():
        if doc_name not in manifest_names:
            plan.deletes.append(DocRef(doc_name=doc_name, doc_id=rec["id"]))
    return plan


def build_meta_fields(entry: TopicManifest) -> dict[str, str]:
    """把清单字段映射为 RAGFlow 文档 meta_fields（检索过滤/审计对账用）。"""
    return {
        "topic_id": entry.topic_id,
        "url": entry.url,
        "language": entry.language,
        "quality": entry.quality,
        "topic_path": entry.topic_path,
        "version": entry.version,
        "source": entry.source,
        "paired_topic_id": entry.paired_topic_id,
        "lastmod": entry.lastmod,
        "content_hash": entry.content_hash,
    }


def classify_run_status(statuses: dict[str, str]) -> tuple[list[str], list[str], list[str]]:
    """把 {doc_id: run} 拆成 (done, failed, pending)。

    DONE=成功；FAIL/CANCEL=失败；其余（UNSTART/RUNNING）=待完成。
    """
    done = [d for d, s in statuses.items() if s == "DONE"]
    failed = [d for d, s in statuses.items() if s in ("FAIL", "CANCEL")]
    pending = [d for d, s in statuses.items() if s not in ("DONE", "FAIL", "CANCEL")]
    return done, failed, pending


def load_import_state(path: Path | str) -> dict[str, str]:
    """读导入状态 {topic_id: content_hash}；文件缺失/为空返回空 dict。"""
    p = Path(path)
    if not p.exists():
        return {}
    state: dict[str, str] = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        state[rec["topic_id"]] = rec["content_hash"]
    return state


def save_import_state(path: Path | str, state: dict[str, str]) -> None:
    """把 {topic_id: content_hash} 落盘为 JSONL（幂等覆盖，key 排序）。"""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps({"topic_id": tid, "content_hash": h},
                        ensure_ascii=False)
             for tid, h in sorted(state.items())]
    p.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
