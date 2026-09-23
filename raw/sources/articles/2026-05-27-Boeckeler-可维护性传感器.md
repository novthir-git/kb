# Maintainability sensors for coding agents（中文结构化研究摘录）

- 原文：https://martinfowler.com/articles/sensors-for-coding-agents.html
- 作者：Birgitta Böckeler（Thoughtworks）
- 发布日期：2026-05-27（以原站为准；第三方镜像 martinfowler.spicytakes.org 标为 2026-05-20，不采用）
- 检索与入库日期：2026-09-23（直连原站）
- 存档说明：要点式中文摘录，非翻译或镜像；保留实验设置、数字与作者结论，细节请回查原文。
- 证据性质：单人、单应用的实践报告，无对照组。
- 前文：`raw/sources/articles/2026-04-02-Boeckeler-Harness-Engineering.md`

## 设置

- 应用：TypeScript / Next.js / React 的内部分析看板，为实验用 AI 从零重建；刻意几乎不给 guides，只观察 sensor 的作用。
  工具为 Cursor、Claude Code、OpenCode；模型以 Claude Sonnet 为主，规划与分析类任务用 Claude Opus。
- 作者眼中可维护性开裂的第一信号：小改动需要改的文件数上升，或改动开始破坏原本正常的功能。
- Sensor 部署：编码会话中（类型检查、ESLint、Semgrep、dependency-cruiser、测试与覆盖率、增量变异测试、pre-commit 的
  GitLeaks）→ CI 重跑 → 周期性运行（安全评审、数据处理评审、依赖新鲜度报告、模块化与耦合评审）。

## 发现

1. **基础 lint**：最容易抓的 AI 短板是参数个数、文件与函数长度、圈复杂度，但 ESLint 默认预设都没启用。作者用自定义
   formatter 把规则消息改写成自纠正指引；阈值类规则允许 agent 在认为重构不必要时略微上调阈值，而非永久豁免，
   将来进一步恶化时规则仍会触发。唯一没配指引的圈复杂度规则，恰是 agent 最常直接上调阈值的一类。规则之间出现权衡：
   限制行数促成了拆分，却把复杂度推进 React 组件越来越长的 props 链。作者担心质量错觉，以及反馈过载引发过度重构。
2. **依赖规则**：用 dependency-cruiser 强制分层（错误消息复述整体分层概念），agent 违规后能依据反馈自纠正；
   工具配置门槛几乎全被 AI 吸收。可替代在 markdown 里描述代码结构，但只能表达 import、文件名与目录层面的约束。
3. **耦合数据**：自建耦合度 CLI 交给 Claude Opus 4.7 解读，结果乏善可陈——把刻意设计的依赖注入工厂和前后端共享的
   schema 判为问题。作者结论：是否合适取决于上下文，原始耦合数据单独对 AI 没用；更实际的用途是审查时按影响半径分诊。
4. **AI 模块化评审**：改用 Vlad Khononov 的 Modularity Skills（纯推理型），发现大量有价值的问题——三个近乎相同的
   route 文件；第三个页面没复用已有 hook，另起一套；核心参数逐层重复传递，此前一次日期范围改动波及 40 多个文件，
   参数对象早已引入却从未贯彻；认证逻辑错放在装配工厂里。另一次重跑又发现首轮遗漏的问题，故重要分析值得多跑。
   作者结论：没有人工评审、也没有这类 AI 评审时，agent 确实在累积无意的技术债；模块化是计算型 sensor 帮不上太多、
   需要推理型 sensor 的领域。作者的经验：agent 在第三、四次重复时通常不会主动重构。
5. **测试作为回归 sensor**：测试全部由 AI 编写、几乎未审。例：`mappers.ts` 语句覆盖 100%、分支覆盖 75%，实际没有
   单元测试，Stryker 报 13 个存活变异体——覆盖来自一个大的验收测试。结论：把大部分测试交给 AI 时，变异测试至关重要；
   验收测试提升覆盖却断言稀疏，造成虚假安全感。变异测试资源消耗大，作者手动触发增量运行。

## 结论与开放问题

- 计算型 sensor 在文件与函数层面表现最好；跨文件的模块化与耦合需要 LLM 的语义解释。
- 预计会出现 sensor 之间的冲突。
- 对 sensor 有信心后能删掉哪些 guides、sensor 能否让较弱模型可用、如何让 guides 与 sensors 保持一致，均未解决；
  测试本身的正确性是另一个问题。
- 这些 sensor 提高了作者对结果的信任，但不能把人完全移出回路。
