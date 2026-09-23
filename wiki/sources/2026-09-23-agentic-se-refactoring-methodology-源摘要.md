---
tags: [素材, AI, Agent, 软件工程, 重构, 方法论]
created: 2026-09-23
updated: 2026-09-23
sources:
  - "raw/sources/notes/2026-09-23-agentic-se-refactoring-methodology.md"
  - "https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2606.05608 （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2603.13428v4 （检索于 2026-09-23）"
  - "https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2602.00180 （检索于 2026-09-23）"
  - "https://pluralistic.net/2026/01/06/1000x-liability/ （检索于 2026-09-23）"
  - "https://kenhuangus.substack.com/p/disposable-code-durable-side-effects （检索于 2026-09-23）"
  - "https://sourcegraph.com/blog/the-death-of-the-junior-developer （检索于 2026-09-23）"
  - "https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html （检索于 2026-09-23）"
  - "https://martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html （检索于 2026-09-23）"
  - "https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html （检索于 2026-09-23）"
  - "https://martinfowler.com/articles/exploring-gen-ai.html （检索于 2026-09-23）"
---

# AI Agentic SE 时代的系统重构——用户调研稿源摘要

## 来源定位

用户提供的多源调研稿（原位于用户本机 cowork-space 工作区，标注调研日期 2026-09-23），侧重范式层思想与架构、
重构方法论。它是**二次综合产物，不是一级来源**：约 30 条参考文献，混合了预印本、厂商博客、个人 Substack、
二手转录与官方文档。入库时已抽查 7 条关键引用并发现 4 处问题（记在 raw 文件头部）；本页记录 2026-09-23 对全文
**逐项回查一级来源**的结果：10 组核验、每组对非"成立"判定再做一次反方复查，关键数字由维护者本人抽查原文。

判断与跨源综合见 [[Agentic SE 时代的系统重构]]。本页只记核验。

## 结构性校正（影响调研稿的主线）

1. **§0 的思想光谱把人放错了位置。**
   - Karpathy 被放在"意图 / prompt 成为一等公民、代码降格为可再生中间产物"一端。但同一场演讲里他反复讲的是
     审慎工程："keep the AI on the leash"，人类验证者是瓶颈，要小步增量，"this is the decade of agents"而不是
     "the year of agents"。更准确的定位是**范式判断激进、工程实践审慎**：他的 generate–verify 论述是 §1.5
     "验证是瓶颈"的证据，不是对立面。
   - Böckeler 被写成"系统性泼冷水"的一方。原文立场更窄：spec-first "在很多场景下有价值"，保留意见针对的是
     重流程工具与 spec-anchored / spec-as-source；她的审查主张是**按风险校准**（影响、概率、可检测性），低风险、
     高可检测性时她接受 vibe coding。
   - Yegge 那篇是 2024-06 的 Sourcegraph 公司博客，不属于"2025–2026 年思想光谱"，也没有主张代码可抛弃。
2. **§5.1"激进主张被自己的基准证伪"不成立。** EvoClaw 不是 AaaS 论文自建的，AaaS 论文援引了它并主动承认局限；
   准确说法是"激进主张在长期演化场景缺乏数据支撑"。
3. **§1.5 把"TDD inside the agent loop"列为路线终点，与来源相反。** Böckeler 2026-08-10 的小样本评估没看到 TDD
   带来收益，她已停止要求 agent 做 TDD，改用变异测试监控回归测试质量。"验证优先"应理解为约束结果，不是规定过程。

## 逐项核验

### §1.1 Software 3.0（Karpathy）

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| 2025 年 YC AI Startup School 演讲 *Software Is Changing (Again)* | **成立** | 2025-06-17，旧金山。调研稿引的 ikyle.me 是二手摘要，应改引 YC Startup Library 官方页（附全文转录）或 Karpathy 2025-06-19 推文里的章节纲要 |
| 1.0 代码 / 2.0 权重 / 3.0 prompt 为程序 | **基本成立** | 原话是"LLM 是一种新计算机"，"运行时"是转述；他强调三种范式**并存**、都要熟练，不是代际取代 |
| "最热门的新编程语言是英语" | **基本成立** | 出自 Karpathy 2023-01-24 的推文，演讲中是回顾，不是首提 |
| LLM 兼具公用事业、晶圆厂、操作系统属性；类似 1960 年代分时主机 | **成立** | 他认为操作系统类比最贴切 |
| "people spirits"、幻觉与缺乏自知 | **成立** | 原文另列了锯齿状智能、顺行性遗忘、易受 prompt injection |
| Iron Man 战衣式增强而非全自主；autonomy slider；generate–verify 循环 | **基本成立** | 丢了时间限定：是"现阶段"应做部分自主产品，并在约十年里把滑杆推向自主端；他没有否定全自主方向 |
| Build for agents：第三类信息消费者，需要 llms.txt 等专属通道 | **基本成立** | 语气偏强：原话是与 LLM"相向而行"，值得做而非必须；llms.txt 由 Jeremy Howard 2024-09 提出，不是 Karpathy 首创 |

