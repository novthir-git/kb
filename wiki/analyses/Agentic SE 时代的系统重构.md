---
tags: [分析, AI, Agent, 软件工程, 重构, 架构, 方法论]
created: 2026-09-23
updated: 2026-09-23
sources:
  - "[[2026-09-23-agentic-se-refactoring-methodology-源摘要]]"
  - "[[2026-07-30-Thoughtworks-重构的经济收益-源摘要]]"
  - "[[2026-05-27-Boeckeler-可维护性传感器-源摘要]]"
  - "[[2026-04-02-Boeckeler-Harness-Engineering-源摘要]]"
  - "[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]"
  - "https://arxiv.org/abs/2603.13428v4 （Deng 等，EvoClaw / SWE-Milestone；检索于 2026-09-23）"
  - "https://www.isaqb.org/blog/ai-agents-dont-modernize-legacy-code-on-their-own/ （Markus Harrer 访谈，2026-05-18；检索于 2026-09-23）"
  - "https://addyo.substack.com/p/brownfield-agentic-engineering （Addy Osmani，2026-09-14；检索于 2026-09-23）"
  - "https://arxiv.org/abs/2504.09691 （Ziftci 等，Google，FSE Companion '25；检索于 2026-09-23）"
  - "https://martinfowler.com/articles/legacy-modernization-gen-ai.html （Thoughtworks，2024-09-24；检索于 2026-09-23）"
  - "https://code.claude.com/docs/en/best-practices （检索于 2026-09-23）"
  - "https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again （检索于 2026-09-23）"
  - "https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic （检索于 2026-09-23）"
  - "https://aws.amazon.com/blogs/migration-and-modernization/reimagine-your-mainframe-applications-with-agentic-ai-and-aws-transform/ （AWS，2025-12-15；检索于 2026-09-23）"
  - "https://every.to/guides/agent-native （Dan Shipper 与 Claude，2026-01-09；检索于 2026-09-23）"
  - "https://maintainable.software/agentic-engineering-part-2-agentic-codebase-principles/ （Salomon，2026-04-05；检索于 2026-09-23）"
  - "https://marmelab.com/blog/2026/01/21/agent-experience.html （Marmelab，2026-01-21；检索于 2026-09-23）"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents （Anthropic，2025-09-29；检索于 2026-09-23）"
  - "https://arxiv.org/abs/2405.15793 （SWE-agent，NeurIPS 2024；检索于 2026-09-23）"
  - "https://arxiv.org/abs/2604.04990 （Architecture Without Architects；检索于 2026-09-23）"
  - "https://arxiv.org/abs/2602.14690 （Galster 等；检索于 2026-09-23）"
---

# Agentic SE 时代的系统重构

> 起点：用户 2026-09-23 的多源调研稿（[[2026-09-23-agentic-se-refactoring-methodology-源摘要|逐项核验见源摘要]]），
> 加同批摄入的四篇一手文章。调研稿是二次综合产物，本页只采信核验过的部分，并在各处标明证据等级。

## 核心判断

1. **重构的目标函数扩展了**：代码库不再只是给人读的产物，也是 agent 的**运行环境**（OpenAI："瓶颈在环境而非
   模型"）。综合（沿用调研稿的判断，机制有一手支撑）：对人可维护与对 agent 可维护高度重合，但 agent 对
   **上下文经济性**远比人敏感——它每次变更都要把相关代码读进上下文、且每次从零开始（Thoughtworks 实验正是利用
   了"agent 不会学习"），也没有人带着的那套隐性 harness（Böckeler）。
2. **结构债可以按 token 计价**：Thoughtworks 的实验（本 wiki 所见的首个此类测量，单实验）里，同一变更的输入
   token 在重构后降了约 83%。这让"重构值不值"从审美争论变成了可以算回本期的投资问题。
