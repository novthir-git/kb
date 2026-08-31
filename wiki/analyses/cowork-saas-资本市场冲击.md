---
tags: [分析, 投资, AI]
created: 2026-07-03
updated: 2026-08-31
sources:
  - "[[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要]]"
  - "[[2026-02-03-Reuters-AI担忧重挫欧洲软件股-源摘要]]"
  - "[[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]]"
  - "https://www.anthropic.com/product/claude-cowork （检索于 2026-07-03）"
  - "https://www.anthropic.com/news/model-context-protocol （检索于 2026-07-03）"
  - "https://www.anthropic.com/research/building-effective-agents （检索于 2026-07-03）"
  - "https://support.claude.com/en/articles/13837440-use-plugins-in-claude （检索于 2026-07-16）"
  - "https://www.anthropic.com/news/google-broadcom-partnership-compute （检索于 2026-07-16）"
  - "https://es.euronews.com/business/2026/02/14/venta-masiva-en-el-sector-del-software-que-empresas-europeas-salen-peor-paradas （检索于 2026-07-16）"
  - "https://news.sap.com/2026/04/sap-announces-q1-2026-results/ （检索于 2026-08-31）"
  - "https://www.investing.com/news/company-news/dassault-systemes-q1-2026-slides-3-growth-ai-roadmap-advances-93CH-4631731 （检索于 2026-08-31）"
  - "https://news.sap.com/2026/07/sap-announces-q2-and-half-year-2026-results/ （检索于 2026-08-31）"
  - "https://www.3ds.com/newsroom/press-releases/dassault-systemes-solid-q2-results-and-confirming-full-year-objectives-delivering-ai-native-solutions-and-expanding-life-sciences-acquisition-arisglobal （检索于 2026-08-31；直连仅返回导航框架，数字经下一条幻灯片摘要核验）"
  - "https://www.investing.com/news/company-news/dassault-systemes-q2-2026-slides-ai-focus-18b-life-sciences-deal-93CH-4807945 （检索于 2026-08-31）"
  - "https://www.investing.com/news/analyst-ratings/ubs-downgrades-sap-stock-rating-on-slow-ai-rollout-concerns-93CH-4876355 （检索于 2026-08-31）"
  - "https://uk.investing.com/news/stock-market-news/morgan-stanley-flags-five-european-software-stocks-to-buy-in-secondhalf-outlook-93CH-4844605 （检索于 2026-08-31）"
  - "https://stockanalysis.com/quote/etr/SAP/ （检索于 2026-08-31）"
  - "https://stockanalysis.com/quote/epa/DSY/ （检索于 2026-08-31）"
---

# Cowork 为什么影响 SaaS 资本市场

## 核心结论

[[Claude Cowork]] 对 SaaS 资本市场的冲击，**不是因为它当前的收入规模大，
而是因为它改变了市场对 SaaS 长期估值的假设。**

- **传统 SaaS 的估值锚**：按 seat/license 持续扩张；靠工作流与数据把用户锁定；
  软件替代人力完成工作；企业长期购买多个垂直工具。
- **Cowork 代表的新趋势**：Agent 直接完成任务；用户从"使用软件"变成"分配目标"；
  多个 SaaS 的 UI 与流程被一个统一 Agent 覆盖；软件价值从 **seat-based 转向 outcome-based**。

> 一句话：Cowork 让资本市场开始怀疑——**未来企业到底要买多个 SaaS，
> 还是只要少数 seat + 更多 Agent 执行能力？**

---

## 1. Cowork 改变了 SaaS 的估值假设

Anthropic 对 Cowork 的定位是：用户给出目标，Claude 在电脑、本地文件和应用中**自主完成任务、
逐项交付成品**。所以它不是普通聊天助手，而是**任务执行者**。
（https://www.anthropic.com/product/claude-cowork）

这直接移动了"价值捕捉点"：

| 传统 SaaS 的价值锚 | Agent 型 Cowork 的价值捕捉点 |
|---|---|
| UI、工作流、数据录入 | 任务入口 |
| 权限系统、协同流程 | 工具调用、上下文整合 |
| seat 订阅 | 跨系统编排、最终结果交付 |

> 综合：当价值从"人操作界面"迁移到"Agent 交付结果"，大量 SaaS 赖以收费的那层价值被稀释。

## 2. Seat-based SaaS 模型受挑战

SaaS 过去最核心的增长故事是 **seat expansion**：公司人变多 → 使用范围扩大 →
每个员工一个席位 → **ARR 随 seat 增长**。

