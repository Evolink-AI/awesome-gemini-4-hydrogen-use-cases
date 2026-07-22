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
7. Record the update in `docs/update-log.md`

Never treat a generated README as the source of truth and never infer a successful remote publication from a local-only audit
