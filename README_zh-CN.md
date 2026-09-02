# Awesome Clustering Research

面向组内学生的聚类研究知识库，围绕三条相互交叉的主线整理：**生物聚类、超图聚类、LLM 聚类**。

## 分类规则

| 标签 | 含义 | 典型范围 |
| --- | --- | --- |
| `BIO` | 生物与医学聚类 | 单细胞、空间转录组、多组学、临床表型等 |
| `HG` | 超图聚类 | 超图是表示、目标函数或算法的核心组成 |
| `LLM` | LLM 增强聚类 | 生成式大语言模型参与表征、监督、反馈、推理或解释 |

一篇论文可以有多个标签。例如：

- `[BIO+HG]`：用超图方法做生物数据聚类；
- `[BIO+LLM]`：用 LLM 增强生物或医学聚类；
- `[HG+LLM]`：用 LLM 做超图聚类；
- `[BIO+HG+LLM]`：三条主线同时覆盖。

目录统一按年份倒序排列，交叉方向通过组合标签表达，不重复收录同一篇论文。详细边界见 [分类规范](docs/TAXONOMY.md)。

## 使用方式

- 在主 [README](README.md) 中按年份阅读；
- 打开 [可筛选论文页](docs/index.html)，按 `BIO / HG / LLM` 或关键词筛选；
- 在 [结构化数据](data/papers.json) 中按年份、标签、会议或代码状态检索；
- 新增论文时遵循 [贡献指南](CONTRIBUTING.md)，不要直接手改 README 中的论文列表。

## 维护原则

1. 论文必须以聚类为核心任务或明确贡献，而不是仅在背景中提到聚类。
2. 优先使用出版社、ACL Anthology、OpenReview、CVF 或 arXiv 摘要页。
3. 只链接能够确认的官方或作者维护代码。
4. 预印本、已发表和待发表状态必须明确区分。
5. 先改 `data/papers.json`，再运行校验与生成脚本。

## 本地检查

```bash
python scripts/validate_catalog.py
python scripts/build_catalog.py
python scripts/check_links.py
```

本项目采用 [MIT License](LICENSE)。
