# Wiki Schema（知识库配置规范）

> 本文件是运行时配置摘要；具体维护铁律以 `AGENTS.md` 为准。若两者冲突，优先遵守 `AGENTS.md`，并同步修正本文件。
> 意图与范围（为什么存在、该问什么）见 `wiki/purpose.md`，本文件不重复。

## 知识库信息

- 主题：个人知识 Wiki
- 创建日期：2026-04-07
- 语言：中文
- 版本：1.3（2026-07-29 布局适配 llm_wiki 桌面应用）

## 三层架构

1. `raw/`：原始信息源，只读；研究中新增的重要网页可存入 `raw/sources/articles/`，存入后同样只读。
2. `wiki/`：AI 维护的结构化知识层；可新建、改写、合并、横向整合。
3. `AGENTS.md` / `wiki/schema.md` / `wiki/purpose.md`：规则与意图层。`AGENTS.md` 是完整 schema 且唯一权威；
   本文件是运行时摘要，供通用 llm-wiki 工具识别语言与路径；`purpose.md` 定义目标、关键问题与范围。

## 目录结构

```text
llm-wiki/
├── raw/
│   ├── sources/           # 素材总根（第三方工具硬编码此路径）
│   │   ├── articles/      # 网页文章与研究中值得存档的重要网页
│   │   ├── pdfs/          # 论文、报告 PDF
│   │   └── notes/         # 用户笔记
│   └── assets/            # 图片、SVG 等附件
├── wiki/
│   ├── index.md           # 内容目录（聚合文件，不是页面）
│   ├── log.md             # append-only 操作日志（聚合文件）
│   ├── purpose.md         # 目标、关键问题、范围、核心论断（配置文件）
│   ├── schema.md          # 本文件（配置文件）
│   ├── overview.md        # 全局知识版图，保持 60 行以内（页面）
│   ├── sources/           # 源摘要页；按需创建，不强制 raw 1:1
│   ├── entities/          # 人物、公司、产品、工具、机构
│   ├── concepts/          # 概念、方法论、技术原理
│   ├── topics/            # 长期论题；用证据点表持续累积
│   ├── comparisons/       # 多方案、多工具、多观点对比
│   ├── analyses/          # 一次研究问答沉淀出的深度分析
│   └── synthesis/         # 演化中的综合观点与判断
├── briefs/                # 每日简报（时效性阅读层，不入索引、不计数）
├── output/                # 交付层：对外分享的单文件 HTML；非知识资产，不进 lint（详见 AGENTS.md）
│   ├── personal/          # 自用：稳定文件名，可原地重渲染
│   └── shared/            # 对外：带日期，发出即冻结，不得原地覆盖
├── AGENTS.md              # 完整 schema（CLAUDE.md 是其 symlink）
├── purpose.md             # → wiki/purpose.md（symlink）
└── schema.md              # → wiki/schema.md（symlink）
```

`wiki/` 根下 `index.md`、`log.md`、`purpose.md`、`schema.md` 为聚合/配置文件，不计入页面数、不进 index 条目；
`overview.md` 计入页面数。

## 页面类型选择

- 一次研究问答的深度产出：写入 `wiki/analyses/`。
- 会跨多源、持续追加证据的长期论题：写入 `wiki/topics/`，使用证据点表。
- 演化中的立场、判断、知识版图：写入 `wiki/synthesis/` 或更新 `wiki/overview.md`。
- 人物、公司、产品、工具、机构：写入 `wiki/entities/`。
- 技术概念、方法论、投资主题中的可复用概念：写入 `wiki/concepts/`。
- 多方案/多观点比较：写入 `wiki/comparisons/`。
- 源摘要：写入 `wiki/sources/`；research 存档的网页仅当被 ≥2 个 wiki 页引用，或本身值得独立摘要时创建。

## 命名与链接

- 正文语言用中文；术语、人名、公司名保留原文。
- 页面间使用 Obsidian 双链：`[[页面名]]` 或 `[[页面名|显示名]]`。
- 全库文件名必须唯一，避免 Obsidian 双链解析歧义。创建 `wiki/sources/` 摘要页时，如果 raw 已有同名文件，使用 `-源摘要` 后缀。
- 重命名或合并页面后，必须全库搜索旧页名并更新入链；或保留一行 stub 指向新页。
- 悬空链接可以作为有意的待写标记，但必须在页面里明确标注“待写”或“待创建”。

## 页面格式

每个 `wiki/` 页面都必须以 YAML frontmatter 开头：

