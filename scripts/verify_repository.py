#!/usr/bin/env python3
"""Verify the public Gemini 4 Hydrogen guide repository contract."""

from __future__ import annotations

import hashlib
import json
import subprocess
import re
import sys
import urllib.parse
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ["en", "es", "pt", "ja", "ko", "de", "fr", "tr", "zh-TW", "zh-CN", "ru"]
READMES = ["README.md", *[f"README_{locale}.md" for locale in LOCALES[1:]]]
R2_PREFIX = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/"
MODEL_PAGE = "https://evolink.ai/gemini-4-hydrogen"
API_KEYS = "https://evolink.ai/dashboard/keys"
API_DOCS_PATH = "api-manual/language-series/gemini/native-api/native-api-quickstart"
DOC_LOCALE_BY_README = {
    "en": "en", "es": "es", "pt": "en", "ja": "ja", "ko": "ko", "de": "de",
    "fr": "fr", "tr": "en", "zh-TW": "en", "zh-CN": "cn", "ru": "en",
}
FALLBACK_MARKERS = {"pt": "inglês", "tr": "İngilizce", "zh-TW": "英文", "ru": "английском"}
GOOGLE_RELEASE = "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/"
MODEL_CARD = "https://deepmind.google/models/model-cards/gemini-4-hydrogen/"
RELATED_REPOSITORY = "https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases"
CAMPAIGN = "awesome-gemini-4-hydrogen-guide-and-use-cases"
URL_RE = re.compile(r'https://[^\s)>"`]+')


# Pinned before generation, from the independent source review package. Updating
# this lock requires a new source review, not regenerated output denominators.
INVENTORY_SHA256 = "d07f9769c546bd3c3017b0c8a799520d49df0909f830ad519bb0e90605261aef"


def validate_source_inventory(curated: dict, inventory: dict) -> list[str]:
    errors = []
    items, candidates = curated.get("items", []), inventory.get("cases", [])
    if len(items) != inventory.get("selected_count") or len(items) != len(candidates):
        errors.append("case count differs from independent source inventory")
    if curated.get("selected_case_count") != len(candidates):
        errors.append("canonical selected-case denominator differs")
    for item, source in zip(items, candidates):
        number = source["public_number"]
        fields = {"public_number": "public_number", "candidate_id": "candidate_id", "id": "source_post_id",
                  "source_url": "source_url", "author_handle": "author_handle",
                  "author_url": "author_url", "date": "date", "category_key": "category_key",
                  "prompt_public": "prompt_public", "prompt_text": "prompt_text"}
        for field, source_field in fields.items():
            if item.get(field) != source.get(source_field):
                errors.append(f"case {number}: {field} differs from independent source")
        expected = [(a["kind"], a["source_url"]) for a in source["source_media"]]
        actual = [(a.get("kind"), a.get("source_url")) for a in item.get("media_assets", [])]
        if actual != expected or item.get("media_source_urls") != [url for _, url in expected]:
            errors.append(f"case {number}: source-media expected set differs")
        for asset in item.get("media_assets", []):
            if not str(asset.get("url", "")).startswith(R2_PREFIX):
                errors.append(f"case {number}: media URL is outside isolated R2 namespace")
            if asset.get("kind") == "video" and (not str(asset.get("poster_url", "")).startswith(R2_PREFIX) or not urllib.parse.urlparse(asset.get("url", "")).path.endswith(".mp4")):
                errors.append(f"case {number}: video requires R2 poster and playable MP4")
    order = curated.get("category_order", [])
    if len(order) != len(set(order)) or set(order) != {s["category_key"] for s in candidates}:
        errors.append("category order does not cover independent selected categories")
    if set(curated.get("category_names", {})) != set(order):
        errors.append("category names differ from category order")
    return errors


def validate_fidelity(items: list, fidelity: dict) -> list[str]:
    errors = []
    for item, case in zip(items, fidelity.get("cases", [])):
        visuals = [a["poster_url"] if a["kind"] == "video" else a["url"] for a in item["media_assets"]]
        videos = [a["url"] for a in item["media_assets"] if a["kind"] == "video"]
        if any(case.get(field) != item.get(field) for field in ("public_number", "source_url")) or case.get("source_media_urls") != item.get("media_source_urls") or case.get("expected_public_media_urls") != visuals:
            errors.append(f"case {item['public_number']}: fidelity identity/media set differs")
        actual_videos = case.get("playable_video_urls", [case["playable_video_url"]] if case.get("playable_video_url") else [])
        if actual_videos != videos:
            errors.append(f"case {item['public_number']}: fidelity playback set differs")
    return errors


