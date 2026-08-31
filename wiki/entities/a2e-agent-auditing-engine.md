---
tags: [实体, AI, Agent, Evals]
created: 2026-08-10
updated: 2026-08-31
sources:
  - "[[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]"
  - "https://github.com/datamllab/A2E （检索于 2026-08-10；GitHub API 复查于 2026-08-31）"
  - "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository （检索于 2026-08-10）"
renders: []
---

# A²E（Agent Auditing Engine）

A²E 是上海人工智能实验室于 2026-08-07 发布的 agent harness 评测引擎预印本及公开参考实现（代码以 MIT 许可公开，见下方证据边界）。它由 Task、Monitor、Evaluation 三层组成，支持 Agno、AutoGen AgentChat、CrewAI、Google ADK、LangGraph、LlamaIndex、OpenAI Agents SDK、Smolagents 和 Anthropic/Claude Agent SDK 等 harness。

关键机制包括 [[agent-task-protocol|ATP]]、OpenTelemetry/OpenInference 风格的 span trace、[[lifecycle-aligned-evaluation]] 与可重评的结构化存储。论文实验显示，同一模型在不同 harness 上的多轮成功率、token 使用和终止行为可出现明显差异，因此 harness 不应被当作“轻量 wrapper”。

> 证据边界（2026-08-31 复查）：仓库已于 2026-08-12 补入 MIT LICENSE（Copyright (c) 2026 Shanghai AI Lab），但仍无 release、无 tag，最近提交停在 2026-08-18（GitHub API `repos/datamllab/A2E` 及其 `/releases`、`/tags`，检索于 2026-08-31）。**许可障碍已消除**：MIT 明确授予复制、修改与再分发权，2026-08-10 首次记录的「未声明 license，依 GitHub 官方许可指南不应默认获得复制、再分发或衍生使用权」已不再成立。综合：无版本化发布这一条仍在，现阶段仍适合隔离 POC 和方法参考，不是已验证的生产组件。

详见 [[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]] 与 [[Agent 全轨迹评测与审计]]。
