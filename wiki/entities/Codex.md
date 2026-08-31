---
tags: [实体, 产品, AI, Agent]
created: 2026-07-03
updated: 2026-07-16
sources:
  - "[[2026-06-25-Axios-Codex-agent-用量增长-源摘要]]"
  - "[[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]"
  - "https://arxiv.org/html/2606.26959v1 （检索于 2026-07-03）"
---

# Codex

OpenAI 的 **agentic 编码 / 工作平台**。最初面向开发者做"自主写代码/改代码"的 coding agent，
2026 年起定位外扩为**通用 agent 工作平台**——用户下达目标，Codex 派出（可并行的）agent
自主执行、交付结果。

## 关键特征
- **并行 agent**：重度用户把任务拆给多个并行 agent 同时跑；99 分位用户单日可累计
  **60+ 小时** agent turns（[[2026-06-25-Axios-Codex-agent-用量增长-源摘要]]）。
- **非开发者外溢**：增长最快的是律师、招聘等非技术岗位（同源，见 [[codex-agent-采用曲线]]）。
- **产品开发循环基础设施**：在 [[Loop Engineering]] 视角里，Codex 这类 coding agent 承担分钟级
  agentic coding loop；它把产品规格 / [[Evals|evals]] 变成可反复执行、测试、观察和修正的工程循环
  （[[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]）。
- **SDD 执行器**：在 [[Specification-Driven Development]] 中，Codex 可依据 requirements / design / tasks
  实现并验证变更；但 current spec、风险接受与验收责任仍需由团队治理，参见 [[SDD 开发规范研究]]。

## 与本 wiki 的关联
- **采用数据**见分析页 [[codex-agent-采用曲线]]。
- **对从业者体验的影响**——工作从"写"转向"监督/验证"——见概念 [[生产力-体验悖论]]。
- 与 [[Anthropic]] 的 [[Claude Cowork]] 构成**同一"agent 替代/放大知识工作"范式的两极**：
  Cowork 主打非技术知识工作者，Codex 从开发者起步再向非开发者外溢——参见
  [[cowork-saas-资本市场冲击]] 的范式切换主线。
- 底层能力范式参见 [[building-effective-agents]]（orchestrator-workers、并行化）。
- 方法论视角参见 [[Loop Engineering]]。
