#!/usr/bin/env python3
"""Audit every expected R2 visual and playable video from the source manifest."""

from __future__ import annotations

import argparse
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check(url: str) -> tuple[str, int, str]:
    command = [
        "curl", "-L", "-sS", "--retry", "4", "--retry-all-errors", "--connect-timeout", "10",
        "--max-time", "45", "--range", "0-31", "--output", "/dev/null", "--write-out",
        "%{http_code} %{content_type}", url,
    ]
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    parts = result.stdout.strip().split(maxsplit=1)
    status = int(parts[0]) if parts and parts[0].isdigit() else 0
    content_type = parts[1].split(";", 1)[0] if len(parts) > 1 else ""
    return url, status, content_type


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((ROOT / "data/source-fidelity-manifest.json").read_text(encoding="utf-8"))
    visuals = [url for case in manifest["cases"] for url in case["expected_public_media_urls"]]
    videos = [case["playable_video_url"] for case in manifest["cases"] if case.get("playable_video_url")]
    urls = list(dict.fromkeys([*visuals, *videos]))
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = {url: (status, kind) for url, status, kind in pool.map(check, urls)}
    failures = []
    for url in visuals:
        status, kind = results[url]
        if status not in {200, 206} or not kind.startswith("image/"):
            failures.append(f"visual status={status} type={kind or '<missing>'} url={url}")
    for url in videos:
        status, kind = results[url]
        if status not in {200, 206} or kind != "video/mp4":
            failures.append(f"video status={status} type={kind or '<missing>'} url={url}")
    passed = not failures and len(visuals) == 42 and len(videos) == 24
    lines = [
        "# R2 Source Media Audit v1", "", f"- Status: `{'passed' if passed else 'failed'}`",
        f"- Expected visual media: {len(visuals)}", f"- Checked visual media: {sum(results[url][0] in {200, 206} for url in visuals)}",
        f"- Expected playable videos: {len(videos)}", f"- Checked playable videos: {sum(results[url][0] in {200, 206} for url in videos)}",
        f"- Failures: {len(failures)}", f"- Command exit code: {0 if passed else 1}",
        f"- Result: {'pass' if passed else 'fail'}",
    ]
    if failures:
        lines.extend(["", "## Failures", "", *[f"- {failure}" for failure in failures]])
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("PASS" if passed else "FAIL")
    print(f"visuals={len(visuals)} videos={len(videos)} failures={len(failures)}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
