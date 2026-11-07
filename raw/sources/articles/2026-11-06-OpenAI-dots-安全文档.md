# Safety and security in dots（中文结构化摘录）

- 原始 URL：https://learn.chatgpt.com/docs/enterprise/dots-security （正文取自同址 `.md` 端点 https://learn.chatgpt.com/docs/enterprise/dots-security.md ）
- 发布方：OpenAI（ChatGPT Learn 文档站 learn.chatgpt.com，Enterprise 栏目；页面 og:title 为 "Safety and security in dots | ChatGPT Learn"，meta description 为 "Review dots security controls, data handling, and audit and offboarding considerations"）
- 页面日期：页面未标注（`.md` 正文与 HTML 均无发布/更新日期字段，HTTP 响应无 Last-Modified；文件名按约定取抓取日 2026-11-06。正文仅提到 "the October 1 rollout"，未注年份）
- 抓取日期：2026-11-06（curl 直连 .md 端点；同址 HTML 仅用于核对标题、元数据与日期）
- 存档原因：常驻 AI 同事研究（2026-11-06）中「Agent 授权三层」与产品安全架构对比的一手证据；厂商文档会事后改版，故冻结快照。
- 存档说明：要点式中文结构化摘录，非翻译；关键原句保留英文原文并加引号。原文 `.md` 约 8.2 万字符（表格对齐空格折叠后约 5.4 万字符），超出 verbatim 阈值。按原文章节顺序组织，二、三级标题保留英文原题；原文表格逐行保留（单元格内容压缩为中文要点）；原页插图在 `.md` 中仅有文字说明（"Illustration: ..."），按要点摘入；正文内外链择要保留，完整清单见文末。所有安全相关的机制、默认值、限制与原文自承的风险/未验证项均已保留。原文中的产品/模型名（dots、Auto-review、Custom Rules、Agent Security、Activity View、GPT-6、GPT‑6.1 Terra 等）照录。
- 存入后视为只读存档。

---

## 导语（页首）

- 定义："A dot is a personal agent that can keep working between conversations."
- 谁能用：管理员用 RBAC（role-based access control）决定谁能用 dots。"A personal dot uses the app connections its owner has authorized, within the app and action limits set by the workspace. The owner specifies what the dot may do."
- 能力边界的三个决定因素："What a dot can do depends on the employee’s permissions, the actions the workspace allows, and where the dot performs the task."

## Security overview

- 运行形态：personal dot 可在对话之间代 owner 工作（例：跟踪项目，随更新到来准备简报）。"The dot works from its own cloud computer and can delegate tasks to Work or Codex. In a connected app, it inherits the permissions of the account its owner authorized. The workspace’s app and action settings apply to both the owner and their dot."
- Prompt injection 防线：项目文档可以为简报提供事实，但 "OpenAI trains the models behind dots to resist any hidden instructions in the project document or similar kinds of prompt injection." "Auto-review checks consequential actions before they run, and safety monitoring can pause or stop work if it detects potentially harmful behavior."
- 六个要点：
  - **Cloud computer**："Admins control browser access, network access for code, and desktop interaction separately." 启用浏览时，dot 可访问公开站点，或 "use a website with the permissions of the account signed in there"。owner 可查看 cloud computer 或接管（take over）。
  - **Action review**：分享简报前，Auto-review "checks what would be shared, who would receive it, and whether the owner’s instructions, Custom Rules, and safety requirements allow it. It can block the action or require confirmation. The dot cannot turn off a required check."
  - **Connected computers and Codex Cloud**：dot 在 connected computer 上运行的工作遵循适用的本地 Agent Security policy；委派到 Codex Cloud 的任务 "follows the Codex Cloud policy and the permissions of its selected environment."
  - **Owner oversight**：在 Activity View 中，owner 可查看进行中与委派出去的任务、纠正指令、要求 dot 停止。
  - **训练与留存**："Enterprise data is not used to train models by default. Dot context, files, delegated tasks, and audit records have different retention and deletion boundaries; verify the requirements for each copy."
  - **Audit records**：管理员用可用的 compliance records 调查 dot 活动，并 "check the connected service’s own records to verify what changed."
- **A familiar cloud environment**：dots 构建在与 ChatGPT Work 相同的 cloud computer 基础设施上，遵循工作区适用的隐私与安全保护。"Dots can preserve cloud computer snapshots across sessions, so work can continue without starting from scratch." 已评估过 Work Cloud 的组织可以把该评估作为评估 dots 的起点。
- **Choose which cloud capabilities to enable**：即使关闭 cloud browser、cloud computer desktop、代码与 shell 命令的互联网访问，成员仍可用 dot 起草内容、整理信息、使用工作区允许的 connected apps。"These settings also apply to Work Cloud, so changing them can affect both dots and Work tasks."
- **Understand proactive research**（dots 与普通用户发起的 Work 任务的区别）："A dot can look for useful information in permitted connected apps without waiting for a new request from its user." "During proactive research, a dot can read permitted information and save private notes. Its research tools can’t directly send messages to other people, change content through connected apps, or control a browser or computer." 其他活动（如用户显式排程的任务）遵循各自适用的权限与动作规则。
- 尚在开发（路线图）："We’re developing additional rules in Agent Security so admins can choose which sites a dot’s cloud browser can visit."

