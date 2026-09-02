#!/usr/bin/env python3
"""Validate the machine-readable LLM4GM catalog using only the standard library."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "papers.json"

REQUIRED = {
    "id",
    "title",
    "acronym",
    "year",
    "venue",
    "section",
    "tasks",
    "roles",
    "paper",
    "code",
    "status",
    "note",
}
SECTIONS = {"surveys", "benchmarks", "general_models", "node_structure", "clustering"}
TASKS = {
    "survey",
    "benchmark",
    "general-purpose",
    "node-classification",
    "link-prediction",
    "graph-classification",
    "structure-learning",
    "graph-clustering",
}
ROLES = {"encoder", "annotator", "refiner", "predictor", "aligner", "agent"}
STATUSES = {"peer-reviewed", "preprint", "forthcoming"}


def is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    papers = data.get("papers")
    errors: list[str] = []

    if not isinstance(papers, list) or not papers:
        print("Catalog must contain a non-empty 'papers' list.", file=sys.stderr)
        return 1

    seen_ids: set[str] = set()
    seen_titles: set[str] = set()
    seen_papers: set[str] = set()

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

        if item["id"] in seen_ids:
            errors.append(f"{label}: duplicate id")
        seen_ids.add(item["id"])

        normalized_title = " ".join(item["title"].lower().split())
        if normalized_title in seen_titles:
            errors.append(f"{label}: duplicate title")
        seen_titles.add(normalized_title)

        if item["section"] not in SECTIONS:
            errors.append(f"{label}: invalid section {item['section']!r}")
        if item["status"] not in STATUSES:
            errors.append(f"{label}: invalid status {item['status']!r}")
        if not isinstance(item["year"], int) or not 2000 <= item["year"] <= 2027:
            errors.append(f"{label}: invalid year {item['year']!r}")
        if not isinstance(item["tasks"], list) or not item["tasks"]:
            errors.append(f"{label}: tasks must be a non-empty list")
        elif unknown := set(item["tasks"]) - TASKS:
            errors.append(f"{label}: invalid tasks {sorted(unknown)}")
        if not isinstance(item["roles"], list) or not item["roles"]:
            errors.append(f"{label}: roles must be a non-empty list")
        elif unknown := set(item["roles"]) - ROLES:
            errors.append(f"{label}: invalid roles {sorted(unknown)}")

        for field in ("paper", "code"):
            value = item[field]
            if value and not is_url(value):
                errors.append(f"{label}: {field} is not an HTTP(S) URL")
        if not item["paper"] and item["status"] != "forthcoming":
            errors.append(f"{label}: only forthcoming records may omit a paper URL")
        if item["paper"]:
            canonical = item["paper"].rstrip("/")
            if canonical in seen_papers:
                errors.append(f"{label}: duplicate paper URL")
            seen_papers.add(canonical)
        if not item["note"].endswith("."):
            errors.append(f"{label}: note must end with a period")

    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(papers)} catalog records (snapshot {data['snapshot_date']}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
