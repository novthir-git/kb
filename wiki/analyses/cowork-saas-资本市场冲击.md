---
tags: [分析, 投资, AI]
created: 2026-07-03
updated: 2026-11-07
sources:
  - "[[常驻 Agent 的算力经济学]]"
  - "[[system-of-record 与专有数据护城河]]"
  - "https://www.sec.gov/Archives/edgar/data/0001000184/000110465926118617/tm2628113d1_ex99-1.htm （SAP Q3 6-K exhibit 99.1；检索于 2026-11-07）"
  - "https://news.sap.com/2026/10/sap-announces-q3-2026-results/ （检索于 2026-11-07）"
  - "https://www.3ds.com/newsroom/press-releases/dassault-systemes-strong-q3-performance-improved-fy26-objectives-and-step-change-life-sciences （检索于 2026-11-07）"
  - "https://www.3ds.com/assets/invest/2026-10/dassault-systemes-26q3-earnings_pr.pdf （Dassault Q3 新闻稿全文 PDF；检索于 2026-11-07）"
  - "https://www.thestar.com.my/tech/tech-news/2026/02/04/anthropic039s-new-ai-tools-deepen-selloff-in-data-analytics-and-software-stocks-investors-say （Reuters 2026-02-03 通讯稿转载；检索于 2026-11-07）"
  - "https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/ （检索于 2026-11-06）"
  - "https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models （检索于 2026-11-06）"
  - "https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/ （检索于 2026-11-06）"
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
  - "https://stockanalysis.com/quote/etr/SAP/ （检索于 2026-08-31；2026-11-07 再检索）"
  - "https://stockanalysis.com/quote/epa/DSY/ （检索于 2026-08-31；2026-11-07 再检索）"
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

> ⚠️ 矛盾：本页把方向写作"seat-based 转向 outcome-based"，但 2026-06 至 11 月常驻 agent 的实际定价显示另一回事：
> - Copilot Cowork 是席位许可加 Copilot Credits；
> - Grok Bot、Muse 用每周额度或 token；
> - Dots、Claude 是高阶订阅加用量池。
>
> 收敛的是"**席位 / 订阅 + 用量**"，没有一家主流厂商落地按结果计价。近期兑现的是 consumption，不是 outcome。"outcome-based"应视为待验证的长期方向，而不是已发生的迁移（证据见 [[常驻 Agent 的算力经济学]]）。（发现于 2026-11-06）

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

### 4.1 2026 财报季跟进（新增于 2026-08-31；Q3 补于 2026-11-07）

抛售之后已过三个财报季，[[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]] 记录的
"UBS 提示 SAP、Dassault Systèmes 的 Q1 订单与许可收入风险"现在可以用实际报表校验。
注意 UBS 当时给的原因是海湾冲突扰乱了 3 月成交，不是 AI（见该源摘要）。

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
- **SAP Q3（2026-10-21）**：current cloud backlog €24.1bn、+28%、**+26% cc**，与 Q2 持平；
  cloud revenue €6,668m、+26% / +25% cc；Cloud ERP Suite +28% cc；总收入首次超过 €100 亿、+12% cc；
  non-IFRS 营业利润 +18%。全年 cloud revenue 指引改为 "towards the upper end of the outlook range
  of €25.8 – 26.2 billion"，全年 CCB 增速仍指引"略微减速"。三个口径要一起看：
  - 6-K 自述云收入增长受季度性因素推高，"mainly a multi-quarter revenue catch-up from customers
    returning from financial distress"；
  - **software licenses 收入 €147m、同比 −9%（cc −9%）**，前三季累计 −27%（cc −26%）；
  - 本季总收入含 Reltio、Dremio、Prior Labs 三笔收购贡献的 €49m。
  （SEC 6-K exhibit 99.1：https://www.sec.gov/Archives/edgar/data/0001000184/000110465926118617/tm2628113d1_ex99-1.htm 、
  https://news.sap.com/2026/10/sap-announces-q3-2026-results/ ，均检索于 2026-11-07）
