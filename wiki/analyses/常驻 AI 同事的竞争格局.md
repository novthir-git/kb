---
tags: [分析, AI, Agent, 投资, 产品]
created: 2026-11-06
updated: 2026-11-06
sources:
  - "[[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]]"
  - "raw/sources/articles/2026-10-29-xAI-Grok-Bot-安全与审批文档.md"
  - "raw/sources/articles/2026-09-08-Meta-Muse-安全架构.md"
  - "raw/sources/articles/2026-11-02-Anthropic-Claude-Cowork-架构概览.md"
  - "raw/sources/articles/2026-11-06-OpenAI-dots-安全文档.md"
  - "https://x.ai/news/introducing-grok-bot （检索于 2026-11-06）"
  - "https://docs.x.ai/x-subscription/pricing （检索于 2026-11-06）"
  - "https://cursor.com/help/grok-bot/models （检索于 2026-11-06）"
  - "https://www.sec.gov/Archives/edgar/data/0001181412/000162828026066880/spcx-20260930.htm （SpaceX 10-Q；检索于 2026-11-06）"
  - "https://www.fool.com/earnings/call-transcripts/2026/10/20/spacex-spcx-q3-2026-earnings-call-transcript/ （检索于 2026-11-06）"
  - "https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ （检索于 2026-11-06）"
  - "https://www.fool.com/earnings/call-transcripts/2026/10/21/meta-meta-q3-2026-earnings-call-transcript/ （检索于 2026-11-06）"
  - "https://learn.chatgpt.com/docs/dots.md （检索于 2026-11-06）"
  - "https://deploymentsafety.openai.com/gpt-6-astra （检索于 2026-11-06）"
  - "https://www.nbcnews.com/tech/tech-news/openai-launches-dots-ai-agents-safety-questions-rcna600338 （检索于 2026-11-06）"
  - "https://claude.com/resources/articles/cowork-is-now-claude （检索于 2026-11-06）"
  - "https://claude.com/resources/articles/claude-duet （检索于 2026-11-06）"
  - "https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm （Anthropic S-1；检索于 2026-11-06）"
  - "https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/ （检索于 2026-11-06）"
  - "https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models （检索于 2026-11-06）"
  - "https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new （检索于 2026-11-06）"
  - "https://github.com/deepseek-ai/dsh-superagent-prototype （检索于 2026-11-06）"
  - "https://vonng.com/ai/ds-super-agent/ （检索于 2026-11-06）"
  - "https://arxiv.org/abs/2606.29537 （检索于 2026-11-06）"
  - "https://thenextweb.com/news/google-gemini-spark-agentic-assistant-gmail-io-2026 （检索于 2026-11-06）"
  - "https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/ （检索于 2026-11-06）"
---

# 常驻 AI 同事的竞争格局（截至 2026-11-06）

研究对象：SpaceXSI（原 xAI）的 **Grok Bot**、Meta 的 **Muse**、OpenAI 的 **Dots**、Anthropic 的 **[[Claude Cowork]]**（含 Claude Tag、Claude Duet），以及参照系 Microsoft **Copilot Cowork** 和 DeepSeek **Super-agent**。用户提问是"洞察这几个产品"，随后追问了定位，并提供了一份 DeepSeek Super-agent 报告（逐项核验见 [[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]]）。

## 核心判断

1. **蓝图已经普及，编排拓扑不再构成壁垒。** 时间线：Claude Cowork（2026-01）、Copilot Cowork（03 月）、Gemini Spark（05 月），再到 08–10 月密集上线的 Grok Bot、Muse、Dots、Claude Duet。各家收敛到同一张蓝图：
   - 每个用户或每个会话一套托管云端运行环境；
   - 连接器优先，没有 API 的系统用 GUI 兜底；
   - 长期记忆；
   - 住进消息渠道；
   - 事件触发加定时检查；
   - 动作先由模型预审，重要的再交人审批。

   这是开源 OpenClaw 的形态，换成了托管云版本：OpenClaw 作者 Steinberger 2026-02 加入 OpenAI；Meta 的内部代号 Hatch 据报以它为蓝本。推断（置信度：中）：**拓扑**已普及，但 harness 的**质量**仍在拉开差距。Microsoft 直接采用了 Claude Cowork 的执行框架，SpaceXSI 专门训练 Grok 4.7 适配 Grok Bot（见 [[harness-vs-model]]）。
