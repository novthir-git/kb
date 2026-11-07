---
tags: [主题, 投资, AI, Agent]
created: 2026-11-07
updated: 2026-11-07
sources:
  - "[[cowork-saas-资本市场冲击]]"
  - "[[cowork-plugins-架构]]"
  - "[[MCP]]"
  - "[[常驻 Agent 的算力经济学]]"
  - "[[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要]]"
  - "[[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]]"
  - "https://www.thestar.com.my/tech/tech-news/2026/02/04/anthropic039s-new-ai-tools-deepen-selloff-in-data-analytics-and-software-stocks-investors-say （Reuters 2026-02-03 通讯稿转载；检索于 2026-11-07）"
  - "https://au.investing.com/news/stock-market-news/european-software-stocks-face-ai-concerns-ahead-of-q1-results-4361415 （Reuters 2026-04-14 署名转载；检索于 2026-11-07）"
  - "https://uk.investing.com/news/stock-market-news/morgan-stanley-flags-five-european-software-stocks-to-buy-in-secondhalf-outlook-93CH-4844605 （检索于 2026-08-31）"
  - "https://www.investing.com/news/analyst-ratings/ubs-downgrades-sap-stock-rating-on-slow-ai-rollout-concerns-93CH-4876355 （检索于 2026-08-31）"
  - "https://www.sec.gov/Archives/edgar/data/0001000184/000110465926118617/tm2628113d1_ex99-1.htm （SAP Q3 6-K exhibit 99.1；检索于 2026-11-07）"
  - "https://erp.today/sap-announces-record-third-quarter/ （二手转述 SAP Q3 电话会；检索于 2026-11-07）"
  - "https://www.3ds.com/assets/invest/2026-10/dassault-systemes-26q3-earnings_pr.pdf （检索于 2026-11-07）"
  - "https://stockanalysis.com/quote/etr/SAP/ （检索于 2026-11-07）"
  - "https://stockanalysis.com/quote/epa/DSY/ （检索于 2026-11-07）"
---

# system-of-record 与专有数据护城河

**核心论点**：Agent 把"界面 + 工作流 + 席位"这一层商品化之后，SaaS 还能守住的护城河主要有两类：
- **system of record（SoR）**：承载企业权威事实与责任边界的记录系统（ERP、总账、HR / CRM 主数据、交易与合规系统），agent 要调用它，而不是替代它；
- **agent 绕不开的专有数据**。但"有数据"本身不够，护城河得是**写入权、实时性、网络效应、合规锁定**，而不是"把数据做成好看的检索界面"。

论点源自 [[cowork-saas-资本市场冲击]] 第 6.1、6.3 节与反方节，本页汇总证据并写清改口条件。

## 别与知识治理义混用

| | 本页（市场 / 产品义） | [[知识图谱]] 的"System of Record 边界"（知识治理义） |
|---|---|---|
| 问的是 | 哪类 SaaS 在 agent 时代还能收租 | agent 知识里哪个副本是权威 |
| SoR 指 | 业务记录系统及其厂商 | 原始业务源；图谱、OKF bundle 等派生物默认不是 |
| 结论 | agent 调用它，不替代它 | 事实修正回到原始业务源，派生视图可重建 |

综合：两者在一点上相通，agent 写回的地方就是权威所在。但本页谈的是商业护城河，知识治理规则见 [[基于IT4IT的Agent知识治理]]。

## 机制：SoR 为什么留得下

- **连接层被商品化，SoR 反而更被需要**：MCP 削弱了"集成难、切换贵"的租金，但 agent "必须调用"的 SoR 因此更不可绕开（[[MCP]] 第 5 节）。
- **架构位置**：在 [[cowork-plugins-架构]] 的第 5 层，CRM、合同库、邮箱、数据仓库仍保存权威业务事实，agent 经 connector 调用它们。
- **写回边界**：agent 不只读，还可能按 connector 权限写回 SoR；是否逐次确认取决于工具、授权和组织策略（[[MCP]] 第 4 节）。综合：谁掌握写入接口和权限，谁就掌握责任边界，这是"写入权"成为护城河的机制。

## 三种失败模式（护城河不等于估值）

1. **有专有数据，却只卖检索界面**：Thomson Reuters、RELX 在 2026-02-03 单日分别跌近 18% 和 14%。它们的模式是"独家内容 + 检索界面 + 高价订阅"，被 agent 剥掉的是界面与检索那层溢价。
2. **SoR 不被替代，却因自己交付 agent 太慢被长期折价**：这是 UBS 2026-08 下调 SAP 的理由，也是 [[agent-生产级落地的鸿沟]] 的"节奏"风险落在在位者身上的形态。
3. **SoR 留下，控制层却不在它手里**：综合（置信度：中）：Microsoft Agent 365 定位为跨厂商的 agent 登记与治理层，采购时"谁拥有身份、审计与计费的控制层"可能比"谁拥有记录"更靠近决策（见 [[cowork-saas-资本市场冲击]] 第 7 节与 [[常驻 AI 同事的竞争格局]]）。

## 证据点（持续追加）

