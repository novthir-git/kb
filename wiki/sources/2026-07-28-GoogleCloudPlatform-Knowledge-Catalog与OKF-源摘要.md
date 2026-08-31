---
tags: [素材, AI, 知识管理, 数据治理, Agent]
created: 2026-07-28
updated: 2026-07-28
sources:
  - "raw/sources/articles/2026-07-28-GoogleCloudPlatform-Knowledge-Catalog-README.md"
  - "raw/sources/articles/2026-07-28-Open-Knowledge-Format-README.md"
  - "raw/sources/articles/2026-07-28-Open-Knowledge-Format-v0.2-SPEC.md"
  - "https://github.com/GoogleCloudPlatform/knowledge-catalog （检索于 2026-07-28）"
  - "https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md （检索于 2026-07-28）"
  - "https://docs.cloud.google.com/dataplex/docs/catalog-overview （检索于 2026-07-28）"
  - "https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/toolbox/mdcode/demo/okf/okf.ts （检索于 2026-07-28）"
---

# GoogleCloudPlatform Knowledge Catalog 与 OKF — 源摘要

## 来源定位

本组材料包含三个不同对象，必须分开读取：

1. **Google Cloud Knowledge Catalog**：Google Cloud 托管的企业元数据目录与治理服务；
2. **`GoogleCloudPlatform/knowledge-catalog` 仓库**：围绕该产品的工具、Agent 和样例，根 README
   明确声明仓库内容“不是 Google 官方产品”；
3. **Open Knowledge Format（OKF）**：该仓库提出的 Markdown + YAML 知识交换格式。

因此，OKF 位于 GoogleCloudPlatform GitHub 组织下，不等于它已经成为 Google Cloud 产品的原生数据模型，
也不等于已经获得跨厂商标准组织或广泛生产采用的背书。

## Knowledge Catalog 的产品能力

Google Cloud 官方文档把数据资产建模为 `Entry`，用 `Aspect` 承载技术和业务元数据，并支持业务术语、
有类型的 `Entry Link`、搜索、第三方源接入及元数据变更事件流。

综合：它适合充当企业**元数据权威面与治理控制面**；但底层订单、库存、代码和政策正文仍由各自业务系统
负责。目录可以成为 Owner、Glossary、Aspect 等“目录元数据”的权威源，不能自动升级为所有业务事实的
System of Record。

## 仓库的主要构成

| 模块 | 作用 | 边界 |
|---|---|---|
| `samples/discovery` | 对查询做语义拆解、多次目录搜索和结果重排 | 发现 Agent 示例，不是通用编排框架 |
| `toolbox/mdcode` | Metadata as Code：在本地 YAML/Markdown 与托管目录间 pull、diff、push | 使用自己的 catalog/entry 文件布局，不等同于 OKF |
| `toolbox/enrichment` | 通过 Agent、MCP 与 Skills 补充目录元数据 | 依赖目录与 mdcode 工作流 |
| `okf` | v0.2 规范、Reference Agent、样例 Bundle、Viewer | 格式及 PoC，不是托管服务 |

仓库中的 OKF demo 使用自定义 Knowledge Catalog Aspect 做转换。2026-07-28 所读实现主要映射
`type`、`resource`、`generated`、`sources` 以及通用标题、描述、标签和正文；未展示对 `verified`、
`status`、`stale_after` 和完整 Attested Computation 合约的全量往返。

## OKF v0.2 的核心事实

- Bundle 是 Markdown 文件组成的目录树；除保留的 `index.md`、`log.md` 外，一个 `.md` 文件代表一个 Concept。
- Concept ID 是去掉 `.md` 后的 Bundle 相对路径。
- 每个 Concept 由 YAML frontmatter 和 Markdown 正文组成；**唯一始终必需的字段是非空 `type`**。
- `title`、`description`、`resource`、`tags` 只是推荐字段；未知类型和扩展字段必须被宽容处理。
- `sources` 表示来源，正文可用与 `sources[].id` 对应的 Markdown 脚注做逐论断归因。
- `generated` 记录生产者，`verified` 记录核验者；消费者据此派生 unverified、
  machine-confirmed、human-reviewed 三档信任信号。
- `status` 可为 `draft | stable | deprecated`，缺失时默认为 `stable`；`stale_after` 用绝对日期表达过期。
- Concept 通过标准 Markdown 链接形成有向图，但**边没有类型**，关系语义由周围正文说明；断链被允许。
- `index.md` 支持逐层浏览，`log.md` 可记录按日期倒序的更新历史。

## Reference Agent

参考实现分两次处理：

1. BigQuery pass 从 Dataset、Table 与 Schema 元数据生成 Concept；
2. Web pass 从显式种子 URL 开始，在域名、路径、深度和页数限制内爬取，由 LLM 决定补充已有 Concept、
   新建可复用 Reference 或跳过。

其写入提示特别要求保护已有 Schema 和来源，不允许 Web enrichment 用概括性改写缩减 BigQuery
元数据；Metric、Dimension、Join Path 被作为高信号结构优先提取。

综合：这是一个“知识编译器”PoC，而不是通用知识平台。目前代码中的结构化 Source 实现主要面向
BigQuery，格式的供应商中立性不能反推参考 Agent 已具备供应商中立的摄取能力。

## Attested Computation

OKF v0.2 可把批准过的 SQL、dbt、Python 等计算独立建模为 `type: Attested Computation`：

```text
定义与批准的计算
→ Executor 绑定声明过的参数并执行
→ 返回实际执行物与结果的 receipt
→ 无 LLM 的 Attester 做确定性校验
→ 消费者只展示通过校验的值
```

`verified` 核验“定义是否仍符合政策”；attestation 核验“这一次结果是否按批准方式计算”，两者不能替代。
规范同时明确：完整运行协议、receipt/verdict wire format、Attester ABI、沙箱、缓存与语义层模板仍待后续版本。

## 证据边界

- “universal”“vendor-neutral”“trustable”是项目的设计目标，不是市场采用率或安全效果证据。
- `human:<id>` 是 actor 字符串约定，不含身份认证或数字签名；规范也声明信任等级不是访问控制。
- 只有 `type` 的文件也完全合规，且缺失 `status` 会默认稳定；OKF 合规不能等同于内容质量合格。
- Markdown 链接只形成无类型边，不能替代 ontology、RDF/属性图约束或 Knowledge Catalog 的 typed link。
- 路径兼任 Concept ID；目标文件重命名或移动会改变身份并可能破坏外部引用。
- Viewer 把 Bundle 数据嵌入单个 HTML，但 Cytoscape.js 与 marked 从 CDN 加载，因此不是严格离线自包含。

## 可复用论点

这组材料的长期价值不在“Google 发布了一个新格式”，而在于两个可复用判断：

1. **托管目录和可携带知识制品是两类东西**：前者负责治理、权限、搜索和变更；后者负责可读、可审、
   可版本化和跨系统交换。
2. **知识可信度与计算可信度必须分开**：来源、生产者、核验者和保鲜期描述知识定义；
   Attested Computation 再证明某次结果遵循批准过的计算过程。

详见 [[Open Knowledge Format]] 与 [[OKF 与 llm-wiki 的关系]]。

## 关联页面

- [[知识图谱]]
- [[Agent 记忆架构]]
- [[从知识图谱到 Agent 编排]]
- [[基于IT4IT的Agent知识治理]]
- [[llm-wiki-方法论]]