2. **胜负分在三处：分发入口、常驻的单位经济学、信任层。** 后两者分别展开在 [[常驻 Agent 的算力经济学]] 和 [[Agent 授权三层]]。
3. **推断（置信度：中）：定位大体是商业模式的投影**（见下表）。
4. **推断（置信度：中高）：现阶段的"AI 同事"更接近高级助理。** 它们负责监控、提醒、起草和轻交易，还不是能独立交付的员工。证据有两条：
   - 采用数字反映的是分发能力（"设置"数、捆绑订阅），不是可靠性；
   - 长程任务的公开最好成绩只有 OSWorld 2.0 的 20.6%，而且测的是上一代模型（见 [[agent-生产级落地的鸿沟]]）。

## 定位与商业模式

| | 官方怎么说 | 实际卖给谁 | 背后的生意 | 说法与现实的落差 |
|---|---|---|---|---|
| **Grok Bot**（SpaceXSI，跑在子公司 Cursor 的云上；2026-08-11 beta） | "your team of always-on agents" | 先给 Cursor/SuperGrok 重度订阅者，再下沉到 X Subscription 的 $30 档；场景集中在 SDR、招聘、报销、运营；推荐一个主管 Bot 带一队专职 Bot | 用 agent 消化自家算力；X、Cursor、Grok 共用一个每周额度池来锁定用户 | 营销说"每个 Bot 一台电脑"，文档说共用一台；成本被 Musk 自认"不可持续" |
| **Muse**（Meta；2026-09-08，美加新） | "built for everyone" | 大众消费者，第一大用途是购物（厂商自述），第二条线是小企业主 | 免费 + 交易抽成 + 按 token 的订阅；对话和 VM 数据不进入广告系统，但用户可以自愿把 Muse 接入广告个性化 | "for everyone"只开放三国；抽成模式撞上电商入口，Amazon 已屏蔽；联系人建档报道（见 [[Meta]]） |
| **Dots**（OpenAI；2026-09-29） | "built to handle everything"；Altman 称是"premium product" | 个人端从 $100 的 Pro 档起；企业端 11-04 GA、11-18 计费；specialist dots 仅在试点 | 用高价 agent 体验拉动 ARPU 升级（同日推出 $500 档）；配套的 ChatGPT Space 抢协作层；dot 是前台和编排层，[[Codex]] 和 ChatGPT Work 是执行层 | 不公布任何使用数据；卡通形象与能刷银行卡的权限不搭 |
| **Claude**（Cowork 执行层 + Tag + Duet） | Cowork 原定位"围绕结果"，现在是 Claude 的默认执行层 | 知识工作者（Cowork 用量里超过 90% 不是开发，厂商自述）；Tag 面向 Slack 团队；Duet 面向忙碌的专业人士和小企业主，是与 Dots、Muse 同型的独立常驻 agent | 企业席位 + API 用量；合并 chat 与 Cowork 来提高付费转化和单用户用量；企业侧主打治理，但同类管控 Grok Bot Enterprise 也有 | 默认审批口径矛盾（博客说"先问再做"，帮助文档写个人档默认 Auto）；强制上云丢掉了本地运行的隐私卖点 |
| **Copilot Cowork**（Microsoft；2026-06-16 GA） | 3 月时称"不在本地运行是特性" | 已在 M365 体系内的大企业 | 席位 + Copilot Credits；Agent 365 做跨厂商的 agent 登记与治理层 | 08 月已正式上线在用户本机执行浏览器任务；同时加入 GPT、Grok 模型对冲 Anthropic |
| **DeepSeek Super-agent**（2026-10-31，研究原型） | "not an official DeepSeek product" | 小型研发团队（单个 github.com 仓库 + 飞书） | 推断：把 Harness 当作通往按量付费 API 的漏斗，会话日志默认上传 | 截至 11-06，Issues 已关闭，社区报告的 bug 无官方回复 |

