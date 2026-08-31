---
tags: [概念, AI, Agent, Evals, 生命周期]
created: 2026-08-10
updated: 2026-08-31
sources:
  - "[[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]"
renders: []
---

# Lifecycle-Aligned Evaluation

Lifecycle-Aligned Evaluation 是 [[a2e-agent-auditing-engine|A²E]] 提出的指标组织方法，按 agent 执行生命周期将指标归到四个阶段：

- **Reasoning**：Task、Flow、Logical，检查目标理解、计划完整性和推理连贯性。
- **Action**：Tool、Skill、Memory，检查如何把计划转为环境交互。
- **Final Answer**：Answer Correctness 与 Task Completion，检查输出质量与真实终态。
- **Runtime Quality**：Efficiency 与 Safety，检查全程成本、延迟和操作风险。

它的可复用点是分离“在哪个阶段评什么”与“用什么方法评”：同一分类可挂规则、环境 verifier、LLM judge 或人工标注。它是组织接口，不是一份封闭的通用指标清单；具体任务仍需以 outcome 作为成功主证据。

注意区分 "lifecycle" 的两个义项：[[Agent 全轨迹评测与审计]] 三分层（Outcome / Process / Lifecycle）中的 **Lifecycle** 仅指运行质量子集（成本、延迟、安全），约当本框架的 Runtime Quality 阶段；而本页的 Lifecycle-Aligned Evaluation 是覆盖全部四阶段的组织框架——Final Answer（即 outcome）也在其内，是全集而非那一层。
