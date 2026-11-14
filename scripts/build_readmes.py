#!/usr/bin/env python3
"""Render the English and localized README files from reviewed structured data."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
R2 = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113"
MODEL_PAGE = "https://evolink.ai/gemini-4-hydrogen"
API_KEYS = "https://evolink.ai/dashboard/keys"
API_DOCS_PATH = "api-manual/language-series/gemini/native-api/native-api-quickstart"
DOC_LOCALE_BY_README = {
    "en": "en",
    "es": "es",
    "pt": "en",
    "ja": "ja",
    "ko": "ko",
    "de": "de",
    "fr": "fr",
    "tr": "en",
    "zh-TW": "en",
    "zh-CN": "cn",
    "ru": "en",
}
GOOGLE_RELEASE = "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/"
MODEL_CARD = "https://deepmind.google/models/model-cards/gemini-4-hydrogen/"
RELATED_REPOSITORY = "https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases"
CAMPAIGN = "awesome-gemini-4-hydrogen-guide-and-use-cases"
MINIMAL_CURL = r"""export EVOLINK_API_KEY="your_api_key_here"

curl --fail-with-body --silent --show-error \
  --request POST \
  --url "https://direct.evolink.ai/v1beta/models/gemini-4-hydrogen:generateContent" \
  --header "Authorization: Bearer $EVOLINK_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{"contents":[{"role":"user","parts":[{"text":"Reply exactly: OK"}]}],"generationConfig":{"candidateCount":1,"maxOutputTokens":2048,"temperature":0,"thinkingConfig":{"thinkingLevel":"low"}}}'"""

CATEGORY_EMOJI = {'agents': '⚡', 'apps-learning': '💻', 'data-search': '📊', 'interactive-3d': '🎮', 'comparisons-limits': '🧪'}

LANGUAGES = [
    ("en", "README.md", "🇺🇸 English", "111111"),
    ("es", "README_es.md", "🇪🇸 Español", "ffb703"),
    ("pt", "README_pt.md", "🇵🇹 Português", "2a9d8f"),
    ("ja", "README_ja.md", "🇯🇵 日本語", "52b788"),
    ("ko", "README_ko.md", "🇰🇷 한국어", "4ea8de"),
    ("de", "README_de.md", "🇩🇪 Deutsch", "f4a261"),
    ("fr", "README_fr.md", "🇫🇷 Français", "e76f51"),
    ("tr", "README_tr.md", "🇹🇷 Türkçe", "d62828"),
    ("zh-TW", "README_zh-TW.md", "🇹🇼 繁體中文", "8338ec"),
    ("zh-CN", "README_zh-CN.md", "🇨🇳 简体中文", "ef476f"),
    ("ru", "README_ru.md", "🇷🇺 Русский", "577590"),
]

ENGLISH = {
    "title": "Awesome Gemini 4 Hydrogen Guide and Use Cases",
    "introduction": "Introduction",
    "intro": "Explore Gemini 4 Hydrogen through source-backed applications, coding workflows, and practical comparisons.",
    "mission": "40 selected examples show what people built, how they worked, and where the results fell short.",
    "boundary": "Each case links to its source and credits its author. Demos, provider examples, and creator comparisons are labeled in the notes; missing prompts are not reconstructed.",
    "overview": "Overview",
    "overview_cases": "40 selected cases from 75 reviewed demo posts in a capped 500-post X collection, captured on November 13, 2026.",
    "overview_coverage": "Five categories cover agents, learning and apps, spreadsheets and Search, interactive 3D, and comparisons and limitations.",
    "overview_media": "All 41 selected source visuals are preserved: 38 playable videos with posters and 3 images.",
    "overview_model": "Gemini 4 Hydrogen was announced on November 12, 2026. Explore the model and its current access options on EvoLink.",
    "note": "Model attribution, costs, timing, and results remain source claims unless stated otherwise. Video review used sampled frames, not full functional testing. Recordings of coded applications are not evidence of native video generation. Different harnesses, reasoning levels, or iteration counts make comparisons uncontrolled.",
    "official_sources": "Official references",
    "official_launch": "Google announcement",
    "official_model_card": "Google DeepMind model card",
    "start_here": "Start here",
    "explore": "Explore Hydrogen on EvoLink",
    "get_key": "Get an API key",
    "open_docs": "Gemini Native API documentation",
    "menu": "Menu",
    "section": "Section",
    "cases": "Cases",
    "case": "Case",
    "category": "Category",
    "what_it_shows": "What to try",
    "type": "Type",
    "by": "by",
    "prompt": "Prompt",
    "date": "Date",
    "play_video": "Play source video",
    "related": "Related Repositories",
    "related_org": "Gemini 4 Carbon examples and comparisons",
    "quickstart": "Quick Start",
    "quick_intro": "Start on EvoLink, then use the Gemini native API when you want to integrate Hydrogen into an application.",
    "quick_model": "View Gemini 4 Hydrogen in your browser",
    "quick_key": "Create or manage an EvoLink API key",
    "quick_docs": "Read the Gemini Native API Quick Start",
    "quick_run": "Minimal native API request",
    "quick_success": "Read the generated text from the response's candidates[].content.parts[].text fields.",
    "important": "Keep your API key in an environment variable and never commit it. See the API documentation for streaming, reasoning, and other request options.",
    "acknowledge": "Acknowledge",
    "ack_text": "Thanks to the creators, developers, and evaluators who shared their Hydrogen work publicly.",
    "thanks": "Source creators",
    "correction": "Attribution follows the cited public sources and may not identify the earliest creator. For corrections or removal requests, open an issue with a public source.",
    "contribute": "Suggest a source-backed example through an issue or pull request following the contribution checklist."
}