## How dots protect workspace data

- **模型防护**：OpenAI 训练 GPT-6 家族模型拒绝有害请求、抵抗隐藏在邮件、文件或网页中的恶意指令。"For example, an email asking a dot to forward a private file does not authorize the dot to send it. That authority comes from the owner or an automation the owner authorized."（引 https://deploymentsafety.openai.com/gpt-6-october/prompt-injection ）
- **Auto-review 在动作执行前检查**：例如发邮件前，按 owner 指令、Custom Rules 与安全要求检查收件人和内容；可阻止发送，"the dot can’t turn off a required check"。评测数据："In a simulated Codex task, none of the GPT-6 models tested bypassed an Auto-review denial."（引 https://deploymentsafety.openai.com/gpt-6-1-terra/respecting-auto-review ）"Some default action and confirmation rules can be customized, but owner approval cannot override built-in safety requirements."
- **Safety monitoring 可中断进行中的工作**："As a dot plans and acts, monitoring looks for potentially harmful behavior, such as attempts to bypass a safeguard or act outside the owner’s instructions." 发现问题可暂停或停止任务；"A pause can surface a warning for the owner to review."
- **插件访问由工作区设置管理**：同一套设置决定用户及其 dot 能用哪些插件与动作；dot 的 cloud browser 访问由另一项设置控制。原文自承的旁路："A read-only plugin limits what a dot can do through that plugin. If cloud browser use is enabled, the dot may still be able to make changes through an account signed in on the website."
- **Owner 复核与纠偏**：在 Activity View 查看委派任务、补充上下文、改方向、要求停止。"When a dot can’t finish a task, it should tell the owner what got in the way and what remains undone." 评测数据："On coding tasks selected to elicit blocker-reporting failures, GPT‑6.1 Terra failed to report the blocker accurately in about 8% of cases, down from 29% for GPT‑5.6 Terra."（引 https://deploymentsafety.openai.com/gpt-6-1-terra/blocker-deception ）时效风险："Timing matters when information is shared. If the dot has already posted in Slack, people in the channel may already have read the message."
- **上线前复核清单**（原文提示框 "What to review before rolling out dots"）：决定哪些员工可用 dots；dot 使用 owner 已有的 app 连接——检查每个连接账号让 owner 能读/改什么、工作区经该连接允许哪些动作；若 dots 可用 cloud browser 或把工作委派到 connected computer，检查那里的登录账号或本地设备允许什么。

## Confirm eligibility and data requirements

| 类别 | 资格与数据要求（要点） |
|---|---|
| Data and inference residency | 数据存储驻留支持 Australia、Canada、Europe（EEA 与 Switzerland）、India、Japan、Singapore、South Korea、UK、US；不含 UAE。dots 推理驻留支持 US 与 Europe，不含 UAE。"Inference residency covers model inference, not every processing step or third-party integration." |
| Enterprise Key Management (EKM) | 符合条件的工作区支持。客户管理密钥保护受支持的静态客户内容，客户可轮换或吊销密钥。"Identify which data your agreement requires the key to protect." |
| HIPAA | 符合条件的工作区支持；需确认 BAA 与配置覆盖预期工作流。 |
| Zero data retention | "Neither dots nor Work with local computer access provides strict zero data retention." |
| FedRAMP | "Dots are unavailable in FedRAMP workspaces." |

## Manage who can use and direct a dot

- **Workspace access**："During the admin preview, access to dots is off by default." 为某组启用：在该组的 custom role 上授予 Use dots。（插图示例：Use dots 与 messaging channels 开；local computer access 与 custom rules 关；原文注明开关位置仅为示意。）
- **Dot ownership**："Only the owner can direct their personal dot. Messages from other people, including Slack mentions, do not start work or give them control over the dot."
- **Connection permissions**：personal dot 使用 owner 已有的插件连接；经每个插件，dot 只能访问 "the connected account, the plugin permissions, and the workspace settings allow" 的数据与动作。
- **Automations**："An owner can use an automation to approve an action in advance by specifying what the dot may do and when."（例：每周五在团队 Slack 频道发项目更新。）"The dot is designed to stay within that authorization and follow the usual permissions and safety checks."

## Where a dot works and which controls apply

