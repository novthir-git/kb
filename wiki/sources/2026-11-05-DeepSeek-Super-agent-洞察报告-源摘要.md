---
tags: [素材, AI, Agent, 架构, 安全]
created: 2026-11-06
updated: 2026-11-06
sources:
  - "raw/sources/notes/2026-11-05-DeepSeek-Super-agent-洞察报告.md"
  - "https://github.com/deepseek-ai/dsh-superagent-prototype （commit 8c32a9d；检索于 2026-11-06）"
  - "https://mp.weixin.qq.com/s/zoS7GlReWPhfCjENGxXCdg （检索于 2026-11-06）"
  - "https://x.com/DeepSeekHarness/status/2116857257245987236 （经 api.fxtwitter.com 读取；检索于 2026-11-06）"
  - "https://api-docs.deepseek.com/quick_start/pricing/ （检索于 2026-11-06）"
  - "https://api-docs.deepseek.com/news/news261017 （检索于 2026-11-06）"
  - "https://www.deepseek.com/en/harness/ （检索于 2026-11-06）"
  - "https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/session/session-log-deepseek/README.md （检索于 2026-11-06）"
  - "https://m.thepaper.cn/newsDetail_forward_34262324 （检索于 2026-11-06）"
  - "https://www.business-standard.com/technology/tech-news/deepseek-drops-enhanced-coding-agent-with-aim-to-rival-anthropic-126110100865_1.html （Bloomberg 转载；检索于 2026-11-06）"
  - "https://github.blog/changelog/2026-06-02-schedule-and-automate-tasks-with-copilot-cloud-agent （检索于 2026-11-06）"
  - "https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations （检索于 2026-11-06）"
  - "https://code.claude.com/docs/en/github-actions （检索于 2026-11-06）"
  - "https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business （经快照读取；检索于 2026-11-06）"
  - "https://cursor.com/docs/subagents （检索于 2026-11-06）"
  - "https://github.com/AFK-surf/Comma/blob/main/docs/bridge-for-teams/design.md （检索于 2026-11-06）"
  - "https://comma.surf/blog/a-brief-history-of-single-session-agents （检索于 2026-11-06）"
  - "https://www.36kr.com/p/4051770972083075 （检索于 2026-11-06）"
  - "https://vonng.com/ai/ds-super-agent/ （检索于 2026-11-06）"
  - "https://arxiv.org/abs/2608.16393 （检索于 2026-11-06）"
  - "https://github.com/deepseek-ai/deepseek-harness/discussions/11793 （检索于 2026-11-06）"
  - "https://github.com/SilasSolivagus/dsh-superagent （检索于 2026-11-06）"
  - "https://dev.to/dishant0406/deepseeks-super-agent-got-14k-stars-the-code-didnt-change-4n7f （检索于 2026-11-06）"
---

# DeepSeek Super-agent 洞察报告——用户提供稿源摘要

## 来源定位

这份报告由用户提供（署名"@Tom"，2026-11-05），研究对象是 DeepSeek 于 2026-10-31 发布的 Super-agent 设计文章，加上 MIT 协议的开源研究原型 `dsh-superagent-prototype`。报告是**二次综合产物，不是一级来源**：它通读了原型仓库和英文版文章，媒体只作背景。

本页记录 2026-11-06 的逐项回查结果，分五组：原型仓库、官方文章与实验、平台与定价、竞品表、第三方反响。回查直接对照仓库文件和行号、微信中文原文、DeepSeek 官方定价与公告，以及各竞品的官方文档。

判断与跨源综合不在本页：常驻 agent 版图见 [[常驻 AI 同事的竞争格局]]，"外壳对 agent 不可写"的推论见 [[Agent 授权三层]]，成本结构见 [[常驻 Agent 的算力经济学]]。本页只记核验。

总评：**事实层大体可靠，核心判断需要降级。** 实验表的全部数字、实验设置、日期、"not an official DeepSeek product"的出处，都能在一手材料里逐字找到。"主要收益是稳定，不是速度"这个读法也有第三方佐证（Offloop、dev.to）。

## 结构性校正（影响报告主线）