但 Cowork 提示了另一种模型：
- 一个 Agent 可以完成多个员工、在多个系统里的重复任务；
- 企业可能**减少 SaaS 席位数**；
- 预算从"软件许可"转向"AI 执行能力"；
- 定价从"输入端口（按人头）"转向"**每任务 / 每结果 / 每工作单元**"。

> 这类担忧的核心，是 SaaS 的**增长天花板**——seat 复利的故事被动摇。

## 3. 单个 SaaS 的产品护城河被穿透

很多 SaaS 过去售卖的是**窄工作流**：法务合同审阅、销售跟进、数据分析、营销自动化、
报告生成、文档处理、客户跟进……

但 Cowork 这类 Agent **不按单点功能组织，而是按任务组织**。例如一个"客户 Brief"任务：

```
读取客户资料 → 查阅 CRM → 汇总飞书/邮件记录
→ 生成客户 Brief → 写入信息系统 → 通知负责人
```

这些原本要跨多个 SaaS 才能完成的步骤，现在由一个 Agent 跨工具串起来。

**为什么“跨工具”这次能成立——Plugin + Connector + [[MCP]]：** 过去 AI 接系统是
**M 个应用 × N 个工具**的定制集成爆炸。MCP 让工具暴露一次 Server、应用实现一次 Client，
理论上把连接工作降为 **M + N**。但 Cowork 的 **Plugin 不是 MCP Server**：Plugin 打包 skills、
connectors、sub-agents；connector 才负责连接外部服务，custom connector 可指向 remote MCP server。
能力层依托 [[building-effective-agents|Agent 架构]] 编排这些组件。详见 [[MCP]] 与 [[cowork-plugins-架构]]。

> 结果：**单个 SaaS 的"单点定位"失效**——它从"用户直接使用的产品"退化为"Agent 编排里的一个功能层"。
> 由此引出的关键追问：**哪些 SaaS 是系统底座，哪些只是可被 Agent 覆盖的功能层？**（见第 5、6 节）

## 4. SaaS 估值中枢被压低

Reuters 报道，Cowork 插件发布后引发软件与服务板块连续抛售，数个交易日内的软件与服务板块
市值损失按不同统计口径接近 **1 万亿美元**。
（[[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要]]）

后续 2026-04-14 的 Reuters 署名报道显示，欧洲软件与 IT 服务股 2026 Q1 下跌 27%，
截至 3 月的过去 12 个月累计下跌 38%（[[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]]）。

市场反应的本质**不是短期业绩变化，而是长期估值锚变化**——以下假设被集体质疑：
- ARR 稳定性、NRR 扩张能力、seat 模型、软件 UI 护城河、部分 SaaS 的定价权。

**价格信号（反映市场重定价，不构成业务分类的因果证明）**：
- S&P 500 Software & Services 指数五个交易日跌约 13%，较 10 月峰值低 26%；
- 冲击甚至外溢到押注软件现金流的私募信贷：Blue Owl -9.8%、Ares -10.2%、KKR -9.7%。

### 4.1 2026 财报季跟进（新增于 2026-08-31）

抛售之后已过两个财报季，[[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]] 记录的
"UBS 提示 SAP、Dassault Systèmes 的 Q1 订单与许可收入风险"现在可以用实际报表校验。

- **SAP Q1（2026-04）**：current cloud backlog €21.9bn、+25% cc；cloud revenue +27% cc；
  Cloud ERP Suite +30% cc。管理层同时提示 Q2 云收入增速将回落、全年 CCB 增速逐季略微减速。
  （https://news.sap.com/2026/04/sap-announces-q1-2026-results/ ，检索于 2026-08-31）
- **Dassault Q1（2026-04-23）**：收入 €1.51bn、+3% cc；**upfront license 收入 +9%**；
  ARR €4.37bn、+6%；营业利润率 30.3%；维持全年目标（€6.29–6.41bn、3–5% cc）。
  （https://www.investing.com/news/company-news/dassault-systemes-q1-2026-slides-3-growth-ai-roadmap-advances-93CH-4631731 ，检索于 2026-08-31）
- **SAP Q2/H1（2026-07）**：cloud revenue +24% cc；current cloud backlog €22.9bn、+26% cc；
  Cloud ERP Suite +27% cc；总收入 +11% cc；non-IFRS 营业利润 +9% cc。全年非 IFRS 利润指引因
  Dremio、Prior Labs 两笔收购的摊薄而下修——**是收购摊薄，不是需求塌方**。
  （https://news.sap.com/2026/07/sap-announces-q2-and-half-year-2026-results/ ，检索于 2026-08-31）
