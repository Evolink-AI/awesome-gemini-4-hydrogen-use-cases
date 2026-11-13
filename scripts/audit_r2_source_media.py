#!/usr/bin/env python3
"""Audit every expected R2 visual and playable video from the source manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from verify_repository import INVENTORY_SHA256, validate_source_inventory, validate_fidelity


ROOT = Path(__file__).resolve().parents[1]


def check(url: str) -> tuple[str, int, str]:
    command = [
        "curl", "-L", "-sS", "--connect-timeout", "10",
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
    videos = [url for case in manifest["cases"] for url in case.get("playable_video_urls", [case["playable_video_url"]] if case.get("playable_video_url") else [])]
    inventory_path = ROOT / "data/source-inventory.json"
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    curated = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    failures = validate_source_inventory(curated, inventory) + validate_fidelity(curated["items"], manifest)
    if hashlib.sha256(inventory_path.read_bytes()).hexdigest() != INVENTORY_SHA256:
        failures.append("independent source inventory hash differs")
    expected_media = [asset for case in inventory["cases"] for asset in case["source_media"]]
    expected_visuals = len(expected_media)
    expected_videos = sum(asset["kind"] == "video" for asset in expected_media)
    if len(visuals) != expected_visuals or len(videos) != expected_videos:
        failures.append("public media counts differ from independent frozen source inventory")
    if failures:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text("# R2 Source Media Audit\n\nFAIL: source contract invalid; network check not run\n" + "\n".join(failures) + "\n")
        print("FAIL: source contract invalid; see report")
        return 1
    urls = list(dict.fromkeys([*visuals, *videos]))
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = {url: (status, kind) for url, status, kind in pool.map(check, urls)}
    for url in visuals:
        status, kind = results[url]
        if status not in {200, 206} or not kind.startswith("image/"):
            failures.append(f"visual status={status} type={kind or '<missing>'} url={url}")
    for url in videos:
        status, kind = results[url]
        if status not in {200, 206} or kind != "video/mp4":
            failures.append(f"video status={status} type={kind or '<missing>'} url={url}")
    passed = not failures and len(visuals) == expected_visuals and len(videos) == expected_videos
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
