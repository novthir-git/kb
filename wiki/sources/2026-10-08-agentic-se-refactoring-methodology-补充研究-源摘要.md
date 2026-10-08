---
tags: [素材, AI, Agent, 软件工程, 重构, 方法论, 上下文]
created: 2026-10-08
updated: 2026-10-08
sources:
  - "raw/sources/notes/2026-10-08-agentic-se-refactoring-methodology-补充研究.md"
  - "https://arxiv.org/abs/2404.06654 （RULER；检索于 2026-10-08）"
  - "https://arxiv.org/abs/2502.05167 （NoLiMa；检索于 2026-10-08）"
  - "https://www.trychroma.com/research/context-rot （检索于 2026-10-08）"
  - "https://genai.club （Reeve Yew，Long-Context LLM Benchmarks 2026，2026-05-22 发布、09-19 更新；30–60 分说法的出处；检索于 2026-10-08）"
  - "https://contextarena.ai （经公开 API 取数；检索于 2026-10-08）"
  - "https://www.anthropic.com/news/claude-opus-4-6 （2026-02-05；检索于 2026-10-08）"
  - "https://deepmind.google/models/gemini/pro/ （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2501.19399 （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2307.03172 （Lost in the Middle；检索于 2026-10-08）"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2602.16069 （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2601.16746 （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2509.09614 （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2511.13998 （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2605.20049 （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2601.02200 （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2606.21804 （检索于 2026-10-08）"
  - "https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html （检索于 2026-10-08）"
  - "https://claude.com/blog/context-management （Anthropic，2025-09-29；检索于 2026-10-08）"
  - "https://platform.claude.com/docs/en/release-notes/overview （检索于 2026-10-08）"
  - "https://platform.claude.com/docs/en/build-with-claude/compaction （检索于 2026-10-08）"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-caching （检索于 2026-10-08）"
  - "https://code.claude.com/docs/en/how-claude-code-works （检索于 2026-10-08）"
  - "https://openai.com/index/gpt-5-1-codex-max/ （2025-11-19；直连 403，经搜索摘要与帮助中心读取；检索于 2026-10-08）"
  - "https://developers.openai.com/api/docs/guides/compaction （检索于 2026-10-08）"
  - "https://developers.openai.com/api/docs/guides/prompt-caching （检索于 2026-10-08）"
  - "https://github.com/github/spec-kit （检索于 2026-10-08）"
  - "https://kiro.dev/docs/specs/ （检索于 2026-10-08）"
  - "https://arxiv.org/abs/2606.05608 （检索于 2026-10-08）"
  - "http://www.incompleteideas.net/IncIdeas/BitterLesson.html （检索于 2026-10-08）"
---

# Agentic SE 重构方法论·补充研究 A/B——用户调研稿续篇源摘要

## 来源定位

用户 2026-10-08 在会话中直接给出的调研稿续篇，接在 09-23 调研稿（[[2026-09-23-agentic-se-refactoring-methodology-源摘要]]）
的第 0–5 节之后，编号为第 6、7 节。性质与原稿相同：**二次综合 + 用户判断，不是一级来源**。

- §6（补充研究 A）回答"上下文经济性有没有数据支撑"，给出三层证据与"会不会被更强模型抹平"的两维判断。
  这一节以经验论断为主，本页逐项回查一级来源。
- §7（补充研究 B）是一把判断尺子和用它做的分档，属**用户判断**。本页只核其中的事实钩子；分档本身的内部一致性
  检查放在 [[AI工程方法论的耐久度]]。
- 文中提到的配套图表 `context-economy-evidence.html` 在用户本机，未随本次提供，未存档。

判断与跨源综合见 [[上下文经济性]]、[[AI工程方法论的耐久度]] 与 [[Agentic SE 时代的系统重构]] §十。本页只记核验。

核验方式：3 个核验代理分组回查一级来源（长上下文退化 / coding agent 与代码库结构 / §7 事实钩子），写进 wiki 的
关键数字由维护者对照代理给出的原文引语复核。

## 结构性校正

1. **第三层"基本缺失"不成立，而且结论的方向要翻过来读。**受控实验有：SonarSource 的极小对照（整洁度不改变通过率、
   token 少 7%）、CodeScene 的 Code Health 研究（开源中等模型在不健康代码上更易破坏语义，Claude 组无显著差异）、
   CodeThread（在 agent 代码上继续开发解决率最多低 13.1%，传统可维护性指标解释不了）。它们少、新、多为厂商所做，
   但拼起来恰好支持用户自己的两维判断：强模型上质量维度已很弱，成本维度为正。原文把这一层当"诚实短板"，实际是
   该判断最直接的证据。
2. **"经济维度：窄读取永远便宜一个数量级以上（≈25×）"失准。**25× 只是 token 数之比；缓存把多轮复用的成本差压到
   约 2.5× 或更低；本库两个实测值（7%、约 5.8×）都不到一个数量级。站得住的是"相对优势与能力无关，倍数看读取比与
   缓存命中"，跨会话的首轮读取最不受缓存影响。
