# Tag taxonomy

The catalog uses three independent topic tags. Assign every tag whose definition is materially satisfied; do not choose only one “primary” topic.

## `BIO` — Biological clustering

Use `BIO` when clustering biological or medical entities is a central evaluated task. Examples include cells, genes, patients, spatial domains, molecular profiles, and multi-omics samples.

Do not use it merely because a generic clustering method is evaluated on one biological dataset without biological motivation or analysis.

## `HG` — Hypergraph clustering

Use `HG` when a hypergraph is central to the clustering representation, objective, algorithm, or theoretical analysis.

Do not use it for ordinary graph clustering, heterogeneous graphs, or higher-order language unless the method actually defines or optimizes a hypergraph.

## `LLM` — LLM-enhanced clustering

Use `LLM` when a generative large language model materially contributes to the clustering pipeline through representations, supervision, pairwise constraints, feedback, reasoning, explanations, or agent actions.

Do not use it for methods that only employ a small pretrained encoder such as BERT, use “language model” as historical terminology, or ask an LLM to describe results after clustering is complete.

## Intersections

Tags follow the fixed order `BIO`, `HG`, `LLM`:

- `[BIO+HG]`: hypergraph-based clustering for biological or medical data.
- `[BIO+LLM]`: LLM-enhanced biological or medical clustering.
- `[HG+LLM]`: LLM-enhanced hypergraph clustering.
- `[BIO+HG+LLM]`: all three definitions are materially satisfied.

## Ordering and status

- Store papers in reverse chronological order by publication year.
- Within a year, editorial order is allowed; the generated views preserve the source order.
- `peer-reviewed` means the paper is published in a peer-reviewed venue.
- `preprint` means only a public manuscript is confirmed.
- `forthcoming` is reserved for a confirmed venue claim without a public paper page.
