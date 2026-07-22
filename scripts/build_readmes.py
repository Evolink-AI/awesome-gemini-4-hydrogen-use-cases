#!/usr/bin/env python3
"""Render the English and localized README files from reviewed structured data."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
R2 = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases"
MODEL_PAGE = "https://evolink.ai/gemini-3-6-flash"
API_KEYS = "https://evolink.ai/dashboard/keys"
API_DOCS = "https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart"
GOOGLE_RELEASE = "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/"
MODEL_CARD = "https://deepmind.google/models/model-cards/gemini-3-6-flash/"
CAMPAIGN = "awesome-gemini-3-6-flash-guide-and-use-cases"
MINIMAL_CURL = r"""export EVOLINK_API_KEY="your_api_key_here"

curl --fail-with-body --silent --show-error \
  --request POST \
  --url "https://direct.evolink.ai/v1beta/models/gemini-3.6-flash:generateContent" \
  --header "Authorization: Bearer $EVOLINK_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{"contents":[{"role":"user","parts":[{"text":"Reply exactly: OK"}]}],"generationConfig":{"candidateCount":1,"maxOutputTokens":128,"temperature":0}}'"""

CATEGORY_EMOJI = {
    "efficiency-agents": "⚡",
    "coding-apps": "💻",
    "web-games-3d": "🎮",
    "evaluations": "🧪",
    "safety-limits": "🛡️",
}

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
    "title": "Awesome Gemini 3.6 Flash Guide and Use Cases",
    "introduction": "Introduction",
    "intro": "Welcome to a source-backed guide to Gemini 3.6 Flash in practice",
    "mission": "This repository collects concrete Gemini 3.6 Flash workflows, builds, evaluations, comparisons, and limits from public creator evidence",
    "boundary": "Every included case comes from the reviewed source package. Titles link to original posts, authors link to creator profiles, and prompts appear only when the source text actually contains them",
    "overview": "Overview",
    "overview_cases": "33 high-confidence cases selected from 33 reviewed source posts",
    "overview_coverage": "Coverage includes agents, coding, websites, games, 3D, benchmark-style comparisons, and practical safety limits",
    "overview_media": "All 24 video cases provide a visible poster and a playable R2-hosted MP4; image cases preserve every reviewed source image",
    "overview_model": "EvoLink lists the production model ID as `gemini-3.6-flash`; this repository links to the current model and Gemini Native API surfaces",
    "note": "This collection favors observable evidence over hype. It does not reconstruct missing prompts, infer unpublished setup steps, or generalize one creator's result into a universal benchmark",
    "start_here": "Start here",
    "explore": "explore Gemini 3.6 Flash",
    "get_key": "get an API key",
    "open_docs": "open the Gemini Native API docs",
    "menu": "Menu",
    "section": "Section",
    "cases": "Cases",
    "case": "Case",
    "category": "Category",
    "what_it_shows": "What it shows",
    "type": "Type",
    "by": "by",
    "prompt": "Prompt",
    "date": "Date",
    "play_video": "Play source video",
    "related": "Related Repositories",
    "related_org": "More model guides and API examples from EvoLink",
    "related_note": "No dedicated installable Gemini 3.6 Flash skill was independently verified during this publication",
    "quickstart": "Quick Start",
    "quick_intro": "Use the verified public surfaces below to start with model ID `gemini-3.6-flash`",
    "quick_model": "Open the Gemini 3.6 Flash model page",
    "quick_key": "Create or manage an EvoLink API key",
    "quick_docs": "Follow the Gemini Native API Quick Start",
    "quick_run": "Run this verified minimal request",
    "quick_success": "Expected result: a JSON response whose visible text is `OK`",
    "important": "This exact request was verified against the live endpoint with HTTP 200 and visible output `OK`; keep your key in the environment and never commit it",
    "acknowledge": "Acknowledge",
    "ack_text": "This collection exists because creators and practitioners shared their Gemini 3.6 Flash work publicly",
    "thanks": "Thanks to the source creators represented here",
    "correction": "We cannot guarantee that every post identifies the earliest original creator. If attribution, translation, or wording needs correction, open a correction issue with a public source",
    "contribute": "To propose another source-backed case, open an issue or pull request and follow the contribution checklist",
}


