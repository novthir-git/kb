---
tags: [概念, AI, Agent, 软件工程, Harness, 方法论]
created: 2026-09-23
updated: 2026-09-23
sources:
  - "[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]"
  - "[[2026-04-02-Boeckeler-Harness-Engineering-源摘要]]"
  - "[[2026-05-27-Boeckeler-可维护性传感器-源摘要]]"
  - "https://openai.com/index/harness-engineering/ （检索于 2026-09-23；直连 403，经官方中文版读取）"
  - "https://martinfowler.com/articles/harness-engineering.html （检索于 2026-09-23）"
  - "https://martinfowler.com/articles/sensors-for-coding-agents.html （检索于 2026-09-23）"
---

# Harness Engineering

**一句话定义**：为 coding agent 设计它工作所处的**环境**——前馈的约束与指引（guides）、反馈的检测与信号
（sensors），以及让两者持续改进的回路——使 agent 首次做对的概率更高、出错时在到达人眼之前自纠正。
OpenAI 的 Ryan Lopopolo（2026-02-11）用它命名自家"零手写代码"实验的工程重心；Thoughtworks 的
Birgitta Böckeler（2026-04-02）把它整理成面向 **coding agent 使用者**的框架，并在 2026-05-27 用一次
可维护性 sensor 实验补了实证。

两位作者的共同结论：**纪律从代码转移到了支撑结构**——最难的是设计环境、反馈回路与控制系统，
而不是写代码本身（[[2026-02-11-OpenAI-Harness-Engineering-源摘要|OpenAI]]）。

## 与 [[harness-vs-model]] 的边界：内层与外层两种 harness

"harness" 在本 wiki 已有一个用法，两者必须分开：

| | 内层 harness | 外层 harness（本页） |
|---|---|---|
| 是什么 | agent 运行时本身：prompt 构造、工具表示、上下文管理、执行循环、终止政策 | 使用者在 agent 之外搭的环境：规则文件、类型与结构约束、测试、linter、CI、周期性评审与清理任务 |
| 谁来建 | agent 厂商或平台团队（Claude Code、Codex、Uber 的统一包装层） | 使用 agent 的团队，落在**仓库与流水线**里 |
| 典型证据 | [[a2e-agent-auditing-engine|A²E]]：同模型换 harness，多轮成功率与 token 成本显著分化 | OpenAI：早期进展慢是因为缺工具、抽象与内部结构，而不是模型不够强 |
| 本 wiki 页 | [[harness-vs-model]] | 本页 |

Böckeler 明确把范围限定在后者："在 agent 内置 harness 之外"由用户搭建的那一层
（[[2026-04-02-Boeckeler-Harness-Engineering-源摘要]]）。

> 综合：两层回答的是同一个问题的两半——**同一个模型的表现取决于它外面包了什么**。内层决定 agent
> 怎么想、怎么调工具；外层决定它看到什么约束、收到什么反馈。评估或归因时，两层都要声明是否被钉死
> （[[harness-vs-model]] 的"想比较谁，就把另一个钉死"对外层同样适用）。

## 两个正交维度

Böckeler 的框架由两根轴组成：

- **Guides（前馈）vs Sensors（反馈）**。只有反馈，agent 会反复犯同一类错；只有前馈，没人知道规则是否奏效。
- **Computational vs Inferential**。前者确定、快、可靠（测试、linter、类型检查、结构分析）；后者是语义分析、
  AI review、LLM-as-judge，更贵且非确定，但能给出语义判断。

综合：交叉成四格。例子取自三份源，归格由本 wiki 完成：

| | Computational（确定性） | Inferential（推理型） |
|---|---|---|
| **Guides** | 类型系统、固定分层与依赖规则、框架与项目模板（替 agent 屏蔽细节） | `AGENTS.md` / 规则文件、结构化 `docs/`、设计文档与执行计划、skills |
| **Sensors** | 测试、类型检查、ESLint、dependency-cruiser、变异测试、结构测试、pre-commit 密钥扫描 | AI 代码评审、模块化评审 skill、周期性安全/数据处理评审、LLM-as-judge |

