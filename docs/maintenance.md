# Maintenance

## Source of truth

`data/use-cases.json` is the reviewed content source and `data/source-fidelity-manifest.json` records immutable source identifiers, prompt boundaries, and media expectations

## Update flow

1. Review new public candidates and exclude hype-only or unsupported claims
2. Add accepted cases to the structured data without changing existing public numbers
3. Preserve prompts only when the public source contains them verbatim
4. Upload source media to the repository's isolated R2 namespace
5. Regenerate all README files with `python3 scripts/build_readmes.py`
6. Run `python3 scripts/verify_repository.py`
7. Run `python3 scripts/audit_public_links.py --report .codex/audits/public-link-audit.md`
8. Record the update in `docs/update-log.md`

## Documentation locale routing

The README-to-documentation mapping is maintained in `scripts/build_readmes.py` and enforced by `scripts/verify_repository.py`

- Native documentation: English → `en`, Spanish → `es`, Japanese → `ja`, Korean → `ko`, German → `de`, French → `fr`, Simplified Chinese → `cn`
- Explicit English fallback: Portuguese, Turkish, Traditional Chinese, and Russian
- Every fallback README must identify the English destination in both the documentation badge and visible link copy

Do not infer a localized documentation route from a README locale. Confirm that the page has a matching canonical URL and localized title; an HTTP 200 alone is not sufficient because documentation sites can return soft-not-found pages

Never treat a generated README as the source of truth and never infer a successful remote publication from a local-only audit
