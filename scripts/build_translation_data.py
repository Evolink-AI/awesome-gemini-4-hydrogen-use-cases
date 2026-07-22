#!/usr/bin/env python3
"""Build reviewed localization payloads with Google Translate as a first-pass translator."""

from __future__ import annotations

import json
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from build_readmes import ENGLISH, LANGUAGES


ROOT = Path(__file__).resolve().parents[1]
LOCALE_DIR = ROOT / "data/localizations"
CACHE_PATH = ROOT / "data/localization-cache.json"
SEPARATOR_1 = "<<<G36SEP1>>>"
SEPARATOR_2 = "<<<G36SEP2>>>"

ZH_OVERRIDES = {
    "zh-CN": {
        "title": "Awesome Gemini 3.6 Flash 指南与用例",
        "intro": "欢迎阅读这份有公开来源证据支撑的 Gemini 3.6 Flash 实践指南",
        "mission": "本仓库收集公开创作者证据中的 Gemini 3.6 Flash 工作流、构建成果、评估对比与实际限制",
        "boundary": "每个案例都来自经过审查的来源包，标题链接到原始帖子，作者链接到创作者主页，只有来源文本确实包含 prompt 时才会收录",
        "overview_model": "EvoLink 标注的正式 model ID 是 `gemini-3.6-flash`，本仓库链接到当前模型页与 Gemini Native API 接入文档",
        "note": "本合集优先保留可观察证据，不重建缺失的 prompt，不推断未公开的设置步骤，也不把单个创作者的结果泛化为通用 benchmark",
        "by": "作者",
        "prompt": "提示词",
        "acknowledge": "致谢",
        "quick_intro": "通过下方经过验证的公开入口开始使用 model ID `gemini-3.6-flash`",
        "quick_run": "运行这个已验证的最小请求",
        "quick_success": "预期结果：可见文本为 `OK` 的 JSON 响应",
        "important": "该请求已在实时 endpoint 验证为 HTTP 200，且可见输出为 `OK`；请将密钥保存在环境变量中，切勿提交到版本库",
        "correction": "我们无法保证每条帖子都指向最早的原创者，如归属、翻译或措辞需要修正，请提交带公开来源的 correction issue",
    },
    "zh-TW": {
        "title": "Awesome Gemini 3.6 Flash 指南與用例",
        "intro": "歡迎閱讀這份有公開來源證據支撐的 Gemini 3.6 Flash 實踐指南",
        "mission": "本倉庫收集公開創作者證據中的 Gemini 3.6 Flash 工作流、建置成果、評估比較與實際限制",
        "boundary": "每個案例都來自經過審查的來源包，標題連結到原始貼文，作者連結到創作者主頁，只有來源文字確實包含 prompt 時才會收錄",
        "overview_model": "EvoLink 標註的正式 model ID 是 `gemini-3.6-flash`，本倉庫連結到目前模型頁與 Gemini Native API 接入文件",
        "note": "本合集優先保留可觀察證據，不重建缺失的 prompt，不推斷未公開的設定步驟，也不把單一創作者的結果泛化為通用 benchmark",
        "by": "作者",
        "prompt": "提示詞",
        "acknowledge": "致謝",
        "quick_intro": "透過下方經過驗證的公開入口開始使用 model ID `gemini-3.6-flash`",
        "quick_run": "執行這個已驗證的最小請求",
        "quick_success": "預期結果：可見文字為 `OK` 的 JSON 回應",
        "important": "此請求已在即時 endpoint 驗證為 HTTP 200，且可見輸出為 `OK`；請將金鑰保存在環境變數中，切勿提交到版本庫",
        "correction": "我們無法保證每則貼文都指向最早的原創者，如歸屬、翻譯或措辭需要修正，請提交附公開來源的 correction issue",
    },
}

ZH_REPLACEMENTS = {
    "zh-CN": {
        "双子座": "Gemini", "十四行诗": "Sonnet", "代币": "token", "思想标记": "思考 token",
        "反重力": "Antigravity", "新型号": "新模型", "源创作者": "来源创作者",
    },
    "zh-TW": {
        "雙子座": "Gemini", "十四行詩": "Sonnet", "代幣": "token", "思想標記": "思考 token",
        "反重力": "Antigravity", "新型號": "新模型", "源創作者": "來源創作者",
    },
}


