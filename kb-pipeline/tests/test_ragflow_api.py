"""RAGFlow API 客户端单元测试（导入工具，接缝 6，fake urlopen）。"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import ragflow_api


class FakeResponse:
    def __init__(self, payload: object):
        self._raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self):
        return self._raw


def _fake_urlopen(monkeypatch, handler):
    calls = []

    def fake_urlopen(req, timeout=30):
        calls.append(req)
        return handler(req, timeout)

    monkeypatch.setattr(ragflow_api, "urlopen", fake_urlopen)
    return calls


def _client():
    return ragflow_api.RagflowClient("http://localhost:80", "test-key")


def test_list_datasets_unwraps_items(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": [{"id": "d1", "name": "kb"},
                             {"id": "d2", "name": "kb2"}]}))
    datasets = _client().list_datasets()
    assert [d["name"] for d in datasets] == ["kb", "kb2"]
    assert calls[0].full_url == "http://localhost:80/api/v1/datasets?page=1&page_size=100"
    assert calls[0].get_header("Authorization") == "Bearer test-key"


def test_create_dataset_sends_embedding_when_given(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": {"id": "ds-1", "name": "kb"}}))
    dataset = _client().create_dataset(
        "kb", "naive", {"chunk_token_num": 512},
        embedding_model="embedding-3@ZHIPU@ZHIPU-AI")
    assert dataset["id"] == "ds-1"
    body = json.loads(calls[0].data.decode("utf-8"))
    assert body["name"] == "kb"
    assert body["chunk_method"] == "naive"
    assert body["embedding_model"] == "embedding-3@ZHIPU@ZHIPU-AI"
    assert calls[0].get_method() == "POST"


def test_create_dataset_omits_embedding_when_empty(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": {}}))
    _client().create_dataset("kb", "naive", {})
    body = json.loads(calls[0].data.decode("utf-8"))
    assert "embedding_model" not in body


def test_upload_document_multipart_has_filename_and_content(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": [{"id": "doc-1", "name": "a.md", "run": "UNSTART"}]}))
    path = Path("_scratch") / "en-us_A_A1.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# Hello", encoding="utf-8")
    try:
        doc = _client().upload_document("ds-1", path)
        assert doc["id"] == "doc-1"
        # urllib 的 add_header 用 capitalize()，把键存成 "Content-type"
        content_type = calls[0].get_header("Content-type")
        assert content_type.startswith("multipart/form-data; boundary=")
        assert 'name="file"; filename="en-us_A_A1.md"' in calls[0].data.decode("utf-8")
        assert b"# Hello" in calls[0].data
    finally:
        path.unlink(missing_ok=True)


def test_error_on_nonzero_code(monkeypatch):
    _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 102, "message": "document_ids is required"}))
    with pytest.raises(ragflow_api.RagflowError) as exc:
        _client().list_datasets()
    assert "code=102" in str(exc.value)
    assert "document_ids" in str(exc.value)


def test_delete_documents_empty_is_noop(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse({"code": 0}))
    _client().delete_documents("ds-1", [])
    assert calls == []


def test_trigger_parse_sends_document_ids(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse({"code": 0}))
    _client().trigger_parse("ds-1", ["doc-1", "doc-2"])
    body = json.loads(calls[0].data.decode("utf-8"))
    assert body["document_ids"] == ["doc-1", "doc-2"]
    assert calls[0].full_url.endswith("/api/v1/datasets/ds-1/chunks")


def test_retrieve_builds_query_body(monkeypatch):
    calls = _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": {"chunks": [], "total": 0}}))
    data = _client().retrieve(["ds-1"], "问题", top_k=5)
    assert data["total"] == 0
    body = json.loads(calls[0].data.decode("utf-8"))
    assert body["question"] == "问题"
    assert body["dataset_ids"] == ["ds-1"]
    assert body["top_k"] == 5


def test_list_documents_accepts_docs_key(monkeypatch):
    # v0.26.4 文档列表响应用 data.docs（不是 data.items）
    _fake_urlopen(monkeypatch, lambda req, t: FakeResponse(
        {"code": 0, "data": {"docs": [{"id": "d1", "name": "a.md",
                                        "run": "DONE"}], "total": 1}}))
    docs = _client().list_documents("ds-1")
    assert len(docs) == 1
    assert docs[0]["name"] == "a.md"


def test_list_documents_paginates(monkeypatch):
    size = ragflow_api.RagflowClient.PAGE_SIZE
    responses = [
        {"code": 0, "data": {"items": [{"id": f"d{i}", "name": f"{i}.md",
                                        "run": "DONE"} for i in range(size)]}},
        {"code": 0, "data": {"items": [{"id": "d-last", "name": "last.md",
                                        "run": "UNSTART"}]}},
    ]

    def handler(req, timeout):
        return FakeResponse(responses.pop(0))

    calls = _fake_urlopen(monkeypatch, handler)
    docs = _client().list_documents("ds-1")
    assert len(docs) == size + 1
    assert len(calls) == 2
    assert "page=2" in calls[1].full_url