def with_utm(url: str, medium: str, content: str) -> str:
    separator = "&" if "?" in url else "?"
    return f"{url}{separator}utm_source=github&utm_medium={medium}&utm_campaign={CAMPAIGN}&utm_content={content}"


def api_docs_for(locale: str) -> str:
    doc_locale = DOC_LOCALE_BY_README[locale]
    return f"https://evolink.ai/docs/{doc_locale}/{API_DOCS_PATH}"


def badges() -> str:
    rows = []
    for _locale, filename, label, color in LANGUAGES:
        encoded = label.replace(" ", "_").replace("-", "--")
        rows.append(f"[![{label}](https://img.shields.io/badge/{encoded}-{color})]({filename})")
    return "\n".join(rows)


def media_block(item: dict, strings: dict) -> list[str]:
    blocks: list[str] = []
    assets = item.get("media_assets", [])
    videos = [asset for asset in assets if asset["kind"] == "video"]
    images = [asset for asset in assets if asset["kind"] == "image"]

    for asset in videos:
        blocks.extend([
            f'<a href="{asset["url"]}"><img src="{asset["poster_url"]}" alt="Case {item["public_number"]} source video poster" height="360"></a>',
            f'[{strings["play_video"]}]({asset["url"]})',
        ])

    if len(images) == 1:
        asset = images[0]
        blocks.append(
            f'<a href="{asset["url"]}"><img src="{asset["url"]}" alt="Case {item["public_number"]} source image 1" height="360"></a>'
        )
    elif images:
        gallery = ["<table>"]
        for offset in range(0, len(images), 2):
            gallery.append("<tr>")
            for index, asset in enumerate(images[offset:offset + 2], start=offset + 1):
                gallery.extend([
                    '<td width="50%" valign="top" align="center">',
                    f'<a href="{asset["url"]}"><img src="{asset["url"]}" alt="Case {item["public_number"]} source image {index}" width="100%"></a>',
                    "</td>",
                ])
            if offset + 1 >= len(images):
                gallery.append('<td width="50%" valign="top"></td>')
            gallery.append("</tr>")
        gallery.append("</table>")
        blocks.append("\n".join(gallery))
    return blocks


