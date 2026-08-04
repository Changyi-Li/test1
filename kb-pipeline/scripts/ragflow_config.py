"""RAGFlow 导入配置加载（导入工具，接缝 1）。

默认配置在 kb-pipeline/config/ragflow.json：RAGFlow 服务地址/目标数据集名/
chunk_method/parser_config/批大小/轮询参数。api_key 属于敏感信息，不放进配置
文件，由环境变量 RAGFLOW_API_KEY 或 CLI --api-key 提供。
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

KB_PIPELINE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = KB_PIPELINE_ROOT / "config" / "ragflow.json"

CHUNK_METHODS = frozenset({
    "naive", "manual", "qa", "table", "paper", "book", "laws",
    "presentation", "picture", "one", "email", "tag",
})


@dataclass(frozen=True)
class RagflowConfig:
    base_url: str
    dataset_name: str
    chunk_method: str
    embedding_model: str
    permission: str
    parser_config: dict[str, object]
    batch_upload: int
    batch_parse: int
    poll_interval_seconds: float
    parse_timeout_seconds: float


def _require_key(data: dict, key: str, path: Path) -> None:
    if key not in data:
        raise ValueError(f"{path}: 缺少配置项 {key!r}")


def _positive_int(value, label: str, path: Path) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"{path}: {label} 必须是正整数，得到 {value!r}")
    return value


def _positive_float(value, label: str, path: Path) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{path}: {label} 必须是数字") from exc
    if number <= 0:
        raise ValueError(f"{path}: {label} 必须 > 0，得到 {number}")
    return number


def load_ragflow_config(path: Path | str | None = None) -> RagflowConfig:
    cfg_path = Path(path) if path is not None else DEFAULT_CONFIG_PATH
    if not cfg_path.exists():
        raise ValueError(f"{cfg_path}: RAGFlow 导入配置文件不存在")
    try:
        data = json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{cfg_path}: 配置文件不是合法 JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{cfg_path}: 配置顶层必须是 JSON 对象")

    for key in ("base_url", "dataset_name", "chunk_method", "parser_config",
                "batch_upload", "batch_parse",
                "poll_interval_seconds", "parse_timeout_seconds"):
        _require_key(data, key, cfg_path)

    base_url = str(data["base_url"]).rstrip("/")
    parsed = urlparse(base_url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError(f"{cfg_path}: base_url 必须是 http(s) URL，"
                         f"得到 {base_url!r}")

    chunk_method = str(data["chunk_method"])
    if chunk_method not in CHUNK_METHODS:
        raise ValueError(f"{cfg_path}: 非法 chunk_method {chunk_method!r}，"
                         f"应为 {'/'.join(sorted(CHUNK_METHODS))} 之一")

    parser_config = data["parser_config"]
    if not isinstance(parser_config, dict):
        raise ValueError(f"{cfg_path}: parser_config 必须是对象")

    return RagflowConfig(
        base_url=base_url,
        dataset_name=str(data["dataset_name"]),
        chunk_method=chunk_method,
        embedding_model=str(data.get("embedding_model", "")),
        permission=str(data.get("permission", "me")),
        parser_config=parser_config,
        batch_upload=_positive_int(data["batch_upload"], "batch_upload", cfg_path),
        batch_parse=_positive_int(data["batch_parse"], "batch_parse", cfg_path),
        poll_interval_seconds=_positive_float(
            data["poll_interval_seconds"], "poll_interval_seconds", cfg_path),
        parse_timeout_seconds=_positive_float(
            data["parse_timeout_seconds"], "parse_timeout_seconds", cfg_path),
    )