3. **但 agent 不会自发偿还它**：重构的选题与发起必须是 harness 的显式职能（[[Agent 不会自发偿还结构债]]）。
4. **验证网是一切的前提**：无论是让 agent 执行重构，还是让它在长期演化中不引入回归，先有可自动运行的验证信号，
   才谈得上委派。持续演化基准里，agent 的失败集中在**防回归**而不是实现新功能。

综合：四条合起来，"为 agent 重构"的正确形态不是一次性的大扫除，而是一个**持续运行、按 token 计价、由 harness
驱动、被验证网兜住**的过程。

## 一、为什么目标函数变了：代码库是 agent 的运行环境

OpenAI 零手写代码实验的第一条结论是**瓶颈在环境而非模型**：早期进展慢是因为缺工具、抽象与内部结构；卡住时
要问"缺什么能力，怎样让它对 agent 可读且可强制执行"（[[2026-02-11-OpenAI-Harness-Engineering-源摘要]]）。
Böckeler 把代码库本身的可约束程度称为 **harnessability**：强类型、清晰的模块边界、能替 agent 屏蔽细节的框架，
决定了能给 agent 套上多完备的 harness（[[Harness Engineering]]）。

两者合起来，重构多了一层理由：

| 重构的传统理由（对人） | agent 时代新增的理由 |
|---|---|
| 降低理解成本 | 降低**每次变更的上下文成本**（token 与轮次） |
| 降低修改风险 | 提高**可被机械约束的程度**（类型、依赖规则、结构测试能覆盖多少） |
| 让设计意图可读 | 让设计意图**对 agent 可执行**（规则写进 linter、分层写进结构测试，而不只写进文档） |

OpenAI 的另一个判断把时间点也改了：人类团队常推迟到数百名工程师规模才引入的严格分层架构，**对 agent 是早期
前提**。综合：原因是 agent 的吞吐让一个小团队在几个月内产出了过去大团队才有的代码量（约 100 万行），架构
约束的收益随代码量增长，引入时点也随之前移。

## 二、结构债的经济学：一份测量

Thoughtworks（Giles Edwards-Alexander，2026-07-30）的实验设计很干净：利用"agent 不会学习"，每做完一步重构，
就让全新 sub-agent 重放**完全相同**的代表性变更，记录 token 后丢弃
（[[2026-07-30-Thoughtworks-重构的经济收益-源摘要]]）。

- **收益**：17,155 行的单文件经 15 步经典重构后最大文件降到 3,695 行，同一变更的输入 token 159,564 → 27,360
  （约 −83%）；数据访问层的代码总量只小幅下降（17,155 → 16,608 行），最终拆成 19 个文件。
- **机制**：节省来自 agent **能找到并只读所需的最小文件子集**。代码量没变，变的是读取路径。
- **成本**：未精确计量，上界 500 万 token（含计划与实验设计）。
- **没变的**（综合，从结果表读出）：输出 token 与耗时都没有下降——重构让 agent 读得更少，没让它写得更少，
  也没让单次变更更快（单次测量，噪声大）。作者结论却称实验显示了重构"在时间与金钱上的价值"，该矛盾已在
  [[2026-07-30-Thoughtworks-重构的经济收益-源摘要|源摘要]]用 ⚠️ 标注。

综合（回本估算，非原文）：若把 500 万 token 上界全按输入价计，约 38 次同类变更回本；真实数字取决于输出/输入
比例与缓存折扣，量级是"几十次"。这给出一个可操作的选题判据：**优先重构被 agent 频繁改动、且单次变更要读进
大量无关代码的热点**——改动频率决定复利次数，无关代码的体量决定单次收益。

这条经济学把重构接进了本 wiki 已有的成本框架：[[Uber-软件工厂的成本工程]] 把"agent 替自己多干的活"定义为浪费，
接地（上下文图谱）砍的是找信息的轮次，重构砍的是读信息的体量；[[Agent 工具上下文膨胀]] 的固定开销来自工具
schema，这里来自代码文件本身。

