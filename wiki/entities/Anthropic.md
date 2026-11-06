---
tags: [实体, 公司, AI, 投资标的]
created: 2026-07-03
updated: 2026-11-06
sources:
  - "https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm （检索于 2026-11-06）"
  - "https://claude.com/resources/articles/cowork-is-now-claude （检索于 2026-11-06）"
  - "https://claude.com/resources/articles/claude-duet （检索于 2026-11-06）"
  - "https://www.anthropic.com/product/claude-cowork （检索于 2026-07-03）"
  - "https://www.anthropic.com/news/google-broadcom-partnership-compute （检索于 2026-07-16）"
  - "[[2026-02-03-Reuters-AI担忧重挫欧洲软件股-源摘要]]"
  - "[[2026-07-21-Anthropic-AI原生SDLC-源摘要]]"
  - "[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]"
---

# Anthropic

AI 公司，Claude 系列大模型的开发者。既是**技术实体**（模型、agent、协议标准的推动者），
也是**投资/商业研究标的**（其产品发布正在重塑软件行业的估值逻辑）。

## 关键产品/资产
- **Claude** 系列大模型（本 wiki 记录到 Opus 4.6 及以后）。
- **[[Claude Cowork]]**：面向非技术知识工作者的 agent 能力。2026-02 引爆软件股抛售；2026-09-16 起并入 Claude，成为默认执行层。常驻形态分为 Claude Tag（Slack，2026-06 起 beta）和 Claude Duet（独立 App，2026-10 起 research preview）。与 Grok Bot、Muse、Dots 的竞争格局见 [[常驻 AI 同事的竞争格局]]。
- **[[Claude Code]]**：面向开发者的 agentic 编码工具。
- **[[MCP]]（Model Context Protocol）**：2024-11 开源的 agent↔数据/工具连接开放标准。
- 研究：[[building-effective-agents]]（agent 设计范式）。

## 商业动态
- 2026-04-06，Anthropic 官方称其 **run-rate revenue 已超过 $30bn**，高于 2025 年底约 $9bn；
  同期年化支出超过 $1m 的企业客户从 2 月的 500+ 增至 1,000+。
  （https://www.anthropic.com/news/google-broadcom-partnership-compute ，检索于 2026-07-16）
- 口径边界：run-rate revenue 是按当前收入速度年化，不等同于经审计年度收入，也不宜无说明地写成 ARR。
- 2026-10-26 提交 S-1，11-02 提交 S-1/A。S-1 称 Cowork 的采用速度超过 Claude Code 同期；年支出 $100K 以上的客户中，超过一半同时使用 Claude Platform 和至少一个第一方应用（2025 年第四季度约为 30%）。S-1 不按产品拆分收入。
- 渠道竞合：Microsoft Copilot Cowork 采用 Claude Cowork 的执行框架，但 Microsoft 同时加入 GPT 和 Grok 模型对冲，管理员可以关闭 Anthropic 模型族。在 Microsoft 体系里，Anthropic 正从"技术来源"退为"可替换的模型供应商之一"（推断，见 [[常驻 AI 同事的竞争格局]]）。

> ⚠️ 溯源修正：旧版把 $9bn → $30bn 归入 2026-02-03 Reuters/UBS 来源；该时间线不成立，
> 已改引 Anthropic 2026-04-06 官方公告。原 raw 重建稿只读保留，矛盾见
> [[2026-02-03-Reuters-AI担忧重挫欧洲软件股-源摘要]]。（发现于 2026-07-16）

## 影响
- 其 2026-02 的 [[Claude Cowork]] 插件发布被 Reuters 称为软件业的 "wake-up call"，
  详见 [[cowork-saas-资本市场冲击]]。

## AI 原生软件工程

- 2026-07，Anthropic 公开其内部 AI 原生 SDLC：截至 5 月约 80% 的已合并生产代码行归因于 Claude，
  同时用风险分级、确定性检查、隔离环境、独立身份、人工门禁和 SIEM 约束生成、审查与事故响应。
- 口径边界：80% 是公司自报的代码行归因，不是 80% 的工程判断或部署权限自动化；完整分析见
  [[Anthropic-AI原生SDLC治理循环]]。
- 同月 Claude Code 团队称，其内部 Claude Tag 提交该团队 **65% 的产品工程 PR**；核心区域仍由 code owner
  人工批准，外围变更经过六个多月的验证后才逐步交给自动 review。65% 只覆盖 Claude Code 产品工程团队，
  也是员工自报口径，不代表全公司 PR 比例或无人审查比例。→ 见
  [[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]，完整流程分析见
  [[Claude Tag 驱动的团队研发流程]]。
