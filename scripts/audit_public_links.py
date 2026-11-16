#!/usr/bin/env python3
"""Audit external, relative, fragment, badge, media, and UTM links on public surfaces."""

from __future__ import annotations

import argparse
import re
import subprocess
import urllib.parse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
R2 = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/"
CAMPAIGN = "awesome-gemini-4-hydrogen-guide-and-use-cases"
URL_RE = re.compile(r'https://[^\s)>"`]+')
MARKDOWN_LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\(([^)]+)\)')
MARKDOWN_DESTINATION_RE = re.compile(r'\]\(([^)]+)\)')
HTML_LINK_RE = re.compile(r'<(?:a|img)\b[^>]*(?:href|src)="([^"]+)"', re.IGNORECASE)
EXPLICIT_ANCHOR_RE = re.compile(r'<a\s+id="([^"]+)"', re.IGNORECASE)
HEADING_RE = re.compile(r'^#{1,6}\s+(.+?)\s*$', re.MULTILINE)
CONVERSION_PREFIXES = (
    "https://evolink.ai/gemini-4-hydrogen",
    "https://evolink.ai/dashboard/keys",
    "https://evolink.ai/docs/",
)
METHOD_BOUND_ENDPOINTS = {
    "https://direct.evolink.ai/v1beta/models/gemini-4-hydrogen:generateContent",
}


def public_files() -> list[Path]:
    paths = [*ROOT.glob("*.md"), *ROOT.glob("README_*.md"), *ROOT.glob("docs/**/*.md"), *ROOT.glob(".github/**/*.md")]
    license_path = ROOT / "LICENSE"
    if license_path.is_file():
        paths.append(license_path)
    return sorted(set(path for path in paths if ".codex" not in path.parts))


