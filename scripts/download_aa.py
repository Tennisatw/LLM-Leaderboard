"""Download Artificial Analysis evaluation pages.

Artificial Analysis evaluation pages only show full results for the currently
selected models. The selection is encoded in the URL query param `models=...`.

You maintain a global models list in:
  scripts/aa_model.txt

This script loads each evaluation page with that models list and saves an MHTML
snapshot (default) for the existing parsers.

Usage
  python scripts/download_aa.py --out 26-01-18/pages

Notes
- MHTML is captured via Chrome DevTools Protocol: Page.captureSnapshot.
- If snapshot capture fails, we fall back to saving plain HTML.
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
        name="aa-gpqa-diamond",
        url="https://artificialanalysis.ai/evaluations/gpqa-diamond",
        filename="GPQA Diamond Benchmark Leaderboard _ Artificial Analysis.mhtml",
    ),
    Target(
        name="aa-mmlu-pro",
        url="https://artificialanalysis.ai/evaluations/mmlu-pro",
        filename="MMLU-Pro Benchmark Leaderboard _ Artificial Analysis.mhtml",
    ),
    Target(
        name="aa-humanitys-last-exam",
        url="https://artificialanalysis.ai/evaluations/humanitys-last-exam",
        filename="Humanity's Last Exam Benchmark Leaderboard _ Artificial Analysis.mhtml",
    ),
    Target(
        name="aa-aime-2025",
        url="https://artificialanalysis.ai/evaluations/aime-2025",
        filename="AIME 2025 Benchmark Leaderboard _ Artificial Analysis.mhtml",
    ),
    Target(
        name="aa-livecodebench",
        url="https://artificialanalysis.ai/evaluations/livecodebench",
        filename="LiveCodeBench Benchmark Leaderboard _ Artificial Analysis.mhtml",
    ),
    Target(
        name="aa-aalcr",
        url="https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning",
        filename="Artificial Analysis Long Context Reasoning Benchmark Leaderboard _ Artificial Analysis.mhtml",
    ),
    Target(
        name="aa-ifbench",
        url="https://artificialanalysis.ai/evaluations/ifbench",
        filename="IFBench Benchmark Leaderboard _ Artificial Analysis.mhtml",
    ),
    Target(
        name="aa-terminalbench-hard",
        url="https://artificialanalysis.ai/evaluations/terminalbench-hard",
        filename="Terminal-Bench Hard Benchmark Leaderboard _ Artificial Analysis.mhtml",
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
        html = page.content()
        path.write_bytes(html.encode("utf-8"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out",
        type=str,
        default="pages",
        help="Output folder (relative to repo root unless absolute)",
    )
    ap.add_argument(
        "--models-file",
        type=str,
        default=str(Path(__file__).resolve().parent / "aa_model.txt"),
        help="Path to URL-encoded models list (value of models=...)",
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
    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = repo_root / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    models_value = Path(args.models_file).read_text(encoding="utf-8").strip()
    if not models_value:
        raise SystemExit(f"Empty models list: {args.models_file}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=args.headless)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(args.timeout_ms)

        for t in TARGETS:
            fetch_url = f"{t.url}{models_value}"
            print(f"Downloading: {t.name} -> {fetch_url}")
            page.goto(fetch_url, wait_until="networkidle")

            out_path = out_dir / t.filename
            _save_mhtml(page, out_path)
            print(f"Saved: {out_path}")

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
