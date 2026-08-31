---
tags: [概念, AI, 知识管理, 数据治理, Agent]
created: 2026-07-28
updated: 2026-08-31
sources:
  - "[[2026-07-28-GoogleCloudPlatform-Knowledge-Catalog与OKF-源摘要]]"
  - "https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md （v0.2，检索于 2026-07-28；该路径已于 2026-08-21 被原仓库标注为冻结快照）"
  - "https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md （检索于 2026-07-28 与 2026-08-31）"
  - "https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md （v0.2，规范新权威位置，检索于 2026-08-31）"
---

# Open Knowledge Format（OKF）

Open Knowledge Format（OKF）是一种用**Markdown 正文 + YAML frontmatter + 目录结构**表达知识的开放文件格式。
它试图让人、Agent、Git、静态站点、搜索索引和图形 Viewer 共同消费同一份知识制品，而不依赖特定模型、
Agent 框架或托管目录。

综合：OKF 最准确的定位是**知识制品的交换协议**，不是知识库产品、知识图谱数据库、RAG 引擎、
Agent 编排器或访问控制系统。

## 不要混淆四个对象

| 对象 | 本质 | 主要职责 |
|---|---|---|
| Google Cloud Knowledge Catalog | 托管元数据与治理服务 | Entry、Aspect、Glossary、typed link、搜索、权限与变更事件 |
| `knowledge-catalog` GitHub 仓库 | 工具和示例集合 | Discovery、Metadata as Code、Enrichment、OKF PoC |
| OKF | 文件格式 | 让知识能被阅读、版本化、打包与交换 |
| Reference Agent / Viewer | OKF 的参考生产者与消费者 | 从 BigQuery/Web 生成 Bundle；把 Bundle 渲染为交互图 |

仓库根 README 明确声明其内容“不是 Google 官方产品”。因此 OKF 的规范价值应根据文本和实现本身判断，
不能因为仓库组织归属就推断为 Google Cloud 产品承诺。

## Bundle 与 Concept

```text
bundle/
├── index.md          # 可选：逐层发现
├── log.md            # 可选：更新历史
├── metrics/
│   ├── index.md
│   └── revenue.md    # Concept
└── computations/
    └── revenue.md    # Concept
```

- Bundle 是目录树；
- 非保留 `.md` 文件是 Concept；
- Concept ID 是去掉 `.md` 后的 Bundle 相对路径；
- 每个 Concept 必须有可解析的 YAML frontmatter，唯一强制字段是非空 `type`；
- 正文没有强制章节，可按需使用 `# Schema`、`# Examples`、`# Computation`；
- 生产者可以增加任意字段，消费者应宽容处理未知类型、未知字段、断链和缺失索引。

这种最小约束有利于互操作，但也意味着“OKF conformant”只证明文件可被基础消费者读取，
不证明内容完整、正确或达到企业治理要求。

## 来源、信任与生命周期

| 字段 | 表达什么 | 不保证什么 |
|---|---|---|
| `sources` | 内容来自哪些内部或外部材料 | 来源本身真实、权威或仍有效 |
| `generated` | 当前内容由谁、何时产生 | 生产者判断正确 |
| `verified` | 谁、何时对照来源或资源核验 | 核验者身份已认证、核验过程充分 |
| `status` | `draft / stable / deprecated` | 自动执行发布审批 |
| `stale_after` | 到哪个时刻应视为过期 | 上游变化发生时自动失效 |

正文可用脚注 ID 连接 `sources[].id`，实现逐论断归因。`generated` 与 `verified` 分离尤其重要：
“谁写的”与“谁确认的”不是同一个问题。

规范根据 `verified` 派生 unverified、machine-confirmed、human-reviewed，但这些只是建议性信号。
`human:<id>` 是命名约定，不是签名、IAM 或访问控制。缺失 `status` 又会默认 `stable`，所以高风险场景
仍需要外部身份、审批、权限和发布系统。

## 链接图不等于知识图谱

OKF Concept 通过标准 Markdown 链接形成有向图，但关系类型由链接周围的文字解释，消费者通常把它们
视为无类型边；断链也被规范允许。

综合：这使 OKF “graph-shaped”，但不等同于 [[知识图谱]]。它没有统一 ontology、typed edge、
实体消歧、关系属性和约束验证。若需要可执行的多跳关系查询，应从 OKF 编译出属性图、RDF 或其他派生索引，
同时保留回到 Concept 与原始来源的引用。

## Attested Computation

`type: Attested Computation` 把批准过的计算独立建模，并声明：