这与 [[AI编码技术债的三层治理]] 证据层的"确定性门禁 vs 概率型 AI review"是**独立得出的同一划分**：
确定性的一侧可以当硬门禁，推理型的一侧默认只是辅助证据。

## 五个关键机制

### 1. 为 LLM 写的 sensor 信号

Sensor 的输出不是给人看的报错，而是 agent 的下一轮输入。OpenAI 的 lint 错误信息直接内嵌修复指令；
Böckeler 用自定义 formatter 把规则消息改写成自纠正指引，并称之为"正面的 prompt injection"。
她的实验里有一条对照性观察：**圈复杂度是 agent 唯一频繁直接上调阈值的规则类别，而它恰好是唯一没配修正指引的规则**
（[[2026-05-27-Boeckeler-可维护性传感器-源摘要]]）。

> 综合：sensor 信号若只说"错了"不说"怎么改"，agent 找到的最短路径往往是**绕过**而非修正。
> 这是古德哈特定律在 agent 身上的形态：阈值变成了可被优化的目标。

### 2. Steering loop：把重复出现的问题编译进环境

某类问题重复出现，就改进对应的 guide 或 sensor；AI 也可以参与写结构测试、起草规则、搭自定义 linter
（Böckeler）。OpenAI 的版本是一个固定问题：**卡住时，追问"缺什么能力，怎样让它对 agent 可读且可强制执行"**。

这与 [[Anthropic-AI原生SDLC治理循环]] 的"把经验编译进控制面"、[[Loop Engineering]] 的"反复出同类错就固化成
evals"是同一个动作在不同层面的名字。

### 3. 时机：按成本分布检查点

检查点按成本从左到右排开：编码会话内（类型检查、lint、增量测试）→ 提交前（pre-commit）→ 集成后流水线 →
**变更生命周期之外持续运行**的漂移与健康 sensor（死代码、覆盖质量、依赖新鲜度、模块化评审）→ 运行时反馈。

最后一个"生命周期之外"的层级是 agent 场景新增的重点。OpenAI 用定期后台任务扫描偏差、发定向重构 PR，
把它做成了**垃圾回收**；详见 [[Agent 不会自发偿还结构债]]。

门禁放在哪里也是取舍。OpenAI 在高吞吐下**减少阻塞式合并门**、偶发失败靠重跑，理由是"纠错便宜、等待昂贵"，
作者也自己说明这在低吞吐环境中不负责任。
> 综合：这与 [[Anthropic-AI原生SDLC治理循环]] 的风险分级门禁并不矛盾——OpenAI 的实验对象是内部 beta，
> 爆炸半径小。**阻塞门的密度应随爆炸半径而不是随吞吐调整**；吞吐高只说明等待贵，不说明错误便宜。

### 4. 三类调节对象，难度依次上升

- **Maintainability harness**：现成工具最多、最容易。计算型 sensor 可靠地抓结构问题（重复、复杂度、缺测试、
  架构漂移）；LLM 能部分处理语义重复、冗余测试、过度设计，但贵且概率性。
- **Architecture fitness harness**：即 fitness functions，约束性能、可观测性等架构特性。OpenAI 为每个 worktree
  起独立应用实例与临时可观测性栈，让性能与用户旅程约束可由 agent 自己验证。
- **Behaviour harness**：Böckeler 称之为"房间里的大象"——当前普遍过度信任 AI 生成的测试。

两类 sensor 都抓不稳的：问题误诊、不必要的功能、误解指令。**需求没说清时，正确性不在任何 sensor 的职责内**
——这一段回到 [[Specification-Driven Development]] 与 [[AI编码技术债的三层治理]] 的意图层。

### 5. 计算型 sensor 管局部，推理型 sensor 管跨文件

