---
tags: [主题, AI, 方法论, 知识治理]
created: 2026-07-29
updated: 2026-08-31
sources:
  - "https://x.com/heynavtoor/status/2067194761446920264 （上游长文，检索于 2026-08-11；存档 raw/sources/articles/2026-06-17-heynavtoor-Stanford-STORM四提示词长文.md）"
  - "https://x.com/heynavtoor/status/2061802543207067794 （同作者 2026-06-02 准确版线程，检索于 2026-08-11）"
  - "https://gist.github.com/thevillagehacker/e09c947b2281827692d43c8ace835049 （检索于 2026-07-29）"
  - "https://secondbrainn.substack.com/p/stanford-quietly-built-a-research （检索于 2026-07-29，第 2 个 prompt 后付费墙）"
  - "https://linas.substack.com/p/stanford-storm-claude-ai-research （检索于 2026-07-29，正文付费墙）"
  - "https://note.com/claudecode_lab/n/nfae8a85d271d （检索于 2026-07-29）"
  - "https://medium.com/ai-all-in/how-to-make-claude-research-like-a-phd-in-minutes-f226e9c40677 （检索于 2026-07-29，会员墙）"
  - "https://mikareyes.com/ai/stanford-storm-research-method （检索于 2026-07-29）"
  - "https://github.com/hadufer/claude-storm （检索于 2026-07-29）"
  - "https://arxiv.org/abs/2402.14207 STORM, Shao et al., NAACL 2024（检索于 2026-07-29）"
  - "https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html （检索于 2026-08-27，逐项核对原文数字）"
  - "https://newsletter.kentbeck.com/p/earn-and-learn （Kent Beck, 2026-02-18；检索于 2026-08-27，全文核对未见流传引语——2026-08-31 已查明该句出自 Beck 的 LinkedIn 帖而非本文）"
  - "https://martinfowler.com/fragments/2026-01-08.html （Martin Fowler《Fragments: January 8》，2026-01-08；检索于 2026-08-31，逐字引用该 Kent Beck 引语并链回其 LinkedIn 出处）"
  - "https://www.linkedin.com/feed/update/urn:li:activity:7413956151144542208/ （Kent Beck 原帖，Fowler 标注的出处；检索于 2026-08-31 未能直连核验——匿名访问 302 跳转登录页）"
  - "[[SDD 收益主张的实证赤字]]"
---

# AI 方法论的去机制化失真

## 论点

一项 AI 研究成果在二次传播中，**权威锚点（机构名、会议名、实验数字）被完整保留，而支撑这些数字的核心机制被抽掉**，
最终包装成"人人几分钟可复现"。读者看到的名字和数据都是真的，拿到的东西却是另一个——
这是 [[代码与文档漂移的本质]] 里**表达漂移**的传播学版本：同一标识符指向两个实质不同的产物，
权威性仍挂在旧的那个上，中间没有任何调和机制。

> 综合：本页原判断（[[STORM-知识策展系统分析]]，2026-07-29 早先）认为这是"整体打包"的三步模式。
> 实读 7 个样本后**修正**：四个特征是**可分离**的，各自独立传播，传播力差异很大。见下方分特征统计。

## 四个特征标记（以 Stanford STORM 为观测对象）

| 标记 | 原始事实 | 失真形态 |
|---|---|---|
| **M1 抽掉检索** | STORM 的 R 就是 Retrieval，每轮提问都对真实网页 grounding | 给出纯 role-play 模板，"不需要任何软件/不用联网" |
| **M2 固定角色表** | persona 由检索到的同类主题语料反推得出，随主题变化 | 写死五个角色：practitioner / academic / skeptic / economist / historian |
| **M3 数字失真** | 25%/10% 是相对作者自建的单一 baseline 的绝对百分点提升 | 说成"比**第二名 / best alternative / next best method**高 25%"，甚至"比**人类**强 25%" |
| **M4 杜撰缺陷 + 自评补丁** | 论文自述局限是 source bias transfer 与 over-association | 改称"STORM 的已知弱点是**它不会自我批判**"，并据此加一步"让 AI 给自己打 1-10 分" |