def render(curated: dict, locale: str, localized: dict | None) -> str:
    items = curated["items"]
    strings = localized["strings"] if localized else ENGLISH
    categories = localized["categories"] if localized else curated["category_names"]
    translated_cases = localized["cases"] if localized else {}
    handles = list(dict.fromkeys(item["author_handle"] for item in items))
    api_docs = api_docs_for(locale)
    docs_fallback = DOC_LOCALE_BY_README[locale] == "en" and locale != "en"
    docs_badge_alt = "Gemini Native API (English)" if docs_fallback else "Gemini Native API"
    docs_badge_text = "Gemini_Native_API-English" if docs_fallback else "Gemini_Native_API-Quick_Start"
    lines = [
        '<div align="center">',
        "",
        f'<a href="{with_utm(MODEL_PAGE, "banner", "readme_banner")}"><img src="{R2}/images/banner.png" alt="Awesome Gemini 4 Hydrogen guide and use cases banner" width="760"></a>',
        "",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)",
        f'[![View Hydrogen in your browser](https://img.shields.io/badge/View_Hydrogen-Browser-4285f4)]({with_utm(MODEL_PAGE, "badge", "model_try")})',
        f'[![{docs_badge_alt}](https://img.shields.io/badge/{docs_badge_text}-f22f3d)]({with_utm(api_docs, "badge", "docs_link")})',
        "",
        badges(),
        "",
        "</div>",
        "",
        f'# {strings["title"]}',
        "",
        f'## 🍌 {strings["introduction"]}',
        "",
        strings["intro"],
        "",
        f'**{strings["mission"]}**',
        "",
        strings["boundary"],
        "",
        f'## 📊 {strings["overview"]}',
        "",
        f'- {strings["overview_cases"]}',
        f'- {strings["overview_coverage"]}',
        f'- {strings["overview_media"]}',
        f'- {strings["overview_model"]}',
        "",
        "> [!NOTE]",
        f'> {strings["note"]}',
        "",
        f'**{strings["official_sources"]}: [{strings["official_launch"]}]({GOOGLE_RELEASE}) · [{strings["official_model_card"]}]({MODEL_CARD})**',
        "",
        f'**{strings["start_here"]}: [{strings["explore"]}]({with_utm(MODEL_PAGE, "readme", "landing_overview")}) · [{strings["get_key"]}]({with_utm(API_KEYS, "overview", "api_key")})**',
        "",
        f'## 📑 {strings["menu"]}',
        "",
        f'| {strings["section"]} | {strings["cases"]} |',
        "|---|---|",
    ]

    for key in curated["category_order"]:
        count = sum(1 for item in items if item["category_key"] == key)
        lines.append(f'| [{CATEGORY_EMOJI[key]} {categories[key]}](#{key}) | {count} |')
    lines.extend([
        f'| [{strings["related"]}](#related-repositories) |  |',
        f'| [{strings["quickstart"]}](#quick-start) |  |',
        f'| [{strings["acknowledge"]}](#acknowledge) |  |',
        "",
        f'| {strings["case"]} | {strings["category"]} | {strings["what_it_shows"]} | {strings["type"]} |',
        "|---|---|---|---|",
    ])
    for item in items:
        translated = translated_cases.get(str(item["public_number"]), item)
        lines.append(
            f'| [{translated["title"]}](#case-{item["public_number"]}) | {categories[item["category_key"]]} | {translated["takeaway"]} | {item["type"]} |'
        )

    for key in curated["category_order"]:
        lines.extend(["", f'<a id="{key}"></a>', f'## {CATEGORY_EMOJI[key]} {categories[key]}', ""])
        for item in [entry for entry in items if entry["category_key"] == key]:
            translated = translated_cases.get(str(item["public_number"]), item)
            lines.extend([
                f'<a id="case-{item["public_number"]}"></a>',
                f'### {strings["case"]} {item["public_number"]}: [{translated["title"]}]({item["source_url"]}) ({strings["by"]} [{item["author_handle"]}]({item["author_url"]}))',
                "",
                f'**{translated["takeaway"]}**',
                "",
                translated.get("notes", translated.get("body_notes", "")),
                "",
            ])
            if item.get("prompt_public"):
                lines.extend([f'**{strings["prompt"]}:**', "", "```", item["prompt_text"], "```", ""])
            media = media_block(item, strings)
            if media:
                lines.extend(["\n\n".join(media), ""])
            lines.extend([f'{strings["type"]}: {item["type"]} | {strings["date"]}: {item["date"]}', "", "---", ""])

    lines.extend([
        '<a id="related-repositories"></a>',
        f'## {strings["related"]}',
        "",
        f'- [Gemini 4 Carbon Guide and Use Cases]({RELATED_REPOSITORY}): {strings["related_org"]}',
        "",
        '<a id="quick-start"></a>',
        f'## ⚡ {strings["quickstart"]}',
        "",
        strings["quick_intro"],
        "",
        f'1. [{strings["quick_model"]}]({with_utm(MODEL_PAGE, "quickstart", "browser_try")})',
        f'2. [{strings["quick_key"]}]({with_utm(API_KEYS, "quickstart", "api_key")})',
        "",
        strings["quick_run"],
        "",
        "```bash",
        MINIMAL_CURL,
        "```",
        "",
        "`POST https://direct.evolink.ai/v1beta/models/gemini-4-hydrogen:generateContent`",
        "",
        f'[{strings["quick_docs"]}]({with_utm(api_docs, "docs", "first_run")})',
        "",
        "> [!TIP]",
        f'> {strings["quick_success"]}',
        "",
        "> [!IMPORTANT]",
        f'> {strings["important"]}',
        "",
        '<a id="acknowledge"></a>',
        f'## 🙏 {strings["acknowledge"]}',
        "",
        strings["ack_text"],
        "",
        f'**{strings["thanks"]}:**',
        "",
        ", ".join(f'[{handle}](https://x.com/{handle[1:]})' for handle in handles),
        "",
        f'*{strings["correction"]}*',
        "",
        strings["contribute"],
        "",
    ])
    rendered = "\n".join(lines)
    quick_start = rendered.index('<a id="quick-start"></a>')
    acknowledge = rendered.index('<a id="acknowledge"></a>')
    quick_block = rendered[quick_start:acknowledge]
    rendered = rendered[:quick_start] + rendered[acknowledge:]
    menu = rendered.index(f'## 📑 {strings["menu"]}')
    return rendered[:menu] + quick_block + rendered[menu:]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated README files differ")
    parser.add_argument("--english-only", action="store_true", help="Render or check the English gate only")
    args = parser.parse_args()
    curated = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    failures = []
    languages = LANGUAGES[:1] if args.english_only else LANGUAGES
    for locale, filename, _label, _color in languages:
        localized = None if locale == "en" else json.loads((ROOT / f"data/localizations/{locale}.json").read_text(encoding="utf-8"))
        expected = render(curated, locale, localized)
        target = ROOT / filename
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != expected:
                failures.append(filename)
        else:
            target.write_text(expected, encoding="utf-8")
            print(filename)
    if failures:
        print("FAIL: generated README drift: " + ", ".join(failures), file=sys.stderr)
        return 1
    if args.check:
        print(f"PASS: {len(languages)} README files match canonical data")
    return 0


if __name__ == "__main__":
    sys.exit(main())
