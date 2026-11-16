# The components of agent memory（中文结构化摘录）

- 原始 URL：https://www.anthropic.com/research/components-of-agent-memory
- 发布方：Anthropic（Research 栏目，Team: Engineering；Topics: Agents / Context engineering / Agent memory）
- 页面日期：Published Nov 6, 2026
- 作者：Lance Martin（editorial guidance: Caitlin Love, Tom Chivers, Rebecca Hiscott, Jake Eaton, Blake Wilson；Pokémon 实验平台 David Hershey；图 Monika Tuchowska）
- 抓取日期：2026-11-16（curl 直连 HTML，HTTP 200；正文与全部图注 alt 文本均从同一份 HTML 提取）
- 存档原因：用户 2026-11-16 查询 Anthropic 官方 agent memory 文章；文章直接引用 Karpathy LLM Wiki gist，并以实验比较 wiki 与纯搜索，是 [[Agent 记忆架构]] 与 [[llm-wiki-方法论]] 的一手证据。厂商页面可能事后改版，故冻结快照。
- 存档说明：要点式中文结构化摘录，非全文翻译；关键原句保留英文原文并加引号。原文正文约 2.2 万字符。按原文章节顺序组织，二级标题保留英文原题；**图中数字全部取自图片 alt 文本**（正文未逐一写出），逐图保留。图片本身未存档。
- 存入后视为只读存档。

---

## 导语

- 以 Kierkegaard "life can only be understood backward, but it must be lived forward" 起题：记忆在当下写入，但价值要事后才知道。
- 人脑类比：海马体即时编码经历；离线（睡眠、安静休息）时回放，把经历逐步整合进新皮层。
- Agent 的对应分工：工作过程留在 logs / transcripts；借 Letta 与 UC Berkeley 的 sleep-time compute（arXiv 2504.13171）思路，在交互间隙"reflecting on logs to fix mistakes or produce new notes and representations"，即 **dreaming**。
- 图 1 alt：记忆层级自下而上为 **transcripts（可搜索事件日志）→ memory notes（Claude 写的笔记）→ memory representations（如 wiki）→ injected context（每次会话都加载）**；"Dreaming" 框内箭头从 transcripts 指向各层，上方相邻层之间双向。
- 图注："This can correct mistakes, create notes, build new memory representations, or shape what's preemptively loaded into future sessions."

## Memory notes

- 定义原句："By "agent memory," we mean knowledge that Claude gains from experience—including interactions with users and tasks it's been assigned—and that it retains between sessions, saved as context it can read later."
- 排除：权重变化；in-context learning（单次对话内获得的知识）；compaction（Claude 写摘要替代旧回合以在新窗口继续）。
- 人脑中，经历前后的化学信号把记忆标记为重要，被标记者在离线期回放更多（replay）。对应地，Claude 可在会话日志里标记显著事件，或写入 memory store（如一个笔记文件夹）。问题："how can Claude tell what's salient in the moment, before it knows what's coming next?"

## Memory can be a prediction about what the future will need

- 论点："Memory is, occasionally, a prediction." 写下一条规则 = 预测该模式会再次相关；写下已验证事实 = 预测未来会话会不经复核直接依赖它。
- **CL-Bench 1.0 数据库任务**（continual-learning-bench.com）：逐题查库作答，作答后告知正确答案，可写记忆。每题新开会话（Claude Managed Agents），唯一跨会话通道是一个持久 memory 目录。
- 各模型的"学习循环"成熟度：
  - Sonnet 4.6：只走到"猜原因"，目录里散落多个未验证猜测的文件；
  - Opus 4.7：合并成单一参考文档，开始标记已核/未核事实；
  - Sonnet 5：判分后标记 confirmed，答错写更正；
  - Opus 5：**第一个闭环**——多数条目含规则 + 如何得知它为真、旧题答案、陷阱警告；
  - Opus 5.5、Sonnet 5.5：同样闭环；有记忆时与 Opus 5 相当，无记忆基线略高。
- 图 3 alt（mean reward，stateless baseline → memory store）：Opus 5.5 0.655→0.838；Sonnet 5.5 0.644→0.833；Opus 5 0.564→0.828；Opus 4.7 0.383→0.700；Sonnet 5 0.306→0.610；Sonnet 4.6 0.330→0.364。右图为 30 题上的滑动平均曲线。

## Claude has learned to judge salience

