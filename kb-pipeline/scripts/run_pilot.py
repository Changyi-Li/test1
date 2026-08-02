"""Getting Started 双语试点：一键跑通 抓取 → 清洗 → 元数据 → 分块 → 自检。

用法：py kb-pipeline/scripts/run_pilot.py [--stage fetch|clean|metadata|chunk|check]
默认全跑。所有产物落在 kb-pipeline/data/ 下。清单取自 pipeline.pilot_manifest()。
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time

import pipeline as P

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
CLEAN = ROOT / "data" / "clean"
META = ROOT / "data" / "metadata.jsonl"
CHUNKS = ROOT / "data" / "chunks.jsonl"
HEADERS = RAW / "headers.json"
TOPICS_JSON = ROOT / "data" / "topics.json"
CHECK_TXT = ROOT / "data" / "selfcheck-results.txt"

ID_FILE = lambda tid: CLEAN / (tid.replace("/", "_") + ".md")  # noqa: E731

# schema 常量已上移共享库 pipeline.py（规格 §4.1/§4.2）
EXPECTED_FIELDS_META = P.EXPECTED_FIELDS_META
EXPECTED_FIELDS_CHUNK = P.EXPECTED_FIELDS_CHUNK


def load_headers() -> dict:
    if HEADERS.exists():
        return json.loads(HEADERS.read_text(encoding="utf-8"))
    return {}


def fetch(manifest: P.Manifest) -> None:
    headers = load_headers()
    RAW.mkdir(parents=True, exist_ok=True)
    for t in manifest.topics:
        url = P.topic_url(manifest, t["lang"], t["page"])
        raw = P.probe(manifest, url, headers)
        if raw:
            (RAW / t["lang"] / t["page"]).parent.mkdir(parents=True, exist_ok=True)
            (RAW / t["lang"] / t["page"]).write_bytes(raw)
            print(f"fetched {t['lang']} {t['page']} ({len(raw)} bytes)")
        time.sleep(manifest.fetch_sleep)
    for zh_page in manifest.zh_probes:
        url = P.topic_url(manifest, "zh-cn", zh_page)
        raw = P.probe(manifest, url, headers)
        if raw:
            (RAW / "zh-cn" / zh_page).parent.mkdir(parents=True, exist_ok=True)
            (RAW / "zh-cn" / zh_page).write_bytes(raw)
            print(f"fetched zh-cn {zh_page} ({len(raw)} bytes)")
        else:
            status = headers.get(url, {}).get("status")
            print(f"zh-cn {zh_page}: {status}")
        time.sleep(manifest.fetch_sleep)
    HEADERS.write_text(json.dumps(headers, ensure_ascii=False, indent=2), encoding="utf-8")


def build_rows(manifest: P.Manifest) -> list[dict]:
    headers = load_headers()
    rows = []
    for t in manifest.topics:
        en_url = P.topic_url(manifest, t["lang"], t["page"])
        en_raw = (RAW / t["lang"] / t["page"]).read_bytes() if (RAW / t["lang"] / t["page"]).exists() else None
        if en_raw is None:
            continue
        md = P.clean_markdown(en_raw.decode("utf-8", errors="replace"), en_url)
        rows.append({
            "lang": "en-us", "page": t["page"], "id": P.topic_id(manifest, "en-us", t["page"]),
            "url": en_url, "raw": str(RAW / "en-us" / t["page"]),
            "clean": str(ID_FILE(P.topic_id(manifest, "en-us", t["page"]))),
            "md": md, "zh_page": t["zh_page"],
        })
    for t in manifest.topics:
        zh_path = RAW / "zh-cn" / t["zh_page"]
        if not zh_path.exists():
            continue
        zh_url = P.topic_url(manifest, "zh-cn", t["zh_page"])
        md = P.clean_markdown(zh_path.read_bytes().decode("utf-8", errors="replace"), zh_url)
        rows.append({
            "lang": "zh-cn", "page": t["zh_page"], "id": P.topic_id(manifest, "zh-cn", t["zh_page"]),
            "url": zh_url, "raw": str(zh_path),
            "clean": str(ID_FILE(P.topic_id(manifest, "zh-cn", t["zh_page"]))),
            "md": md, "zh_page": t["zh_page"],
        })
    return rows


def clean_stage(manifest: P.Manifest) -> None:
    rows = build_rows(manifest)
    CLEAN.mkdir(parents=True, exist_ok=True)
    for r in rows:
        ID_FILE(r["id"]).write_text(r["md"], encoding="utf-8")
        print(f"cleaned {r['id']} -> {ID_FILE(r['id']).name} ({len(r['md'])} chars)")


def metadata_stage(manifest: P.Manifest) -> None:
    rows = build_rows(manifest)
    headers = load_headers()
    en_by_page = {t["page"]: P.topic_id(manifest, "en-us", t["page"]) for t in manifest.topics}
    zh_by_page = {t["zh_page"]: P.topic_id(manifest, "zh-cn", t["zh_page"]) for t in manifest.topics}
    zh_discovered = {t["zh_page"] for t in manifest.topics if (RAW / "zh-cn" / t["zh_page"]).exists()}
    out = []
    for r in rows:
        md = r["md"]
        raw_file = RAW / r["lang"] / (r["id"].rsplit("/", 1)[-1] + ".htm")
        raw_html = raw_file.read_bytes().decode("utf-8", errors="replace")
        h = headers.get(r["url"], {})
        images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md)
        quality = "canonical" if r["lang"] == "en-us" else "reference"
        paired: str | None = None
        if r["lang"] == "en-us":
            zh_page = r["zh_page"]
            if zh_page in zh_discovered:
                paired = zh_by_page[zh_page]
        else:
            en_page = next((t["page"] for t in manifest.topics if t["zh_page"] == r["page"]), None)
            if en_page:
                paired = en_by_page[en_page]
        out.append({
            "id": r["id"],
            "title": P.extract_title(md, raw_html),
            "url": r["url"],
            "source": manifest.source,
            "version": P.extract_version(raw_html),
            "language": r["lang"],
            "topic_path": manifest.topic_path,
            "quality": quality,
            "lastmod": h.get("lastmod"),
            "etag": h.get("etag"),
            "content_hash": P.sha256_hex(md),
            "images": images,
            "paired_topic_id": paired,
        })
    out.sort(key=lambda x: (x["language"], x["id"]))
    META.write_text("\n".join(json.dumps(o, ensure_ascii=False) for o in out) + "\n", encoding="utf-8")
    print(f"metadata: {len(out)} rows -> {META.name}")


def chunk_stage() -> None:
    rows = []
    for line in META.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    out = []
    pos_by_chunk = {}
    en_pos = {}
    for r in rows:
        md = ID_FILE(r["id"]).read_text(encoding="utf-8")
        chunks = P.chunk_markdown(md)
        for order, c in enumerate(chunks):
            content = c["content"]
            pos_by_chunk[f"{r['id']}::{order}"] = c["pos"]
            chunk = {
                "chunk_id": f"{r['id']}::{order}",
                "topic_id": r["id"],
                "order": order,
                "title": r["title"],
                "heading_path": [p["text"] for p in c["path"]],
                "content": content,
                "language": r["language"],
                "quality": r["quality"],
                "url": r["url"],
                "topic_path": r["topic_path"],
                "images": re.findall(r"!\[[^\]]*\]\(([^)]+)\)", content),
                "paired_chunk_id": None,
                "char_count": len(content),
                "token_estimate": P.est_tokens(content),
            }
            out.append(chunk)
            if r["language"] == "en-us":
                en_pos[(r["id"], c["pos"])] = chunk["chunk_id"]
    for chunk in out:
        r = next(row for row in rows if row["id"] == chunk["topic_id"])
        if r["language"] == "zh-cn" and r["paired_topic_id"]:
            chunk["paired_chunk_id"] = en_pos.get(
                (r["paired_topic_id"], pos_by_chunk.get(chunk["chunk_id"], ())), None)
    # 二次配对：zh 块按位置路径重新匹配（chunk.pos 未存，按 heading_path 文本序列兜底）
    if any(c["paired_chunk_id"] is None for c in out if c["language"] == "zh-cn"):
        en_by_path: dict[tuple[str, ...], list[str]] = {}
        for chunk in out:
            if chunk["language"] == "en-us":
                en_by_path.setdefault(tuple(chunk["heading_path"]), []).append(chunk["chunk_id"])
        for chunk in out:
            if chunk["language"] == "zh-cn" and chunk["paired_chunk_id"] is None:
                r = next(row for row in rows if row["id"] == chunk["topic_id"])
                if r["paired_topic_id"]:
                    key = tuple(chunk["heading_path"])
                    cands = en_by_path.get(key, [])
                    if cands:
                        chunk["paired_chunk_id"] = cands[0]
    out.sort(key=lambda x: (x["topic_id"], x["order"]))
    CHUNKS.write_text("\n".join(json.dumps(o, ensure_ascii=False) for o in out) + "\n", encoding="utf-8")
    print(f"chunks: {len(out)} rows -> {CHUNKS.name}")


def check_stage(manifest: P.Manifest) -> bool:
    rows = [json.loads(line) for line in META.read_text(encoding="utf-8").splitlines() if line.strip()]
    chunks = [json.loads(line) for line in CHUNKS.read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = {r["id"] for r in rows}
    lines = []
    ok = True

    def report(name, passed, detail=""):
        nonlocal ok
        ok = ok and passed
        lines.append(f"[{'PASS' if passed else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

    id_re = rf"(en-us|zh-cn)/{re.escape(manifest.topic_path)}/[A-Za-z0-9_-]+"
    url_re = (rf"{re.escape(manifest.site)}/(en-us|zh-cn)/Content/Topics/"
              rf"{re.escape(manifest.topic_path)}/.+\.htm")

    # ---- 元数据 ----
    report("M1 主题清单 JSONL 可解析且字段集合 = 13 字段", all(set(r) == EXPECTED_FIELDS_META for r in rows),
           f"{len(rows)} rows")
    dups = [r["id"] for r in rows if sum(1 for x in rows if x["id"] == r["id"]) > 1]
    report("M2 id 唯一且符合稳定格式", not dups and all(re.fullmatch(id_re, r["id"]) for r in rows),
           f"dup={dups}")
    report("M3 url 规范且与 language 一致",
           all(re.fullmatch(url_re, r["url"]) and r["url"].split("/")[4] == r["language"] for r in rows))
    report("M4 language 枚举且与 id 前缀一致",
           all(r["language"] in ("en-us", "zh-cn") and r["id"].startswith(r["language"] + "/") for r in rows))
    report("M5 quality 枚举（en→canonical, zh→reference）",
           all((r["language"] == "en-us" and r["quality"] == "canonical") or (r["language"] == "zh-cn" and r["quality"] == "reference") for r in rows))
    report("M6 version/lastmod/etag 非空且 lastmod 为 ISO8601 UTC",
           all(r["version"] and r["etag"] and r["lastmod"] and re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", r["lastmod"]) for r in rows))
    report("M7 images 为绝对 URL 数组",
           all(isinstance(r["images"], list) and all(str(x).startswith("http") for x in r["images"]) for r in rows))
    hash_fail = []
    for r in rows:
        md = ID_FILE(r["id"]).read_text(encoding="utf-8")
        if P.sha256_hex(md) != r["content_hash"]:
            hash_fail.append(r["id"])
    report("M8 content_hash 重算一致", not hash_fail, f"mismatch={hash_fail}")
    # 期望配对表
    expect_pair: dict[str, str | None] = {}
    for t in manifest.topics:
        en = P.topic_id(manifest, "en-us", t["page"])
        zh = P.topic_id(manifest, "zh-cn", t["zh_page"])
        if (RAW / "zh-cn" / t["zh_page"]).exists():
            expect_pair[en] = zh
            expect_pair[zh] = en
        else:
            expect_pair[en] = None
    pair_fail = []
    for r in rows:
        want = expect_pair.get(r["id"], None)
        if want != r["paired_topic_id"]:
            pair_fail.append(f"{r['id']}: want={want} got={r['paired_topic_id']}")
        if r["paired_topic_id"] is not None and r["paired_topic_id"] not in ids:
            pair_fail.append(f"{r['id']}: dangling {r['paired_topic_id']}")
    report("M9 paired_topic_id 引用完整且与镜像映射一致", not pair_fail, "; ".join(pair_fail))

    # ---- 分块 ----
    report("C1 分块 JSONL 可解析且字段集合 = 14 字段", all(set(c) == EXPECTED_FIELDS_CHUNK for c in chunks), f"{len(chunks)} rows")
    cid_fail = [c["chunk_id"] for c in chunks if c["chunk_id"] != f"{c['topic_id']}::{c['order']}" or c["topic_id"] not in ids]
    report("C2 chunk_id 格式与 topic_id 引用", not cid_fail, f"bad={cid_fail}")
    order_fail = []
    by_topic: dict[str, list[int]] = {}
    for c in chunks:
        by_topic.setdefault(c["topic_id"], []).append(c["order"])
    for tid, orders in by_topic.items():
        if sorted(orders) != list(range(len(orders))):
            order_fail.append(tid)
    report("C3 order 每主题 0 起连续", not order_fail, f"bad={order_fail}")
    report("C4 heading_path 非空字符串列表",
           all(isinstance(c["heading_path"], list) and c["heading_path"]
               and all(isinstance(x, str) and x for x in c["heading_path"]) for c in chunks))
    report("C5 content 非空", all(bool(c["content"]) for c in chunks))
    cc_fail = [c["chunk_id"] for c in chunks if c["char_count"] != len(c["content"])]
    report("C6 char_count 与内容一致", not cc_fail, f"bad={cc_fail}")
    ctx = {r["id"]: r for r in rows}
    ctx_fail = []
    for c in chunks:
        r = ctx[c["topic_id"]]
        if not (c["language"] == r["language"] and c["quality"] == r["quality"]
                and c["url"] == r["url"] and c["topic_path"] == r["topic_path"]):
            ctx_fail.append(c["chunk_id"])
    report("C7 块上下文字段与主题清单一致", not ctx_fail, f"bad={ctx_fail}")
    tk_fail = [c["chunk_id"] for c in chunks
               if not isinstance(c["token_estimate"], int) or not (0 < c["token_estimate"] <= 1200)]
    report("C8 token_estimate 为正整数且 ≤ 1200 硬上限", not tk_fail,
           f"bad={tk_fail}; max={max(c['token_estimate'] for c in chunks) if chunks else '-'}")
    en_ids = {c["chunk_id"] for c in chunks if c["language"] == "en-us"}
    pair_fail2 = []
    for c in chunks:
        if c["language"] == "zh-cn":
            if c["paired_chunk_id"] is not None and c["paired_chunk_id"] not in en_ids:
                pair_fail2.append(f"{c['chunk_id']}->{c['paired_chunk_id']}")
            if c["paired_chunk_id"] is not None:
                pt = c["paired_chunk_id"].rsplit("::", 1)[0]
                if pt != ctx[c["topic_id"]]["paired_topic_id"]:
                    pair_fail2.append(f"{c['chunk_id']}->topic {pt}")
        else:
            if c["paired_chunk_id"] is not None:
                pair_fail2.append(f"en {c['chunk_id']} 不应有配对")
    report("C9 中文块 paired_chunk_id 引用真实英文块（英文块为 null）", not pair_fail2, "; ".join(pair_fail2))
    img_fail = []
    for c in chunks:
        if c["images"] != re.findall(r"!\[[^\]]*\]\(([^)]+)\)", c["content"]):
            img_fail.append(c["chunk_id"])
    report("C10 块 images 与内容内图片一致", not img_fail, f"bad={img_fail}")

    # ---- 转换质量代理 ----
    report("--- 转换质量代理（逐页） ---", True)
    for r in rows:
        raw_file = RAW / r["language"] / (r["id"].rsplit("/", 1)[-1] + ".htm")
        raw_html = raw_file.read_bytes().decode("utf-8", errors="replace")
        md = ID_FILE(r["id"]).read_text(encoding="utf-8")
        rb = P.raw_body_stats(raw_html)
        ms = P.md_stats(md)
        noise = [p for p in P.NOISE_PATTERNS if re.search(p, md, re.I)]
        report(f"Q1[{r['id']}] 无导航/页脚/版本/脚本残留", not noise, f"found={noise}")
        rh = [(lv, txt) for lv, txt in rb["headings"]]
        mh = ms["headings"]
        hdiff = []
        for k in range(max(len(rh), len(mh))):
            a = rh[k] if k < len(rh) else None
            b = mh[k] if k < len(mh) else None
            if a != b:
                hdiff.append(f"#{k}: raw={a} md={b}")
        report(f"Q2[{r['id']}] 标题层级/文本一致", not hdiff, "; ".join(hdiff[:4]))
        report(f"Q3[{r['id']}] 正文链接数量一致", len(rb["links"]) == len(ms["links"]),
               f"raw={len(rb['links'])} md={len(ms['links'])}")
        img_abs = all(x.startswith("http") for x in ms["images"])
        report(f"Q4[{r['id']}] 图片数量一致且绝对 URL", len(rb["images"]) == len(ms["images"]) and img_abs,
               f"raw={len(rb['images'])} md={len(ms['images'])} abs={img_abs}")
        report(f"Q5[{r['id']}] 提示框转 blockquote", rb["callouts"] == ms["blockquote_lines"],
               f"raw_callouts={rb['callouts']} md_blockquotes={ms['blockquote_lines']}")
        report(f"Q6[{r['id']}] 表格/代码计数一致",
               rb["tables"] == ms["tables"] and rb["pre"] == ms["code_fences"] // 2,
               f"tables raw={rb['tables']} md={ms['tables']}; pre raw={rb['pre']} fences={ms['code_fences']}")

    txt = "\n".join(lines) + f"\n\nRESULT: {'ALL PASS' if ok else 'HAS FAILURES'}\n"
    CHECK_TXT.write_text(txt, encoding="utf-8")
    print(txt)
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["fetch", "clean", "metadata", "chunk", "check"])
    args = ap.parse_args()
    manifest = P.pilot_manifest()
    stages = [args.stage] if args.stage else ["fetch", "clean", "metadata", "chunk", "check"]
    for s in stages:
        print(f"== stage: {s} ==")
        if s == "fetch":
            fetch(manifest)
        elif s == "clean":
            clean_stage(manifest)
        elif s == "metadata":
            metadata_stage(manifest)
        elif s == "chunk":
            chunk_stage()
        elif s == "check":
            if not check_stage(manifest):
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

