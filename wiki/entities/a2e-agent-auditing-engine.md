---
tags: [实体, AI, Agent, Evals]
created: 2026-08-10
updated: 2026-11-07
sources:
  - "[[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]"
  - "https://github.com/datamllab/A2E （检索于 2026-08-10；GitHub API 复查于 2026-08-31；git 克隆复查于 2026-11-07）"
  - "https://github.com/datamllab/A2E/releases （检索于 2026-11-07）"
  - "https://arxiv.org/abs/2608.07346v4 （v4，2026-09-07；检索于 2026-11-07）"
  - "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository （检索于 2026-08-10）"
---

# A²E（Agent Auditing Engine）

A²E 是上海人工智能实验室于 2026-08-07 发布的 agent harness 评测引擎预印本及公开参考实现（代码以 MIT 许可公开，见下方证据边界）。它由 Task、Monitor、Evaluation 三层组成，支持 Agno、AutoGen AgentChat、CrewAI、Google ADK、LangGraph、LlamaIndex、OpenAI Agents SDK、Smolagents 和 Anthropic/Claude Agent SDK 等 harness。

关键机制包括 [[agent-task-protocol|ATP]]、OpenTelemetry/OpenInference 风格的 span trace、[[lifecycle-aligned-evaluation]] 与可重评的结构化存储。论文实验显示，同一模型在不同 harness 上的多轮成功率、token 使用和终止行为可出现明显差异，因此 harness 不应被当作“轻量 wrapper”。这一结论在 v1 与现行 v4 中都成立，但两版的实验设计完全不同，引用具体数字须注明版本（见 [[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]「版本变化」）。

> 证据边界（2026-11-07 复查，克隆 origin/main）：代码以 MIT 许可公开（Copyright (c) 2026 Shanghai AI Lab），MIT 明确授予复制、修改与再分发权。仍无 release、无 tag（`git ls-remote --tags` 为空，Releases 页 "There aren't any releases here"）；main 持续开发到 2026-10-09，当日新增 Jev judge，为四个事实类指标在原 LLM judge 旁并列写 `*_jev` 分数。2026-09-04 的提交 6f92413 把 hallucination 指标极性反转为 1 = 幻觉（`higher_is_better=false`），同名指标在不同 commit 下评分语义相反、不可直接比较。综合：无版本化发布这一条仍在，现阶段仍适合隔离 POC 和方法参考，不是已验证的生产组件；POC 应 pin 到具体 commit。

详见 [[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]] 与 [[Agent 全轨迹评测与审计]]。

## 历史

- **2026-08-10**：仓库未声明 license，依 GitHub 官方许可指南不应默认获得复制、再分发或衍生使用权。仓库 2026-08-12 补入 MIT LICENSE 后失效（2026-08-31 经 GitHub API 确认）。
- **2026-08-31 复查**：仍无 release、无 tag，最近提交停在 2026-08-18（GitHub API `repos/datamllab/A2E` 及其 `/releases`、`/tags`）。2026-11-07 复查时 main 已持续开发到 2026-10-09，“停在 08-18”不再成立。
- **论文 v1（2026-08-07）→ v3（2026-09-04）**：实验从 DeepSeek-V4-Pro × 23 benchmark × 每格 5 任务（1,035 runs）换成 gpt-5.6-sol 与 glm-5.3 两个底座 × 4 个前沿 benchmark 族的官方指标；v4（2026-09-07）沿用。
