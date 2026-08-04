"""RAGFlow 导入 CLI（导入工具，接缝 2 + 编排）。

把 RAG-ready 数据集的 clean md（metadata.jsonl + data/clean/*.md）以 naive
方式导入 RAGFlow：幂等建数据集 → 全量对账（跳过未变/重建变更/清除消失）→
写文档级元数据（meta_fields）→ 触发解析 → 轮询至完成。api_key 从环境变量
RAGFLOW_API_KEY 或 --api-key 提供，不进入配置文件。--dry-run 只预览清单
范围，不连接 RAGFlow。
"""
from __future__ import annotations

import argparse
import math
import os
import sys
import time
from pathlib import Path

import import_engine
import ragflow_api
import ragflow_config

KB_PIPELINE_ROOT = Path(__file__).resolve().parent.parent
METADATA_PATH = KB_PIPELINE_ROOT / import_engine.METADATA_REL
CLEAN_DIR = KB_PIPELINE_ROOT / import_engine.CLEAN_DIR_REL
STATE_PATH = KB_PIPELINE_ROOT / import_engine.IMPORT_STATE_REL

LANGS = ("en-us", "zh-cn")


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="import_ragflow.py",
        description="把 RAG-ready 数据集的 clean md 导入 RAGFlow（全量对账式）",
    )
    ap.add_argument("--dry-run", action="store_true",
                    help="只预览清单范围，不连接 RAGFlow")
    ap.add_argument("--language", choices=LANGS,
                    help="只导入该语言（en-us=保真层 | zh-cn=参考层）")
    ap.add_argument("--module", metavar="NAME",
                    help="只导入该模块（topic_path 首段，如 UserGuide）")
    ap.add_argument("--topic-path", metavar="PREFIX",
                    help="只导入该主题路径前缀（如 UserGuide/GettingStarted）")
    ap.add_argument("--limit", metavar="N", type=int,
                    help="最多导入 N 个主题（在其它过滤之后取前 N）")
    ap.add_argument("--no-wait", action="store_true",
                    help="触发解析后不轮询等待完成")
    ap.add_argument("--api-key", metavar="KEY",
                    help="RAGFlow API key（默认读环境变量 RAGFLOW_API_KEY）")
    ap.add_argument("--dataset-name", metavar="NAME",
                    help="覆盖配置中的目标数据集名")
    ap.add_argument("--config", metavar="PATH",
                    help="覆盖配置路径（默认 config/ragflow.json）")
    return ap


def parse_args(argv=None) -> argparse.Namespace:
    ap = build_parser()
    ns = ap.parse_args(argv)
    if ns.limit is not None and ns.limit <= 0:
        ap.error(f"--limit 必须为正整数，得到 {ns.limit}")
    if ns.module is not None and not ns.module.strip():
        ap.error("--module 必须是非空模块名")
    if ns.topic_path is not None and not ns.topic_path.strip():
        ap.error("--topic-path 必须是非空主题路径前缀")
    return ns


def _resolve_api_key(args) -> str:
    return (args.api_key or os.environ.get("RAGFLOW_API_KEY", "")).strip()


def _get_or_create_dataset(client: ragflow_api.RagflowClient,
                           cfg: ragflow_config.RagflowConfig,
                           dataset_name: str) -> dict:
    for ds in client.list_datasets():
        if ds.get("name") == dataset_name:
            return ds
    return client.create_dataset(dataset_name, cfg.chunk_method,
                                 cfg.parser_config, cfg.embedding_model,
                                 cfg.permission)


def _batches(items: list, size: int):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def _wait_parsing(client: ragflow_api.RagflowClient, dataset_id: str,
                  doc_ids: list[str], cfg: ragflow_config.RagflowConfig) -> None:
    deadline = time.monotonic() + cfg.parse_timeout_seconds
    pending = set(doc_ids)
    while pending:
        docs = {d["id"]: d for d in client.list_documents(dataset_id)}
        statuses = {did: str(docs.get(did, {}).get("run") or "UNSTART")
                    for did in pending}
        done, failed, _pending = import_engine.classify_run_status(statuses)
        if failed:
            raise ragflow_api.RagflowError(
                f"解析失败: {failed}（数据集 {dataset_id}）")
        pending = set(_pending)
        if not pending:
            return
        if time.monotonic() > deadline:
            raise ragflow_api.RagflowError(
                f"解析超时（>{cfg.parse_timeout_seconds}s）: "
                f"{sorted(pending)}")
        time.sleep(cfg.poll_interval_seconds)


