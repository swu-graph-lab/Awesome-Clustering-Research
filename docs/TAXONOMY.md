# LLM4GM Taxonomy and Scope

## Design principle

The catalog separates the **task being solved** from the **role played by the LLM**. A single paper can therefore receive multiple task and role tags without being duplicated across unrelated taxonomies.

## Graph-mining tasks

| Tag | Include when the main evaluation contains |
| --- | --- |
| `survey` | A systematic synthesis of LLMs used for graph learning or graph mining |
| `benchmark` | A reusable dataset, testbed, or evaluation protocol for graph/LLM systems |
| `general-purpose` | Multiple graph-mining tasks or datasets under one transferable model |
| `node-classification` | Node label prediction, including zero/few-shot settings |
| `link-prediction` | Edge existence, relation, or temporal-link prediction |
| `graph-classification` | Whole-graph label or property prediction |
| `structure-learning` | Graph construction, denoising, augmentation, or topology refinement for a graph task |
| `graph-clustering` | Node clustering, community detection, or dynamic community tracking |

## LLM roles

| Tag | Definition | Typical signal |
| --- | --- | --- |
| `encoder` | Produces semantic node, edge, or graph features | Embeddings or generated explanations become model inputs |
| `annotator` | Produces labels, preferences, synthetic examples, or constraints | Pseudo-labels, rankings, triplets, or generated nodes |
| `refiner` | Reviews or corrects an intermediate graph/mining result | Edge-weight updates, cluster feedback, or topology edits |
| `predictor` | Directly returns a graph-task answer | A node label, link decision, cluster assignment, or graph property |
| `aligner` | Is trained or projected jointly with graph representations | Cross-modal projector, contrastive alignment, or joint objective |
| `agent` | Plans or coordinates multiple model/tool calls for the graph task | Multi-agent collaboration or tool-using workflow |

## Inclusion test

Include a paper when all three statements are true:

1. The input, intermediate representation, or output contains an explicit graph.
2. An LLM materially affects the proposed method rather than appearing only in discussion or baselines.
3. The evaluation includes a graph-mining task or a benchmark designed for such tasks.

## Exclusions and borderline cases

- **GraphRAG / KGQA:** exclude if the only output is a natural-language answer. Include only when the work also evaluates a graph-mining output such as node labels or links.
- **Knowledge-graph construction:** exclude by default; include only if framed and evaluated as structure or link prediction over an existing graph.
- **Graph reasoning puzzles:** keep in the benchmark section only when they materially inform graph-mining model evaluation.
- **PLM-only methods:** BERT-like encoders alone do not qualify unless the paper explicitly studies an LLM-scale model or an LLM-generated signal.
- **Clustering with LLMs:** ordinary text/image clustering is out of scope unless a graph is constructed or graph topology is part of the method/evaluation.
- **Graph foundation models without LLMs:** out of scope even if they use textual prompts.

## Status vocabulary

- `peer-reviewed`: accepted or published in a named archival venue.
- `preprint`: publicly available manuscript without a verified archival venue.
- `forthcoming`: venue claim can be verified, but the final paper page or proceedings entry is not yet public.
