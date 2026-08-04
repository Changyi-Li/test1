"""RAGFlow 导入 CLI 单元测试（导入工具，接缝 2）。"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import import_ragflow


def test_parse_args_valid_flags():
    ns = import_ragflow.parse_args(
        ["--language", "en-us", "--module", "UserGuide",
         "--topic-path", "UserGuide/GettingStarted", "--limit", "5",
         "--dry-run", "--no-wait"])
    assert ns.language == "en-us"
    assert ns.module == "UserGuide"
    assert ns.topic_path == "UserGuide/GettingStarted"
    assert ns.limit == 5
    assert ns.dry_run is True
    assert ns.no_wait is True


def test_parse_args_nonpositive_limit_rejected():
    with pytest.raises(SystemExit):
        import_ragflow.parse_args(["--limit", "0"])


def test_parse_args_empty_topic_path_rejected():
    with pytest.raises(SystemExit):
        import_ragflow.parse_args(["--topic-path", "  "])


def test_parse_args_invalid_language_rejected():
    with pytest.raises(SystemExit):
        import_ragflow.parse_args(["--language", "fr-fr"])


def test_main_requires_api_key_without_dry_run(capsys):
    assert import_ragflow.main(["--limit", "1"]) == 1
    assert "API key" in capsys.readouterr().err


def test_main_dry_run_loads_real_manifest_and_returns_zero(capsys):
    code = import_ragflow.main(
        ["--dry-run", "--topic-path", "UserGuide/GettingStarted"])
    out = capsys.readouterr().out
    assert code == 0
    assert "GettingStarted" in out
    assert "清单主题: 5" in out


def test_main_with_key_and_dry_run_returns_zero(capsys):
    code = import_ragflow.main(
        ["--api-key", "test-key", "--dry-run",
         "--topic-path", "UserGuide/GettingStarted"])
    assert code == 0
