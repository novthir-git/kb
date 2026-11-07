---
tags: [概念, AI, Agent, Evals, Harness]
created: 2026-08-10
updated: 2026-11-06
sources:
  - "[[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]]"
  - "[[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]]"
  - "https://docs.x.ai/developers/release-notes.md （检索于 2026-11-06）"
  - "https://fortune.com/2026/03/09/microsoft-copilot-cowork-ai-agents-anthropic-e7-m365-saas/ （检索于 2026-11-06）"
  - "[[2026-08-27-Uber-软件工厂成本效率-源摘要]]"
  - "[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]"
  - "[[2026-04-02-Boeckeler-Harness-Engineering-源摘要]]"
---

# Harness 不是轻量 Wrapper

Agent 系统的实际表现由模型与 harness 共同决定。Harness 的 prompt 构造、工具表示、上下文管理、执行循环、错误处理和终止政策，会在模型不变时改变任务成功率、token 成本和失败路径。

[[a2e-agent-auditing-engine|A²E]] 提供了这一判断的受控实验证据：单轮任务的最终分常看不出 harness 差异，多轮与工具型任务则显著分化；同时轨迹可显示即使 correctness 接近，计划、工具选择和成本仍可差很多。但由于每格仅 5 个任务，证据支持“必须评整个系统”，不支持稳定的全局 harness 排名。评测契约的完整展开见 [[Agent 全轨迹评测与审计]]。

## 工程推论：想比较谁，就把另一个钉死

Uber 的公开实践把这条判断变成了可执行规程（[[Uber-软件工厂的成本工程]]）：

- **比较模型**时固定 harness——"一个接口后面接任意模型（前沿或开源权重）"，据此在
  成本/完成任务 × 输出质量 × 可靠性的空间里取 Pareto 最优，并因"前沿每几周就移动一次"而持续迁移。
- **测量自身优化收益**时固定模型——原文明说不这样做就无法把自己的工程收益从模型换代和
  厂商调价里分离出来（其 −34% / −52% 即在固定模型下测得）。

> 综合：两个方向都做，才构成完整的对照设计。只做前者会把 harness 改进误记为模型进步，
> 只做后者会把模型换代误记为自己的功劳——**agent 系统的任何成本或质量归因，都必须先声明哪一半被钉死了。**

## 本页说的是内层 harness；外层另见 [[Harness Engineering]]

2026 年起 "harness" 还有第二个常用义：**使用者在 agent 之外为它搭的环境**——规则文件、类型与依赖约束、测试、
linter、CI 与周期性评审（Böckeler 明确把这一层称为 agent 内置 harness 之外的外层 harness，
见 [[2026-04-02-Boeckeler-Harness-Engineering-源摘要]]）。本页的 A²E 与 Uber 证据针对的是**内层**：
agent 运行时自身的 prompt、工具与执行循环。

OpenAI 的零手写代码实验从外层给出同向证据：早期进展慢的原因是缺工具、抽象与内部结构，**瓶颈在环境而非模型**
（[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]）。

> 综合：本页的归因纪律对外层同样适用。"换了模型后成功率上升"的结论，若同期还改了规则文件、测试或 lint，
> 就同样无法归因——**钉死的对象要把内外两层都算进去**。

## 2026-11 补：harness 差异的三条新信号

- **结构稳住长尾（低权重）**：DeepSeek Super-agent 的消融实验里，同一条消息流同时驱动四种方案。两级架构把"要不要委派"从模型的临场判断变成结构上的保证：p95 从 29.0 降到 15.7 分钟，p50 只快约 10%。代价是缓存读变成单会话方案的 2.1–3.8 倍。但用的是合成负载，每组 5 次，没人复现，只能算方向性证据（[[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]]）。
- **厂商把模型训练到自家 harness 上**：SpaceXSI 称 Grok 4.7（2026-09-21）经过训练，能"natively understand the Grok Bot harness"。综合：harness 不只是模型的外壳，它也成了模型训练的目标环境。这让"固定模型、换 harness"的对照更难做干净：模型与 harness 的组合本身就是被优化过的整体。
- **harness 作为可授权的资产**：Microsoft Copilot Cowork 采用了与 Claude Cowork 相同的 agentic harness，跑在自己的 M365 租户里，同时把模型换成多家可选。综合：这说明 harness 可以与模型解耦、单独授权给别人用。也说明常驻 agent 赛道里，编排**拓扑**虽已普及，harness 的**质量**仍在拉开差距，见 [[常驻 AI 同事的竞争格局]]。