1. **"授权由宿主强制执行"的边界比报告写的窄得多。** 准入检查确实挡住了外部文本直接改策略，但还有下面这些缺口。
   - Router 可以通过 `orchestrator_settings_save` 改写 Policy（允许名单、规则、accept mode），也可以通过 `orchestrator_prompts_save` 改写团队 prompt。"须有人类明确请求"这一条只写在工具描述里（`src/app/tools/main.ts:249-296`）。
   - 本机管理 HTTP API 只检查三样东西：Host 为 localhost、固定请求头 `x-orchestrator-request: 1`、Origin。它没有 token 鉴权，保存时拥有面板权限，文档明说"agents can also call"（`src/app/http.ts:75-78`；`docs/006-deployment.md`）。Worker 和 Router 都以 danger-full-access 运行 bash，所以被注入后理论上可以绕过授权改写配置。这是推断，没有公开 PoC；有一篇第三方审计定为高危，但 PoC 仓库是私有的。
   - 已结束的工单，只要线程里有人留言就会按原授权恢复，原文是 "regardless of who sent it"（`docs/002-authorization.md:239`）。PR 里的 AGENTS.md 会进入 Worker 的系统 prompt（`docs/004-prompts.md:61`，攻击路径属推断）。
   - subagent 嵌套超过 8 层后 fail-open，工具限制和工单结束后的 guard 都会失效。这是社区报告（Discussions #11793），代码已核（`src/app/sessions.ts:306-310`）。
2. **合并权限不在宿主强制层。** auto-merge 完全由团队 prompt「Delivery requirements」决定，宿主没有任何合并逻辑，原文是 "The host has no merge-specific decision logic."（`docs/003-execution.md:84`）。这个功能默认关闭，开启需要几个前提：approval 覆盖 head commit、配好另一个账号的 merge CLI。报告把它归入"宿主强制的第一级"，"认知债"那段论证也因此说重了。
3. **"开源自托管、宿主授权、默认安静"都不是 DeepSeek 独有的。**
   - Copilot cloud agent 只接受有写权限的用户触发，无写权限用户的评论永远不交给 agent。
   - Claude Code GitHub Action 在启动前检查触发者的写权限，并确认不是 bot。
   - Claude Tag 用 Agent Proxy 在边界注入凭据。
   - Comma（AGPL 开源）已有结构高度相似的 Router/Worker、宿主检查的准入和默认沉默。

   DeepSeek 真正不同的是**粒度**：按消息是"明确要求"还是"推断"分级准入、工单授权一经下达不可变、策略带版本号。另外，它把这套设计讲得最系统。
4. **成本推算只取了最便宜的口径。** 缓存命中价是未命中价的 1/50，这只对 deepseek-flash 在同一时段成立。v4-pro 是 1/30（$0.022 对 $0.66），高峰时段价格翻倍。如果 Worker 用"最强模型" v4-pro，缓存读成本约高 7 倍。

## 逐项核验

### 定位、时间线与平台

| 报告论断 | 核验 | 校正后的口径 |
|---|---|---|
| 不是产品发布，官方原话 "not an official DeepSeek product" | **成立** | 出自原型 README。文章开篇另有一句更直接的定位："并非对 DeepSeek Harness 现有产品功能的介绍"，报告没有引用 |
| 公众号 10-31 首发，X 英文版 11-01（机器翻译） | **成立** | 微信原文标题《Super-agent 设计探索：迈向更自主的 Agent 系统》，作者字段为"DeepSeek 产品部"，发布时间 10-31 20:29 |
| 微信中文原文受 robots 限制，无法读取 | **不成立** | 可以直接读取。报告因此只依赖英文机翻版，产生了术语回译偏差（见下一行） |
| 四个特征"连续、高产、主动、持久" | **校正** | 中文原文是"高效"，"高产"是从英文回译出来的。"持久"在原文里还包括"直接接入用户真实的工作环境"。五个模块是：双层架构、事件驱动、面向人的交互、计算/状态/环境分离、Watchdog |
| 原型 MIT、1 个 commit、源码与测试各约 1.5 万行 | **成立** | src 约 15,205 行，tests 约 14,960 行。补充：这一个 commit 是压平后的内部历史；11-02 到 11-03 之间被 force-push 替换过一次（tree 相同）；仓库关闭了 Issues，发布后没有修过任何 bug |
| 11-04 约 15.9k star | **无法回溯** | 11-06 约 19.8k star、2.3k fork |
| Harness 约 26.9 万 star | **数量级成立** | 11-06 约 27.4 万 |
| Harness v0.1 与 V4-Pro 正式版同日（08-13） | **成立** | — |
| Harness 桌面版 09-30 | **差一天** | 官方中文渠道和发版记录是 09-29（v0.2 预览版） |
| 10-16 Harness 与 Web/App/Platform 合并为产品部 | **校正** | 10-16 是澎湃的报道日，信源是知情人士，并经崔添翼证实。合并发生在"最近"，具体日期未披露，也没有官方公告 |
| V4.1-Flash-1017 官方写明针对 Harness 调优 | **成立** | 调优对象还包括腾讯 CodeBuddy、WorkBuddy；权重已开源 |
| 11-01 起对经 Harness、Claude Code、Codex 发起的服务端工具调用按次计费 | **范围说宽了** | 只限 Search/Fetch，每千次成功请求 $0.75，北京时间 11-01 00:00 起，10-17 已预告。失败、空结果、超时不计费 |
| Bloomberg 以"对标 Anthropic"为题报道 | **成立** | 具体对象是 Claude Code。同文提到 DeepSeek 最新一轮融资约 1,000 亿元，属于 IPO 前的融资 |

