#!/usr/bin/env python3
"""Build the reviewed Gemini 3.6 Flash public use-case dataset from the owner source package"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Every record is a source-grounded editorial boundary, keyed by the immutable X post id
EDITORIAL = {
    "2079591562145870043": ("efficiency-agents", "Token Efficiency Side by Side", "Compare output-token use on the same workflow before choosing a Flash model for agent-scale workloads", "Jeff Dean shared a side-by-side demonstration comparing Gemini 3.6 Flash with 3.5 Flash and highlighted lower token use in the newer model", "Evaluation"),
    "2079663375991046351": ("efficiency-agents", "Modernizing Legacy Code in Antigravity", "Use a controlled legacy-code migration task to compare agent latency, edit quality, and completion behavior", "Google Antigravity demonstrated both Flash generations rebuilding legacy software and reported faster completion with improved latency and output from Gemini 3.6 Flash", "Evaluation"),
    "2079599477216956437": ("efficiency-agents", "Canvas Token Efficiency Test", "Run the same Canvas task across model versions and inspect both the artifact and token usage", "The creator compared Gemini 3.6 Flash and 3.5 Flash on a short Canvas task and observed substantially lower token usage from 3.6 Flash", "Evaluation"),
    "2079602472516264010": ("efficiency-agents", "Browser Agent Benchmark", "Benchmark browser-agent success and cost together instead of optimizing either metric alone", "Browser Use reported 68% on its BU Benchmark for Gemini 3.6 Flash, compared with 67% for GPT-5.6 Sol, 62% for Sonnet 4.6, and 74% for Opus 4.8", "Benchmark"),
    "2079603658141184134": ("efficiency-agents", "Long-Tail Fact Retrieval Efficiency", "Use difficult fact-retrieval tasks to compare reasoning steps and thought-token overhead", "The creator ran Gemini 3.5 and 3.6 Flash head to head on a complex long-tail fact retrieval task and reported half as many steps and 75% fewer thought tokens for 3.6 Flash", "Evaluation"),
    "2079598684455551326": ("efficiency-agents", "Enterprise Document Processing", "Evaluate reasoning effort on long patents and document parsing before setting a production default", "Databricks reported higher document-classification accuracy than 3.5 Flash, strong results on long patents, and about 32% fewer total tokens at medium effort than high effort for document parsing", "Benchmark"),
    "2079618218587574636": ("efficiency-agents", "Engineering Task Evaluation in JetBrains", "Build an objective engineering task and compare model generations inside the same IDE workflow", "JetBrains presented an objective engineering-task evaluation for Gemini 3.6 Flash versus the previous Flash generation in AI Assistant and Junie", "Evaluation"),
    "2079607995861021073": ("efficiency-agents", "Multi-Agent Code Migration", "Test code migration with the same orchestration plan and compare latency, edits, and final quality", "The demonstration shows Gemini 3.6 Flash executing a code migration through multi-agent orchestration in Antigravity and reports lower latency and higher quality than 3.5 Flash", "Demo"),
    "2079675781794443640": ("coding-apps", "Android Guitar Tuner", "Prototype a focused mobile utility that combines conventional audio tooling with AI-assisted alternate tunings", "The creator used Gemini 3.6 Flash to build an Android guitar-tuner application with AI-driven alternate tuning support", "Demo"),
    "2079588206513631483": ("coding-apps", "Traffic-Light Simulation", "Ask the model for an executable visualization to inspect whether generated code captures timing and random traffic behavior", "The public prompt requests Python code that visualizes a one-way-street traffic light with cars arriving at random rates, and the post includes the resulting demonstration", "Demo"),
    "2079734240540041230": ("coding-apps", "Keyboard Piano App", "Turn a simple interaction concept into a playable keyboard-controlled web application", "The creator built a piano application with Gemini 3.6 Flash that can be played from a computer keyboard and framed it as an app children could explore", "Demo"),
    "2079716688745132044": ("coding-apps", "Desktop Robot Voice Assistant", "Integrate both Flash and Flash-Lite into a voice application and compare first-response behavior", "The creator added Gemini 3.6 Flash and Gemini 3.5 Flash-Lite to a voice-dialog application for a desktop robot and noted that the initial response felt slightly slow but usable", "Integration"),
    "2079597030922465407": ("web-games-3d", "Golden Gate Bridge HTML Failure", "Use a strict file-delivery task to test instruction following before trusting generated 3D web experiences", "The tester needed three prompts, saw the model attempt an in-app simulation and web-image responses instead of the requested HTML file, and judged the final 3D bridge output materially weaker than Gemini 3.1 Pro", "Limit"),
    "2079592671530938537": ("web-games-3d", "Public Prompt Visual Test", "Open the source thread when you need the creator's full prompt instead of reconstructing it from the output", "MotionViz published a Gemini 3.6 Flash visual test with media and indicated that the full prompt is available in the source thread; this repository does not reconstruct prompt text not present in the source package", "Demo"),
    "2079599565565468672": ("web-games-3d", "Single-Prompt Canvas Game", "Use one prompt in Canvas to test how quickly the model can turn a compact game concept into an interactive result", "The creator tested Gemini 3.6 Flash in early access and used a single Canvas prompt to produce a playable game demonstration", "Demo"),
    "2079596099854307650": ("web-games-3d", "Landing Page Version Comparison", "Keep the prompt fixed across model generations to isolate changes in landing-page execution and visual judgment", "The creator added Gemini 3.6 Flash to a same-prompt landing-page archive and judged the newer result worse than the Gemini 3 and 3.5 outputs", "Evaluation"),
    "2079597536155668890": ("web-games-3d", "Subway Surfers 3D Prototype", "Enable extended thinking for coding experiments and inspect both interaction quality and visual fidelity", "The creator used Gemini 3.6 Flash to build a simple 3D Subway Surfers-style replica and recommended extended thinking for coding tasks", "Demo"),
    "2079606113306325496": ("web-games-3d", "One-Page Website Comparison", "Hold the website prompt and reasoning level constant, then compare token cost, speed, and design preference", "On the same one-page website prompt, the creator reported about 6,100 tokens for Gemini 3.6 Flash versus about 9,300 for 3.5 Flash, while personally preferring the older model's look", "Evaluation"),
    "2079635008424169901": ("web-games-3d", "Wild West Game Failure", "Treat failed game-generation outputs as evidence for deciding when to switch models or revise the task", "The tester used a Wild West game-generation prompt and judged Gemini 3.6 Flash materially behind GPT-5.6, Kimi K3, and Fable 5 on the observed result", "Limit"),
    "2079592731211399460": ("web-games-3d", "Antigravity Game Material Failure", "Check both visual materials and actual interaction behavior before accepting an AI-generated game prototype", "In a second Antigravity game test, the creator found weaker wood textures and a marble element that looked similar but remained nonfunctional", "Limit"),
    "2079610251444437335": ("web-games-3d", "Rolls-Royce SVG Comparison", "Use a fixed SVG subject to compare how two Flash generations handle shape, detail, and composition", "The post places Gemini 3.6 Flash and 3.5 Flash outputs side by side for the same Rolls-Royce SVG task", "Evaluation"),
    "2079681107516170431": ("web-games-3d", "Realistic Aquarium Test", "Use a bounded 3D scene to compare realism and implementation quality across model versions", "The creator asked Gemini 3.6 Flash to build a realistic aquarium and judged it only marginally better than 3.5 Flash", "Evaluation"),
    "2079609162431181193": ("evaluations", "Gemini Versus Grok at Max Reasoning", "Use the same prompt and maximum reasoning settings to compare speed, cost, and output rather than relying on model reputation", "The creator ran Gemini 3.6 Flash and Grok 4.5 under the same prompt and maximum reasoning settings, observing that both were fast while Grok was slightly faster and cheaper", "Evaluation"),
    "2079617706693902416": ("evaluations", "Gemini Versus Sonnet at Max Settings", "Compare models on identical prompts and their strongest settings, then inspect the actual generated artifact", "The creator tested Gemini 3.6 Flash and Sonnet 5 with the same prompts at maximum settings and preferred the Gemini output in the shown task", "Evaluation"),
    "2079607042403381313": ("evaluations", "Visual Understanding Test", "Use a concrete image task to inspect response quality and interaction style before adopting the model for vision workflows", "The creator presented a vision test that Gemini 3.6 Flash passed and highlighted the response personality as part of the observed experience", "Demo"),
    "2079712480683790743": ("evaluations", "Rocket League Game Benchmark", "Run a repeated game-generation benchmark and record both build time and a consistent subjective ranking", "The creator tested Gemini 3.6 Flash on a Rocket League-style task, ranked it third on a personal leaderboard, and reported completion in under two minutes", "Benchmark"),
    "2079631807817933222": ("evaluations", "EyeBench Visual Comparison", "Use a stable visual benchmark to separate incremental efficiency gains from absolute quality", "On EyeBench, the creator judged Gemini 3.6 Flash marginally better than 3.5 Flash but still worse than Gemini 3.1 Pro Preview, while noting improved token efficiency", "Benchmark"),
    "2079603778441957776": ("evaluations", "Paper-Cut Animation Comparison", "Compare response speed and the final animation separately when evaluating creative generation", "The creator compared Gemini 3.6 Flash with Fable 5 on a paper-cut animation task, praising Gemini's near-immediate response but expressing reservations about the result", "Evaluation"),
    "2079663080049660220": ("evaluations", "AI Arena Generation Benchmark", "Use the same arena task to compare build time, price, and artifact quality across multiple coding models", "The creator tested Grok 4.5, Gemini 3.6 Flash, and GPT-5.6 Luna on one AI Arena task and judged the Gemini result weakest in that run", "Benchmark"),
    "2079710299918401907": ("evaluations", "Cross-Model Game Build Cost", "Track iteration count, developer experience, features, and cost together when choosing a model for game prototyping", "Using the same design workflow, the creator reported needing six to seven iterations to fix a Gemini-generated jump-and-fall bug and listed a $0.15 run cost alongside comparative scores", "Benchmark"),
    "2079602157779566836": ("safety-limits", "Cybersecurity Refusal Benchmark", "Include refusal behavior in security-tool evaluations because defensive code review may be blocked with offensive requests", "A cybersecurity benchmark run was refused, leading the evaluator to report that the tested policy blocked vulnerability-finding behavior for defensive code as well as malicious use", "Limit"),
    "2079587359851737339": ("safety-limits", "Knowledge Freshness Failure", "Verify current facts with retrieval instead of trusting a claimed knowledge cutoff", "The tester asked for current flagship models and received older names, then reported that the model acknowledged knowledge current only to early 2025 despite claiming a March 2026 cutoff", "Limit"),
    "2079711268899086484": ("safety-limits", "Jailbreak Red-Team Test", "Treat jailbreak claims as red-team signals that require controlled reproduction and safety review, not as reusable instructions", "The post claims a jailbreak across the Gemini App and API and lists harmful-content categories tested; this repository records the safety signal without reproducing exploit instructions", "Limit"),
}

CATEGORY_ORDER = ["efficiency-agents", "coding-apps", "web-games-3d", "evaluations", "safety-limits"]
CATEGORY_NAMES = {
    "efficiency-agents": "Efficiency & Agents",
    "coding-apps": "Coding & Apps",
    "web-games-3d": "Web, Games & 3D",
    "evaluations": "Evaluation & Comparisons",
    "safety-limits": "Safety & Limits",
}
PROMPTS = {
    "2079588206513631483": "write a python code that visualizes how a traffic light works in a one way street with cars entering at random rate.",
    "2079606113306325496": "create a modern website! Should look amazing! One-code page",
    "2079610251444437335": "SVG of a Rolls Royce",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = json.loads(args.source.read_text(encoding="utf-8"))
    source_items = payload["items"]
    by_id = {str(item["id"]): item for item in source_items}
    if set(by_id) != set(EDITORIAL):
        raise SystemExit(f"editorial/source mismatch: source={len(by_id)} editorial={len(EDITORIAL)}")

    ordered_ids = [
        item_id
        for category in CATEGORY_ORDER
        for item_id, editorial in EDITORIAL.items()
        if editorial[0] == category
    ]
    items = []
    for number, item_id in enumerate(ordered_ids, start=1):
        raw = by_id[item_id]
        category_key, title, takeaway, notes, case_type = EDITORIAL[item_id]
        author = raw["author"]
        prompt = PROMPTS.get(item_id, "")
        items.append({
            "public_number": number,
            "id": item_id,
            "dedup_key": raw["url"],
            "source_url": raw["url"],
            "author_handle": "@" + author["username"],
            "author_url": "https://x.com/" + author["username"],
            "author_name": author["name"],
            "title": title,
            "takeaway": takeaway + ".",
            "body_notes": notes + ".",
            "type": case_type,
            "date": raw["created_at_iso"][:10],
            "category_key": category_key,
            "category": CATEGORY_NAMES[category_key],
            "decision": "high_confidence_update",
            "decision_reason": raw["use_case"]["evidence"],
            "quality_tier": "high",
            "prompt_boundary": "exact-public-text" if prompt else "not-present-in-source-package",
            "prompt_public": bool(prompt),
            "prompt_text": prompt,
            "source_text": raw["text"],
            "source_media_raw": raw["media"],
            "media_type": None,
            "media_assets": [],
            "media_source_urls": [],
        })
    output = {
        "schema_version": 1,
        "source_artifact": str(args.source.resolve()),
        "source_created_at": payload["metadata"]["created_at"],
        "selected_case_count": len(items),
        "category_order": CATEGORY_ORDER,
        "category_names": CATEGORY_NAMES,
        "items": items,
    }
    destination = ROOT / "data/use-cases.json"
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"cases={len(items)}")
    print(f"output={destination}")


if __name__ == "__main__":
    main()
