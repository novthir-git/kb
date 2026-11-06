# xAI Grok Bot 安全与审批文档：Grok Bot security FAQ + Approvals, security, and privacy（verbatim 存档）

- 原始 URL：https://docs.x.ai/grok-bot/security-faq ；https://docs.x.ai/grok-bot/approvals-security-and-privacy
- 发布方：xAI（docs.x.ai；页面 JSON-LD 署名 "SpaceX Super Intelligence"，页面标题后缀 "SpaceXSI Docs"）
- 页面日期：security-faq 页面标注 "Last updated: October 28, 2026"（JSON-LD dateModified 2026-10-28）；approvals-security-and-privacy 页面标注 "Last updated: October 29, 2026"（JSON-LD dateModified 2026-10-29）；文件名取较晚者 2026-10-29
- 抓取日期：2026-11-06（curl 直连 .md 端点 `https://docs.x.ai/grok-bot/<page>.md`；页面日期取自同址 HTML 的可见 "Last updated" 行与 JSON-LD）
- 存档原因：常驻 AI 同事研究（2026-11-06）中「Agent 授权三层」与产品安全架构对比的一手证据；厂商文档会事后改版，故冻结快照。
- 存档说明：正文 verbatim（英文原文），仅去除导航/页脚（含两页顶部的栏目标签 "Manage and protect"）。为把两页合入一个文件，各页 H1 改为 "## " 节标题、其下各级标题统一降一级，文字未改；站内相对链接（如 `/grok-bot/security`）保持原样，相对于 https://docs.x.ai 。每节开头的「本节来源」引用行为存档者所加。
- 存入后视为只读存档。

---

## Grok Bot security FAQ

> 本节来源：https://docs.x.ai/grok-bot/security-faq （页面标注 Last updated: October 28, 2026）

These are the questions security reviews ask most often. The controls behind
each answer are on [Grok Bot security](/grok-bot/security). Dashboard settings
and rollout steps are on
[Grok Bot for teams and enterprises](/grok-bot/teams-and-enterprises).

### Isolation and access

#### How are users isolated from each other?

Each user gets a dedicated Firecracker microVM with its own kernel, memory, and
virtual devices. One user cannot reach another user's computer. Within one
user, every Bot shares that computer. Treat a login or file on the computer as
available to every Bot that user runs. When a workload needs its own computer
and credential set, give it its own Cursor user. A teammate's
[shared Bot](/grok-bot/shared-bots) usually works on a user's computer during
that user's own chat with it.

#### What can a Bot access?