### §1.2 AaaS 论文与 EvoClaw

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| arXiv 2606.05608 是"激进重构派"代表 | **基本成立** | 单作者预印本、无自有实验。v1（2026-06-04）题为 *The End of Software Engineering*；v2（2026-06-10）改题 *Agentic Software*，改口为"扩展而非终结"软件工程。"激进"主要适用于 v1，引用须注明版本 |
| S=(算力,静态规则,执行环境) vs A=(LLM,工具,记忆,规划) | **成立** | — |
| Software 3.0 = Agent-as-a-Service（按结果计费） | **基本成立** | 论文按**交付形态**分代（本地授权 → SaaS → AaaS），与 Karpathy 的 Software 3.0 不是同一概念；按结果计费在正文只是待研究方向 |
| 否定"AI 辅助开发"的中间形态 | **部分成立** | 论文批判该范式，但其四阶段路线图明确包含中间阶段，并建议当下采用 human-in-the-loop |
| 从业者转型为 intent architect | **成立** | 原文是三重角色：intent architect、agent coordinator、outcome auditor——人没有退出验证环 |
| EvoClaw 是 AaaS 论文的"自建基准" | **归属错误** | 实为 Deng 等（14 位作者）arXiv 2603.13428，2026-03-13 首发，v3 起更名 SWE-Milestone，arXiv 注明 ICML 2026 |
| 孤立任务成功率 >80%，持续演化 ≤38% | **失准** | 指标是综合 Score（新功能 Recall 与防回归 Precision 的调和），**不是成功率**。持续演化最佳 38.03%（Claude Opus 4.6）；按完全解决计最高 13.37%（Gemini 3 Pro）——证据比调研稿写的更强 |
| 失败原因：上下文漂移、错误传播、无法建模技术债 | **部分成立** | 原文机制是回归无法阻止、错误沿依赖链滚雪球（Recall 近线性增长而 Precision 饱和）。"上下文漂移"是 AaaS 论文的附会；SWE-Milestone 观察到 Claude Code + Opus 4.6 的上下文用量稳定可控 |
| 激进主张"被自己的基准证伪" | **不成立** | 改为：AaaS 援引的第三方基准显示持续演化场景表现很差，论文承认差距但断言"非根本性、数年内可解"，该断言缺乏数据支撑 |
| AaaS 一方主张 agent→result 直达、人可退出验证环 | **部分成立** | 只适用于其 2028 年以后的第四阶段愿景；当前流程中人仍审计结果 |

### §1.3 SDD

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| Spec Kit：constitution → specify/plan/tasks | **基本成立** | 现版本：constitution 每项目一次；每个 feature 走 specify → plan → tasks → implement（另有 converge 与可选质量门） |
| Kiro：Requirements → Design → Tasks | **成立** | 现另有 Bugfix Specs、Design-First 变体与不设审批门的 Quick Spec |
| Tessl 追求 spec-as-source，代码标注 "GENERATED FROM SPEC - DO NOT EDIT" | **基本成立** | 是 Böckeler 2025-09 试用 Tessl Framework（私测）时所见；"spec 是新的源代码"是转述。Tessl 2026-09 首页已转型为 agent enablement 平台，须加时间限定 |
| Böckeler 区分 spec-first / spec-anchored / spec-as-source | **成立** | 2025-10-15 首提。**连带发现**：本 wiki [[Specification-Driven Development]] 原把三层级归于 arXiv 2602.00180，属归属错误，已更正 |
| 单一重流程不适配问题尺度；"宁愿 review 代码也不愿 review markdown" | **成立** | 基于 2025-09 版本工具，两款工具此后增加了按规模区分的流程 |
| agent 经常无视或过度解读 spec | **基本成立** | 原文是"常不遵循全部指令"和"过度热切地执行某条 constitution 条款"，并质疑"虚假的控制感" |
| 与 2000 年代 MDD 失败历史平行 | **基本成立** | 原文没写"2000 年代"；类比主要针对 spec-as-source |
| SDD 叠加"僵化 + 非确定性"两种缺陷 | **失准** | 原文是**担忧**而非结论，对象是 spec-as-source 乃至 spec-anchored，不含 spec-first |
| "spec 是新源代码"的正方是 Tessl / Spec Kit / Kiro | **部分成立** | 正方实际只有 2025 年的 Tessl；Kiro 基本是 spec-first；Spec Kit 文档声明三种持久化模型都不是默认 |

