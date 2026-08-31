---
tags: [分析, AI, Agent, 知识管理]
created: 2026-07-29
updated: 2026-08-31
sources:
  - "https://github.com/stanford-oval/storm （检索于 2026-07-29）"
  - "https://cdn.openai.com/API/docs/deep_research_blog.pdf （OpenAI Deep Research 官方公告 PDF，检索于 2026-08-11）"
  - "https://winbuzzer.com/2026/02/11/chatgpt-deep-research-gpt-52-upgrade-xcxwbn/ （Deep Research 换 GPT-5.2 及 MCP/可信站点/实时进度升级报道，公告日 2026-02-10，检索于 2026-08-11）"
  - "https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/ （Google Deep Research / Max 官方公告，检索于 2026-08-11）"
  - "https://gigazine.net/gsc_news/en/20260422-google-deep-research-max/ （Max 基准数字报道，检索于 2026-08-11）"
  - "https://arxiv.org/abs/2402.14207 Shao et al., NAACL 2024, pp.6252-6278（检索于 2026-07-29）"
  - "https://arxiv.org/abs/2408.15232 Jiang et al., EMNLP 2024, pp.9917-9955（检索于 2026-07-29）"
  - "https://github.com/stanford-oval/storm/releases （检索于 2026-07-29）"
  - "https://zhuanlan.zhihu.com/p/2051623683756766563 （检索于 2026-07-29；本机不可达，摘录存档已按质量要求移除，见下方失真小节）"
---

# STORM 知识策展系统分析

Stanford OVAL（Monica Lam 组）的 LLM 知识策展系统。**它真正的贡献不是写文章，
而是把"如何自动提出好问题"变成了可执行的工程结构。**

> 综合：这是 2024 年最好的自动化研究报告开源实现，但已停止演进——
> 最后一次 commit 停在 2025-09-30。30.4k star 是历史存量，不是活跃度。

## 两代系统解决两个不同的问题

| | 解决的问题 | 核心机制 |
|---|---|---|
| **STORM**（NAACL 2024） | 我知道要研究什么主题，但**不知道该问哪些问题** | 检索驱动的多视角提问 + 模拟对话 |
| **Co-STORM**（EMNLP 2024） | 我**连自己该研究什么都不知道**（unknown unknowns） | 多 agent 圆桌 + 人类旁听插话 + 动态心智图 |

综合：Co-STORM 的问题定义更有价值：LLM 聊天机器人和生成式搜索都要求你**先会提问**，
而人在陌生领域最大的障碍恰恰是提不出问题。论文的类比是小孩通过旁听大人对话学习。
这个需求到 2026 年仍未被商业产品很好覆盖（见下文"还剩什么价值"）。

## 四个可复用的技术机制

### 1. 用结构制造多样性，而不是用指令请求多样性

**perspective-guided question asking** 是全项目最值得单独拆用的一条原则。

它不是在 prompt 里写"请提出多样化的问题"——那样得到的问题总是又浅又同质。做法是
**先检索同主题的既有文章，从中反推该主题特有的编辑视角**（persona），再让每个 persona 独立提问。
所以研究"半导体制程"和"宋代科举"得到的视角结构完全不同。

工程上体现为 `persona_generator.py` 独立成模块，`knowledge_curation.py` 里并存两个 dspy Signature：
`AskQuestion`（无 persona）与 `AskQuestionWithPersona`（有 persona）。多 persona 走
`ThreadPoolExecutor`，`max_workers = min(max_thread_num, len(considered_personas))`。

> 综合：**多样性由架构保证，不是由措辞祈求。** 这条原则脱离 STORM 也成立，
> 已移植进 [[STORM-研究提示词组]] 的阶段 0。

### 2. 把检索从一次性变成对话式

`ConvSimulator` 模拟 "Wikipedia writer ↔ topic expert" 多轮对话。每轮：writer 提问 →
`QuestionToQuery` 把问题翻译成搜索查询（提示语是"你会在 Google 搜索框里输入什么？"）→
检索 top-k → `AnswerQuestion` 基于 snippet 作答。对话历史截断 2500 词，单条 snippet 上限 1000 词。