## 证据点表

| 日期 | 来源 | 信号 | 备注 |
|---|---|---|---|
| 2026-06-17 | X 长文 / Nav Toor（@heynavtoor），存档 `raw/sources/articles/2026-06-17-heynavtoor-Stanford-STORM四提示词长文.md` | M1「No software. No GitHub. No setup. Just paste.」M2 五角色（THE PRACTITIONER…THE HISTORIAN 编号列出）M3「25 percent more organized than the next best method」M4 Phase 6 称"系统不做自我批判"+ Prompt 4 让 Claude 按 1-10 打信心分 | **上游节点，四标记齐全**；抓取时 305 万 views / 1.8 万收藏；hadufer 仓库 README 署名此文为出处（2026-08-11 取证） |
| 2026-06-18 | gist / thevillagehacker | M1「No software. No GitHub. No setup. Just paste.」M2 五角色 M3「25 percent more organized than the next best method」M4「The system does not self critique」+ 1-10 打分 | **四标记齐全**；最早的下游复制件（上游长文次日），措辞与上游几乎逐字一致 |
| 2026-06-19 | secondbrainn.substack | M1「you don't need any of the software」M2 五角色 M3 标题即「25% Better Than Humans」+ 正文「than the best alternative method」 | M3 **进一步升级**：baseline 被换成"人类"；M4 落在付费墙后未见 |
| 2026-06-21 | 知乎（林夕，摘录存档已按质量要求移出 raw，见 git `88c8ad8`） | M1 M2 M3「比第二名高 25%」M4 杜撰"不会主动批判自己"+ 1-10 自评 | 自述转写自 `x.com/heynavtoor` 推文（即上表上游节点，2026-08-11 已证实）；知乎原文本机不可达 |
| 2026-06-25 | linas.substack（Linas Beliūnas） | **M3 反例**：「25-percentage-point margin over outline-driven retrieval-augmented baselines」 | 数字表述**正确**；视角数为 10 而非 5；正文付费墙，M1/M4 未知 |
| 2026-06-26 | note.com / Claude Code研究所（日文） | M1「専用ソフトもGitHubもセットアップもいりません」M2 五角色 M3「次点の手法よりも25%」M4「自己批判をしません」+ 1-10 打分 | **四标记齐全**；「次点」＝字面"第二名"，与中文版同构 |
| 2026-06-29 | medium / Yanli Liu | 「ninety seconds later you get a dissertation」 | 会员墙，二级标题后截断；M1-M4 均未能确认 |
| 2026-07-08 | mikareyes.com（Mika Reyes） | M2 五角色 + 五分钟/40-60 小时；**M1 反例**：明确披露官方 STORM「searches the internet, collects citations」 | 机制差异**被披露而非隐藏**；完全不用 25%/10% 数字 |
| 检索于 2026-07-29 | github / hadufer/claude-storm | **M1 反例**：「interviews each one against real web sources」真的实现了检索；但 M2 五角色、M4「the system does not critique itself」+ 1-10 confidence 照旧 | 机制被**重新装回去**，杜撰缺陷却跟着一起传了过来 |

## 分特征统计（9 个样本 = 上游长文 + 8 个下游，含 3 个部分不可见）

| 标记 | 确认出现 | 确认反例 | 未能确认 |
|---|---|---|---|
| M2 固定五角色 | 7 | 1（linas 为 10 视角） | 1（medium） |
| M4 杜撰缺陷 + 自评补丁 | 5 | 0 | 4 |
| M1 抽掉检索 | 5 | 2（mikareyes 披露、hadufer 实装） | 2 |
| M3 数字失真 | 5 | 1（linas 表述正确） | 3 |