- `runtime`：BigQuery、Postgres、dbt、Python、Looker 等执行语义；
- `parameters`：Agent 只能填写的具名参数；
- `computation` 或正文 `# Computation`：批准过的 SQL、代码或模型；
- `executor`：怎样运行，以及 receipt 必须返回什么证据；
- `attester`：无 LLM 的确定性校验器。

消费者应执行计算、获得 receipt、校验实际执行物与显示值，并拒绝展示未通过 attestation 的结果。
这回答的是“本次数字是否按批准方式生成”，而 `verified` 回答“批准的定义是否仍符合政策”。

综合：它为 [[从知识图谱到 Agent 编排]] 的“知识 → 行动 → 验证”边界提供了有价值的契约模型。
但 OKF 本身不执行计算；v0.2 尚未定义完整运行协议、Attester ABI、沙箱和缓存，现阶段不能把它当成熟执行平台。

## Reference Agent 的位置

参考 Agent 先从 BigQuery 元数据生成 Concept，再从显式 Web 种子开始做受限补充。它会保护已有 Schema
和来源，优先抽取可复用的 Metric、Dimension 与 Join Path。

综合：Reference Agent 是**知识编译器**，不是 [[Agent 记忆架构|记忆系统]] 或编排器。它负责把来源编译成
可携带语义制品，但不提供完整的 Write/Retrieve/Update/Forget 策略，也不决定业务任务如何分解和执行。

## 已知边界

> 2026-08-31 联网复核：规范**仍是 v0.2**，未发布新版本（SPEC §12「This document specifies OKF
> version 0.2」）；但一个月内有两项实质变化。
> ① **权威仓库搬家**：OKF 已于 2026-08-21 迁到独立仓库
> https://github.com/GoogleCloudPlatform/open-knowledge-format （建仓 2026-08-11），
> `knowledge-catalog/okf/` 被原仓库自己标注为“frozen snapshot, no longer maintained”，
> 而本页最初引用的正是该快照路径。
> ② **v0.2 被原地修订**：同日起所有时间戳字段必须是**带显式 UTC 偏移的 ISO 8601 datetime**，
> 仅有日期的 `stale_after`、`sources[].last_modified`、`usage_window` 值消费者必须拒绝
> （此前 `stale_after` 是裸日期）。
> 未变的部分：§12「Considered and deferred」仍把完整运行协议、receipt/verdict wire format、
> Attester ABI、沙箱与缓存留给未来版本，故上文 Attested Computation 一节的判断仍成立。
> （以上均检索于 2026-08-31，来源为该仓库 SPEC.md、README.md 与 commit #323 / PR #6）

1. **规范早期**：当前为 v0.2，且 v0.2 对 v0.1 仍包含字段替换；更要紧的是 v0.2 文档本身会被
   **原地修订而不 bump 版本号**（见上方 2026-08-31 复核），因此“锁定 v0.2”并不等于锁定了一份稳定文本。
2. **关系弱类型**：Markdown 边不能承载正式图模型的关系约束。
3. **路径即身份**：重命名或移动目标 Concept 会改变 ID 并可能破坏外部引用。
4. **信任可声明但未认证**：actor 和 verified 缺少规范级签名与身份绑定。
5. **保鲜是静态日期**：`stale_after` 没有上游依赖变更触发和 Desired–Actual 调和。
6. **托管目录映射不完整**：Knowledge Catalog 的 OKF custom Aspect 仍是实验性局部转换。
7. **Viewer 非严格离线**：数据嵌入 HTML，但运行库从 CDN 加载。

## 在七层架构中的位置

| 七层 | OKF 承担什么 | 不承担什么 |
|---|---|---|
| 权威事实 | 通过 `sources` 指回事实源 | 不自动成为事实源 |
| 派生表示 | 可读、可版本化的知识制品 | 不替代图、向量、全文索引 |
| 检索与证据 | 为搜索或 RAG 提供可索引输入 | 不规定召回和路由算法 |
| Agent 记忆 | 可作为持久语义记忆载体 | 不实现完整记忆生命周期 |
| 决策与编排 | 可保存 Playbook、Skill、计算契约 | 不负责执行控制流 |
| 集成与行动 | Executor 可引用外部执行说明 | 不提供 MCP、API 或权限系统 |
| 验证与调和 | `verified`、`stale_after`、attestation 提供信号 | 不提供完整发布、IAM、事件调和 |

与本仓库的采用判断见 [[OKF 与 llm-wiki 的关系]]；企业治理映射见 [[基于IT4IT的Agent知识治理]]。