- 权限图（插图要点）：工作区权限启用 dots；owner 指挥 dot；connected apps、cloud computer、local computer、委派的 Work 与 Codex 任务各有适用的权限与控制；"The main dot conversation has separate model-control boundaries."
- 原文自承的覆盖缺口："Auto-review coverage across browser, desktop, and delegated actions remains under review."
- 协调在云端、执行可在本地："A dot coordinates work in the cloud." 例：要它总结 connected laptop 上的报告，读文件的命令在 laptop 上运行，由 Agent Security 本地策略决定该命令能读哪些文件。
- 架构图（插图要点）：owner 向 dot 发请求并接收交还；dot 把 selected context 和任务送往委派的 Work 或 Codex 线程并取回结果；需要复核的动作送 Auto-review，Auto-review 返回 "a block and reason" 或允许该动作在 cloud workspace 中执行；复核考虑 owner 的指示、Custom Rules 与安全要求；cloud workspace 连接 apps，并经 local-access gate 与设备权限连到个人电脑。原句："Dashed task boundaries do not establish isolation; review coverage remains under review."
- 本地工作的两级开关："To make local work available, an admin enables Allow local computer access for dots. Each employee then chooses whether to connect their computer in ChatGPT."
- 并行委派：dot 可在 owner 继续对话的同时并行委派任务，"It can start a Work or Codex thread on the owner’s behalf."本地访问启用且 owner 已连接电脑时，任务可使用该电脑上的文件或工具；仓库类工作 dot 还可在可用的云端编码环境里开 Codex Cloud 线程，不使用 owner 的电脑。在 Activity View 打开任务可看其运行位置。

### Controls by work environment

- 判定原则："Start with where the dot takes an action and which account it uses." 例：限制员工 laptop 上文件修改的规则只在那里生效，dot 自己的云端文件另有控制。"If an action must be blocked everywhere, check every enabled way the dot could take it. Some actions also require owner approval."

| 环境 | 适用哪些控制 | 管理员设置 / 成员动作 |
|---|---|---|
| Main dot conversation | 工作区角色决定谁能用 dots、谁能设 custom rules；owner 在此对话中指挥 dot。"Enterprise model controls and defaults do not apply to the main dot conversation." | Admin：Admin Console → Permissions 中，在工作区默认或 custom role 上设 Use dots 与 Use custom rules for dots；managed approvals 与 web search 在 Agent Security → Global；在 Plugin controls 查 app 权限。Member：告诉 dot 要做什么；若工作区启用 custom rules，可设常驻指令，如 "Ask me before changing a shared file." |
| Plugins (connected apps) | 使用 owner 已授权的 app 连接；经该连接能读/改什么，取决于 owner 在该 app 内的权限、授予插件的权限、工作区允许的动作。 | Admin：在 Plugin controls 设可用 app 与允许动作；在源服务查连接账号的权限与授权 scope。Member：连接管理员允许的插件。 |
| Dot’s cloud computer | cloud computer 设置管浏览、代码与 shell 命令的网络访问、computer use。"The dot can create, edit, or delete its own cloud files. Websites use the account signed in to the cloud browser. The employee’s laptop sign-ins, VPN, and device policies do not automatically carry over." | Admin：Admin Console → Permissions → 选工作区默认或角色 → Workspace capabilities → Let agents use cloud computers，分别设 Use a browser、Allow network access (code and shell)、Allow computer use；Use password manager 在 Workspace capabilities 下单独设。Agent Security 站点规则 "would let admins allow or block domains in the dot’s cloud browser and choose which sites permit uploads or downloads"（原文为条件式）。Member：从 dot profile 打开 cloud computer 看它在做什么；Take over 亲自做一步，Return control 交还；网站要求登录时用 private form 或接管 cloud browser 登录。 |
| Delegated Work or Codex task | dot 开出独立的 Work 或 Codex 线程时，由该产品的 model controls 决定任务可用的模型；"The task follows the Agent Security requirements and other controls that apply where it runs." | Admin：在 Permissions 查 Work/Codex 访问并审该产品的 model controls；connected computer 查 Agent Security → Global 及 Local overrides；Work Cloud 审 cloud-computer capabilities；Codex Cloud 查 Agent Security → Codex Cloud 与 Settings → Codex Cloud → Environments。Member：在 Activity View 打开委派线程，查看运行位置、来源与结果，在那里补上下文。 |
| Connected employee computer | 工作区须允许 dots 本地访问，且员工须连接电脑；其上的命令遵循适用的 Agent Security 与设备策略。"The dot can use permitted local files, tools, and apps while the cloud continues to coordinate the task and can process its context." | Admin：Admin Console → Permissions → Use dots 中启用 Allow local computer access；connected computers 继承适用的 Agent Security → Global 设置，同一策略内可用 Local 覆盖受支持的文件系统或网络限制；设备权限同样作用于桌面 app 与屏幕访问。Member：在该电脑的 ChatGPT app 打开 dot profile → Computers → Your computer → Allow access 并确认；保持电脑在线且 ChatGPT 打开。 |

- 插图（私密登录表单示意）："Credentials are sent privately to the website; using a saved credential requires confirmation."

### How managed policies apply

- **Global policy**：在 Agent Security → Global 检查 managed approval requirements，以及该工作流是否允许 web search。
- **Execution overrides**：员工 laptop 上的命令，查 Agent Security → Local 的文件系统与网络限制；委派到 Codex Cloud 的命令，查 Agent Security → Codex Cloud 与所选环境的网络设置。
- **Separate controls**：dot 的 cloud computer 与 Work Cloud，需分别检查浏览器访问、代码与 shell 网络访问、computer use；委派的 Codex Cloud 任务需检查所选 Codex 环境。

## Control connected apps and credentials