Only accounts and connected apps the member or team grants. A Bot has no
identity of its own and cannot hold more access than the signed-in member.
Connector tokens stay on Cursor's backend. Logins and cards saved in Vault, and
values entered in a Secure Form, are filled without the model seeing them.
Steps a form cannot handle, such as single sign-on or a passkey, are handed to
the member. See
[identity and sign-ins](/grok-bot/security#identity-and-sign-ins).

#### If we block an app, can a Bot still reach that service in the browser?

Yes. Blocking an app does not block that service's website. The connector
policy and the [network policy](/grok-bot/security#network-policy) are separate
layers. Closing the website path takes **Network Controls**, which is
Enterprise only.

#### Can admins push connectors to members?

No. The connector policy allows or blocks servers. Provisioning connectors to
members, whether mandatory or default-on, is not available.

### Network and egress

#### Can we restrict which destinations computers can reach?

**Network Controls is Enterprise only.** Admins set a Grok Bot network policy
from that panel on the Grok Bot page of the dashboard. Self-serve Teams do not
see it and cannot set a destination allowlist. Teams without a policy default
to allow-all. See [network policy](/grok-bot/security#network-policy).

#### Do admin controls apply per group, or only org-wide?

Directory-group scope is part of **Network Controls**, which is Enterprise
only. Groups can set their own policy, and a lock makes the team policy
effective for everyone. The organization-wide enable switch is also Enterprise
only and applies to the whole organization. Cloud Agents, Team Rules, and
public template sharing apply to the whole team on Teams and Enterprise.
Enforce Auto-review and Auto-review rules are Enterprise only and also apply
to the whole team. Allow Local Egress Routing is Enterprise only and applies to
the whole team. On Enterprise, a group's Grok Bot tab can widen Cloud Agents,
agent email, local execution, local egress, Auto-review, rules, and setup
scripts for that group's members, never tighten them. See
[Group settings](/grok-bot/teams-and-enterprises#group-settings).

#### Why do some websites block Bots?

Some services flag datacenter IP addresses. The egress ranges are shared static
ranges, available from your account team; allowlist them on your own services
where appropriate.

#### Are dedicated egress IPs available?

No. Computers use shared static egress IP addresses. Dedicated per-customer
IPs are not available. Current ranges are available from your account team.

#### Can traffic run through our own network?

Yes. A member can route a Grok Bot computer's web traffic through their
desktop, using its network and IP address. On that route, sites that resolve to
a private or VPN address are blocked unless they have been allowed for your
organization. Enterprise teams can also install a networking client on every
hosted computer through **Team Setup Scripts**. See
[Connect to private networks](/grok-bot/private-networks).

#### Grok Bot hangs at computer setup from our network. Why?

A TLS-inspecting gateway such as Zscaler is letting `api2.cursor.sh` through
and blocking or inspecting the computer's nested `cursorvm.com` hostname. Chat
may or may not keep working; the computer link fails either way. Allow
`*.cursorvm.com` and `*.*.cursorvm.com`, exempt them from inspection, and apply
the change to off-network profiles too. See
[Configure TLS-inspecting proxies](/grok-bot/proxies).

### Approvals, logging, and data

#### What does Auto Review check?

With enforcement on, Auto Review evaluates shell commands, app calls,
computer use, automation writes, and delegation such as Cloud Agent and
subagent launches. It can let an action proceed, require approval, or deny it.
On Enterprise, team admins can enforce Auto-review from the Grok Bot page and
add team Auto-review rules that every member inherits. Members can add stricter
personal rules on top, and **Ask first** wins when rules conflict. If an admin
turns enforcement off, members go back to their own rules only. It does not
review every side effect, such as memory writes and most settings changes.

#### Can our own security tooling check what Grok Bot sends to models?

Yes, with inference hooks, an Enterprise beta. Cursor sends each Grok Bot model
request, signed, to an AI security server your organization runs or uses
through a security vendor, and your server allows or denies it before the model
runs. Hooks check model inputs, not actions as they run. Team admins on any
Enterprise team can set them up from the dashboard. See
[Grok Bot inference hooks](/grok-bot/inference-hooks).

#### Can I see what Bots did on behalf of my team?

Spend and usage are on the dashboard usage page, broken down by product.
**Audit logs are Enterprise only.** They cover admin, security, and
authentication events, plus Grok Bot control-plane events like Bot creation,
access changes, Team Setup, and routines, filterable by application, and can
stream to your SIEM. **Action Recording is Enterprise only** and is a separate
setting, off by default. When enabled, it records Bot actions internally.
**OpenTelemetry Export is Enterprise only.** Configure it to receive those
events in your own collector, tagged `cursor.surface=grok_bot`. They do not
appear on the Audit Log page.

#### Can I restrict which models Grok Bot uses?

No. The team model allowlist does not govern Grok Bot. It uses SpaceXSI
first-party models and may use third-party models from providers on the
[sub-processor list](https://trust.cursor.com/subprocessors) regardless of that
setting. Teams with a model allowlist see this acknowledgement when they enable
Grok Bot. Grok Bot manages model selection, and there is no customer-facing
model picker. If your contract restricts subprocessors, contact your account
team. See
[Which AI models power Grok Bot?](https://cursor.com/help/grok-bot/models).

#### Where do Grok Bot computers run?

In the United States. Grok Bot is also covered by Cursor's
[US-only data residency](https://cursor.com/docs/enterprise/privacy-and-data-governance#us-data-residency)
program, which keeps inference, data processing, and storage in the US for
enrolled customers. Contact your account team to enroll. See
[data residency](/grok-bot/security#data-residency).

#### Can we run Grok Bot on-premises or from our own image?

No. Grok Bot runs only on Cursor-hosted cloud computers. On-premises
deployment, deployment inside your own perimeter, and bring-your-own-image
deployment are not supported today.

#### Can we install our own security tooling on team computers?

**Team Setup Scripts** is Enterprise only. Those admins can install their own
tooling on every team computer. Grok Bot does not ship a built-in
customer-facing EDR feed.

#### Why do members have to sign in to company tools again?

Sign-in sessions inside the computer can drop when the computer is recreated,
for example after an image update or when an admin recreates it. Sessions ride
your identity provider, so your session policies also apply.

#### What happens to data when an admin terminates a computer?

Computer management is Enterprise only. Organization admins and Enterprise team
admins can terminate a member's computer. The durable disk is kept, and the
member's next session starts a fresh computer on that disk. Terminating a
computer is separate from the Enterprise-only enable switch.

#### What certifications apply to Grok Bot?

Anysphere holds ISO/IEC 27001 and ISO/IEC 42001 certifications, issued by
Schellman, and Grok Bot is included in the current ISO scope. Certificates and
reports are available at [trust.cursor.com](https://trust.cursor.com).

### Related pages

* [Grok Bot security](/grok-bot/security)
* [Grok Bot for teams and enterprises](/grok-bot/teams-and-enterprises)
* [Grok Bot inference hooks](/grok-bot/inference-hooks)
* [Configure identity and access](/grok-bot/identity-and-access)
* [Connect to private networks](/grok-bot/private-networks)
* [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance)

## Approvals, security, and privacy

> 本节来源：https://docs.x.ai/grok-bot/approvals-security-and-privacy （页面标注 Last updated: October 29, 2026）

Grok Bot is designed to complete work while keeping sensitive inputs and
consequential actions under your control. Use approvals, secure handoffs, and
clear Bot boundaries together.

### Set a boundary in the request

Tell the Bot which actions it can take and where it must stop:

> Reconcile the campaign data and draft a recommended budget change. Do not
> change the campaign or message the agency. Ask for approval after showing the
> current value, proposed value, and expected impact.

Prefer explicit boundaries for:

* Sending messages or invitations
* Publishing content
* Purchases and financial transfers
* Deleting or overwriting data
* Changing permissions
* Production changes
* Accepting legal terms

An approval controls the proposed action. It does not reverse work already
completed.

### Review an action

Auto Review checks each action your Bot is about to take, for example before it
runs a command, uses a connected app, or uses its computer. Most actions run on
their own. When one needs your OK, the Bot shows an approval card in your chat
with the proposed operation and its inputs, and waits for your answer. An action
that matches one of your **Ask first** rules always gets a card. Review the
target, scope, and values before approving.

Auto Review takes into account what you asked for in your own messages. Text
from somewhere else, such as an email or a web page, doesn't count as your
request. Some cards carry a warning, such as **This can't be undone**, **This
changes sign-in or security settings**, or **This shares your data outside this
chat**.

* **Allow once:** the Bot does the action now. No rule is saved.
* **Always allow:** the Bot does the action now and saves an Allow rule to your
  Custom Rules, so similar actions run on their own. The card shows **Saved to
  Custom Rules**.
* **Deny:** the Bot doesn't do it. It won't try that action again or ask you
  about it until you send another message.

Some cards use other labels. A card for a terminal command shows **Allow** and
**Skip**, plus **Manage settings**, which opens your Auto Review settings. A
card paused by one of your **Ask first** rules shows **Allow** and **Not now**,
and **Edit rule** opens your Custom Rules. When the card has no rule to offer,
you see **Allow** instead of **Allow once**, and no **Always allow**. On the
phone, tap a card to see the full request and all of its buttons.

For email the Bot sends from [its own
address](/grok-bot/computer-and-apps#give-your-bots-an-email-address):

* When you ask for an email in chat, it goes out once Auto Review allows it. If
  Auto Review needs you, you see an approval card first.
* Email from a routine, an incoming message, or other work you didn't start
  with that request waits as a draft until you press **Send**.
* A forward, or an email with an attachment Auto Review can't fully read,
  always waits for your OK.

Do not approve an action whose target or effect you cannot identify. Ask the Bot
to explain it in plain language or produce a draft first.

#### If you don't answer

When the work started from a chat message, the card waits for an answer and
doesn't expire on a timer. When a routine, an incoming message, or other
background work raised the card, it expires after 30 minutes. If you send a new
message instead of answering, any open card in that chat closes, and changing
your Auto Review settings also closes open cards.

A closed card shows **Expired** and says the Bot didn't do the action. If the
card offered a rule, you can still press **Always allow next time**; the Bot
saves the rule and can go ahead the next time. To finish the task now, ask the
Bot to try again.

#### Shared Bots and group chats

On a [shared Bot](/grok-bot/shared-bots), each teammate answers cards for their
own requests in their own chat with the Bot. In a Slack thread, the card has
**Allow once**, **Deny**, and **View details**, and only the person who asked
can answer. In a group chat, only the person whose message the Bot is answering
can approve; everyone else sees who the card is waiting on, and group chat cards
don't offer **Always allow**.

An approval card asks whether the Bot may take an action. A [Secure
Form](/grok-bot/vault#secure-forms) collects a password, key, or other secret,
and a connect card asks you to sign in to an [app](/grok-bot/computer-and-apps#connect-an-app)
so the Bot can use it.

### Configure Auto Review

Auto Review is on by default. For each action, it either lets the action run or
has the Bot ask you first, and your Custom Rules can change that choice for the
actions you care about. Built-in safety checks always apply, whatever your rules
say.

The **Auto-review** switch is in **Settings → General**, under **Bot**; on iPhone
and Android, it's in the **Bot** group of **Settings**. With Auto Review off,
the Bot runs actions without checking them first, and your Custom Rules are
hidden and not used but kept; turn it back on to use them again.

While Auto Review is on, **Custom Rules** appears under the switch on desktop;
on the phone, tap **Custom Rules** in the **Bot** group. To add a rule:

1. Under **When Grok Bot wants to:**, describe one action in plain words, like
   “reply to emails for me.”
2. Under **It should:**, choose **Allow automatically** or **Ask first**.
3. Press **Add Rule**.

On desktop, use the edit button next to a rule, make your change, and press
**Save Rule**, or press **Cancel** to keep it as it was; use the delete button to
remove it. On the phone, tap a rule to open it, then press **Save Rule** or
**Delete Rule**.

* **Ask first** rules always stop matching actions for you.
* **Allow automatically** rules let matching actions proceed only when the
  automated review does not identify another reason to stop.
* If both kinds of rule match, **Ask first** wins.

You can have up to 20 **Allow automatically** rules and up to 20 **Ask first**
rules, and each rule can be up to 1,000 characters. If you already have 20 Allow
rules, **Always allow** on a card removes your oldest Allow rule to make room
and tells you which rule it removed.

If your admin requires Auto Review, the switch stays on and shows **Required by
your admin. You can't turn this off.** Team rules appear in the same table with
**Required by your admin. You can't edit or delete this rule.** Team rules always
apply; your own rules apply only to you, on top of the team's, and can only make
behavior stricter. Your team can also share rules that apply to your Bots
instead of your own rules; built-in safety checks still apply. See
[Auto-review rules](/grok-bot/teams-and-enterprises#auto-review-rules).

Write one short, narrow rule for each action, around a known action and scope:

* Ask first before sending any external email.
* Ask first before changing a production dashboard.
* Allow automatically when running `git status` in `/workspace/reports`.

Avoid broad rules such as “allow everything in the browser.” Websites and tool
behavior change over time. Auto Review is model-based and should complement,
not replace, least privilege and explicit approval boundaries.

Personal Auto-review rules are saved to your account, so they apply from every
desktop and the mobile app.

### Keep passwords and payment details out of the chat

Bots sign in and check out without seeing secret values. A Bot uses a login
saved in [Vault](/grok-bot/vault) first, then a connected password manager such
as 1Password, then asks you with a Secure Form. Values from Vault and Secure
Forms are filled into the page without being shown to the model.

When a form can't do the step, such as single sign-on, a passkey, a CAPTCHA, an
approval on another device, or a bank card verification, the Bot hands you the
computer:

1. Choose **Take over** on the request in the conversation, or open the computer
   and choose **Take control**.
2. Complete the sensitive step.
3. Choose **I'm done**, then tell the Bot to continue.

Do not send a password, one-time code, or API key in ordinary chat. For an API
key or another secret, enter it in the secure secret card when the Bot asks; the
value is masked, excluded from the transcript, and not shown to the model.

A card saved in Vault fills in at checkout without a separate approval each
time. If you want to approve every payment, don't save the card: leave
**Securely save to Bot's vault** unchecked when you enter it in a Secure Form,
or remove it in **Settings → Vault**.

If you sign in with a hardware security key, such as a YubiKey, the Bot's
browser can use a key plugged into your desktop while **Use hardware security
keys** is on under **Settings → General → Security Key**. The setting is on by
default on macOS and Windows and is not yet supported on Linux; every use asks
you to approve it first.

### Control access to your local computer

The shared Grok Bot computer runs in the cloud. Access to the Mac or Windows
computer in front of you is a separate capability.

In **Settings → Computer → Your computer**, choose **Ask every time**,
**Always allow**, or **Never allow** in **Execution on this computer**. Each
listed desktop has its own setting; until a desktop is listed, the page shows
**Execution on Local Computer** instead.

The default is **Ask every time**. Use **Never allow** unless a Bot has a
specific reason to work on your local files. Your team admin can cap this
setting for the whole team; when the team's policy is stricter than yours, the
team's applies. These settings do not prevent the Bot from using its cloud
computer.

Your team's cap also applies when a Bot uses apps on your phone. See
[Let a Bot use your phone's apps](/grok-bot/mobile#let-a-bot-use-your-phones-apps).

The first time a Bot asks to run a command on your computer, the conversation
shows **Allow Grok Bot and all Bots to run commands on your local computer?**
with **Always allow**, **Allow once**, **Never**, and **Deny once** (Esc).
**Always allow** and **Never** set **Execution on Local Computer** for every
Bot, and you can change the setting later in Settings. If your team's admin has
set a stricter ceiling, **Always allow** is unavailable.

### Understand the shared-computer boundary

All of your Bots share one cloud computer assigned to your user account. Files,
browser sessions, and command line credentials on that computer are available
across your Bot roster.

* Do not use separate Bots as a security boundary.
* Sign out of a service when it should no longer be available.
* Remove sensitive temporary files after the work is complete.
* Delete a connector or revoke its authorization in the source service when
  access is no longer needed.

Do not treat this user assignment as a guarantee that is broader than Cursor's
published security documentation. Review current infrastructure and encryption
controls there.

### Sharing a Bot is not a security boundary

A public share link lets others copy the Bot's configuration. It does not share
your computer or logins. Still, do not put secrets, customer data, or internal
URLs in a Bot you share. See [Share a Bot](/grok-bot/bots#share-a-bot) and the
[third-party bot terms](https://x.ai/legal/bot-sharing-terms).

A [shared Bot](/grok-bot/shared-bots) is different: teammates chat with the same
Bot, and the apps, secrets, skills, and files its owner adds work in every
teammate's chat. Only add keys and files you're happy for everyone you share it
with to use.

### Cursor account and data settings

Grok Bot uses Cursor authentication and account data settings.

* Grok Bot requires data storage and does not support Legacy Privacy Mode.
* Privacy and data-sharing choices are managed through Cursor account settings
  and, when required, the Grok Bot access flow.
* Training opt-out follows the applicable Cursor account and privacy settings.
* Review the current [Cursor Privacy Policy](https://cursor.com/privacy) and
  [security information](https://cursor.com/security) for contractual details.

Organization administrators can restrict local-computer execution and may
provide managed setup for the cloud computer. Available controls depend on the
organization's rollout and plan.

### Remove access and working data

When a project or login should no longer be available:

1. Pause or delete related routines.
2. Sign out of websites on the shared computer.
3. Uninstall connectors and revoke their authorization in the source service.
4. Remove sensitive project files from `/workspace`.
5. Hide or delete Bots that should no longer appear in Grok Bot.
6. Use the account settings flow if you need to delete the Cursor account.

Deleting a Bot does not remove shared-computer files or browser sessions.
Backend retention and account deletion follow the applicable Cursor terms.

### Use a least-privilege setup

* Connect only the tools a workflow needs.
* Use scoped service accounts where the source system supports them.
* Start with read-only tasks and draft outputs.
* Keep sending, publishing, purchasing, deletion, and production changes behind
  approval.
* Review installed connectors and active routines regularly.
* Pause a routine when its source system or expected workflow changes.
* Preserve source links and an action log for important decisions.

For information on using Grok Bot in X Chat, see [Using Grok Bot in X Chat](https://help.x.com/using-x/about-grok#grok-bot).
