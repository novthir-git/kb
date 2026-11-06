---
tags: [概念, AI, Agent, 安全, 治理]
created: 2026-11-06
updated: 2026-11-06
sources:
  - "raw/sources/articles/2026-10-29-xAI-Grok-Bot-安全与审批文档.md"
  - "raw/sources/articles/2026-09-08-Meta-Muse-安全架构.md"
  - "raw/sources/articles/2026-11-02-Anthropic-Claude-Cowork-架构概览.md"
  - "raw/sources/articles/2026-11-06-OpenAI-dots-安全文档.md"
  - "[[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]]"
  - "https://deploymentsafety.openai.com/gpt-6-astra （检索于 2026-11-06）"
  - "https://arxiv.org/abs/2608.16393 （检索于 2026-11-06）"
  - "https://simonwillison.net/2026/Jan/14/claude-cowork-exfiltrates-files/ （检索于 2026-11-06）"
  - "https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude （检索于 2026-11-06）"
  - "https://www.techrepublic.com/article/news-meta-ai-facebook-marketplace-buyer-seller-address/ （检索于 2026-11-06）"
  - "https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations （检索于 2026-11-06）"
  - "https://claude.com/docs/claude-tag/concepts/security-and-data （检索于 2026-11-06）"
---

# Agent 授权三层

给常驻 agent 授权时，要分开回答三个问题。三层的失效方式不同，补救手段也不同；一层做得好，补不了另一层。

| 层 | 回答的问题 | 典型机制 |
|---|---|---|
| **准入**（admission） | 谁的、什么样的输入能触发 agent 行动？ | 允许名单、写权限门槛（Copilot 只接受有写权限的人触发）、按消息强度分级（DeepSeek 区分"明确要求"与"推断"） |
| **授权语义**（grant semantics） | 一次同意覆盖多大范围、多长时间？ | 动作类别 × 对象 × 有效期；"仅这一次 / 总是允许 / 禁止"；不可变的工单授权、带版本号的策略 |
| **执行隔离**（containment） | agent 被攻破或犯错时，它能碰到什么？ | 每会话或每 agent 一台 VM、出站代理、替身 token（凭据在网络边界才换入）、控制面不可达 |

综合：**身份**是三层共同的前提。准入要按身份判断，授权要绑定在身份上，隔离要按身份限定凭据。所以企业侧正在从"agent 用你的身份登录"转向"agent 有自己的身份"：Claude Tag 的 Agent Identity、Google Gemini Agents 的独立 Workspace 账号、OpenAI specialist dots 的组织身份、Microsoft Entra / Agent 365。

## 五家常驻 agent 的对照（2026-11）

| | 准入 | 授权语义 | 执行隔离 |
|---|---|---|---|
| DeepSeek Super-agent | **最细**：按消息强度分级，工单授权不可变 | 策略带版本号，但 Router 能通过工具改写策略 | **最弱**：以全权限在运维者账户下运行，本机管理 API 没有 token 鉴权 |
| Grok Bot | 由模型做 Auto Review（不审查记忆写入和大多数设置变更） | 有"Always allow"，可以把审批变成永久规则 | 同账户所有 Bot 共用一台电脑和全部登录状态。官方原话："Do not use separate Bots as a security boundary" |
| Muse | 独立的 Sentinel agent 是唯一放行者 | **出过事**："Allow Always" 之后在 Marketplace 泄露住址 | 强：替身 token、出站审查（eBPF 追踪读过用户数据的进程）；但 Mac 端出过一次本地提权漏洞，当天修复 |
| Dots | 由第二个模型预审（Auto-review） | 四档 Custom Rules；用户批准不能凌驾核心安全要求 | 每个 dot 一台 VM；截至 11-06 无产品级公开事故 |
| Claude（Cowork / Tag） | Tag 有频道级身份 | 个人档默认 Auto（不逐步询问，靠自动安全检查放行）；持久化的"always allow"只有企业管理员能禁用；官方承认 computer use 会绕过其他工具的权限检查 | 临时沙箱，凭据不进沙箱；**出过事**：PromptArmor 借已放行的 API 域名外传文件 |

来源：xAI 与 Meta 的安全文档已冻结存档（见 sources）；其余见 [[常驻 AI 同事的竞争格局]] 与 [[2026-11-05-DeepSeek-Super-agent-洞察报告-源摘要]]。架构部分多为厂商自述，未经独立审计。

## 共同缺陷：授权的单位是"通道"，不是"动作"