> 综合（2026-08-11 两处修正：① 原表 M2 行误计 5/0/2、行总和 7≠8，且把 linas 反例计成 0，
> 按证据点表逐样本重算；② 上游长文取证后纳入为第 9 个样本，四行确认数各 +1）：按确认数，
> **M2（固定五角色）传播最广**（9 个样本确认 7），但有 linas 的 10 视角反例；
> **M4 是唯一零反例的一项**——6 个全文可判定样本中 5 个命中（第 6 个是 mikareyes：全文可见
> 但无此内容，按"缺席非反例"口径计入表中未确认列），包括那个把检索重新实装回去的 GitHub 项目
> 也照抄了"STORM 不会自我批判"这个杜撰缺陷；其余 3 个未确认均为付费墙/截断不可见。
> M2 与 M4 恰是四项里**可直接复制粘贴**的两项（角色表、自评指令），
> 而 M1/M3 只是描述。**能被复制粘贴的错误，比只能被相信的错误传得更远。**

> ⚠️ 这个"补丁"恰好踩中已知缺陷：让模型给自己的产出打 1-10 分，正是 [[Evals]] 记录的
> LLM-as-judge 自我偏好偏差（arXiv:2404.13076），且评判错误与生成错误高度相关——
> 同一盲区不会因为换个 prompt 就被看见。自评比不评更糟，因为它把未验证内容包装成已验证内容。

## 第二观测对象：SDD 批评的二次传播（2026-08-27 新增）

本页原「待追踪」问的是：这个形态**是否会在下一个热门系统上复现**。答案是会——
在与 STORM 完全无关的主题（[[Specification-Driven Development|SDD]] 的批评性论述）上取到两个疑似样本，
其中**一例经复查确认失真**（Scott Logic 数字口径），**另一例于 2026-08-31 定向复查后证伪**
（Kent Beck 引语实为原话，见下表备注与 M5 小节）。
但**失真的载体变了**：STORM 那批样本是人写的博客与推文；这两个样本的来源都是
**检索工具自动生成的结果摘要**。

| 日期 | 来源 | 信号 | 备注 |
|---|---|---|---|
| 2026-08-27 | 检索工具对 Scott Logic 实测的自动摘要 | 转述为「33 minutes and 2,577 lines of markdown to produce 689 lines of code, compared to 8 minutes using iterative prompting — **approximately 10x slower**」。但 33.5 / 8 ≈ **4 倍**；原文的「约十倍」来自**含人工 review 的总时长**（SDD 第一增量约 4 小时 vs 迭代提示约 32 分钟） | **M3 同构：数量锚点的口径被替换。**两个不同口径的数字被并列成一个比值。原文数据本身准确且 caveat 充分，失真发生在转述层。已逐项回查原文核实 |
| 2026-08-27 | 检索工具对 Kent Beck 批评的自动摘要 | 归给 Beck 一句引语：SDD「encodes the (to me bizarre) assumption that you aren't going to learn anything during implementation that would change the specification」 | **原判 M5 引文归属漂移，2026-08-31 定向复查后撤销**：该句确为 Beck 本人所写，出自其 LinkedIn 帖，Martin Fowler《Fragments: January 8》（2026-01-08）在署名「Kent Beck」的引块中逐字引用并链回该帖（https://martinfowler.com/fragments/2026-01-08.html ，检索于 2026-08-31；LinkedIn 原帖匿名访问 302 跳登录，未能直连核验）。08-27 判「未见此句」是因为只核对了 Beck 的一篇 newsletter（《Earn *And* Learn》，2026-02-18），**检索范围不足，不是归属漂移**。附注：本页未记录该摘要是否同时指定了具体篇目；若曾指定为该 newsletter，则仍属「作者对、篇目错」的出处定位问题，但记录不足以判定，故不计入 M5 |

### 这一例为什么值得单独记

> 综合（2026-08-31 修正，原标题为「这两例」）：Beck 引语一例已证伪，以下以确认的
> Scott Logic 一例为准；原第 2、3 点依赖「两例」的表述相应收窄。

1. **失真载体从「人写的二手文章」变成「自动生成的检索摘要」。** 后者无署名、无固定 URL、
   随查询即时生成，因此**无法被逐篇纠错，也无法定位上游节点**——本页原结论「要找的是上游节点，
   不是逐篇纠错」在这里失效了，因为上游节点是一次即时推理。
