---
tags: [实体, 产品, AI, Agent]
created: 2026-07-03
updated: 2026-11-07
sources:
  - "https://www.anthropic.com/product/claude-cowork （检索于 2026-07-03）"
  - "https://support.claude.com/en/articles/13837440-use-plugins-in-claude （检索于 2026-07-16）"
  - "https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp （检索于 2026-07-16）"
  - "[[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要]]"
  - "https://claude.com/resources/articles/cowork-is-now-claude （检索于 2026-11-06）"
  - "https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude （检索于 2026-11-06）"
  - "https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile （检索于 2026-11-06；2026-11-07 复核）"
  - "https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview （检索于 2026-11-06）"
  - "https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork （检索于 2026-11-06）"
  - "https://support.claude.com/en/articles/12138966-release-notes （检索于 2026-11-06；2026-11-07 复核 07-07 条目）"
  - "https://claude.com/resources/articles/claude-enterprise-security-updates （检索于 2026-11-06）"
  - "https://claude.com/resources/articles/claude-duet （检索于 2026-11-06）"
  - "https://www.anthropic.com/news/introducing-claude-tag （检索于 2026-11-06）"
  - "https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm （检索于 2026-11-06）"
  - "https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/ （检索于 2026-11-06）"
  - "https://simonwillison.net/2026/Jan/14/claude-cowork-exfiltrates-files/ （检索于 2026-11-06）"
  - "https://airisk.mit.edu/ai-incidents/1441-claude-cowork-allegedly-deleted-folder-containing-15 （检索于 2026-11-06）"
  - "https://github.com/anthropics/claude-code/issues/67188 （检索于 2026-11-06）"
---

# Claude Cowork

[[Anthropic]] 的 agentic AI 能力。它围绕"**结果（outcome）**"而不是单条 prompt 设计：用户下达目标，收到成品交付，不必逐步指挥。

**现状（2026-11）**：Cowork 已不再是独立产品，而是 Claude 应用的**默认执行层**。2026-09-16 起与 chat 合并为"一个 Claude"；2026-10-06 起，Pro/Max/Ultra 的新任务一律在云端运行，且不能切回本地。更主动的常驻形态拆给了两条线：Slack 里的 Claude Tag，以及独立 App Claude Duet。

## 核心能力（四大工作流，未变）
1. 整理/管理文件（重命名、排序、去重）。
2. 从素材综合、装配、准备文档。
3. 跨多源综合复杂研究。
4. 从合同/报告等非结构化文件抽取结构化数据。

## 运行架构（2026-11）
- **云端为默认**：agent loop 和代码执行跑在 Anthropic 托管的临时隔离沙箱里，每个会话一个，会话结束即销毁。
  - 所有出站流量强制经过沙箱无法改配的代理，只放行白名单地址；
  - 连接器的授权 token 从不进入沙箱；
  - Enterprise 默认关闭网络访问。
- **本地能力**：本地文件、本地 MCP、浏览器、computer use 经 Anthropic 中转，交给用户设备上的 Claude Desktop 执行，要求 Desktop 在线。想纯本地运行的用户，官方建议改用 [[Claude Code]] desktop。
- **插件体系**：Plugin 是 **[[Agent Skills|skills]] + connectors + sub-agents** 的可安装能力包，不等于 MCP Server，详见 [[cowork-plugins-架构]]。

## 常驻形态
- **定时任务**：2026-02-25 上线，自 07-07 起在云端运行，设备离线照常执行。帮助文档里**没有事件触发器**（"收到某类邮件即运行"）；对照：Copilot Cowork 2026-08 已上线事件触发。
- **云端后台会话**：合上笔记本后继续运行，可在桌面、web、手机之间接续。
- **Claude Tag**（2026-06-23 起 beta，Team/Enterprise）：Slack 里的 @Claude。支持常驻指令和 ambient 主动跟进，在客户系统里用独立的 Agent Identity，记忆按频道和身份隔离。流程分析见 [[Claude Tag 驱动的团队研发流程]]。
- **Claude Duet**（2026-10-21 起 research preview，仅美国、需排队）：独立的个人主动式 agent，带浏览器的云端 VM，基于 Opus 5.5。
  - 每隔几小时检查一次已连接账户，官方理由是节省额度（见 [[常驻 Agent 的算力经济学]]）；
  - 审批比 Cowork 更严：发消息、付款、签署、删除都要批准；买卖证券和账户间转账即使批准也禁止。

## 权限与治理
- **默认审批**：Pro/Max/Ultra/Team 默认 **Auto**，不逐步询问，每个动作执行前有自动安全检查；Enterprise 默认 **Manual**，逐个动作请求批准。永久删除文件默认要用户显式点 Allow。官方承认 computer use 会绕过其他工具的权限检查。

  > ⚠️ 矛盾：Anthropic 2026-09-16 博客称 "By default, Claude asks before taking an action"，但帮助文档写个人档和 Team 默认是 Auto。截至 2026-11-06 两种说法并存。（发现于 2026-11-06）

