---
tags: [实体, 产品, AI, Agent, 软件工程]
created: 2026-08-11
updated: 2026-11-07
sources:
  - "[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]"
  - "https://simonwillison.net/2026/Jul/21/cat-and-thariq/ （检索于 2026-08-03）"
  - "https://docs.anthropic.com/zh-CN/docs/claude-code/memory （检索于 2026-08-07）"
  - "[[2026-08-27-Uber-软件工厂成本效率-源摘要]]"
  - "[[2026-07-30-Thoughtworks-重构的经济收益-源摘要]]"
  - "[[2026-05-27-Boeckeler-可维护性传感器-源摘要]]"
  - "[[2026-05-19-Sonar-代码整洁度最小对实验-源摘要]]"
  - "https://arxiv.org/abs/2610.36346 （Over-Compliant Refactoring，预印本；检索于 2026-11-07）"
  - "https://x.com/bcherny/status/2088014489438621990 （Boris Cherny，2026-08-13；检索于 2026-11-07，经 fxtwitter API）"
  - "https://claude.dev/blog/solving-code-review-at-anthropic/ （Claude Code 团队，2026-10-15；检索于 2026-11-07）"
  - "https://code.claude.com/docs/en/changelog （v2.1.277；检索于 2026-11-07）"
---

# Claude Code

[[Anthropic]] 面向开发者的 agentic 编码工具与平台：以终端/CLI 为主要界面，让 agent 在代码库中
自主读写、执行、测试并迭代。与 [[Codex]] 同类。本 wiki 不追它的功能更新，只沿三条线追踪其**判断价值**。

## 线 1：agentic coding loop 的加速器

- 在 [[Loop Engineering]] 的三层循环中，它加速的是分钟级 agentic coding loop，从而把人的工作
  上移到规格、[[Evals|evals]] 与产品判断——瓶颈从写代码迁移到设计循环。
- 其产品设计本身是 agent 工程的一手样本（[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要|团队访谈]]）：
  前沿模型的系统提示缩短约 80%（旧模型保留完整提示，不可外推为通用法则）；工具数收敛
  （grep/glob 归入原生 Bash）；文件编辑工具因可确定性渲染 diff 而保留——**工具同时服务模型、用户与审计**。

- **harness 的默认值本身是成本杠杆**：Uber 在自建统一包装层里把压缩阈值设为 400K（即便模型有 1M
  上下文）、reasoning effort 默认 Medium、交互 session 的 prompt 缓存 TTL 从 5 分钟改为 1 小时
  （子 agent 保持 5 分钟）、**子 agent 默认弱模型**（其称之为交互侧最有效的单一杠杆），
  并在 status line 挂实时花费计数器（[[2026-08-27-Uber-软件工厂成本效率-源摘要]]）。
  综合：这是一份来自外部大型企业的一手证据，说明 **harness 的可配置面同时是成本控制面**——
  与 [[harness-vs-model]] 的判断一致，也解释了为什么企业倾向在官方 CLI 外再包一层。
  完整语境见 [[Uber-软件工厂的成本工程]]。

- **自发发起重构是它的弱项（单个外部实验，2026-07-30）**：Thoughtworks 在一个约 15 万行、主要由 Claude Code 写成的应用上做
  重构实验。开发 harness 里原有的显式重构步骤从未促使它处理一个 17,155 行的文件；作者称 Claude 需要人主动引导才能
  选对重构；另据其轶事观察，制定计划时 Claude.ai 看出应抽出整个 client 类，Claude Code 只提出 Extract Function。
  执行时用 Python 调 grep/sed 做机械改写，常被缩进搞乱；价值最大的一步首轮被漏掉，经唯一一次人工重新引导补做。
  整个实验约 8 小时，基本无人值守，同一变更的输入 token 降了约 83%
  （[[2026-07-30-Thoughtworks-重构的经济收益-源摘要]]；单次运行，与 Sonar 受控实验整体 −7.1%、认知热点轨 +1.8% 矛盾，
  见 [[Agentic SE 时代的系统重构]] §二 ⚠️）。综合：它**不会自发发起重构**；被要求制定计划
  时选题偏浅（单实验）；执行能在人工选定后基本无人值守地完成，但不可靠。与 [[Birgitta Böckeler|Böckeler]] 用 Cursor / Claude Code /
  OpenCode 做的 sensor 实验一致的只有"不会自发发起"这一层——在选题上，她用推理型模块化评审反而得到了大量有价值的
  线索（[[2026-05-27-Boeckeler-可维护性传感器-源摘要]]）。论点页见 [[Agent 不会自发偿还结构债]]。

- **被驱动后不会停（2026-11-07 补，预印本）**：Over-Compliant Refactoring 让 Codex 与 Claude Code 在 5 个模型上对已经
  干净的代码反复要求"再重构"（>3,000 轮），没有一个因认出代码已经优化而停下；首次停下前最多把代码库重写到原来的 31 倍，
  宣称完成后还会恢复编辑（https://arxiv.org/abs/2610.36346 ，检索于 2026-11-07）。综合：与"不会自发发起"是同一缺口的两面——发起与停止都要由
  harness 给出（[[Agent 不会自发偿还结构债]] 第 3 层）。