## 三、谁来发起：重构必须是 harness 的职能

三个来源同向显示 agent 不会自发**发起**重构（证据表见 [[Agent 不会自发偿还结构债]]；被明确分派后的**选题**质量则
证据分化）：Thoughtworks 的开发
harness 里写着显式重构步骤，却从未促使 agent 处理那个 17,155 行的文件；Böckeler 的经验是 agent 在第三、四次
重复时通常不会主动重构；OpenAI 观察到 agent 会复制仓库里已有的坏模式。

可用的驱动方式，按来源整理：

| 驱动方式 | 做法 | 来源 |
|---|---|---|
| 计算型 sensor + 自纠正信号 | 文件/函数长度、参数个数、复杂度、依赖规则；消息里写明怎么改；阈值可上调但不永久豁免 | Böckeler、OpenAI |
| 推理型周期评审 | 模块化评审 skill 定期跑、重要分析多跑几次；按影响半径分诊 | Böckeler |
| 定期垃圾回收 | 黄金原则编码为机械规则；后台任务扫描偏差、更新质量等级、发小而定向的重构 PR | OpenAI |
| 人选题、agent 执行 | 人或多个模型给出重构计划，限定为可证明保持正确性的编辑序列，每步可单独测试 | Thoughtworks |

综合：前三种解决"发现与发起"，第四种解决"选对题"（推理型评审也能给出候选，但非确定、需多跑）。执行质量随粒度分化——OpenAI 的小 PR 多数一分钟内审完并
自动合并；Thoughtworks 的 15 步大重构里，价值最大的一步（拆分 store）首轮被漏掉，靠全程唯一一次人工重新引导
才补做。**默认把重构切成小而
定向的步骤**，是目前证据下最稳的做法。

## 四、验证网先行

验证网在三个层面上是前提：

- **让 agent 能安全执行重构**：Thoughtworks 的每一步都可单独测试、也都单独测过（原文称这比多数人类工程师的
  做法更严格）。综合：这很可能是它能 8 小时基本无人值守的条件之一。
- **让 sensor 的"绿"可信**：Böckeler 的实验里，一个语句覆盖 100% 的文件没有任何单元测试，变异测试报出 13 个
  存活变异体。测试也由 AI 写时，覆盖率门禁要配变异测试（[[AI编码技术债的三层治理]]）。
- **让长期演化不崩**：Deng 等的持续演化基准（EvoClaw，现名 SWE-Milestone，arXiv 2603.13428）显示，agent 在
  "每个里程碑都从标准快照起步"的独立设置下得分可超过 80%（这一水平部分是构造基准时反复修订需求规格、直到
  前沿模型能解出而校准出来的，用来证明单个任务可解），在持续演化设置下最佳组合只有约 38%（综合得分，
  非成功率），按完全解决计最高约 13%；失败集中在**防回归**，错误沿依赖链滚雪球。**适度而有纪律**的测试验证
  得分最高（验证过度同样偏低），"频繁改同一文件却很少跑测试"的盲目试错表现最差。

综合：这组证据把"验证优先"从一条工程格言变成了可观察的机制——**agent 在长期演化中缺的不是写新功能的能力，
而是不破坏旧功能的能力**，而后者正是验证网提供的东西。

两条约束，防止"验证优先"走样：

- **约束结果，不规定过程。**Böckeler 2026-08-10 的小样本评估里，要求 agent 在自己的循环里做 TDD 没带来可见收益，
  她改用变异测试直接衡量回归测试的质量（[[Specification-Driven Development]] 有展开）。
- **推理型验证会制造噪音。**Claude Code 官方最佳实践提醒：被要求找缺口的 reviewer 通常总能报出一些，追逐每条
  发现会导致过度工程，应只标记影响正确性或需求的缺口；确定性的 Stop hook 门禁也会在连续拦截 8 次后被强制放行。
  Osmani 的对策是把举证责任放回作者：PR 附可运行的证据，而不是加大 review。

