"""同步配置加载（规格 §5.4，票 #14）。

默认配置在 kb-pipeline/config/sync.json：限速/时段/UA/退避/停止阈值由配置驱动，
CLI 可用 --rate 覆盖当前模式的限速。
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

KB_PIPELINE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = KB_PIPELINE_ROOT / "config" / "sync.json"

MODES = ("incremental", "reconcile")


@dataclass(frozen=True)
class ModeConfig:
    cadence: str
    rate_per_sec: float
    time_window: str


@dataclass(frozen=True)
class BackoffConfig:
    base_seconds: float
    max_seconds: float


@dataclass(frozen=True)
class StopConditions:
    consecutive_failures: int
    error_rate_percent: float


@dataclass(frozen=True)
class SyncConfig:
    incremental: ModeConfig
    reconcile: ModeConfig
    user_agent: str
    backoff: BackoffConfig
    stop_conditions: StopConditions


def _require_key(data: dict, key: str, path: Path) -> None:
    if key not in data:
        raise ValueError(f"{path}: 缺少配置项 {key!r}")


def _positive_float(value, label: str, path: Path) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{path}: {label} 必须是数字") from exc
    if number <= 0:
        raise ValueError(f"{path}: {label} 必须 > 0，得到 {number}")
    return number


def _mode_config(data: dict, path: Path) -> ModeConfig:
    for key in ("cadence", "rate_per_sec", "time_window"):
        _require_key(data, key, path)
    rate = _positive_float(data["rate_per_sec"], "rate_per_sec", path)
    return ModeConfig(
        cadence=str(data["cadence"]),
        rate_per_sec=rate,
        time_window=str(data["time_window"]),
    )


def _backoff_config(data: dict, path: Path) -> BackoffConfig:
    for key in ("base_seconds", "max_seconds"):
        _require_key(data, key, path)
    base = _positive_float(data["base_seconds"], "base_seconds", path)
    maximum = _positive_float(data["max_seconds"], "max_seconds", path)
    if maximum < base:
        raise ValueError(f"{path}: max_seconds 不得小于 base_seconds")
    return BackoffConfig(base_seconds=base, max_seconds=maximum)


def _stop_conditions(data: dict, path: Path) -> StopConditions:
    for key in ("consecutive_failures", "error_rate_percent"):
        _require_key(data, key, path)
    consecutive = data["consecutive_failures"]
    if not isinstance(consecutive, int) or isinstance(consecutive, bool) or consecutive <= 0:
        raise ValueError(f"{path}: consecutive_failures 必须是正整数")
    percent = _positive_float(data["error_rate_percent"], "error_rate_percent", path)
    if percent > 100:
        raise ValueError(f"{path}: error_rate_percent 不得大于 100")
    return StopConditions(
        consecutive_failures=consecutive,
        error_rate_percent=percent,
    )


def load_sync_config(path: Path | str | None = None) -> SyncConfig:
    cfg_path = Path(path) if path is not None else DEFAULT_CONFIG_PATH
    if not cfg_path.exists():
        raise ValueError(f"{cfg_path}: 同步配置文件不存在")
    try:
        data = json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{cfg_path}: 配置文件不是合法 JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{cfg_path}: 配置顶层必须是 JSON 对象")
    for key in ("incremental", "reconcile", "user_agent", "backoff", "stop_conditions"):
        _require_key(data, key, cfg_path)
    return SyncConfig(
        incremental=_mode_config(data["incremental"], cfg_path),
        reconcile=_mode_config(data["reconcile"], cfg_path),
        user_agent=str(data["user_agent"]),
        backoff=_backoff_config(data["backoff"], cfg_path),
        stop_conditions=_stop_conditions(data["stop_conditions"], cfg_path),
    )


def effective_rate(config: SyncConfig, mode: str, override: float | None = None) -> float:
    """返回当前模式的限速；override（如 CLI --rate）优先。"""
    if mode not in MODES:
        raise ValueError(f"非法模式 {mode!r}，应为 {'/'.join(MODES)} 之一")
    if override is not None:
        rate = _positive_float(override, "--rate", Path("--rate"))
        return rate
    return getattr(config, mode).rate_per_sec