---
tags: [实体, 公司, AI, 投资标的]
created: 2026-07-03
updated: 2026-11-07
sources:
  - "https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm （检索于 2026-11-06）"
  - "https://claude.com/resources/articles/cowork-is-now-claude （检索于 2026-11-06）"
  - "https://claude.com/resources/articles/claude-duet （检索于 2026-11-06）"
  - "https://www.anthropic.com/product/claude-cowork （检索于 2026-07-03）"
  - "https://www.anthropic.com/news/google-broadcom-partnership-compute （检索于 2026-07-16）"
  - "[[2026-02-03-Reuters-AI担忧重挫欧洲软件股-源摘要]]"
  - "[[2026-07-21-Anthropic-AI原生SDLC-源摘要]]"
  - "[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]"
  - "[[2026-09-14-Anthropic-CI规模化压力-源摘要]]"
  - "https://techcrunch.com/2026/10/26/anthropics-ipo-filing-reveals-its-strategy-for-keeping-enterprise-customers-hooked/ （检索于 2026-10-27）"
  - "https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/ （检索于 2026-10-27）"
  - "[[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]]"
  - "https://claude.dev/blog/solving-code-review-at-anthropic/ （2026-10-15；检索于 2026-11-07）"
  - "https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic （2025-12-02；检索于 2026-11-07）"
---

# Anthropic

AI 公司，Claude 系列大模型的开发者。既是**技术实体**（模型、agent、协议标准的推动者），
也是**投资/商业研究标的**（其产品发布正在重塑软件行业的估值逻辑）。

## 关键产品/资产
- **Claude** 系列大模型（本 wiki 记录到 Opus 4.6 及以后）。
- **[[Claude Cowork]]**：面向非技术知识工作者的 agent 能力。2026-02 引爆软件股抛售；2026-09-16 起并入 Claude，成为默认执行层。常驻形态分为 Claude Tag（Slack，2026-06 起 beta）和 Claude Duet（独立 App，2026-10 起 research preview）。与 Grok Bot、Muse、Dots 的竞争格局见 [[常驻 AI 同事的竞争格局]]。
- **[[Claude Code]]**：面向开发者的 agentic 编码工具。
- **Claude Tag**：Slack 里的团队级常驻 agent（2026-06-23 起 public beta，归属见上方 Cowork 一条与 [[Claude Cowork]]）；
  官方 playbook 把它用作 Maintain 阶段的 on-call play。研发流程分析见 [[Claude Tag 驱动的团队研发流程]]。
- **[[MCP]]（Model Context Protocol）**：2024-11 开源的 agent↔数据/工具连接开放标准。
- 研究：[[building-effective-agents]]（agent 设计范式）。

## 商业动态
- 2026-04-06，Anthropic 官方称其 **run-rate revenue 已超过 $30bn**，高于 2025 年底约 $9bn；
  同期年化支出超过 $1m 的企业客户从 2 月的 500+ 增至 1,000+。
  （https://www.anthropic.com/news/google-broadcom-partnership-compute ，检索于 2026-07-16）
- 口径边界：run-rate revenue 是按当前收入速度年化，不等同于经审计年度收入，也不宜无说明地写成 ARR。
- 渠道竞合：Microsoft Copilot Cowork 采用 Claude Cowork 的执行框架，但 Microsoft 同时加入 GPT 和 Grok 模型对冲，管理员可以关闭 Anthropic 模型族。在 Microsoft 体系里，Anthropic 正从"技术来源"退为"可替换的模型供应商之一"（推断，见 [[常驻 AI 同事的竞争格局]]）。

### 2026-10 IPO S-1 披露

2026-10-26 向 SEC 提交 S-1（EDGAR CIK 2130357，accession 0001628280-26-067168）。以下数字出自 TechCrunch 对 S-1 的
解读；S-1 正文篇幅过大，本次未逐字复核，仅核实了申报文件确实存在。
（https://techcrunch.com/2026/10/26/anthropics-ipo-filing-reveals-its-strategy-for-keeping-enterprise-customers-hooked/ ，
https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/ ，均检索于 2026-10-27）

- **收入**：2026 上半年 $16.3bn，上年同期 $1.2bn。这是确认收入，和 04 月的 run-rate（>$30bn 年化）口径不同，不能直接对比。
- **客户规模**（截至 09-30）：年消费 ≥$100k 的客户 11,900+，≥$1M 的 1,900+，≥$10M 的约 250。
  对比 04 月"年化 >$1m 客户 1,000+"，半年内大约翻了一倍（两者口径接近但不完全相同）。
- **净收入留存率**：Q3 末约 900%，公司归因于客户在组织内扩大部署带来的用量扩张。
- **交叉销售漏斗**：$100k+ 客户中，同时使用 Claude Platform 和一方应用（[[Claude Code]] 或 [[Claude Cowork]]）的
  超过一半，上年末约 30%。Q3 使用 Claude Code 的前 5% Enterprise 客户，人均月消费约为不用 Claude Code 的普通
  企业用户的 20 倍。
- **结构性风险（公司自陈）**：通过 AWS、Google Cloud、Azure 联合销售（Anthropic 持有客户合同、向云厂商付费），
  但这三家云厂商越来越把 Anthropic 视为竞争对手，可能优先满足自身或其投资的竞品，进而让 Anthropic 更难拿到所需算力；
  另披露大客户需求变化的集中度风险。
