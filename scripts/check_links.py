#!/usr/bin/env python3
"""Best-effort external-link checker for catalog URLs."""

from __future__ import annotations

import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "papers.json"


def check(url: str) -> tuple[str, int | str]:
    request = Request(url, headers={"User-Agent": "Awesome-Clustering-Research-link-checker/1.0"})
    for attempt in range(2):
        try:
            with urlopen(request, timeout=20) as response:
                return url, response.status
        except HTTPError as error:
            if error.code in {401, 403, 429}:
                return url, f"soft-{error.code}"
            if attempt == 1:
                return url, error.code
        except (URLError, TimeoutError) as error:
            if attempt == 1:
                return url, type(error).__name__
        time.sleep(1)
    return url, "unknown"


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    urls = sorted({item[field] for item in data["papers"] for field in ("paper", "code") if item[field]})
    failures: list[tuple[str, int | str]] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(check, url) for url in urls]
        for future in as_completed(futures):
            url, result = future.result()
            print(f"{result}\t{url}")
            if isinstance(result, int) and result >= 400:
                failures.append((url, result))
            elif isinstance(result, str) and not result.startswith("soft-"):
                failures.append((url, result))

    if failures:
        print(f"\n{len(failures)} hard link failure(s).", file=sys.stderr)
        return 1
    print(f"\nChecked {len(urls)} URLs; no hard failures.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