| 访问路径 | 要检查什么 | 控制覆盖什么 |
|---|---|---|
| Plugins (connected apps) | 在 Plugin controls 审成员可用的 app 与动作；在源服务查是哪个账号授权的连接；发邮件需验证该动作已启用、且该账号能发给目标收件人。 | "The dot can use an existing connection only for actions allowed by the workspace and permitted for the connected account." 结束访问：在源服务吊销 app 授权。"This stops new requests through the connection. The dot may still have information it retrieved earlier. App access is shared with other ChatGPT experiences." |
| Browser sign-ins | 确认网站上登录的是哪个账号；授予敏感数据访问前，同时核对 app 连接与网站账号在源系统中的权限。 | "For example, a plugin may allow the dot to read a document while the website account can also edit it. Check the website account’s role before allowing that browser workflow." |
| Website credentials | 网站登录用 private sign-in form 或接管浏览器。"For supported sign-ins, OpenAI sends the password directly from the private form to the cloud browser without exposing it to the model." App 工具可经后端凭据处理认证，浏览器自动化可使用已登录会话；cloud browser 的会话 cookie 与成员设备分开存储。原文自承风险："Code on the dot’s computer can read an app token or browser cookie if its value is exposed to that code; do not assume the session or token is isolated from code running there." "Plugin credentials and values used only in browser sessions do not appear in logs." | "A new sign-in with a saved password requires confirmation. Once signed in, the dot can use the website with that account’s permissions." 结束访问：管理员在源服务吊销网站会话（where supported）；成员可在 cloud browser 中登出，或在 Settings → Cloud browser → Browser data 清除该站 cookie。 |
| Codex Cloud secrets | 委派的 Codex Cloud 任务用文档化的环境 secret 控制。"Network secrets pass a placeholder to programs and substitute the credential for allowed HTTPS destinations. Direct environment variables are visible to programs." | 仅适用于 Codex Cloud（配置见 Codex Cloud environments 文档）。 |

## Set rules for approvals and unattended work

- Proactive research 定义与边界："Proactive research is background work a dot does between requests to find updates relevant to its owner’s work. This research is read-only." 可读取 owner 有权经 connected apps 访问的信息，并保留关于发现的私人笔记；"Its research tools cannot send messages, edit shared content, or control a browser or computer." "To send a finding to Slack, the dot needs the owner’s authorization for the send and its audience. Auto-review checks the proposed send."
- 插图要点：dot 与研究任务都在 dot 的 cloud environment 内；研究向 connected apps 发读请求，取回 owner 权限允许的信息，向 dot 返回 private notes；"research tools are read-only"。
- 授权常驻任务的写法："When authorizing a recurring task, name the action, recipients, trigger, and schedule. Permission to draft a customer email covers the draft. Sending it requires authorization."

| 机制 | 做什么 | 条件与限制 |
|---|---|---|
| Action approval | owner 可授权 "Email the weekly project update to the project leads every Friday."，该指令覆盖所列收件人与日程。 | "A new approval will be needed for changes that fall outside that scope, including changes to the audience, content, or timing." |
| Auto-review | "Auto-review checks tool calls labeled “write” before they run." 例：发邮件前，按 owner 指令、Custom Rules 与安全要求检查收件人与内容。 | 可阻止发送，或提示 owner 澄清收件人/批准该动作。"Approval cannot override a required safety check. Computer Use asks separately for permission to use a desktop app." |
| Custom Rules | owner 可设"发邮件前先问我"之类规则，增加一个审批步骤。"It cannot grant a send permission the connected account lacks or override a required safety check." | "Disabling custom rules does not force every action to ask for approval." 需区分：成员可编辑的规则 / Agent Security 中的企业要求 / 被连接服务强制的权限。 |

- 插图（Auto-review 流程）要点同上文架构图；原句："Coverage across browser, desktop, and delegated actions remains under review."
- **Delegated work on a local computer**：委派线程使用成员的 connected computer。"When Computer Use is enabled and the app is approved, selecting “Always allow” lets ChatGPT use the app without asking for access again."

### Example: Sending the same external email through three routes

- 场景：owner 授权 dot 每周五把已批准的项目更新发给客户方的 Lee，不带附件；对比加一个新收件人。"A new recipient needs fresh authorization. If company policy prohibits the recipient, even the owner’s approval cannot authorize delivery."

| 途径 | 技术上被阻断 | 需要新批准 | 常驻授权 |
|---|---|---|---|
| Email plugin | 发送动作被禁用，或连接账号没有发送权限。 | 加收件人需要新决定；若 app policy 要求写操作前询问，原始那次发送也需批准。 | 若动作已启用、账号能发、适用检查放行，周五发送可进行。 |
| Cloud browser in web-based email | 工作区禁用 cloud browser，或邮件服务拒绝该登录账号的投递。 | 新收件人需批准才能发。"Confirming a saved login approves sign-in only. A prompt at the Send button is unverified." | "An active session can be reused. The Friday instruction covers the original message. Verify whether web-based email can send it unattended." |
| Approved desktop mail app | managed Computer Use policy 拒绝该 app，或邮件服务拒绝 app 内账号的投递。 | "A new recipient needs approval even if the app is already open. Whether Computer Use prompts at Send is unverified." | "Always allow lets the dot reopen the app. The Friday send still needs its own standing instruction. Verify unattended delivery in the delegated task." |