### §1.4–1.5 代码的地位与验证瓶颈（前半）

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| Doctorow：代码是负债；AI 能写代码不能做软件工程；10,000 倍代码 = 同规模负债；"往墙里铲石棉" | **成立** | 2026-01-06。倍数以正文 10,000 为准（URL 写 1000x），属修辞而非测量 |
| Doctorow：多 agent 链条可靠性乘法衰减 | **基本成立** | 针对的是微软式个人助理 agent（订票、订酒店），是独立性假设下的算术示意，不是编码流水线的实测 |
| Ken Huang：代码可抛弃，副作用持久 | **基本成立** | 2026-06-17。语境是员工绕过流水线临时生成的影子 IT 应用，不是反驳"代码可由 spec 再生"；该文推介合著方公司的产品，有利益关联 |
| Yegge 预测 LLM 对话成为"源代码的常态"，属可抛弃派 | **失准** | 原预测（2024-06）是源代码将"由 LLM 通过 prompt 编写和修改"——说的是代码怎么生产，不是对话取代代码；文中也未主张代码可抛弃 |
| CHOP 出自该文；chat 对资深者更安全 | **成立** | 依据是作者个人经历，不是系统数据 |
| Böckeler：LLM 不是编译器而是推断器 | **成立** | 《I still care about the code》，2025-07-09 |
| 影响 × 概率 × 可检测性的风险评估 | **基本成立** | 三因素"组合"判断，原文无乘法公式；用来**校准**审查力度 |
| "今晚 on-call 的你，敢部署没读过的 1000 行变更吗" | **失准** | 拼接了两篇：原问是"负责 on-call 时，什么情况下能接受部署 1,000 或 5,000 行变更"；"今晚 on-call"出自 2025-09-23《To vibe or not to vibe》；"没读过"为调研稿所加。不能当直接引语 |
| Exploring Gen AI 路线：技能不降反升 → 全自主只适合小任务 → context / harness engineering、TDD inside the agent loop | **部分成立** | 系列是 Thoughtworks 多位作者合写。TDD inside the agent loop 在系列中是**被质疑**的做法（见结构性校正第 3 条）；"不降反升""可验证"是调研稿自加 |

### §1.5 验证瓶颈与 agent-native（后半）

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| "review is the bottleneck"是共识（引 Osmani《Code Review in the Age of AI》） | **基本成立** | Osmani（2026-01-05）主张瓶颈从"写代码"移到"证明代码能用"；原文无此句，对策是让作者在 PR 里附可运行证据（PR Contract），而不是加大 review。称"共识"偏强 |
| Osmani《Vibe Coding: Revolution or Reckless Abandon?》支持同一论点 | **部分成立** | 2025-04-03 的这篇论证的是 review 与验证不可省，没有提出"review 是瓶颈" |
| "多数开发者不信任 AI 代码但也不检查它"（引 The Register 2026-01-09） | **失准** | 底层是 Sonar 2026 State of Code 调查（2025-10 在线问卷，n=1,149，自报，厂商主导）：96% 不"完全"信任 AI 代码功能正确；48% 完全同意"提交前总是检查"，另 27% 部分同意。应表述为"普遍不完全信任，但坚持每次都检查的不到一半"。The Register 放大了两点 |
| Every / Shipper 的 agent-native 三原则：Parity / Granularity / Improvement over time | **失准** | 指南（Dan Shipper 与 Claude 合著，2026-01-09，规范 URL `every.to/guides/agent-native`）列的是**五条**：Parity、Granularity、Composability、Emergent capability、Improvement over time。多处标注为 Claude 贡献、Dan 尚未背书 |
| 检验标准：agent 能否完成你从未显式构建的功能 | **基本成立** | 对应被漏掉的 Emergent capability；原文限定"在应用领域之内" |

