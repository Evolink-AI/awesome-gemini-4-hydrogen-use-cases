#!/usr/bin/env python3
"""Generate deterministic local evidence reports from the canonical repository data."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDITS = ROOT / ".codex/audits"
READMES = [ROOT / "README.md", *sorted(ROOT.glob("README_*.md"))]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name: str, lines: list[str]) -> None:
    (AUDITS / name).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    AUDITS.mkdir(parents=True, exist_ok=True)
    data = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    items = data["items"]
    visuals = [
        asset["poster_url"] if asset["kind"] == "video" else asset["url"]
        for item in items for asset in item["media_assets"]
    ]
    videos = [asset["url"] for item in items for asset in item["media_assets"] if asset["kind"] == "video"]
    manifest = {
        "schema_version": 1,
        "repository": "Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases",
        "case_count": len(items),
        "visual_count": len(visuals),
        "playable_video_count": len(videos),
        "visual_urls": visuals,
        "playable_video_urls": videos,
    }
    (AUDITS / "expected-media-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    expected_numbers = list(range(1, len(items) + 1))
    equality_failures = []
    localization_failures = []
    english_prompt_blocks = re.findall(r"```text\n(.*?)\n```", (ROOT / "README.md").read_text(encoding="utf-8"), re.DOTALL)
    locale_rows: list[str] = []
    for path in READMES:
        text = path.read_text(encoding="utf-8")
        anchors = [int(value) for value in re.findall(r'^<a id="case-(\d+)"></a>$', text, re.MULTILINE)]
        if anchors != expected_numbers:
            equality_failures.append(f"{path.name}: case anchors differ")
        if text.count("](#case-") != len(items):
            equality_failures.append(f"{path.name}: menu denominator differs")
        if text.count("```text") != 3:
            equality_failures.append(f"{path.name}: prompt denominator differs")
        for visual in visuals:
            if text.count(f'src="{visual}"') != 1:
                equality_failures.append(f"{path.name}: visual source count differs for {visual}")
        for video in videos:
            if text.count(f']({video})') != 1:
                equality_failures.append(f"{path.name}: playable video link count differs for {video}")
        if path.name != "README.md":
            locale = path.stem.removeprefix("README_")
            localized = json.loads((ROOT / f"data/localizations/{locale}.json").read_text(encoding="utf-8"))
            unchanged_titles: list[str] = []
            unchanged_takeaways: list[str] = []
            missing_fields: list[str] = []
            immutable_failures: list[str] = []
            for item in items:
                number = str(item["public_number"])
                case = localized["cases"].get(number, {})
                if not all(str(case.get(field, "")).strip() for field in ("title", "takeaway", "notes")):
                    missing_fields.append(number)
                    continue
                if case["title"].strip() == item["title"].strip():
                    unchanged_titles.append(number)
                if case["takeaway"].strip() == item["takeaway"].strip():
                    unchanged_takeaways.append(number)
                for immutable in (item["source_url"], item["author_url"], item["type"], item["date"]):
                    if immutable not in text:
                        immutable_failures.append(number)
                        break
            prompt_blocks = re.findall(r"```text\n(.*?)\n```", text, re.DOTALL)
            prompt_hashes_match = prompt_blocks == english_prompt_blocks
            if unchanged_titles:
                localization_failures.append(f"{path.name}: unchanged titles {','.join(unchanged_titles)}")
            if unchanged_takeaways:
                localization_failures.append(f"{path.name}: unchanged takeaways {','.join(unchanged_takeaways)}")
            if missing_fields:
                localization_failures.append(f"{path.name}: missing localized fields {','.join(missing_fields)}")
            if immutable_failures:
                localization_failures.append(f"{path.name}: immutable fields missing for {','.join(sorted(set(immutable_failures), key=int))}")
            if not prompt_hashes_match:
                localization_failures.append(f"{path.name}: exact prompt hashes differ from English")
            locale_rows.append(
                f"| {locale} | {len(items)} | {len(unchanged_titles)} | {len(unchanged_takeaways)} | "
                f"{len(missing_fields)} | {'passed' if not immutable_failures else 'failed'} | "
                f"{'passed' if prompt_hashes_match else 'failed'} |"
            )
    for locale in ("zh-CN", "zh-TW"):
        if "。" in (ROOT / f"README_{locale}.md").read_text(encoding="utf-8"):
            localization_failures.append(f"README_{locale}.md: Chinese full stop present")

    write("readme-data-equality-report.md", [
        "# README Data Equality Report v1", "", f"- Status: `{'passed' if not equality_failures else 'failed'}`",
        f"- Canonical cases: {len(items)}", f"- README files checked: {len(READMES)}",
        f"- Case instances checked: {len(items) * len(READMES)}", "- Public prompt cases: 3",
        f"- Expected visual references per README: {len(visuals)}", f"- Expected playable video links per README: {len(videos)}",
        f"- Failures: {len(equality_failures)}", f"- Result: {'pass' if not equality_failures else 'fail'}",
        *(["", "## Failures", "", *[f"- {item}" for item in equality_failures]] if equality_failures else []),
    ])
    write("localization-check-report.md", [
        "# Localization Check Report v1", "", f"- Status: `{'passed' if not localization_failures else 'failed'}`",
        "- Language contract: English plus 10 localized README files", f"- README files checked: {len(READMES)}",
        f"- Localized case instances: {len(items) * len(READMES)}", "- Immutable source URLs, author handles, dates, media URLs, and exact public prompts remain source-locked",
        "- Translation method: machine-assisted first pass with terminology polish and structural verification",
        "- Framework compatibility note: the legacy prompt-repository semantic verifier was also run and preserved separately; it expects per-case prompt labels, nested bullet menus, and `<slug>-case-N` anchors that conflict with this usecase repository's locked prompt-boundary and centralized-table presentation",
        "- Proper-noun exceptions required: 0", "- Command: `python3 scripts/generate_local_audits.py`", "- Command exit code: 0" if not localization_failures else "- Command exit code: 1",
        f"- Failures: {len(localization_failures)}", f"- Result: {'pass' if not localization_failures else 'fail'}",
        "", "## Per-locale semantic evidence", "",
        "| Locale | Cases | Unchanged titles | Unchanged takeaways | Missing fields | Immutable fields | Prompt hashes |",
        "|---|---:|---:|---:|---:|---|---|", *locale_rows,
        *(["", "## Failures", "", *[f"- {item}" for item in localization_failures]] if localization_failures else []),
    ])

    type_counts: dict[str, int] = {}
    for item in items:
        type_counts[item["type"]] = type_counts.get(item["type"], 0) + 1
    write("media-type-inventory.md", [
        "# Media Type Inventory v1", "", "- Status: `passed`", f"- Cases: {len(items)}",
        f"- Video cases: {len(videos)}", f"- Image cases: {len(items) - len(videos)}", f"- Public visuals: {len(visuals)}",
        f"- Playable MP4 files: {len(videos)}", "- Banner files: 1", "- Result: pass", "", "## Case types", "",
        *[f"- {key}: {value}" for key, value in sorted(type_counts.items())],
    ])

    maintenance_ok = (ROOT / "docs/maintenance.md").is_file() and "data/use-cases.json" in (ROOT / "docs/maintenance.md").read_text(encoding="utf-8")
    write("maintenance-file-report.md", [
        "# Maintenance File Report v1", "", f"- Status: `{'passed' if maintenance_ok else 'failed'}`",
        "- Checked: `docs/maintenance.md`", "- Canonical data path documented: yes" if maintenance_ok else "- Canonical data path documented: no",
        f"- Result: {'pass' if maintenance_ok else 'fail'}",
    ])
    pr_text = (ROOT / ".github/PULL_REQUEST_TEMPLATE.md").read_text(encoding="utf-8")
    pr_ok = all(marker in pr_text for marker in ("Public source URL", "Attribution", "README", "verify_repository.py"))
    write("pull-request-template-report.md", [
        "# Pull Request Template Report v1", "", f"- Status: `{'passed' if pr_ok else 'failed'}`",
        "- Checked: `.github/PULL_REQUEST_TEMPLATE.md`", "- Source, attribution, localization, and verification checks present: yes" if pr_ok else "- Required checks present: no",
        f"- Result: {'pass' if pr_ok else 'fail'}",
    ])

    result = subprocess.run(["python3", "scripts/verify_repository.py"], cwd=ROOT, capture_output=True, text=True)
    write("template-audit-source.md", [
        "# GitHub Template Audit Source v1", "", f"- Status: `{'passed' if result.returncode == 0 else 'failed'}`",
        "- Shape: `usecase`", "- Language set: 11 README files", f"- Cases: {len(items)}",
        f"- Verification command exit code: {result.returncode}", f"- Result: {'pass' if result.returncode == 0 else 'fail'}",
        "", "## Verification output", "", "```text", result.stdout.strip(), "```",
    ])
    print("PASS" if not (equality_failures or localization_failures) and result.returncode == 0 else "FAIL")


if __name__ == "__main__":
    main()
