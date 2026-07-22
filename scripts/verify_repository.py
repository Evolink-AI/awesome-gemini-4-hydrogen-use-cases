#!/usr/bin/env python3
"""Verify the public Gemini 3.6 Flash guide repository contract."""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ["en", "es", "pt", "ja", "ko", "de", "fr", "tr", "zh-TW", "zh-CN", "ru"]
READMES = ["README.md", *[f"README_{locale}.md" for locale in LOCALES[1:]]]
R2_PREFIX = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/"
MODEL_PAGE = "https://evolink.ai/gemini-3-6-flash"
API_KEYS = "https://evolink.ai/dashboard/keys"
API_DOCS_PATH = "api-manual/language-series/gemini/native-api/native-api-quickstart"
DOC_LOCALE_BY_README = {
    "en": "en", "es": "es", "pt": "en", "ja": "ja", "ko": "ko", "de": "de",
    "fr": "fr", "tr": "en", "zh-TW": "en", "zh-CN": "cn", "ru": "en",
}
FALLBACK_MARKERS = {"pt": "inglês", "tr": "İngilizce", "zh-TW": "英文", "ru": "английском"}
GOOGLE_RELEASE = "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/"
MODEL_CARD = "https://deepmind.google/models/model-cards/gemini-3-6-flash/"
RELATED_REPOSITORY = "https://github.com/Evolink-AI/gemini-omni-flash-api-skill"
CAMPAIGN = "awesome-gemini-3-6-flash-guide-and-use-cases"
URL_RE = re.compile(r'https://[^\s)>"`]+')