- **Pokémon Red**：每次运行开始给一个可读写的记忆文件夹。比较 Sonnet 3.7 与 Fable 5 各一次运行、约第 10,000 步时的记忆目录。
- Sonnet 3.7："assumed everything might matter and wrote to memory indiscriminately"——每场战斗、每件物品、每个 NPC 一个文件；共 **413 个文件 / 225 个文件夹，1 枚徽章**。图 4 alt：977,930 字符，含多个 "consolidated" 文件夹。
- Fable 5：两个文件夹 9 个文件 + 顶层 `global.md`（图 4 alt：10 个文件、43,406 字符），**4 枚徽章**。
- 失败机理：游戏状态不断变化，详尽记录持续过时，越往后越多时间花在翻记忆。约第 10,000 步 Sonnet 3.7 开第四个 "master" 记忆文件夹，随后 17 步里新建 6 个文件、删 9 个、游戏内零动作。
- Fable 5 的原则：只记"游戏没有明确告诉它的东西"。屏幕每回合可读的信息（金钱、位置）存了是冗余；策略、计划、经检验的规则只有 Claude 推出来才存在，不写下就会消失。
- 组织方式：`global.md` 作为 dashboard（当前目标、打道馆的预写计划、自己的记忆使用规则）；`locations/` 放路线计划；`gameplay/` 放机制策略。例：连续 7 个精灵球没抓到鲤鱼王后写下 "If 3+ balls fail in a row, VARY the timing …"。
- Opus 5.5 同样只保留小型笔记文件夹追踪当前目标与下一步、边玩边重写，并通关。

## Steering Claude to write memory

- 原则："it helps to tell Claude what memory is for, but not how to use it." CL-Bench 上只告诉"有一个 memory 文件夹可用"，已足以让 Opus 4.7、Opus 5 有效使用并明显提分。
- 规则消融：每次测试给一条写什么的具体规则。规则 "record only failures" 使强模型丢掉大部分记忆增益。图 5 右 alt：记忆增益变化 Opus 5 −0.234、Opus 4.7 −0.150、Sonnet 4.6 −0.020。结论：强模型自行判断 salience 优于预设固定规则，规则反而可能削弱表现。
- 引导对旧模型帮助最大：Sonnet 4.6 常不读记忆、不检验理论；提示"先读记忆再答、显式检验理论"后分数近乎翻倍。图 5 左 alt：0.330（baseline）→ 0.364（memory）→ 0.641（memory + refined instruction）；参考线 Opus 4.7 0.700、Opus 5 0.828。
- Sonnet 5 不经提示 10 次中 9 次先读记忆；Sonnet 4.6 不到一半。
- 前沿模型的默认做法：只给简单指引——用户要求或明显值得记时写笔记，判断交给 Claude。

## Dreaming can correct memory

- 风险：会话内按 salience 写的笔记可能一开始就错，或随环境漂移，之后的会话会读到并信任它。dreaming 让 Claude 用原始 transcript 检验笔记（图 6）。
- **Mt. Moon 案例**（Managed Agents + 挂载记忆目录）：Claude 误记 PokéCenter 在山东侧，走出时宣布 "Mt Moon is behind me" 并写 "Mt Moon DONE"，随即跌下单向崖回到来路；导航工具不显示落差，它反而认定 "I overshot far west"。
- 对含错误位置的记忆文件夹跑 dreaming：对照 transcript 发现错误并改写（"The transcript gave Claude a ground truth to validate its memory against"）。改正后 Claude 回到洞内并最终抵达 Cerulean City。
- 未改正的运行：三次跌回来路后写 "I'm going to stop rather than keep looping"，被自动回复要求继续，一路退回 Pewter City，始终未达 Cerulean。
- 图 8 alt：3,000 步累计行动内，memory + dreaming 在第 **1,935** 步抵达 Cerulean；raw memory 跌崖并退回 Pewter；no memory 从未抵达。

## Dreaming can build new memory representations

- wiki 定义："a collection of pages written and maintained by Claude that gathers what Claude knows about one subject and links it to other notes"；链接为 Claude 提供检索记忆的地图。（原文此处链接 Karpathy LLM Wiki gist：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f ）
- **Stainless 语料**（Anthropic 5 月收购的软件公司内部文档，约 350,000 文件、约 420M tokens），25 题评测集，提供搜索工具。Opus 5 agents 经 128 次会话 dreaming：探索文件、写/改链接页面、合并重复、对照来源核验论断；各会话通过 **shared log** 协调、承接前序进度。
- 结果（图 10 alt，dreaming token 从 2M 增至 128M）：wiki only 13% → 48%；wiki + search 54% → 61%；search only（无 wiki）持平 53%。wiki + search 每题约省 20,000 tokens。早期 wiki 像新员工，越 dream 越像老员工。wiki 规模：2 次会话后 103 页 / 766 链接，128 次后 222 页 / 12,893 链接。
- 原文："we found that the wiki helped Claude the most when we also gave it access to a search tool."
- **Harvey LAB**（github.com/harveyai/harvey-labs）+ 一组并购文档：
  - 24 道并购问题，过半需跨多文档、许多需判断或计算：wiki 87% vs 仅搜索 73%。图 11 左 alt：24 条判分项多数关联 10 份文档中的 ≥2 份，9 条需判断或算术。
  - 另一 LAB 任务：判分项多可在单文档内文本搜索命中（图 11 右 alt：57 条判分项，多来自 deal overview memo），wiki 无明显增益。
  - 又一 LAB 任务：wiki 比原文还大。图 12 alt：语料 10 份文档 115 KB → wiki 68 页、255 链接、203 KB（**1.77 倍**），部分页面无链接。原文以 Borges《论科学的精确性》作比："an extremely detailed wiki that effectively abstracted nothing."