3. **第二层"方向一致"要加限定。**LoCoBench-Agent 是反例：带 harness 的 agent 在长上下文软件任务上表现稳健。
   裸模型方向一致，agent 不一定——可能正是 harness 的上下文管理吸收了退化。

## §6 逐项核验

| 论断 | 核验 | 校正后的口径 |
|---|---|---|
| RULER（2024）区分标称与有效上下文 | **成立** | Hsieh 等，NVIDIA，arXiv 2404.06654，COLM 2024。声称 32K 以上的 17 个模型只有一半在 32K 保持合格（阈值为 Llama2-7B 在 4K 的 85.6%）；有效长度全部短于声称长度。原文只测到 128K |
| NoLiMa（2025）：去掉字面匹配后绝大多数模型 32K 即跌破短上下文性能的 50% | **成立** | Modarressi 等，arXiv 2502.05167，ICML 2025。v3："At 32K … 11 models drop below 50% of their strong short-length baselines"，共 13 个模型（v1 为 10/12）。基线取 250 / 500 / 1K 三个长度中的最高分 |
| Chroma "Context Rot"（2025，18 模型）：极简任务也随长度非均匀退化 | **成立** | 2025-07-14，Hong、Troynikov、Huber。"even on simple tasks"；"increasing non-uniformity in performance as input length grows"。18 个模型并非每个实验都全覆盖 |
| 截至 2026 年多事实检索在 200K+ 仍有 30–60 分退化 | **部分成立** | 出自营销博客 genai.club（2026-05-22），30–60 无数据链接，且它援引的 RULER 只测到 128K。第三方 Context Arena（MRCR v2 8-needle，高推理档，2026-10-08 取数）：从 8K 到 (128K,256K] 区间跌约 11–53 分、到 (256K,512K] 区间约 22–69 分。退化存在，范围比 30–60 宽，且一年内明显收窄（Gemini 3.1 Pro 2026-04 跌约 53 分，Gemini 3.7 Flash 2026-08 跌约 11 分），作为通则写死不成立 |
| 没有任何前沿实验室公布过经第三方验证的 500K+ 多事实检索分数 | **失准** | Google 自报 Gemini 3.1 Pro MRCR v2 8-needle 1M 为 26.3%，Context Arena 复现为 25.9%；Gemini 3.7 Flash 第三方测得 63.5%。只对 Anthropic、OpenAI 成立：Anthropic 自报 Opus 4.6 1M 为 76%（2026-02-05），第三方只测到 512K 区间（49–54%，推理档不同不可直接比） |
| softmax attention 下"上下文越满、单位信息利用质量越低"有机制根源 | **部分成立** | Nakanishi 2025（arXiv 2501.19399，预印本）：softmax 输出最大元素随输入长度趋于零（attention fading）。Anthropic 文章同时列 n² 成对关系与训练分布（短序列更常见）两种原因；Lost in the Middle 是位置效应的实证。可写作"有部分机制解释"，不能说已证明是主因 |
| 《The Limits of Long-Context Reasoning in Automated Bug Fixing》：agent 约 30% vs 64K 全量上下文 0–7%；失败轨迹 token 约为成功的 2 倍；作者结论 | **基本成立** | Raju 等（SambaNova），arXiv 2602.16069，ICLR 2026 ICBINB workshop。SWE-bench Verified 100 题：GPT-5-nano 31%、DeepSeek-R1 30.3%、Qwen3-32B 15.2%；64K：Qwen3-Coder-30B-A3B 7%、GPT-5-nano 0%。只有 GPT-5-nano 两种设置都跑了；"约 2 倍"只在 v1 表中（1.82×、1.99×，两个模型）。结论原文："agentic success primarily arises from task decomposition into short-context steps rather than effective long-context reasoning"——由 token 分布推断，非因果实验 |
| SWE-Pruner：裁剪上下文反而提升表现 | **部分成立** | arXiv 2601.16746。SWE-bench Verified：Claude Sonnet 4.5 70.6% → 72.0%，GLM-4.6 55.4% → 56.6%，token −23.1% / −38.3%；未报重复运行或显著性。准确说法是"少读 23–38% 而不伤成功率"。摘要的"23–54%"混入了 SWE-QA 数字 |
| LoCoBench 同向 | **部分成立** | LoCoBench（arXiv 2509.09614）是单轮 LLM 评测，退化只做定性描述，且难度按上下文长度定义，两者混淆。**反例**：LoCoBench-Agent（arXiv 2511.13998）称"agents exhibit remarkable long-context robustness"。附带发现：LoCoBench-Agent 把"Claude 3.5 Sonnet 29%→3%"归于 LoCoBench，实出 LongCodeBench（arXiv 2505.07897），属引用错误 |
| "代码库结构 → agent 成功率"的直接因果实验基本缺失 | **失准** | 见结构性校正第 1 条。SonarSource（arXiv 2605.20049）：6 对极小对照仓库、33 任务、660 次试验，Claude Code + Sonnet 4.6，通过率 0.913 vs 0.921，输入 token −7.1%、重访文件 −33.8%；作者自建仓库与任务、单配置、无显著性检验。CodeScene（arXiv 2601.02200，FORGE 2026）：测的是重构后语义是否保持而非任务成功；Sonnet 4.5 −2.74pp、Claude agent −1.38pp（p=0.439），作者自承 1,000 文件的子样本可能功效不足。CodeThread（arXiv 2606.21804）：4 个前沿 agent、4 个基准，在 agent 代码上解决率最多低 13.1% |
| AGENTS.md 是少数有实证研究的实践 | **成立** | Lulla 等 2601.20404、Gloaguen 等（ETH）2602.11988、McMillan 2605.10039 均存在，结论互相矛盾，见 [[AI编码技术债的三层治理]] |
| 质量维度在收窄：退化起点后移（32K → 200K → 更远） | **基本成立** | 收窄有直接迹象（见上 Context Arena 一行；CodeScene 中强模型对代码健康度不敏感）。"32K → 200K"是示意性的路线，不是同一测量上的数字 |
| 经济维度：窄读取永远比全量读取便宜一个数量级以上（≈25×） | **失准** | 见 §7 表"窄读取"一行与结构性校正第 2 条 |
| 多 agent 并行依赖可分解的窄变更；人类 review 与 CI 的窄范围需求不随模型变强而消失 | 判断，不核验 | 与 09-23 已核验的 `/batch`、Bun 案例（拆成独立单元、以既有测试为门禁）方向一致 |