- **Dassault Q3（2026-10-28）**：收入 €1.55bn、软件收入 €1.39bn，均 +5% cc；ARR €4.50bn、+6%；
  3DEXPERIENCE 软件收入 +25%，云软件 +14%；**licenses and other software 收入 €219m、+14%**；
  营业利润率 31.6%（+150 bps），EPS €0.32、+8%。全年目标上调为收入 €6.399–6.459bn（+4–5%，原 3–5%）、
  营业利润率 32.5–32.7%、EPS +6–7%，但原文写明 "This includes ArisGlobal contribution"：ArisGlobal
  9 月下旬完成交割，Q4 指引的 5–8% 增长里约 2 个点来自它，上调不全是有机增长。
  （https://www.3ds.com/newsroom/press-releases/dassault-systemes-strong-q3-performance-improved-fy26-objectives-and-step-change-life-sciences 、
  https://www.3ds.com/assets/invest/2026-10/dassault-systemes-26q3-earnings_pr.pdf ，均检索于 2026-11-07）
- **股价（2026-08-28 收盘）**：SAP（ETR:SAP）€191.32，52 周涨跌 **-19.1%**，52 周区间
  €127.50–€244.30；Dassault（EPA:DSY）€23.09，52 周涨跌 **-14.0%**，52 周区间 €15.83–€30.36。
  （https://stockanalysis.com/quote/etr/SAP/ 、https://stockanalysis.com/quote/epa/DSY/ ，检索于 2026-08-31）
  > 修订（2026-11-07）：本条原把 -19.1% / -14.0% 写成"年初至今"，实为 52 周涨跌幅。按 stockanalysis
  > 页面的年初基准价（€208.35 / €23.84）计算，08-28 的年初至今应为 **-8.2% / -3.1%**。
- **股价（2026-11-06 收盘）**：SAP €210.75，年初至今约 **+1.2%**，52 周涨跌 -7.6%，52 周区间
  €127.50–€226.85；Dassault €25.95，年初至今约 **+8.9%**，52 周涨跌 +8.2%，接近 52 周高点 €26.27。
  年初至今是按上述基准价算出的值。（同上两页及其 statistics 页，检索于 2026-11-07）
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
>
> 修订（2026-11-07）：上段有两处不准。一是"Q1、Q2 都没有出现许可收入塌方"只看了 Dassault；
> SAP 的 software licenses 收入其实一直在跌（按 Q3 季报的前三季累计与 Q3 单季倒算，H1 约 −34%，
> 综合：倒算值）。二是"年初至今 -19% / -14%"实为 52 周涨跌，年初至今应为 -8% / -3%。

> 综合（2026-11-07，三个财报季）：**订单端的风险仍未兑现**。SAP 的 current cloud backlog 连续三季
> +25% / +26% / +26% cc，UBS 08-26 预期的 H2 回落没有在 Q3 出现；Dassault 三季都确认或上调全年目标。
> 但方向并不完全一致，准确说法是：**backlog 与云增长延续，许可收入下滑，指引上调部分来自并购**。
> - 许可收入要分开看：SAP 的 software licenses Q3 −9%、前三季 −27%，Dassault 的 licenses and other
>   software Q3 反而 +14%。SAP 的下滑与它多年推动的上云迁移同向（6-K 也预期 support 收入会因客户加速
>   上云而加速下滑），无法单独归因于 Agent 替代。
> - 两处要打折：SAP Q3 云收入含多季度追补；Dassault 上调的目标含 ArisGlobal 贡献。
> - 估值端也变了：截至 11-06，SAP 年初至今约 +1%、Dassault 约 +9%，较 08-28 分别回升约 10% / 12%，
>   但较 2025-10 高点仍低约 14% / 15%。08-31 所说的"估值端未修复"已不成立，更准确的是"年内跌幅已收复，
>   前高未收复"。股价只是价格信号，不证明因果。
>
> 范式论断的时间尺度仍长于三个季度，三季报表依然不足以证伪它。下一跟踪点是 Q4/FY（2027-01）。

> 综合（2026-08-31）：更值得记的是**风险叙事换了方向**。UBS 2026-08 的下调理由不再是
> "SAP 会被 Agent 吃掉"，而是"SAP 自己的 agent 铺不出来"。对 system-of-record 型厂商，
> 市场关心的问题已从**"会不会被替代"**变成**"能不能把自己变成 Agent 的执行层"**。
> 这对第 6.1 节是加强而非削弱——它默认了 SoR 会留下，争的只是它能否把 Agent 能力装进去；
> 但也给第 6.1 节加了一个新的失败模式：**SoR 不会被替代，却可能因为交付 Agent 太慢而被
> 长期折价**。这条正是 [[agent-生产级落地的鸿沟]] 说的"节奏"风险落在在位者身上的形态。