终止条件三个：撞到 `max_turn`、writer 返回空、或 writer 说出硬编码的
"Thank you so much for your help!"。最后这个设计朴素但有效——给了模型一个显式退出信号。

### 3. Moderator：一个专门制造意外发现的角色

Co-STORM 设计得最巧的部分。Moderator agent 的职责被定义为
**基于"检索到了、但前面轮次没用上"的信息提出问题**——直接工程化地回应 unknown unknowns。

配套的防收敛机制更实在：`DiscourseManager.get_next_turn_policy()` 中，
连续 N 轮只回答不提新问题就强制插入 Moderator 发言，并置 `should_reorganize_knowledge_base=True`。
这是在用规则对抗多 agent 对话最典型的失败模式——聊着聊着陷进局部话题出不来。

关键默认参数（`RunnerArgument`）：

| 参数 | 默认值 | 含义 |
|---|---|---|
| `total_conv_turn` | 20 | 对话最大轮数 |
| `retrieve_top_k` | 10 | 每次检索返回数 |
| `max_search_queries_per_turn` | 3 | 每轮最大查询数 |
| `max_num_round_table_experts` | 2 | 圆桌活跃专家数 |
| `warmstart_max_num_experts` | 3 | 预热阶段专家数 |
| `moderator_override_N_consecutive_answering_turn` | 3 | **防收敛阈值** |
| `node_expansion_trigger_count` | 10 | 概念树节点扩展触发片段数 |

### 4. Mind map 作为共享概念空间

Co-STORM 维护动态更新的 `KnowledgeBase`，把信息组织成层级概念结构，UI 上呈现为思维导图。
README 措辞是建立人机之间的**共享概念空间**。

> 综合：意图比实现更重要。多 agent 讨论若只呈现为线性对话流，人跟不住，
> 也就无法在正确时机插话；必须投影成可俯瞰的结构，人机协作才成立。

## 架构定位：它是 workflow，不是 agent

对照 [[building-effective-agents]]：STORM 四模块（`knowledge_curation` → `outline_generation`
→ `article_generation` → `article_polish`）由**预定义代码路径**编排，属于
prompt chaining + parallelization，无动态自主决策。Co-STORM 稍微挪了一点——
`DiscourseManager` 运行时决定下一个发言者——但该决策本身是规则分支
（模拟用户 / RAG 基线 / moderator 覆盖 / 专家轮转），不是 LLM 自主判断。

> 综合：这在 2024 年是**正确取舍**而非缺陷——当时模型能力不足以支撑自主编排，
> 写死流程才拿得到稳定输出。但它也解释了掉队原因：**流程写死意味着模型变强时系统不会跟着变强。**
> 这是 Simplicity 原则的一个反面边界。

## 现状：停滞，且被商品化浪潮吞没

| 项 | 情况 |
|---|---|
| 最后 commit | 2025-09-30（放宽依赖版本限制） |
| 最后 release | v1.1.0，2025-01-23（接入 litellm） |
| 2025 全年活动 | 1 月 litellm、4 月修 typo、5 月改 README、9 月松依赖 |
| 社区 | 30.4k star / 2.8k fork；研究预览累计 70,000+ 试用 |

同期该品类的商业进展（出处与检索日期见 frontmatter，2026-08-11 核实并加限定）：OpenAI Deep Research
2025-02-02 发布（东京发布会当地时间为 2 月 3 日；首发仅 Pro 订阅，o3 特化版驱动），2026-02-10 宣布
升级并于次日推送：底层换 GPT-5.2、可接任意 MCP、限定可信站点、实时看进度；Google 2026-04-21 在
Gemini API 公开预览（付费档）Deep Research / Deep Research Max（均基于 Gemini 3.1 Pro），
其中 **Max 版**在 DeepSearchQA 报 93.3%（2025-12 初版为 66.1%）。

> 综合：**STORM 是被自己开创的品类反噬的研究原型。** 它证明了"多视角提问 + 迭代检索 +
> 结构化大纲"走得通，然后大厂用更强的模型加端到端 RL 把同一件事做得更好，且用户不必配 API key。
> 学术团队既无动力也无资源跟这场军备竞赛——OVAL 2025 年后的公开动向是 WikiChat
> 与几个 Magic Grants 资助的多语言/垂直项目，**没有 STORM 的直接后继**。