## 五、遗留系统：最需要 harness 的地方最难建 harness

Böckeler 的这句话（[[Harness Engineering]]）是遗留重构的出发点：没有测试、边界模糊、弱类型的代码库，恰恰最难给
agent 套上约束。调研稿给出的方法框架经回查后，主要出自 Markus Harrer（INNOQ，iSAQB 博客 2026-05-18 的访谈），
并且调研稿引的 awesome 清单也由他维护——**这一段不是"多来源共识"，而是 Harrer 一人的方法**。独立佐证来自
Osmani、Google、AWS 与 Thoughtworks。

| 方法 | 做法 | 出处与证据等级 |
|---|---|---|
| 先缩小范围 | 能用标准软件替代、外包或删掉的，先不现代化——Harrer 转引 Scott Hanselman 的老话 "The less you do, the more of it you can do" | Harrer（观点）；Thoughtworks 与 AWS 都有识别死代码、未用作业再决定退役的环节 |
| 先铺 characterization tests | 用代表性输入录下现有系统的输出，改完再比对（Harrer）；"丑陋"的现有行为也要锁住，因为业务可能正依赖它（Osmani 补充） | Harrer；Osmani（2026-09-14）独立主张同一做法 |
| 用 seam 给 agent 划沙箱 | 给 agent 一个清晰的接缝，它就不必理解整个系统，跨代码库的意外改动大幅减少 | Harrer（观点） |
| 人画地图，按区授权 | 绿区（测试好、隔离好）agent 紧循环；黄区先补 characterization tests；红区（鉴权、计费、权限）人逐步结对或不做。**地图由人画**，否则 agent 会从"名字最有意思"的最危险文件开始；区域要"挣"来升级 | Osmani（实践者观点） |
| 确定性与非确定性混合 | "guided AI"：LLM 只改分析脚本事先确定性圈定的位置；或让 AI 生成代码转换 recipe，再由确定性工具执行。"Agents provide speed, guardrails provide accuracy" | Harrer（观点） |
| 先理解再重写 | Thoughtworks CodeConcise：AST 知识图谱 + LLM 做逆向工程、提取业务规则，由领域专家校验，重写仍由团队完成 | Thoughtworks 2024-09（提效数字是 PoC 估算） |
| 警惕"modern legacy" | 只在代码层现代化、业务流程照旧，得到的是被 agent 打磨过的新遗留系统 | Harrer（观点） |

**工业级数据**只有一份：Google 的 LLM 迁移（Ziftci 等，FSE 2025 Companion）。3 名开发者 12 个月完成 39 次同类的
32→64 位 ID 迁移，提交 595 个变更；74.45% 的变更由 LLM 生成（按字符编辑量计 69.46%），但**无人改动的纯 LLM 变更
只占约 36%**；每个变更都经开发者目视核查和代码所有者审批；"省约 50% 时间"是这 3 位开发者的主观估计，没有实测
工时。它支持"人机混合 + 自动校验 + 人审"的流水线在机械迁移上可行，不支持"agent 自主完成现代化"。

**campaign 式批量执行**的两个公开案例（Osmani 转述，厂商口径）：Bun 的 Zig → Rust 移植约 50 个 workflow、11 天、
53.5 万行，每个生成单元配两个对抗性 reviewer、以全部既有测试为合并门禁，且在任何 agent 开跑前先花数小时写了
Zig 到 Rust 的惯用法对照指南；Asana 两周清掉多年的 Enzyme 积压，模型与基础设施成本约 1.2 万美元（这是生成的
账单，不是对照过的节省）。可迁移的共同点：**变更是机械的、既有测试套件完整、人仍审每个变更**。Claude Code 的
`/batch`（v2.1.63 起）把同一模式产品化：拆成 5–30 个独立单元、人批准计划、每单元在独立 worktree 里实现并开 PR。