> 综合（2026-11-07）：SAP 的 Q3 季报与新闻稿都没有给出 agent 交付数，UBS"agent 铺得太慢"的论点
> 无法用 Q3 官方数据校验。同一份 6-K 给了另一种证据：SAP 把 Reltio（主数据管理）收购的理由写成让客户的
> 主数据成为"serve both traditional analytics workloads and AI agents"的可信数据产品，把 Dremio（湖仓）
> 写成为 AI agents 提供"governed access"。SoR 厂商正在花钱把自己改造成 agent 的受治理数据层。
> 这条线索的证据与改口条件汇总在 [[system-of-record 与专有数据护城河]]。

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
  → 2026 财报季校验见第 4.1 节：SAP 的 CCB 连续三季 +25% / +26% / +26% cc，SoR 的当期需求未被证伪；
  真正的新风险是"自己交付 Agent 太慢"而非"被 Agent 替代"。论点页见 [[system-of-record 与专有数据护城河]]。
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

**2026-11 补：租金不只从 SaaS 流向 agent，也在 agent 厂商之间流向控制层。**
- Microsoft 的 Agent 365（2026-05-01 GA，$15/用户/月）定位为跨厂商的 agent 登记与治理层。截至 11-03 已接入 Agentforce、Bedrock、Anthropic、Gemini 等，OpenAI 仍在计划中。
- Copilot Cowork 采用 Claude Cowork 的执行框架，但模型选择器已加入 GPT 6.1 Sol 和 Grok 4.7，管理员可以一键关闭 Anthropic 模型族。

推断（置信度：中高）：在大企业的采购路径里，"谁的 agent 最好"会让位给"谁拥有身份、审计与计费的控制层"。agent 能力本身也在被商品化，所以本页 §6"相对安全的 SaaS"清单里，应当加上身份与治理层这一类。详见 [[常驻 AI 同事的竞争格局]]。

## 反方与边界（避免单一叙事）

> ⚠️ 争议：这套"AI 替代 SaaS"叙事并非共识。
- **J.P. Morgan（Mark Murphy）**：从“Cowork 插件”外推到“人人自己写软件、抛弃 SaaS”是 **“illogical leap”**。
- **一个反常识观察**：并非"有数据就安全"。Thomson Reuters（Westlaw）**-16~18%**、
  RELX（LexisNexis）**单日 -14~17%（1988 年来最大）**、LSEG **两日约 -19%**（周二 -13%、周三 -6.9%，
  据 [[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要]]；综合：两日为累计值）——它们都有专有数据，却跌得很惨。
  （Reuters 02-03 当日通讯稿写 LSEG、Experian 等"fell between 6% and 12%"，综合：应为盘中口径。出处：
  https://www.thestar.com.my/tech/tech-news/2026/02/04/anthropic039s-new-ai-tools-deepen-selloff-in-data-analytics-and-software-stocks-investors-say ，检索于 2026-11-07）
  因为其模式是"独家内容 + 检索界面 + 高价订阅"打包，被 Agent 剥掉的是"界面与检索"那层溢价。
  → 第 6.3 类"数据壁垒"要安全，护城河得是**写入权/实时性/网络效应/合规锁定**，而非"把数据做成好看的界面"。
- **同期 S&P 500 创新高**（Nvidia/hyperscaler 领涨）：这是科技板块内部的再分配（AI 供给侧 vs 应用层），
  不是全面看空科技。

## 相关

- 实体：[[Anthropic]]、[[Claude Cowork]]
- 常驻 agent 格局与定价证据：[[常驻 AI 同事的竞争格局]]、[[常驻 Agent 的算力经济学]]
- 概念：[[MCP]]、[[building-effective-agents]]
- 必要对照：[[agent-生产级落地的鸿沟]] —— 本页按"能力天花板"重定价的叙事，需与该页"短期落地节奏
  显著滞后于试验渗透"的证据对照读，两条线一条定方向、一条定时机。
- 校正来源：[[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]]
- 论点页：[[system-of-record 与专有数据护城河]]（第 4.1、6.1、6.3 节与反方节的 SoR 线索汇总于此）
- 定价迁移：原待写的"per-seat 定价的黄昏"已撤销（2026-11-07），论点并入 [[常驻 Agent 的算力经济学]]
  （定价收敛到席位/订阅 + 用量，按结果计价缺席）与本页开头的 ⚠️ 矛盾
