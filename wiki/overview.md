---
tags: [综合]
created: 2026-07-03
updated: 2026-08-31
sources: []   # 本页不罗列内部页面：关联由正文双链 + wiki/index.md 承载（详见 AGENTS.md）
---

# Overview — 当前知识版图

## 主要板块
- **AI Agent 与软件行业颠覆**：[[Anthropic]] 的 [[Claude Cowork]] + [[MCP]] + [[building-effective-agents]]
  构成"能替代人+传统软件界面"的栈；其资本市场冲击见 [[cowork-saas-资本市场冲击]]；[[cowork-plugins-架构]] 已校正为 Plugin → Connector → MCP Server 的分层。
- **Agent 采用与人的体验**：[[Codex]] 的采用爆发（[[codex-agent-采用曲线]]）与其体验成本
  （[[生产力-体验悖论]]、"从创造到验证"的监督式工程）——新增企业 / 成熟仓库 RCT、生产遥测与维护负担证据，
  显示局部活动量、实际任务速度、感知速度和 release 价值可能背离。
- **Agent 知识—记忆—行动架构**：[[从知识图谱到 Agent 编排]] 以权威事实、派生表示、检索、
  [[Agent 记忆架构|记忆]]、编排、[[MCP]]/[[RPA]] 行动与验证调和构成七层闭环；检索选型见 [[GraphRAG 与 Vector RAG]]；
  [[Open Knowledge Format|OKF]] 是可携带知识制品，和本仓库的边界见 [[OKF 与 llm-wiki 的关系]]。
- **Loop Engineering / 产品开发循环**：[[Loop Engineering]] 把 coding agent 的分钟级自测自修、
  开发者小时级反馈、外部用户天/周级反馈接成三层循环；[[Claude Tag 驱动的团队研发流程]]进一步把它落到
  协作频道、意图固化、Agent 路由、分层审查、内部试用和事故回灌组成的团队工作面；分钟级循环的加速器与 SDLC 载体见 [[Claude Code]]，可复用流程知识的固化格式见 [[Agent Skills]]。
- **Agent Eval 与全轨迹审计**：[[Agent 全轨迹评测与审计]] 用任务、Trace、指标和历史重评四类契约补全 [[Evals]]，强调 outcome 证明成功、trace 负责归因。
- **SDD / Agent 开发治理**：[[Specification-Driven Development]]、[[SDD 开发规范研究]] 与 [[代码与文档漂移的本质]] 将意图固化、四类漂移与持续调和连成生命周期治理；[[BMAD 项目文档治理方案]]落到文档分类、存量清理与两周试点；[[AI编码技术债的三层治理]]补出技术债、认知债与意图债，并把 RCT、遥测、安全冲突与 NIST / DORA / OpenSSF 基线压缩为意图、证据、责任三层。
  企业实例见 [[论代码与文档漂移解决方案]]、[[基于IT4IT的Agent知识治理]]、[[Anthropic-AI原生SDLC治理循环]]；授权机制见 [[控制带]]（信号强度 × 产物风险二维矩阵）。**但 SDD 收益主张的实证是负的**——见 [[SDD 收益主张的实证赤字]]。
- **落地节奏 / 生产成熟度**：[[agent-生产级落地的鸿沟]]——热度与资本高企，但真正卡点是生产级落地而非 Demo；
  Gartner、McKinsey、Deloitte 与 Meta 信号共同显示“试验广、规模化价值窄”，同时保留长期方向的乐观面。
- **Agent 的单位经济学**：[[Uber-软件工厂的成本工程]] 把 agent 花销拆成六项相乘的方程，把"agent 替自己
  多干的活"定义为浪费；机制层见 [[Agent 工具上下文膨胀]]，选型与归因纪律见 [[harness-vs-model]]。