def with_utm(url: str, medium: str, content: str) -> str:
    separator = "&" if "?" in url else "?"
    return f"{url}{separator}utm_source=github&utm_medium={medium}&utm_campaign={CAMPAIGN}&utm_content={content}"


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
    lines = [
        '<div align="center">',
        "",
        f'<a href="{with_utm(MODEL_PAGE, "banner", "readme_banner")}"><img src="{R2}/images/banner.png" alt="Awesome Gemini 3.6 Flash guide and use cases banner" width="760"></a>',
        "",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)",
        f'[![Gemini 3.6 Flash](https://img.shields.io/badge/Gemini_3.6_Flash-Model_Page-00d4e6)]({with_utm(MODEL_PAGE, "badge", "top_badge")})',
        f'[![Gemini Native API](https://img.shields.io/badge/Gemini_Native_API-Quick_Start-f22f3d)]({with_utm(API_DOCS, "docs", "docs_link")})',
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
        f'**{strings["start_here"]}: [{strings["explore"]}]({with_utm(MODEL_PAGE, "quickstart", "model_link")}) · [{strings["get_key"]}]({with_utm(API_KEYS, "quickstart", "api_key")}) · [{strings["open_docs"]}]({with_utm(API_DOCS, "docs", "first_run")})**',
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
        f'| [{strings["related"]}](#related-repositories) | {strings["related"]} |',
        f'| [{strings["quickstart"]}](#quick-start) | {strings["quickstart"]} |',
        f'| [{strings["acknowledge"]}](#acknowledge) | {strings["acknowledge"]} |',
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
                lines.extend([f'**{strings["prompt"]}:**', "", "```text", item["prompt_text"], "```", ""])
            media = media_block(item, strings)
            if media:
                lines.extend(["\n\n".join(media), ""])
            lines.extend([f'{strings["type"]}: {item["type"]} | {strings["date"]}: {item["date"]}', "", "---", ""])

    lines.extend([
        '<a id="related-repositories"></a>',
        f'## {strings["related"]}',
        "",
        f'- [EvoLink-AI on GitHub](https://github.com/Evolink-AI) — {strings["related_org"]}',
        f'- [Gemini 3.6 Flash official launch]({GOOGLE_RELEASE})',
        f'- [Gemini 3.6 Flash model card]({MODEL_CARD})',
        f'- {strings["related_note"]}',
        "",
        '<a id="quick-start"></a>',
        f'## ⚡ {strings["quickstart"]}',
        "",
        strings["quick_intro"],
        "",
        f'1. [{strings["quick_model"]}]({with_utm(MODEL_PAGE, "quickstart", "model_link")})',
        f'2. [{strings["quick_key"]}]({with_utm(API_KEYS, "quickstart", "api_key")})',
        f'3. [{strings["quick_docs"]}]({with_utm(API_DOCS, "docs", "first_run")})',
        "",
        strings["quick_run"],
        "",
        "```bash",
        MINIMAL_CURL,
        "```",
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
    return "\n".join(lines)


def main() -> None:
    curated = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    (ROOT / "README.md").write_text(render(curated, "en", None), encoding="utf-8")
    print("README.md")
    locale_dir = ROOT / "data/localizations"
    for locale, filename, _label, _color in LANGUAGES[1:]:
        config_path = locale_dir / f"{locale}.json"
        if not config_path.exists():
            continue
        localized = json.loads(config_path.read_text(encoding="utf-8"))
        (ROOT / filename).write_text(render(curated, locale, localized), encoding="utf-8")
        print(filename)


if __name__ == "__main__":
    main()
