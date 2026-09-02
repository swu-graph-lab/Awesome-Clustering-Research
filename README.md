# Awesome Clustering Research

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated, cross-disciplinary reading map for **biological clustering**, **hypergraph clustering**, and **LLM-enhanced clustering**.

> **Snapshot:** 2026-09-02 · **Catalog:** 51 papers · [中文说明](README_zh-CN.md)

## Topics and tags

| Tag | Topic | Inclusion rule |
| --- | --- | --- |
| `BIO` | Biological clustering | Clustering biological or medical data is a central task, such as single-cell, spatial transcriptomics, multi-omics, or clinical phenotyping. |
| `HG` | Hypergraph clustering | Hypergraphs are central to the clustering formulation, representation, objective, or algorithm. |
| `LLM` | LLM-enhanced clustering | A generative large language model materially supplies representations, supervision, feedback, reasoning, or explanations for clustering. |

Tags are intentionally multi-label. For example, `[BIO+HG]` denotes biological clustering with a hypergraph method, while `[BIO+LLM]` denotes biological clustering enhanced by an LLM. See [the taxonomy](docs/TAXONOMY.md) for boundary cases.

## Browse the collection

- Open the [live filterable publications page](https://liangqi-l.github.io/Awesome-Clustering-Research/), or serve `docs/` locally when developing the site.
- Filter the canonical [machine-readable catalog](data/papers.json) by year, tag, venue, or code availability.
- Papers below are grouped by year in reverse chronological order. Topic is expressed by tags rather than mutually exclusive sections.

## Publications

<!-- CATALOG:START -->
### 2026

- `[BIO+LLM]` [**scLLM-DSC: A Dual-level Contrastive Framework with Large Language Models for Single-cell RNA-seq Clustering**](https://arxiv.org/abs/2606.13007) — Ping Xu, Pengjiang Li, Tian Du, Zaitian Wang, Jiawei Gu, Zhiyuan Ning, Ziyue Qiao, Pengfei Wang, and Yuanchun Zhou. *arXiv*. [Paper](https://arxiv.org/abs/2606.13007)
- `[HG]` [**CAHC** — From Representation to Clusters: A Contrastive Learning Approach for Attributed Hypergraph Clustering](https://arxiv.org/abs/2603.09370) — Li Ni, Shuaikang Zeng, Lin Mu, and Longlong Lin. *WWW*. [Paper](https://arxiv.org/abs/2603.09370) · [Code](https://github.com/nilics/CAHC)
- `[LLM]` **MASK** — Minority-aware Semantic Alignment via Knowledge Enhancement for Long-tailed Graph Clustering — Yiwei Fu, Chunchun Chen, Yuxing Zhang, Weizhi Zhang, Guanjie Zheng, Wei Ye, Xiao Luo, Philip S. Yu, and Minghua Deng. *CIKM*. [Code](https://github.com/fuyw-aisw/MASK)
- `[LLM]` [**DyG-RoLLM** — Node Role-Guided LLMs for Dynamic Graph Clustering](https://doi.org/10.1145/3774904.3792704) — Dongyuan Li, Ying Zhang, Yaozu Wu, and Renhe Jiang. *WWW*. [Paper](https://doi.org/10.1145/3774904.3792704) · [Code](https://github.com/Clearloveyuan/DyG-RoLLM)
- `[BIO]` [**scMUSCLE: Multi-scale Subspace Contrastive Learning for Single-cell RNA-seq Data Clustering**](https://doi.org/10.1093/bib/bbag005) — Yun Ding, Yangzhen Jiang, Jing Wang, Dayu Tan, Yansen Su, and Chunhou Zheng. *Briefings in Bioinformatics*. [Paper](https://doi.org/10.1093/bib/bbag005) · [Code](https://github.com/GodIsGad/scMUSCLE)
- `[LLM]` [**ESMC: MLLM-Based Embedding Selection for Explainable Multiple Clustering**](https://ojs.aaai.org/index.php/AAAI/article/view/39867) — Xinyue Wang, Yuheng Jia, Hui Liu, and Junhui Hou. *AAAI*. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39867) · [Code](https://github.com/JCSTARS/Embedding-Selective-Multiple-Clustering)
- `[LLM]` [**Optimized Algorithms for Text Clustering with LLM-Generated Constraints**](https://arxiv.org/abs/2601.11118) — Chaoqi Jia, Weihong Wu, Longkun Guo, Zhigang Lu, Chao Chen, and Kok-Leong Ong. *AAAI*. [Paper](https://arxiv.org/abs/2601.11118) · [Code](https://github.com/weihong-wu/LSCK-HC)
- `[LLM]` [**LLM-CER** — In-context Clustering-based Entity Resolution with Large Language Models: A Design Space Exploration](https://doi.org/10.1145/3749170) — Jiajie Fu, Haitong Tang, Arijit Khan, Sharad Mehrotra, Xiangyu Ke, and Yunjun Gao. *SIGMOD*. [Paper](https://doi.org/10.1145/3749170)
- `[LLM]` [**NILC: Discovering New Intents with LLM-assisted Clustering**](https://doi.org/10.1145/3773966.3777979) — Hongtao Wang, Renchi Yang, and Wenqing Lin. *WSDM*. [Paper](https://doi.org/10.1145/3773966.3777979)
- `[LLM]` [**ComGPT: Detecting Local Community Structure with Large Language Models**](https://arxiv.org/abs/2408.06658) — Li Ni, Haowen Shen, Lin Mu, Yiwen Zhang, and Wenjian Luo. *IEEE TCSS*. [Paper](https://arxiv.org/abs/2408.06658)

### 2025

- `[HG]` [**AHRC** — On Graph Representation for Attributed Hypergraph Clustering](https://doi.org/10.1145/3709741) — Zijin Feng, Miao Qiao, Chengzhi Piao, and Hong Cheng. *SIGMOD*. [Paper](https://doi.org/10.1145/3709741) · [Code](https://github.com/ForPaperSubmissions/Attributed_Hypergraph_Representation_for_Clustering_Code)
- `[HG]` [**HCN-PAI** — Hypergraph Clustering Network with Partial Attribute Imputation](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Hypergraph_Clustering_Network_with_Partial_Attribute_Imputation_ICCV_2025_paper.html) — Qianqian Wang, Bowen Zhao, Zhengming Ding, Wei Feng, and Quanxue Gao. *ICCV*. [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Hypergraph_Clustering_Network_with_Partial_Attribute_Imputation_ICCV_2025_paper.html)
- `[HG]` [**HCN** — A Simple yet Effective Hypergraph Clustering Network](https://www.ijcai.org/proceedings/2025/0707) — Qianqian Wang, Bowen Zhao, Zhengming Ding, Xiangdong Zhang, and Quanxue Gao. *IJCAI*. [Paper](https://www.ijcai.org/proceedings/2025/0707)
- `[HG]` [**Edge-Colored Clustering in Hypergraphs: Beyond Minimizing Unsatisfied Edges**](https://openreview.net/forum?id=QAkh7c3r7c) — Alex Crane, Thomas Stanley, Blair D. Sullivan, and Nate Veldt. *ICML*. [Paper](https://openreview.net/forum?id=QAkh7c3r7c)
- `[HG]` [**Hypergraph Clustering Using Ricci Curvature: An Edge Transport Perspective**](https://openreview.net/forum?id=HMROU8MXqV) — Olympio Hacquard. *TMLR*. [Paper](https://openreview.net/forum?id=HMROU8MXqV)
- `[BIO+HG]` [**Hypergraph Representations of scRNA-seq Data for Improved Clustering with Random Walks**](https://arxiv.org/abs/2501.11760) — Wan He, Daniel I. Bolnick, Samuel V. Scarpino, and Tina Eliassi-Rad. *arXiv*. [Paper](https://arxiv.org/abs/2501.11760)
- `[BIO]` [**CHOIR Improves Significance-Based Detection of Cell Types and States from Single-Cell Data**](https://www.nature.com/articles/s41588-025-02148-8) — Cathrine Sant, Lennart Mucke, and M. Ryan Corces. *Nature Genetics*. [Paper](https://www.nature.com/articles/s41588-025-02148-8) · [Code](https://github.com/corceslab/CHOIR)
- `[BIO]` [**CLUEY: Clustering Single-Cell RNA-seq Data with Deep Embedded Learning**](https://doi.org/10.1093/bioinformatics/btaf528) — Daniel Kim, Carissa Chen, Lijia Yu, Jean Yee Hwa Yang, and Pengyi Yang. *Bioinformatics*. [Paper](https://doi.org/10.1093/bioinformatics/btaf528) · [Code](https://github.com/SydneyBioX/CLUEY)
- `[BIO]` [**scG-cluster: A Clustering Method for Single-Cell RNA Sequencing Data Based on Graph Neural Network**](https://www.nature.com/articles/s41598-025-87672-7) — Yi Zhang, Xi Feng, Yin Wang, and Kai Shi. *Scientific Reports*. [Paper](https://www.nature.com/articles/s41598-025-87672-7) · [Code](https://github.com/xixi-wq/scG-cluster)
- `[BIO+LLM]` [**EHR-DeBERTa** — Identifying Clusters of People with Multiple Long-Term Conditions Using Large Language Models: A Population-Based Study](https://doi.org/10.1038/s41746-025-01806-9) — Alexander Smith, Thomas Beaney, Carinna Hockham, Bowen Su, Paul Elliott, Laura Downey, Spiros Denaxas, Payam Barnaghi, Abbas Dehghan, and Ioanna Tzoulaki. *npj Digital Medicine*. [Paper](https://doi.org/10.1038/s41746-025-01806-9)
- `[LLM]` [**MARK: Multi-Agent Collaboration with Ranking Guidance for Text-Attributed Graph Clustering**](https://aclanthology.org/2025.findings-acl.314/) — Yiwei Fu, Yuxing Zhang, Chunchun Chen, Jianwen Ma, Quan Yuan, Rong-Cheng Tu, Xinli Huang, Wei Ye, Xiao Luo, and Minghua Deng. *Findings of ACL*. [Paper](https://aclanthology.org/2025.findings-acl.314/) · [Code](https://github.com/fuyw-aisw/MARK)
- `[LLM]` [**D2CS: Documents Graph Clustering Using LLM Supervision**](https://aclanthology.org/2025.findings-emnlp.1283/) — Yoel Ashkenazi, Etzion Harari, Regev Yehezkel Imra, Naphtali Abudarham, Dekel Cohen, and Yoram Louzoun. *Findings of EMNLP*. [Paper](https://aclanthology.org/2025.findings-emnlp.1283/) · [Code](https://github.com/D2CS-sub/D2CS)
- `[LLM]` [**Dial-In LLM: Human-Aligned LLM-in-the-Loop Intent Clustering for Customer Service Dialogues**](https://aclanthology.org/2025.emnlp-main.300/) — Mengze Hong, Wailing Ng, Chen Jason Zhang, Yuanfeng Song, and Di Jiang. *EMNLP*. [Paper](https://aclanthology.org/2025.emnlp-main.300/)
- `[LLM]` [**Controllable Clustering with LLM-Driven Embeddings**](https://aclanthology.org/2025.emnlp-industry.48/) — Kerria Pang-Naylor, Shivani Manivasagan, Aitong Zhong, Mehak Garg, Nicholas Mondello, Blake Buckner, Jonathan P. Chang, Khyati Mahajan, Masoud Hashemi, and Fabio Casati. *EMNLP Industry Track*. [Paper](https://aclanthology.org/2025.emnlp-industry.48/)
- `[HG+LLM]` [**LLMCom** — Semi-supervised Graph Convolutional Community Detection Empowered by Large Language Models](https://www.sciencedirect.com/science/article/abs/pii/S0950705125012778) — Shan Yang, Xiaoling Huang, Shan Ji, Cheng Zhang, and Shuai Zhang. *Knowledge-Based Systems*. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0950705125012778)
- `[LLM]` [**Text-attributed Community Detection in Complex Networks through LLMs and GNNs: A Powerful Fusion of Language and Graphs**](https://www.sciencedirect.com/science/article/pii/S0925231225012457) — Sruthi K. S., A. Sreekumar, and Kannan Balakrishnan. *Neurocomputing*. [Paper](https://www.sciencedirect.com/science/article/pii/S0925231225012457)
- `[LLM]` [**LLM-DAMVC: A Large Language Model Assisted Dynamic Agent for Multi-View Clustering**](https://proceedings.nips.cc/paper_files/paper/2025/hash/ad48f017e6c3d474caf511208e600459-Abstract-Conference.html) — Haiming Xu and Qianqian Wang. *NeurIPS*. [Paper](https://proceedings.nips.cc/paper_files/paper/2025/hash/ad48f017e6c3d474caf511208e600459-Abstract-Conference.html)
- `[LLM]` [**Agent-Centric Personalized Multiple Clustering with Multi-Modal LLMs**](https://arxiv.org/abs/2503.22241) — Ziye Chen, Yiqun Duan, Riheng Zhu, Zhenbang Sun, and Mingming Gong. *arXiv*. [Paper](https://arxiv.org/abs/2503.22241)
- `[LLM]` [**Text Clustering with Large Language Model Embeddings**](https://doi.org/10.1016/j.ijcce.2024.11.004) — Alina Petukhova, João P. Matos-Carvalho, and Nuno Fachada. *International Journal of Cognitive Computing in Engineering*. [Paper](https://doi.org/10.1016/j.ijcce.2024.11.004)
- `[LLM]` [**Unsupervised Text Clustering with Large Language Models**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5865188) — Leonid Kuligin, Jacqueline Lammert, Florence Heinkelein, Keno Bressem, Martin Boeker, and Maximilian Tschochohei. *SSRN*. [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5865188)
- `[LLM]` [**LLM-MemCluster: Empowering Large Language Models with Dynamic Memory for Text Clustering**](https://arxiv.org/abs/2511.15424) — Yuanjie Zhu, Liangwei Yang, Ke Xu, Weizhi Zhang, Zihe Song, Jindong Wang, and Philip S. Yu. *arXiv*. [Paper](https://arxiv.org/abs/2511.15424)
- `[LLM]` [**GC** — Information-Theoretic Generative Clustering of Documents](https://ojs.aaai.org/index.php/AAAI/article/view/33802) — Xin Du and Kumiko Tanaka-Ishii. *AAAI*. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/33802) · [Code](https://github.com/kduxin/lmgc)
- `[LLM]` [**LiSA** — LLM-Guided Semantic-Aware Clustering for Topic Modeling](https://aclanthology.org/2025.acl-long.902/) — Jianghan Liu, Ziyu Shang, Wenjun Ke, Peng Wang, Zhizhao Luo, Jiajun Liu, Guozheng Li, and Yining Li. *ACL*. [Paper](https://aclanthology.org/2025.acl-long.902/) · [Code](https://github.com/ljh986/LiSA)
- `[LLM]` [**ZeroDL: Zero-shot Distribution Learning for Text Clustering via Large Language Models**](https://aclanthology.org/2025.findings-acl.1005/) — Hwiyeol Jo, Hyunwoo Lee, Kang Min Yoo, and Taiwoo Park. *Findings of ACL*. [Paper](https://aclanthology.org/2025.findings-acl.1005/)
- `[LLM]` [**Cequel: Cost-Effective Querying of Large Language Models for Text Clustering**](https://doi.org/10.1145/3746252.3761074) — Hongtao Wang, Taiyan Zhang, Renchi Yang, and Jianliang Xu. *CIKM*. [Paper](https://doi.org/10.1145/3746252.3761074)
- `[LLM]` [**Context-Aware Hierarchical Taxonomy Generation for Scientific Papers via LLM-Guided Multi-Aspect Clustering**](https://aclanthology.org/2025.emnlp-main.788/) — Kun Zhu, Lizi Liao, Yuxuan Gu, Lei Huang, Xiaocheng Feng, and Bing Qin. *EMNLP*. [Paper](https://aclanthology.org/2025.emnlp-main.788/)
- `[LLM]` [**ClusterFusion: Hybrid Clustering with Embedding Guidance and LLM Adaptation**](https://arxiv.org/abs/2512.04350) — Yiming Xu, Yuan Yuan, Vijay Viswanathan, and Graham Neubig. *arXiv*. [Paper](https://arxiv.org/abs/2512.04350)
- `[LLM]` [**Text Clustering as Classification with LLMs**](https://doi.org/10.1145/3767695.3769519) — Chen Huang and Guoxiu He. *SIGIR-AP*. [Paper](https://doi.org/10.1145/3767695.3769519) · [Code](https://github.com/ECNU-Text-Computing/Text-Clustering-via-LLM)
- `[LLM]` [**CS-Agent: LLM-based Community Search via Dual-agent Collaboration**](https://doi.org/10.1145/3746252.3761335) — Jiahao Hua, Long Yuan, Qingshuai Feng, Qiang Fan, and Shan Huang. *CIKM*. [Paper](https://doi.org/10.1145/3746252.3761335)
- `[LLM]` [**CommLLM** — LLMs Between the Nodes: Community Discovery Beyond Vectors](https://arxiv.org/abs/2507.22955) — Ekta Gujral and Apurva Sinha. *CSIT*. [Paper](https://arxiv.org/abs/2507.22955)
- `[LLM]` [**ICC** — In-Context Clustering with Large Language Models](https://arxiv.org/abs/2510.08466) — Ying Wang, Mengye Ren, and Andrew Gordon Wilson. *arXiv*. [Paper](https://arxiv.org/abs/2510.08466) · [Code](https://agenticlearning.ai/icc/)

### 2024

- `[BIO+HG]` [**Hypergraph Neural Networks Reveal Spatial Domains from Single-Cell Transcriptomics Data**](https://arxiv.org/abs/2410.19868) — Mehrad Soltani and Luis Rueda. *arXiv*. [Paper](https://arxiv.org/abs/2410.19868)
- `[BIO]` [**scMLC: A Multi-Level Clustering Method for Single-Cell RNA-seq Data**](https://doi.org/10.1093/bib/bbae101) — Yuxuan Chen, Ruiqing Zheng, Jin Liu, and Min Li. *Briefings in Bioinformatics*. [Paper](https://doi.org/10.1093/bib/bbae101)
- `[LLM]` [**Large Language Models Enable Few-Shot Clustering**](https://aclanthology.org/2024.tacl-1.18/) — Vijay Viswanathan, Kiril Gashteovski, Carolin Lawrence, Tongshuang Wu, and Graham Neubig. *TACL*. [Paper](https://aclanthology.org/2024.tacl-1.18/) · [Code](https://github.com/viswavi/few-shot-clustering)
- `[LLM]` [**GCLR** — Large Language Model Guided Graph Clustering](https://openreview.net/forum?id=CLyhlb5DG5) — Puja Trivedi, Nurendra Choudhary, Eddie Huang, Vassilis N. Ioannidis, Karthik Subbian, and Danai Koutra. *LoG*. [Paper](https://openreview.net/forum?id=CLyhlb5DG5)
- `[LLM]` [**LLMEdgeRefine: Enhancing Text Clustering with LLM-Based Boundary Point Refinement**](https://aclanthology.org/2024.emnlp-main.1025/) — Zijin Feng, Luyang Lin, Lingzhi Wang, Hong Cheng, and Kam-Fai Wong. *EMNLP*. [Paper](https://aclanthology.org/2024.emnlp-main.1025/)
- `[LLM]` [**Improving Hierarchical Text Clustering with LLM-guided Multi-view Cluster Representation**](https://aclanthology.org/2024.emnlp-industry.54/) — Anup Pattnaik, Cijo George, Rishabh Kumar Tripathi, Sasanka Vutla, and Jithendra Vepa. *EMNLP Industry Track*. [Paper](https://aclanthology.org/2024.emnlp-industry.54/)

### 2023

- `[LLM]` [**ClusterLLM: Large Language Models as a Guide for Text Clustering**](https://aclanthology.org/2023.emnlp-main.858/) — Yuwei Zhang, Zihan Wang, and Jingbo Shang. *EMNLP*. [Paper](https://aclanthology.org/2023.emnlp-main.858/) · [Code](https://github.com/zhang-yu-wei/ClusterLLM)
- `[HG]` [**AHCKA** — Efficient and Effective Attributed Hypergraph Clustering via K-Nearest Neighbor Augmentation](https://doi.org/10.1145/3589261) — Yiran Li, Renchi Yang, and Jieming Shi. *SIGMOD*. [Paper](https://doi.org/10.1145/3589261) · [Code](https://github.com/CyanideCentral/AHCKA)
- `[BIO]` [**MoClust: Identifying Cell Types from Single-Cell Transcriptomics Data Using Multi-Objective Clustering**](https://doi.org/10.1093/bioinformatics/btac736) — Musu Yuan, Liang Chen, and Minghua Deng. *Bioinformatics*. [Paper](https://doi.org/10.1093/bioinformatics/btac736) · [Code](https://doi.org/10.5281/zenodo.7306504)

### 2021

- `[HG]` [**GRAC** — HyperGraph Convolution Based Attributed HyperGraph Clustering](https://doi.org/10.1145/3459637.3482437) — Barakeel Fanseu Kamhoua, Lin Zhang, Kaili Ma, James Cheng, Bo Li, and Bo Han. *CIKM*. [Paper](https://doi.org/10.1145/3459637.3482437) · [Code](https://github.com/BarakeelFanseu/GRAC_CIKM)
<!-- CATALOG:END -->

## Status legend

- `peer-reviewed`: published in a peer-reviewed venue.
- `preprint`: public manuscript without a confirmed peer-reviewed venue at this snapshot.
- `forthcoming`: venue information is public but the paper page is not yet available.
- Missing code means no clearly official implementation was found during curation; it does not prove that none exists.

## Related collections

- [Awesome-LLMs-for-Clustering](https://github.com/Marigoldwu/Awesome-LLMs-for-Clustering)
- [Awesome Deep Graph Clustering](https://github.com/yueliu1999/Awesome-Deep-Graph-Clustering)
- [PyAGC](https://github.com/Cloudy1225/PyAGC)
- [Awesome Single-Cell Clustering](https://github.com/DayuHuu/Awesome-Single-Cell-Clustering)
- [Awesome Hypergraph Network](https://github.com/gzcsudo/Awesome-Hypergraph-Network)
- [MASK](https://github.com/fuyw-aisw/MASK)

These repositories are discovery sources. Records here are normalized and checked against paper or project pages rather than copied wholesale.

## Contributing

Edit `data/papers.json`, then run:

```bash
python scripts/validate_catalog.py
python scripts/build_catalog.py
python scripts/check_links.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion checklist. The repository is released under the [MIT License](LICENSE).