## Dreaming can promote notes up the memory hierarchy

- dreaming 可把笔记上浮到层级顶端，由 harness 在每次会话开始预加载（context injection），Claude 无需搜索甚至无需知道有东西可搜。
- 代价："Injected memories use up valuable tokens, and an incorrect note can be carried into every session." 加载也不保证被执行——文章引 Claude Code 文档称 "longer instruction files reduce adherence"。故顶层须保持小，dreaming 在此的主要工作是维持它小：把细节下移、留下链接。
- Claude Code auto memory 同理：不把全部 auto memory 载入，只载入 `MEMORY.md` 的**前 200 行或 25 KB**；这段头部充当索引，"shows Claude what it knows and where to find it"。

## Dreaming can focus memory on a specific goal

- 记忆的生长方向可按目标调校；如 Claude Duet 这类助理适合围绕所服务的人组织记忆。
- **合同条款任务**（LAB 模拟收购，判分看简报是否正确描述合同条款）：初始指令未说明 wiki 用途；建库时多个 agent 同时写一张共享条款表 → 简报只覆盖 **41/57（72%）** 事实。原因：共享表概括差、遗漏条款，"agents had overwritten one another's work"。图 14 alt：4 个 agent 写同一 `provisions.md`，一个的保存抹掉另一个的行。
- 改进方式：跑一个循环——Claude 反思失败、提出指令修改、重建 wiki；由此发现合同条款最重要并改写建库指令。新形态：**每份合同一页、单一 agent 撰写、逐字引用条款**，不再汇总成共享表 → **57/57（100%）**。

## Dreaming can fill in gaps a session leaves behind

- 单次会话写笔记只见本会话上下文；dreaming 可跨多会话找共同模式、修共同错误。
- 建 LAB wiki 时 Claude 有时链向尚未创建的页面。第二轮 dreaming：发现 9 条（来自 6 页）链向不存在的 `escrow-agreement`，改指向同一文档的已有页 `buyer-form-escrow-agreement`；新增 3 页（含 index）。图 15 alt：38 条目 / 225 链接 → 41 条目 / 278 链接。

## Thinking backward, looking forward（开放问题）

1. **何时创建记忆**：任务中写入能在源头捕捉 salience 并立即可用，但分散主任务注意力；dreaming 移到后台，但产出不能立即被用上。
2. **如何保持记忆可靠更新**：规则可能一开始就错，也会随环境漂移。dreaming 能修，但耗算力；持续检查全部记忆不现实，或应聚焦易变信息、按访问频率调节 dreaming 节奏。
3. **以 transcript 搜索为记忆底座**也合理；表示（wiki）+ 搜索有时有效，但维护表示需算力，并要防止累积错误与幻觉。
- 收尾："no model can really know what will happen in future turns"；"we still have a lot to learn about designing Claude's memory systems."
- 入门 cookbooks：dreaming（platform.claude.com/cookbook/managed-agents-cma-dreaming-with-a-dynamic-workflow）、knowledge wikis（github.com/anthropics/claude-quickstarts/tree/main/managed-agents/knowledge-wiki）。

## 文中外链（择要）

- 相关文章：Harness design for long-running application development（Anthropic Engineering，2026-03-24）；In-context learning and induction heads
- 文档：Managed Agents overview / memory / dreams；compaction；memory tool（platform.claude.com/docs）；Claude Code memory（code.claude.com/docs/en/memory）；Claude Duet 入门（support.claude.com/en/articles/17631495）
- 外部：sleep-time compute（arXiv 2504.13171）；CL-Bench 1.0；Harvey LAB；Karpathy LLM Wiki gist；Google SLEEP 框架博客；McClelland, McNaughton & O'Reilly 1995（互补学习系统）及若干 Nature / Science 神经科学文献