> 综合：批量改动可以按"定位是否确定 × 改写是否确定"分成三种形态——
> - **LLM 拆分 + LLM 改写**：`/batch`、Bun，靠既有测试套件与对抗性 reviewer 兜底；
> - **确定性定位 + LLM 逐处改写**：Google 的迁移（Kythe 找引用、LLM 改每个文件、逐变更自动校验与人审），
>   也就是 Harrer 说的 guided AI；
> - **LLM 产出确定性转换 + 工具执行**：Harrer 的 code transformation recipe。
>
> 变更越机械、越可枚举，越该往后一种靠：确定性工具的输出可以整体验证，LLM 的逐处改写只能逐处验证。

认知债在遗留系统里尤其危险：agent 只掌握外化的知识，快速改码会侵蚀团队对系统的共享理解。该概念出自
Margaret-Anne Storey（ACM Queue 2026），Harrer 把它用到了现代化场景，治理方式见 [[AI编码技术债的三层治理]]。

## 六、思想光谱（按核验结果校正）

调研稿把 2025–2026 年的思想画成一条轴：一端是"意图 / spec 成为一等公民、代码可再生"，另一端是"代码与工程判断
仍是责任落点"。回到一手来源后，几个代表的位置都要挪（逐条依据见
[[2026-09-23-agentic-se-refactoring-methodology-源摘要|源摘要]]）：

| 代表 | 调研稿的站位 | 核验后的站位 |
|---|---|---|
| Karpathy（Software 3.0，2025-06） | 激进端 | **范式判断激进、工程实践审慎**："keep the AI on the leash"、人类验证者是瓶颈、"decade of agents"而非"year of agents"。他还举了自己的 MenuGen："the code was actually the easy part"，认证、支付、部署花了一周 |
| AaaS 论文（arXiv 2606.05608） | 激进重构派 | 单作者预印本、无自有实验。v1 题为《The End of Software Engineering》；**6 天后的 v2 撤回"终结"、改称"扩展"软件工程**，但仍坚持 AaaS 是"逻辑终点"；人仍是 outcome auditor |
| Tessl（spec-as-source） | spec 是新源代码 | 2025 年私测时在**探索** spec-as-source——人只编辑规格，代码由规格再生成并标注 "GENERATED FROM SPEC - DO NOT EDIT"（三层级见 [[Specification-Driven Development]]）；2026-09 首页已转型为 agent enablement 平台 |
| Every agent-native | 可抛弃派 | 讲的是**应用架构**而非代码库：功能不是写死的代码，而是用 prompt 描述的结果，由 agent 用原子工具在循环里完成。五条原则（不是三条）：Parity（用户能在界面上做的，agent 都能用工具做到）、Granularity（工具是原子原语，判断留给 agent；检验标准是"改行为时改 prompt 还是重构代码"）、Composability（新功能只需写新 prompt）、Emergent capability（agent 能完成没专门设计过的任务，高频模式再固化为专用工具）、Improvement over time（靠积累的上下文与 prompt 迭代改进，不必发版）。高频操作可"毕业"为代码以提效；agent 自改 prompt 或代码需审批门、检查点与回滚。多处标注为 Claude 贡献、作者尚未背书 |
| Yegge（CHOP，2024-06） | 可抛弃派 | 不在此光谱内：预测的是代码由 LLM 写，不是代码可抛弃 |
| Doctorow（Code is a liability，2026-01） | 负债派 | 成立；"10,000 倍"是修辞，乘法衰减针对的是个人助理 agent |
| Böckeler（Thoughtworks） | 系统性泼冷水 | **按风险校准审查**（影响、概率、可检测性），认可 spec-first，低风险高可检测时接受 vibe coding |

