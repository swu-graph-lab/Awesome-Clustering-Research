# LLM4GM 组内使用说明

这是一个面向 **Large Language Models for Graph Mining（LLM4GM）** 的可维护论文仓库，不是简单的链接堆积。英文 `README.md` 用于公开展示；机器可读目录 `data/papers.json` 是唯一数据源。

## 仓库定位

当前重点覆盖：

- 图聚类与社区发现，特别是文本属性图、长尾/不平衡图和动态图；
- 节点分类、图结构学习和通用图任务；
- LLM 与 GNN 的特征增强、监督生成、结果修正、对齐和协同训练；
- 能帮助公平比较方法的 survey、benchmark 和开源实现。

默认不收录纯 GraphRAG、知识图谱问答、Graph-of-Thought，以及只使用小型预训练编码器但没有 LLM 参与的方法。边界规则见 `docs/TAXONOMY.md`。

## 日常使用

1. 在 `README.md` 按任务快速浏览。
2. 需要筛选时直接读取 `data/papers.json`，可以按 `tasks`、`roles`、`year`、`status` 和是否有 `code` 过滤。
3. 研究图聚类时建议依次看 GCLR、MARK、MASK、DyG-RoLLM，再用 PyAGC 和 Awesome Deep Graph Clustering 补传统基线。

## 新增论文

不要直接改 `README.md` 中的论文表格。复制 `data/papers.json` 里的一条记录，补全元数据后运行：

```bash
python scripts/validate_catalog.py
python scripts/build_catalog.py
```

提交前至少确认：题目、年份、venue、稳定论文链接、官方代码链接、任务标签、LLM 角色和发表状态。

## 关于 contributors

GitHub 中有两个不同概念：

- **Collaborator** 是有仓库读写权限的人，需要仓库 owner 在 Settings → Collaborators 中邀请。
- **Contributor** 通常由实际 commit/PR 自动产生，不能只靠在 README 写名字来可靠地生成。

因此，老师和王奕涵如果要显示为 contributors，最稳妥的做法是各自用 GitHub 账号提交一次真实修改并合并；如果还需要维护权限，再单独邀请为 collaborators。创建远程仓库前需要先确认两人的 GitHub 用户名。

## 首次发布

本地检查通过后，由仓库 owner 在本目录执行：

```bash
gh repo create LLM4GM --public --source=. --remote=origin --push
```

这个命令会创建公开远程仓库并推送；执行前应先确认仓库名称、公开性和两位协作者的账号。
