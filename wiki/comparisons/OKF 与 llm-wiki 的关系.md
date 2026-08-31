---
tags: [对比, AI, 知识管理, Agent, 方法论]
created: 2026-07-28
updated: 2026-08-31
sources:
  - "[[Open Knowledge Format]]"
  - "[[2026-07-28-GoogleCloudPlatform-Knowledge-Catalog与OKF-源摘要]]"
  - "[[llm-wiki-方法论]]"
  - "[[从知识图谱到 Agent 编排]]"
  - "https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md （v0.2，规范新权威位置，检索于 2026-08-31）"
---

# OKF 与 llm-wiki 的关系

## 核心结论

OKF 与本仓库都采用 Markdown、YAML、目录、链接和 Git 友好的知识制品，但目标不同：

- **OKF 优先解决互操作**：不同生产者和消费者怎样交换最低限度可读的知识；
- **llm-wiki 优先解决长期维护**：来源怎样被编译、横向整合、修订、体检并持续产生复利。

综合：两者应是“**严格内部模型 + 宽松交换格式**”的关系，不宜把本仓库直接改造成最低合规的 OKF Bundle。

## 逐维比较

| 维度 | OKF v0.2 | 当前 llm-wiki |
|---|---|---|
| 首要目标 | 跨工具、Agent 和平台交换 | 个人研究知识的持续编译与治理 |
| 最小合规 | 每个 Concept 只需 `type` | 页面必须有类型、日期、来源，并遵守目录和工作流 |
| 分层 | 一个 Bundle 可混合来源、概念、Skill、计算 | `raw/` 不可变、`wiki/` 可修订、`AGENTS.md` 管流程 |
| 链接 | 标准 Markdown 链接，边无类型 | Obsidian 双链，同样主要是轻量语义关系 |
| 索引 | 每级目录可有 `index.md` | 根 `index.md` 是全站内容导航 |
| 日志 | 可选、按作用域、规范示例为最新在前 | 根 `log.md` 强制 append-only，固定事件前缀 |
| 来源 | 结构化 `sources[]`，可带 claim ID、author、usage、时间 | `sources` 为字符串列表，强调可回查但机器语义较弱 |
| 信任 | `generated` 与 `verified` 分离 | 主要靠来源、综合标记、人工确认和维护流程 |
| 生命周期 | `status`、`stale_after` | `created/updated`，加 schema 中的退役与原始源只读规则 |
| 计算验证 | Attested Computation | 现有页面尚无统一的逐次计算证明合约 |
| 质量治理 | 消费者宽容、约束大多可选 | Research/Ingest/Lint、矛盾标注、入链和索引一致性是强约束 |

## 本仓库更强的部分

1. **来源与综合分层**：`raw/` 不可变，`wiki/` 是可修订的编译层，避免来源和模型综合互相覆盖。
2. **有维护协议**：Query、Research、Ingest、Lint、横向更新、索引和日志是一套可执行的知识运维流程。
3. **主动处理矛盾和孤儿页**：知识不是“能解析就算完成”，还要求跨页一致性和入链。
4. **沉淀价值守门**：强调“事件是证据，论点才是资产”，避免 Bundle 演化为自动生成文件堆。

这些能力属于 [[llm-wiki-方法论]] 的维护层，不应为了兼容一个宽松交换格式而降级。

## OKF 更强的部分

1. **生产与核验分离**：`generated` 和 `verified` 能表达 Agent 生成、人审与机器确认的区别。
2. **结构化来源**：稳定的 source ID 可支持逐论断归因和自动检查。
3. **显式保鲜期**：`stale_after` 比只有 `updated` 更直接地表达“何时必须重新核验”。
4. **执行证明**：Attested Computation 把批准定义、本次执行与展示结果连接起来。
5. **标准 Markdown 可移植性**：相比 Obsidian 双链，更容易给 GitHub、静态站点和通用消费者直接读取。

这些设计值得吸收，但它们目前多数是**声明和契约字段**，仍需身份、发布、权限、事件与确定性检查支撑。

## 字段映射与缺口

| llm-wiki | OKF | 转换问题 |
|---|---|---|
| 目录类别 + `tags` | `type` + `tags` | 需要定义 analyses/concepts/topics 等稳定 type 映射 |
| `created` / `updated` | `generated.at` | `updated` 没记录生产者；`created` 在 OKF 无直接标准字段 |
| 字符串 `sources` | 映射形式 `sources[]` | URL、双链、本地 raw 路径需要规范化为 `resource`，并生成稳定 ID |
| Obsidian wikilink | 标准 Markdown 路径链接 | 导出时需解析唯一文件名并计算相对路径 |
| 矛盾 blockquote | 无专门字段 | 可保留正文，或作为扩展字段而非丢失 |
| `raw/` 与 `wiki/` | 单个 Bundle | 导出时应只发布选定 wiki 页，并保留 sources 指回 raw 或外部源 |
| 强制根 index/log | 可选、可分级 index/log | 应由导出器生成，不能手工维护第二套事实源 |

## 采用决策（2026-07-28）

当前不修改 `AGENTS.md` 的规范，也不把现有页面整体迁移到 OKF，理由是：

- v0.2 仍处早期，且对 v0.1 有两项刻意的字段替换；
- 当前仓库的严格维护规则比 OKF 最低合规更适合作为内部 canonical model；
- `sources`、双链、索引和日志的语义不同，直接改造会产生大面积迁移与 lint 成本；
- Knowledge Catalog 的 OKF 往返仍是实验性、非全字段映射。

> 2026-08-31 联网复核：**决策不变，前两条理由被加强。** 规范仍是 v0.2、未发新版本，但
> ① OKF 的权威仓库已于 2026-08-21 迁至
> https://github.com/GoogleCloudPlatform/open-knowledge-format ，
> 原 `knowledge-catalog/okf/` 被标注为不再维护的冻结快照；
> ② v0.2 文档同日被**原地修订**（所有时间戳字段改为必须带显式 UTC 偏移的 ISO 8601 datetime，
> 裸日期值消费者必须拒绝），即版本号不变而文本仍在变。
> 综合：因此下方第 5 条“规范稳定后再评估双向同步”里的“稳定”不能以版本号为准——v0.2 目前
> 不构成可锚定的稳定目标；若要建 export profile，须对齐**具体 commit** 而非版本号。
> 变化细节见 [[Open Knowledge Format]] 的「已知边界」。（检索于 2026-08-31）

推荐按以下顺序试验：

1. **只吸收语义，不改 schema**：先在关键判断中区分 generated、verified、freshness。
2. **局部试用 Attested Computation**：选择一个 SQL 指标或自动报告，验证批准计算、receipt 与确定性检查。
3. **建立单向 OKF export profile**：从 `wiki/` 生成独立 Bundle；导出物可重建，不手工编辑。
4. **定义验收标准**：往返不丢来源、标题、正文和关键链接；断链为零；来源可回查；导出结果可被通用 Markdown 工具读取。
5. **规范稳定后再评估双向同步**：只有出现真实外部消费者时，才承担兼容层成本。

综合：本仓库应继续充当**知识编译与治理系统**，OKF 只充当**发布和交换边界**。这与
[[从知识图谱到 Agent 编排]] 的原则一致：canonical knowledge、派生表示和消费接口可以彼此连接，
但不能互相冒充。
