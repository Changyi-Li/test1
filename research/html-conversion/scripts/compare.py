#!/usr/bin/env python3
"""Compare HTML->Markdown conversion approaches on Flare WebHelp2 topic pages.

Usage:
    compare.py <input.html>... --out <output_dir>

Tools compared:
  1. trafilatura (markdown output)
  2. readability-lxml (extract article) + pandoc (HTML->Markdown)
  3. pandoc on the raw page (no cleaning)
  4. custom BeautifulSoup pipeline (#contentBody extraction + element walk)

Writes one Markdown file per tool per input, plus a summary file.
"""

import argparse
import pathlib
import re
import sys
from bs4 import BeautifulSoup
import trafilatura
from readability import Document
import pypandoc


def inline_md(el):
    """Convert inline content (text, links, images, code, br) to Markdown."""
    out = []
    for child in el.children:
        if getattr(child, "name", None) is None:
            out.append(child.string or "")
            continue
        name = child.name.lower()
        if name == "br":
            out.append("\n")
        elif name == "img":
            alt = child.get("alt", "") or ""
            src = child.get("src", "") or ""
            out.append(f"![{alt}]({src})")
        elif name == "a":
            txt = re.sub(r"\s+", " ", child.get_text(" ", strip=True))
            href = child.get("href", "") or ""
            if txt and href and not href.startswith("#"):
                out.append(f"[{txt}]({href})")
            elif txt:
                out.append(txt)
        elif name == "code":
            out.append("`" + (child.get_text() or "") + "`")
        elif name in ("span", "strong", "em", "b", "i", "u", "sup", "sub", "font"):
            out.append(inline_md(child))
        else:
            out.append(re.sub(r"\s+", " ", child.get_text(" ", strip=True)))
    text = "".join(out)
    return re.sub(r"[ \t]+", " ", text).strip()


def table_md(table):
    rows = []
    for tr in table.find_all("tr"):
        cells = [inline_md(c) or " " for c in tr.find_all(["th", "td"])]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |"]
    lines.append("|" + "---|" * ncols)
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def custom_convert(raw):
    soup = BeautifulSoup(raw, "lxml")
    body = soup.select_one("#contentBody") or soup.select_one(".body-container") or soup.body
    lines = []

    def walk(el):
        for child in el.children:
            if getattr(child, "name", None) is None:
                continue
            name = child.name.lower()
            if name in ("script", "style", "nav", "header", "footer", "aside"):
                continue
            if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = int(name[1])
                txt = inline_md(child) or " "
                lines.append("\n" + "#" * level + " " + txt)
            elif name == "p":
                t = inline_md(child)
                if t:
                    cls = " ".join(child.get("class", [])) or ""
                    if re.search(r"note|warning|tip|important|alert|caution", cls, re.I):
                        lines.append("> " + t)
                    else:
                        lines.append(t)
            elif name == "ul":
                for li in child.find_all("li", recursive=False):
                    t = inline_md(li)
                    if t:
                        lines.append("- " + t)
            elif name == "ol":
                for i, li in enumerate(child.find_all("li", recursive=False), 1):
                    t = inline_md(li)
                    if t:
                        lines.append(f"{i}. " + t)
            elif name == "table":
                t = table_md(child)
                if t:
                    lines.append(t)
            elif name == "pre":
                lines.append("```\n" + (child.get_text() or "") + "\n```")
            elif name == "img":
                alt = child.get("alt", "") or ""
                src = child.get("src", "") or ""
                lines.append(f"![{alt}]({src})")
            elif name == "blockquote":
                t = inline_md(child)
                if t:
                    lines.append("> " + t)
            elif name in ("div", "section", "article", "figure", "span", "main"):
                cls = " ".join(child.get("class", [])) or ""
                if re.search(r"note|warning|tip|important|alert|caution|callout", cls, re.I):
                    t = inline_md(child)
                    if t:
                        lines.append("> " + t)
                else:
                    walk(child)
            elif name in ("dl",):
                for dt in child.find_all("dt", recursive=False):
                    lines.append("**" + inline_md(dt) + "**")
                for dd in child.find_all("dd", recursive=False):
                    t = inline_md(dd)
                    if t:
                        lines.append(": " + t)

    walk(body)
    return "\n".join(x for x in lines if x)


def stats(md_text):
    return {
        "chars": len(md_text),
        "headings": len(re.findall(r"^#{1,6} ", md_text, re.M)),
        "links": len(re.findall(r"\[[^\]]+\]\([^)]+\)", md_text)),
        "images": len(re.findall(r"!\[[^\]]*\]\([^)]+\)", md_text)),
        "tables": len(re.findall(r"^\|.*\|$", md_text, re.M)),
        "lines": len(md_text.splitlines()),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    summary = ["# Conversion comparison summary", ""]

    for inp in args.inputs:
        path = pathlib.Path(inp)
        raw = path.read_text(encoding="utf-8", errors="replace")
        url = re.search(r'data-mc-path-to-help-system="([^"]*)"', raw)
        stem = path.stem
        results = {}

        converters = {
            "trafilatura": lambda: trafilatura.extract(
                raw, output_format="markdown", include_comments=False,
                include_tables=True, with_metadata=False, include_links=True,
            ) or "",
            "readability_pandoc": lambda: pypandoc.convert_text(
                Document(raw).summary(), "markdown", format="html",
                extra_args=["--wrap=none"],
            ),
            "pandoc_raw": lambda: pypandoc.convert_text(
                raw, "markdown", format="html", extra_args=["--wrap=none"],
            ),
            "custom_bs4": lambda: custom_convert(raw),
        }
        for tool, fn in converters.items():
            try:
                md = fn()
            except Exception as exc:  # pragma: no cover - tool-specific failures
                md = f"ERROR: {exc}"
            out_file = out_dir / f"out-{tool}-{stem}.md"
            out_file.write_text(md, encoding="utf-8")
            results[tool] = stats(md)

        summary.append(f"## {stem}")
        summary.append("")
        header = "| tool | chars | headings | links | images | table rows | lines |"
        sep = "|---|---|---|---|---|---|---|"
        summary.append(header)
        summary.append(sep)
        for tool, s in results.items():
            summary.append(
                f"| {tool} | {s['chars']} | {s['headings']} | {s['links']} | "
                f"{s['images']} | {s['tables']} | {s['lines']} |"
            )
        summary.append("")

    (out_dir / "summary.md").write_text("\n".join(summary), encoding="utf-8")
    print("\n".join(summary))


if __name__ == "__main__":
    sys.exit(main())
