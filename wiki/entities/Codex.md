---
tags: [实体, 产品, AI, Agent]
created: 2026-07-03
updated: 2026-11-07
sources:
  - "[[2026-06-25-Axios-Codex-agent-用量增长-源摘要]]"
  - "https://learn.chatgpt.com/docs/dots.md （检索于 2026-11-06）"
  - "https://venturebeat.com/technology/openai-launches-dots-always-on-ai-agent-coworkers-and-chatgpt-space-where-they-can-collaborate-with-human-teams （检索于 2026-11-06）"
  - "[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]"
  - "[[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]"
  - "https://arxiv.org/html/2606.26959v1 （检索于 2026-07-03；2026-11-07 全文复核）"
---

# Codex

OpenAI 的 **agentic 编码 / 工作平台**。最初面向开发者做"自主写代码/改代码"的 coding agent，
2026 年起定位外扩为**通用 agent 工作平台**——用户下达目标，Codex 派出（可并行的）agent
自主执行、交付结果。

## 关键特征
- **并行 agent**：重度用户把任务拆给多个并行 agent 同时跑；**OpenAI 员工** 99 分位单日累计约
  **71 小时** agent turns，外部用户显著更低（底层论文 https://arxiv.org/html/2606.26959v1 ，检索于 2026-11-07；
  Axios 重建稿泛写成"99 分位用户 60+ 小时"，口径差异见 [[2026-06-25-Axios-Codex-agent-用量增长-源摘要]]）。
- **非开发者外溢**：增长最快的是律师、招聘等非技术岗位（同源，见 [[codex-agent-采用曲线]]）。
- **产品开发循环基础设施**：综合：Ng 原文没有提 Codex（开篇点名的是 [[Claude Code]] 作者 Boris Cherny 与 OpenClaw 作者 Peter Steinberger），
  但按 [[Loop Engineering]] 的框架，Codex 这类 coding agent 同样承担分钟级
  agentic coding loop；它把产品规格 / [[Evals|evals]] 变成可反复执行、测试、观察和修正的工程循环
  （[[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]）。
- **零手写代码实验的执行者**：OpenAI 内部团队 2025-08 下旬起五个月不手写代码，用 Codex 做出约 100 万行、
  约 1,500 个 PR 的内部 beta 产品；单次运行常在单个任务上持续 6 小时以上。团队的结论是瓶颈在环境而非模型，
  并据此提出 [[Harness Engineering]]（[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]；全部为公司自报，无对照）。
- **SDD 执行器**：在 [[Specification-Driven Development]] 中，Codex 可依据 requirements / design / tasks
  实现并验证变更；但 current spec、风险接受与验收责任仍需由团队治理，参见 [[SDD 开发规范研究]]。

- **常驻 agent 的执行层**（2026-09 起）：OpenAI 2026-09-29 发布的常驻 agent **Dots** 可以把长任务派给 Codex 云任务和 ChatGPT Work。Dots 发起的任务计入 Codex/Work 的常规额度，与 dot 自身的对话额度分开计算。综合：dot 是人格化的前台和编排层，Codex 是执行层。产品演进路线是 Operator → ChatGPT agent → ChatGPT Work / Codex 云代理 → Dots，见 [[常驻 AI 同事的竞争格局]]。

## 与本 wiki 的关联
- **采用数据**见分析页 [[codex-agent-采用曲线]]。
- **编码侧的直接同类**是 Anthropic 的 [[Claude Code]]：两者都是面向开发者的 agentic 编码工具。
- **对从业者体验的影响**——工作从"写"转向"监督/验证"——见概念 [[生产力-体验悖论]]。
- 与 [[Anthropic]] 的 [[Claude Cowork]] 构成**同一"agent 替代/放大知识工作"范式的两极**：
  Cowork 主打非技术知识工作者，Codex 从开发者起步再向非开发者外溢——参见
  [[cowork-saas-资本市场冲击]] 的范式切换主线。
- 底层能力范式参见 [[building-effective-agents]]（orchestrator-workers、并行化）。
- 方法论视角参见 [[Loop Engineering]]。
- 长期运行下代码库的熵增与 OpenAI 的"垃圾回收"做法，见 [[Agent 不会自发偿还结构债]]。