综合：调研稿说"两端共同承认"生成成本趋零后验证成为稀缺资源（它原话还包括规格化与治理）。这一点在审慎一端有
多条一手支持，口径各异：Karpathy 说在审 10,000 行 diff 时"I'm still the bottleneck"；Osmani 说瓶颈移到了"证明代码
能用"；Sonar 2026 调查中 96% 的受访者不完全信任 AI 代码，但坚持每次都检查的不到一半；Anthropic 内部调查里超过一半
的人能完全委派的工作只占 0–20%；SWE-Milestone 显示 agent 缺的是系统级维护能力。激进一端对此的承认较弱——AaaS
把人定为 outcome auditor，但断言差距"非根本性"。

> 综合：激进一端的代表在**工程实践**上普遍后撤到"人仍在验证环"——AaaS v2 撤回"软件工程终结"的标题、把人定为
> outcome auditor，Karpathy 主张 "keep the AI on the leash"，Tessl 转向 agent enablement 平台——但范式层的激进
> 判断仍在（AaaS 仍称自己是"逻辑终点"）。所以与其说这是两派之争，不如说是**实践层向"验证是瓶颈"的收敛**；真正悬而未决的不是"代码还重不重要"，而是**在 agent
> 吞吐下由谁、用什么来验证**。本页与 [[Harness Engineering]] 的答案是：确定性 sensor 管局部、推理型评审管跨文件、
> 人管选题与高风险区。

## 七、重构的优先级顺序（修订版）

调研稿 §5.3 的顺序是：先铺验证网 → 再建 agent 接口层 → 再做边界重构 → 最后才是批量 campaign，并判断"跳过前两步
直接放 agent 进遗留系统是最常见的失败模式"（这句判断调研稿未给出处）。综合：这个顺序与 Harrer（characterization
tests 先行）、Osmani（其文中有"Parallelize last"一节）等来源方向一致，但没有被当作整体独立核验过。本 wiki 的修订版
补了一个起点和一个终点（下表整体是综合推断）：

| 步骤 | 做什么 | 依据 | 进入下一步的条件 |
|---|---|---|---|
| 0. 度量与缩范围 | 选几个代表性变更，记录输入 token 与改动文件数；先砍掉不必现代化的部分 | Thoughtworks 的计价法；Böckeler 的"小改动要改的文件数"信号；Harrer 的缩范围 | 知道热点在哪、基线是多少 |
| 1. 验证网 | characterization tests、CI 门禁；AI 写测试时配变异测试 | Harrer、Osmani、Böckeler、SWE-Milestone | 热点区域的行为被锁住 |
| 2. agent 接口层 | 短入口文件做地图（只写推断不出的约定），深层文档按需加载；统一命令入口；依赖与分层规则写成 linter | OpenAI；ETH 评测（仓库概览无益、成本 +20%）；Claude Code 修剪判据 | 规则能机械执行，而不只是写在文档里 |
| 3. 边界重构 | 人画区域图、划 seam；按 agent 的读取路径拆热点大文件、去重 | Osmani 的区域；Harrer 的 seam；Thoughtworks 的 −83% | 代表性变更的 token 与文件数下降 |
| 4. 批量 campaign | 小而定向、每单元可独立测试；机械变更优先走确定性转换 | `/batch`、Bun、Google、Harrer 的 recipe | 既有测试全绿、人审每个变更 |
| 5. 持续偿还 | 定期 GC 任务、周期性推理型评审、阈值上调可见 | OpenAI、Böckeler | ——（不结束） |

> 综合：第 5 步是这个顺序与传统"重构项目"的根本区别。在 agent 吞吐下结构债持续产生，而 agent 不会自发偿还
> （[[Agent 不会自发偿还结构债]]），所以重构不能是一次性项目，必须是 harness 里一个一直在跑的职能。

## 八、争议与开放问题

