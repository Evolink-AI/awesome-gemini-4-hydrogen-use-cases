#!/usr/bin/env python3
"""Check unique public URLs referenced by every README."""

from __future__ import annotations

import argparse
import re
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r'https://[^\s)>"]+')
R2 = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/"


def check(url: str) -> tuple[str, int | str]:
    check_url = url
    is_status = bool(re.match(r"https://x\.com/[^/]+/status/\d+$", url))
    if is_status:
        check_url = "https://publish.twitter.com/oembed?omit_script=1&url=" + urllib.parse.quote(url, safe="")
    command = [
        "curl", "-L", "-sS", "--retry", "3", "--retry-all-errors", "--connect-timeout", "10",
        "--max-time", "35", "--user-agent", "Mozilla/5.0 awesome-gemini-3.6-flash-guide-link-audit/1.0",
    ]
    if url.startswith(R2):
        command.extend(["--range", "0-0"])
    command.extend(["--output", "/dev/null", "--write-out", "%{http_code}", check_url])
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    status = result.stdout[-3:]
    return (url, int(status)) if result.returncode == 0 and status.isdigit() else (url, result.stderr.strip() or f"curl-exit-{result.returncode}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    urls: set[str] = set()
    for path in [ROOT / "README.md", *sorted(ROOT.glob("README_*.md"))]:
        urls.update(URL_RE.findall(path.read_text(encoding="utf-8")))
    urls = {url.rstrip(".,`") for url in urls if "img.shields.io" not in url}
    with ThreadPoolExecutor(max_workers=10) as pool:
        results = sorted(pool.map(check, urls))
    rows = []
    failures = []
    for url, status in results:
        accepted_x_profile = url.startswith("https://x.com/") and "/status/" not in url and status in {401, 403}
        ok = isinstance(status, int) and (200 <= status < 400 or accepted_x_profile)
        rows.append(f"{'PASS' if ok else 'FAIL'} {status} {url}")
        if not ok:
            failures.append((url, status))
    lines = [
        "# Public Link Audit v1", "", f"- Status: `{'passed' if not failures else 'failed'}`",
        f"- Checked unique URLs: {len(results)}", f"- Failures: {len(failures)}",
        f"- Command exit code: {0 if not failures else 1}", f"- Result: {'pass' if not failures else 'fail'}",
        "", "## Results", "", "```text", *rows, "```",
    ]
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("PASS" if not failures else "FAIL")
    print(f"checked={len(results)} failures={len(failures)}")
    for url, status in failures:
        print(f"FAIL {status} {url}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