## 还剩什么价值

按重要性排序：

1. **方法论可拆下来单独用。** 机制 1 与 3 跟这个具体系统无绑定关系，可移植到任何自动研究场景。
   这是最耐用的部分，本 wiki 的移植成果见 [[STORM-研究提示词组]]。
2. 综合：**Co-STORM 的人机协作范式至今无商业对标**（基于 2026-08-11 对该品类商业产品的
   检索对比，见 frontmatter 源）。Deep Research 类产品的交互是
   "提交任务 → 等 5-30 分钟 → 收报告"，用户全程缺席；Co-STORM 是"旁听 → 随时插话改方向"。
   两者面向不同认知任务：前者适合已知道要什么，后者适合探索中才逐渐搞清要什么。
   后一种需求真实存在，但没人做产品。
3. **可控性。** 开源、任意 litellm 模型、十余种检索器（含 `VectorRM` 接私有向量库、
   SearXNG 自托管）。商业 deep research 给不了"私有语料 + 指定模型 + 完全本地"这个组合。

反过来说：**若只是想要一份带引用的调研报告，2026 年不应再自己跑 STORM**——商业产品在质量和成本上都赢。

## 局限

**论文与专家评估承认的：**
- **Source bias transfer**：检索到什么立场的源，文章就带什么立场，无中立性校正机制。
- **Over-association**：把不相关事实强行关联，长文本生成通病。
- Wikipedia 编辑总评：不能产出发表级文章，仅在 pre-writing 阶段有帮助。

**评估数字的语境（重要）：** STORM 相比 outline-driven retrieval-augmented baseline，
"组织良好"**绝对提升 25 个百分点**、覆盖广度提升 10 个百分点。注意这是
**与作者自建的单一较弱基线相比**，不存在排行榜意义上的"第二名"，也不是相对提升。
Co-STORM 的 70%（胜搜索引擎）/ 78%（胜 RAG chatbot）偏好度同理——2024 年的基线，
且偏好度不等于产出质量。

**本 wiki 补充的一条：二次失真。**
`TopicExpert` 的回答是 LLM 基于检索 snippet 生成的，**不是原文**；后续大纲与文章又基于这些回答生成。
最终文章与原始来源之间隔了**两层 LLM 转述**，而引用标注指向的仍是最初那个 URL。
引用看起来可溯源，中间的信息损耗却不可见。snippet 上限 1000 词进一步压缩了这个通道。

## 二次传播中的"去机制化失真"

最初的观测样本是知乎《Stanford STORM 方法：如何让 Claude 在几分钟内完成博士级研究》
（`https://zhuanlan.zhihu.com/p/2051623683756766563`，编辑于 2026-06-21，自述转写自
`x.com/heynavtoor` 推文）。

> ⚠️ 证据强度已降级（2026-07-29）：该文的摘录存档因**二手转写、非全文 verbatim、原文不可核验**
> 被移出 `raw/`（用户判定质量不足）。原 URL 在本机实测无响应（curl 裸请求与浏览器 UA 均 HTTP 000，
> DNS 与 443 均正常），既不能证实也不能证伪。存档内容仍可从 git 历史取回：
> `git show 88c8ad8:"raw/sources/articles/2026-06-21-知乎-Stanford-STORM方法.md"`。
> 下方核对表的逐条对照基于该存档做出，**当前不在仓库内**——若要重新引证，应改用下方英文侧的活样本。

**它抽掉了什么：** STORM 的名字里 **R 就是 Retrieval**，该文给出的却是
**固定五角色（从业者/学者/怀疑者/经济学家/历史学家）、全程无检索**的 role-play 模板，
并声称"不需要安装任何软件""复现 STORM 的核心研究能力"。被抽掉的三个环节：
检索驱动的视角发现（固定角色表对所有主题一视同仁）、每轮的真实检索 grounding、引用可溯源。

**核对表：**