def validate_public_copy(text: str, filename: str) -> list[str]:
    errors = []
    # The repository slug is retained by owner request. It is an identity, not model copy.
    scrubbed = text.replace("awesome-gemini-3.6-flash-guide-and-use-cases", "repository-slug")
    if re.search(r"gemini[ _-]*3[._-]6[ _-]*flash", scrubbed, re.I):
        errors.append(f"{filename}: stale model content")
    if re.search(r"(?:/Users/|/home/|file://)", text):
        errors.append(f"{filename}: non-portable private path")
    if re.search(r"(?:independently verified smoke|verified smoke|smoke test verified|smoke-test evidence)", text, re.I):
        errors.append(f"{filename}: unsupported independent smoke verification claim")
    for url in URL_RE.findall(text):
        parsed = urllib.parse.urlparse(url)
        if parsed.hostname in {"direct.evolink.ai", "api.evolink.ai"} and "utm_" in parsed.query:
            errors.append(f"{filename}: API endpoint must not carry UTM")
    return errors


def validate_localized_case(case: dict, item: dict, locale: str) -> list[str]:
    errors = []
    for field in ("title", "takeaway", "notes"):
        value = str(case.get(field, "")).strip()
        original = str(item.get("body_notes" if field == "notes" else field, "")).strip()
        if not value or value == original:
            errors.append(f"{locale} case {item['public_number']}: {field} is empty or unchanged from English")
    return errors


def validate_conversion_url(url: str, filename: str) -> list[str]:
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)
    if parsed.hostname == "evolink.ai":
        if query.get("utm_source") != ["github"] or query.get("utm_campaign") != [CAMPAIGN] or not query.get("utm_medium") or not query.get("utm_content"):
            return [f"{filename}: conversion URL has incorrect UTM attribution"]
    return []


