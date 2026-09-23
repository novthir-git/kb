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
  - "https://addyo.substack.com/p/code-review-in-the-age-of-ai （检索于 2026-09-23）"
  - "https://www.sonarsource.com/state-of-code-developer-survey-report.pdf （检索于 2026-09-23）"
  - "https://every.to/guides/agent-native （检索于 2026-09-23）"
  - "https://maintainable.software/agentic-engineering-part-2-agentic-codebase-principles/ （检索于 2026-09-23）"
  - "https://marmelab.com/blog/2026/01/21/agent-experience.html （检索于 2026-09-23）"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents （检索于 2026-09-23）"
  - "https://code.claude.com/docs/en/best-practices （检索于 2026-09-23）"
  - "https://code.claude.com/docs/en/changelog （检索于 2026-09-23）"
  - "https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic （检索于 2026-09-23）"
  - "https://agents.md （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2601.20404 （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2602.11988v2 （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2602.14690 （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2405.15793 （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2604.04990 （检索于 2026-09-23）"
  - "https://www.isaqb.org/blog/ai-agents-dont-modernize-legacy-code-on-their-own/ （检索于 2026-09-23）"
  - "https://arxiv.org/abs/2504.09691 （检索于 2026-09-23）"
  - "https://addyo.substack.com/p/brownfield-agentic-engineering （检索于 2026-09-23）"
  - "https://github.com/feststelltaste/awesome-agentic-software-modernization （检索于 2026-09-23）"
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

### Anthropic 来源专项（§2.1、§2.4、§3.2、§3.3）

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| Anthropic 属于"代码库比 MCP / 子 agent 更根本"的收敛方 | **部分成立** | 一手材料支持"目录层级、命名影响 agent 检索效率"与"工具集宜精简"，但**推荐**子 agent 架构；相关文章发表于 2025-09，不宜计入"2026 年收敛" |
| context rot、n² 注意力约束 | **成立** | context rot 一词引自 Chroma 的研究；强调性能逐渐下降，不是到某长度突然失效 |
| just-in-time 检索优于预加载 | **基本成立** | 原文是 JIT **补充**预检索，承认运行时探索更慢，多数场景推荐混合 |
| compaction、NOTES.md、子 agent 压缩回传 | **成立** | 各有适用场景；子 agent 回传摘要通常 1,000–2,000 token |
| 可运行验证是"看守式会话"与"可离开会话"的分水岭 | **成立** | 出自 Claude Code 最佳实践（活文档，无发布日期，检索于 2026-09-23） |
| 验证可升级为 Stop hook 门禁、对抗性 review subagent、Writer/Reviewer 双会话 | **基本成立** | 官方阶梯是：自检 → `/goal` 独立评估 → Stop hook 确定性门禁（**连续拦截 8 次后强制结束本轮**）→ 第二意见。官方另有告诫："被要求找缺口的 reviewer 通常总能报出一些"，追逐每条发现会导致过度工程，应只标记影响正确性或需求的缺口 |
| Claude Code 有 `/batch` | **成立** | v2.1.63（2026-02-28）起的 bundled skill：调研 → 拆成 5–30 个独立单元 → 人批准计划 → 每单元在独立 worktree 由后台 subagent 实现、跑测试、各开 PR |
| 先在 2–3 个文件上调 prompt 再全量 fan-out；ratchet 式渐进收紧 | **基本成立** | 2–3 文件试跑是官方给自写 `claude -p` 循环的步骤，`/batch` 走自己的流程；"ratchet 式收紧"不出自 Anthropic，出处待查 |
| 2026 趋势报告：工程师 60% 的工作用 AI，能完全委派的仅 0–20% | **失准** | 一手来源是 Anthropic Societal Impacts 2025-12-02《How AI is transforming work at Anthropic》：2025-08 对 **132 名内部**工程师与研究员的非匿名自报调查，约 59% 的工作使用 Claude，其中**超过一半的受访者**表示能完全委派的只占 0–20%。趋势报告转引时泛化成 "developers" 并丢了"超过一半"的限定 |
| 角色转向 agent 编排者；新技能是系统架构、质量评估、问题分解 | **成立** | 厂商报告对 2026 年的趋势预测，不是实测；原文另列 agent coordination |
| 0–20% 与 EvoClaw ≤38% "互相印证"：全自动重构目前不成立 | **部分成立** | 方向一致但口径不同（主观可委派比例 vs 基准综合得分），不是直接互证；外推到"重构"属综合推断 |
| "AI 提供速度，护栏保证正确" | **基本成立** | "验证优先"对 Anthropic 成立，但这句话不出自 Anthropic |