- **Enterprise requirement across all routes**：若组织禁止外发，须在邮件服务中对每个发送账号强制该限制，或禁用每一条能发送的途径；若每封外部邮件都须有人批准，须验证每条启用途径都会在投递前暂停，"including when a browser session or desktop approval is already active. A member’s custom rule or a successful plugin test alone does not establish that coverage."
- **Verification**：每条途径用同一个测试邮箱和一次性消息，分别测试被禁止的收件人、新但允许的收件人、已授权的周五发送；记录哪个控制起作用、是否有人批准、邮件服务接受还是拒绝。"Verify per-send behavior for each enabled browser and desktop route before approving the workflow."

## Review browser, network, and device access

（插图：示例 cloud computer 设置中 browser、network access、computer use 均开启，仅为一种配置示意。）

### Dot’s cloud computer

- **Cloud capabilities**：Use a browser 控制 dot 的 cloud browser；Allow network access (code and shell) 控制命令的互联网访问；Allow computer use 控制与桌面 app 的交互。"Site rules in Agent Security would let admins allow or block domains in the dot’s cloud browser and set upload and download permissions by site."（原文为条件式）"Within an allowed site, the dot’s access also depends on the account signed in there."
- **Password manager**：单独审查 password manager 访问。"Cloud browser, network, and computer-use controls can apply to dots even when ChatGPT Work is disabled."
- **Local protections**："A dot’s cloud browser has its own session. Signing in to an internal site on a laptop or connecting the laptop to a VPN does not give the cloud browser that session or network route."
- **Network rules**：例：在 laptop 上为终端命令屏蔽某主机名，只限制该命令路径；若 cloud browser、plugins、web search 能到达同一目标，需分别测试。"Disabling code and shell internet access does not, by itself, disable the cloud browser or connected apps."

### How sign-in works in the cloud browser

- "The cloud browser is optional in dots. Admins can disable it by turning off “Use a browser.”"
- 企业 SSO 网站：员工从 dot 的 cloud browser 登录；使用 private sign-in form 时先核对站点地址，再在表单中输入凭据与验证码。"The form sends them directly to the cloud browser, outside the model’s view."
- 表单无法完成某个登录步骤时：选 **Open computer** → **Take over**，亲自完成企业 SSO 与 MFA；app 打开后选 **Return control**，dot 以你的已登录账号继续；若站点再次要求验证，先完成再让 dot 继续。
- 设备与 VPN 前提无法满足："If corporate SSO requires a company-managed device or a connection through your corporate VPN, the cloud browser cannot use your laptop’s device status or VPN connection to meet that requirement. Keep the policy in place." 替代做法：若有已批准插件支持该任务，用插件 + 为该动作授权的连接账号；仅网站可做的任务，在满足策略的设备与网络上完成。
- Cookies 与令牌："The cloud browser keeps its own cookies, separate from the browser on your device. This includes authorization tokens to retain signed-in states for saved sessions, as applicable." 要登出并结束保存的会话：Settings → Cloud browser → Browser data 清除该站 cookie。

### Connected employee computer

- **Connection requirements**：管理员须允许本地访问，成员须连接电脑；本地工作期间保持在线且 ChatGPT 打开。"Taking it offline leaves the connection in place."
- **Messaging channels**：成员可从另一设备经消息渠道发请求，dot 随后可开新线程并附上该成员的 connected computer（若可用）。
- **Device permissions**：摄像头、麦克风、屏幕访问还取决于 connected computer 本身，以及设备设置中授予 ChatGPT app 的权限。

## Review memory, retention, and deletion

- **Retained context**："A dot can save information it reads through an authorized app connection, such as a team decision shared in a Slack thread. Disconnecting the app stops future reads through that connection. Information the dot already saved may remain in its memory."
- **Model training**：默认不用企业数据训练模型。"Human review may occur in limited circumstances, including safety-related cases, even when model improvement is turned off."
- **Encryption**：静态数据 AES-256；传输 TLS 1.2 或更高（组织 ↔ OpenAI、OpenAI ↔ 其服务提供方之间）。
- **Dot context**："Removing workspace access preserves the dot’s data." 删除 dot 会在 30 天内删除其保留上下文（含私人研究笔记与后台研究线程历史），dot 自有备份同样 30 天内删除。**不随 dot 一起删除**：单独存储的 ChatGPT 对话与 Codex 线程、Space 中的文件、projects、connected storage 或用户电脑上的文件、基于 dot 对话加入 ChatGPT Memory 的信息——"Their owners must manage those copies separately."
- **ChatGPT Memory**：dot 对话可以贡献到 ChatGPT Memory；删除信息时须同时检查 saved memories 与 chat history。"Deleting only a conversation can leave a saved memory in place."

### Data retention by category

