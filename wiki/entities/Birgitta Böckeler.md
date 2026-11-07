---
tags: [实体, 人物, AI, 软件工程, Harness]
created: 2026-11-07
updated: 2026-11-07
sources:
  - "[[2026-04-02-Boeckeler-Harness-Engineering-源摘要]]"
  - "[[2026-05-27-Boeckeler-可维护性传感器-源摘要]]"
  - "[[2026-09-23-agentic-se-refactoring-methodology-源摘要]]"
  - "[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]"
  - "[[Specification-Driven Development]]"
  - "https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html （2026-08-10；检索于 2026-11-07）"
  - "https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html （2025-10-15；检索于 2026-09-23）"
---

# Birgitta Böckeler

Thoughtworks 的 Distinguished Engineer，自述方向是 AI-assisted delivery，有 20 多年开发、架构与技术领导经验
（作者简介，https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html ，检索于 2026-11-07）。
她在 martinfowler.com 的 Exploring Gen AI 系列（Thoughtworks 多位作者合写）里持续发表 coding agent 的实践文章。

## 本库引用她的什么

- **外层 harness 框架**（2026-04-02，取代 2026-02-17 的初步备忘）：guides / sensors × computational / inferential 两根轴、
  harnessability、人带着的隐性 harness。见 [[Harness Engineering]]、[[2026-04-02-Boeckeler-Harness-Engineering-源摘要]]。
- **可维护性 sensor 实验**（2026-05-19 起连载、05-27 完结）：计算型 sensor 管文件与函数层面、推理型管跨文件；圈复杂度阈值
  被 agent 频繁上调；语句覆盖 100% 的文件仍有 13 个存活变异体。见 [[2026-05-27-Boeckeler-可维护性传感器-源摘要]]、
  [[变异测试]]、[[Agent 不会自发偿还结构债]]。
- **规格寿命三层级**（2025-10-15）：spec-first / spec-anchored / spec-as-source 的最早提出者，[[GitHub Spec Kit]] 的持久化文档
  引用的就是这篇。见 [[Specification-Driven Development]]。
- **对 OpenAI harness engineering 文的评注**（2026-02-17）：认为它只覆盖可维护性、缺功能与行为验证，并提醒利益关联。本库在
  [[Harness Engineering]] 用 ⚠️ 标注了它与 OpenAI 原文的出入。
- **"LLM 不是编译器而是推断器"**（《I still care about the code》，2025-07-09），见 [[2026-09-23-agentic-se-refactoring-methodology-源摘要]]。

## 当前立场（本库核验后的口径）

- **思想光谱**：不是"系统性泼冷水"的一方，而是**按风险校准审查**（影响、概率、可检测性三因素组合判断，原文无乘法公式），
  低风险、高可检测时接受 vibe coding（[[2026-09-23-agentic-se-refactoring-methodology-源摘要]]、[[Agentic SE 时代的系统重构]]）。
- **spec-first**：认可 spec-first 的一般原则（"在很多场景下有价值"）。保留意见针对的是 2025-09 时那批 spec-first 工具的重流程与
  审查负担（"宁愿 review 代码也不愿 review 一堆 markdown"、"虚假的控制感"），以及 spec-anchored / spec-as-source 可能兼有
  MDD 的僵化与 LLM 的非确定性（[[Specification-Driven Development]]、[[SDD 收益主张的实证赤字]]）。
- **TDD**：2026-08-10 起不再让 coding agent 先写测试，"let alone do TDD (which I never did, to be honest), until I see evals or
  other strong arguments"；改为"monitor and improve regression quality with the help of mutation testing"，并试用 Ivett Ördög
  倡导的 Approved Scenarios。依据是她的小样本评估：5 批方案，Sonnet 4.6 生成、Opus 4.8 盲评，TDD 与否没有可辨别差异，变异得分
  也无差异（同上 URL）。
- **人在回路**：sensor 提高了她对结果的信任，但不能把人完全移出回路（[[2026-05-27-Boeckeler-可维护性传感器-源摘要]]）。

## 历史

本库对她立场的记录与校正，按时间：

- **2026-07-16**：本库 [[Specification-Driven Development]] 初版把三层级归于 arXiv 2602.00180。2026-09-23 更正为 Böckeler
  2025-10-15 首提（该页有 ⚠️ 归属更正块）。
- **2026-08-10 之前**：她让 coding agent 先写测试（test-first，非完整 TDD），并自述 agent 一向难以被引导着守 TDD 纪律
  （"Historically that hasn't gone well for me"）。2026-08-10 的评估后停止这样要求（同上 URL）。
- **2026-09-23 摄入的用户调研稿**（raw 只读，原文不改）：把她列为 SDD 的"批评方"、放在思想光谱"系统性泼冷水"一端，
  并把"TDD inside the agent loop"列为 Exploring Gen AI 系列路线的终点。核验后三处都已校正：
  站位改为按风险校准审查；spec-first 一般原则她是认可的；TDD 在系列中是被质疑的做法，她本人已停止让 agent 先写测试（完整 TDD 她从未要求过）
  （[[2026-09-23-agentic-se-refactoring-methodology-源摘要]]）。

## 关联

- [[Harness Engineering]]、[[变异测试]]、[[Specification-Driven Development]]、[[Agentic SE 时代的系统重构]]
- [[AI编码技术债的三层治理]]、[[Agent 不会自发偿还结构债]]、[[harness-vs-model]]