- **企业控制**：RBAC/SCIM、组级支出上限、按 connector 工具粒度的读写管控、OTel（记录每个动作是人工批准还是自动批准）、Compliance API。2026-11-05 又推出安全中心（beta）、inference hooks（GA，可以把提示和工具调用交给客户自己的 DLP 检查），以及可装进本地 VM 的 EDR 传感器。
- **已知限制**：EDR 看不到云端会话；Admin API 强制登出不会终止已经在跑的云端会话和定时任务。
- 推断：放进 [[Agent 授权三层]] 看，Claude 的执行隔离最规范，但授权语义一层默认偏宽（个人档 Auto、持久化的 "always allow" 只有企业管理员能禁用）。

## 已知事件
- 2026-01：PromptArmor 演示了间接提示注入，借已放行的 Anthropic API 域名把文件外传到攻击者账户（Simon Willison 转述）。
- 2026 年多起误删文件报告。投资人 Nick Davidov 称约 15 年的家庭照片被删，后经 iCloud 找回（MIT AI Incident 数据库 #1441）。GitHub #67188 报告删除任务时连带删掉文件、停止按钮无效，被当作重复 issue 关闭并锁定，data-loss 标签被移除，始终没有维护者回复。
- 2026-10-06 强制上云，引发"失去本地选项、敏感文件上云"的反弹。
- 2026-10-30，Claude Code 与 Cowork 的产品负责人 Cat Wu 离职，随后加入 OpenAI。

## 采用与市场
- Anthropic 自述：Cowork 用量中超过 90% 不是软件开发（2026-07-07）。
- Anthropic S-1（2026-10-26，11-02 S-1/A 未改此措辞）：截至 2026-09-30，Cowork 的采用速度超过了 Claude Code 在同一阶段的水平。S-1 没有按产品拆分收入，也没有 Cowork 的用户数。
- 2026-02 插件发布触发全球软件股抛售，见 [[cowork-saas-资本市场冲击]]。
- **Microsoft Copilot Cowork**（2026-03-09 发布，06-16 GA）：采用 Claude Cowork 的执行框架，在 M365 租户内运行。但 Microsoft 在持续对冲：
  - 模型选择器已加入 GPT 6.1 Sol 和 Grok 4.7，管理员可以关掉 Anthropic 模型族；
  - 它自称每个 prompt 比"Claude Cowork + M365 connector"便宜 30–40%（厂商自测）。

## 同类产品与竞争
- 2026-08 至 10 月，Grok Bot、Meta Muse、OpenAI Dots 相继上线，都是"每人一台托管云电脑的常驻 agent"。Anthropic 的回应是"降为执行层 + Tag + Duet"三线拆分，不再推出单一的对应产品。格局与定位见 [[常驻 AI 同事的竞争格局]]。
- 与 [[Claude Code]] 的分界：Cowork 面向非技术知识工作者，Claude Code 面向开发者与工程流程；综合：两者共享同一 agent 能力栈（互见该页"与 Claude Cowork 的分界"）。
- [[Codex]] 与 Cowork 是"agent 替代/放大知识工作"的两极：Cowork 从非技术知识工作者切入，Codex 从开发者起步、再向非开发者外溢。采用数据见 [[codex-agent-采用曲线]]，体验成本见 [[生产力-体验悖论]]。

## 安全边界（产品原则，未变）
"完成任务，但**consequential decisions 仍留给用户**"，保留人类监督。实际默认值见上方"权限与治理"。

## 命名与对外话术
- 对外和内部一律使用官方名 **Cowork**（Claude Cowork），不使用自定义别名。2026-09 合并后，官方叙事是 "Cowork is now Claude"。
- 底层机制是"Agent 编排 + 能力包（skills / sub-agents）+ connector（可基于 [[MCP]]）"；本地文件与桌面能力经 Claude Desktop 执行，不能一律说成 MCP 连接。对外提到 MCP 时应说"connector 可基于开放标准 MCP"。
- 演示素材：架构图 `raw/assets/cowork-plugins-mcp-architecture.svg` 已因"plugin = MCP Server"的错误废弃，仅供追溯；现行承载页是 [[cowork-plugins-架构]]。

## 历史
- **2026-01-12**：research preview，仅限 macOS 桌面端的 Max 用户；agent loop 原生运行在设备上，代码在专用的本地 Linux VM 里执行。
- **2026-07-03 检索口径**：只在所有付费计划的 Claude 桌面应用中提供，定位强调"运行在桌面端，知识工作真正发生的地方"。
- **2026-07-07 至 2026-10-05**：web/mobile 可以发起并运行云端会话（beta，从 Max 档开始分批开放），本地文件与应用依赖 desktop bridge。用户可以在设置里选 "Only on your computer"。（Anthropic release notes 2026-07-07 条目 "Claude Cowork on web and mobile"：https://support.claude.com/en/articles/12138966-release-notes ；帮助文 https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile ；均检索于 2026-11-07）
- **2026-09-16**：与 chat 合并为一个 Claude，Pro/Max 先行；Enterprise 于 10-23 GA。
- **2026-10-06**：Pro/Max/Ultra 的新任务一律在云端运行，"Only on your computer" 选项被移除且不可切回；已在本地启动的任务和定时任务可以继续在本地跑完。
- **2026-10-30**：套餐改名，原 Max 5x 改称 Max（$100），原 Max 20x 改称 Ultra（$200）。
