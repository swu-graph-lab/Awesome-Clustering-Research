# Contributing

Thank you for helping maintain the group reading map.

## Inclusion checklist

Before adding a paper, confirm that:

- clustering is a central task or contribution;
- at least one of `BIO`, `HG`, or `LLM` applies under `docs/TAXONOMY.md`;
- the title, authors, year, venue, and publication status match a primary paper page;
- the code link is official or author-maintained;
- the paper is not already present under a different title or preprint version.

## Add a record

Edit `data/papers.json`. Preserve reverse chronological year order and the field order shown in existing records. For multiple tags, use canonical order: `BIO`, `HG`, `LLM`.

Use a short note that explains why the paper belongs in this repository. Do not paste an abstract.

Then run:

```bash
python scripts/validate_catalog.py
python scripts/build_catalog.py
python scripts/check_links.py
```

Commit the canonical data and generated `README.md` and `docs/papers.json` together.

## Pull request checklist

- [ ] I checked the metadata against a publisher, anthology, OpenReview, CVF, or arXiv page.
- [ ] I used all applicable tags and followed canonical tag order.
- [ ] I linked only official or author-maintained code.
- [ ] I ran validation, generation, and link checks.
- [ ] I did not edit the generated publication list by hand.