| 数据类别 | 留存策略 | 谁发起删除、如何删 | 期限、残留副本与例外 |
|---|---|---|---|
| Dot chats, native subagent history and scheduled tasks | 主 dot 在其生命周期内保留自身历史、配置与日程。 | 成员用 Reset 删除 dot（含对话、saved memories、日程）；移除工作区访问会保留 dot 数据；工作区管理员也可删除 dot，包括 owner 不在时。 | dot 删除后 30 天内删除 dot 自有聊天、原生 subagent 历史与定时任务。 |
| Dot memory, profile and private research notes | dot 在生命周期内保留自身上下文，独立于 ChatGPT Memory 设置；后台研究可从 connected sources 保存私人笔记。 | "Members cannot remove a specific dot memory or source-derived research note while keeping the dot." 要删只能删除整个 dot。 | "Revoking source access stops future access but can leave a derived note intact." 删除 dot 后 30 天内删除私人研究笔记与 dot 自有备份。 |
| Background research threads | 生命周期内保留与 dot 关联的研究上下文。 | 随 dot 删除一并删除。 | dot 删除后 30 天内删除其历史及 dot 自有副本。 |
| ChatGPT Memory | 由 ChatGPT 管理，与 dot 自身记忆分开。 | 成员在 ChatGPT 中删除 saved memory，并删除含该记忆的聊天。"Turning off sharing leaves context already received by the dot in place." | 删除 dot 不删除单独保存的 ChatGPT memories。OpenAI 可为安全与调试保留已删除 saved memory 的日志至多 30 天。 |
| Space files | 遵循 Enterprise 工作区留存策略；打开、下载或重新附加已有 Space 文件不会重启其留存期。 | 成员在 Space 中删除；合规管理员可经 Space API 删除；也可按工作区策略过期。 | Space 文件在 dot 删除后仍存在。Space 删除后 30 天内安排永久移除；例外：已去标识化且解除关联的数据，或为安全/法律义务保留的数据（另见 Backups）。 |
| Cached files and Outputs | "The dot chat can keep a separate copy of a Space file." Space 的留存与删除控制只作用于 Space 那份。 | "Deleting the Space file, even from Trash, does not trigger deletion of the dot-chat cache. No separate self-service removal procedure is confirmed." | "A file may remain listed in Outputs after the Space copy is deleted." dot 自有缓存副本在 dot 删除后 30 天内删除。"A separate way to clear the listing remains unconfirmed." |
| Cloud computer files and browser state | dot 的云盘可保留文件与浏览器状态；快照过期取决于工作区配置。 | 删除 dot 会删除其 cloud browser 与 computer。 | dot 的云电脑数据、磁盘、浏览器状态、快照与备份在 dot 删除后 30 天内删除；存到别处的副本按目的地策略。 |
| VM snapshots | 对启用了数据驻留、EKM 或两者的符合条件工作区，"the enabled control wipes snapshots on a five-day cycle, with a seven-day maximum." | 平台自动让快照过期；删除 dot 另行启动云电脑删除流程。 | "For workspaces without data residency or EKM, there is no maximum age for an active dot’s snapshots. They may remain for as long as the dot exists, and customers cannot currently request an early purge." dot 删除后 30 天内删除快照。 |
| Backups | Space 备份有单独的文档化窗口；dot 自有备份在 dot 删除后 30 天内删除。 | Space 文件被删除、过期或失活后，活跃的 Compliance API 不再返回它；备份过期由平台管理。 | "A Space backup may remain for up to 30 additional days, or longer for security or legal obligations." |
| Delegated Work and Codex threads | 托管的 Work 与 Codex 线程遵循工作区留存策略；仅存在设备上的记录遵循本地存储与备份策略。 | 托管线程何时过期由工作区策略决定（Codex Cloud 见工作区留存指引）。"Deleting a dot leaves its delegated Codex and Work threads intact." | 在桌面 app 删除 Codex 聊天后，OpenAI 在 30 天内安排永久删除（有公开例外）；Work Cloud 删除的聊天同样 30 天内安排永久删除（有公开例外）。 |
| Files and pages in Spaces | Space 页面持续存在直到有人删除，工作区聊天留存期不会让其过期；Space 中合格文件遵循工作区文件留存。 | 页面的 creator 或 owner 可把页面及子页移到 Trash；单独保存的附件在其各自位置删除；成员可删自己的 Space 文件；具备所需 API 权限的合规管理员可删除合格文件。 | 永久删除或在 Trash 中满 30 天后清除。"Pages trashed before the October 1 rollout require manual deletion." 删除页面不删除单独存储的附件。 |
| Local files and connected-app copies | 由设备或被连接服务管理其上的文件、消息与导出。 | 有删除权限的人在源 app 或设备上删除；单独保留的副本由组织管理。 | "These copies survive dot deletion." 何时删完取决于目的地的留存期、备份规则与任何 hold。 |
| Compliance logs and customer exports | Compliance Logs Platform 自事件创建起保留每个事件 30 天；下载副本遵循接收系统策略。 | 平台自动过期；下载副本由组织在自己系统中删除。 | "Dot deletion neither erases emitted events nor restarts their clock. An organization cannot use the Compliance API to erase OpenAI’s internal audit or security logs." |

