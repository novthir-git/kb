---
tags: [对比, AI, RAG, 知识管理]
created: 2026-07-28
updated: 2026-08-11
sources:
  - "https://li.feishu.cn/file/CXkubLDs5oF6EUxJA9Ucedi7nBh （原视频，读取于 2026-07-28）"
  - "https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/ （检索于 2026-07-28）"
  - "https://www.microsoft.com/en-us/research/blog/benchmarkqed-automated-benchmarking-of-rag-systems/ （检索于 2026-07-28）"
  - "https://neo4j.com/docs/neo4j-graphrag-python/current/user_guide_rag.html （检索于 2026-07-28）"
  - "[[知识图谱]]"
---

# GraphRAG 与 Vector RAG

## 先消除术语歧义

“GraphRAG”不是一个边界统一的单一算法。至少要区分四种机制：

| 机制 | 核心做法 | 典型问题 |
|---|---|---|
| Vector RAG | 将问题与文本 chunk 嵌入后做相似度召回 | “哪里提到退款条件？” |
| Text2Cypher / 图谱问答 | LLM 把问题翻译成 Cypher，再查询已有属性图 | “A 通过哪些公司与 B 关联？” |
| Microsoft GraphRAG Global Search | 从语料构建实体图与社区摘要，再综合各社区的局部回答 | “整个语料的主要主题是什么？” |
| 混合检索 | 向量召回、全文、图遍历或社区摘要按问题组合 | 查询类型未知或同时需要原文与关系 |

[[从知识图谱到 Agent 编排]] 所析原视频（li.feishu.cn，读取于 2026-07-28，URL 见 frontmatter）演示的“自然语言问题 → Cypher → Neo4j → 答案”更准确地属于
**Text2Cypher / 知识图谱问答**。Neo4j 的 GraphRAG 包将 Text2Cypher、VectorRetriever、
HybridRetriever 和 VectorCypherRetriever 明确列为不同 Retriever；不能用一个“GraphRAG”标签抹平差别。

## 能力与代价

| 维度 | Vector RAG | Text2Cypher / 图检索 | Microsoft GraphRAG Global |
|---|---|---|---|
| 基本检索单元 | 文本 chunk | 实体、关系、属性、路径 | 图社区及预生成摘要 |
| 相对优势 | 局部语义相关、原文定位、部署简单 | 精确关系、多跳路径、结构约束 | 跨整个语料的主题与全局 sensemaking |
| 主要前提 | 合理切块、embedding 与排序 | 稳定 Schema、实体消歧、可验证查询 | 高质量建图、社区划分和摘要 |
| 常见失败 | 片段割裂、错过全局结构 | 错图、错 Cypher、Schema 不覆盖问题 | 索引成本高、摘要丢细节或放大抽取错误 |
| 溯源方式 | 返回原始 chunk | 返回路径后仍应关联原始证据 | 社区摘要仍需下钻到源文本 |
| 更新成本 | 通常较低 | 需同步实体与关系 | 还需维护社区与摘要 |

## 没有绝对赢家

Microsoft 的 BenchmarkQED 结果显示，各系统在为其设计的问题类型上相对更强：
GraphRAG Global 对全局查询更合适，Vector RAG 对局部查询更合适，结合两类策略的
GraphRAG Drift Search 是最强的总体挑战者之一。

这不是对所有数据集和模型的永久排名。评测使用特定语料、查询类别、上下文预算、生成模型和自动指标；
正式选型仍需用自己的查询集、权限规则和成本约束做 [[Evals|Eval]]。

## 按问题路由

| 问题特征 | 首选路径 |
|---|---|
| 高频变化、必须取当前值 | 直接查询权威 API / 数据库 |
| 找原文、相似案例、局部事实 | 全文或 Vector RAG |
| 已有可靠图谱，问题要求明确关系或多跳路径 | 图查询 / Text2Cypher |
| 问整个语料的主题、结构或跨群体模式 | GraphRAG Global 类方法 |
| 同时需要模糊召回、关系扩展和原文证据 | Vector → graph expansion → source evidence |
| 查询类型不确定 | 先分类路由，并保留降级路径 |

## 安全边界

- LLM 生成的 Cypher 应限制为只读、限制可访问标签/属性，并在执行前做语法与策略检查。
- 图谱中的关系必须携带来源；“存在一条边”不是事实证明。
- 图或向量索引都不应绕过源系统 ACL。
- 生成回答应引用原始文本或权威记录，而不只引用派生摘要。
- 索引更新必须有版本、回归 Eval、回滚和旧知识退役机制。

## 结论

综合：检索架构的正确问题不是“GraphRAG 还是 Vector RAG”，而是：

> **当前查询属于局部语义、显式关系、全局综合还是实时权威事实？**

先按问题分类，再选择或组合检索器。总体位置见 [[从知识图谱到 Agent 编排]]。

