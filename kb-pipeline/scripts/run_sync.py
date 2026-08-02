"""生产同步 CLI 骨架（规格 §5.7，票 #14）。

当前交付：解析/校验全部规划参数（--mode/--url/--limit/--rate/--dry-run）、
加载配置并解析限速覆盖、输出本轮同步计划。同步引擎由后续票（#15+）实现。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse

import sync_config

STATE_FILE_REL = "state/sync-state.jsonl"
STATE_PATH = Path(__file__).resolve().parent.parent / STATE_FILE_REL


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="run_sync.py",
        description="Monitor ERP 知识库同步 CLI（骨架：解析/校验/配置/计划）",
    )
    ap.add_argument("--mode", required=True, choices=sync_config.MODES,
                    help="incremental=日常增量 | reconcile=全量对账")
    ap.add_argument("--url", metavar="URL",
                    help="只处理单个主题 URL（与 --limit 互斥）")
    ap.add_argument("--limit", metavar="N", type=int,
                    help="最多处理 N 个 URL（与 --url 互斥）")
    ap.add_argument("--rate", metavar="REQ/S", type=float,
                    help="覆盖当前模式限速（必须 > 0）")
    ap.add_argument("--dry-run", action="store_true",
                    help="只预览本轮将抓取的 URL，不写任何产物")
    return ap


def parse_args(argv=None) -> argparse.Namespace:
    ap = build_parser()
    ns = ap.parse_args(argv)
    if ns.url is not None and ns.limit is not None:
        ap.error("--url 与 --limit 不能同时使用（两者都是范围限定方式）")
    if ns.limit is not None and ns.limit <= 0:
        ap.error(f"--limit 必须为正整数，得到 {ns.limit}")
    if ns.rate is not None and ns.rate <= 0:
        ap.error(f"--rate 必须 > 0，得到 {ns.rate}")
    if ns.url is not None:
        parsed = urlparse(ns.url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            ap.error(f"--url 必须是 http(s) 绝对 URL，得到 {ns.url!r}")
    return ns


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        cfg = sync_config.load_sync_config()
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    rate = sync_config.effective_rate(cfg, args.mode, args.rate)
    mode_cfg = getattr(cfg, args.mode)
    if args.url is not None:
        scope = f"单 URL: {args.url}"
    elif args.limit is not None:
        scope = f"最多 {args.limit} 个 URL"
    else:
        scope = "全部清单 URL"
    rate_line = f"{rate} req/s"
    if args.rate is not None:
        rate_line += f"（配置 {mode_cfg.rate_per_sec}，由 --rate 覆盖）"

    print("== run_sync 计划（骨架） ==")
    print(f"模式: {args.mode}")
    print(f"范围: {scope}")
    print(f"限速: {rate_line}")
    print(f"UA: {cfg.user_agent}")
    print(f"退避: {cfg.backoff.base_seconds}s → {cfg.backoff.max_seconds}s（指数）")
    print(f"停止阈值: 连续失败 {cfg.stop_conditions.consecutive_failures} 次 "
          f"或错误率 > {cfg.stop_conditions.error_rate_percent}%")
    print(f"dry-run: {'是' if args.dry_run else '否'}")
    print(f"状态文件: {STATE_FILE_REL}")
    print("提示: 同步引擎由后续票实现，本票仅交付参数解析、配置加载与状态原语。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
