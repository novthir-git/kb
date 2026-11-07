# DeepSeek Super-agent 洞察报告——用户提供稿

> 类型：用户提供的洞察报告（二次综合产物，非一级来源）；署名"@Tom"，标注日期 2026-11-05  
> 原始位置：用户在对话中上传的 Markdown 文件（文件名 `DeepSeek_Super-agent_____.md`）  
> 收录日期：2026-11-06  
> 说明：本文件按用户原始输入存档，未做事实校正；首行标题并入本标题，其余内容逐字保留（含原文第 52 行未展开的嵌入图占位符）。
> 入库时已逐项回查一级来源（原型仓库 commit 8c32a9d 的文件与行号、微信中文原文、X 英文版、DeepSeek 定价与公告、竞品官方文档）。
> 事实层大体成立；需校正的要点：Router 并非"只读文件系统"、合并权限不属于宿主强制层（由团队 prompt 决定且默认关闭）、
> "授权由宿主强制"被 Router 可改写 Policy 与无 token 的本机管理 API 削弱、"开源自托管 / 宿主授权 / 默认安静"并非独有差异点、
> Copilot automations 首发应为 2026-06-02、ChatGPT workspace agents 部署到 Slack 时用共享认证而非请求人身份、
> 缓存命中 1/50 只适用于 deepseek-flash（v4-pro 为 1/30）、11-01 起按次计费只限 Search/Fetch。
> 逐项核验见 [[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]]。正式沉淀前须回查一级来源。

---

Nov 5, 2026 · @Tom

## 核心结论

DeepSeek Super-agent 是一份架构提案，思路是把计算机系统工程的经典做法用到 agent 上，外加一个只实现了约一半设计的研究原型。它不是产品发布。

1. **定位**：发布物是一篇架构文章（2026-10-31 公众号首发，11-01 发 X 英文版）和一个 MIT 协议的研究原型。官方原话是 "not an official DeepSeek product"。
2. **新意在控制面，不在拓扑**：Router＋Worker 的结构已是行业共识。真正值得学的是“代码管规则、模型管判断”：授权、状态、消息上限都由宿主程序强制执行，模型只负责语义判断。
3. **主要收益是稳定，不是速度**：与提示中鼓励委派的单会话方案相比，p50 只快约 10%，p95 快约 46%。单会话方案的长尾来自 5 次运行中有 1 次模型没有委派，自己动手做了。两级架构把“是否委派”从模型的临场判断变成了系统结构上的保证。
4. **原型只落地了一半**：两级架构、两级过滤、订阅直达、上下文组织、全双工已经实现；存算分离、BYOM、Watchdog 没有实现，实验代码也没有发布。
5. **安全上只适合小范围可信环境**：授权层很严，但执行层以 `danger-full-access` 权限、以运维者本人的 OS 用户身份运行。官方也承认，安全和隐私问题不解决，它只能在很小的可信范围内工作。
6. **战略上是 Harness 平台和模型 API 的样板间（推断）**：Router 用轻模型，Worker 用强模型；缓存读 token 比单会话方案多 2–4 倍。DeepSeek 的缓存命中价约为未命中价的 1/50，这部分开销几乎可以忽略。把编排层开源，会挤压靠编排层收费的创业公司。

## 它是什么

Super-agent 分三层：一篇设计文章、一个研究原型，以及它们依附的 DeepSeek Harness 平台。

