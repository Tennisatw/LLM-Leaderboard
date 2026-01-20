"""Download leaderboard pages as MHTML.

This repo already parses saved .mhtml files under a dated folder's `pages/`.
This script automates downloading a few known pages.

Notes
- MHTML is not a standard HTTP response type. Most sites won't serve it directly.
- So we use Playwright (Chromium) to load the page and then save a snapshot.

Usage
  python scripts/download_pages.py --out 25-12-14

It will create:
  <out>/pages/*.mhtml

Then you can run the existing get_*.py parsers against those files.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import sync_playwright


@dataclass(frozen=True)
class Target:
    name: str
    url: str
    filename: str


TARGETS: list[Target] = [
    Target(
        name="lmarena-text",
        url="https://lmarena.ai/leaderboard/text",
        filename="Text Arena _ LMArena.mhtml",
    ),
    Target(
        name="lmarena-vision",
        url="https://lmarena.ai/leaderboard/vision",
        filename="Vision Arena _ LMArena.mhtml",
    ),
    Target(
        name="vals-swebench",
        url="https://www.vals.ai/benchmarks/swebench",
        filename="SWE-bench.mhtml",
    ),
]


def _save_mhtml(page, path: Path) -> None:
    # MHTML is a MIME message. Preserve bytes as-is.
    try:
        cdp = page.context.new_cdp_session(page)
        res = cdp.send("Page.captureSnapshot", {"format": "mhtml"})
        data = res["data"]  # str
        path.write_bytes(data.encode("latin-1", errors="ignore"))
        return
    except Exception:
        # Fallback: save HTML (not MHTML). Still write bytes to avoid newline mangling.
        html = page.content()
        path.write_bytes(html.encode("utf-8"))


def _expand_vals_swebench(page) -> None:
    # The page shows only top N models by default.
    # Button text looks like: "See 35 more models".
    btn = page.locator("button:has-text('more models')").first
    if btn.count() == 0:
        return

    btn.scroll_into_view_if_needed()

    # Capture current row count, then click and wait for it to increase.
    rows = page.locator("div.background-primary a")
    before = rows.count()

    btn.click()

    try:
        page.wait_for_function(
            "([sel, before]) => document.querySelectorAll(sel).length > before",
            arg=["div.background-primary a", before],
            timeout=15_000,
        )
    except Exception:
        # Fallback: wait a bit for animation / client-side render.
        page.wait_for_timeout(1500)



def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out",
        type=str,
        default="pages",
        help="Output folder name under repo root",
    )
    ap.add_argument(
        "--headless",
        action="store_true",
        help="Run browser headless (default: false for easier debugging)",
    )
    ap.add_argument(
        "--timeout-ms",
        type=int,
        default=90_000,
        help="Navigation timeout in ms",
    )
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    out_dir = repo_root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=args.headless)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(args.timeout_ms)

        for t in TARGETS:
            print(f"Downloading: {t.name} -> {t.url}")
            page.goto(t.url, wait_until="networkidle")
            if t.name == "vals-swebench":
                _expand_vals_swebench(page)

            _save_mhtml(page, out_dir / t.filename)
            print(f"Saved: {out_dir / t.filename}")

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