**连带发现**：Claude Code 自 v2.1.277（2026-09-18）起在项目没有 `CLAUDE.md` 时读取 `AGENTS.md`，调研稿"CLAUDE.md 是厂商变体"的说法需要更新（已同步到 [[AI编码技术债的三层治理]]）。

### §2.3–2.5 AGENTS.md、ACI 与 vibe architecting

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| AGENTS.md 已成跨工具事实标准（OpenAI / Google / Cursor 采用） | **基本成立** | OpenAI 2025-08 推出，2025-12-09 捐给 Linux 基金会旗下 Agentic AI Foundation 托管；Codex、Jules、Cursor、Copilot 等原生支持。但 Galster 等（arXiv 2602.14690）对 2,853 个使用 AI 编码工具的仓库的调查显示，在其中有上下文文件的 2,586 个里，`CLAUDE.md` 仍更普遍（45.9% 对 39.5%） |
| CLAUDE.md / .cursorrules 是厂商变体 | **部分成立** | 二者早于 AGENTS.md；`.cursorrules` 已弃用。Claude Code 自 2026-09-18 起在无 `CLAUDE.md` 时读取 AGENTS.md |
| 实践已形成"仓库级 → 目录级 → skills 按需加载"分层 | **部分成立** | 是厂商推荐模式，不是普遍实践：同一样本中上下文文件常是唯一的配置机制，定义了 skills 的仓库仅 158 个 |
| 分层"已有实证研究（arXiv 2601.20404）" | **不成立** | 该文（Lulla 等，5 页短文）只研究根目录单个 AGENTS.md 对 Codex 效率的影响（10 仓库、124 PR：中位运行时间 −28.64%、输出 token −16.58%，未测正确性），不涉及分层或 skills |
| asdlc.io 页面是"AGENTS.md 规范" | **归属错误** | 官方规范是 agents.md；asdlc.io 是第三方实践者解读，部分内容已过时 |
| ACI 源自 SWE-agent（NeurIPS 2024），为 agent 设计工具是 UX 学科 | **基本成立** | 术语出自 SWE-agent；"UX 学科"是后来实践者的概括 |
| ACI 要求：错误信息可操作、输出省 token、操作幂等 | **部分成立** | SWE-agent 原则是四条：动作简单、动作紧凑、反馈充分而简洁、护栏阻断错误传播。"可操作错误信息 / 省 token"出自 Anthropic《Writing effective tools for AI agents》（2025-09）；"幂等"是更后来的实践者补充 |
| agentpatterns.ai 作为出处 | **基本成立** | 数字须回原文：ACI 相对 shell 基线提升 10.7 个百分点，绝对 pass@1 为 12.5%，不是"提升 12.5%" |
| arXiv 2604.04990 提出 vibe architecting | **成立** | position paper，仅 arXiv 预印本、未经同行评审 |
| 仅改 prompt 使代码量增长 5.9 倍（141→827 行） | **基本成立** | 三个 prompt 各跑一次、单一工具与模型，作者明言是"示意而非实验证明"；增量来自 prompt 新增的功能要求；依赖图与故障模式的改变是定性判断 |
| prompt 规范本身是架构制品，应纳入架构评审 | **成立** | — |
| 治理重心从"审代码"转向"审 prompt / 审架构决策" | **部分成立** | 原文主张在代码评审**之外新增**一层治理，不是替代；"重心转移"是调研稿推断 |
| 文档变为 agent 的 API：ADR、自文档化 CLI、Makefile 统一入口 | **基本成立** | 出自 Marmelab、Deska 等实践者博客；"文档即 agent 的 API"是综合概括 |

**调研稿未引、与本节结论直接相关的对照实证**：Gloaguen 等（ETH，arXiv 2602.11988v2）发现上下文文件总体不提升成功率、
成本增加 20% 以上，仓库概览无益，指令本身会被遵循——与 2601.20404 的效率结论矛盾，已在
[[AI编码技术债的三层治理]] 显式标注。

### §3 遗留系统重构

