---
tags: [实体, 公司, AI, 投资标的]
created: 2026-07-03
updated: 2026-11-06
sources:
  - "https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ （检索于 2026-07-03）"
  - "https://www.reuters.com/business/zuckerberg-says-ai-agent-development-going-slower-than-expected-2026-07-02/ （Reuters 独家原文；检索于 2026-07-03，直连返回 401，事实经 TechCrunch 转载核验）"
  - "https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ （检索于 2026-11-06）"
  - "https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse （检索于 2026-11-06）"
  - "https://www.meta.com/help/subscriptions/1021145227643680/ （检索于 2026-11-06）"
  - "https://www.fool.com/earnings/call-transcripts/2026/10/21/meta-meta-q3-2026-earnings-call-transcript/ （检索于 2026-11-06）"
  - "https://siliconangle.com/2026/09/21/amazon-blocks-metas-muse-agent-from-shopping-on-users-behalf/ （检索于 2026-11-06）"
  - "https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/09/22/meta-testing-a-human-concierge-for-its-new-personal-ai-agent-muse-reuters-exclusive/ （Reuters 独家转载；检索于 2026-11-06）"
  - "https://www.techrepublic.com/article/news-meta-ai-facebook-marketplace-buyer-seller-address/ （检索于 2026-11-06）"
  - "https://time.com/article/2026/10/06/meta-muse-ai-agent-privacy/ （检索于 2026-11-06）"
  - "https://thenextweb.com/news/meta-muse-sharing-back-on-dns-leak （检索于 2026-11-06）"
  - "https://9to5mac.com/2026/09/30/report-metas-muse-crosses-5-million-downloads-amid-massive-advertising-push/ （检索于 2026-11-06）"
---

# Meta

Facebook、Instagram、WhatsApp 的母公司，也是 AI 基础设施与 agent 产品的重要投入方。本 wiki 关注它的两重角色：一是 **agent 生产级落地节奏**的信号来源，二是**消费级常驻 agent**（Muse）的主要玩家。

## 2026-09：Muse 个人 agent 上线
- **产品**：2026-09-08 在美国上线（加拿大约 09-18、新加坡 10-27 跟进），包括独立 App、muse.ai、WhatsApp 和 Mac 客户端；内部代号 Hatch，据 The Information，产品以开源的 OpenClaw 为蓝本。底层模型是闭源的 Muse Spark 系列（2026-04 起），付费档用 Muse Wonder（10-12 发布）。
- **架构**：每个用户一台专属云端 VM。另有一个在系统层隔离的 Sentinel agent，是唯一的权限裁决者，Muse 只拿得到替身 token。架构细节是厂商自述，未经独立审计。
- **商业模式**：免费，靠交易抽成（"we get paid a fee based on the transactions that we help facilitate"），付费档 Power $20、Maximum $100，按每周 token 计。官方承诺对话和 VM 数据不进入广告系统，但用户可以自愿把 Muse 接入 Meta 的内容与广告个性化；训练用途默认开启。
- **采用**（Q3 电话会，厂商自述）：6 周内美加超过 1,000 万人完成设置，约 25% 每天使用；超过四分之一的用户用它购物，平均客单价超过 $200。口径是"设置"数，不是月活；9 月中下旬 Muse 最多占 Meta 自家广告位当日曝光的 50%（Sensor Tower）。
- **事故**：
  - Amazon 以"不自报 agent 身份、能查看订单历史"为由屏蔽（09-20）；
  - 内部测试的 human concierge 由外包人员代接电话且未披露，后回滚（Reuters，09-22）；
  - 用户选了 "Allow Always" 后，Muse 在 Facebook Marketplace 接受低价，并把卖家住址发给买家（09 月底起多家媒体报道）；
  - TIME 报道它约每小时更新用户及其联系人（包括非用户）的档案（10-06）；
  - 6,800 多个分享页可经被动 DNS 查到（10-20 暂停，10-22 修复）。
- 综合：07-02 扎克伯格说 agent 进展"没有按预期加速"，两个月后 Muse 带着大众级的分发上线。采用曲线证明了需求，但上面的事故谱系都出在授权语义和数据边界上，没有一起是能力问题。这与 [[agent-生产级落地的鸿沟]] 的判断一致：落地卡在治理，不在能力。格局与定位见 [[常驻 AI 同事的竞争格局]]，授权分析见 [[Agent 授权三层]]，算力约束见 [[常驻 Agent 的算力经济学]]。

## 2026-07：Zuckerberg 对 agent 进展降温
- 2026-07-02，Mark Zuckerberg 在内部全员会上表示，过去约四个月 AI agent 进展"没有按预期加速"，预计还需 3-6 个月才会看到更显著回报。
- 同期 Meta 仍计划高强度投入 AI 基础设施，相关资本开支信号高达 1450 亿美元量级。
- 综合：这不是看空 agent 长期方向，而是一个来自大厂 CEO 的节奏信号：从 Demo 到生产级落地仍受工程、组织和可靠性约束。

## 与 wiki 的关联
- [[agent-生产级落地的鸿沟]] 已把这条信号作为首个证据点。
- 与 [[codex-agent-采用曲线]] 形成对照：采用数据证明需求与使用强度，Meta 信号提醒兑现节奏不能线性外推。

## 相关页面
- [[常驻 AI 同事的竞争格局]]
- [[agent-生产级落地的鸿沟]]
- [[building-effective-agents]]
- [[Codex]]
