---
tags: [实体, 产品, AI, Agent]
created: 2026-07-03
updated: 2026-08-31
sources:
  - "https://www.anthropic.com/product/claude-cowork （检索于 2026-07-03）"
  - "https://support.claude.com/en/articles/13837440-use-plugins-in-claude （检索于 2026-07-16）"
  - "https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp （检索于 2026-07-16）"
  - "[[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要]]"
---

# Claude Cowork

[[Anthropic]] 的 agentic AI 产品，围绕"**结果（outcome）**"而非单条 prompt 设计：
用户下达目标、收到成品交付，而不必逐步指挥。

## 核心能力（四大工作流）
1. 整理/管理本地文件（重命名、排序、去重）。
2. 从素材综合、装配、准备文档。
3. 跨多源综合复杂研究。
4. 从合同/报告等非结构化文件抽取结构化数据。

## 与 chatbot 的区别
- 能**在本地文件与应用间移动**、跨源综合、**无需用户协调每一步**即完成任务；
- 桌面端之外，**web / mobile 也可运行云端会话**；本地文件与应用等本地能力依赖 desktop bridge
  （Anthropic 官方资料与帮助中心 2026-07-07 起口径，经 2026-08-04 lint 核验，见 wiki/log.md）。
- 通过**插件**连接 legal、sales、marketing、data analysis 等外部系统（依托 [[MCP]]）。

## 定位与目标用户
面向 researchers、analysts、operations、legal、finance 等**非技术知识工作者**——
"工作日里那些耗时但技术上不复杂的任务"。

## 安全边界
"完成任务，但**consequential decisions 仍留给用户**"——保留人类监督。

## 可用性
面向所有付费计划：web / mobile 可发起并运行**云端会话**；操作本地文件与应用等本地能力
依赖 Claude 桌面应用的 desktop bridge（Anthropic 官方资料与帮助中心 2026-07-07 起口径，
经 2026-08-04 lint 核验，见 wiki/log.md）。

## 市场影响
- 2026-02 其插件发布触发全球软件股抛售，见 [[cowork-saas-资本市场冲击]]。

## 插件体系架构
- Plugin 是 **[[Agent Skills|skills]] + connectors + sub-agents** 的可安装能力包，不等于 MCP Server。
- Connector 负责接外部服务；custom connector 可指向 remote MCP server，plugin 也可能携带 local MCP server。
- 校正后的分层图与对外讲解见 [[cowork-plugins-架构]]。

## 同类范式：OpenAI Codex
- [[Codex]] 与 Cowork 是"agent 替代/放大知识工作"范式的两极：Cowork 从非技术知识工作者切入，
  Codex 从开发者起步再向非开发者外溢（自 2025-08 非开发者用户增长百倍量级）。
  采用数据见 [[codex-agent-采用曲线]]，其体验成本见 [[生产力-体验悖论]]。

## 历史
- 发布初期（2026-07-03 检索口径）：仅在所有付费计划的 Claude 桌面应用中提供，
  对外定位强调"运行在桌面端——知识工作真正发生的地方"。2026-07-07 起官方口径更新为
  web / mobile 可运行云端会话、本地能力依赖 desktop bridge（见上方"可用性"）。

## 命名与对外话术
- 对外与内部一律使用官方名 **Cowork**（Claude Cowork），不使用任何自定义别名。
- 底层机制始终是"Agent 编排 + [[MCP]] 连接"；对外表述 MCP 时应说"采用开放标准 MCP"。
- 演示素材：架构图 `raw/assets/cowork-plugins-mcp-architecture.svg`（已因"plugin = MCP Server"
  错误废弃，仅供追溯），现行承载页 [[cowork-plugins-架构]]。