| 问题 | 现状（2026-09-23） |
|---|---|
| spec 是否是新的源代码 | 旗手是 2025 年的 Tessl（已转型）；GitHub 的 Spec Kit 方法论文档在理念上接近 spec-as-source，但工具实际形态是 spec-first，其持久化文档另列三种变更模型并声明都不是默认；Böckeler 担心 spec-as-source 兼有僵化与非确定性。SDD 的收益证据见 [[SDD 收益主张的实证赤字]] |
| 规则 / 上下文文件写多详尽 | 形态已收敛为"常驻入口极简 + 深层按需加载"；但效果证据相互矛盾——ETH 测得成本 +20% 且不提升成功率，Lulla 等测得 Codex 运行时间 −28.64%；McMillan 在 25–500 行内未测到文件大小影响指令遵循，与官方"膨胀导致忽略"的说法相左（两处 ⚠️ 矛盾标注见 [[AI编码技术债的三层治理]]） |
| 人能否退出验证环 | 没有一手来源支持"现在"退出：AaaS 也只在 2028 年以后的愿景阶段让人退到元治理层；Google 每个变更都人审 |
| agent 该不该在循环里做 TDD | 目前唯一的评估（Böckeler，小样本）显示无收益甚至略差；需要更大样本 |
| 重构粒度与执行质量 | OpenAI 的小 PR 顺利、Thoughtworks 的 15 步大重构粗糙；缺同仓库对照 |
| 结构债的回本点 | 只有一个实验、一种变更；换一种变更类型、换一个模型，−83% 能保持多少，未知 |

调研稿 §4 表中"模块化单体 vs 微服务"一行没有给出处，本次核验未覆盖，暂不采信。

## 九、改成什么样：agent 友好代码库的目标形态

§一给了重构的新理由，这里是重构要达到的形态。材料来自调研稿 §2，按核验结果收窄（逐条依据见
[[2026-09-23-agentic-se-refactoring-methodology-源摘要|源摘要]] §2 与 Anthropic 专项）。Salomon 给的判据可以当总目标：
好的代码库应"让一个不熟悉的 agent 找到正确上下文、做窄变更并验证，而无需把整个系统装入工作记忆"。

| 形态 | 做法 | 出处与证据等级 |
|---|---|---|
| 上下文经济性 | 小而内聚的文件；目录浅而可预测、按领域命名（Salomon 主张"领域顶层 + 用例切片"两级，优于纯扁平）；避免缩写与重名（Marmelab 称"代码 SEO"）。Salomon 的五项特征：Locality、Blast radius、Boundary integrity、Navigability、Rebuild/test scope。上下文是有限资源、性能随长度逐渐下降（context rot），Anthropic 推荐**混合**策略：少量内容常驻，其余按需检索；长任务靠 compaction、外置笔记、子 agent 回传摘要 | Salomon、Marmelab（实践者观点）；Anthropic（2025-09-29，厂商工程文章）；收益的测量见 §二 |
| 显式契约 | 强类型让接口自带文档；显式边界防止 agent 推断出错误契约；消除全局状态、时序耦合、语义耦合（Salomon 列了六类有害耦合）；抵制过早抽象。在 ARCHITECTURE.md 里点名众所周知的模式，agent 就不必读实现 | Salomon（观点）；点名模式一条是 Marmelab 与 Deska 的经验之谈，未见实证，且 ARCHITECTURE.md 这一惯例本身强调简短 |
| 给 agent 读的文档 | 常驻入口极简、深层按需加载：OpenAI 约 100 行的 AGENTS.md 指向结构化 `docs/`；Anthropic 让 CLAUDE.md 只写删掉就会出错的内容，按场景才需要的知识放进 skills；Marmelab 用短入口加就近嵌入的文档。统一命令入口、自文档化 CLI、ADR 也是 agent 的接口。AGENTS.md 与 CLAUDE.md 并存（2,586 个有上下文文件的仓库里 CLAUDE.md 45.9%、AGENTS.md 39.5%；Claude Code 自 2026-09-18 起在无 CLAUDE.md 时读 AGENTS.md） | 形态上三方同向；**效果**证据相互矛盾（ETH vs Lulla、McMillan vs 官方说法，见 [[AI编码技术债的三层治理]]） |
| 为 agent 设计接口（ACI） | SWE-agent 把 LM agent 当作一类新的终端用户，四条原则：动作简单、动作紧凑、反馈充分而简洁、护栏阻断错误传播；相对 shell 基线提升 10.7 个百分点（绝对 pass@1 12.5%）。可操作的错误信息、省 token 的输出，另见 Anthropic《Writing effective tools for AI agents》（2025-09） | SWE-agent（NeurIPS 2024，基准测量） |
| prompt 也是架构制品 | 开发者用自然语言描述需求时，agent 数秒内做出框架选择、基建与集成决策，本质是无人评审的架构决策（vibe architecting）。示意：只改 prompt，代码量 141 → 827 行（5.9 倍），依赖图与故障模式随之改变。主张在代码评审**之外新增**一层架构评审，审 prompt 规范与 agent 做出的架构决策 | arXiv 2604.04990（position paper；三个 prompt 各跑一次、单一工具，作者自称示意） |