def validate_conversion_placements(actual: dict, docs_url: str, filename: str) -> list[str]:
    expected = {
        MODEL_PAGE: [("banner", "readme_banner"), ("badge", "model_try"),
                     ("readme", "landing_overview"), ("quickstart", "browser_try")],
        API_KEYS: [("overview", "api_key"), ("quickstart", "api_key")],
        docs_url: [("badge", "docs_link"), ("docs", "first_run")],
    }
    if set(actual) != set(expected) or any(sorted(actual.get(base, [])) != sorted(pairs) for base, pairs in expected.items()):
        return [f"{filename}: conversion placement UTM matrix differs"]
    return []


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
        "data/localization-cache.json", "data/usecase-update-config.json", "data/source-inventory.json",
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
    inventory_path = ROOT / "data/source-inventory.json"
    if hashlib.sha256(inventory_path.read_bytes()).hexdigest() != INVENTORY_SHA256:
        errors.append("frozen independent candidate inventory hash differs")
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    errors.extend(validate_source_inventory(curated, inventory))
    if numbers != expected_numbers:
        errors.append("public case numbers are not contiguous")
    if len({item.get("source_url") for item in items}) != expected_count:
        errors.append("source URLs are not unique")
    if any(item.get("quality_tier") != "high" or item.get("decision") != "high_confidence_update" for item in items):
        errors.append("curated data includes a non-high-confidence case")
    expected_prompts = sum(bool(case.get("prompt_public")) for case in inventory["cases"])
    if any(not item.get("media_assets") or not item.get("media_source_urls") for item in items):
        errors.append("one or more cases lacks source-media lineage")

    visual_urls = [
        asset["poster_url"] if asset["kind"] == "video" else asset["url"]
        for item in items for asset in item.get("media_assets", [])
    ]
    playable_urls = [
        asset["url"] for item in items for asset in item.get("media_assets", []) if asset["kind"] == "video"
    ]
    source_media = [asset for case in inventory["cases"] for asset in case["source_media"]]
    if len(visual_urls) != len(source_media):
        errors.append("public visual count differs from independent source inventory")
    if len(playable_urls) != sum(asset["kind"] == "video" for asset in source_media):
        errors.append("playable video count differs from independent source inventory")
    if any(not url.startswith(R2_PREFIX) for url in [*visual_urls, *playable_urls]):
        errors.append("one or more public media URLs are outside the isolated R2 namespace")

    fidelity = json.loads((ROOT / "data/source-fidelity-manifest.json").read_text(encoding="utf-8"))
    errors.extend(validate_fidelity(items, fidelity))
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
        if locale in {"zh-CN", "zh-TW"} and re.search(r"[\u3400-\u9fff]Gemini|Hydrogen[\u3400-\u9fff]", localized["strings"]["quick_model"]):
            errors.append(f"data/localizations/{locale}.json: model link label lacks CJK/Latin spacing")
        if sorted(int(key) for key in localized.get("cases", {})) != expected_numbers:
            errors.append(f"data/localizations/{locale}.json: case keys differ from 1..{expected_count}")
            continue
        for item in items:
            case = localized["cases"][str(item["public_number"])]
            errors.extend(validate_localized_case(case, item, locale))
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
        errors.extend(validate_public_copy(text, filename))
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
        if sum(text.count(f'src="{url}"') for url in visual_urls) != len(visual_urls):
            errors.append(f"{filename}: rendered source visual count differs")
        if sum(text.count(f']({url})') for url in playable_urls) != len(playable_urls):
            errors.append(f"{filename}: playable source video count differs")
        if text.count("```text") != expected_prompts:
            errors.append(f"{filename}: public prompt block count differs")
        menu_start = text.find("## 📑")
        first_case = text.find('<a id="case-')
        menu_text = text[menu_start:first_case] if menu_start >= 0 else ""
        if re.findall(r'\]\(#case-(\d+)\)', menu_text) != [str(n) for n in expected_numbers]:
            errors.append(f"{filename}: centralized menu identities/order differ")
        category_anchors = [a for a in re.findall(r'<a id="([^"\n]+)"></a>', text) if a in curated.get("category_order", [])]
        if category_anchors != curated.get("category_order"):
            errors.append(f"{filename}: category anchors/order differ")
        for item in items:
            block = text.split(f'<a id="case-{item["public_number"]}"></a>', 1)[-1].split("\n---", 1)[0]
            if item["date"] not in block or item["author_url"] not in block or item["type"] not in block:
                errors.append(f'{filename}: case {item["public_number"]} attribution/date/type differs')
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
        if docs_routes != [DOC_LOCALE_BY_README[locale]] * 2:
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
            errors.extend(validate_conversion_url(url, filename))
            parsed = urllib.parse.urlparse(url)
            base = urllib.parse.urlunparse(parsed._replace(query="", fragment=""))
            query = urllib.parse.parse_qs(parsed.query)
            if base in conversion_pairs:
                if query.get("utm_source") != ["github"] or query.get("utm_campaign") != [CAMPAIGN]:
                    errors.append(f"{filename}: conversion URL has incorrect source or campaign")
                conversion_pairs[base].append((query.get("utm_medium", [""])[0], query.get("utm_content", [""])[0]))
        errors.extend(validate_conversion_placements(conversion_pairs, expected_docs, filename))

        overview_text = text.split(f'## 📊', 1)[-1].split(f'## 📑', 1)[0]
        related_text = text.split('<a id="related-repositories"></a>', 1)[-1].split('<a id="quick-start"></a>', 1)[0]
        if GOOGLE_RELEASE not in overview_text or MODEL_CARD not in overview_text:
            errors.append(f"{filename}: official sources are not placed in Overview")
        if GOOGLE_RELEASE in related_text or MODEL_CARD in related_text:
            errors.append(f"{filename}: official sources are incorrectly placed in Related Repositories")
        if RELATED_REPOSITORY not in related_text or "https://github.com/Evolink-AI)" in related_text:
            errors.append(f"{filename}: Related Repositories does not link the verified adjacent repository")
        headings = re.findall(r"^## .+$", text, re.MULTILINE)
        quick_start = text.find('<a id="quick-start"></a>')
        if not 0 <= quick_start < first_case or "🙏" not in headings[-1]:
            errors.append(f"{filename}: Quick Start must precede cases and Acknowledge must be last")
        pre_code = text[quick_start:].split("```bash", 1)[0]
        if len(re.findall(r"\]\(https://evolink\.ai/", pre_code)) > 2:
            errors.append(f"{filename}: Quick Start exceeds two pre-code conversion links")
        if fidelity.get("owner_presentation", {}).get("quick_start_position") != "before-first-case":
            errors.append("source-fidelity Quick Start position differs from before-first-case")
        if creator_line not in text.split('<a id="acknowledge"></a>', 1)[-1]:
            errors.append(f"{filename}: canonical inline creator list differs")
        if re.search(r'<(?:img|video)[^>]+src="[^"]+\.mp4', text):
            errors.append(f"{filename}: MP4 is directly embedded instead of poster-linked")
        if index == 0:
            english_titles = titles
        else:
            changed = sum(a != b for a, b in zip(titles, english_titles))
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

    rendered = subprocess.run([sys.executable, str(ROOT / "scripts/build_readmes.py"), "--check"], cwd=ROOT, capture_output=True, text=True)
    if rendered.returncode:
        errors.append("README regeneration check failed: " + rendered.stdout.strip() + rendered.stderr.strip())
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