2. **它发生在「批评性论述」上，而非推广性论述。** STORM 那批失真服务于「这个方法很厉害且你几分钟
   就能用」的叙事；这一例失真服务于「这个方法有问题」的叙事。它沿最省力的路径发生——
   「给出一个干脆的倍数」比「交代口径」省力。
   综合：原写作「**失真不挑立场**」，但那是靠两例支撑的；证伪一例后仅剩单样本，
   该一般结论**降为待补证**。
3. **原始来源是干净的。** Scott Logic 数据准确、caveat 充分。
   这排除了「源头就错」的解释，把失真严格定位在转述层。

> 综合：因此本页的识别方法要补一条**针对 AI 摘要的**：凡是从检索摘要拿到的数字或引语，
> 在写进任何论断之前必须回到原文核对——**核对的成本远低于事后纠正一条已被引用的错误论断**。
> 本 wiki 的铁律 3（论断必有出处）本就要求这一点；本次两轮核对说明该要求在 AI 检索时代不是形式主义，
> 且**两个方向都需要它**：一次证实了失真（数字口径被替换），一次证伪了疑似（引语实为原话）。

### 对识别方法的补充：M5 引文归属漂移

原有四个标记（M1–M4）是以 STORM 为观测对象归纳的。M5 是本次新增的一般形态：

| 标记 | 形态 | 检查方法 |
|---|---|---|
| **M5 引文归属漂移** | 一句措辞漂亮、立场鲜明的话被归给某位权威，但其原文中不存在该句 | 拿引语的**特征词组**回原文全文检索，**范围须覆盖作者的全部公开渠道**（newsletter、博客、社交平台帖子、访谈、他人的逐字引用），不能只查一篇；找不到只支持「未经证实、暂不引用」，不支持断定归属有误，也不因为「听起来很像他会说的话」而放行 |

M5 与 M4（杜撰缺陷）共享同一机制——**给权威加上原文没有的内容**——但传播力可能更强：
M4 需要编造一个缺陷加一个补丁，M5 只需要一句话，而且越像那位作者的风格越不容易被质疑。

> 综合（2026-08-31）：M5 提出时的唯一样本已被证伪（Beck 引语实为其 LinkedIn 原话），
> **该标记目前无确认样本**，保留为**待观察形态**而非已证实形态——上面那段关于传播力的比较
> 同样只是推断，尚无样本支撑。这次复查还暴露了检查方法的缺口：只核对作者的一篇文章就下结论，
> 会把真引语误判为漂移。**"未在原文找到"与"归属有误"是两个结论，前者不蕴含后者**；
> 上表检查方法已据此收紧。

## 传播链形态

**上游节点已于 2026-08-11 定位并存档**：Nav Toor（@heynavtoor）2026-06-17 10:36 UTC 发布的 X 长文
（存档 `raw/sources/articles/2026-06-17-heynavtoor-Stanford-STORM四提示词长文.md`；抓取时 305 万 views、
1.8 万收藏、无 Community Note），M1–M4 四特征齐全，早于此前最早样本（gist，06-18）一天；
hadufer/claude-storm 的 README 明确署名该文为 four-prompt adaptation 出处（检索于 2026-08-11）——
上下游关系有直接署名证据，不止时间吻合。下游复制件集中在 **2026-06-18 → 2026-07-08 共三周内**，
跨中文、日文、英文三种语言与 substack / note / 知乎 / gist / medium / 个人博客 / GitHub 七个平台，
同一杜撰措辞以四种表述在三种语言里同构出现（英文 "next best method" 与 "best alternative method"、
中文"第二名"、日文"次点の手法"）。

> 综合：这不是"多人分别读错论文"，而是一条**已证实的单点污染 → 多语言复制**链。
> 更关键的对照：同一作者 2026-06-02 的线程对 STORM 的描述基本准确——明确说它搜索网页、读来源、
> 带引用写报告（https://x.com/heynavtoor/status/2061802543207067794 ，检索于 2026-08-11）；
> 两周后的"四提示词改编"才引入 M1。**失真不是无知，是改编时的主动删减**——为"无需任何软件、
> 只要粘贴"的传播卖点让路。治理上要找的是上游节点而非逐篇纠错，本条链的上游已找到。