- **Dassault Q2（2026-07-23）**：收入 €1,556m、+4% cc；云 +14%（占软件收入 27%）；
  3DEXPERIENCE +14%；订阅收入 +8%；EPS €0.31、+8%；确认全年目标；同时以 **18 亿美元**（另加
  2 亿美元与 AI 里程碑挂钩的或有对价）收购 ArisGlobal，切入生命科学法规与药物安全。
  （https://www.investing.com/news/company-news/dassault-systemes-q2-2026-slides-ai-focus-18b-life-sciences-deal-93CH-4807945 ，检索于 2026-08-31）
- **股价（2026-08-28 收盘）**：SAP（ETR:SAP）€191.32，年初至今 **-19.1%**，52 周区间
  €127.50–€244.30；Dassault（EPA:DSY）€23.09，年初至今 **-14.0%**，52 周区间 €15.83–€30.36。
  （https://stockanalysis.com/quote/etr/SAP/ 、https://stockanalysis.com/quote/epa/DSY/ ，检索于 2026-08-31）
- **卖方口径在同一周分叉**：Morgan Stanley 2026-08-24 称 "SaaSpocalypse" 可能被过度定价，
  对 SAP 等五只欧洲软件股给 Overweight，理由是开放权重模型会降低在位者的 AI 成本；
  UBS 2026-08-26 把 SAP 从 Buy 下调至 Neutral，**却同时把目标价从 €164 上调到 €201**，
  理由不是被 Agent 替代，而是 SAP 自己的 agentic AI 铺得太慢（已交付 17 个开箱即用 agent、
  15 个在 ramp，年底 200 个的目标有难度），并预期 H2 云 backlog 增速继续回落。
  （https://uk.investing.com/news/stock-market-news/morgan-stanley-flags-five-european-software-stocks-to-buy-in-secondhalf-outlook-93CH-4844605 、
  https://www.investing.com/news/analyst-ratings/ubs-downgrades-sap-stock-rating-on-slow-ai-rollout-concerns-93CH-4876355 ，均检索于 2026-08-31）

> 综合（2026-08-31）：UBS 在 2026-04 提示的**订单与许可收入风险，在报表层面没有兑现**。
> 两家公司的 Q1、Q2 都没有出现订单或许可收入塌方：SAP 的 current cloud backlog 连续两季
> +25% / +26% cc，Dassault 的 upfront license 在 Q1 还 +9%，并两次确认全年目标。
> 兑现的是**估值端而非基本面端**——两家年初至今仍分别 -19% / -14%，且 SAP 现价较 52 周低点
> 已高约 50%、较高点仍低约 22%。这与本节原判断（"定价的不是短期业绩变化，而是长期估值锚变化"）
> 一致：两个财报季既没有证实、也不足以证伪范式论断本身——若 Agent 替代 SaaS 成立，其时间尺度
> 长于两个季度，用两季报表去"证伪"是尺度错配。

> 综合（2026-08-31）：更值得记的是**风险叙事换了方向**。UBS 2026-08 的下调理由不再是
> "SAP 会被 Agent 吃掉"，而是"SAP 自己的 agent 铺不出来"。对 system-of-record 型厂商，
> 市场关心的问题已从**"会不会被替代"**变成**"能不能把自己变成 Agent 的执行层"**。
> 这对第 6.1 节是加强而非削弱——它默认了 SoR 会留下，争的只是它能否把 Agent 能力装进去；
> 但也给第 6.1 节加了一个新的失败模式：**SoR 不会被替代，却可能因为交付 Agent 太慢而被
> 长期折价**。这条正是 [[agent-生产级落地的鸿沟]] 说的"节奏"风险落在在位者身上的形态。

## 5. 最危险的 SaaS 类型

综合产品结构与本轮价格信号，风险更高的候选类型包括：

- **5.1 信息搬运型**：主要做数据汇总、搬运、报告整理，靠界面复制粘贴——**风险较高**。
  → 同轮信号：Gartner -21%、S&P Global -11%；跌幅只能证明投资者担忧，不能单独证明替代路径。
- **5.2 轻工作流型**：工作流简单、数据整合薄、主要靠 UI 模板、替换成本低——**容易被 Agent 覆盖**。
  → 后续信号：Euronews 2026-02-14 记录 Sidetrade 近 -50%、Lime -38%、cBrain -35%、
  LINK Mobility / SmartCraft 约 -32%（检索于 2026-07-16）。
