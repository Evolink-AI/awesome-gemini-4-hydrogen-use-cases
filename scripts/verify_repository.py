#!/usr/bin/env python3
"""Verify the public Gemini 3.6 Flash guide repository contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ["en", "es", "pt", "ja", "ko", "de", "fr", "tr", "zh-TW", "zh-CN", "ru"]
READMES = ["README.md", *[f"README_{locale}.md" for locale in LOCALES[1:]]]
R2_PREFIX = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/"
MODEL_PAGE = "https://evolink.ai/gemini-3-6-flash"
API_DOCS = "https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart"


def main() -> int:
    errors: list[str] = []
    required = [
        *READMES, "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
        ".github/PULL_REQUEST_TEMPLATE.md", ".github/ISSUE_TEMPLATE/case.yml",
        ".github/ISSUE_TEMPLATE/correction.yml", ".github/workflows/validate.yml",
        "docs/maintenance.md", "docs/update-log.md", "data/use-cases.json",
        "data/ingested_tweets.json", "data/source-fidelity-manifest.json",
        "data/localization-cache.json", "data/usecase-update-config.json",
    ]
    required.extend(f"data/localizations/{locale}.json" for locale in LOCALES[1:])
    errors.extend(f"missing required file: {path}" for path in required if not (ROOT / path).is_file())
    if errors:
        return fail(errors)

    curated = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    items = curated.get("items", [])
    expected_count = len(items)
    expected_numbers = list(range(1, expected_count + 1))
    numbers = [item.get("public_number") for item in items]
    if expected_count != 33:
        errors.append(f"expected 33 reviewed cases, found {expected_count}")
    if numbers != expected_numbers:
        errors.append("public case numbers are not contiguous")
    if len({item.get("source_url") for item in items}) != expected_count:
        errors.append("source URLs are not unique")
    if any(item.get("quality_tier") != "high" or item.get("decision") != "high_confidence_update" for item in items):
        errors.append("curated data includes a non-high-confidence case")
    if sum(bool(item.get("prompt_public")) for item in items) != 3:
        errors.append("public prompt count is not exactly 3")
    if any(not item.get("media_assets") or not item.get("media_source_urls") for item in items):
        errors.append("one or more cases lacks source-media lineage")

    visual_urls = [
        asset["poster_url"] if asset["kind"] == "video" else asset["url"]
        for item in items for asset in item.get("media_assets", [])
    ]
    playable_urls = [
        asset["url"] for item in items for asset in item.get("media_assets", []) if asset["kind"] == "video"
    ]
    if len(visual_urls) != 42:
        errors.append(f"expected 42 public visuals, found {len(visual_urls)}")
    if len(playable_urls) != 24:
        errors.append(f"expected 24 playable videos, found {len(playable_urls)}")
    if any(not url.startswith(R2_PREFIX) for url in [*visual_urls, *playable_urls]):
        errors.append("one or more public media URLs are outside the isolated R2 namespace")

    fidelity = json.loads((ROOT / "data/source-fidelity-manifest.json").read_text(encoding="utf-8"))
    if fidelity.get("selected_case_count") != expected_count:
        errors.append("source-fidelity selected-case denominator differs")
    if fidelity.get("expected_public_visual_count") != len(visual_urls):
        errors.append("source-fidelity visual denominator differs")
    if len(fidelity.get("cases", [])) != expected_count:
        errors.append("source-fidelity case inventory differs")

    ingested = json.loads((ROOT / "data/ingested_tweets.json").read_text(encoding="utf-8"))
    if ingested.get("ids") != [str(item["id"]) for item in items]:
        errors.append("ingested tweet IDs differ from the canonical case order")

    english_titles: list[str] = []
    canonical_handles = list(dict.fromkeys(item["author_handle"] for item in items))
    creator_line = ", ".join(f'[{handle}](https://x.com/{handle[1:]})' for handle in canonical_handles)
    for index, filename in enumerate(READMES):
        text = (ROOT / filename).read_text(encoding="utf-8")
        for marker in ("TODO", "TBD", "lorem ipsum", "<placeholder>"):
            if marker in text:
                errors.append(f"{filename}: unresolved marker {marker}")
        anchors = [int(value) for value in re.findall(r'^<a id="case-(\d+)"></a>$', text, re.MULTILINE)]
        if anchors != expected_numbers:
            errors.append(f"{filename}: case anchors differ from 1..{expected_count}")
        titles = re.findall(r'^### .+? \d+: \[([^\]]+)\]\(https://x\.com/[^)]+\)', text, re.MULTILINE)
        if len(titles) != expected_count:
            errors.append(f"{filename}: rendered case heading count is {len(titles)}")
        if text.count("](#case-") != expected_count:
            errors.append(f"{filename}: centralized menu case count differs")
        if text.count(f'src="{R2_PREFIX}media/source-cases/') != len(visual_urls):
            errors.append(f"{filename}: rendered source visual count differs")
        if text.count(f']({R2_PREFIX}media/source-cases/') != len(playable_urls):
            errors.append(f"{filename}: playable source video count differs")
        if text.count("```text") != 3:
            errors.append(f"{filename}: public prompt block count differs")
        for item in items:
            if text.count(item["source_url"]) != 1:
                errors.append(f'{filename}: case {item["public_number"]} source URL is missing or duplicated')
            for asset in item["media_assets"]:
                visual = asset["poster_url"] if asset["kind"] == "video" else asset["url"]
                if text.count(f'src="{visual}"') != 1:
                    errors.append(f'{filename}: case {item["public_number"]} visual is missing or duplicated')
        if MODEL_PAGE not in text or API_DOCS not in text or "https://evolink.ai/dashboard/keys" not in text:
            errors.append(f"{filename}: model, key, or API conversion route is missing")
        headings = re.findall(r"^## .+$", text, re.MULTILINE)
        if len(headings) < 2 or "⚡" not in headings[-2] or "🙏" not in headings[-1]:
            errors.append(f"{filename}: Quick Start and Acknowledge are not the final two sections")
        if creator_line not in text.split('<a id="acknowledge"></a>', 1)[-1]:
            errors.append(f"{filename}: canonical inline creator list differs")
        if re.search(r'<(?:img|video)[^>]+src="[^"]+\.mp4', text):
            errors.append(f"{filename}: MP4 is directly embedded instead of poster-linked")
        if index == 0:
            english_titles = titles
        else:
            changed = sum(a != b for a, b in zip(titles, english_titles, strict=False))
            if changed < 20:
                errors.append(f"{filename}: only {changed} of {expected_count} titles are localized")

    for filename in ("README_zh-CN.md", "README_zh-TW.md"):
        if "。" in (ROOT / filename).read_text(encoding="utf-8"):
            errors.append(f"{filename}: Chinese full stop violates the vault writing rule")

    if errors:
        return fail(errors)
    print("PASS")
    print(f"readmes={len(READMES)}")
    print(f"cases={expected_count}")
    print(f"localized_case_instances={expected_count * len(READMES)}")
    print(f"visuals_per_readme={len(visual_urls)}")
    print(f"playable_videos_per_readme={len(playable_urls)}")
    return 0


def fail(errors: list[str]) -> int:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
