#!/usr/bin/env python3
"""Download source-backed media and bind it to the repository R2 namespace"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
R2_ROOT = (
    "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/"
    "model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases"
)


def unique(urls: list[str]) -> list[str]:
    return list(dict.fromkeys(url for url in urls if isinstance(url, str) and url.startswith("http")))


def resolution(url: str) -> tuple[int, int]:
    match = re.search(r"/(\d+)x(\d+)/", url)
    return (int(match.group(1)), int(match.group(2))) if match else (0, 0)


def select_video(urls: list[str]) -> str:
    variants = [url for url in urls if "video.twimg.com/" in url and ".mp4" in url]
    if not variants:
        raise ValueError("video item has no direct MP4 variant")
    practical = [url for url in variants if max(resolution(url)) <= 1280]
    candidates = practical or variants
    return max(candidates, key=lambda value: resolution(value)[0] * resolution(value)[1])


def extension(url: str) -> str:
    suffix = Path(urlparse(url).path).suffix.lower()
    return ".jpg" if suffix in {"", ".jpeg"} else suffix


def valid_image(path: Path) -> bool:
    head = path.read_bytes()[:16]
    return head.startswith(b"\xff\xd8\xff") or head.startswith(b"\x89PNG\r\n\x1a\n") or head.startswith((b"GIF87a", b"GIF89a")) or (head.startswith(b"RIFF") and head[8:12] == b"WEBP")


def valid_video(path: Path) -> bool:
    head = path.read_bytes()[:32]
    return len(head) >= 12 and head[4:8] == b"ftyp"


def download(url: str, target: Path, *, video: bool = False) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    validator = valid_video if video else valid_image
    minimum = 10_000 if video else 1_000
    if target.is_file() and target.stat().st_size >= minimum and validator(target):
        return target
    partial = target.with_suffix(target.suffix + ".part")
    result = subprocess.run([
        "curl", "--location", "--fail", "--silent", "--show-error",
        "--retry", "5", "--retry-all-errors", "--retry-delay", "1",
        "--output", str(partial), url,
    ], check=False)
    if result.returncode or not partial.exists() or partial.stat().st_size < minimum or not validator(partial):
        partial.unlink(missing_ok=True)
        raise ValueError(f"invalid download: {url}")
    partial.replace(target)
    return target


def r2(path: Path) -> str:
    return f"{R2_ROOT}/{path.relative_to(ROOT).as_posix()}"


def main() -> None:
    data_path = ROOT / "data/use-cases.json"
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    downloaded: list[Path] = []
    for item in payload["items"]:
        number = item["public_number"]
        nn = f"{number:02d}"
        urls = unique(item.pop("source_media_raw", []))
        posters = [url for url in urls if "pbs.twimg.com/" in url and "video_thumb" in url]
        images = [url for url in urls if "pbs.twimg.com/media/" in url]
        videos = [url for url in urls if "video.twimg.com/" in url and ".mp4" in url]
        assets = []
        source_urls = []
        if videos:
            if not posters:
                raise ValueError(f"case {number} has a video but no poster")
            selected_video = select_video(videos)
            poster = download(posters[0], ROOT / "media/source-cases" / f"case-{nn}-poster.jpg")
            video = download(selected_video, ROOT / "media/source-cases" / f"case-{nn}.mp4", video=True)
            downloaded.extend([poster, video])
            assets.append({
                "kind": "video",
                "poster_url": r2(poster),
                "url": r2(video),
                "play_label": f"Play case {number} source video",
            })
            source_urls.append(selected_video)
        for index, url in enumerate(images, start=1):
            path = download(url, ROOT / "media/source-cases" / f"case-{nn}-{index:02d}{extension(url)}")
            downloaded.append(path)
            assets.append({"kind": "image", "url": r2(path)})
            source_urls.append(url)
        if not assets:
            raise ValueError(f"case {number} has no usable media")
        item["media_type"] = "video" if videos else "image"
        item["media_assets"] = assets
        item["media_source_urls"] = source_urls
    data_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"cases={len(payload['items'])}")
    print(f"video_cases={sum(item['media_type'] == 'video' for item in payload['items'])}")
    print(f"image_cases={sum(item['media_type'] == 'image' for item in payload['items'])}")
    print(f"visual_assets={sum(len(item['media_assets']) for item in payload['items'])}")
    print(f"downloaded_files={len(downloaded)}")


if __name__ == "__main__":
    main()