- **补充（2026-11-06 研究）**：11-02 另提交 S-1/A；S-1 称 Cowork 的采用速度超过 Claude Code 同期，且不按产品拆分收入
  （见 [[常驻 AI 同事的竞争格局]]）。

综合：这组数字是 [[cowork-saas-资本市场冲击]] 价值捕获问题的量化锚点：一方应用（Claude Code / Cowork）在拉动
平台消费，收入扩张来自**用量**而非席位。但另一面，算力供给依赖的正是三家潜在竞争者，"模型厂商 vs 云厂商"的
渠道冲突第一次以监管披露的形式出现。900% NRR 和 20 倍都是公司自选口径，定义细节以 S-1 原文为准。

> ⚠️ 溯源修正：旧版把 $9bn → $30bn 归入 2026-02-03 Reuters/UBS 来源；该时间线不成立，
> 已改引 Anthropic 2026-04-06 官方公告。原 raw 重建稿只读保留，矛盾见
> [[2026-02-03-Reuters-AI担忧重挫欧洲软件股-源摘要]]。（发现于 2026-07-16）

## 影响
- 其 2026-02 的 [[Claude Cowork]] 插件发布被 Reuters 称为软件业的 "wake-up call"，
  详见 [[cowork-saas-资本市场冲击]]。

## AI 原生软件工程

- 2025-12-02 的内部调查（2025-08，132 名工程师与研究员）给出"高用量、低完全委派"的对照：自报约 59% 的工作
  使用 Claude、生产力 +50%，但超过一半的人能"完全委派"的工作只占 0–20%。口径：非匿名自报；
  2025-08 为 Sonnet 4 / Opus 4 时期。→ 见 [[agent-生产级落地的鸿沟]] 证据点表。
- 2026-07，Anthropic 公开其内部 AI 原生 SDLC：截至 5 月约 80% 的已合并生产代码行归因于 Claude，
  同时用风险分级、确定性检查、隔离环境、独立身份、人工门禁和 SIEM 约束生成、审查与事故响应。
- 口径边界：80% 是公司自报的代码行归因，不是 80% 的工程判断或部署权限自动化；完整分析见
  [[Anthropic-AI原生SDLC治理循环]]。
- 同月 Claude Code 团队称，其内部 Claude Tag 提交该团队 **65% 的产品工程 PR**；核心区域仍由 code owner
  人工批准，外围变更经过六个多月的验证后才逐步交给自动 review。65% 只覆盖 Claude Code 产品工程团队，
  也是员工自报口径，不代表全公司 PR 比例或无人审查比例。→ 见
  [[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]，完整流程分析见
  [[Claude Tag 驱动的团队研发流程]]。
- 2026-08-21，官方发布六阶段 AI-native SDLC playbook：16 个 play，其中 13 个附 leading / lagging indicator，
  但全文零实测值，是度量框架而非效果证据；Stage 6 的确定性授权机制单独收在 [[控制带]]。
  → 见 [[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]]。
- 2026-08-13，Boris Cherny 自述用**每日 routines** 维护自家 app（死代码删除、重复统一等十余类），数周开 388 个 PR、
  合并 180 个，每个 PR 过 Claude Code Review 加人工复审。→ 见 [[Agent 不会自发偿还结构债]]。
- 2026-09-14，官方工程博客首次公开这套高出码密度的**下游代价**：6 个月内 **CI job 数涨 25 倍**，
  人均季度出码量为 2021–2025 的 8 倍、其中 **80% 由 Claude 撰写**，测试总量涨 10 倍，
  而工程师人数只有 "nominal" 增加。决定"每个 PR 跑哪些测试"的测试影响分析服务因此被压垮，
  三次临时补丁（加大机器 / 分片 / 每日重启）分别只撑了 70 天、29 天、不到 1 天，最终靠架构重写
  （无状态 worker + 内存数据存储 + 日志定期汇总）解决，单人 3 周完成。原文明示新架构**运行成本更高**。
  → 见 [[2026-09-14-Anthropic-CI规模化压力-源摘要]]。
- 口径边界：单一公司自报、无第三方审计；Anthropic 是 AI 出码密度的极端值（80%），25× 这个倍数
  不宜外推到 AI 代码占比更低的团队。该源证明的是"基建被压垮并被重写"，不是"重写后质量更好"——
  它没有给出逃逸缺陷率或事故率。
- 2026-10-15，code review 博客：约 90% 的 Claude Code 自身代码由 Claude 编写（原文 "we've said before" 的转述）；
  6–9 月该代码库合并 PR 翻倍以上、需回退的占比降超 40%；风险分级由分类器按变更判定，中风险一人、高风险两人批准。
  口径边界：90% 指 Claude Code 代码库（2026-10），80% 指全公司已合并生产代码行（截至 2026-05），范围不同、
  不矛盾，也不可互换；回退占比是自报相对降幅、无对照，不是逃逸缺陷率或事故率。
  → 见 [[Anthropic-AI原生SDLC治理循环]]、[[全AI代码库的治理决策]]。

> ⚠️ 矛盾：同一个 "8×" 出现在两个不同口径上——[[2026-07-21-Anthropic-AI原生SDLC-源摘要]] 称
> "每名工程师**每日合并代码行**约为 **2024 年**的 8 倍"，[[2026-09-14-Anthropic-CI规模化压力-源摘要]]
> 称"人均**季度出码量**为 **2021–2025** 的 8 倍"。分母（日/季度）与基线（单年/五年区间）都不同，
> 两者不可互换或叠加；引用任一处都必须带上其自身口径。（发现于 2026-09-16）
