---
tags: [素材, AI, Agent, 软件工程, Harness, 测试]
created: 2026-09-23
updated: 2026-09-23
sources:
  - "raw/sources/articles/2026-05-27-Boeckeler-可维护性传感器.md"
  - "https://martinfowler.com/articles/sensors-for-coding-agents.html （检索于 2026-09-23）"
---

# 2026-05-27 Böckeler《Maintainability sensors for coding agents》源摘要

**原文**：Birgitta Böckeler（Thoughtworks），martinfowler.com，2026-05-27（以原站为准；第三方镜像
martinfowler.spicytakes.org 标为 2026-05-20，不采用）。
**存档**：`raw/sources/articles/2026-05-27-Boeckeler-可维护性传感器.md`（要点式中文摘录）。
**前文**：[[2026-04-02-Boeckeler-Harness-Engineering-源摘要]]。

概念归位见 [[Harness Engineering]]；"agent 在累积无意的技术债"作为证据行收在 [[Agent 不会自发偿还结构债]]。
本页只做忠实摘录与口径标注。

## 一句话

一次刻意"几乎不给 guides、只看 sensors"的实验：**计算型 sensor 在文件与函数层面表现最好，跨文件的模块化
与耦合需要推理型 sensor；把测试交给 AI 时，覆盖率会制造虚假安全感，变异测试至关重要。**

## 设置

- 应用：TypeScript / Next.js / React 的内部分析看板，为实验用 AI 从零重建。工具为 Cursor、Claude Code、
  OpenCode；模型以 Claude Sonnet 为主，规划与分析类任务用 Claude Opus。
- 作者眼中可维护性开裂的**第一信号**：小改动需要改的文件数上升，或改动开始破坏原本正常的功能。
- Sensor 按三个时机部署：编码会话中（类型检查、ESLint、Semgrep、dependency-cruiser、测试与覆盖率、增量变异测试、
  pre-commit 的 GitLeaks）→ CI 重跑 → 周期性运行（安全评审、数据处理评审、依赖新鲜度报告、模块化与耦合评审）。

## 五项发现（摘录）

1. **基础 lint**：最容易抓的 AI 短板是参数个数、文件与函数长度、圈复杂度，但 ESLint 默认预设都没启用。
   作者用自定义 formatter 把规则消息改写成自纠正指引；阈值类规则允许 agent 在认为重构不必要时**略微上调阈值**
   而非永久豁免。**唯一没配指引的圈复杂度规则，恰是 agent 最常直接上调阈值的一类。**规则之间有权衡：限制行数
   促成了拆分，却把复杂度推进 React 组件越来越长的 props 链。作者担心质量错觉，以及反馈过载引发过度重构。
2. **依赖规则**：dependency-cruiser 强制分层，错误消息复述整体分层概念，agent 违规后能据此自纠正；工具配置门槛
   几乎全被 AI 吸收。可替代在 markdown 里描述代码结构，但只能表达 import、文件名与目录层面的约束。
3. **耦合数据**：自建耦合度 CLI 的输出交给 Claude Opus 4.7 解读，结果乏善可陈——把刻意设计的依赖注入工厂和
   前后端共享的 schema 判为问题。原始耦合数据单独对 AI 没用；更实际的用途是审查时按影响半径分诊。
4. **AI 模块化评审**：改用 Vlad Khononov 的 Modularity Skills（纯推理型），发现大量有价值的问题——三个近乎相同的
   route 文件；第三个页面没复用已有 hook；核心参数逐层重复传递，此前一次日期范围改动波及 40 多个文件，参数对象
   早已引入却从未贯彻；认证逻辑错放在装配工厂里。重跑又发现首轮遗漏的问题。结论：没有人工或 AI 评审时，
   agent 确实在累积无意的技术债；agent 在第三、四次重复时通常不会主动重构。
5. **测试作为回归 sensor**：测试全由 AI 编写、几乎未审。`mappers.ts` 语句覆盖 100%、分支覆盖 75%，实际没有
   单元测试，Stryker 报 13 个存活变异体——覆盖来自一个大的验收测试。结论：把大部分测试交给 AI 时变异测试至关
   重要；验收测试提升覆盖却断言稀疏，造成虚假安全感。变异测试资源消耗大，作者手动触发增量运行。

## 作者的结论与开放问题

- 计算型 sensor 在文件与函数层面最好；跨文件的模块化与耦合需要 LLM 的语义解释。预计会出现 sensor 之间的冲突。
- 未解决：对 sensor 有信心后能删掉哪些 guides；sensor 能否让较弱模型可用；如何让 guides 与 sensors 保持一致；
  测试本身的正确性。
- 这些 sensor 提高了作者对结果的信任，但**不能把人完全移出回路**。

## 口径与证据边界

1. **单人、单应用的实践报告，无对照组**；应用是为实验重建的内部看板，规模与复杂度有限。
2. 刻意少给 guides 的设置放大了 sensor 的作用，也让"没有评审时 agent 累积技术债"更容易出现；
   不能直接外推到 guides 完备的仓库。
3. 推理型评审非确定：同一分析重跑结果不同，本文未给多次运行的一致性数据。

## 本 wiki 的用法

- [[Harness Engineering]]"计算型管局部、推理型管跨文件"与"为 LLM 写的 sensor 信号"两节的实证来源。
- [[AI编码技术债的三层治理]] 证据层的补充：阈值会被 agent 当作可优化目标；覆盖率不是测试质量。
- [[Agent 不会自发偿还结构债]] 的证据行。
