---
tags: [分析, AI, Agent, Evals, 审计, 可观测性]
created: 2026-08-10
updated: 2026-08-31
sources:
  - "[[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]"
  - "[[Evals]]"
  - "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository （检索于 2026-08-10）"
  - "https://github.com/datamllab/A2E （GitHub API 复查于 2026-08-31）"
renders: []
---

# Agent 全轨迹评测与审计

## 核心判断

Agent 评测的对象不应只是“模型给了什么答案”，而应是**模型 + harness + 工具 + 环境 + 运行政策**共同产生的系统行为。最终结果回答“任务是否完成”，全轨迹回答“为什么成功或失败、代价和风险是什么”；两者必须同时存在。

[[a2e-agent-auditing-engine|A²E]]（源摘要：[[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]）的主要价值不是又增加一张 framework 排名表，而是把任务适配、原生执行可观测、分层评分与历史重评组合成可复用的评测管线。

## 可复用的四类契约

### 1. Task Contract：固定“测什么”

一个可比较任务至少包含 instruction、initial state、tool schema、expected action/output、sandbox、seed 与终止条件。[[agent-task-protocol|ATP]] 的 `TaskInput`、`AgentBinding`、`AgentRunner`、`TaskTrace` 是一种实现，不是唯一标准。

### 2. Trace Contract：固定“看到什么”

Trace 不只是文本日志，而应有稳定语义和因果关系：trace/run ID、span 类型、parent-child、开始/结束、输入/输出、状态/错误、token/耗时/成本、工具参数与结果。OpenTelemetry 适合作为运输与因果骨架，但仍需定义 agent 特有的语义。

### 3. Metric Contract：固定“怎么判断”

指标至少要区分三层：

- **Outcome**：真实环境是否到达目标终态，是成功的主证据。
- **Process**：计划、工具、记忆、错误恢复与终止策略，用于定位机制。
- **Lifecycle**：成本、延迟、安全、权限和注入韧性，用于判断能否生产运行。

[[lifecycle-aligned-evaluation]] 提供了稳定分类骨架，但具体指标应可版本化，并声明是规则、环境 verifier、LLM judge 还是人工标注。注意 "lifecycle" 在此有两个义项：本页三分层中的 **Lifecycle** 只是运行质量子集（约当该框架四阶段中的 Runtime Quality）；而 Lifecycle-Aligned Evaluation 本身是覆盖 Reasoning、Action、Final Answer、Runtime Quality 全部四阶段的组织框架，Outcome 也在其内——全集与子集不可混用。

### 4. Re-evaluation Contract：固定“如何重判”

维持轨迹原始记录，评分另存 `metric_version`、`judge_model`、`prompt_version`、`evaluator_code`、`evaluated_at` 和环境版本。这样新的安全规则或 judge 可重评旧轨迹，且不会把“系统行为变了”与“裁判标准变了”混在一起。

## 最小生产实现

| 层 | 最小产物 | 先证明什么 |
|---|---|---|
| 任务 | 20–50 个来自真实失败的版本化 cases，含正反例和 reference solution | 任务、grader 与环境可运行 |
| 观测 | 模型/工具/工作流 span，统一 run ID，关键副作用存 outcome | 能重建关键决策和环境变化 |
| 评分 | 确定性 outcome grader + 少量 process 指标 + 人工抽检 | 最终分与失败分类基本可靠 |
| 比较 | 固定 task IDs/seed/模型配置，报告分布与失败簇 | 变化来自 harness 而非样本漂移 |
| 治理 | 脱敏、ACL、保留期、指标/judge 版本与责任人 | trace 可用于审计且不制造新的数据风险 |

第一版不需要复刻 A²E 的 23×9 矩阵。先选一条真实业务链路、一个模型和两个 harness/policy 变体，验证“同结果不同过程”与“同模型不同系统行为”是否在本地任务出现。

## 证据边界

- A²E 是预印本；每个 harness×benchmark 仅 5 个任务，无法支持稳定总排名。
- 论文中若干过程指标在该 benchmark mix 上变动很小，作者把“转换为 harness 设计指导”留给未来工作。
- CrewAI 的 LLM span 缺 token 数，被排除在部分成本图之外；某些行为指标实为 instrumentation 产物。
- 过程评分也会被指标博弈；LLM judge 不是独立裁判者，必须与 outcome verifier 和人工 trace 抽检组合。
- 2026-08-31 复查：A²E 仓库已于 2026-08-12 补入 MIT LICENSE，但仍无 release、无 tag，最近提交停在 2026-08-18（GitHub API `repos/datamllab/A2E`，检索于 2026-08-31）。原「未见 license，故不宜再分发」的限制已解除。综合：方法仍可独立实现，现有代码属早期参考实现，应先作隔离 POC 与设计参考，再决定是否并入生产。

## 与现有判断的关系

- [[harness-vs-model]]：本页实验证据的核心结论——同模型在不同 harness 上产生不同系统行为，harness 不是轻量 wrapper。
- [[Evals]]：增加“outcome 优先证明、trace 负责归因、历史轨迹可重评”的工程契约。
- [[从知识图谱到 Agent 编排]]：为第 6 层“验证与调和”补全可运行的轨迹、结果与重评契约。
- [[agent-生产级落地的鸿沟]]：生产成熟度不能只看通过率，还要看失败发生在哪一步、如何恢复、成本与副作用是否可控。