## §7 的事实钩子

| 论断 | 核验 | 校正后的口径 |
|---|---|---|
| context engineering 机制层（compaction、外置笔记、子 agent 压缩回传）正被 harness 与模型内建吸收 | **成立** | API 层：Anthropic 2025-09-29 推出 context editing（自动清除过时的工具调用与结果）与基于文件的 memory tool（自报内部评测：两者合用提升 39%，context editing 使 token 消耗降 84%）；2025-11-24 SDK 加客户端 compaction；2026-02-05 上线服务端 compaction API（beta）；2026-09-14 按需 compaction。harness 层：Claude Code 先清旧工具输出、必要时再摘要，子 agent 的工具调用不进主上下文、结束时只回传摘要。模型层：OpenAI 称 GPT-5.1-Codex-Max（2025-11-19）是其"first model natively trained to operate across multiple context windows through a process called compaction"；Responses API 另有 `/responses/compact` 端点。**模型层"原生训练"目前只有 OpenAI 明说**，Anthropic 一侧落在 API 与 harness |
| 窄读取永远比全量读取便宜一个数量级以上（读 2k 行 vs 50k 行 ≈ 25×），与能力无关 | **失准** | 25× 只是 token 数之比。缓存读价通常是基础输入价的 0.1×（Anthropic 现行文档，部分新模型更低至 0.05× 或 0.025×；OpenAI GPT-5.x 系列为 0.1×），全量上下文在多轮中被缓存复用后，每轮边际成本比约 25×0.1 = 2.5×，在更低读价的模型上接近持平甚至反转；首轮另付 1.25×（5 分钟）或 2×（1 小时）的写入费。另：50k 行约合 50 万 token，可能直接超出上下文窗口。本库唯一的实测是 Thoughtworks 同一变更输入 −83%，约 5.8×，也不到一个数量级。站得住的说法是：**窄读取的相对优势与模型能力无关，但倍数取决于读取体量比与缓存条件**；缓存折扣本身是厂商定价，不是物理常数 |
| Spec Kit / Kiro 的"三步 markdown 流程" | **基本成立** | Kiro 原文就是 "three-phase workflow"（requirements.md → design.md → tasks.md），另有 Design-First、Bugfix spec 与无审批门的 Quick Spec。Spec Kit 现为 "Constitution once per project; specify → plan → tasks → implement → converge per feature"，三步是简化 |
| AaaS 论文的 "intent architect" | **成立** | Zhenfeng Cao，arXiv 2606.05608（单作者预印本，v1 2026-06-04，v2 2026-06-10）。摘要："intent architect rather than code author"；第 1 节给的是三重角色："intent architects, agent coordinators, and outcome auditors" |
| bitter lesson | **成立** | Sutton 2019-03-13："general methods that leverage computation are ultimately the most effective, and by a large margin." 用户的引申（押注模型弱点的工程投资折旧期一两年）是估计，无测量 |
| 委派比例 0–20% | **成立（沿用 09-23 核验）** | 一手来源是 Anthropic 2025-12-02 研究文章，须带"超过一半的受访者"限定，见 [[2026-09-23-agentic-se-refactoring-methodology-源摘要]] |

§7 其余内容（四档分法、各条目归档、"先投折旧最慢的"）是判断而非事实，不在本页核验范围；按用户自己的尺子
复查出的四处不一致及其修订（用户同日裁定）见 [[AI工程方法论的耐久度]] 修订记录。