| 调研稿论断 | 核验 | 校正后的口径 |
|---|---|---|
| iSAQB（Harrer）的核心论点 | **基本成立** | 是 iSAQB 博客 2026-05-18 发布的 Markus Harrer（INNOQ）**个人访谈**，观点应记在 Harrer 名下，不是 iSAQB 机构立场 |
| 企业代码充满 agent 无法获取的隐性领域知识，agent 不会自己完成现代化 | **成立** | — |
| Harrer 提出"认知债 / 意图债"警告 | **归属错误** | 概念出自 Margaret-Anne Storey（ACM Queue 24(2), 2026）；Harrer 引用 Storey 并把它用到现代化场景 |
| "modern legacy"陷阱 | **成立** | Harrer 自创的说法 |
| characterization tests 先行铺网 | **成立** | 另有独立佐证：Osmani《Brownfield Agentic Engineering》（2026-09-14） |
| seam 限定干预点、给 agent 沙箱化的爆炸半径；与 strangler fig 结合 | **部分成立** | seam 出自 Harrer；strangler fig 是 AWS 方案的总体框架；"agent 加速新旧并行期封套"是调研稿推断 |
| Thoughtworks CodeConcise：LLM + 图谱逆向工程、提取业务规则再重写 | **基本成立** | 内部加速器、仅供顾问使用；业务规则由领域专家校验；重写由团队完成；提效数字是 PoC 估算 |
| Google（FSE 2025）：定位 → LLM 生成 → 验证三阶段 | **基本成立** | 实际流水线：Kythe 定位 → 按置信度分类 → LLM 改码 → 多级自动校验 → 开发者目视核查 → 代码所有者审批。发表于 FSE 2025 Companion |
| 12 个月 39 次迁移、93,574 处编辑 | **失准** | 3 名开发者 12 个月完成 39 次**同类**（32→64 位 ID）迁移，提交 595 个变更；93,574 是字符级 Levenshtein 编辑距离，不是"处" |
| LLM 生成占约 70–74% | **基本成立** | 按变更计 74.45%，按字符编辑量计 69.46%；无人改动的纯 LLM 变更只占 35.97% |
| 省约 50% 时间 | **失准** | 是 3 位开发者（也是系统作者）的主观估计，论文明言没有实测工时 |
| 人工审查从未退出 | **基本成立** | 原文无此说法，但每个变更都要开发者核查与代码所有者审批，是流程的固定环节 |
| AWS Transform 主机现代化是 agentic + 人在环 | **成立** | 厂商博客（2025-12-15），只针对 reimagine 一种路径 |
| §3.2 方法框架是"多来源共识" | **部分成立** | 调研稿引的 awesome-agentic-software-modernization 清单由 Harrer 本人维护（GitHub 用户名 feststelltaste），characterization tests 与 seam 两条实质上出自一人。独立佐证是 Google、AWS、Thoughtworks 与 Osmani |
| "AI 提供速度，护栏保证正确"（§2.4，调研稿作多来源收敛） | **归属错误** | Harrer 访谈原话："Agents provide speed, guardrails provide accuracy" |
| AaaS 主张人退出验证环 | **失准** | AaaS 省掉的是"人写的静态软件"这一层，人仍作为 outcome auditor 审结果 |

调研稿漏掉的 Harrer 方法：**确定性与非确定性混合**——"guided AI"只让 LLM 改分析脚本事先确定性圈定的位置，或由 AI
生成代码转换 recipe 再由确定性工具执行；以及**先缩小现代化范围**（"The less you do, the more of it you can do"）。

### 四篇同批文章存档的抽查

对另外四份 raw 摘录抽查 23 个关键事实：19 条成立、4 条基本成立，无失准。已据此在对应源摘要页修正或补注：
OpenAI 原文只说扩员后"吞吐在上升"，未明说人均；Böckeler sensors 文是 2026-05-19 起连载、05-27 完结；
"圈复杂度"一条的"唯一"修饰的是 agent 频繁上调阈值的类别；Thoughtworks 原文导言（约 12 万行 Rust）与结果表
（约 5 万行）口径不一。OpenAI 原站对直连与 WebFetch 均返回 403，本次经 Wayback 快照核对英文原文。

### 未核验

§4 表中"模块化单体 vs 微服务"一行调研稿未给出处，本次未核验，不采信。

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
