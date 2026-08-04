"""RAGFlow 导入配置加载单元测试（导入工具，接缝 1）。"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import ragflow_config


def test_loads_real_default_config():
    cfg = ragflow_config.load_ragflow_config()
    assert cfg.base_url == "http://localhost:80"
    assert cfg.dataset_name == "monitorerp-help"
    assert cfg.chunk_method == "naive"
    assert cfg.embedding_model == ""
    assert cfg.parser_config["chunk_token_num"] == 512
    assert cfg.batch_upload >= 1
    assert cfg.batch_parse >= 1
    assert cfg.poll_interval_seconds > 0
    assert cfg.parse_timeout_seconds > 0


def test_loads_valid_config_from_path(tmp_path):
    data = {
        "base_url": "http://localhost:9380",
        "dataset_name": "my-kb",
        "chunk_method": "naive",
        "embedding_model": "embedding-3@ZHIPU@ZHIPU-AI",
        "permission": "me",
        "parser_config": {"chunk_token_num": 256, "delimiter": "\n"},
        "batch_upload": 10,
        "batch_parse": 30,
        "poll_interval_seconds": 5,
        "parse_timeout_seconds": 600,
    }
    path = tmp_path / "ragflow.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    cfg = ragflow_config.load_ragflow_config(path)
    assert cfg.base_url == "http://localhost:9380"
    assert cfg.dataset_name == "my-kb"
    assert cfg.embedding_model == "embedding-3@ZHIPU@ZHIPU-AI"
    assert cfg.parser_config["chunk_token_num"] == 256
    assert cfg.batch_upload == 10
    assert cfg.parse_timeout_seconds == 600


def test_missing_config_raises_readable_error(tmp_path):
    path = tmp_path / "missing.json"
    try:
        ragflow_config.load_ragflow_config(path)
    except ValueError as exc:
        assert str(path) in str(exc)
    else:
        raise AssertionError("缺失配置文件应抛 ValueError")


def test_invalid_base_url_raises(tmp_path):
    data = {
        "base_url": "ftp://localhost",
        "dataset_name": "x",
        "chunk_method": "naive",
        "parser_config": {},
        "batch_upload": 20,
        "batch_parse": 50,
        "poll_interval_seconds": 10,
        "parse_timeout_seconds": 3600,
    }
    path = tmp_path / "bad.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    try:
        ragflow_config.load_ragflow_config(path)
    except ValueError as exc:
        assert "base_url" in str(exc)
    else:
        raise AssertionError("非 http(s) base_url 应抛 ValueError")


def test_nonpositive_batch_raises(tmp_path):
    data = {
        "base_url": "http://localhost:80",
        "dataset_name": "x",
        "chunk_method": "naive",
        "parser_config": {},
        "batch_upload": 0,
        "batch_parse": 50,
        "poll_interval_seconds": 10,
        "parse_timeout_seconds": 3600,
    }
    path = tmp_path / "bad.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    try:
        ragflow_config.load_ragflow_config(path)
    except ValueError as exc:
        assert "batch_upload" in str(exc)
    else:
        raise AssertionError("非正 batch_upload 应抛 ValueError")


def test_invalid_chunk_method_raises(tmp_path):
    data = {
        "base_url": "http://localhost:80",
        "dataset_name": "x",
        "chunk_method": "unknown-parser",
        "parser_config": {},
        "batch_upload": 20,
        "batch_parse": 50,
        "poll_interval_seconds": 10,
        "parse_timeout_seconds": 3600,
    }
    path = tmp_path / "bad.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    try:
        ragflow_config.load_ragflow_config(path)
    except ValueError as exc:
        assert "chunk_method" in str(exc)
    else:
        raise AssertionError("非法 chunk_method 应抛 ValueError")
