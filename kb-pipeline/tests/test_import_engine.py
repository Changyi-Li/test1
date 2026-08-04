"""RAGFlow 导入引擎纯函数单元测试（导入工具，接缝 3/4/5）。"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

import import_engine
import pipeline as P


def _write_metadata(meta_dir: Path, rows: list[dict]) -> Path:
    path = meta_dir / "metadata.jsonl"
    path.write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
        encoding="utf-8")
    return path


def _topic(id_: str, title: str = "Title", topic_path: str = "A/B",
           language: str = "en-us", quality: str = "canonical",
           md: str = "# Title\nBody") -> dict:
    return {
        "id": id_, "title": title, "url": f"https://help.monitorerp.cn/{id_}",
        "source": "help.monitorerp.cn", "version": "25.8",
        "language": language, "topic_path": topic_path, "quality": quality,
        "lastmod": "2026-05-21T08:16:50Z", "etag": '"e"',
        "content_hash": P.sha256_hex(md), "images": [],
        "paired_topic_id": None,
    }


def _clean_files(clean_dir: Path, rows: list[dict]) -> None:
    clean_dir.mkdir(parents=True, exist_ok=True)
    for r in rows:
        (clean_dir / (r["id"].replace("/", "_") + ".md")).write_text(
            "# Title\nBody", encoding="utf-8")


class TestLoadManifest:
    def test_builds_entries_from_metadata_and_clean(self, tmp_path):
        rows = [
            _topic("en-us/A/A1"),
            _topic("zh-cn/A/A1", language="zh-cn", quality="reference"),
        ]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        manifest = import_engine.load_manifest(meta, tmp_path / "clean")
        assert len(manifest) == 2
        first = manifest[0]
        assert first.topic_id == "en-us/A/A1"
        assert first.quality == "canonical"
        assert first.doc_name == "en-us_A_A1.md"
        assert first.clean_path.name == "en-us_A_A1.md"

    def test_filters_by_language_module_topic_path_and_limit(self, tmp_path):
        rows = [
            _topic("en-us/Accounting/A", topic_path="Accounting/A"),
            _topic("en-us/Stock/S", topic_path="Stock/S"),
            _topic("zh-cn/Stock/S", topic_path="Stock/S", language="zh-cn",
                   quality="reference"),
        ]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        by_lang = import_engine.load_manifest(meta, tmp_path / "clean",
                                              language="zh-cn")
        assert [e.topic_id for e in by_lang] == ["zh-cn/Stock/S"]
        by_module = import_engine.load_manifest(meta, tmp_path / "clean",
                                                module="Accounting")
        assert [e.topic_id for e in by_module] == ["en-us/Accounting/A"]
        by_path = import_engine.load_manifest(meta, tmp_path / "clean",
                                              topic_path="Stock")
        assert {e.topic_id for e in by_path} == {"en-us/Stock/S",
                                                 "zh-cn/Stock/S"}
        limited = import_engine.load_manifest(meta, tmp_path / "clean", limit=2)
        assert len(limited) == 2

    def test_missing_clean_file_raises(self, tmp_path):
        rows = [_topic("en-us/A/Missing")]
        meta = _write_metadata(tmp_path, rows)
        (tmp_path / "clean").mkdir(parents=True)
        with pytest.raises(ValueError) as exc:
            import_engine.load_manifest(meta, tmp_path / "clean")
        assert "缺少 clean 文件" in str(exc.value)
        assert "en-us/A/Missing" in str(exc.value)

    def test_hash_mismatch_raises(self, tmp_path):
        rows = [_topic("en-us/A/A1", md="# Different body")]
        meta = _write_metadata(tmp_path, rows)
        clean = tmp_path / "clean"
        clean.mkdir(parents=True)
        (clean / "en-us_A_A1.md").write_text("# Not the hashed body",
                                             encoding="utf-8")
        with pytest.raises(ValueError) as exc:
            import_engine.load_manifest(meta, clean)
        assert "content_hash" in str(exc.value)


class TestPlanReconcile:
    def test_all_upload_when_empty(self, tmp_path):
        rows = [_topic("en-us/A/A1")]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        manifest = import_engine.load_manifest(meta, tmp_path / "clean")
        plan = import_engine.plan_reconcile(manifest, rf_docs={}, state={})
        assert [e.topic_id for e in plan.uploads] == ["en-us/A/A1"]
        assert not plan.rebuilds and not plan.skips and not plan.deletes

    def test_skip_when_hash_unchanged_and_run_done(self, tmp_path):
        rows = [_topic("en-us/A/A1")]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        manifest = import_engine.load_manifest(meta, tmp_path / "clean")
        doc_name = manifest[0].doc_name
        plan = import_engine.plan_reconcile(
            manifest, rf_docs={doc_name: {"id": "doc-1", "run": "DONE"}},
            state={rows[0]["id"]: rows[0]["content_hash"]})
        assert [e.topic_id for e in plan.skips] == ["en-us/A/A1"]
        assert not plan.uploads and not plan.rebuilds and not plan.deletes

    def test_rebuild_when_hash_changed(self, tmp_path):
        rows = [_topic("en-us/A/A1")]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        manifest = import_engine.load_manifest(meta, tmp_path / "clean")
        doc_name = manifest[0].doc_name
        plan = import_engine.plan_reconcile(
            manifest, rf_docs={doc_name: {"id": "doc-1", "run": "DONE"}},
            state={rows[0]["id"]: "old-hash-different"})
        assert [e.topic_id for e in plan.rebuilds] == ["en-us/A/A1"]
        assert not plan.uploads and not plan.skips

    def test_rebuild_when_hash_match_but_run_not_done(self, tmp_path):
        # --no-wait 后解析失败/未完成：即使 hash 匹配也不能跳过，需重试
        rows = [_topic("en-us/A/A1")]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        manifest = import_engine.load_manifest(meta, tmp_path / "clean")
        doc_name = manifest[0].doc_name
        for run in ("UNSTART", "RUNNING", "FAIL", "CANCEL"):
            plan = import_engine.plan_reconcile(
                manifest, rf_docs={doc_name: {"id": "doc-1", "run": run}},
                state={rows[0]["id"]: rows[0]["content_hash"]})
            assert [e.topic_id for e in plan.rebuilds] == ["en-us/A/A1"], run
            assert not plan.skips, run

    def test_delete_orphan_docs_not_in_manifest(self, tmp_path):
        rows = [_topic("en-us/A/A1")]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        manifest = import_engine.load_manifest(meta, tmp_path / "clean")
        plan = import_engine.plan_reconcile(
            manifest,
            rf_docs={"en-us_A_A1.md": {"id": "doc-1", "run": "DONE"},
                     "en-us_Old_Gone.md": {"id": "doc-2", "run": "DONE"}},
            state={rows[0]["id"]: rows[0]["content_hash"]})
        assert plan.skips and not plan.uploads and not plan.rebuilds
        assert [(d.doc_name, d.doc_id) for d in plan.deletes] == [
            ("en-us_Old_Gone.md", "doc-2")]

    def test_existing_doc_without_state_is_rebuilt(self, tmp_path):
        rows = [_topic("en-us/A/A1")]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        manifest = import_engine.load_manifest(meta, tmp_path / "clean")
        plan = import_engine.plan_reconcile(
            manifest, rf_docs={manifest[0].doc_name:
                               {"id": "doc-1", "run": "DONE"}}, state={})
        assert [e.topic_id for e in plan.rebuilds] == ["en-us/A/A1"]


class TestHelpers:
    def test_build_meta_fields(self, tmp_path):
        rows = [_topic("en-us/A/A1", topic_path="A",
                       md="# Title\nBody")]
        meta = _write_metadata(tmp_path, rows)
        _clean_files(tmp_path / "clean", rows)
        entry = import_engine.load_manifest(meta, tmp_path / "clean")[0]
        fields = import_engine.build_meta_fields(entry)
        assert fields["topic_id"] == "en-us/A/A1"
        assert fields["language"] == "en-us"
        assert fields["quality"] == "canonical"
        assert fields["content_hash"] == rows[0]["content_hash"]
        assert fields["paired_topic_id"] == ""
        assert set(fields) == {
            "topic_id", "url", "language", "quality", "topic_path",
            "version", "source", "paired_topic_id", "lastmod", "content_hash",
        }

    def test_classify_run_status(self):
        done, failed, pending = import_engine.classify_run_status({
            "a": "DONE", "b": "DONE", "c": "FAIL", "d": "CANCEL",
            "e": "UNSTART", "f": "RUNNING",
        })
        assert sorted(done) == ["a", "b"]
        assert sorted(failed) == ["c", "d"]
        assert sorted(pending) == ["e", "f"]

    def test_state_round_trip(self, tmp_path):
        path = tmp_path / "state" / "ragflow-import.jsonl"
        import_engine.save_import_state(path, {"en-us/A/A1": "hash-1",
                                               "zh-cn/A/A1": "hash-2"})
        state = import_engine.load_import_state(path)
        assert state == {"en-us/A/A1": "hash-1", "zh-cn/A/A1": "hash-2"}

    def test_load_missing_state_returns_empty(self, tmp_path):
        assert import_engine.load_import_state(
            tmp_path / "nope.jsonl") == {}
