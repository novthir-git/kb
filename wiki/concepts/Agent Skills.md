---
tags: [概念, AI, Agent]
created: 2026-08-11
updated: 2026-08-31
sources:
  - "https://agentskills.io/specification （检索于 2026-07-28）"
  - "https://support.claude.com/en/articles/13837440-use-plugins-in-claude （检索于 2026-07-16）"
  - "[[2026-07-21-Anthropic-AI原生SDLC-源摘要]]"
  - "[[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]]"
  - "[[2026-08-27-Uber-软件工厂成本效率-源摘要]]"
renders: []
---

# Agent Skills

**一句话定义**：Agent Skills 是把「何时做、按什么步骤做、调用什么工具、如何验证」的流程知识
打包成可安装文件夹、供 agent 按需加载的开放格式（agentskills.io 规范）。每个 Skill 至少包含
`SKILL.md`，可附带 `scripts/`、`references/`、`assets/`，按 progressive disclosure 三级加载：

1. 启动时只加载名称与描述；
2. Skill 命中后加载完整 `SKILL.md`；
3. 脚本、参考与资产仅在需要时读取。

综合：本 wiki 此前在三种互不贯通的语境里论述 Skills，本页把三者收拢为同一对象的三个侧面——
**格式（记忆载体）→ 分发（plugin 组件）→ 治理（SDLC 回灌目标）**。

## 语境一：显式程序记忆的工程载体

在 CoALA 四类记忆中，Skills 落在 procedural memory：它是**可读、可版本化、按需加载的显式
程序记忆**，特别适合沉淀执行流程与验证方法（[[Agent 记忆架构]]）。两条既有修正：

- Skills 只是程序记忆的**一种工程载体**，不是全部——模型权重中的隐式能力、Agent 代码与
  外部 workflow 同属程序性知识（[[从知识图谱到 Agent 编排]]）。
- CoALA 指出修改程序记忆比写入情景/语义记忆风险更高（可能引入缺陷、偏离设计意图），
  因此 agent 自行修改 Skill 不应默认自动生效（[[Agent 记忆架构]]）。

本仓库自身的映射：`AGENTS.md` 与已装 skills 即显式程序记忆，规则仍需测试、版本化和审查
（[[从知识图谱到 Agent 编排]]）。

## 语境二：Plugin 的三组件之一

Anthropic 官方定义：**Plugin = skills + connectors + sub-agents 的组合包**，不是 MCP Server
的同义词（[[cowork-plugins-架构]]、[[Claude Cowork]]）。三组件分工：

| 组件 | 职责 |
|---|---|
| Skills | 领域知识与工作流（「知道怎么做」） |
| Connectors | 外部服务连接；custom connector 指向 remote MCP server（「连得上」） |
| Sub-agents | 专门执行单元（「谁来做」） |

Skills 在此语境中是**分发单元**：随 plugin 安装进组织环境，与 [[MCP]] 是并列组件，
不在同一层竞争。

## 语境三：SDLC 组织学习的写入目标

Anthropic 内部 AI 原生 SDLC 把复发缺陷写回 `CLAUDE.md`、组织 skills、review 规则与 evals，
再经专职 review agents、风险分级与人工批准影响后续合并（[[Anthropic-AI原生SDLC治理循环]]、
[[2026-07-21-Anthropic-AI原生SDLC-源摘要]]）。[[论代码与文档漂移解决方案]] 由此提炼出
**指令也要进入调和循环**：事故 → 可版本化政策/skills/evals → 后续生成与审查 → 生产结果 →
再校准。Skills 在此语境是**组织学习的沉淀介质**——教训以可版本化文件复用，而非留在个人经验里。

## progressive disclosure 是工具上下文膨胀的现成答案

> 综合：Skills 的三级加载与 MCP 侧的 tool search 是**同一设计原则的两次独立实现**——
> 只是 Skills 从规范第一天就把"启动只带名称与描述"写死，而 MCP tools 的默认路径是全量预加载
> （[[Agent 工具上下文膨胀]]）。实践含义：**当一段能力既可做成 MCP tool 也可做成 Skill 时，
> 上下文占用应进入选型考量**——Skills 天然按需，工具默认常驻。

规模化的一手数据：Uber 报告工程师已建 **3,600+ 个 agent skills**、**30K 次/日执行**，
并对最常访问的 MCP server 预写 25+ 个 code-mode skill，让常见流程默认走最省上下文的路径；
在建项包括**自动记录 skill 执行中的 papercut 并从 trace 自动生成 skill 更新**
（[[2026-08-27-Uber-软件工厂成本效率-源摘要]]、[[Uber-软件工厂的成本工程]]）。
综合：后者正是下节"Skill 变更需要治理"警告的高风险写入形态——**自动生成 skill 更新若无 eval 门禁，
等于让 agent 无门禁地改写自己的行为程序**；Uber 未说明该流水线的审查环节。

## 误区与边界

- **Skills ≠ MCP**：MCP 统一的是连接与交换格式（工具调用的管道），Skills 装的是流程知识；
  前者解决「能调到」，后者解决「知道怎么用」（[[MCP]]、[[cowork-plugins-架构]]）。
- **Skills ≠ 程序记忆的全部**：见语境一，这是本 wiki 已正式记录的失真修正
  （[[从知识图谱到 Agent 编排]]）。
- **Skills ≠ 语义知识库**：综合：wiki/文档类语义记忆回答「是什么」，Skills 回答「怎么做」；
  把事实性沉淀塞进 `SKILL.md` 会使其膨胀且难保鲜，两层应互链而非合并。
- **Skill 变更需要治理**：语境三的回灌若无 shadow mode、评审与版本化，等于无门禁地改写
  agent 的行为程序——正是 CoALA 警告的高风险写入（[[Anthropic-AI原生SDLC治理循环]]）。
  Anthropic 的 AI-native SDLC playbook 已把这条机制化：eval 套件在 skills / `CLAUDE.md` / hooks
  任何变更时运行，pass rate 下降的配置变更必须先 review 才能合并——skill 变更由此获得
  与代码同级的回归测试和合并门禁；且 skill 只是建议性控制，必须永远成立的政策需要 hook
  作确定性层兜底（"The skill makes violations rare and the hook makes them close to
  impossible"）（[[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]]）。
