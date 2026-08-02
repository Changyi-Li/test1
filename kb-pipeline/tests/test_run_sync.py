"""run_sync CLI 骨架单元测试（票 #14，AC1/AC4）。"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import run_sync
import sync_config


def test_parse_minimal_reconcile():
    ns = run_sync.parse_args(["--mode", "reconcile"])
    assert ns.mode == "reconcile"
    assert ns.url is None
    assert ns.limit is None
    assert ns.rate is None
    assert ns.dry_run is False


def test_parse_all_planned_arguments():
    ns = run_sync.parse_args([
        "--mode", "incremental",
        "--url", "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm",
        "--rate", "3.5",
        "--dry-run",
    ])
    assert ns.mode == "incremental"
    assert ns.url.startswith("https://")
    assert ns.rate == 3.5
    assert ns.dry_run is True


def test_missing_mode_exits_nonzero_with_readable_error(capsys):
    with pytest.raises(SystemExit) as exc:
        run_sync.parse_args(["--limit", "1"])
    assert exc.value.code != 0
    assert "--mode" in capsys.readouterr().err


def test_invalid_mode_exits_nonzero_with_readable_error(capsys):
    with pytest.raises(SystemExit) as exc:
        run_sync.parse_args(["--mode", "full"])
    assert exc.value.code != 0
    assert "full" in capsys.readouterr().err


def test_nonpositive_limit_exits_nonzero(capsys):
    with pytest.raises(SystemExit) as exc:
        run_sync.parse_args(["--mode", "reconcile", "--limit", "0"])
    assert exc.value.code != 0
    assert "--limit" in capsys.readouterr().err


def test_nonpositive_rate_exits_nonzero(capsys):
    with pytest.raises(SystemExit) as exc:
        run_sync.parse_args(["--mode", "reconcile", "--rate", "0"])
    assert exc.value.code != 0
    assert "--rate" in capsys.readouterr().err


def test_invalid_url_exits_nonzero(capsys):
    with pytest.raises(SystemExit) as exc:
        run_sync.parse_args(["--mode", "reconcile", "--url", "not-a-url"])
    assert exc.value.code != 0
    assert "--url" in capsys.readouterr().err


def test_url_and_limit_together_exit_nonzero(capsys):
    with pytest.raises(SystemExit) as exc:
        run_sync.parse_args([
            "--mode", "reconcile", "--url", "https://example.test/a.htm",
            "--limit", "3",
        ])
    assert exc.value.code != 0
    err = capsys.readouterr().err
    assert "--url" in err and "--limit" in err


def test_main_prints_plan_with_override(tmp_path, capsys, monkeypatch):
    monkeypatch.setattr(sync_config, "DEFAULT_CONFIG_PATH", tmp_path / "sync.json")
    (tmp_path / "sync.json").write_text(
        '{"incremental": {"cadence": "weekly", "rate_per_sec": 2, '
        '"time_window": "night_asia_shanghai"}, '
        '"reconcile": {"cadence": "monthly", "rate_per_sec": 5, '
        '"time_window": "night_asia_shanghai"}, '
        '"user_agent": "MonitorERP-KB-Bot/1.0", '
        '"backoff": {"base_seconds": 1, "max_seconds": 60}, '
        '"stop_conditions": {"consecutive_failures": 5, "error_rate_percent": 10}}',
        encoding="utf-8",
    )
    code = run_sync.main(["--mode", "reconcile", "--rate", "7.5", "--dry-run"])
    assert code == 0
    out = capsys.readouterr().out
    assert "reconcile" in out
    assert "7.5" in out
    assert "MonitorERP-KB-Bot" in out
    assert "dry-run" in out.lower() or "预演" in out


def test_main_config_error_returns_nonzero(capsys, monkeypatch, tmp_path):
    monkeypatch.setattr(sync_config, "DEFAULT_CONFIG_PATH", tmp_path / "missing.json")
    code = run_sync.main(["--mode", "reconcile"])
    assert code != 0
    assert "配置" in capsys.readouterr().err