| 日期 | 来源 | 信号 | 备注 |
|---|---|---|---|
| 2026-11-06 | stockanalysis 收盘价 | SAP €210.75，年初至今约 +1%，已高于 UBS 08-26 的目标价 €201；Dassault €25.95，年初至今约 +9%，接近 52 周高点 | 年初至今按页面年初基准价计算；较 2025-10 高点仍低约 14% / 15%。股价是价格信号，不证明因果 |
| 2026-10-28 | Dassault Q3 新闻稿 | 收入 +5% cc、ARR +6%；licenses and other software 收入 +14%；全年目标上调 | 上调"includes ArisGlobal contribution"，不全是有机增长 |
| 2026-10-22 | ERP Today（转述 SAP Q3 电话会） | 本季前 50 大交易中有 9 成包含 AI 与 SAP Business Data Cloud；Joule Work Desktop 已对超过 11 万名员工上线（未说明是否为 SAP 自家员工） | 二手转述，未见于官方季报；仍没有 agent 交付数，UBS 的"交付慢"论点无法用官方数据校验 |
| 2026-10-21 | SAP Q3 6-K | CCB +26% cc，连续第三季 ≥25%；software licenses −9%，前三季 −27%；云收入含多季度追补。收购 Reltio（主数据）的理由写成让主数据"serve both traditional analytics workloads and AI agents"，Dremio（湖仓）为 AI agents 提供"governed access" | 订单端风险未兑现。许可下滑与上云迁移同向，难归因于 AI。综合：SoR 厂商在花钱把自己改造成 agent 的受治理数据层 |
| 2026-08-26 | UBS（Investing.com） | SAP 从 Buy 下调至 Neutral，目标价却从 €164 上调到 €201；理由是 SAP 自己的 agentic AI 铺得太慢（17 个已交付、15 个在 ramp，年底 200 个的目标有难度） | 风险叙事从"会不会被替代"变成"能不能把自己变成 agent 的执行层"，即失败模式 2 |
| 2026-08-24 | Morgan Stanley（Investing.com） | 称 "SaaSpocalypse" 可能被过度定价，对 SAP 等五只欧洲软件股给 Overweight；理由是开放权重模型会降低在位者的 AI 成本 | 与 UBS 同周分叉；综合：截至 11-06 的股价走势偏向 MS 一侧 |
| 2026-07（Q2） | SAP、Dassault Q2 报表 | SAP CCB +26% cc；Dassault 确认全年目标，并以 18 亿美元收购 ArisGlobal（生命科学法规与药物安全） | 数据与出处见 [[cowork-saas-资本市场冲击]] 第 4.1 节 |
| 2026-04（Q1） | SAP、Dassault Q1 报表 | SAP CCB +25% cc；Dassault upfront license +9% | 同上 |
| 2026-04-14 | Reuters（Investing.com 转载） | UBS 提示 SAP、Dassault Q1 bookings 与 licensing 收入可能偏弱；报道转引 Handelsblatt：SAP 计划限制第三方访问其系统内数据，"could help maintain its market position" | UBS 的原因是海湾冲突扰乱 3 月成交，不是 AI。综合：限制第三方数据访问，是把"数据访问权"当护城河的直接动作 |
| 2026-02-03 | Reuters 当日通讯稿 | Thomson Reuters 跌近 18%，RELX 跌 14%（将是 1988 年以来最大单日跌幅），LSEG、Experian 等跌 6%–12% | 失败模式 1 的样本：有专有数据也跌。综合：LSEG 的 6%–12% 应为盘中口径；02-04 Reuters 存档记其周二 −13%、周三 −6.9%（[[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要\|源摘要]]） |
| 2026-02-03 至 02-04 | Reuters（[[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要\|源摘要]]） | Salesforce 等跌 2%–6.6%，SAP 约 −4%；同期 Gartner 约 −21% | SoR 型标的跌幅相对小，但不能据跌幅做单因果归因 |

## 当前判断

综合（2026-11-07）：三个财报季下来，SoR 型在位者的**订单端**没有被 agent 替代的迹象。市场的问题已经从"会不会被替代"换成"能不能把自己变成 agent 的执行层或数据层"，SAP 的并购方向也指向后者。论点**成立但远未被证明**：报表只覆盖三个季度，比范式替代的时间尺度短得多。

## 改口条件

- **推翻"SoR 不被替代"**：SoR 型厂商的订单端连续两季以上明显下台阶（如 CCB / ARR 增速），且管理层或客户把原因指向 agent 绕开或替代；或者主流 agent 平台自带可审计的记录层，客户开始把权威数据迁出原 SoR。
- **推翻"写入权才是护城河、检索界面不是"**：TR、RELX 这类内容检索型厂商的订阅收入不受影响、估值完全修复，说明界面层溢价并没有被剥掉。
- **失败模式 2 升级或降级**：SAP 等年底的 agent 交付目标落空，且估值相对同业持续折价，则升级；交付兑现而折价消失，则降级。
- **失败模式 3 坐实**：采购开始以 Agent 365 这类治理层作为准入点，SoR 厂商被迫按其规则接入。届时本页要补"SoR 留下但议价权下降"。

## 待追踪

- SAP Q4 / FY（2027-01）：CCB、许可收入、agent 交付数是否达到年底目标。
- Dassault 并表 ArisGlobal 后的有机增速。
- SoR 厂商会不会对 agent 的 API / connector 调用按用量收费。常驻 agent 自身的定价已收敛到"席位或订阅 + 用量"（[[常驻 Agent 的算力经济学]]）；综合：SoR 侧若跟进，就是从"不被替代"走到"能变现"的信号。
- 主数据、数据层收购会不会成为在位者的普遍动作（SAP 之后）。

## 关联

- 母题：[[cowork-saas-资本市场冲击]]（第 4.1 节财报跟进、第 6 节相对安全类型、反方节）
- 机制：[[cowork-plugins-架构]]（第 5 层）、[[MCP]]（写回边界、连接层商品化）
- 节奏：[[agent-生产级落地的鸿沟]]
- 控制层：[[常驻 AI 同事的竞争格局]]
- 别混淆：[[知识图谱]]（SoR 的知识治理义）
