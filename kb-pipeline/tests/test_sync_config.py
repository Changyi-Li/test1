"""同步配置加载单元测试（票 #14，AC5）。"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import sync_config


def test_loads_real_default_config():
    cfg = sync_config.load_sync_config()
    assert cfg.incremental.cadence == "weekly"
    assert cfg.incremental.rate_per_sec == 2
    assert cfg.reconcile.cadence == "monthly"
    assert cfg.reconcile.rate_per_sec == 5
    assert cfg.user_agent.startswith("MonitorERP-KB-Bot")
    assert cfg.backoff.base_seconds == 1
    assert cfg.backoff.max_seconds == 60
    assert cfg.stop_conditions.consecutive_failures == 5
    assert cfg.stop_conditions.error_rate_percent == 10


def test_loads_valid_config_from_path(tmp_path):
    data = {
        "incremental": {"cadence": "weekly", "rate_per_sec": 1.5,
                        "time_window": "night_asia_shanghai"},
        "reconcile": {"cadence": "monthly", "rate_per_sec": 4,
                      "time_window": "night_asia_shanghai"},
        "user_agent": "MonitorERP-KB-Bot/1.0 (test)",
        "backoff": {"base_seconds": 2, "max_seconds": 30},
        "stop_conditions": {"consecutive_failures": 3, "error_rate_percent": 20},
    }
    path = tmp_path / "sync.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    cfg = sync_config.load_sync_config(path)
    assert cfg.incremental.rate_per_sec == 1.5
    assert cfg.reconcile.rate_per_sec == 4
    assert cfg.user_agent == "MonitorERP-KB-Bot/1.0 (test)"
    assert cfg.backoff.base_seconds == 2
    assert cfg.backoff.max_seconds == 30
    assert cfg.stop_conditions.consecutive_failures == 3
    assert cfg.stop_conditions.error_rate_percent == 20


def test_missing_config_raises_readable_error(tmp_path):
    path = tmp_path / "missing.json"
    try:
        sync_config.load_sync_config(path)
    except ValueError as exc:
        assert str(path) in str(exc)
    else:
        raise AssertionError("缺失配置文件应抛 ValueError")


def test_invalid_config_raises_readable_error(tmp_path):
    data = {
        "incremental": {"cadence": "weekly", "rate_per_sec": 0,
                        "time_window": "night_asia_shanghai"},
        "reconcile": {"cadence": "monthly", "rate_per_sec": 5,
                      "time_window": "night_asia_shanghai"},
        "user_agent": "MonitorERP-KB-Bot/1.0",
        "backoff": {"base_seconds": 1, "max_seconds": 60},
        "stop_conditions": {"consecutive_failures": 5, "error_rate_percent": 10},
    }
    path = tmp_path / "bad.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    try:
        sync_config.load_sync_config(path)
    except ValueError as exc:
        assert "rate_per_sec" in str(exc)
    else:
        raise AssertionError("非法限速应抛 ValueError")


def test_effective_rate_uses_mode_then_cli_override():
    cfg = sync_config.load_sync_config()
    assert sync_config.effective_rate(cfg, "incremental") == 2
    assert sync_config.effective_rate(cfg, "reconcile") == 5
    assert sync_config.effective_rate(cfg, "incremental", override=7.5) == 7.5
    assert sync_config.effective_rate(cfg, "reconcile", override=0.25) == 0.25