def api_docs_for(locale: str) -> str:
    return f"https://evolink.ai/docs/{DOC_LOCALE_BY_README[locale]}/{API_DOCS_PATH}"


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
    if fidelity.get("owner_presentation", {}).get("localization_fallback") != "english":
        errors.append("source-fidelity localization fallback is not english")

    update_config = json.loads((ROOT / "data/usecase-update-config.json").read_text(encoding="utf-8"))
    if update_config.get("localization_fallback") != "english":
        errors.append("recurring update localization fallback is not english")

    ingested = json.loads((ROOT / "data/ingested_tweets.json").read_text(encoding="utf-8"))
    if ingested.get("ids") != [str(item["id"]) for item in items]:
        errors.append("ingested tweet IDs differ from the canonical case order")

    localization_cache = json.loads((ROOT / "data/localization-cache.json").read_text(encoding="utf-8"))
    for locale in LOCALES[1:]:
        localized = json.loads((ROOT / f"data/localizations/{locale}.json").read_text(encoding="utf-8"))
        if localization_cache.get(locale) != localized:
            errors.append(f"data/localizations/{locale}.json: differs from localization cache")
        quick_labels = [localized.get("strings", {}).get(key, "") for key in ("quick_model", "quick_key", "quick_docs")]
        if any(label.endswith((".", "。", "!", "！", "?", "？", ";", "；")) for label in quick_labels):
            errors.append(f"data/localizations/{locale}.json: Quick Start link label ends with punctuation")
        if locale in FALLBACK_MARKERS:
            marker = FALLBACK_MARKERS[locale]
            if marker not in localized["strings"]["open_docs"] or marker not in localized["strings"]["quick_docs"]:
                errors.append(f"data/localizations/{locale}.json: English documentation fallback is not disclosed")
        if locale in {"zh-CN", "zh-TW"} and re.search(r"[\u3400-\u9fff]Gemini|Flash[\u3400-\u9fff]", localized["strings"]["quick_model"]):
            errors.append(f"data/localizations/{locale}.json: model link label lacks CJK/Latin spacing")
        if sorted(int(key) for key in localized.get("cases", {})) != expected_numbers:
            errors.append(f"data/localizations/{locale}.json: case keys differ from 1..{expected_count}")
            continue
        for item in items:
            case = localized["cases"][str(item["public_number"])]
            if not all(str(case.get(field, "")).strip() for field in ("title", "takeaway", "notes")):
                errors.append(f'{locale} case {item["public_number"]}: empty localized field')
            if case["title"].strip() == item["title"].strip():
                errors.append(f'{locale} case {item["public_number"]}: title is unchanged from English')
            if case["takeaway"].strip() == item["takeaway"].strip():
                errors.append(f'{locale} case {item["public_number"]}: takeaway is unchanged from English')

    english_titles: list[str] = []
    canonical_handles = list(dict.fromkeys(item["author_handle"] for item in items))
    creator_line = ", ".join(f'[{handle}](https://x.com/{handle[1:]})' for handle in canonical_handles)
    for index, filename in enumerate(READMES):
        locale = LOCALES[index]
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
        expected_docs = api_docs_for(locale)
        if MODEL_PAGE not in text or expected_docs not in text or API_KEYS not in text:
            errors.append(f"{filename}: model, key, or API conversion route is missing")
        docs_routes = re.findall(rf"https://evolink\.ai/docs/([^/]+)/{re.escape(API_DOCS_PATH)}", text)
        if docs_routes != [DOC_LOCALE_BY_README[locale]] * 3:
            errors.append(f"{filename}: documentation routes do not match locale mapping")
        if locale in FALLBACK_MARKERS and "Gemini Native API (English)" not in text:
            errors.append(f"{filename}: English documentation fallback badge is not disclosed")
        if locale not in FALLBACK_MARKERS and "Gemini Native API (English)" in text:
            errors.append(f"{filename}: localized documentation is incorrectly marked as English fallback")

        conversion_pairs: dict[str, list[tuple[str, str]]] = {MODEL_PAGE: [], API_KEYS: [], expected_docs: []}
        conversion_urls = [url.rstrip(".,;") for url in URL_RE.findall(text) if any(url.startswith(base) for base in conversion_pairs)]
        exact_duplicates = [url for url, count in Counter(conversion_urls).items() if count > 1]
        if exact_duplicates:
            errors.append(f"{filename}: duplicate EvoLink conversion URL reuses one placement UTM")
        for url in conversion_urls:
            parsed = urllib.parse.urlparse(url)
            base = urllib.parse.urlunparse(parsed._replace(query="", fragment=""))
            query = urllib.parse.parse_qs(parsed.query)
            if base in conversion_pairs:
                if query.get("utm_source") != ["github"] or query.get("utm_campaign") != [CAMPAIGN]:
                    errors.append(f"{filename}: conversion URL has incorrect source or campaign")
                conversion_pairs[base].append((query.get("utm_medium", [""])[0], query.get("utm_content", [""])[0]))
        expected_pairs = {
            MODEL_PAGE: [("banner", "readme_banner"), ("badge", "top_badge"), ("overview", "model_link"), ("quickstart", "model_link")],
            API_KEYS: [("overview", "api_key"), ("quickstart", "api_key")],
            expected_docs: [("badge", "docs_link"), ("overview", "docs_link"), ("docs", "first_run")],
        }
        if any(sorted(conversion_pairs[base]) != sorted(pairs) for base, pairs in expected_pairs.items()):
            errors.append(f"{filename}: conversion placement UTM matrix differs")

        overview_text = text.split(f'## 📊', 1)[-1].split(f'## 📑', 1)[0]
        related_text = text.split('<a id="related-repositories"></a>', 1)[-1].split('<a id="quick-start"></a>', 1)[0]
        if GOOGLE_RELEASE not in overview_text or MODEL_CARD not in overview_text:
            errors.append(f"{filename}: official sources are not placed in Overview")
        if GOOGLE_RELEASE in related_text or MODEL_CARD in related_text:
            errors.append(f"{filename}: official sources are incorrectly placed in Related Repositories")
        if RELATED_REPOSITORY not in related_text or "https://github.com/Evolink-AI)" in related_text:
            errors.append(f"{filename}: Related Repositories does not link the verified adjacent repository")
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
            if changed != expected_count:
                errors.append(f"{filename}: only {changed} of {expected_count} titles are localized")

    for filename in ("README_zh-CN.md", "README_zh-TW.md"):
        if "。" in (ROOT / filename).read_text(encoding="utf-8"):
            errors.append(f"{filename}: Chinese full stop violates the vault writing rule")

    security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
    if "[support@evolink.ai](mailto:support@evolink.ai)" not in security:
        errors.append("SECURITY.md: direct security contact is missing")
    if "](https://evolink.ai)" in security:
        errors.append("SECURITY.md: generic homepage is used as a security contact")

    if errors:
        return fail(errors)
    print("PASS")
    print(f"readmes={len(READMES)}")
    print(f"cases={expected_count}")
    print(f"localized_case_instances={expected_count * len(READMES)}")
    print(f"visuals_per_readme={len(visual_urls)}")
    print(f"playable_videos_per_readme={len(playable_urls)}")
    print("docs_locales=en,es,ja,ko,de,fr,cn")
    print("docs_fallbacks=pt,tr,zh-TW,ru->en")
    return 0


def fail(errors: list[str]) -> int:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
