# Contributing to Awesome LLM4GM

Thank you for helping keep the list accurate and useful.

## Before adding a paper

Confirm that the work passes the inclusion test in [`docs/TAXONOMY.md`](docs/TAXONOMY.md). In particular, a paper that merely mentions graphs and LLMs is not enough: the LLM must materially participate in a graph-mining method or benchmark.

## Add or update a record

1. Edit `data/papers.json`; do not hand-edit generated tables in `README.md`.
2. Use the paper's exact title and a stable abstract/landing page when possible.
3. Link only official or author-maintained code. Leave `code` as an empty string when uncertain.
4. Use all applicable `tasks` and `roles`, with the primary display task first.
5. Add a short factual `note` describing the method's contribution, not a promotional claim.
6. Run:

```bash
python scripts/validate_catalog.py
python scripts/build_catalog.py
```

## Pull-request checklist

- [ ] The entry is in scope.
- [ ] Title, year, venue, and publication status were checked against a paper or publisher page.
- [ ] Paper and code URLs are canonical and do not use tracking parameters.
- [ ] The record is not a duplicate.
- [ ] The note is one neutral sentence.
- [ ] Validation passes and the generated README is committed.

One paper per pull request is preferred because it makes metadata review and contributor attribution clear.
