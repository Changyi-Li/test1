"""同步状态原语单元测试（票 #14，AC5）。"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import sync_state


def test_missing_state_file_loads_empty(tmp_path):
    st = sync_state.SyncState(tmp_path / "sync-state.jsonl")
    st.load()
    assert st.urls() == []
    assert st.get("https://example.test/topics/GettingStarted.htm") is None


def test_record_writes_full_jsonl_record_and_reloads(tmp_path):
    st = sync_state.SyncState(tmp_path / "sync-state.jsonl")
    st.load()
    st.record(
        "https://example.test/topics/GettingStarted.htm",
        language="en-us",
        etag='"abc123"',
        lastmod="2026-08-02T00:00:00Z",
        content_hash="deadbeef",
        status="ok",
        last_ok_at="2026-08-02T01:00:00Z",
    )
    lines = (tmp_path / "sync-state.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    st2 = sync_state.SyncState(tmp_path / "sync-state.jsonl")
    st2.load()
    got = st2.get("https://example.test/topics/GettingStarted.htm")
    assert got is not None
    assert got["language"] == "en-us"
    assert got["etag"] == '"abc123"'
    assert got["lastmod"] == "2026-08-02T00:00:00Z"
    assert got["content_hash"] == "deadbeef"
    assert got["status"] == "ok"
    assert got["last_ok_at"] == "2026-08-02T01:00:00Z"
    assert got["deleted_at"] is None


def test_record_same_url_updates_in_place_and_is_idempotent(tmp_path):
    st = sync_state.SyncState(tmp_path / "sync-state.jsonl")
    st.load()
    url = "https://example.test/topics/GettingStarted.htm"
    st.record(url, status="ok", etag="v1", last_ok_at="2026-08-02T01:00:00Z")
    st.record(url, etag="v2", content_hash="hash2")
    lines = (tmp_path / "sync-state.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    st2 = sync_state.SyncState(tmp_path / "sync-state.jsonl")
    st2.load()
    got = st2.get(url)
    assert got["etag"] == "v2"
    assert got["content_hash"] == "hash2"
    assert got["status"] == "ok"
    assert got["last_ok_at"] == "2026-08-02T01:00:00Z"


def test_mark_deleted_leaves_tombstone_then_mark_ok_clears_it(tmp_path):
    st = sync_state.SyncState(tmp_path / "sync-state.jsonl")
    st.load()
    url = "https://example.test/topics/GettingStarted.htm"
    st.record(url, language="en-us", etag='"v1"', content_hash="h1",
              status="ok", last_ok_at="2026-08-02T01:00:00Z")
    st.mark_deleted(url, deleted_at="2026-08-02T02:00:00Z")
    tombstone = st.get(url)
    assert tombstone["status"] == "deleted"
    assert tombstone["deleted_at"] == "2026-08-02T02:00:00Z"
    assert tombstone["etag"] == '"v1"'      # 墓碑保留最后指纹
    assert tombstone["content_hash"] == "h1"
    st.mark_ok(url, etag='"v2"', content_hash="h2",
               last_ok_at="2026-08-02T03:00:00Z")
    revived = st.get(url)
    assert revived["status"] == "ok"
    assert revived["deleted_at"] is None
    assert revived["etag"] == '"v2"'
    assert revived["content_hash"] == "h2"


def test_mark_error_preserves_last_ok_at_and_fingerprint(tmp_path):
    st = sync_state.SyncState(tmp_path / "sync-state.jsonl")
    st.load()
    url = "https://example.test/topics/GettingStarted.htm"
    st.record(url, etag='"v1"', status="ok", last_ok_at="2026-08-02T01:00:00Z")
    st.mark_error(url)
    got = st.get(url)
    assert got["status"] == "error"
    assert got["etag"] == '"v1"'
    assert got["last_ok_at"] == "2026-08-02T01:00:00Z"
    assert got["deleted_at"] is None


def test_record_rejects_invalid_status_and_unknown_fields(tmp_path):
    st = sync_state.SyncState(tmp_path / "sync-state.jsonl")
    st.load()
    try:
        st.record("https://example.test/topics/x.htm", status="gone")
    except ValueError as exc:
        assert "状态" in str(exc)
    else:
        raise AssertionError("非法 status 应抛 ValueError")
    try:
        st.record("https://example.test/topics/x.htm", magic="yes")
    except ValueError as exc:
        assert "magic" in str(exc)
    else:
        raise AssertionError("未知字段应抛 ValueError")


def test_load_rejects_corrupt_line_with_location(tmp_path):
    path = tmp_path / "sync-state.jsonl"
    path.write_text(
        '{"url": "https://example.test/topics/a.htm", "status": "ok"}\n'
        "not-json\n",
        encoding="utf-8",
    )
    st = sync_state.SyncState(path)
    try:
        st.load()
    except ValueError as exc:
        assert "sync-state.jsonl:2" in str(exc)
    else:
        raise AssertionError("损坏的状态行应抛 ValueError")
