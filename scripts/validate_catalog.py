#!/usr/bin/env python3
"""Validate the clustering-paper catalog using the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "papers.json"
REQUIRED = {"id", "title", "acronym", "authors", "year", "venue", "tags", "paper", "code", "status", "note"}
TAG_ORDER = ["BIO", "HG", "LLM"]
STATUSES = {"peer-reviewed", "preprint", "forthcoming"}


def is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    papers = data.get("papers")
    errors: list[str] = []

    if data.get("tag_order") != TAG_ORDER:
        errors.append(f"tag_order must be {TAG_ORDER}")
    if not isinstance(papers, list) or not papers:
        errors.append("catalog must contain a non-empty papers list")
        papers = []

    seen_ids: set[str] = set()
    seen_titles: set[str] = set()
    previous_year = 10_000

    for index, item in enumerate(papers, start=1):
        label = item.get("id", f"record-{index}")
        missing = REQUIRED - item.keys()
        extra = item.keys() - REQUIRED
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
        if extra:
            errors.append(f"{label}: unknown fields {sorted(extra)}")
        if missing:
            continue

        if not re.fullmatch(r"[a-z0-9-]+", item["id"]):
            errors.append(f"{label}: id must use lowercase letters, digits, and hyphens")
        if item["id"] in seen_ids:
            errors.append(f"{label}: duplicate id")
        seen_ids.add(item["id"])

        normalized_title = " ".join(item["title"].casefold().split())
        if normalized_title in seen_titles:
            errors.append(f"{label}: duplicate title")
        seen_titles.add(normalized_title)

        year = item["year"]
        if not isinstance(year, int) or not 2000 <= year <= 2027:
            errors.append(f"{label}: invalid year {year!r}")
        elif year > previous_year:
            errors.append(f"{label}: records must be ordered by year descending")
        else:
            previous_year = year

        tags = item["tags"]
        if not isinstance(tags, list) or not tags:
            errors.append(f"{label}: tags must be a non-empty list")
        elif len(tags) != len(set(tags)) or any(tag not in TAG_ORDER for tag in tags):
            errors.append(f"{label}: invalid or duplicate tags {tags!r}")
        elif tags != [tag for tag in TAG_ORDER if tag in tags]:
            errors.append(f"{label}: tags must follow canonical order {TAG_ORDER}")

        if item["status"] not in STATUSES:
            errors.append(f"{label}: invalid status {item['status']!r}")
        for field in ("paper", "code"):
            if item[field] and not is_url(item[field]):
                errors.append(f"{label}: {field} must be an HTTP(S) URL")
        if not item["paper"] and item["status"] != "forthcoming":
            errors.append(f"{label}: only forthcoming records may omit a paper URL")
        for field in ("title", "authors", "venue", "note"):
            if not isinstance(item[field], str) or not item[field].strip():
                errors.append(f"{label}: {field} must be a non-empty string")
        if not item["note"].endswith("."):
            errors.append(f"{label}: note must end with a period")

    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(papers)} records across {', '.join(TAG_ORDER)} (snapshot {data['snapshot_date']}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
