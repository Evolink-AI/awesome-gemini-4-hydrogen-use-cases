# Contributing

Thanks for helping improve this source-backed Gemini 4 Hydrogen collection

## Propose a case

Open a case proposal issue and provide:

- A public source URL
- The creator's public handle
- A concise description of what the evidence shows
- The original prompt only when it appears verbatim in the public source
- Direct source media URLs when available

We prioritize observable workflows, builds, evaluations, and limits over announcements or unsupported claims

## Corrections

Use the correction issue template for attribution, translation, broken-link, or factual corrections and attach a public source

## Pull requests

- Keep source URLs and author attribution intact
- Do not reconstruct missing prompts
- Do not commit downloaded media; public media is served from the repository's R2 namespace
- Use Python 3.12. Run `python3 scripts/build_readmes.py --check`, `python3 scripts/verify_repository.py`, and `python3 -m unittest discover -s tests -v` before opening a pull request
- Treat `data/source-inventory.json` as the independently reviewed source lock. An intentional source update must update its reviewed inventory hash and regression fixtures, not only generated counts
- Keep all 11 README variants structurally aligned

By contributing, you agree that your contribution is licensed under CC BY 4.0