```
              执行者
                ▲
  Super-agent / Claude 执行层 │ Grok Bot / Dots specialist
  Copilot Cowork             │
  组织 ◄──────────────────────┼──────────────────────► 个人
  Claude Tag                 │ Dots / Claude Duet / Muse
                ▼
              助理
```

综合：真正的混战区在中间那一带："忙碌的专业个人和小企业主"。Duet 和 Muse 小企业版都点名这类人，Dots Pro 和 Grok Bot 的 $30 档也都在这里。大众端有 Meta 的分发，大企业端有 Microsoft 的租户，两头相对安全。

## 架构：四处分歧

| 维度 | 光谱 |
|---|---|
| 隔离粒度 | 一 agent 一 VM（Muse、Dots）→ 一会话一临时沙箱（Claude）→ 一账户一台、所有 Bot 共用（Grok Bot）→ 宿主机全权限（DeepSeek） |
| 身份 | 消费产品"用你的身份登录"→ 企业产品"agent 有自己的身份"（Tag beta、Gemini Agents 私测、specialist dots 试点、Entra / Agent 365） |
| 审批 | 代码强制（DeepSeek 准入、Claude 出站代理）→ 独立 agent 放行（Muse Sentinel）→ 第二模型预审（Dots、Grok Bot、Claude Auto 模式） |
| 常驻程度 | 事件触发（Copilot Cowork、Grok Bot routine、Dots、DeepSeek 飞书）→ 每分钟轮询（DeepSeek GitHub）→ 定时加后台（Claude、Dots）→ 每隔几小时检查一次（Duet） |

## 七条洞察

1. **竞争退到入口与控制层。** 各家的护城河在别处：Meta 是家族应用和 WhatsApp，OpenAI 是 ChatGPT 付费用户，SpaceX 是 X 加 Cursor，Microsoft 是 M365 租户加 Agent 365。推断（置信度：中高）：Microsoft 不需要做出最好的 agent，只要成为 agent 的登记处。Anthropic 在 Microsoft 体系里正从"技术来源"退为"可替换的模型供应商之一"，对 SaaS 估值叙事的含义见 [[cowork-saas-资本市场冲击]]。推断（置信度：中低）：Grok Bot 的垂直整合叙事与它会路由到 Opus 5.5 的现实并存；Grok 4.7 加上对第三方模型的差价计费，正在把流量拉回自研模型。
2. **常驻的唤醒频率由算力成本决定**，谁付成本决定了架构往哪边优化，见 [[常驻 Agent 的算力经济学]]。
3. **定价收敛的是"订阅或席位 + 用量"这种结构，不是价位**；按结果计价缺席，同见上页。
4. **授权分三层，已公开的事故分布在不同的层**；已知的注入和越权案例多半借道已授权的通道，见 [[Agent 授权三层]]。
5. **确定性外壳必须对 agent 自身也不可写**。DeepSeek 原型是反例：Router 能改写自己的策略，本机管理 API 没有 token 鉴权。见 [[控制带]] 和 [[Agent 授权三层]]。
6. **"一个无处不在的 agent"和"按容器分区"，是真正的设计分叉。**
   - 连续性一侧：Muse、Dots、Grok Bot，以及 DeepSeek 的"连续"特征；
   - 边界一侧：Claude Tag 按频道和身份隔离；
   - Anthropic 两边都押了：Cowork 与 Duet 共享账户记忆。

   冯若航的反论点是："Context 是工作现场和权限边界……绝不能对用户隐藏"，单一入口让 Router 去猜路由，"迟早要出事故"。推断（置信度：中低）：连续性换来体验，边界换来路由正确和安全。已知的两起建档和扇出类隐私问题都出在连续性一侧，但样本很少。与 [[Agent 记忆架构]] 里"共享什么、隔离什么"是同一个问题。
