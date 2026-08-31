---
tags: [实体, 产品, AI, Agent, 软件工程]
created: 2026-08-11
updated: 2026-08-31
sources:
  - "[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]"
  - "https://simonwillison.net/2026/Jul/21/cat-and-thariq/ （检索于 2026-08-03）"
  - "https://docs.anthropic.com/zh-CN/docs/claude-code/memory （检索于 2026-08-07）"
  - "[[2026-08-27-Uber-软件工厂成本效率-源摘要]]"
renders: []
---

# Claude Code

[[Anthropic]] 面向开发者的 agentic 编码工具与平台：以终端/CLI 为主要界面，让 agent 在代码库中
自主读写、执行、测试并迭代。与 [[Codex]] 同类。本 wiki 不追它的功能更新，只沿三条线追踪其**判断价值**。

## 线 1：agentic coding loop 的加速器

- 在 [[Loop Engineering]] 的三层循环中，它加速的是分钟级 agentic coding loop，从而把人的工作
  上移到规格、[[Evals|evals]] 与产品判断——瓶颈从写代码迁移到设计循环。
- 其产品设计本身是 agent 工程的一手样本（[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要|团队访谈]]）：
  前沿模型的系统提示缩短约 80%（旧模型保留完整提示，不可外推为通用法则）；工具数收敛
  （grep/glob 归入原生 Bash）；文件编辑工具因可确定性渲染 diff 而保留——**工具同时服务模型、用户与审计**。

- **harness 的默认值本身是成本杠杆**：Uber 在自建统一包装层里把压缩阈值设为 400K（即便模型有 1M
  上下文）、reasoning effort 默认 Medium、交互 session 的 prompt 缓存 TTL 从 5 分钟改为 1 小时
  （子 agent 保持 5 分钟）、**子 agent 默认弱模型**（其称之为交互侧最有效的单一杠杆），
  并在 status line 挂实时花费计数器（[[2026-08-27-Uber-软件工厂成本效率-源摘要]]）。
  综合：这是一份来自外部大型企业的一手证据，说明 **harness 的可配置面同时是成本控制面**——
  与 [[harness-vs-model]] 的判断一致，也解释了为什么企业倾向在官方 CLI 外再包一层。
  完整语境见 [[Uber-软件工厂的成本工程]]。

## 线 2：Anthropic 内部 AI 原生 SDLC 的载体

- 团队内部以 Claude Tag（Slack 中的团队级常驻协作层）+ Claude Code（个人复杂任务的交互式执行）分工，
  完整流程模型见 [[Claude Tag 驱动的团队研发流程]]。
- Claude Tag 提交该团队 **65% 的产品 PR**。口径边界：员工自报，且仅指 Claude Code 产品工程团队，
  不是全 Anthropic 数据，也不是无人审查比例。
- 分层审查：系统提示等核心区域保留 code owner 人工批准；外围文件经六个多月 shadow mode 验证后
  才逐步交给自动 review。放权单位是**文件范围 × 风险等级 × 回归证据**，不是全局开关。
- Eval 驱动：新模型替换前跑产品级 eval；事故致因 PR 转为 eval 用例回灌 reviewer。
  治理侧全景见 [[Anthropic-AI原生SDLC治理循环]]。

## 线 3：本仓库自身的维护工具

- Claude Code 是本 wiki `wiki/` 目录的**唯一写手**（本仓库 `AGENTS.md` 铁律），承担
  [[llm-wiki-方法论]] 的 Ingest / Query / Lint 三大操作——本仓库即"用 agent 维护语义记忆"的活体实验。
- 其 `CLAUDE.md` 记忆文件机制对应 [[AI编码技术债的三层治理]] 的意图层：承载项目特定、可执行的约定，
  但只能提高遵循概率，硬约束仍须落在门禁。
- [[STORM-研究提示词组]] 的多视角检索阶段可在 Claude Code 中用 subagent 并行执行，是最接近
  原系统并行架构的手工执行方式。

## 与 Claude Cowork 的分界

[[Claude Cowork]] 面向**非技术知识工作者**的通用 agent 场景；Claude Code 面向开发者与工程流程。
综合：两者共享同一 agent 能力栈，分界在界面与治理对象——前者的冲击面是 SaaS 资本市场
（见 [[cowork-saas-资本市场冲击]]），后者的冲击面是软件工程组织方式。

## 关联页面

- [[Anthropic]] / [[Claude Cowork]] / [[Codex]]
- [[Claude Tag 驱动的团队研发流程]] / [[Anthropic-AI原生SDLC治理循环]]
- [[Loop Engineering]] / [[Evals]] / [[AI编码技术债的三层治理]]
- [[llm-wiki-方法论]] / [[STORM-研究提示词组]]
- [[生产力-体验悖论]] / [[agent-生产级落地的鸿沟]]