- **5.3 报告/分析生成型**：输入是已有数据，输出报告/图表/摘要；用户真正要的是**结论而非工具界面**——
  被 outcome-based Agent 压缩界面溢价的风险较高。→ 同轮信号：Intuit / Equifax 各 -10%+。
- **5.4 重度 Copilot 式**：只是"给已有流程加个 AI 按钮"，没有专有数据、强流程控制权或系统记录权——
  **长期价值有限**。

## 6. 相对安全的 SaaS 类型

不是所有 SaaS 都会被攻破，更抗打的是：

- **6.1 System of Record**：ERP、财务总账、HR 主数据、CRM 主数据、交易系统、合规系统。
  它们**承载企业核心事实与责任边界**，Agent 要**调用**它们而非替代。
  → 同轮信号：Salesforce 约 -2% 至 -6.6%；但 SAP 同时受 cloud backlog 指引影响，不能据跌幅做单因果归因。
  → 2026 财报季校验见第 4.1 节：SAP 的 CCB 连续两季 +25% / +26% cc，SoR 的当期需求未被证伪；
  真正的新风险是"自己交付 Agent 太慢"而非"被 Agent 替代"。
- **6.2 强合规 / 强审计**：法务审计、财务归账、安全合规、医疗/金融核心系统。
  需可追责、可审计，Agent 可辅助但很难完全接过（呼应 Cowork “consequential decisions 留给用户”）。
- **6.3 数据壁垒型**：拥有独家行业数据、深度网络效应的 SaaS，会从"被替代对象"变成
  "**Agent 必须调用的基础设施**"。
- **6.4 Agent-native**：本身就在卖 Agent 平台/任务执行层/业务编排的公司，反而可能获得估值重估。
  → 相关信号：[[Anthropic]] 2026-04-06 官方称 **run-rate revenue** 从 2025 年底约 $9bn
  升至超过 $30bn；这不是经审计 ARR，且不能归入 2026-02-03 Reuters 报道。

## 7. 市场真正在切换的，不是 Cowork 本身，而是范式切换

Cowork 本身或许还很早期，但它传递了一个信号：
**企业软件的支出，可能从"买多个 SaaS 应用"切换到"买通用 Agent 执行能力"。**

- 过去：员工打开多个 SaaS，人操作界面完成工作；
- 未来（市场担心的方向）：员工向 Agent 分配目标，Agent 跨系统调用、直接交付结果。

> 综合：所以这轮抛售定价的不是“Cowork 今天能抢多少收入”，而是**这个范式一旦成立，
> 软件价值链里“界面 + 工作流 + 席位”这一层的经济租金要被重估。** Cowork 只是让这件事
> 第一次"看得见"。

## 反方与边界（避免单一叙事）

> ⚠️ 争议：这套"AI 替代 SaaS"叙事并非共识。
- **J.P. Morgan（Mark Murphy）**：从“Cowork 插件”外推到“人人自己写软件、抛弃 SaaS”是 **“illogical leap”**。
- **一个反常识观察**：并非"有数据就安全"。Thomson Reuters（Westlaw）**-16~18%**、
  RELX（LexisNexis）**单日 -14~17%（1988 年来最大）**、LSEG **两日 -19%**——它们都有专有数据，却跌得很惨。
  因为其模式是"独家内容 + 检索界面 + 高价订阅"打包，被 Agent 剥掉的是"界面与检索"那层溢价。
  → 第 6.3 类"数据壁垒"要安全，护城河得是**写入权/实时性/网络效应/合规锁定**，而非"把数据做成好看的界面"。
- **同期 S&P 500 创新高**（Nvidia/hyperscaler 领涨）：这是科技板块内部的再分配（AI 供给侧 vs 应用层），
  不是全面看空科技。

## 相关

- 实体：[[Anthropic]]、[[Claude Cowork]]
- 概念：[[MCP]]、[[building-effective-agents]]
- 必要对照：[[agent-生产级落地的鸿沟]] —— 本页按"能力天花板"重定价的叙事，需与该页"短期落地节奏
  显著滞后于试验渗透"的证据对照读，两条线一条定方向、一条定时机。
- 校正来源：[[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]]
- 待写（悬空链接）：[[per-seat 定价的黄昏]]、[[system-of-record 与专有数据护城河]]
