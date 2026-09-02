# 参考仓库写作风格与本仓库取舍

这份说明记录首版 LLM4GM 仓库如何借鉴现有项目，方便后续维护者保持一致风格。

## 观察到的写法

### Awesome-LLMs-for-Clustering

- 优点：开头直接给 taxonomy，正文按年份展开，paper/code 入口紧凑，贡献模板明确。
- 可改进处：覆盖范围横跨普通文本、视觉、多视图和图聚类，任务边界不够明显；datasets 与 citation 仍是占位内容；分类法没有实际落到每条记录上。
- 本仓库采用：紧凑的论文入口和 taxonomy-first 的叙述。
- 本仓库改进：限定 graph mining scope，并给每篇论文同时标注 task 和 LLM role。

### MASK

- 优点：README 很短，直接给安装和复现实验命令，适合代码型论文仓库。
- 可改进处：研究动机、方法流程、数据准备、预期输出、硬件环境和 citation 信息不足。
- 本仓库采用：对核心项目保留直达 code 的入口。
- 本仓库改进：在清单里说明该方法解决长尾图聚类问题，并把 paper 尚未公开这一状态显式标为 `forthcoming`。

### PyAGC

- 优点：采用“问题 → 解决方案 → 特性 → Quick Start → Benchmark → Reproducibility”的完整叙事；表格口径清楚，ECO 框架把方法差异讲得很直观。
- 可改进处：作为库和 benchmark，其 README 信息量很大，不适合原样套到 Awesome List。
- 本仓库采用：问题导向的 scope、快速阅读路径、表格和可复现维护命令。

### Awesome Deep Graph Clustering

- 优点：先定义研究问题，再按方法家族列 survey、论文、数据集、citation，覆盖面广，读者容易从领域全景逐步下钻。
- 可改进处：长期手工维护的超长表格容易出现重复、年份/venue 不一致和链接漂移。
- 本仓库采用：任务优先的浏览方式和 graph clustering 一级分类。
- 本仓库改进：JSON 单一数据源、重复检查、自动生成 README 和 CI 校验。

### Awesome Graph LLM / Awesome LLM4Graph Papers

- 优点：前者按应用任务查找方便，后者按 GNN/LLM 交互方式解释方法机制，两种视角互补。
- 可改进处：只按任务会看不清 LLM 的具体作用，只按集成范式又不方便研究者快速找到某个 graph-mining task；两者都包含大量超出 LLM4GM 的 GraphRAG、KGQA 或通用图推理内容。
- 本仓库采用：把两个视角拆成独立标签轴。
- 本仓库改进：README 按任务展示，机器目录保留全部 LLM role 标签，并写清排除项。

## 最终写作约定

1. 先讲清范围，再给论文；不以“收得多”替代“收得准”。
2. 摘要句只陈述方法做了什么，不写 SOTA、significant、novel 等宣传性词语。
3. 论文状态、代码缺失和元数据不确定性要显式标注。
4. 公开 README 使用简洁英文，组内流程和账号协作说明放在中文文档。
5. 所有表格来自机器可读目录，避免同一论文在多个章节复制粘贴。
