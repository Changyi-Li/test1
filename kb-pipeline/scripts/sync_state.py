"""按 URL 记录的同步状态原语（规格 §4.4，票 #14）。

状态文件为 gitignore 的 JSONL：每行一条 URL 记录。新环境首跑无状态文件时
自动退化为空状态（全量 HEAD 重建），重跑幂等。
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

STATE_FIELDS = (
    "url", "language", "etag", "lastmod", "content_hash",
    "status", "last_ok_at", "deleted_at",
)
VALID_STATUSES = ("ok", "deleted", "error")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class SyncState:
    def __init__(self, path: Path):
        self.path = path
        self._records: dict[str, dict] = {}

    def load(self) -> None:
        self._records = {}
        if not self.path.exists():
            return
        for line_no, line in enumerate(self.path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"{self.path}:{line_no}: 同步状态行不是合法 JSON: {exc}"
                ) from exc
            if not isinstance(record, dict) or "url" not in record:
                raise ValueError(f"{self.path}:{line_no}: 同步状态行缺少 url 字段")
            self._records[record["url"]] = record

    def urls(self) -> list[str]:
        return list(self._records)

    def get(self, url: str) -> dict | None:
        record = self._records.get(url)
        return dict(record) if record is not None else None

    def record(self, url: str, **fields) -> dict:
        """合并写入一条 URL 记录并即时落盘；重复写入同一 URL 为幂等更新。"""
        if not url:
            raise ValueError("同步状态记录必须有非空 url")
        for key in fields:
            if key not in STATE_FIELDS or key == "url":
                raise ValueError(f"未知同步状态字段: {key}")
        status = fields.get("status")
        if status is not None and status not in VALID_STATUSES:
            raise ValueError(
                f"非法状态 {status!r}，应为 {'/'.join(VALID_STATUSES)} 之一"
            )
        record = self._records.get(url)
        if record is None:
            record = {"url": url, **{f: None for f in STATE_FIELDS if f != "url"}}
            self._records[url] = record
        record.update(fields)
        self._save()
        return dict(record)

    def mark_ok(self, url: str, *, last_ok_at: str | None = None, **fields) -> dict:
        """记 ok 并清除墓碑（页面重现时恢复）；保留/更新传入的指纹字段。"""
        if last_ok_at is None:
            last_ok_at = utc_now_iso()
        return self.record(url, status="ok", last_ok_at=last_ok_at,
                           deleted_at=None, **fields)

    def mark_deleted(self, url: str, *, deleted_at: str | None = None, **fields) -> dict:
        """记 deleted 墓碑；未提供的指纹字段保留最后已知值。"""
        if deleted_at is None:
            deleted_at = utc_now_iso()
        return self.record(url, status="deleted", deleted_at=deleted_at, **fields)

    def mark_error(self, url: str, **fields) -> dict:
        """记 error；保留 last_ok_at 与最后已知指纹。"""
        return self.record(url, status="error", **fields)

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            json.dumps(self._records[u], ensure_ascii=False)
            for u in sorted(self._records)
        ]
        self.path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