### 架构与原型

| 报告论断 | 核验 | 校正后的口径 |
|---|---|---|
| Router 保留了限时 5 秒的 bash | **不准确** | 前台命令最多等 5 秒，之后转为后台 job 继续运行，不会被杀掉。Worker 也是 5 秒；Worker 派生的 subagent 是 60 秒 |
| Router 是只读文件系统 | **不成立** | 只是 fs 工具关掉了写入。Router 仍有全权限的 bash，"不读代码"也只是 prompt 里的规则 |
| 两级过滤（代码 gate + 模型 assessment），推断出的任务默认只记录 | **成立** | accept mode 有三档：off / observe（默认）/ auto；非 auto 模式下记录 `would_accept` |
| 订阅直达：后续消息直接送到 Worker，绕过 Router | **部分成立** | 绕过的是 Router 的分派决定，Router 仍会收到 follow_up relay、消耗 token。订阅扇出不检查发送者，bot 和 CI 的消息同样会进入 Worker |
| 每页 4000 字符 | **补充** | 4000 是默认值，最大 8000，单位是 UTF-16 code unit |
| 五级规则层级；代码里有 `IM_WORDS = 100` | **成立** | 第二级还包括团队对内置 section 的 override |
| 授权、状态、消息长度和**合并权限**都在第一级 | **不成立** | 合并权限属于团队 prompt（第四级），见结构性校正 2 |
| 200 行以内可以自动合并 | **漏了前提** | 还要求 approval 覆盖 head commit、涉及 UI 时有指定人批准、配好另一个账号的 merge CLI；默认不开，全部是 prompt 规则 |
| 以 danger-full-access、运维者 OS 用户身份运行；能读 home；黑名单可用绝对路径绕过；建议专用账户 | **成立** | 补充默认路径上的凭据护栏：worker-bin shim、替换 gitconfig、剥离名字形似凭据的环境变量。这些是护栏，不是隔离 |
| 单 Router；SQLite "Nothing deletes old records yet"；没有 Watchdog，只有外部每小时状态检查 | **大体成立** | 每小时那个任务不只是检查：它是由 agent 按 prompt 执行"检查加修复"，会重启并读日志自行修复。另有每轮后台工作 30 分钟上限、瞬时故障重试三次等机制 |
| Router 用轻模型、Worker 用强模型 | **校正** | 原型里两者默认是同一个模型（null，即 profile 默认），分开只是可选配置；maxWorkers 默认 3 |
| 代码主要由 coding agent 写成；安装运维交给 agent | **说重了** | README 原话是 "much of the engineering done by coding agents"。交给 agent 安装是推荐路径，文档同样完整写了手动流程 |
| （报告未提）事件接入方式 | **补充** | GitHub 侧每 60 秒轮询 agent 账号的 notifications，不用 webhook；agent 必须是 GitHub 用户账号，不能是 GitHub App |

### 证据检验

| 报告论断 | 核验 | 校正后的口径 |
|---|---|---|
| 实验表数值（12.4/15.7/23.2M 等四组）、合成负载、每组 5 次、"indicative only" | **成立** | 中英文原文逐字吻合 |
| 中性提示 0/5 委派，委派优先 4/5 | **成立** | — |
| 去掉订阅直达后 Router 决定 +30%、缓存读 +37% | **成立** | — |
| Router 压测：batch 1.0→2.8，单次 2.5s→3.9s，每个决定分摊 6.4s→1.6s | **成立** | — |
| 缓存读 token 多 2–4 倍 | **措辞高估** | 应为"是单会话方案的 2.1–3.8 倍" |
| p95 实际上由一次运行决定 | **推断** | 原文只说那次运行形成了长尾。推断合理，但应标注 |
| 命中价约为未命中价的 1/50；23.2M 缓存读约 $0.07–0.14 | **只对最便宜口径成立** | 见结构性校正 4 |
| 尚无第三方真实负载报告 | **过时** | 已有小规模 issue→PR 实测，例如 Discussions #11706、#11769；一个 fork 一天开了 42 个 PR、合并 38 个，都是文档和小修复。但没有质量、返工或成本的量化数据 |

### 竞品格局