- **代码整洁度对它读取成本的量级基准**：Sonar 的最小对实验固定 Claude Code + Sonnet 4.6，660 次运行，整洁度不改变通过率
  （−0.9 pp），输入 token 整体 −7.1%、跨模块任务 −10.7%（[[2026-05-19-Sonar-代码整洁度最小对实验-源摘要]]）。
  综合：比上面的 −83% 更适合作回本估算的基准；单人项目据此怎么决策见 [[全AI代码库的治理决策]]。

## 线 2：Anthropic 内部 AI 原生 SDLC 的载体

- 团队内部以 Claude Tag（Slack 中的团队级常驻协作层）+ Claude Code（个人复杂任务的交互式执行）分工，
  完整流程模型见 [[Claude Tag 驱动的团队研发流程]]。
- Claude Tag 提交该团队 **65% 的产品 PR**。口径边界：员工自报，且仅指 Claude Code 产品工程团队，
  不是全 Anthropic 数据，也不是无人审查比例。
- 分层审查：系统提示等核心区域保留 code owner 人工批准；外围文件经六个多月 shadow mode 验证后
  才逐步交给自动 review。放权单位是**文件范围 × 风险等级 × 回归证据**，不是全局开关。
- Eval 驱动：新模型替换前跑产品级 eval；事故致因 PR 转为 eval 用例回灌 reviewer。
  治理侧全景见 [[Anthropic-AI原生SDLC治理循环]]。
- **团队自报的 review 数据（2026-11-07 补）**：Claude 写了 Claude Code 约 90% 的代码；6–9 月合并 PR 增加一倍以上，需要回退的
  占比降了 40% 以上。做法是把大部分"阅读"交给机器：提 PR 前第二个 agent 在全新上下文里审 diff，每个 PR 过必需 CI（红即阻断）、
  Claude Code Review 与单独的安全审查，再按风险分级人工审批（https://claude.dev/blog/solving-code-review-at-anthropic/ ，
  2026-10-15，检索于 2026-11-07）。口径：团队自报、无对照。
- **偿还结构债的 routines**：Boris Cherny 自述 Claude Tag 每日跑一批维护 routine（崩溃 fuzz、重复统一、死代码删除、抽象审查等），数周开
  388 个 PR、在 Claude Code Review 加人工复审后合并 180 个（约 46%；https://x.com/bcherny/status/2088014489438621990 ，
  检索于 2026-11-07）。口径：个人自述，未合并原因未披露。证据行见 [[Agent 不会自发偿还结构债]]。

## 线 3：本仓库自身的维护工具

- Claude Code 是本 wiki `wiki/` 目录的**唯一写手**（本仓库 `AGENTS.md` 铁律），承担
  [[llm-wiki-方法论]] 的 Ingest / Query / Lint 三大操作——本仓库即"用 agent 维护语义记忆"的活体实验。
- 其 `CLAUDE.md` 记忆文件机制对应 [[AI编码技术债的三层治理]] 的意图层：承载项目特定、可执行的约定，
  但只能提高遵循概率，硬约束仍须落在门禁。
- [[STORM-研究提示词组]] 的多视角检索阶段可在 Claude Code 中用 subagent 并行执行，是最接近
  原系统并行架构的手工执行方式。
- 自 v2.1.277（2026-09-18）起，项目没有 `CLAUDE.md` 时 Claude Code 读取 `AGENTS.md`
  （https://code.claude.com/docs/en/changelog ，检索于 2026-11-07；[[2026-09-23-agentic-se-refactoring-methodology-源摘要]]）。
  本仓库以 `AGENTS.md` 为权威、`CLAUDE.md` 为其 symlink，两种读法拿到的是同一份规范。

## 与 Claude Cowork 的分界

[[Claude Cowork]] 面向**非技术知识工作者**的通用 agent 场景；Claude Code 面向开发者与工程流程。
综合：两者共享同一 agent 能力栈，分界在界面与治理对象——前者的冲击面是 SaaS 资本市场
（见 [[cowork-saas-资本市场冲击]]），后者的冲击面是软件工程组织方式。

## 关联页面

- [[Anthropic]] / [[Claude Cowork]] / [[Codex]]
- [[Claude Tag 驱动的团队研发流程]] / [[Anthropic-AI原生SDLC治理循环]]
- [[Loop Engineering]] / [[Evals]] / [[AI编码技术债的三层治理]]
- [[Harness Engineering]] / [[Agent 不会自发偿还结构债]] / [[Agentic SE 时代的系统重构]] / [[全AI代码库的治理决策]]
- [[llm-wiki-方法论]] / [[STORM-研究提示词组]]
- [[生产力-体验悖论]] / [[agent-生产级落地的鸿沟]]