### §2 架构方法论：代码库成为 agent 的环境

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| 多个独立来源（Maintainable Software、Marmelab、Deska、Anthropic）2026 年收敛：代码库比堆 MCP / 子 agent 更根本 | **部分成立** | 只有 Marmelab（2026-01-21）接近原话。Salomon 的主要依据就是 OpenAI 与 Anthropic 的两篇，"多来源收敛"大半是**同一两份原文的转述链**；Anthropic 反而推荐子 agent 架构；Deska 是厂商营销文 |
| Salomon 的判据："让一个不熟悉的 agent 找到正确上下文、做窄变更并验证，而无需把整个系统装入工作记忆" | **基本成立** | 引文逐字对应。出处补正：Jan-Gerke Salomon，《How to Design a Maintainable Codebase for AI Coding Agents》，2026-04-05（"Agentic Codebase Principles"只是 URL slug） |
| Salomon 的七特征 | **失准** | 原文定义**五项**特征：Locality、Blast radius、Boundary integrity、Navigability、Rebuild/test scope；Cohesive modules、Ownership-aligned boundaries 属于另列的设计手段 |
| 小而内聚的文件；扁平、语义化目录；避免缩写重名（"代码 SEO"） | **基本成立** | "代码 SEO"出自 Marmelab。"扁平"只见于 Deska；Salomon 明确主张"领域顶层 + 用例切片"两级结构，优于纯扁平。应改为"浅而可预测、按领域命名" |
| Anthropic：context rot、n² 注意力、JIT 检索优于预加载、compaction、NOTES.md、子 agent 压缩回传 | **基本成立** | 该文发表于 **2025-09-29**，不是 2026 年；原文推荐**混合**策略（预载 CLAUDE.md + glob/grep 按需检索），并说明运行时探索更慢 |
| 强类型让 API 自文档化；消除全局状态、时序与语义耦合；抵制过早抽象 | **成立** | 主要出处是 Salomon（列六类有害耦合），Deska 为单一厂商来源 |
| ARCHITECTURE.md 点名设计模式可激活预训练知识 | **基本成立** | 只出自 Deska 厂商博客，未见实证；ARCHITECTURE.md 本身是 matklad 2021 年为人类贡献者提出的惯例，同样强调"保持简短" |
| Anthropic：CLAUDE.md 只写"删掉会出错"的内容 | **成立** | 限制的是每次会话都载入的文件；按场景需要的知识建议放进按需加载的 skills |
| 文档粒度之争：Anthropic、Marmelab 主张极简 vs 另一派主张详尽 .ai-context | **部分成立** | Marmelab 实为"短入口文件 + 大量就近嵌入的文档"；".ai-context"只是 Deska 的可选建议，谈不上一派。各方实际收敛于**常驻入口极简 + 深层文档按需加载**（OpenAI、Anthropic、Marmelab 同向），分歧只在哪些内容常驻上下文 |

<!-- 待补：§2.3 AGENTS.md / ACI / vibe architecting（G8）、Anthropic 专项（G7）、§3 遗留系统（G9）、四篇文章存档抽查（G10） -->

## 调研稿未引、但会改变结论的一级来源

- Böckeler，《TDD inside the agent loop - theater or actual value?》，2026-08-10：5 批方案、Sonnet 4.6 生成、Opus 4.8
  盲评，TDD 组整体略差、变异得分无差异；作者停止要求 agent 做 TDD，改用变异测试与 Approved Scenarios。
- Deng 等，SWE-Milestone（arXiv 2603.13428v4）：失败集中在防回归而非新功能；有纪律的测试验证得分最高，
  "高频改同一文件却很少跑测试"最差——这是"验证优先"最直接的一级证据。
- Karpathy 演讲中的 MenuGen 一段："the code was actually the easy part"——demo 几小时跑通，认证、支付、部署
  这些非代码的集成花了一周。
- Böckeler，《Harness Engineering - first thoughts》，2026-02-17：指出 OpenAI 的文章缺少"功能与行为的验证"，
  并提醒 OpenAI 有利益关联。
- Thoughtworks，《The Economic Benefit of Refactoring》，2026-07-30：已同批摄入，见
  [[2026-07-30-Thoughtworks-重构的经济收益-源摘要]]。

## 关联页面

- [[Agentic SE 时代的系统重构]]
- [[Harness Engineering]]、[[Agent 不会自发偿还结构债]]
- [[Specification-Driven Development]]、[[SDD 收益主张的实证赤字]]
- [[AI编码技术债的三层治理]]、[[生产力-体验悖论]]
- [[AI方法论的去机制化失真]]