### Access changes and deletion actions

| 动作或数据类别 | 发生什么 | 管理员应做什么 |
|---|---|---|
| Disconnect an app | 停止经该连接的新访问；"The dot keeps its existing context." | 分别审查已保留的上下文与其他副本。 |
| Turn off ChatGPT Memory | 停止与 dots 的记忆共享；"Any context the dot already received remains." | 要移除 dot 已收到的上下文，需查看 dot 的删除选项。 |
| Individual dot memories | "Individual dot memories cannot be deleted." 要删 dot 全部上下文，成员或管理员只能删除 dot；ChatGPT memories 在 ChatGPT 中单独管理。 | dot 自有上下文：成员或管理员删除整个 dot；单独保存的 ChatGPT memories 在 ChatGPT 中处理。 |
| Reset/delete the dot | Reset 移除 dot、其对话、dot 自有记忆与定时任务。 | 先阅读删除通知并保全所需证据。 |
| Files and delegated records | Spaces 文件、本地/外部文件、Codex 线程、单独的 ChatGPT 对话，遵循其存储所在 app 或工作区的留存策略。 | 在每个存储位置分别完成删除。 |
| Cloud state, snapshots, and backups | 快照自动过期、云电脑删除、Space 备份留存各有独立时钟。 | 按上表逐份副本的期限处理；dot 自有备份在 dot 删除后 30 天内删除。 |

- **Data categories**：针对一条 Slack 消息的擦除请求，要定位源消息、引用或总结它的私人笔记、以及据其保存的报告，逐份核查删除路径。
- **Revoked source access**："Changing source-system permissions restricts future access through that source; it does not prove that retained context was deleted."
- **Privacy requests**：审查发现、更正、擦除需求时，须包含客户与非用户（non-user）的信息。

## Review messaging and audience boundaries

- **Slack identities**：离职处理时须同时检查 dot 自己的 Slack 身份与 owner 的 Slack 插件连接。"ChatGPT and enabled messaging channels reach the same dot." 各渠道对话分开，但 saved notes and context "can inform work across channels"。
- **Slack setup**：检查工作区通信权限与所需的 Slack app 审批，之后由成员完成设置。
- **Audience visibility**："Anyone with access to the conversation can read the dot’s posts." 用内部 Slack 频道做 dot 协助的工作；"We recommend using your dot only in channels where everyone is part of your organization. That excludes Slack Connect channels shared with customers or partners."
- **Sharing restrictions**：例：若 dot 能读一份私密 HR 文档，把其中薪资数字发到项目频道，就会暴露给所有能读该频道的人。"Before approving a post, specify what the dot may share and confirm that everyone in the channel is authorized to see it."

## Collect audit evidence and protect exports

### Choose the report for your task

- 调查用 compliance records；采用率报告用 Analytics API 数据。
- "Usage counts do not show who authorized an action or whether it succeeded."

### Trace an action

1. **Find the action**：找到成员的 prompt 与 dot 的回复，再查工具或插件事件；Slack 发送需对比插件结果与目标频道里的消息。
2. **Match the records**：用 user 与 workspace 标识定位记录。"Dots-attributed records use `client_id = DOTS` and include dot metadata where available." 用接收服务的日志核对结果。
3. **Trace delegated work**：委派工作找 parent thread 与 task ID；"Record any missing or redacted fields that prevent you from tracing the action."
4. **Check the destination**："A tool record can identify a requested command or browser action." 要验证实际到达的目的地，需对比该路径的 proxy 或 gateway 日志（若有）。"A local OpenTelemetry collector covers supported local execution events. Cloud orchestration falls outside that collector."

### Read today’s Compliance API records

| 活动 | 看什么 | 记录能告诉你什么 |
|---|---|---|
| Cloud browser or computer | TOOL_CALL_SUGGESTED | 识别 dot 尝试的工具。"Even with status=completed, the detailed output may be missing." |
| Connected app (plugin) | APP_MCP_CALL and APP_MCP_RESULT | call 写明工具名；result 报告成功或错误，可含输出预览或错误详情。 |

- 导出内容："Compliance API exports include user prompts, dot replies, tool-call requests and responses, and background activity." 调查时需关联可用记录并到被连接服务核对外部效果；"Some links and outcomes may not be present in the export."
- 尚在开发（路线图）："We’re working on more detailed Compliance API records for dots and other agents that run in the cloud." 目标是让安全团队能跟随 agent 在任务中的步骤，包括调用了哪些工具与 connected apps、何时经过自动审查；"We’re also exploring ways to show what those tools returned and which sites the cloud browser visited."

### Retain and protect exports

- **Retention period**：Compliance Logs Platform 保留记录 30 天；"Export the records you need continuously if you must retain them longer."
- **Export access**：限制谁能读导出、谁能用其密钥；"An export can contain an employee’s message or a preview of a plugin result." 对系统实际收到的记录套用留存、e-discovery 与 legal-hold 规则；"Confirm separately whether a hold covers original chats, files, or dot notes."
- **Log permissions**："Broad compliance access and conversation-message permissions require a workspace owner’s grant." owner 或 admin 可授予受支持的更窄日志权限。