| 报告论断 | 核验 | 校正后的口径 |
|---|---|---|
| Claude Tag 结构最接近；"常驻协调会话 + 每任务一个 worker"已是共识 | **成立** | 差别：Claude Tag 默认就主动回复（Respond automatically），与 Super-agent 的默认安静相反；会话也可以跑在客户自己的 runner 上 |
| GitHub Copilot automations 于 2026-10-28 推出 | **不成立** | 06-02 就已上线，比 Claude Tag 还早。10-28 Universe 发布的是共享 automations、API 触发、MCP 工具和 credits 上限。跨仓库并行属于 Copilot projects，不属于 automations |
| ChatGPT workspace agents 以请求人身份运行，入口为 Slack、Linear、IDE | **不成立** | 部署到 Slack 时，所有连接必须用共享认证。Linear 和 IDE 是 Codex 的入口，不是 workspace agents 的 |
| Cursor 每个 subagent 占一台独立 VM | **夸大** | 每个 Cloud Agent 一台 VM；subagent 默认共用父 agent 的 checkout |
| DeepSeek 的差异在于开源自托管、授权由宿主强制、默认安静 | **不成立** | 见结构性校正 3 |
| 36氪"硅谷团队提前半年做出了同样的架构"站不住 | **结论成立，论据偏弱** | 原文出自新智元，36氪是转载。AFK 自己的博客比较克制：只说 4/28 发过 Bridge 文章、Comma 于 10-01 上线，并承认 Super-agent "follows its own design"。拿 Claude Code agent teams 当反例不贴切，它是本地交互式 CLI；更有力的先例是 Claude Tag（06-23）、Copilot automations（06-02）、Cursor automations（03-05）。另外，10 月版 Comma 已经高度同构 |

### 洞察与推断

| 报告论断 | 核验 | 校正后的口径 |
|---|---|---|
| 注入风险换了形态，"官方已经承认这一限制" | **只承认了前提** | 官方承认的是全权限、不隔离进程（`docs/006:19`），以及文章 8.4 节承认不可信输入可能攻破 Agent Loop；"在已授权线程里埋指令"是报告的推演。实际注入面比报告写的更宽，见结构性校正 1 |
| 开放问题里提到要专门训练做 Router 工作的模型 | **说重了** | 原文 8.1 节只说"值得探索的方向""有可能进一步提升"。洞察 6 的"模型厂商杠杆"应弱化为推断 |
| 开源编排层会挤压 Comma、CellCog、Offloop 这类靠编排收费的公司 | **前提不成立** | Comma 本身是 AGPL 开源，另有托管和 credits；Offloop 自称仍在内部测试；CellCog 和 Offloop 关于本项目的文章本身就是带 CTA 的竞品营销稿 |
| 官方开放问题共 5 条 | **结构不对** | 官方是 4 个方向（8.1–8.4），报告漏了 8.2 中"用户在执行中途介入、接管、实时协同"这一产品问题 |
| 群聊监听的知情同意，各方都没有讨论 | **成立（限 DeepSeek 相关报道）** | 这是"没找到"式的确认，不能外推到整个品类 |

## 报告漏掉的（均已核）

- **冯若航的反论点**：Session 藏进底层"天经地义"，但 Context"是工作现场和权限边界……绝不能对用户隐藏"；单一入口让 Router 去猜路由，"迟早要出事故"。他主张以显式的群作为上下文容器，同时肯定原型"工程设计相当扎实"。
- **腾讯 A.I.G 对 Harness 底座的间接提示注入评测**（arXiv 2608.16393）：14,560 次执行、16 个渠道，最高攻击成功率为 17.0%（fake-completion，LLM 判官）和 25.5%（hidden Unicode 的 file 模式，规则判官）。
- **商业模式信号**：
  - Harness 内置 DeepSeek 账号登录，客户端读取余额和赠金通知，是通往按量付费 API 的入口。
  - 插件 `session-log-deepseek` 默认开启，使用官方 API 时把会话日志增量上传给 DeepSeek，单次最多 8 MiB，可在设置里关闭。
  - 截至 11-06，没有任何托管版或企业版的公告。
- **文章里的实现声明与外部对标**：4.1 节写明，异步 start()/stop() 机制"已经在 DeepSeek Harness 中实现，但尚未默认开启"。5.2 节明确引用了 Anthropic 的 managed agents（"Decoupling the brain from the hands"），称思路一致。
- **反响与维护**：X 帖截至 11-06 约 320 万浏览；Hacker News 反响冷淡，最高 11 分、0 评论。社区在 Harness Discussions 里提了大量 bug 和补丁，抽查 7 帖都没有官方回复。dev.to 的评论是："Ten percent faster than a decent prompt is not a new architecture."
- **漏列的直接开源竞品**：AFK-surf 的 still.fail（MIT）把团队对话里的 coding agent 跑在用户自己的机器上，支持 Slack 和飞书，可以把 DeepSeek Harness 当作运行时之一。
