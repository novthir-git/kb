---
tags: [概念, AI, Agent, 方法论]
created: 2026-07-03
updated: 2026-07-29
sources:
  - "https://www.anthropic.com/engineering/building-effective-agents （检索于 2026-07-28）"
  - "[[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]"
---

# Building Effective Agents（Agent 设计范式）

[[Anthropic]] 的研究文章，为构建有效 agent 提供一套分类与设计原则。

## 核心区分：Agent vs Workflow
- **Workflow**：LLM 与工具被**预定义的代码路径**编排。
- **Agent**：LLM **动态自主**决定自己的流程与工具选择，自行决定如何完成任务。

## 基石：Augmented LLM
增强了**检索、工具、记忆**能力的 LLM——能主动生成查询、选择工具、管理信息留存。

## Workflow 模式（复杂度递增）
1. **Prompt chaining**：拆成顺序步骤，程序化 checkpoint 校验。
2. **Routing**：分类输入并路由到专门的下游流程。
3. **Parallelization**：并行多次调用（sectioning 分工 / voting 投票）。
4. **Orchestrator-workers**：中央 LLM 动态拆解不可预测的任务、委派 worker、再综合。
5. **Evaluator-optimizer**：一个 LLM 生成、另一个评估反馈，迭代精修。

### Orchestrator-workers 的边界

Anthropic 把 orchestrator-workers 放在 **Workflow** 类，而不是把它定义成多个完全自主 Agent 的必然组合。
中央 LLM 可以动态决定子任务，但预算、并发、权限、终止条件和 checkpoint 仍可由确定性代码控制。
固定子任务也不需要包装成 Agent；普通函数、队列消费者、[[RPA]] 或 API 调用通常更简单。

## 何时用 agent
适合**开放式、解法路径不可预测**、需要高度自主的问题；但成本更高、错误会累积，
需强测试、沙箱与护栏。

## 三条设计原则
- **Simplicity**（最小化架构复杂度）
- **Transparency**（显式暴露规划步骤）
- **Interface Design / ACI**（像重视 HCI 一样重视 agent-computer interface 与工具文档）

## 与本 wiki 的关联
- 这套范式是 [[Claude Cowork]] 能"端到端完成一段工作"的能力层基础，
  参见 [[cowork-saas-资本市场冲击]] 的"能力层"分析。
- **orchestrator-workers / parallelization** 是 [[Codex]] 重度用户"一人调度多并行 agent、
  单日 60+ 小时 agent turns"的能力底座，见 [[codex-agent-采用曲线]]。
- **evaluator-optimizer** 与人类护栏对应工作从"创造转向验证"的趋势——但该转向也有代价，
  见 [[生产力-体验悖论]]。
- [[Loop Engineering]] 可看作把本页的 workflow/agent 模式放进产品开发节奏：分钟级 coding loop、
  小时级开发者反馈、天/周级外部反馈，三层循环共同把 agent 输出转化为可用产品。
- [[Specification-Driven Development]] 把透明规划与 checkpoint 进一步外化为规格、设计、任务和验证证据；
  [[SDD 开发规范研究]] 的门禁让 agent 在任务内自主，但不能自行改写产品意图、风险接受或验收标准。
- [[从知识图谱到 Agent 编排]] 将本页放入“权威事实—检索—记忆—编排—行动—调和”的完整闭环，
  并区分 [[MCP]] 的连接作用与 [[RPA]] 的界面执行作用。
- Stanford STORM 是 **prompt chaining + parallelization** 的完整实证案例：四个模块由预定义代码路径
  编排，多个 persona 走线程池并行提问，**是 workflow 而非 agent**（见 [[STORM-研究提示词组]]）。
  > 综合：这在 2024 年是正确取舍——当时模型能力不足以支撑自主编排，写死流程才拿得到稳定输出。
  > 但它也解释了该项目为何掉队：**流程写死意味着模型变强时系统不会跟着变强**。
  > 这是 Simplicity 原则的一个反面边界——简单架构降低当下复杂度，也可能锁死未来的能力上限。
