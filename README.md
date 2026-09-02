# Awesome LLM4GM

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated, task-oriented map of **Large Language Models for Graph Mining (LLM4GM)**: papers, code, benchmarks, and practical reading paths.

> **Snapshot:** 2026-09-02 · **Catalog:** 30 entries · [中文说明](README_zh-CN.md)

## Scope

This list includes work where an LLM materially participates in a graph-mining pipeline, such as graph representation learning, node or edge prediction, graph structure learning, community detection, or graph clustering.

It intentionally does **not** try to cover every paper involving both graphs and language models. GraphRAG for question answering, knowledge-graph construction, graph-of-thought prompting, and methods that only use a small pretrained encoder are out of scope unless they also evaluate a graph-mining task.

## How to use this repository

- **New to the area?** Read one survey, then inspect a benchmark before choosing a method.
- **Working on graph clustering?** Jump to [Graph clustering and community detection](#graph-clustering-and-community-detection).
- **Comparing methods?** Filter the machine-readable catalog in [`data/papers.json`](data/papers.json) by task, LLM role, venue, year, or code availability.
- **Maintaining the list?** Follow [`CONTRIBUTING.md`](CONTRIBUTING.md); tables in this README are generated, not hand-edited.

## Taxonomy

We index every method on two independent axes:

1. **Graph-mining task** — what the system is evaluated on: node classification, link prediction, graph classification, structure learning, clustering/community detection, or a multi-task benchmark.
2. **LLM role** — what the LLM contributes: `encoder`, `annotator`, `refiner`, `predictor`, `aligner`, or `agent`.

This avoids mixing *what a method solves* with *how the LLM is used*. See [`docs/TAXONOMY.md`](docs/TAXONOMY.md) for definitions and borderline cases.

## Recommended reading path

1. **Map the field:** *A Survey of Large Language Models for Graphs* (KDD 2024).
2. **Check evaluation practice:** GLBench and LLMNodeBed.
3. **Learn the main integration patterns:** TAPE, GraphAdapter, GraphGPT, and LLaGA.
4. **For graph clustering:** start with GCLR, then compare MARK, MASK, and DyG-RoLLM.

## Catalog

<!-- CATALOG:START -->
### Surveys and perspectives

| Year | Venue | Paper | LLM role(s) | Code | Status | Why it matters |
| ---: | --- | --- | --- | --- | --- | --- |
| 2025 | Mathematics | [Large Language Models Meet Graph Neural Networks: A Perspective of Graph Mining](https://doi.org/10.3390/math13071147) | `encoder`, `predictor`, `aligner` | — | `peer-reviewed` | Frames the area as GNN-driving-LLM, LLM-driving-GNN, and co-driving approaches from a graph-mining perspective. |
| 2025 | arXiv | [Large Language Models Meet Text-Attributed Graphs: A Survey of Integration Frameworks and Applications](https://arxiv.org/abs/2510.21131) | `encoder`, `annotator`, `predictor`, `aligner` | — | `preprint` | Focuses on orchestration patterns and applications for LLM integration with text-attributed graphs. |
| 2024 | IJCAI | [A Survey of Graph Meets Large Language Model: Progress and Future Directions](https://arxiv.org/abs/2311.12399) | `encoder`, `annotator`, `predictor`, `aligner` | [code](https://github.com/yhLeeee/Awesome-LLMs-in-Graph-tasks) | `peer-reviewed` | Reviews representative graph–LLM architectures, training strategies, and graph-task applications. |
| 2024 | KDD | [A Survey of Large Language Models for Graphs](https://arxiv.org/abs/2405.08011) | `encoder`, `annotator`, `predictor`, `aligner` | [code](https://github.com/HKUDS/Awesome-LLM4Graph-Papers) | `peer-reviewed` | Organizes graph–LLM methods into four integration paradigms and discusses their strengths and limitations. |
| 2024 | IEEE TKDE | [Large Language Models on Graphs: A Comprehensive Survey](https://arxiv.org/abs/2312.02783) | `encoder`, `annotator`, `predictor`, `aligner` | [code](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) | `peer-reviewed` | Surveys graph-enhanced LLMs and LLM-enhanced graph learning under a unified framework. |

### Benchmarks and evaluation

| Year | Venue | Paper | LLM role(s) | Code | Status | Why it matters |
| ---: | --- | --- | --- | --- | --- | --- |
| 2025 | ICLR | [**GraphArena** — GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://arxiv.org/abs/2407.00379) | `predictor` | [code](https://github.com/squareRoot3/GraphArena) | `peer-reviewed` | Studies LLM graph-computation capability across task difficulty, prompting, and graph scale. |
| 2025 | ICLR | [How Do Large Language Models Understand Graph Patterns? A Benchmark for Graph Pattern Comprehension](https://openreview.net/forum?id=CkKEuLmRnr) | `predictor` | — | `peer-reviewed` | Evaluates graph-pattern recognition and autonomous pattern discovery by LLMs. |
| 2025 | ICML | [**LLMNodeBed** — When Do LLMs Help With Node Classification? A Comprehensive Analysis](https://openreview.net/forum?id=O3WqAhxuc7) | `encoder`, `annotator`, `predictor`, `aligner` | [code](https://github.com/WxxShirley/LLMNodeBed) | `peer-reviewed` | Compares LLM-based node classifiers across datasets, learning paradigms, homophily, model size, and prompts. |
| 2024 | NeurIPS Datasets and Benchmarks | [**ProGraph** — Can Large Language Models Analyze Graphs like Professionals? A Benchmark, Datasets and Models](https://arxiv.org/abs/2409.19667) | `agent`, `predictor` | [code](https://github.com/BUPT-GAMMA/ProGraph) | `peer-reviewed` | Evaluates tool-using LLMs on professional graph-analysis workflows and large graphs. |
| 2024 | NeurIPS Datasets and Benchmarks | [**GLBench** — GLBench: A Comprehensive Benchmark for Graph with Large Language Models](https://arxiv.org/abs/2407.07457) | `encoder`, `annotator`, `predictor`, `aligner` | [code](https://github.com/NineAbyss/GLBench) | `peer-reviewed` | Standardizes data splits and evaluation for representative LLM-based node-classification methods. |
| 2023 | NeurIPS | [**NLGraph** — Can Language Models Solve Graph Problems in Natural Language?](https://arxiv.org/abs/2305.10037) | `predictor` | [code](https://github.com/Arthur-Heng/NLGraph) | `peer-reviewed` | Benchmarks language models on graph problems expressed in natural language. |

### General-purpose graph models

| Year | Venue | Paper | LLM role(s) | Code | Status | Why it matters |
| ---: | --- | --- | --- | --- | --- | --- |
| 2026 | arXiv | [**GraspLLM** — GraspLLM: Towards Zero-Shot Generalization on Text-Attributed Graphs with LLMs](https://arxiv.org/abs/2606.11898) | `encoder`, `aligner`, `predictor` | [code](https://github.com/Heinz217/GraspLLM) | `preprint` | Combines motif-aware structural learning with LLM alignment for cross-dataset and cross-task zero-shot transfer. |
| 2025 | IEEE TPAMI | [**MuseGraph** — Graph-Oriented Instruction Tuning of Large Language Models for Generic Graph Mining](https://arxiv.org/abs/2403.04780) | `predictor`, `aligner` | — | `peer-reviewed` | Instruction-tunes one language model across node-, link-, and graph-level mining tasks. |
| 2024 | SIGIR | [**GraphGPT** — GraphGPT: Graph Instruction Tuning for Large Language Models](https://arxiv.org/abs/2310.13023) | `aligner`, `predictor` | [code](https://github.com/HKUDS/GraphGPT) | `peer-reviewed` | Aligns graph representations with an LLM through graph instruction tuning. |
| 2024 | WWW | [**GraphTranslator** — GraphTranslator: Aligning Graph Model to Large Language Model for Open-ended Tasks](https://arxiv.org/abs/2402.07197) | `aligner`, `predictor` | [code](https://github.com/alibaba/GraphTranslator) | `peer-reviewed` | Connects a pretrained graph encoder to an LLM for open-ended graph tasks. |
| 2024 | KDD | [**HiGPT** — HiGPT: Heterogeneous Graph Language Model](https://arxiv.org/abs/2402.16024) | `aligner`, `predictor` | [code](https://github.com/HKUDS/HiGPT) | `peer-reviewed` | Extends graph-language alignment and instruction tuning to heterogeneous graphs. |
| 2024 | ICML | [**LLaGA** — LLaGA: Large Language and Graph Assistant](https://arxiv.org/abs/2402.08170) | `aligner`, `predictor` | [code](https://github.com/VITA-Group/LLaGA) | `peer-reviewed` | Maps graph structures into a language-model token space for transferable graph instruction following. |
| 2024 | KDD | [**ZeroG** — ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs](https://arxiv.org/abs/2402.11235) | `encoder`, `aligner`, `predictor` | [code](https://github.com/NineAbyss/ZeroG) | `peer-reviewed` | Studies cross-dataset zero-shot transfer using language-aligned graph representations and task descriptions. |

### Node classification and structure learning

| Year | Venue | Paper | LLM role(s) | Code | Status | Why it matters |
| ---: | --- | --- | --- | --- | --- | --- |
| 2025 | WSDM | [**LOGIN** — LOGIN: A Large Language Model Consulted Graph Neural Network Training Framework](https://arxiv.org/abs/2405.13902) | `annotator`, `refiner` | [code](https://github.com/QiaoYRan/LOGIN) | `peer-reviewed` | Queries an LLM selectively during GNN training to improve labels and supervision under a limited budget. |
| 2025 | arXiv | [**GraphALP** — When Noisy Labels Meet Class Imbalance on Graphs: A Graph Augmentation Method with LLM and Pseudo Label](https://arxiv.org/abs/2507.18153) | `annotator`, `refiner` | — | `preprint` | Uses LLM-generated minority nodes and dynamic pseudo-labeling for node classification with class imbalance and noisy labels. |
| 2024 | WWW | [**GraphAdapter** — Can GNN Be Good Adapter for LLMs?](https://arxiv.org/abs/2402.12984) | `aligner`, `predictor` | [code](https://github.com/zjunet/GraphAdapter) | `peer-reviewed` | Uses a GNN as an efficient structural adapter for an LLM on text-attributed graphs. |
| 2024 | arXiv | [**GAugLLM** — GAugLLM: Improving Graph Contrastive Learning for Text-Attributed Graphs with Large Language Models](https://arxiv.org/abs/2406.11945) | `annotator`, `refiner` | [code](https://github.com/NYUSHCS/GAugLLM) | `preprint` | Uses LLM-derived semantic signals to construct graph augmentations for contrastive learning. |
| 2024 | arXiv | [**GraphEdit** — GraphEdit: Large Language Models for Graph Structure Learning](https://arxiv.org/abs/2402.15183) | `annotator`, `refiner` | [code](https://github.com/HKUDS/GraphEdit) | `preprint` | Uses LLM knowledge to edit noisy text-attributed graph structures before downstream learning. |
| 2024 | ICLR | [**TAPE** — Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://arxiv.org/abs/2305.19523) | `encoder`, `annotator` | [code](https://github.com/XiaoxinHe/TAPE) | `peer-reviewed` | Uses LLM-generated explanations as additional features for text-attributed graph learning. |

### Graph clustering and community detection

| Year | Venue | Paper | LLM role(s) | Code | Status | Why it matters |
| ---: | --- | --- | --- | --- | --- | --- |
| 2026 | CIKM | **MASK** — Minority-aware Semantic Alignment via Knowledge Enhancement for Long-tailed Graph Clustering | `annotator`, `aligner` | [code](https://github.com/fuyw-aisw/MASK) | `forthcoming` | Uses LLM knowledge to produce balanced mixed groups with emphasis on minority classes; the public paper URL was pending at snapshot time. |
| 2026 | WWW | [**DyG-RoLLM** — Node Role-Guided LLMs for Dynamic Graph Clustering](https://doi.org/10.1145/3774904.3792704) | `predictor`, `refiner` | [code](https://github.com/Clearloveyuan/DyG-RoLLM) | `peer-reviewed` | Uses semantic node-role prototypes and hierarchical LLM reasoning for interpretable dynamic graph clustering. |
| 2026 | Neurocomputing | [**UniS2A** — UniS2A: Unified Semantic and Structural Augmentation for Text-Attributed Graphs with Large Language Models](https://doi.org/10.1016/j.neucom.2026.133800) | `annotator`, `refiner` | — | `peer-reviewed` | Integrates LLM semantic reasoning with feature- and structure-level augmentation for text-attributed graphs. |
| 2025 | Findings of EMNLP | [**D2CS** — D2CS - Documents Graph Clustering using LLM supervision](https://aclanthology.org/2025.findings-emnlp.1283/) | `refiner`, `annotator` | [code](https://github.com/D2CS-sub/D2CS) | `peer-reviewed` | Iteratively updates edges in a document-similarity graph using LLM assessments of cluster coherence. |
| 2025 | Findings of ACL | [**MARK** — MARK: Multi-agent Collaboration with Ranking Guidance for Text-attributed Graph Clustering](https://aclanthology.org/2025.findings-acl.314/) | `agent`, `annotator`, `refiner` | [code](https://github.com/fuyw-aisw/MARK) | `peer-reviewed` | Coordinates concept, generation, and inference agents to create ranking supervision for uncertain nodes. |
| 2024 | LoG | [**GCLR** — Large Language Model Guided Graph Clustering](https://openreview.net/forum?id=CLyhlb5DG5) | `annotator`, `refiner` | — | `peer-reviewed` | Selectively queries an LLM for noisy feedback and uses it to refine GNN-based clustering on text-attributed graphs. |
<!-- CATALOG:END -->

### Legend

- **Status:** `peer-reviewed`, `preprint`, or `forthcoming`.
- **Code:** `—` means that no official implementation was found during the snapshot check; it does not prove that no implementation exists.
- A paper may have multiple tasks and LLM roles. The first task determines its display section, while all tags remain available in the JSON catalog.

## Related collections

- [Awesome-LLMs-for-Clustering](https://github.com/Marigoldwu/Awesome-LLMs-for-Clustering) — broad LLM-for-clustering coverage across text, vision, and graphs.
- [Awesome Deep Graph Clustering](https://github.com/yueliu1999/Awesome-Deep-Graph-Clustering) — deep graph clustering methods, datasets, and surveys.
- [PyAGC](https://github.com/Cloudy1225/PyAGC) — attributed graph clustering library, benchmark, and ECO taxonomy.
- [Awesome Graph LLM](https://github.com/XiaoxinHe/Awesome-Graph-LLM) — broad graph/LLM collection, including GraphRAG and reasoning.
- [Awesome LLM4Graph Papers](https://github.com/HKUDS/Awesome-LLM4Graph-Papers) — integration-oriented taxonomy accompanying the KDD 2024 survey.
- [MASK](https://github.com/fuyw-aisw/MASK) — LLM-enhanced long-tailed graph clustering implementation.

These repositories were used as discovery sources. Metadata in this catalog was restructured around graph-mining tasks and checked against paper/project pages rather than copied wholesale.

## Quality policy

- Prefer stable paper pages (publisher, OpenReview, ACL Anthology, or arXiv abstract) over direct PDF links.
- Mark preprints and forthcoming papers explicitly; do not silently upgrade venue claims.
- Link only official or author-maintained code when it can be identified.
- Keep one canonical record per paper and record all applicable tags in that record.
- Re-check title, venue, year, paper URL, and code URL before merging a contribution.

## Contributing

Add or update records in [`data/papers.json`](data/papers.json), then run:

```bash
python scripts/validate_catalog.py
python scripts/build_catalog.py
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the inclusion checklist and pull-request format.

## License

Released under the [MIT License](LICENSE). Paper titles and bibliographic facts remain attributable to their respective authors and publishers.
