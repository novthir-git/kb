---
tags: [主题, AI, Agent, 投资, 定价]
created: 2026-11-06
updated: 2026-11-06
sources:
  - "https://x.com/elonmusk/status/2116992258520064397 （检索于 2026-11-06）"
  - "https://docs.x.ai/x-subscription/pricing （检索于 2026-11-06）"
  - "https://www.fool.com/earnings/call-transcripts/2026/10/20/spacex-spcx-q3-2026-earnings-call-transcript/ （检索于 2026-11-06）"
  - "https://www.fool.com/earnings/call-transcripts/2026/10/21/meta-meta-q3-2026-earnings-call-transcript/ （检索于 2026-11-06）"
  - "https://www.meta.com/help/subscriptions/1021145227643680/ （检索于 2026-11-06）"
  - "https://www.nbcnews.com/tech/tech-news/openai-launches-dots-ai-agents-safety-questions-rcna600338 （检索于 2026-11-06）"
  - "https://learn.chatgpt.com/docs/dots.md （检索于 2026-11-06）"
  - "https://fortune.com/2026/11/05/openais-dots-are-coming-up-against-the-price-of-privacy-and-the-price-of-compute/ （付费墙，经转述核验；检索于 2026-11-06）"
  - "https://publish.twitter.com/oembed?url=https://x.com/thsottiaux/status/2115850175868727621 （检索于 2026-11-06）"
  - "https://claude.com/resources/articles/claude-duet （检索于 2026-11-06）"
  - "https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork （检索于 2026-11-06）"
  - "https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new （检索于 2026-11-06）"
  - "https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/ （检索于 2026-11-06）"
  - "https://api-docs.deepseek.com/quick_start/pricing/ （检索于 2026-11-06）"
  - "[[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]]"
---

# 常驻 Agent 的算力经济学

**核心论点**：常驻（always-on）agent 号称 7×24 在线，但工程上它的"在线程度"其实是一个预算参数：
- 多久醒来一次；
- 用哪一档模型；
- 能同时开几块屏幕。

这三样都由**谁承担算力成本**决定。厂商自付算力时，它就有动力压低唤醒频率和模型档位，并把计价改成"订阅或席位 + 用量池"。近期收敛的是计价结构，不是某个价位；按结果计价在主流产品里还没有出现。

> 证据边界：
> - 各家都没有披露单用户的服务成本或毛利，下面的证据都是行为信号：额度调整、开放范围、唤醒设计、定价结构。
> - 唯一的成本自述来自 Musk 的一句回复。

## 三种成本结构

| 谁付算力 | 代表 | 架构上的倾向 |
|---|---|---|
| **厂商**（固定订阅内含） | Grok Bot、Muse、Dots、Claude Duet | 压低唤醒频率（Duet 每隔几小时才检查一次账户）；按任务换用更小的模型（Dots 加入 GPT-6.1 Terra）；把用量并进共享额度池（Grok Bot）；收窄开放范围（Muse 不全球上线，Dots 只给 $100 起的档） |
| **企业**（席位 + 用量计量） | Copilot Cowork（M365 许可 + Copilot Credits）、Claude Enterprise（$20/席 + API 用量） | 成本直接转嫁给用户，厂商侧没有压缩唤醒频率的压力；事件触发也最早落地（Copilot Cowork 2026-08） |
| **API 用户**（按 token 付费） | DeepSeek Super-agent（自托管，跑在 DeepSeek API 上） | 架构可以放心多耗 token：Router 常驻、批处理、大量缓存读。前提是缓存命中价足够低：flash 是未命中价的 1/50，v4-pro 是 1/30，高峰时段价格翻倍。综合：对模型厂商来说，编排的开销本身就是 API 收入 |

## "常驻"在工程上是什么

- **事件触发**：只覆盖已接入、能推送的信号。已落地的有：
  - Copilot Cowork：08 月上线邮件和 Teams 消息触发，10 月扩展到非 Microsoft 的 connector；
  - Grok Bot：routine 可由 webhook、Slack、git、邮件、Linear 触发；
  - Dots：DevDay 推出了事件触发自动化；
  - DeepSeek：接入飞书实时事件。
- **定时检查与轮询**：覆盖其余数据源。Claude 帮助文档里只有定时任务，没有事件触发器；Duet 每隔几小时检查一次；DeepSeek 每 60 秒轮询一次 GitHub 通知。
- 综合：**"7×24"指的是可以被唤醒，不是一直在看。** 对"没有推送能力的数据源"，常驻程度 = 轮询频率 × 单次检查成本，这正是厂商最先裁剪的地方。

## 证据点（持续追加）

