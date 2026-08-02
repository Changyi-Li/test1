"""生产同步 CLI（规格 §5.7/§6，票 #14/#15/#16/#17/#20）。

解析/校验全部规划参数（--mode/--url/--limit/--rate/--dry-run/--module）、加载
配置并解析限速覆盖。`--mode incremental` 基于同步状态对已知主题发起条件请求，
只 GET 变化页并可断点续跑（票 #17）；`--mode reconcile --url <主题 URL>` 执行
单页端到端全量对账（票 #15）；`--mode reconcile [--limit N]` 执行清单驱动全量
对账（sitemap → en 清单 → HEAD → zh 镜像 → 完整管道 → 图片验证 → 例外表 →
自检，票 #16/#20）；`--mode check [--module M]` 本地抽查模板——机器检查 100%、
转换质量按模块抽样（每模块 ≥5% 且 ≥10 页，票 #20 AC4）。
"""
from __future__ import annotations

import argparse
import sys
from urllib.parse import urlparse

import sync_config
import sync_engine

STATE_FILE_REL = sync_engine.STATE_FILE_REL

# check 模式不抓取（只读本地 data/ 产物），不是 effective_rate 的 fetch 模式。
CLI_MODES = sync_config.MODES + ("check",)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="run_sync.py",
        description="Monitor ERP 知识库同步 CLI（单 URL 与清单驱动全量对账）",
    )
    ap.add_argument("--mode", required=True, choices=CLI_MODES,
                    help="incremental=日常增量 | reconcile=全量对账 | check=抽查模板")
    ap.add_argument("--url", metavar="URL",
                    help="只处理单个主题 URL（与 --limit 互斥）")
    ap.add_argument("--limit", metavar="N", type=int,
                    help="最多处理 N 个 URL（与 --url 互斥）")
    ap.add_argument("--rate", metavar="REQ/S", type=float,
                    help="覆盖当前模式限速（必须 > 0）")
    ap.add_argument("--dry-run", action="store_true",
                    help="只预览本轮将抓取的 URL，不写任何产物")
    ap.add_argument("--module", metavar="NAME",
                    help="check 模式限定单模块（topic_path 首段，如 UserGuide）")
    return ap


def parse_args(argv=None) -> argparse.Namespace:
    ap = build_parser()
    ns = ap.parse_args(argv)
    if ns.mode == "check" and (ns.url is not None or ns.limit is not None
                               or ns.rate is not None or ns.dry_run):
        ap.error("--mode check 只读本地数据集，不使用 --url/--limit/--rate/--dry-run")
    if ns.module is not None and ns.mode != "check":
        ap.error("--module 只用于 --mode check（限定抽查模块）")
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

    if args.mode == "check":
        return sync_engine.check_dataset_sampled(cfg, module=args.module)

    rate = sync_config.effective_rate(cfg, args.mode, args.rate)
    mode_cfg = getattr(cfg, args.mode)
    if args.mode == "incremental":
        return sync_engine.incremental_sync(args.limit, args.url, cfg, rate,
                                            dry_run=args.dry_run)
    if args.mode == "reconcile" and args.url is not None and not args.dry_run:
        return sync_engine.reconcile_single_url(args.url, cfg, rate)
    if args.mode == "reconcile" and args.url is None and not args.dry_run:
        return sync_engine.reconcile_manifest(args.limit, cfg, rate)
    if args.url is not None:
        scope = f"单 URL: {args.url}"
    elif args.limit is not None:
        scope = f"最多 {args.limit} 个 URL"
    else:
        scope = "全部清单 URL"
    rate_line = f"{rate} req/s"
    if args.rate is not None:
        rate_line += f"（配置 {mode_cfg.rate_per_sec}，由 --rate 覆盖）"

    print("== run_sync 计划 ==")
    print(f"模式: {args.mode}")
    print(f"范围: {scope}")
    print(f"限速: {rate_line}")
    print(f"UA: {cfg.user_agent}")
    print(f"退避: {cfg.backoff.base_seconds}s → {cfg.backoff.max_seconds}s（指数）")
    print(f"停止阈值: 连续失败 {cfg.stop_conditions.consecutive_failures} 次 "
          f"或错误率 > {cfg.stop_conditions.error_rate_percent}%")
    print(f"dry-run: {'是' if args.dry_run else '否'}")
    print(f"状态文件: {STATE_FILE_REL}")
    if args.mode == "reconcile" and args.url is not None:
        print("提示: --dry-run 只预览；去掉后执行单 URL 全量对账"
              "（抓取→清洗→元数据→分块→自检）。")
    else:
        print("提示: --dry-run 只预览；去掉后执行清单驱动全量对账"
              "（sitemap → en 清单 → HEAD 校验 → zh 镜像扫描 → 完整管道 → "
              "例外表 → 自检）；--limit N 限定本轮主题数。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