```yaml
---
tags: [分析]
created: 2026-07-03
updated: 2026-07-03
sources:                        # 必须用块状列表，不用行内数组
  - "[[某源摘要页]]"
  - "https://example.com （检索于 2026-07-03）"
---
```

行内数组 `sources: ["[[页]]", ...]` 会被第三方工具的解析器在第一个 `]` 处截断、丢失其余条目；
块状列表解析正常。全库现有页面均为块状列表。

- 编辑任何 wiki 页面，都要同步 bump `updated` 字段。唯一例外：纯机械迁移（批量路径改写、格式统一）不 bump，
  改为在 `wiki/log.md` 记 `schema` 条目说明范围——避免把"这页有新判断"变成噪音。
- 每个关键论断必须可溯源：双链指向源摘要页，或 URL + 检索日期。
- 综合推断显式标注“综合：”。
- 矛盾必须显式标注：`> ⚠️ 矛盾：[[源A]] 称 X，但 [[源B]] 称 Y。（发现于 2026-07-03）`
- `topics/` 证据点表统一表头：`| 日期 | 来源 | 信号 | 备注 |`。
- `wiki/overview.md` 的 `sources` 只列外部 URL，不罗列内部页面（避免与正文双链、index 形成三份副本）；
  无外部来源时写 `sources: []`。
- `renders:` 字段自 2026-08-31 废止：不再新增、不再校验；存量字段留着无害。

## Query & Research

1. 先读 `wiki/index.md` 定位相关页面，再读相关 `wiki/` 页面。
2. 已有沉淀足够时直接回答；不够时联网 research。
3. 回答必须可溯源：wiki 内容用双链，联网内容注明 URL 与检索日期。
4. 回答后评估沉淀价值：先对照 `wiki/purpose.md` 的范围与关键问题，再看沉淀标准。值得沉淀时提醒用户确认。
5. 用户确认后写入合适的 `wiki/` 页面，横向更新相关 entity/concept/topic，必要时存档重要网页到 `raw/sources/articles/`，并更新 `wiki/index.md`、`wiki/overview.md`、`wiki/log.md`。

## Ingest

1. 通读新源；图片先读文本，再逐张查看引用的本地图片。
2. 生成 `wiki/sources/` 摘要页。
3. 横向整合到相关实体、概念、主题、分析页。
4. 必要时新建页面，新页面必须至少有一条入链。
5. 更新 `wiki/index.md`、`wiki/overview.md`（若知识版图有变）、`wiki/log.md`。

## Lint

检查并报告：

- 页面间矛盾、过时论断、缺失来源。
- 孤儿页、意外断链、缺失交叉引用。
- 重名文件（全库文件名唯一）。
- `wiki/index.md` 条目与实际 `wiki/` 文件是否一致；概览计数是否与
  `find wiki -name '*.md' -not -name 'index.md' -not -name 'log.md' -not -name 'purpose.md' -not -name 'schema.md' | wc -l` 一致。
- 路径引用有效性：wiki 页中的 `raw/sources/...` 引用是否指向真实文件；根目录 `purpose.md`、`schema.md` symlink 是否可解析。
- `wiki/overview.md` 是否 ≤ 60 行。
- `topics/` 证据点表是否使用统一表头。
- URL 引用是否可达；访问受限但已有替代溯源说明的不算死链。

`output/` **不在 lint 范围内**：它是交付层不是知识层，不检查新鲜度、meta 或登记。
唯一相关的是判断类的一条——对外原创稿的可复用论点是否已在 wiki 有对应页（查的是 wiki 的完整性）。

Lint 结果经用户确认后再修复；lint 与修复都记入 `wiki/log.md`。

## wiki/index.md 与 wiki/log.md

- `index.md` 顶部只维护 raw 总数、wiki 页面总数、最后更新日期；不维护分类明细计数。
- 每个 wiki 页面按类别一行：`- [[页面名]] — 一句话描述`。
- `log.md` append-only；research / ingest / lint / output / schema 五类必记，纯 query 默认不记。
- log 前缀固定：`## [YYYY-MM-DD] research|ingest|lint|output|schema | 标题`。

## 第三方工具兼容

布局已适配 nashsu/llm_wiki 桌面应用（可直接作为 project 打开，用其图谱与检索）。
**Claude Code 是 `wiki/` 的唯一写手，不得使用该 App 的 ingest 写入。** 详细约束见 `AGENTS.md`「第三方工具兼容」。
