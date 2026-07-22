#!/usr/bin/env python3
"""Build the pre-mutation source-fidelity manifest and handoff package"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OWNER_PRESENTATION = {
    "menu_layout": "centralized-single-table",
    "acknowledge_layout": "inline-comma",
    "quick_start_position": "penultimate-section",
    "media_policy": "all-source-media",
    "video_playback_policy": "r2-playable",
    "localization_fallback": "english",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=ROOT / "data/source-fidelity-manifest.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = args.source.expanduser().resolve()
    source_payload = json.loads(source.read_text(encoding="utf-8"))
    source_urls = {item["url"] for item in source_payload["items"]}
    curated = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    items = curated["items"]
    if source_urls != {item["source_url"] for item in items}:
        raise ValueError("source package and selected public set differ")
    source_hash = sha256(source)
    selected = []
    manifest_cases = []
    expected_total = 0
    for item in items:
        assets = item["media_assets"]
        lineage = item["media_source_urls"]
        if item["media_type"] == "video":
            videos = [asset for asset in assets if asset["kind"] == "video"]
            images = [asset for asset in assets if asset["kind"] == "image"]
            if len(videos) != 1:
                raise ValueError(f"case {item['public_number']} video asset mismatch")
            expected_urls = [videos[0]["poster_url"], *[asset["url"] for asset in images]]
            disposition = "r2-video"
            media_fields = {
                "poster_url": videos[0]["poster_url"],
                "playable_video_url": videos[0]["url"],
                "r2_media_urls": [asset["url"] for asset in images],
            }
        else:
            expected_urls = [asset["url"] for asset in assets]
            disposition = "r2-image"
            media_fields = {"r2_media_urls": expected_urls}
        if len(lineage) != len(expected_urls):
            raise ValueError(f"case {item['public_number']} source/visual denominator mismatch")
        expected_total += len(expected_urls)
        selected.append({
            "source_url": item["source_url"],
            "author_handle": item["author_handle"],
            "author_url": item["author_url"],
            "title": item["title"],
            "takeaway": item["takeaway"],
            "body_notes": item["body_notes"],
            "type": item["type"],
            "date": item["date"],
            "category": item["category"],
            "decision": item["decision"],
            "decision_reason": item["decision_reason"],
            "dedup_key": item["dedup_key"],
            "prompt_boundary": item["prompt_boundary"],
            "media_type": item["media_type"],
            "source_media_urls": lineage,
            "source_media_count": len(lineage),
            "public_media_disposition": disposition,
            "expected_public_visual_count": len(expected_urls),
            "public_number": item["public_number"],
            **media_fields,
        })
        manifest_case = {
            "public_number": item["public_number"],
            "source_url": item["source_url"],
            "source_media_urls": lineage,
            "public_media_disposition": disposition,
            "expected_public_media_urls": expected_urls,
        }
        if item["media_type"] == "video":
            manifest_case["playable_video_url"] = media_fields["playable_video_url"]
        manifest_cases.append(manifest_case)
    manifest = {
        "schema_version": 1,
        "source_artifact": str(source),
        "source_manifest_sha256": source_hash,
        "selected_case_count": len(selected),
        "cases_with_source_media": len(selected),
        "expected_public_visual_count": expected_total,
        "media_policy": "all-source-media",
        "owner_presentation": OWNER_PRESENTATION,
        "cases": manifest_cases,
    }
    package = {
        "run_id": "gemini-3-6-flash-first-publication-2026-07-22",
        "run_mode": "first-publication",
        "repo": str(ROOT),
        "source_package": str(source),
        "source_index_policy": "data/use-cases.json is the canonical public index",
        "case_namespace": {
            "name": "Gemini 3.6 Flash public use cases",
            "heading_prefix": "Case",
            "anchor_prefix": "case",
            "section_anchor": "use-cases",
            "numbering_policy": "global-contiguous",
            "menu_policy": "centralized-single-table",
            "existing_count": 0,
            "intended_count": len(selected),
        },
        "collector_evidence": {
            "requested_repository_count": 1,
            "resolved_repository_count": 1,
            "executed_repository_count": 1,
            "skipped_repository_count": 0,
            "fixed_collected_at": source_payload["metadata"]["created_at"],
        },
        "counts": {
            "within_24_hours": len(selected),
            "high_confidence_update": len(selected),
            "deferred": 0,
            "unsure": 0,
            "drop": 0,
        },
        "source_fidelity_manifest": {
            "source_manifest_sha256": source_hash,
            "selected_case_count": len(selected),
            "cases_with_source_media": len(selected),
            "expected_public_visual_count": expected_total,
            "media_policy": "all-source-media",
        },
        "owner_presentation": OWNER_PRESENTATION,
        "selected_cases": selected,
        "deferred_cases": [],
        "unsure_cases": [],
        "dropped_cases": [],
    }
    args.package.parent.mkdir(parents=True, exist_ok=True)
    args.package.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"selected_cases={len(selected)}")
    print(f"expected_public_media={expected_total}")
    print(f"source_manifest_sha256={source_hash}")


if __name__ == "__main__":
    main()
