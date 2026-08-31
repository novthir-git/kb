---
tags: [概念, AI, Agent, Evals, 协议]
created: 2026-08-10
updated: 2026-08-31
sources:
  - "[[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]"
renders: []
---

# Agent Task Protocol（ATP）

ATP 是 [[a2e-agent-auditing-engine|A²E]] 内部的**软件接口协议**，不是网络协议或行业标准。它用 `TaskInput`、`AgentBinding`、`AgentRunner`、`TaskTrace` 分离 benchmark 适配与 harness 执行，让 m 个 benchmark 和 n 个 harness 通过共享边界组合，而非维护 m×n 个成对适配器。

可复用的设计点是把**任务语义**、**工具/环境绑定**、**harness 原生控制循环**和**标准化运行结果**分开。但 registry 中有适配器不等于所有 benchmark×harness 组合都已通过端到端验证。在 [[Agent 全轨迹评测与审计]] 的 Task Contract 中，ATP 被作为一种实现引用，而非唯一标准。
