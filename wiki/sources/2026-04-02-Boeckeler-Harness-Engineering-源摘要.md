---
tags: [素材, AI, Agent, 软件工程, Harness, 方法论]
created: 2026-09-23
updated: 2026-09-23
sources:
  - "raw/sources/articles/2026-04-02-Boeckeler-Harness-Engineering.md"
  - "https://martinfowler.com/articles/harness-engineering.html （检索于 2026-09-23）"
---

# 2026-04-02 Böckeler《Harness engineering for coding agent users》源摘要

**原文**：Birgitta Böckeler（Thoughtworks），martinfowler.com，2026-04-02。它取代了 2026-02-17 的初步备忘
《Harness Engineering - first thoughts》，原备忘 URL 已重定向至此。
**存档**：`raw/sources/articles/2026-04-02-Boeckeler-Harness-Engineering.md`（要点式中文摘录，保留概念名与作者的开放问题）。
**实证跟进**：同作者 2026-05-27 的 sensor 实验，见 [[2026-05-27-Boeckeler-可维护性传感器-源摘要]]。

概念展开见 [[Harness Engineering]]。本页只做忠实摘录与口径标注。

## 一句话

一个面向 **coding agent 使用者**的外层 harness 框架：用 guides（前馈）与 sensors（反馈）、computational 与
inferential 两根正交轴组织控制手段，目标是提高首次做对的概率，并让问题在到达人眼之前尽量自纠正。

## 框架（摘录）

- **范围**：用户在 agent 内置 harness **之外**搭建的外层 harness。收益是减少审查苦工与浪费的 token。
- **Guides vs Sensors**：只有反馈，agent 会反复犯同一类错；只有前馈，不知道规则是否奏效。为 LLM 消费而写的
  sensor 信号（如附带自纠正指令的 lint 消息）尤其有效，作者称之为**正面的 prompt injection**。
- **Computational vs Inferential**：前者确定、快、可靠（测试、linter、类型检查、结构分析）；后者是语义分析、
  AI review、LLM-as-judge，更贵且非确定，但能给语义判断。
- **与 context engineering 的关系**：后者是把 guides 与 sensors 交给 agent 的手段。
- **Steering loop**：某类问题重复出现，就改进前馈与反馈控制；也可以让 AI 写结构测试、起草规则、搭自定义 linter。
- **时机**：按成本把检查分布到提交前、集成后流水线，以及**变更生命周期之外持续运行**的漂移与健康 sensor
  （死代码、覆盖质量、依赖扫描），直至运行时反馈。

## 三类调节对象

- **Maintainability harness**：现成工具最多，最容易。计算型 sensor 可靠地抓重复、复杂度、缺测试、架构漂移；
  LLM 能部分处理语义重复、冗余测试、过度设计，但贵且概率性；问题误诊、不必要的功能、误解指令两者都抓不稳——
  **需求没说清时，正确性不在任何 sensor 的职责内**。
- **Architecture fitness harness**：即 fitness functions（性能、可观测性等架构特性）。
- **Behaviour harness**："房间里的大象"。当前普遍做法过度信任 AI 生成的测试。

## Harnessability、模板与人

- 可被约束性取决于代码库性质：强类型、清晰的模块边界、能替 agent 屏蔽细节的框架（同事 Ned Letcher 称之为
  ambient affordances）。遗留系统的难题：**最需要 harness 的地方最难建 harness**。
- 企业常见的少数服务拓扑可能演化为 **harness 模板**；作者引 Ashby 必要多样性定律说明拓扑定义是一次多样性削减；
  但模板会遇到与服务模板相同的版本脱节，非确定性控制也更难测试。
- 人带着**隐性 harness**（约定、对复杂度的痛感、问责、组织记忆），agent 没有；harness 只能部分外化它们，
  目标是把人的输入引到最重要的地方。

## 作者列出的开放问题与实践信号

- 开放问题：增长的 harness 如何保持连贯、guides 与 sensors 不互相矛盾；信号冲突时能否信任 agent 取舍；
  sensor 从不触发是质量高还是检测不足；需要评估 harness 覆盖与质量的方法；缺少把各阶段控制作为一个系统来
  配置与推理的工具。
- 实践信号：OpenAI 的分层约束与定期"垃圾回收"（见 [[2026-02-11-OpenAI-Harness-Engineering-源摘要]]）、
  Stripe minions 的反馈左移与 blueprints、变异测试与结构测试复兴、LSP 接入 coding agent、Thoughtworks 团队的
  "janitor army"。

## 口径与证据边界

1. **概念框架，不是实证研究**；所列实践信号是作者观察到的行业动向，本 wiki 未逐条回查（Stripe minions、
   janitor army 仅见于本文转述）。
2. 框架本身不给效果数据；同作者的实证跟进只有单人单应用的 sensor 实验。

## 本 wiki 的用法

- [[Harness Engineering]] 的主体框架来源；其"computational vs inferential"与 [[AI编码技术债的三层治理]]
  的"确定性门禁 vs 概率型 AI review"独立同构。
- "最需要 harness 的地方最难建 harness"是 [[Agentic SE 时代的系统重构]] 遗留系统一节的出发点。