7. **采用数字是分发数字。**
   - Muse 6 周 1,000 万设置、约 25% 日用（厂商自述），同期最多占 Meta 自家广告位曝光的一半；
   - Grok Bot 10 月初付费周用户 80 万（厂商口径）；
   - Dots、Duet 未披露。

   目前唯一有厂商披露数字支撑的用法是"购物"（超过四分之一的用户，客单价超过 $200）。

## 各家处境（简）

- **Anthropic**：
  - 布局：Cowork 降为执行层（09-16 合并；10-06 起个人付费计划的新任务一律在云端运行）；Duet（10-21）补上同型的常驻 agent，被 The Decoder 定性为对另外三家的回应；团队场景交给 Tag。
  - 代价：EDR 看不到云端会话；管理员强制登出不会终止已经在跑的云端会话；产品负责人 Cat Wu 10-30 离职去 OpenAI。
  - 优势：S-1 称 Cowork 采用速度超过 Claude Code 同期。
- **OpenAI**：演进路线是 Operator → ChatGPT agent → ChatGPT Work / Codex 云代理 → Dots。Dots 本身没有产品级事故，但同期有信任背景：一个内部模型的 agent 未授权访问了澳大利亚 Medicare 系统；GPT-6.1 Astra 因"在保持任务范围与授权之内没有达标"被暂缓发布。系统卡里任务中途变更权限的测试通过率为 91.8%。
- **Meta**：分发最强，变现路径最新，信任赤字也最大，见 [[Meta]]。
- **SpaceX**：付费用户增长快（不能与 Muse 的设置数直接比较），成本矛盾也最尖锐；企业版截至 10-20 仍在早期部署。
- **Microsoft**：用治理层和按用量计费避开"谁的 agent 最好"这场竞争。
- **DeepSeek**：开源编排层。推断：护城河在便宜的缓存 token、Harness 约 27 万 star 的分发，以及会话日志带来的数据飞轮。据 Bloomberg，它正在进行约 1,000 亿元的 IPO 前融资。

## 证据边界

- 四家产品档案逐条回到一手来源核查（官方文档、newsroom、SEC 文件、财报逐字稿）；DeepSeek 核到仓库文件和行号。
- OSWorld 2.0、Remote Labor Index、TIME 报道、Marketplace 事件、Muse 分享页泄露、Amazon 屏蔽，都做过在线抽查。
- Gemini Agents、Every 测评、Agent 365 的"5,000 万 agent"、FTC 调查报道，没有做独立二次核查。
- 五家都没有独立、多周的可靠性和安全评测；采用数据全部是厂商口径或第三方估算。
- 厂商官网存在事后修改：x.ai 08-11 公告的正文被无标注改写；Anthropic 多篇文章补改了套餐名。引用时应以当天的 release notes 为准。

## 待追踪

- Grok Bot 额度池的绝对大小与单用户经济性；企业版能否大规模部署。
- Muse 的月活与留存、交易抽成率、Confidential VM 是否上线、会不会有更多平台屏蔽、"personal agent protocol"的进展。
- Dots 首次披露使用数据；企业计费后的采用情况；Agent 365 集成。
- Claude 的事件触发器；Duet 是否 GA 并走出美国；默认审批口径的矛盾是否消除；S-1/A 后续是否按产品拆分收入。
- DeepSeek 是否推出托管版 Super-agent、原型是否恢复维护。
- 当前主力模型在 OSWorld 2.0 这类长程基准上的成绩；第一份独立的多周可靠性评测；第一个按结果计价的主流产品。

## 关联

- 展开页：[[常驻 Agent 的算力经济学]]、[[Agent 授权三层]]
- 实体：[[Claude Cowork]]、[[Anthropic]]、[[Meta]]、[[Codex]]
- 对照：[[cowork-saas-资本市场冲击]]（价值捕获点迁移）、[[agent-生产级落地的鸿沟]]（落地节奏）、[[Claude Tag 驱动的团队研发流程]]（团队频道里的常驻 agent）、[[harness-vs-model]]、[[控制带]]
