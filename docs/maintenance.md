# Maintenance

## Source of truth

- `data/use-cases.json` contains the reviewed public copy and original-to-hosted media mapping
- `data/source-inventory.json` freezes the independently reviewed source identities, attribution, prompt boundaries, and source-media set
- `data/source-fidelity-manifest.json` connects that inventory to the expected public visuals and playable videos
- `data/localizations/*.json` contains translated copy; `data/localization-cache.json` must match those files
- `scripts/build_readmes.py` renders the English and ten localized README files deterministically

The source inventory hash is pinned in the verifier. A deliberate collection update requires a fresh source review and a matching lock update. Changing generated counts alone must never make missing source material pass validation.

All 11 README editions use the same R2-hosted Hydrogen cover. Link and render audits include that cover.

## Update flow

Use Python 3.12.

1. Review public candidates and exclude unsupported claims. Preserve source caveats, affiliation, evaluation settings, and the limits of media review
2. Add accepted cases to the canonical data. Keep existing public case numbers stable within the Hydrogen edition. The November 2026 model migration is recorded in the update log
3. Include a reproduction prompt only when the public source contains it verbatim. Do not turn a task description into an invented prompt
4. Preserve every selected original image, video, and source poster. Upload media to an isolated versioned R2 namespace and verify public bytes and playable video metadata
5. Update the independent source inventory, fidelity manifest, ingested IDs, translations, and reviewed inventory lock together
6. Render and check all README files:

```bash
python3 scripts/build_readmes.py
python3 scripts/build_readmes.py --check
python3 scripts/verify_repository.py
python3 -m unittest discover -s tests -v
```

7. Run link and media checks with reports outside the repository:

```bash
python3 scripts/audit_public_links.py --report /path/to/evidence/public-link-audit.md
python3 scripts/audit_r2_source_media.py --report /path/to/evidence/media-audit.md
```

8. Inspect desktop and narrow-screen renders, record changes in `docs/update-log.md`, and open a reviewable pull request

Keep raw research exports, local machine paths, downloaded source media, credentials, and internal audit reports out of commits. Do not claim functional testing or a successful API call merely because a URL or source video loads. Report blocked checks rather than silently passing them.

## README model links

Every EvoLink README link points to the Gemini 4 Hydrogen model detail page. The model page provides access to API keys and the Gemini Native API documentation. The README continues to show the runnable API request directly.

Use the placement-specific UTM values defined in `scripts/build_readmes.py`. The validator checks the model destination and attribution for all eight placements in each language. Keep the native API endpoint free of UTM parameters.

The current repository slug identifies Hydrogen. The November 13 edition still references its original versioned R2 paths. Later updates use their own versioned paths.