| 层 | 内容 | 状态 |
| --- | --- | --- |
| 设计文章 | [《Super-agent设计探索》](https://x.com/DeepSeekHarness/status/2116857257245987236)，提出 4 个特征、由 5 个模块支撑。由 Yujia Qiao 实现系统并执笔 | 公众号 10-31 首发；X 英文版 11-01 发布，官方注明是机器翻译 |
| 研究原型 | [dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)：只有 1 个 commit，源码与测试各约 1.5 万行 TS；只服务一个 GitHub 仓库，可选接入飞书 | MIT；11-04 时约 15.9k star |
| 底座平台 | [DeepSeek Harness](https://www.deepseek.com/en/harness/)，口号是 "Everything is a plugin" | developer preview，MIT；据报道约 26.9 万 star |

文章定义的 4 个特征：

- **连续**：从任何入口进来，面对的都是同一个 agent。
- **高产**：多个任务并行，互不阻塞。
- **主动**：监听事件，没事就保持安静。
- **持久**：始终在线，出问题能自动恢复。

文章自称“不提出新理论”，而是把计算机系统里的经典做法搬到 agent 上：Fast/Slow Path、缓存与局部性、推测执行、存算分离、外部控制回路和批处理。

时间线（新到旧）：

| 日期 | 事件 |
| --- | --- |
| 2026-11-01 | X 英文版发布；Bloomberg 以“对标 Anthropic”为题报道；DeepSeek 开始对经 Harness、Claude Code、Codex 发起的服务端工具调用按次计费 |
| 2026-10-31 | 公众号文章与开源原型同日发布 |
| 2026-10-17 | V4.1-Flash-1017 发布，官方写明针对 Harness 做了调优 |
| 2026-10-16 | Harness 与 Web、App、Platform 团队合并为产品部 |
| 2026-09-30 | Harness 桌面版发布 |
| 2026-08-13 | Harness v0.1 developer preview 与 V4-Pro 正式版同日上线 |
| 2026-06-23 | Anthropic 发布 Claude Tag，这是结构上最接近的竞品 |
| 2026-04-24 | V4 Preview 发布 |

## 架构要点

架构的核心是“两级分工＋代码先行”。Router 只负责分派和回复，Worker 各自独立执行；授权、状态和消息上限都由代码强制。

&#91;embedded content: Super-agent 架构 · 按原型代码与官方文章绘制\]

新事件先过代码准入，再交给模型研判；已订阅线程的后续消息直接送到对应的 Worker，不经过 Router。所有状态都由底部的控制面统一写入。

| 文章模块 | 设计要点 | 原型实现 |
| --- | --- | --- |
| 两级架构 | Router 常驻，只分派不拆解任务，可用轻模型；Worker 有独立上下文，用最强模型 | 已实现。Router 保留了限时 5 秒的 bash 和只读文件系统 |
| 事件过滤 | Fast Path 用代码准入，Slow Path 用模型研判 | 已实现（gate＋assessment）。推断出的任务默认只记录 |
| 订阅直达 | 后续消息按 Thread 直达 Worker，Worker 可以把不属于自己的消息退回 | 已实现 |
| 上下文组织 | Inline & Spill：把上下文窗口当缓存用；Chain of Recall：沿 ID 引用逐跳召回 | 已实现。截断处附读取指针，每页 4000 字符，所有 ID 都可读取 |
| 推测执行 | 先在后台复现并修复，确认后才出声 | 可用规则＋auto 模式近似实现，默认关闭 |
| 全双工 | 异步 start/stop，后台结果作为新事件回送 | 已实现。前台命令 5 秒后转入后台 |
| 多渠道 | IM 里保持简短（每条 ≤100 词），GitHub 和邮件里写结构化内容 | 部分实现。支持飞书＋GitHub，没有邮件和日历 |
| 存算分离 / BYOM | 云端无状态 loop＋端侧 daemon，可接入个人机器 | 未实现。目前是单机、tmux、SQLite |
| Watchdog | 独立的 Session 判断 Worker 是否真的在推进 | 未实现。只有外部每小时一次的状态检查 |

## 证据检验

官方实验里，Super-agent 把 p95 从 29.0 分钟压到 15.7 分钟，代价是缓存读 token 多出 2–4 倍。但实验用的是合成负载，每组只跑了 5 次，官方也称结果仅供参考（"indicative only"）。

实验设置如下：

- 每次运行约 300 条消息，其中约 20 条是工作请求。
- 编码工作用“只消耗时间”的工具模拟。
- 消息间隔和工作时长按 1/4 缩放，模型调用时间不缩放。

| 方案 | 完成时间 p50（分钟） | p95（分钟） | 每次运行的缓存读 token |
| --- | --- | --- | --- |
| Super-agent | 12.4 | 15.7 | 23.2M |
| Super-agent，去掉订阅直达 | 12.6 | 15.5 | 31.8M |
| 单 Session＋Subagent，中性提示 | 20.4 | 29.5 | 6.1M |
| 单 Session＋Subagent，委派优先提示 | 13.8 | 29.0 | 10.8M |

怎么读这组数据：

- **长尾来自一次“没委派”**。用中性提示时，5 次运行一次都没委派。用委派优先提示时，5 次里有 4 次委派了，剩下 1 次模型判断“活很小”就自己做了，这一次拉长了尾部。
- **订阅直达省的是 token，不是时间**。去掉它以后，Router 的决定次数多了约 30%，缓存读多了约 37%，完成时间基本不变。
- **Router 靠批处理抗住突发**。压测时 Router 用真实模型、Worker 用 mock。触发从每分钟 1 条升到 40 条时，batch 从 1.0 升到 2.8，单次请求从 2.5 秒升到 3.9 秒，每个决定分摊的推理时间反而从 6.4 秒降到 1.6 秒。
- **成本量级（推断）**。按 deepseek-flash 的缓存命中价（每百万 token 0.003–0.006 美元）算，每次运行的 23.2M 缓存读约 0.07–0.14 美元，对应约 20 个请求。如果按未命中价 0.15 美元算，约为 3.5 美元。实验实际用了哪个模型、什么价位，官方没有披露。
- **缺口**。没有测人的注意力（被打断的次数、需要人决策的次数、review 时长），也没有测代码质量和返工率。p95 实际上由一次运行决定。原型仓库里没有实验代码，无法复现。

## 竞品格局

“IM 或仓库作入口＋常驻协调会话＋每个任务一个 worker”已经是行业共识。DeepSeek 的差异在三点：开源可自托管、授权由宿主强制执行、默认安静。短板在执行隔离和成熟度。

| 产品 | 入口 | 主动性 | 编排方式 | 权限与隔离 | 形态 |
| --- | --- | --- | --- | --- | --- |
| [DeepSeek Super-agent](https://github.com/deepseek-ai/dsh-superagent-prototype) | GitHub＋飞书 | 常驻；推断出的任务默认只记录不执行 | 主 Session＋每个工单一个 Worker | 授权由宿主强制；执行在宿主机上、全权限 | MIT 开源，自托管原型 |
| [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag)（2026-06） | Slack | ambient 模式＋routines，可订阅单个 PR | 频道级 session＋每个线程一个工作 session，结构最接近 | 临时沙箱，凭据不进沙箱 | 托管，按用量计费 |
| [Claude Code](https://code.claude.com/docs/en/agent-teams) | GitHub @claude、CLI、Web | scheduled tasks、PR 自动修复 | coordinator；agent teams（实验性） | 触发者需有仓库写权限 | 占用订阅额度 |
| [Codex / ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) | Slack、Linear、IDE | workspace agents 定时运行 | app 内管理多个 agent | 以请求人身份运行；通过 Allow/Deny 卡片授权 | 托管 |
| [GitHub Copilot](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) | issue、Slack/Teams、IDE | automations（2026-10-28 推出） | 跨仓库并行的托管会话 | rulesets、可要求额外审批；单次会话上限 59 分钟 | 托管，按 AI credits 计费 |
| [Cursor](https://cursor.com/changelog/03-05-26) | Slack、Linear、GitHub、webhook | 常驻的 automations | 每个 subagent 占一台独立 VM | Slack 用户映射到 Cursor 账户 | 托管 |
| [OpenClaw](https://github.com/openclaw/openclaw) | 20 多个聊天 app | 个人助理式常驻 | 2.0 版加入多人共享会话 | 沙箱默认关闭 | MIT 开源，面向个人 |
| [Comma（AFK）](https://github.com/AFK-surf/Comma) | Web、Mac、聊天工具、Linear | Loops 全天候运行 | 可把 Codex 或 Claude Code 注册为 worker | 需先打开 Allow operations | AGPL 开源 |

36 氪称“硅谷团队提前半年做出了同样的架构”，这个说法站不住。AFK 的 Bridge 在 4 月底公开时是个人助理，没有宿主侧授权；Comma 公开仓库的第一个 commit 是 2026-09-30。而“lead＋teammates”模式早在 2026-02 就出现在 Claude Code agent teams 里。

## 七条核心洞察

最有长期价值的是控制面和授权设计。宣传最多的 Router/Worker 拓扑，反而最容易过时。

1. **一套“系统工程词汇表”**。文章把 agent 的问题逐个对应到已有成熟解法的系统问题。这样，设计决策就能借用几十年的系统工程经验来讨论。对应关系是：
   - 过滤对应 Fast/Slow Path。
   - 上下文对应缓存与局部性（Inline & Spill、Chain of Recall）。
   - 主动性对应推测执行。
   - 持久在线对应存算分离＋外部控制回路。
   - 吞吐对应批处理。
2. **确定性外壳，概率性内核**。原型把规则分成五级，从强到弱是：宿主强制的事实、内置 prompt、规则级指令、团队 prompt、外部文本。授权、状态、消息长度和合并权限都在第一级，比如代码里写死了 `IM_WORDS = 100`。模型只判断“这段讨论是否构成明确的改动意图”。
3. **耐久度：拓扑会被抹平，控制面会保值**。有些设计是在补模型的短板：Router 去能力化、“不要改写请求”、命令 5 秒转后台、大量判例。这些会随模型变强而过时。另一些设计解决的是信任与协调问题：宿主强制授权、不可变的 Mandate、单一写入者 Engine、幂等 Outbox、署名与问责。这些会保值。
4. **注意力与认知债之间有张力**。它工作时保持沉默、只报结果，把细节都推到 PR 里。这把瓶颈从“盯会话”移到了“审 PR”，而审 PR 本来就是公认的瓶颈。200 行以内可以自动合并，又会加速团队对代码理解的流失。
5. **注入风险换了形态**。宿主的准入检查挡住了“借一条消息扩大权限”。但订阅线程里的所有内容都会进入一个全权限的 Worker。攻击者不需要扩权，只要在已经授权的工单线程里埋指令就够了。官方已经承认这一限制。
6. **定价与架构互相成全（推断）**。Router 用轻模型、Worker 用最强模型，开放问题里还提到要专门训练做 Router 工作的模型。这是模型厂商才有的杠杆。多消耗的缓存读 token 在 DeepSeek 的定价下几乎不花钱，同时又推高了 API 用量。
7. **这是平台策略，不是单点产品（推断）**。开源编排层是“把互补品商品化”，会压缩 Comma、CellCog、Offloop 这类靠编排收费的公司，同时展示了 Harness 插件体系能做到什么程度。原型本身也是 agent 工程的一个样本：
   - 代码主要由 coding agent 写成。
   - 测试强制要求文档覆盖全部模块。
   - 安装和运维都交给 agent 完成。

## 风险与局限

目前原型只适合在隔离的、单仓库的小团队环境里试用。

- **执行隔离**：两个 preset 都以 `danger-full-access` 权限、以运维者的 OS 用户身份运行。Worker 能读取 home 目录，命令黑名单用绝对路径就能绕过。官方建议用专用 OS 账户。
- **适用范围**：只支持单个 github.com 仓库，不支持 GitHub Enterprise Server。IM 只有飞书，PR 绑定逻辑写死了 GitHub，而且依赖仍在预览期的 Harness。
- **运维**：只有一个 Router，是单点。SQLite 里的记录会无限增长，文档原话是 "Nothing deletes old records yet"。没有 Watchdog，只有外部每小时一次的状态检查。
- **证据**：实验用的是合成负载，每组 5 次，无法复现。内部版本运行至今没有任何量化披露。observe 模式下“本来会接”的判断准确率也不知道，而这正是决定是否切到 auto 模式的依据。
- **合规**：主动监听群聊，群里其他人是否知情、是否同意，官方和各方评论都没有讨论过。
- **官方列出的开放问题**：
  - Router 何时要分片，Worker 之间何时需要直接通信。
  - 运行数月之后的长期记忆。
  - 不以 session 为中心时，交互该长什么样。
  - 组织内哪些上下文共享、哪些隔离，以及 agent 之间（A2A）如何通信。
  - 云端与端侧之间如何互信，如何做到“能用凭据但看不到凭据”。

## 行动建议

先借鉴它的授权和控制面设计；原型只在隔离环境里、用 observe 模式试用。

值得借鉴的设计：

1. 授权由宿主强制执行，外部文本一律只当数据处理。
2. 用不可变的 Mandate 加带版本的策略；策略变更时只通知工单，不取消正在进行的工作。
3. 控制面只有一个写入者，配合“先存后做”的幂等副作用队列。
4. 把注意力预算写进代码：消息长度上限、回复目的校验、一次只问一个问题。
5. 用测试守住文档和模型可见的那部分内容。

试用原型前的准备：

- [ ] 放进专用 VM 或专用 OS 账户里运行
- [ ] 保持 observe 模式，允许名单里只放自己，不打开 receive-all
- [ ] 不配置 merge CLI，所有 PR 都人工合并
- [ ] 先看一两周“本来会接”的记录，再决定是否打开 auto 模式

后续要关注的信号：

- 内部版的 Watchdog、云端 loop 加端侧 daemon 是否开源。
- 是否出现第三方的真实负载报告。
- 是否新增 Slack、GitLab 等来源。
- Harness 是否推出托管版 Super-agent。这将决定它只是“参考架构”，还是正式产品的前奏。

## 来源与可信度

结论主要基于两份一手资料：官方英文版文章全文和原型仓库。仓库里的 README、docs 000–008、全部 prompts 和关键源码都已通读。媒体和评论只用作背景；推断的内容已在正文中标注。

**一手资料**

- [Exploring Super-agent Design（DeepSeek Harness，X 英文版）](https://x.com/DeepSeekHarness/status/2116857257245987236)：官方注明是机器翻译。
- [dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)
- [DeepSeek API 更新日志](https://api-docs.deepseek.com/updates/)
- [DeepSeek 定价](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek Harness](https://www.deepseek.com/en/harness/)
- [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag)
- [GitHub Universe 2026](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/)

**媒体与评论**

- [Help Net Security](https://www.helpnetsecurity.com/2026/11/02/deepseek-dsh-superagent/)
- [TNW](https://thenextweb.com/news/deepseek-super-agent-open-source-coding-agent)
- [第一财经](https://www.yicai.com/news/103419784.html)
- [爱范儿](https://www.ifanr.com/1687026)
- [量子位](https://www.qbitai.com/2026/10/506904.html)
- [IT之家](https://www.ithome.com/1/020/615.htm)
- [36氪](https://www.36kr.com/p/4051770972083075)
- [Offloop](https://offloop.org/learn/deepseek-super-agent-design)
- [CellCog](https://cellcog.ai/blog/deepseek-super-agent/)
- [冯若航](https://vonng.com/ai/ds-super-agent/)
- [Business Standard（转载 Bloomberg）](https://www.business-standard.com/technology/tech-news/deepseek-drops-enhanced-coding-agent-with-aim-to-rival-anthropic-126110100865_1.html)
- [澎湃](https://m.thepaper.cn/newsDetail_forward_34262324)
- [VentureBeat](https://venturebeat.com/technology/deepseek-harness-launches-as-open-source-rival-to-claude-code-alongside-v4-pro-on-api-with-higher-prices)

**未能读取的资料**

- 微信中文原文：受 robots 限制。
- Bloomberg 正文：付费墙。
- Reddit 与 X 上的互动数据：只有二手转述。
