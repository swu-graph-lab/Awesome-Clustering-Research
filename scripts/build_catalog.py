#!/usr/bin/env python3
"""Render README catalog tables from data/papers.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "papers.json"
README = ROOT / "README.md"
START = "<!-- CATALOG:START -->"
END = "<!-- CATALOG:END -->"
META_PREFIX = "> **Snapshot:**"

SECTIONS = [
    ("surveys", "Surveys and perspectives"),
    ("benchmarks", "Benchmarks and evaluation"),
    ("general_models", "General-purpose graph models"),
    ("node_structure", "Node classification and structure learning"),
    ("clustering", "Graph clustering and community detection"),
]


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def link(label: str, url: str) -> str:
    return f"[{label}]({url})" if url else "—"


def render_record(item: dict) -> str:
    display = f"**{esc(item['acronym'])}** — {esc(item['title'])}" if item["acronym"] else esc(item["title"])
    title = link(display, item["paper"]) if item["paper"] else display
    roles = ", ".join(f"`{esc(role)}`" for role in item["roles"])
    status = f"`{esc(item['status'])}`"
    return (
        f"| {item['year']} | {esc(item['venue'])} | {title} | {roles} | "
        f"{link('code', item['code'])} | {status} | {esc(item['note'])} |"
    )


def render_catalog(papers: list[dict]) -> str:
    blocks: list[str] = []
    for key, heading in SECTIONS:
        records = [item for item in papers if item["section"] == key]
        records.sort(key=lambda item: (-item["year"], item["title"].lower()))
        blocks.extend(
            [
                f"### {heading}",
                "",
                "| Year | Venue | Paper | LLM role(s) | Code | Status | Why it matters |",
                "| ---: | --- | --- | --- | --- | --- | --- |",
                *(render_record(item) for item in records),
                "",
            ]
        )
    return "\n".join(blocks).rstrip()


def update_readme(content: str, generated: str, snapshot_date: str, count: int) -> str:
    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError("README must contain exactly one catalog marker pair")
    before, rest = content.split(START, 1)
    _, after = rest.split(END, 1)
    updated = f"{before}{START}\n{generated}\n{END}{after}"
    lines = updated.splitlines()
    matches = [index for index, line in enumerate(lines) if line.startswith(META_PREFIX)]
    if len(matches) != 1:
        raise ValueError("README must contain exactly one snapshot metadata line")
    lines[matches[0]] = (
        f"> **Snapshot:** {snapshot_date} · **Catalog:** {count} entries · "
        "[中文说明](README_zh-CN.md)"
    )
    return "\n".join(lines) + ("\n" if updated.endswith("\n") else "")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if README is not up to date")
    args = parser.parse_args()

    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    current = README.read_text(encoding="utf-8")
    updated = update_readme(
        current,
        render_catalog(data["papers"]),
        data["snapshot_date"],
        len(data["papers"]),
    )

    if args.check:
        if updated != current:
            print("README catalog is stale; run python scripts/build_catalog.py")
            return 1
        print("README catalog is up to date.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"Rendered {len(data['papers'])} records into {README.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