## Stop work, revoke access, and manage departures

- 适用场景：拥有 personal dot 的员工（dot owner）已离职或无法协助；ChatGPT workspace owner 或 workspace admin 从自己的账号操作。"If activity continues or you cannot verify that sensitive work has stopped, open an OpenAI Support case immediately while you take the steps below."
- **Remove workspace access if the employee has left**：手动管理的成员由 workspace owner/admin 移除；目录管理（SCIM）的成员由身份管理员移除 workspace assignment，同步后验证该员工已不是活跃成员。"Workspace access ends when membership is removed. Verify dot containment separately: running work can complete after dot revocation, and the effect of member removal on each active and delegated task requires confirmation."
- **Revoke dots access if the employee needs to keep workspace access**：workspace owner 在 Workspace settings → Permissions & roles 审查 Use dots (Beta)，检查工作区默认、直接分配的角色与组角色。"Any remaining grant can keep dots enabled." 改动共享授权前先查谁还依赖它。
- **Find the employee’s agents in the Admin console**：workspace admins（含 owners）可查看某用户的 agents，并暂停或删除 dot。
- **Pause the dot**："This prevents it from starting new work, including its own scheduled runs. If the dot already started a task in a separate Work or Codex thread, that task can keep running." 要停止须单独取消该任务；还要检查 dot 创建的独立日程。
- **Resume the dot**："Only an admin can resume a dot paused by an admin." 恢复后先前会话重新响应消息；委派工作不受影响。
- **Revoke dots access**："Currently running work can complete, new messages do not trigger model actions, and schedules are paused." 移除工作区成员资格的效果需另行验证。
- **Delete the dot**："Deletion is unrecoverable, so preserve required evidence first. Deleting a dot deletes its cloud browser and computer, but does not remove user-level plugins."
- **Revoke connected accounts and sessions**：由相关服务管理员吊销 app 授权，并在支持时终止 dot 的 cloud browser 使用的网站会话；Slack 须同时检查 dot 自己的身份与员工连接的 Slack 账号；由设备管理员限制对 connected computer 的访问，并检查已在运行的本地工作。"Verify each revocation in the service that issued it."
- **Verify activity**："Running-work state can be checked in the Compliance API with a reported 30-minute p95. Scheduled-work state can be checked 30 minutes after the next scheduled run. These are reporting timings, not immediate-stop guarantees." 已完成的动作需到接收服务核查。
- **Contact support**：从自己账号在 help.openai.com 打开 chat bubble。"Support can guide a user or admin through stopping a dot; it cannot directly take actions affecting dots in the customer’s workspace." 需提供 workspace ID、员工邮箱、可用的 dot 或任务标识、已采取的动作、带时区的时间戳、最后观察到的活动。

## Related resources 与正文引用的一手链接

原文 Related resources：

- dots privacy, security, and safety FAQs：https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
- Manage dots in ChatGPT workspaces：https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces
- Manage dots permissions and capabilities：https://learn.chatgpt.com/docs/enterprise/dots-admin-guide
- Local computer access for Work Cloud and dots：https://learn.chatgpt.com/docs/enterprise/cloud-local-access
- ChatGPT Work cloud security：https://learn.chatgpt.com/docs/enterprise/chatgpt-work-cloud-security
- Agent Security：https://learn.chatgpt.com/docs/enterprise/agent-security
- Compliance API and audit events：https://learn.chatgpt.com/docs/enterprise/compliance-api

正文中另引的链接（择要）：

- Auto-review 机制（OpenAI 博客）：https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/
- Built-in safeguards（dots 发布文）：https://openai.com/index/introducing-dots/
- Auto-review 文档：https://learn.chatgpt.com/docs/sandboxing/auto-review
- GPT-6 model safeguards（prompt injection）：https://deploymentsafety.openai.com/gpt-6-october/prompt-injection
- Auto-review 拒绝遵从评测：https://deploymentsafety.openai.com/gpt-6-1-terra/respecting-auto-review
- Blocker reporting 评测：https://deploymentsafety.openai.com/gpt-6-1-terra/blocker-deception
- Connect computers and apps to your dot：https://learn.chatgpt.com/docs/dots/computers-and-apps
- Control your dot（Activity View）：https://learn.chatgpt.com/docs/dots/controls
- Codex Cloud environments：https://learn.chatgpt.com/docs/environments/cloud-environments
- Computer Use approvals：https://learn.chatgpt.com/docs/computer-use
- Analytics API：https://learn.chatgpt.com/docs/enterprise/analytics-api
- App permissions：https://help.openai.com/en/articles/20001495-managing-app-permissions-in-chatgpt
- Memory in ChatGPT：https://help.openai.com/en/articles/8590148-memory-in-chatgpt
- OpenAI Compliance Platform：https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-and-edu-customers
- SCIM provisioning and management：https://help.openai.com/en/articles/10011769-scim-provisioning-and-management
- Getting started with your dot（删除通知）：https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