def normalize(text: str, locale: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("Gemini 3.6 Flash", "Gemini 3.6 Flash")
    text = text.replace("gemini-3.6-flash", "gemini-3.6-flash")
    if locale in {"zh-CN", "zh-TW"}:
        text = text.replace("。", "")
        for source, target in ZH_REPLACEMENTS[locale].items():
            text = text.replace(source, target)
    return text


def polish_payload(payload: dict, locale: str) -> dict:
    if locale in ZH_OVERRIDES:
        payload["strings"].update(ZH_OVERRIDES[locale])
    for section in ("strings", "categories"):
        payload[section] = {key: normalize(value, locale) for key, value in payload[section].items()}
    for case in payload["cases"].values():
        for key in ("title", "takeaway", "notes"):
            case[key] = normalize(case[key], locale)
    return payload


def translate(text: str, locale: str) -> str:
    command = [
        "curl", "-sS", "--retry", "3", "--retry-delay", "1", "--get",
        "https://translate.googleapis.com/translate_a/single",
        "--data-urlencode", "client=gtx",
        "--data-urlencode", "sl=en",
        "--data-urlencode", f"tl={locale}",
        "--data-urlencode", "dt=t",
        "--data-urlencode", f"q={text}",
        "-H", "User-Agent: Mozilla/5.0",
    ]
    last_error = "unknown translation failure"
    for attempt in range(4):
        result = subprocess.run(command, check=False, capture_output=True, text=True, timeout=45)
        if result.returncode == 0:
            try:
                payload = json.loads(result.stdout)
                translated = "".join(segment[0] for segment in payload[0] if segment and segment[0])
                if translated.strip():
                    return translated.strip()
            except (json.JSONDecodeError, TypeError, IndexError) as error:
                last_error = str(error)
        else:
            last_error = result.stderr.strip() or f"curl exit {result.returncode}"
        time.sleep(1 + attempt)
    raise RuntimeError(f"{locale}: {last_error}")


def translate_case(item: dict, locale: str) -> tuple[str, dict]:
    source = f'{item["title"]}\n{SEPARATOR_1}\n{item["takeaway"]}\n{SEPARATOR_2}\n{item["body_notes"]}'
    output = translate(source, locale)
    parts = re.split(r"\s*<<<G36SEP[12]>>>\s*", output)
    if len(parts) != 3:
        raise RuntimeError(f'{locale} case {item["public_number"]}: separator mismatch')
    return str(item["public_number"]), {
        "title": normalize(parts[0], locale),
        "takeaway": normalize(parts[1], locale),
        "notes": normalize(parts[2], locale),
    }


def translate_mapping(mapping: dict[str, str], locale: str) -> dict[str, str]:
    translated: dict[str, str] = {}
    entries = list(mapping.items())
    for offset in range(0, len(entries), 7):
        chunk = entries[offset:offset + 7]
        markers = [f"⟦G36S{offset + index:03d}⟧" for index in range(len(chunk) - 1)]
        pieces: list[str] = []
        for index, (_key, value) in enumerate(chunk):
            pieces.append(value)
            if index < len(markers):
                pieces.append(markers[index])
        output = translate("\n".join(pieces), locale)
        if markers:
            pattern = r"\s*(?:" + "|".join(re.escape(marker) for marker in markers) + r")\s*"
            values = re.split(pattern, output)
        else:
            values = [output]
        if len(values) != len(chunk):
            raise RuntimeError(f"{locale} static translation separator mismatch at {offset}")
        for (key, _value), value in zip(chunk, values, strict=True):
            translated[key] = normalize(value, locale)
    return translated


def main() -> None:
    curated = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    LOCALE_DIR.mkdir(parents=True, exist_ok=True)
    locale_names = [entry[0] for entry in LANGUAGES[1:]]
    cache = json.loads(CACHE_PATH.read_text(encoding="utf-8")) if CACHE_PATH.exists() else {}

    for locale in locale_names:
        if locale in cache and len(cache[locale].get("cases", {})) == len(curated["items"]):
            cache[locale] = polish_payload(cache[locale], locale)
            print(f"{locale}: cache hit")
            continue
        print(f"{locale}: translating")
        strings = translate_mapping(ENGLISH, locale)
        categories = translate_mapping(curated["category_names"], locale)
        cases: dict[str, dict] = {}
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = [pool.submit(translate_case, item, locale) for item in curated["items"]]
            for future in as_completed(futures):
                number, translated = future.result()
                cases[number] = translated
        cache[locale] = polish_payload({
            "locale": locale,
            "translation_method": "machine-assisted first pass with source-locked fields",
            "strings": strings,
            "categories": categories,
            "cases": dict(sorted(cases.items(), key=lambda pair: int(pair[0]))),
        }, locale)
        CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for locale in locale_names:
        destination = LOCALE_DIR / f"{locale}.json"
        destination.write_text(json.dumps(cache[locale], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
