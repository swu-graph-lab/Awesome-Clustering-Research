#!/usr/bin/env python3
"""Generate the README catalog and GitHub Pages data from data/papers.json."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "papers.json"
README = ROOT / "README.md"
SITE_DATA = ROOT / "docs" / "papers.json"
START = "<!-- CATALOG:START -->"
END = "<!-- CATALOG:END -->"
META_PREFIX = "> **Snapshot:**"


def link(label: str, url: str) -> str:
    return f"[{label}]({url})" if url else ""


def render_record(item: dict) -> str:
    badge = "+".join(item["tags"])
    name = f"**{item['acronym']}** — {item['title']}" if item["acronym"] and not item["title"].startswith(item["acronym"]) else f"**{item['title']}**"
    name = link(name, item["paper"]) if item["paper"] else name
    resources = [link("Paper", item["paper"]), link("Code", item["code"])]
    resources = " · ".join(resource for resource in resources if resource)
    suffix = f" {resources}" if resources else ""
    return f"- `[{badge}]` {name} — {item['authors']}. *{item['venue']}*.{suffix}"


def render_catalog(papers: list[dict]) -> str:
    by_year: dict[int, list[dict]] = defaultdict(list)
    for item in papers:
        by_year[item["year"]].append(item)
    lines: list[str] = []
    for year in sorted(by_year, reverse=True):
        lines.extend([f"### {year}", ""])
        lines.extend(render_record(item) for item in by_year[year])
        lines.append("")
    return "\n".join(lines).rstrip()


def updated_readme(current: str, generated: str, snapshot: str, count: int) -> str:
    if current.count(START) != 1 or current.count(END) != 1:
        raise ValueError("README must contain exactly one catalog marker pair")
    before, rest = current.split(START, 1)
    _, after = rest.split(END, 1)
    result = f"{before}{START}\n{generated}\n{END}{after}"
    lines = result.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith(META_PREFIX)]
    if len(matches) != 1:
        raise ValueError("README must contain exactly one snapshot line")
    lines[matches[0]] = f"> **Snapshot:** {snapshot} · **Catalog:** {count} papers · [中文说明](README_zh-CN.md)"
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    current = README.read_text(encoding="utf-8")
    readme = updated_readme(current, render_catalog(data["papers"]), data["snapshot_date"], len(data["papers"]))
    site_data = json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        stale = []
        if readme != current:
            stale.append("README.md")
        if not SITE_DATA.exists() or SITE_DATA.read_text(encoding="utf-8") != site_data:
            stale.append("docs/papers.json")
        if stale:
            print(f"Generated files are stale: {', '.join(stale)}")
            return 1
        print("README and site data are up to date.")
        return 0

    README.write_text(readme, encoding="utf-8")
    SITE_DATA.write_text(site_data, encoding="utf-8")
    print(f"Rendered {len(data['papers'])} records into README.md and docs/papers.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