- **AI 知识策展与研究方法论**：本 wiki 自身方法论 [[llm-wiki-方法论]]与 Stanford [[STORM-知识策展系统分析]] 互补——**STORM 强在发现、llm-wiki 强在沉淀**；
  可执行移植见 [[STORM-研究提示词组]]（检索驱动视角发现 + Moderator 挖 unknown unknowns + 异源校验替代自评）。二次传播的失真治理见 [[AI方法论的去机制化失真]]。
- **叙事、论证与知识表达**：[[叙事与故事结构方法论]] 以 Situation、Story、Discourse、Audience Effect 与 Evidence 为总骨架，建立从情境到交付的七层体系，并区分叙事理论、创作方法和表达模板。
- **AI 与儿童学习媒介**：[[书与AI的优势边界及家庭组合]] 区分书、AI、手机与阅读，主张书建知识骨架、AI 做个性化反馈、实践负责验证。

## 活跃线索
- Agent 对 SaaS 估值逻辑的再定价——已沉淀 [[cowork-saas-资本市场冲击]]；08-31 补 Q1/Q2 财报校验：UBS 提示的订单与许可
  风险**未在报表兑现**（SAP backlog 连续两季 +25%/+26% cc）但估值端未修复，叙事转为“在位者交付太慢”；下一跟踪点 Q3。
- Agent 化工作跨越技术人群边界：Codex 非开发者用户百倍增长——待跟踪企业侧渗透率（现约 17%）爬坡。
- Loop Engineering：待补 Boris Cherny / Peter Steinberger / Addy Osmani 原始论述，区分"工程闭环"与"产品反馈闭环"。
- Agent 知识架构：已完成概念边界校正；待用真实查询集验证 Vector、Text2Cypher、GraphRAG Global 与混合路由的质量/成本。
- OKF v0.2：只作为知识交换候选，不改内部 schema；待真实外部消费者出现后验证单向导出、来源/链接无损和 Knowledge Catalog 全字段往返。
- SDD：规范 v1.0 的门禁与追溯链设计不变，但**默认收益假设已被推翻**（[[SDD 收益主张的实证赤字]]：119 仓库 / 10 万 PR
  显示规格与更高返工相关）。新命题：规格换来的是可治理度更高的漂移，**只有配套建了调和机制才划算**——待对照数据。
- **AI 方法论二次传播的“去机制化失真”**：已沉淀 [[AI方法论的去机制化失真]]；上游节点 08-11 定案，08-27 确认在
  SDD 主题上复现，载体变为**检索工具的自动摘要**（无署名、无固定 URL，“找上游节点”在此失效）。M5 唯一样本 08-31
  复查证伪、降为待观察；待跟踪自动摘要载体是否再出现可确认样本。
- Demo→生产的鸿沟：已纳入 Anthropic 治理架构、Claude Code 团队访谈与 08-31 的 Uber 规模化案例（>70% PR 归因，
  但其依赖项无一来自“模型更强”）；**质量侧仍是空白**——Uber 只公布成本数字，逃逸缺陷率 / 事故率 / 人工介入率仍待跟踪。
- A²E 方法已沉淀；待在真实业务上用一个固定模型、两个 harness/policy 变体验证轨迹语义、敏感数据治理与失败分类是否可复用。

## 悬而未决的问题
- 哪些"软件股"是 system of record（安全），哪些只是可被 Agent 覆盖的功能层（危险）？
- per-seat → outcome/consumption 定价迁移的实际节奏与对倍数的影响？
- "监督式工程"下的体验下滑，是过渡期阵痛还是结构性代价？产品/组织如何对冲？
- AI 加速 coding loop 后，0-to-1 产品的 [[Evals|evals]] 如何覆盖功能正确性、体验质量与真实用户价值？
- SDD 的规格成本能被什么抵消？（原问法预设了“返工与缺陷会下降”，该前提已被最大样本证据否定）
  任务粒度的 Standard→Quick 降级阈值仍无量化切换点。
- 待写页面：[[per-seat 定价的黄昏]]、[[system-of-record 与专有数据护城河]]。
