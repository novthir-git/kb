---
tags: [概念, AI, Agent, 审计, Evals]
created: 2026-08-10
updated: 2026-08-10
sources:
  - "[[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]"
renders: []
---

# Agent Auditing

Agent Auditing 是对 agent 系统的**结果、执行过程与运行边界**进行可重复检查的方法。其对象是模型、harness、工具、任务环境和权限策略组成的整体，不是只检查最终文本。

最小证据链是：`Task Contract → Trace/Outcome → 版本化 Grader → 审计记录`。其中 outcome 证明任务是否真实完成，trace 支持失败归因和成本/安全审查，二者不可互相替代。

[[a2e-agent-auditing-engine|A²E]] 是一个参考实现；更完整的可复用契约、最小落地与证据边界见 [[Agent 全轨迹评测与审计]]。