| 该文说法 | 实际 |
|---|---|
| STORM 全称与 OVAL / NAACL 2024 归属 | ✅ 准确 |
| "同行评审测试中结构化程度比第二名高 25%" | ❌ 非同行评审测试、无"第二名"、是绝对百分点 |
| "STORM 有一个已知问题：它不会主动批判自己" | ❌ 杜撰；真实自述局限是 source bias transfer 与 over-association |
| "5 分钟完成博士级研究" | ❌ 与论文"仅在 pre-writing 阶段有帮助"直接冲突 |

**最关键的一点**：25%/10% 这组数字的成立前提是
**带检索的 STORM 打赢了另一个带检索的 baseline**。搬去给一个无检索的 prompt 模板背书，
数字的前提已经不存在了。

**该文推荐的"同行评审"步骤（让 Claude 给自己的研究打 1-10 分）恰好踩中已知缺陷**：
[[Evals]] 记录的 LLM-as-judge 自我偏好偏差（arXiv:2404.13076），
以及评判错误与生成错误高度相关——同一盲区不会因为换个 prompt 就被看见。
自评比不评更糟，因为它把未验证内容包装成已验证内容。

> 综合：这类失真有固定的三步模式——**保留原系统的名字与实验数字 → 抽掉最难实现的那个机制
> → 包装成"人人 5 分钟可复现"**。名字和数据都还在，可验证性已经没了，
> 而读者看到"斯坦福""NAACL 2024""25%"这些锚点很难察觉拿到的是另一个东西。
> 识别方法很朴素：**看它有没有把原系统最难的那部分一起搬过来；搬不动的地方往往正是价值所在。**
> （此法只覆盖机制类失真 M1–M4；对无"最难机制"可查的引文归属漂移 M5 不适用，
> 见 [[AI方法论的去机制化失真]] 的识别方法清单。）

这与 [[代码与文档漂移的本质]] 的**表达漂移**同构：同一标识符（STORM）指向两个实质不同的产物，
权威性还挂在旧的那个上，中间无任何调和机制。

**已升格为论点页（2026-07-29）**：另外 7 个样本已逐篇实读取证，本节的判断不再依赖已移除的知乎存档。
完整证据点表、分特征统计与反例见 [[AI方法论的去机制化失真]]。三条与本页直接相关的结论：

1. 上表四条核对**在独立样本上复现**：同一杜撰措辞以四种表述在三种语言里同构出现
   （英文 "next best method" 与 "best alternative method"、中文"第二名"、日文"次点の手法"），
   且样本集中在 2026-06-18 → 07-08 三周内。共同上游已于 2026-08-11 取证确认：Nav Toor
   2026-06-17 的 X 长文（含知乎版自述转写的那条推文；存档与逐特征核验见论点页）。
2. 原判断"三步打包模式"**已修正**：四个失真特征可分离、独立传播。
   按确认数传播最广的是固定五角色（9 个样本确认 7），**唯一零反例**的是"杜撰缺陷 + 自评补丁"——
   连把检索重新实装回去的 GitHub 项目也照抄了它。
3. 存在反例：有样本把 25/10 的比较对象准确写成 "retrieval-augmented baselines"，
   也有样本明确披露自己与官方 STORM 的机制差异。**二次传播不等于必然失真**。
4. 论点已于 2026-08-27 在第二主题（SDD 批评的二次传播）上复现——失真载体从人写的二手文章
   扩展到检索工具的自动摘要，论点页因此不再以 STORM 为单一观测对象。同批提出的
   **M5（引文归属漂移）**其唯一样本已于 2026-08-31 定向复查中被证伪（该引语实为 Kent Beck
   原话），M5 现无确认样本、保留为待观察形态，详见 [[AI方法论的去机制化失真]]。

## 关联

- [[STORM-研究提示词组]]：本页机制 1、3 的可执行移植；刻意保留被上述失真样本抽掉的三环节。
- [[llm-wiki-方法论]]：**STORM 强在发现、llm-wiki 强在沉淀**。STORM 每次研究跑完即弃、
  跨会话不积累，本质是高级 RAG——正是 Karpathy 批评的对象；本 wiki 恰好接住它的产物。
- [[building-effective-agents]]：workflow vs agent 的判定依据与 Simplicity 反面边界。
- [[Evals]]：自评不可靠的实证依据。
- [[代码与文档漂移的本质]]：去机制化失真作为表达漂移的一个变体。