def github_slug(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
    heading = re.sub(r"[^\w\-\s]", "", heading, flags=re.UNICODE)
    return re.sub(r"\s+", "-", heading)


def anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(EXPLICIT_ANCHOR_RE.findall(text)) | {github_slug(value) for value in HEADING_RE.findall(text)}


def current_head() -> str:
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else "unavailable"


def check_external(url: str) -> tuple[str, int | str, str, bool]:
    checked_url = url
    is_status = bool(re.match(r"https://x\.com/[^/]+/status/\d+$", url))
    if is_status:
        checked_url = "https://publish.twitter.com/oembed?omit_script=1&url=" + urllib.parse.quote(url, safe="")
    command = [
        "curl", "-L", "-sS", "--connect-timeout", "10",
        "--max-time", "35", "--user-agent", "Mozilla/5.0 awesome-gemini-4-hydrogen-guide-link-audit/2.0",
    ]
    if url.startswith(R2):
        command.extend(["--range", "0-0"])
    command.extend(["--output", "/dev/null", "--write-out", "%{http_code}\t%{url_effective}", checked_url])
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    parts = result.stdout.strip().split("\t", 1)
    if result.returncode != 0 or not parts or not parts[0].isdigit():
        return url, result.stderr.strip() or f"curl-exit-{result.returncode}", "", is_status
    return url, int(parts[0]), parts[1] if len(parts) > 1 else checked_url, is_status


def expected_method_endpoint_reuse(relative_path: str, url: str, count: int, text: str) -> bool:
    """Only the required POST reference plus its runnable request may duplicate."""
    if Path(relative_path).parent != Path(".") or not Path(relative_path).name.startswith("README") or url not in METHOD_BOUND_ENDPOINTS or count != 2:
        return False
    blocks = re.findall(r"```bash\n(.*?)```", text, re.DOTALL)
    runnable = [block for block in blocks if f'--url "{url}"' in block and "--request POST" in block]
    outside = re.sub(r"```bash\n.*?```", "", text, flags=re.DOTALL)
    return len(runnable) == 1 and outside.count(f"POST {url}") == 1


def host_is_skipped(url: str, skipped_hosts: list[str]) -> bool:
    host = (urllib.parse.urlparse(url).hostname or "").lower().rstrip(".")
    return any(host == denied.lower().rstrip(".") or host.endswith("." + denied.lower().rstrip(".")) for denied in skipped_hosts)


def external_status_verified(status: int | str) -> bool:
    return isinstance(status, int) and 200 <= status < 400


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--skip-host", action="append", default=[], metavar="HOST", help="Do not request a denied host; report its URLs BLOCKED and fail the audit. Repeatable.")
    args = parser.parse_args()
    paths = public_files()
    external_urls: set[str] = set()
    relative_failures: list[str] = []
    fragment_failures: list[str] = []
    utm_failures: list[str] = []
    copy_failures: list[str] = []
    total_references = 0
    relative_checked = 0
    fragment_checked = 0
    utm_checked = 0
    utm_exemptions = 0
    method_bound_exemptions: set[str] = set()
    external_occurrences: dict[str, list[str]] = defaultdict(list)
    within_file_occurrences: Counter[tuple[str, str]] = Counter()

    for path in paths:
        text = path.read_text(encoding="utf-8")
        local_anchors = anchors(path)
        markdown_matches = list(MARKDOWN_LINK_RE.finditer(text))
        markdown_targets = MARKDOWN_DESTINATION_RE.findall(text)
        html_targets = HTML_LINK_RE.findall(text)
        raw_url_matches = list(URL_RE.finditer(text))
        raw_urls = [match.group(0) for match in raw_url_matches]
        total_references += len(markdown_targets) + len(html_targets) + len(raw_urls)
        targets = [target.strip() for target in markdown_targets] + html_targets
        for match in raw_url_matches:
            url = match.group(0).rstrip(".,;")
            location = f"{path.relative_to(ROOT)}:{text.count(chr(10), 0, match.start()) + 1}"
            external_occurrences[url].append(location)
            within_file_occurrences[(str(path.relative_to(ROOT)), url)] += 1
            if url in METHOD_BOUND_ENDPOINTS:
                method_bound_exemptions.add(url)
            else:
                external_urls.add(url)
        for match in markdown_matches:
            label = match.group(2).strip().lower()
            if not match.group(1) and label in {"here", "click here", "link"}:
                copy_failures.append(f"{path.relative_to(ROOT)}: ambiguous link label {label!r}")
        for target in targets:
            if target.startswith(("http://", "https://")):
                external_urls.add(target.rstrip(".,;"))
                continue
            if target.startswith(("mailto:", "tel:")):
                continue
            if target.startswith("#"):
                fragment_checked += 1
                if target[1:] not in local_anchors:
                    fragment_failures.append(f"{path.relative_to(ROOT)}: unresolved {target}")
                continue
            relative_checked += 1
            file_target, _, fragment = target.partition("#")
            resolved = (path.parent / urllib.parse.unquote(file_target)).resolve()
            if not resolved.is_file():
                relative_failures.append(f"{path.relative_to(ROOT)}: missing {target}")
                continue
            if fragment:
                fragment_checked += 1
                if fragment not in anchors(resolved):
                    fragment_failures.append(f"{path.relative_to(ROOT)}: unresolved {target}")

        if path.name.startswith("README"):
            for url in {url.rstrip(".,;") for url in raw_urls if urllib.parse.urlparse(url).hostname in {"evolink.ai", "www.evolink.ai"}}:
                utm_checked += 1
                query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
                if query.get("utm_source") != ["github"] or query.get("utm_campaign") != [CAMPAIGN] or not query.get("utm_medium") or not query.get("utm_content"):
                    utm_failures.append(f"{path.relative_to(ROOT)}: incomplete UTM {url}")
        elif "https://evolink.ai" in text:
            utm_exemptions += 1

    accepted_duplicate_groups: list[str] = []
    duplicate_failures: list[str] = []
    for (relative_path, url), count in sorted(within_file_occurrences.items()):
        if count < 2:
            continue
        parsed = urllib.parse.urlparse(url)
        expected_creator_reuse = parsed.hostname == "x.com" and "/status/" not in parsed.path
        expected_video_reuse = url.startswith(R2) and parsed.path.endswith(".mp4")
        expected_image_reuse = url.startswith(R2) and re.search(r"/hydrogen-202611(?:13|17)/media/", parsed.path) and parsed.path.endswith((".jpg", ".jpeg", ".png", ".webp"))
        expected_endpoint_reuse = expected_method_endpoint_reuse(relative_path, url, count, (ROOT / relative_path).read_text(encoding="utf-8"))
        if expected_creator_reuse or expected_video_reuse or expected_image_reuse or expected_endpoint_reuse:
            if expected_creator_reuse:
                reason = "case attribution + Acknowledge"
            elif expected_video_reuse:
                reason = "clickable poster + text playback"
            elif expected_image_reuse:
                reason = "clickable image + rendered image"
            else:
                reason = "POST method reference + runnable request"
            accepted_duplicate_groups.append(f"{relative_path}: {count}× {url} ({reason})")
        else:
            duplicate_failures.append(f"{relative_path}: unclassified exact duplicate {count}× {url}")

    blocked_urls = {url for url in external_urls if host_is_skipped(url, args.skip_host)}
    with ThreadPoolExecutor(max_workers=10) as pool:
        results = sorted(pool.map(check_external, external_urls - blocked_urls))
    results.extend((url, "BLOCKED", "", False) for url in sorted(blocked_urls))

    p0: list[str] = []
    p1: list[str] = [*relative_failures, *fragment_failures, *utm_failures, *copy_failures, *duplicate_failures]
    p2: list[str] = []
    redirects: list[str] = []
    rows: list[str] = []
    checked_count = 0
    for url, status, final_url, used_oembed in results:
        ok = external_status_verified(status)
        if status != "BLOCKED":
            checked_count += 1
        if ok and final_url and not used_oembed and final_url.rstrip("/") != url.rstrip("/"):
            redirects.append(f"{url} -> {final_url}")
        if not ok:
            failure = f"status={status} url={url}" + (" (unverified; access denied or deliberately skipped)" if status in {401, 403, "BLOCKED"} else "")
            if url.startswith(CONVERSION_PREFIXES):
                p0.append(failure)
            else:
                p1.append(failure)
        rows.append(f"{'PASS' if ok else 'BLOCKED' if status in {401, 403, 'BLOCKED'} else 'FAIL'} {status} {url}" + (f" -> {final_url}" if final_url and not used_oembed and final_url != url else ""))

    blocked_count = sum(status in {401, 403, "BLOCKED"} for _, status, _, _ in results)
    passed = not p0 and not p1
    cross_file_duplicate_urls = sum(1 for locations in external_occurrences.values() if len({value.rsplit(":", 1)[0] for value in locations}) > 1)
    lines = [
        "# Public Surface Link Audit v2", "", f"- Status: `{'passed' if passed else 'blocked' if blocked_count else 'failed'}`",
        f"- Target commit: `{current_head()}`",
        f"- Checked at: `{datetime.now(timezone.utc).isoformat()}`",
        "- Method: Markdown link/image, HTML href/src, raw URL, relative file, explicit/heading fragment, exact-duplicate classification, external curl readback, and README EvoLink UTM extraction",
        f"- Public files in scope: {len(paths)}", "- Excluded paths: `.codex/**` run-local evidence, `data/**/*.json` structured data, and generated/downloaded media not exposed as Markdown surfaces",
        f"- Total extracted references: {total_references}", f"- Unique external URLs: {len(external_urls)}",
        f"- External URLs checked: {checked_count}", f"- Relative file links checked: {relative_checked}",
        f"- Fragment links checked: {fragment_checked}", f"- README EvoLink URLs checked for UTM: {utm_checked}",
        f"- Recorded non-README UTM exemptions: {utm_exemptions}", f"- Blocked URLs not requested: {len(blocked_urls)}",
        f"- Method-bound API endpoint exemptions: {len(method_bound_exemptions)}",
        f"- Redirects: {len(redirects)}", f"- Relative file failures: {len(relative_failures)}",
        f"- Fragment failures: {len(fragment_failures)}", f"- UTM failures: {len(utm_failures)}",
        f"- Link-copy failures: {len(copy_failures)}", f"- Cross-file duplicate URLs (expected localization reuse): {cross_file_duplicate_urls}",
        f"- Accepted within-file duplicate groups: {len(accepted_duplicate_groups)}", f"- Unclassified within-file duplicate failures: {len(duplicate_failures)}",
        f"- P0 failures: {len(p0)}", f"- P1 failures: {len(p1)}",
        f"- P2 warnings: {len(p2)}", f"- Command exit code: {0 if passed else 1}", f"- Result: {'pass' if passed else 'fail'}",
        "", "## Scope", "", *[f"- `{path.relative_to(ROOT)}`" for path in paths],
        "", "## External results", "", "```text", *rows, "```",
    ]
    if redirects:
        lines.extend(["", "## Redirects", "", *[f"- {row}" for row in redirects]])
    if method_bound_exemptions:
        lines.extend(["", "## Method-bound API endpoints", "", *[f"- POST-only endpoint: {url}" for url in sorted(method_bound_exemptions)]])
    if accepted_duplicate_groups:
        lines.extend(["", "## Accepted exact duplicates", "", "These are intentional UI or attribution repetitions, not competing destinations", "", *[f"- {row}" for row in accepted_duplicate_groups]])
    if p0 or p1 or p2:
        lines.extend(["", "## Findings", ""])
        lines.extend(f"- P0: {row}" for row in p0)
        lines.extend(f"- P1: {row}" for row in p1)
        lines.extend(f"- P2: {row}" for row in p2)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("PASS" if passed else "FAIL")
    print(f"files={len(paths)} external={len(external_urls)} relative={relative_checked} fragments={fragment_checked} utm={utm_checked} p0={len(p0)} p1={len(p1)} p2={len(p2)}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
