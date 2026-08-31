---
tags: [概念, AI, Agent, 方法论, 产品]
created: 2026-07-03
updated: 2026-08-11
sources:
  - "[[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]"
  - "[[Evals]]"
  - "https://x.com/AndrewYNg/status/2071988145667928442 （检索于 2026-07-03；X 正文动态渲染，全文以用户粘贴原文入库）"
---

# Loop Engineering

**Loop Engineering** 是围绕 AI agent 设计反馈闭环的工程方法：不把 agent 当成一次性回答器，而是让它在目标、行动、观察、评估与修正之间持续迭代，直到满足规格、触发停止条件，或需要人类注入新上下文。

在 Andrew Ng 的三层产品开发框架里，Loop Engineering 同时覆盖"怎么做软件"和"决定做什么软件"（[[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]）。

## 三层产品开发循环

| 循环 | 核心接口 | 时间尺度 | 人/agent 分工 |
|---|---|---|---|
| Agentic coding loop | 产品规格 / [[Evals|evals]] ↔ coding agent | 分钟级 | agent 写代码、测试、用浏览器检查并迭代 |
| Developer feedback loop | 开发者愿景 ↔ 产品规格 / [[Evals|evals]] | 小时级 | 人检查产品、调整愿景、澄清规格、决定功能/UI/用户流 |
| External feedback loop | 外部反馈 ↔ 开发者愿景 | 天到周级 | 用户、朋友、alpha、A/B 测试等真实反馈修正产品方向 |

## 关键判断

- **瓶颈从写代码转向设计循环**：coding agent 越能自测自修，人的工作越从手工 QA 上移到规格、[[Evals|evals]]、产品判断与反馈节奏设计。
- **[[Evals]] 是规格的硬化形式**：当 agent 反复出同类错时，应把问题固化成 evals，让循环自动吸收反馈，而不是依赖下一轮人工提醒。
- **人的价值是 context advantage**：Andrew Ng 将常被称为"品味"的人类贡献，改写成"人比 AI 更知道用户和场景"。这个说法更可操作，因为它指出了人类需要向系统注入什么。
- **外部反馈没有被自动化消灭**：AI 加速的是构建速度，不会自动生成真实用户需求。0-to-1 产品仍要在构建与获取外部反馈之间平衡。

## 与已有页面的关系

- [[building-effective-agents]] 描述的是 agent/workflow 的底层模式；Loop Engineering 更像把这些模式放进可运行、可验证、可停机的产品开发系统。
- [[Specification-Driven Development]] 把本页的“规格 / [[Evals|evals]] ↔ coding agent”接口固化为可版本化的
  requirements、design、tasks 与 verification 链；团队级门禁见 [[SDD 开发规范研究]]。
- [[Claude Tag 驱动的团队研发流程]] 把三层循环落到团队工作面：协作频道承接信号，Claude Tag 负责常驻协调与
  常规执行，Claude Code 处理复杂交互，风险门禁、内部试用和事故回灌把团队反馈与生产反馈接回 coding loop。
- [[Codex]]、[[Claude Code]] 这类工具让 agentic coding loop 变快，进而把开发者推向更高层的产品循环。
- [[生产力-体验悖论]] 提醒：从"写"到"监督/验证"会带来认知负荷。Loop Engineering 的正面版本，是把人从低层 QA 解放出来，让其上下文优势进入产品愿景与外部反馈循环。
- [[agent-生产级落地的鸿沟]] 的核心问题之一，是 Demo 常只有局部闭环；生产落地需要把 [[Evals|evals]]、权限、真实用户反馈和人工判断都纳入循环。

## 待追踪

- Boris Cherny、Peter Steinberger、Addy Osmani 对 Loop Engineering 的原始论述与 Andrew Ng 框架之间的差异。
- 不同 agent 产品（[[Codex]]、Claude Code、OpenClaw）如何把 loop 变成内建能力，而不是用户手写脚本。
- 适合 0-to-1 产品的 [[Evals|evals]] 应该如何设计：功能正确性、用户体验、学习效果、留存/转化等指标是否应分层。
