"""检索实测探针（导入工具，接缝 7）。

对 RAGFlow 数据集逐条跑 docs/questions-fixture.md 的中文问题清单，打印每题
top-k 命中（映射回 topic_path/quality/url）并判定是否命中预期主题。纯检索，
不依赖 LLM，用于导入后的检索冒烟与验收（questions-fixture 的落地用法）。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import ragflow_api
import ragflow_config

KB_PIPELINE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FIXTURE = KB_PIPELINE_ROOT / "docs" / "questions-fixture.md"
METADATA_PATH = KB_PIPELINE_ROOT / "data" / "metadata.jsonl"

# RAGFlow 检索的 top_k 是候选池（默认 1024），返回条数由 page_size 控制。
# 候选池保持大值，只用 page_size 限制打印条数，避免漏掉排名靠后的预期主题。
CANDIDATE_POOL = 1024


def parse_questions(md_text: str) -> list[dict]:
    """把 questions-fixture.md 的 markdown 表解析为问题清单。

    每行: {number, question, expected_en, expected_zh, facts}；
    expected 为 None 表示无预期主题（表中“—”或空）。
    """
    questions: list[dict] = []
    for line in md_text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        number = cells[0].strip()
        if not number.isdigit():
            continue  # 表头/分隔行

        def expected(value: str) -> str | None:
            value = value.strip()
            if not value or value.startswith("—"):
                return None
            return value

        expected_en = expected(cells[2])
        expected_zh = expected(cells[3])
        # fixture 用「同路径 zh」简写表示与 en 同路径的 zh 主题
        if expected_zh and "同路径" in expected_zh:
            expected_zh = expected_en
        questions.append({
            "number": int(number),
            "question": cells[1],
            "expected_en": expected_en,
            "expected_zh": expected_zh,
            "facts": cells[4],
        })
    return questions


def load_topic_map() -> dict[str, dict]:
    """doc 名（clean 文件名）→ 清单元数据行，用于命中富化与预期比对。"""
    topic_map: dict[str, dict] = {}
    if not METADATA_PATH.exists():
        return topic_map
    with open(METADATA_PATH, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            name = row["id"].replace("/", "_") + ".md"
            topic_map[name] = row
    return topic_map


def hit_expected(hits: list[dict], expected_path: str | None,
                 language: str) -> bool:
    """top-k 命中里是否存在预期主题（full_path 精确匹配 + 语言一致）。

    full_path 由 topic_id 去掉语言前缀得到（如
    en-us/UserGuide/GettingStarted/GettingStarted →
    UserGuide/GettingStarted/GettingStarted），与 fixture 的“预期主题”口径一致。
    language 区分 en/zh 期望：英文期望必须由 en-us 文档满足，中文期望由 zh-cn。
    """
    if expected_path is None:
        return True  # 无预期主题视为不判定
    return any(h.get("full_path") == expected_path
               and h.get("language") == language for h in hits)


def run_probe(cfg: ragflow_config.RagflowConfig, api_key: str,
              dataset_name: str, top_k: int = 5,
              fixture: Path | None = None,
              question_limit: int | None = None) -> int:
    client = ragflow_api.RagflowClient(cfg.base_url, api_key)
    datasets = {d["name"]: d["id"] for d in client.list_datasets()}
    if dataset_name not in datasets:
        print(f"错误: 数据集 {dataset_name!r} 不存在（现有: "
              f"{', '.join(datasets) or '无'}）", file=sys.stderr)
        return 1
    dataset_id = datasets[dataset_name]

    fixture_path = Path(fixture) if fixture is not None else DEFAULT_FIXTURE
    questions = parse_questions(fixture_path.read_text(encoding="utf-8"))
    if question_limit is not None:
        questions = questions[:question_limit]
    topic_map = load_topic_map()

    print(f"== 检索实测（数据集 {dataset_name}，top-{top_k}）==")
    print(f"问题数: {len(questions)}")
    pass_count = 0
    for q in questions:
        data = client.retrieve([dataset_id], q["question"],
                               top_k=CANDIDATE_POOL, page_size=top_k)
        chunks = data.get("chunks", [])[:top_k]
        hits = []
        for c in chunks:
            doc_name = c.get("document_keyword", "")
            meta = topic_map.get(doc_name, {})
            topic_id = meta.get("id", "")
            hits.append({
                "doc_name": doc_name,
                "topic_path": meta.get("topic_path", ""),
                "full_path": (topic_id.split("/", 1)[1]
                              if "/" in topic_id else ""),
                "quality": meta.get("quality", ""),
                "language": meta.get("language", ""),
                "url": meta.get("url", ""),
                "similarity": c.get("similarity"),
                "snippet": (c.get("content") or "")[:140].replace("\n", " "),
            })
        expected = (hit_expected(hits, q["expected_en"], "en-us")
                    and hit_expected(hits, q["expected_zh"], "zh-cn"))
        pass_count += 1 if expected else 0
        print(f"\nQ{q['number']}: {q['question']}")
        exp = " | ".join(x or "—" for x in
                         (q["expected_en"], q["expected_zh"]))
        print(f"  期望: {exp}   命中: {'✓' if expected else '✗'}")
        for i, h in enumerate(hits, 1):
            sim = f"{h['similarity']:.3f}" if h["similarity"] is not None else "-"
            print(f"  {i}. [{sim}] {h['doc_name']}"
                  f"（{h['topic_path']} | {h['quality']} | {h['language']}）")
            if h["url"]:
                print(f"     {h['url']}")
            print(f"     {h['snippet']}")
    print(f"\n== 汇总: {pass_count}/{len(questions)} 命中预期主题 ==")
    return 0 if pass_count == len(questions) else 2


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="retrieval_probe.py",
        description="对 RAGFlow 数据集跑 questions-fixture 检索实测")
    ap.add_argument("--api-key", metavar="KEY",
                    help="RAGFlow API key（默认读环境变量 RAGFLOW_API_KEY）")
    ap.add_argument("--config", metavar="PATH",
                    help="覆盖配置路径（默认 config/ragflow.json）")
    ap.add_argument("--dataset-name", metavar="NAME",
                    help="覆盖配置中的数据集名")
    ap.add_argument("--top-k", type=int, default=5,
                    help="每问取前 N 命中（默认 5）")
    ap.add_argument("--fixture", metavar="PATH",
                    help="覆盖问题清单路径（默认 docs/questions-fixture.md）")
    ap.add_argument("--limit", metavar="N", type=int,
                    help="只跑前 N 个问题")
    return ap


def main(argv=None) -> int:
    ap = build_parser()
    ns = ap.parse_args(argv)
    if ns.top_k <= 0:
        ap.error(f"--top-k 必须为正整数，得到 {ns.top_k}")
    if ns.limit is not None and ns.limit <= 0:
        ap.error(f"--limit 必须为正整数，得到 {ns.limit}")
    try:
        cfg = ragflow_config.load_ragflow_config(ns.config)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1
    api_key = (ns.api_key or os.environ.get("RAGFLOW_API_KEY", "")).strip()
    if not api_key:
        print("错误: 未提供 RAGFlow API key"
              "（用 --api-key 或设置环境变量 RAGFLOW_API_KEY）", file=sys.stderr)
        return 1
    return run_probe(cfg, api_key, ns.dataset_name or cfg.dataset_name,
                     top_k=ns.top_k, fixture=ns.fixture, question_limit=ns.limit)


if __name__ == "__main__":
    sys.exit(main())