## 反例告诉我们的边界

不能把"二次传播"等同于"失真"——2026-07-29 实读的 7 个英文/日文样本里有 3 个在某一维度上是干净的：

- **linas.substack** 把 25/10 的比较对象准确写成 "outline-driven retrieval-augmented baselines"。
- **mikareyes.com** 明确告诉读者：四提示词版本和官方 STORM 不是一回事，后者会真的联网检索。
- **hadufer/claude-storm** 直接用 subagent + 真实 web search 把被抽掉的机制装了回去。

> 综合：所以本论点的正确表述不是"二手解读必然失真"，而是**"失真沿最省力的路径发生"**——
> 需要工程实现的 M1 最容易被砍（也最容易被有能力的人补回来），
> 而只需复制一句话的 M4 几乎无损传播。

## 识别方法（可操作）

1. **查最难的那一步在不在**：原系统里最需要工程实现的环节（这里是检索 grounding），
   二手版本有没有一起搬过来。搬不动的地方往往正是价值所在。
2. **查数字的比较对象**："比第二名高 X%" 是高危措辞——多数论文的对照是自建 baseline，没有"第二名"。
3. **查局限是不是原文的**：把二手版本列出的"已知缺陷"拿去和论文的 Limitations 节对照。
   杜撰缺陷的作用通常是**为它接下来要卖的那个补丁做铺垫**。
4. **警惕可执行的补丁**：越是"加一步就能解决"的动作，越要查它解决的是不是一个真问题。
5. **查引语在不在原文里**（M5）：拿引语的**特征词组**回原文全文检索，**范围要覆盖作者的全部公开渠道
   （只查一篇会误判）**，找不到就当作未经证实、暂不引用——但别就此断定归属有误，
   也不因为"听起来很像他会说的话"而放行；凡从 AI 检索摘要拿到的数字或引语，写进论断前必须回原文核对。

## 证据方法说明

- 本页 7 个英文/日文样本于 2026-07-29 逐篇抓取实读；引语经抓取工具提取，**未逐字人工校对**。
  结论建立在多个独立样本的**一致性**上，而非任何单条引语的精确措辞。
- 3 个样本（secondbrainn、linas、medium）有付费墙，只能确认可见部分，表中已逐条标注"未确认"。
- 未把下游复制件网页存入 `raw/`：它们是活链接、可随时复核，且本页已把关键措辞逐条记入证据表；
  若某条日后失效，以表中记录为准。这与知乎样本的处理不同——那篇原文本身已不可达。
- **唯一例外是上游长文**（2026-08-11 经 fxtwitter API 抓取，Draft.js blocks 转 markdown 后存档
  `raw/sources/articles/2026-06-17-heynavtoor-Stanford-STORM四提示词长文.md`）：Wayback、archive.today、
  Rattibha、Hive 均无独立快照，抓取依赖第三方 API 可用性，故按"研究中重要网页"规则存档为一级证据。

## 关联

- [[STORM-知识策展系统分析]]：本论点的首个观测对象，含 STORM 四机制与失真核对表。
- [[STORM-研究提示词组]]：针对 M1 的工程对冲——刻意保留被失真样本抽掉的检索环节的可执行移植，
  其「设计前提」即以本页失真链为反面教材。
- [[代码与文档漂移的本质]]：表达漂移——同一标识符指向不同产物、权威性错挂。
- [[Evals]]：M4 自评补丁踩中的 LLM-as-judge 自我偏好偏差实证。
- [[llm-wiki-方法论]]：本 wiki 要求"论断必有出处 + 矛盾显式标注"，正是针对这类失真的对冲。
- [[SDD 收益主张的实证赤字]]：第二观测对象所在的论题；该页对 Hill 研究显式标注了「直连 403、
  经检索摘要核验」，即本页 M3/M5 教训的直接应用。