def run_import(cfg: ragflow_config.RagflowConfig, api_key: str,
               manifest: list[import_engine.TopicManifest],
               dataset_name: str, state_path: Path,
               wait: bool = True) -> int:
    """执行全量对账导入，返回进程退出码。"""
    client = ragflow_api.RagflowClient(cfg.base_url, api_key)
    dataset = _get_or_create_dataset(client, cfg, dataset_name)
    dataset_id = dataset["id"]
    state = import_engine.load_import_state(state_path)
    rf_docs = {d["name"]: d for d in client.list_documents(dataset_id)}
    plan = import_engine.plan_reconcile(manifest, rf_docs, state)

    print(f"== 对账计划（数据集 {dataset_name}）==")
    print(f"清单主题: {len(manifest)}")
    print(f"上传: {len(plan.uploads)}（新主题）")
    print(f"重建: {len(plan.rebuilds)}（content_hash 变更/解析未完成）")
    print(f"跳过: {len(plan.skips)}（未变化且已解析）")
    print(f"删除: {len(plan.deletes)}（清单外文档）")

    if plan.deletes:
        client.delete_documents(
            dataset_id, [d.doc_id for d in plan.deletes])
        print(f"已删除 {len(plan.deletes)} 个清单外文档")

    rebuild_ids = [rf_docs[e.doc_name]["id"] for e in plan.rebuilds]
    if rebuild_ids:
        client.delete_documents(dataset_id, rebuild_ids)
        print(f"已删除 {len(rebuild_ids)} 个待重建旧文档")

    to_import = plan.uploads + plan.rebuilds
    if not to_import:
        import_engine.save_import_state(state_path, state)
        print("无需导入（全部跳过）。")
        return 0

    imported: list[tuple[import_engine.TopicManifest, dict]] = []
    for batch in _batches(to_import, cfg.batch_upload):
        for entry in batch:
            doc = client.upload_document(dataset_id, entry.clean_path)
            imported.append((entry, doc))
            print(f"  上传 {entry.doc_name} -> {doc.get('id')}")
        for entry, doc in imported[-len(batch):]:
            client.update_document_metadata(
                dataset_id, doc["id"], import_engine.build_meta_fields(entry))
        print(f"  批次 {len(batch)} 篇元数据已写入")

    doc_ids = [doc["id"] for _, doc in imported]
    if doc_ids:
        for batch in _batches(doc_ids, cfg.batch_parse):
            client.trigger_parse(dataset_id, batch)
        print(f"已触发解析 {len(doc_ids)} 篇"
              f"（{math.ceil(len(doc_ids) / cfg.batch_parse)} 批）")
        if wait:
            _wait_parsing(client, dataset_id, doc_ids, cfg)
            print("解析全部完成")

    for entry, _doc in imported:
        state[entry.topic_id] = entry.content_hash
    import_engine.save_import_state(state_path, state)
    print(f"导入状态已更新（{len(imported)} 篇）。")
    return 0


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        cfg = ragflow_config.load_ragflow_config(args.config)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    api_key = _resolve_api_key(args)
    if not api_key and not args.dry_run:
        print("错误: 未提供 RAGFlow API key"
              "（用 --api-key 或设置环境变量 RAGFLOW_API_KEY）",
              file=sys.stderr)
        return 1

    dataset_name = args.dataset_name or cfg.dataset_name
    scope = []
    if args.language:
        scope.append(f"语言 {args.language}")
    if args.module:
        scope.append(f"模块 {args.module}")
    if args.topic_path:
        scope.append(f"主题路径前缀 {args.topic_path}")
    if args.limit:
        scope.append(f"最多 {args.limit} 篇")
    scope_text = "；".join(scope) if scope else "全部"

    try:
        manifest = import_engine.load_manifest(
            METADATA_PATH, CLEAN_DIR, language=args.language,
            module=args.module, topic_path=args.topic_path, limit=args.limit)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    en_count = sum(1 for e in manifest if e.language == "en-us")
    zh_count = len(manifest) - en_count
    print("== import_ragflow 计划 ==")
    print(f"数据集: {dataset_name}（{cfg.base_url}）")
    print(f"范围: {scope_text}")
    print(f"清单主题: {len(manifest)}（en {en_count} + zh {zh_count}）")
    print(f"dry-run: {'是（不连接 RAGFlow）' if args.dry_run else '否'}")

    if args.dry_run:
        return 0
    return run_import(cfg, api_key, manifest, dataset_name, STATE_PATH,
                      wait=not args.no_wait)


if __name__ == "__main__":
    sys.exit(main())