已知的注入和越权案例，多半借道已经授权的通道：
- **Claude**：PromptArmor 借已放行的 Anthropic API 域名把文件外传到攻击者账户；
- **Muse**：在 Marketplace 上选一次"Allow Always"，覆盖了此后所有回复，包括发住址；
- **DeepSeek**：已结束的工单，只要线程里有人留言就会按原授权恢复，"regardless of who sent it"（理论路径）；
- **Grok Bot**：一台共享电脑让每个 Bot 都继承了所有登录状态。

推断（置信度：中）：一次同意、一个已订阅的线程、一台共享电脑，都会让之后进入这条通道的所有内容被当作已获授权。这可能是行业共同的缺陷。但公开样本只有个位数，而且已公开的事故分布在不同的层，Dots 至今没有产品级事故。

注意，**有作用域还不够**。Muse 的授权本来就是严格的 capability，有一次性、会话、任务、限时、永久五种范围（存档的 Meta 安全文档）。Marketplace 事件出在用户选了永久档，并以为之后仍会先确认。Grok Bot 的做法是另一种：群聊里的审批卡不提供 "Always allow"，后台工作触发的审批卡 30 分钟过期（存档的 xAI 文档）。综合：授权语义要成立，除了**有作用域**，还要**默认值保守**、**用户能看懂"总是"意味着什么**。

## 推论：确定性外壳必须对 agent 自身也不可写

"代码管规则、模型管判断"是这一代常驻 agent 最好的设计思想（与 [[控制带]] 的"检测端完全确定性"同构）。但 DeepSeek 原型说明，**只要 agent 能写到、或者能绕过存放规则的地方，宿主强制就退化成了建议**。外壳要成立，必须同时满足三点：

1. 规则存在 agent 写不到的地方：策略、允许名单、路由清单对 agent 只读；
2. 修改规则必须走 agent 碰不到的通道：人工面板、PR 审查、带鉴权的管理 API；
3. 执行层被攻破后也够不到控制面：这一点靠执行隔离保证，而不是靠 prompt。

## 模型预审的位置

模型预审（Dots 的 Auto-review、Grok Bot 的 Auto Review、Claude 个人档 Auto 模式的自动安全检查）只是准入和授权语义层的**软补充**，不能替代最小权限与执行隔离。
- **数据**：GPT-6 Astra 系统卡中，Gray Swan IPI Arena 的 1,810 次攻击、每个场景 15 次尝试内至少成功一次，估计攻击成功率为 8.5%，前代 GPT-5.6 Sol 是 27.0%。腾讯 A.I.G 对 DeepSeek Harness 的评测，最高攻击成功率为 17.0%（fake-completion，LLM 判官）和 25.5%（hidden Unicode，规则判官）。
- **厂商自己的口径**：xAI 文档说 Auto Review 只是补充、不能替代最小权限；OpenAI 说 Auto-review 不能当安全保证，红队发现过它被误导放行；Anthropic 说浏览器场景的提示注入风险"可降低但无法消除"。
- 推断：如果预审由与执行者同类的模型担任，会有同量级的漏检。它适合用来降低噪声，不适合当作边界。

## 设计清单

1. 准入按身份和输入强度分级；外部文本，包括仓库里的 AGENTS.md 和第三方评论，一律只当数据。
2. 授权必须有作用域和有效期。"总是允许"应拆成"这一类动作 × 这些对象 × 这段时间"，并且可以撤销、留有审计。
3. 恢复或复用一个旧授权（重开工单、复用会话），必须重新过准入。
4. 控制面对 agent 只读；管理接口要有真正的鉴权，而不只是同源检查。
5. 执行隔离按"已被攻破"来设计：不在同一台机器上叠多个 agent 当隔离；凭据在边界注入，agent 只拿替身。
6. 用 agent 自己的身份，而不是员工的身份，离职交接和审计才可行。

## 证据状态与边界

- 对照表的架构部分大多是厂商自述，未经独立安全审计；事故样本只有个位数，多数以媒体报道为一级证据。
- 本框架是归纳出的分析工具，不是任何厂商或标准组织的官方分类。
- 三层与 [[控制带]] 的"信号强度 × 产物风险"授权矩阵是正交的：控制带回答"此刻授予多大行动权"，本页回答"这份授权的边界在哪、靠什么兜底"。

## 关联

- [[常驻 AI 同事的竞争格局]]：五家产品全貌，本页是其中授权一条的展开。
- [[控制带]]：确定性检测加穷举路由，以及 DeepSeek 的反例。
- [[Anthropic-AI原生SDLC治理循环]]：控制单元上移到身份、委托与风险门禁，本页是同一判断在常驻 agent 上的具体化。
- [[Claude Tag 驱动的团队研发流程]]：频道级身份与分层放权。
- [[MCP]]：连接器是准入与授权语义的主要作用面。