Böckeler 的实验结论：计算型 sensor 在**文件与函数层面**表现最好；跨文件的模块化与耦合需要 LLM 的语义解释。
原始耦合数据直接交给模型解读"乏善可陈"（把刻意设计的依赖注入工厂判成问题），而推理型的模块化评审 skill
找到了一批真问题；再跑一次又找到首轮漏掉的——**重要分析值得多跑**。测试侧，覆盖率高不等于测试有效：
一个语句覆盖 100% 的文件，变异测试报出 13 个存活变异体。把大部分测试交给 AI 时，变异测试是必需的 sensor。

## Harnessability：代码库本身决定能被约束到什么程度

- **可被约束性**取决于代码库性质：强类型自带类型检查，清晰的模块边界才撑得起架构规则，框架能替 agent 屏蔽
  细节（Böckeler 引同事 Ned Letcher 称之为 ambient affordances）。
- **遗留系统的悖论**：最需要 harness 的地方最难建 harness。
- OpenAI 的对应判断：人类团队常推迟到数百名工程师规模才引入的严格分层架构，**对 agent 是早期前提**；
  并偏好能在仓库内被完整推理的"枯燥"技术。
- **Harness 模板**：企业里常见的少数服务拓扑可能演化为 harness 模板。Böckeler 引 Ashby 必要多样性定律——
  定义拓扑是一次多样性削减，使完备的 harness 变得可及；代价是会遇到服务模板同样的版本脱节，且非确定性控制
  更难测试。

> 综合：harnessability 让"为 agent 重构"获得了一个与"为人重构"不同的理由——重构不只是降低人的理解成本，
> 还是**提高代码库可被机械约束的程度**。展开见 [[Agentic SE 时代的系统重构]]。

## 人在哪里

人带着一套**隐性 harness**：约定、对复杂度的痛感、问责、组织记忆，这些 agent 都没有。Harness 只能部分
外化它们；目标不是消除人的输入，而是把人的输入引到最重要的地方（Böckeler）。她的 sensor 实验结论相同：
sensor 提高了对结果的信任，但**不能把人完全移出回路**。OpenAI 一侧，人主要通过提示工作，审查大部分转为
agent 对 agent，但每周人工清理"AI 残渣"的阶段先于自动化出现。

## 开放问题（Böckeler 原文列出）

- 不断增长的 harness 如何保持连贯，guides 与 sensors 如何不互相矛盾；信号冲突时能否信任 agent 取舍。
- Sensor 从不触发，是质量高还是检测不足；需要评估 harness 覆盖与质量的方法。
- 缺少把各阶段控制作为**一个系统**来配置与推理的工具。
- 对 sensor 有信心后能删掉哪些 guides；sensor 能否让较弱模型可用。

综合：第一条与 [[代码与文档漂移的本质]] 同构——guides 本身就是文档，会与 sensors、与代码发生表达漂移。
OpenAI 用 linter 与 CI 校验 `docs/` 的新鲜度与交叉链接、再由 doc-gardening agent 发修复 PR，
是本 wiki 收录的来源里唯一一个把 guides 自身纳入 sensor 覆盖的做法（本仓库的 Lint 对 `wiki/` 做的是同一件事）。

## 证据边界

- OpenAI：公司自述的内部实验，无外部审计、无对照组；作者自己限定"不应在没有类似投入时假定可泛化"。
  Böckeler 的评注指出它只覆盖可维护性一侧，**缺少功能与行为的验证**，且 OpenAI 对该结论有利益关联
  （[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]）。
- Böckeler harness 文：概念框架；sensor 文：单人、单应用的实践报告，无对照组。
- 本页的四格归类与"阻塞门密度随爆炸半径调整"是本 wiki 的综合，不是原文结论。

## 关联

- 内层 harness：[[harness-vs-model]]、[[Agent 全轨迹评测与审计]]
- 应用与论点：[[Agentic SE 时代的系统重构]]、[[Agent 不会自发偿还结构债]]
- 同构治理：[[AI编码技术债的三层治理]]、[[Anthropic-AI原生SDLC治理循环]]、[[Loop Engineering]]、[[控制带]]
- 文档作为 guide：[[代码与文档漂移的本质]]、[[llm-wiki-方法论]]
- 成本侧：[[Uber-软件工厂的成本工程]]、[[Agent 工具上下文膨胀]]