"代码库比堆 MCP / 子 agent 更根本"不作为结论采信：只有 Marmelab 接近原话，Anthropic 把表现归因于整个 harness 并推荐子
agent 架构；它可取的部分是"基础先于工具"——Anthropic 2026-05-14 的大型代码库文章把"基础没做好就先接 MCP"列为常见错误。

> 综合：五条形态对应 §一的三条新理由——降低上下文成本 → 上下文经济性；提高可被机械约束的程度 → 显式契约；让设计意图
> 对 agent 可执行 → 给 agent 读的文档、ACI 与 prompt 评审。它们大多是老原则，新的是 agent 对上下文成本敏感得多
> （核心判断 1）。ACI 的"反馈充分而简洁"与 [[Harness Engineering]] 的"sensor 信号要写明怎么改"是同一条原则。

## 证据边界

- **一手实验都是单点**：Thoughtworks（单实验、单开发者、greenfield、每步只测一次）、Böckeler（单人单应用、无对照）、
  OpenAI（公司自述、无对照，且被指缺少功能与行为验证）。
- **唯一的大样本基准**是 SWE-Milestone（98 个里程碑、12 个模型），它测的是功能演化而不是专门的重构。
- **唯一的工业级迁移数据**是 Google（3 名开发者、同一类迁移、时间节省是自估）。
- 遗留系统的方法框架主要出自 Harrer 一人，Osmani 是较独立的佐证；campaign 案例的数字来自厂商或转述。
- 本页的回本估算、"三种批量形态"、"实践层向验证收敛"与修订版六步顺序表都是本 wiki 的综合推断；核心判断 1
  的"agent 对上下文经济性远比人敏感"沿用自调研稿，只有机制层面的一手支撑。
- 置信度（对外引用时标注）：回本量级为**低**（分子分母口径不同，只到"几十次"）；其余综合推断为**中**——核心判断 1 的
  程度、架构约束时点前移、选题判据、驱动方式分工与"默认小步"、古德哈特形态、验证网是无人值守的条件、"缺的是不破坏
  旧功能的能力"、三种批量形态、实践层收敛、六步顺序、"重构必须是持续职能"、§九"五条形态对应三条新理由"。依据即以上几条证据边界。
- §九的做法多为实践者观点；有测量支撑的只有 ACI（SWE-agent 基准）与上下文经济性的收益（§二，单实验）。

## 关联

- 框架：[[Harness Engineering]]
- 论点：[[Agent 不会自发偿还结构债]]
- 成本：[[Uber-软件工厂的成本工程]]、[[Agent 工具上下文膨胀]]
- 债务模型与门禁：[[AI编码技术债的三层治理]]
- 文档作为运行时输入：[[代码与文档漂移的本质]]
- 规格：[[Specification-Driven Development]]、[[SDD 收益主张的实证赤字]]
- 落地节奏：[[agent-生产级落地的鸿沟]]