| 日期 | 来源 | 信号 | 备注 |
|---|---|---|---|
| 2026-11-05 | Fortune（转述）、ChatGPT 文档 | 驱动 Dots 的模型家族加入了 GPT-6.1 Terra（官方周报列在 11-04），一个 dot 可以按环节调用不同模型；Fortune 称部分任务已因算力成本转给 Terra | 官方口径是"扩充模型家族"，降本动机是媒体解读 |
| 2026-11-01 | Musk（X 回复用户的额度重置请求） | "The cost of serving Grok Bot was unsustainably high relative to revenue"；大量付费用户的周额度提前数天耗尽 | 唯一的厂商成本自述。额度是否被下调官方未说明；论坛转述的客服邮件称额度"不固定，只保证不低于套餐价格"（单一来源） |
| 2026-10-31 | DeepSeek Super-agent 设计文章与实验 | 两级架构的缓存读是单会话方案的 2.1–3.8 倍，换来 p95 更稳 | 第三种成本结构：由 API 用户承担；见 [[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]] |
| 2026-10-29 | OpenAI Codex 负责人 Tibo（X） | Pro 100/200/500 与 Business Premium 的额度全部翻倍，并撤回原定的 Pro 200 下调；dots 的扩展额度"for now"继续与默认用量分开 | **反向证据**：OpenAI 选择补贴，而不是收紧 |
| 2026-10-21 | Meta Q3 电话会 | Zuckerberg 称 Muse "very compute-intensive"，暂不全球上线，部分因为算力、部分为了逐地优化；押注一年内成本效率提升 10 倍以上 | 付费档按每周 Muse token 计（Power $20 每周 5 亿，Maximum $100 每周 30 亿） |
| 2026-10-21 | Anthropic Claude Duet 发布文 | Duet 每隔几小时检查一次已连接账户，理由是持续检查会更快耗尽套餐额度；官方承认它可能漏掉检查间隙到来的事项 | 常驻程度被明确写成预算决策 |
| 2026-10-20 | SpaceX Q3 电话会 | Musk 称 Grok Bot 可能成为 SI 算力的最大消耗方；10 月初付费周用户 80 万 | 算力消化叙事与 11-01 的成本表态是同一枚硬币的两面 |
| 2026-10-12 | xAI X Subscription 定价页 | Grok Bot 只在 $30/$100/$200 档提供，改为与 Grok、Cursor 共用每周额度池（此前是独立额度）；第三方模型从第一次使用起按 API 牌价扣费 | 共享池 + 用量差价，把用户推向自研模型 |
| 2026-09-29 | OpenAI DevDay（NBC 报道） | Dots 只向 Pro 和 Business Premium 开放；Altman 以计算强度为由分阶段推出；同日推出 $500 的 Pro 档 | 用开放范围控制成本 |
| 2026-06-16 | Microsoft Copilot Cowork GA | 需要 M365 Copilot 席位许可，另按 Copilot Credits 计量（$0.01/credit） | "席位 + 用量"结构的企业样本 |

## 推论

1. **定价收敛的是结构，不是价位。** 入门门槛差别很大：Muse 免费，Duet 含在 $20 的 Pro 里，Grok Bot 从 $30 起，Dots 从 $100 起。但高阶"agent 档"多落在 $100–200/月，而且都叠加了每周额度、token 或 credits。
2. **按结果计价缺席。** 推断（置信度：中）：原因有二。一是结果难以归因和验收，长程任务的公开完成率只有 20% 量级（见 [[agent-生产级落地的鸿沟]]）；二是厂商最大的不确定性在自己的算力成本，按用量计价才能把这部分风险转给用户。这与 [[cowork-saas-资本市场冲击]] 的"seat → outcome"叙事有张力，已在该页标注。
3. **固定月费与 7×24 agent 的张力不是单向的。** SpaceX 在收紧，OpenAI 在补贴。各家的成本承受力与补贴意愿不同，所以额度可能朝两个方向变；企业做预算时要按"唤醒频率 × 模型档位"建模，并为额度调整留余量。
4. **成本纪律从企业内部外溢到了消费产品。** [[Uber-软件工厂的成本工程]] 把"agent 替自己多干的活"定义为浪费，那是企业内部的工程问题。常驻 agent 把同一笔账变成了消费产品的定价与额度问题。

## 待追踪

- 第一次披露单用户服务成本或毛利的常驻 agent 产品。
- Grok Bot 额度池的绝对大小，以及 11 月前后是否下调。
- Meta"一年内成本效率提升 10 倍"能否兑现，以及 Muse 何时全球上线。
- 第一个按结果计价的主流 agent 产品。
- OpenAI 的 dots 扩展额度何时结束，以及之后的条款。

## 关联

- [[常驻 AI 同事的竞争格局]]：五家产品的全貌，本页是其中"单位经济学"一条的证据库。
- [[Uber-软件工厂的成本工程]]：企业内部的 agent 成本方程。
- [[cowork-saas-资本市场冲击]]：席位模型受挑战的资本市场叙事。
- [[Agent 工具上下文膨胀]]：每轮重发的固定上下文，是常驻成本的另一个来源。
