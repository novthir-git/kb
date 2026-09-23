# AI Agentic SE 时代的系统重构:思想与方法论调研——用户调研稿

> 类型：用户提供的多源调研稿（二次综合产物，非一级来源）  
> 原始位置：用户本机 cowork-space 工作区，文件名 `agentic-se-refactoring-methodology.md`（原文标注调研日期 2026-09-23）  
> 收录日期：2026-09-23  
> 说明：本文件按用户原始输入存档，未做事实校正；首行标题并入本标题，其余内容逐字保留。
> 入库时已抽查 7 条关键引用：1 处归属错误（EvoClaw 并非 AaaS 论文自建基准，实为 Deng 等 arXiv 2603.13428，
> 现更名 SWE-Milestone），3 处引用失准（arXiv 2601.20404 挂错论断；Anthropic「0–20%」丢失"超过一半受访者"
> 限定、一手来源为 2025-12-02 研究文章；Google「省约 50%」为开发者自估）；§5.1「被自己的基准证伪」随归属错误
> 不成立。其余引用未核验。逐项核验待写入 [[2026-09-23-agentic-se-refactoring-methodology-源摘要]]（待写）。
> 正式沉淀前须回查一级来源。

---

> 调研日期:2026-09-23 · 侧重:范式层思想 + 架构与重构方法论

## 0. 一句话综述

2025–2026 年的思想光谱可以画成一条轴:一端主张「意图/spec/prompt 成为一等公民,代码降格为可再生的中间产物」(Karpathy Software 3.0、AaaS、spec-driven、agent-native);另一端坚持「代码与工程判断仍是责任与风险的落点」(Böckeler/Fowler、Doctorow、review-bottleneck 论者)。两端共同承认的事实是:**生成成本趋零之后,验证、规格化与治理成为新的稀缺资源**。相应地,系统重构的目标函数也变了——从"对人可维护"扩展为"代码库本身是 agent 的运行环境与接口"。

---

## 1. 范式层:五条思想主线

### 1.1 Software 3.0(Karpathy)

Karpathy 在 2025 年 YC AI Startup School 演讲中提出三代框架:1.0 是人写的显式代码,2.0 是神经网络权重,3.0 以 LLM 为运行时、自然语言 prompt 为程序("最热门的新编程语言是英语")。三个关键主张:

- **LLM as OS**:LLM 兼具公用事业、芯片厂、操作系统三重属性,当前形态类似 1960 年代分时主机。
- **部分自主 + autonomy slider**:LLM 是"people spirits",有幻觉与缺乏自知等认知缺陷,最佳产品形态是 Iron Man 战衣式增强而非全自主,依赖紧凑的 generate–verify 循环。
- **Build for agents**:agent 成为与人(GUI)、程序(API)并列的第三类信息消费者,需要 llms.txt、机器可读文档等专属通道。

### 1.2 Agentic Software / AaaS(arXiv 2606.05608)

该论文是"激进重构派"的代表:传统软件 S=(算力, 静态决策规则, 执行环境) vs. agent 系统 A=(LLM 推理引擎, 工具集, 记忆, 规划)——决策逻辑从"预先编码"变为"运行时生成"。它把 Software 3.0 定义为 **Agent-as-a-Service**(按结果计费),否定"AI 辅助开发"的中间形态,主张从业者转型为 intent architect。但其自建基准 EvoClaw 反而暴露了要害:agent 在孤立任务成功率 >80%,在**持续演化场景骤降至 ≤38%**(上下文漂移、错误传播、无法建模技术债)——恰恰说明"系统长期演化"才是 agentic SE 尚未攻克的部分,这也是本调研关注重构方法论的原因。

### 1.3 Spec-driven Development(SDD)

- **主张方**:GitHub Spec Kit(constitution → specify/plan/tasks)、Amazon Kiro(Requirements → Design → Tasks)把"先写规格"制度化;Tessl 追求 spec-as-source——代码标注 "GENERATED FROM SPEC - DO NOT EDIT","spec 是新的源代码"。
- **批评方**:Böckeler 在 martinfowler.com 区分 spec-first / spec-anchored / spec-as-source 三个层级,并系统性泼冷水:单一重流程不适配问题尺度、"我宁愿 review 代码也不愿 review 一堆 markdown"、agent 经常无视或过度解读 spec;与 2000 年代 Model-Driven Development 的失败历史平行——SDD 甚至叠加了"僵化 + 非确定性"两种缺陷。

### 1.4 代码可抛弃 vs. 代码是负债

- **可抛弃派**:agent-native 阵营认为代码可再生,prompt/spec 才是持久资产;Yegge 预测 LLM 对话可能成为"源代码的常态"。
- **反方**:Doctorow《Code is a liability (not an asset)》——代码随外部世界变化不断累积义务,AI 能"写代码"但不能做"软件工程";产出 10,000 倍代码等于同规模制造负债("往技术社会的墙里铲石棉");多 agent 链条的可靠性按乘法衰减。Ken Huang 补充安全视角:代码可抛弃,但其副作用(数据、权限、漏洞)是持久的。

### 1.5 实践观察式怀疑(Fowler / Thoughtworks)与验证瓶颈

Böckeler 的 "Exploring Gen AI" 系列呈现一条清晰路线:开发者技能不降反升 → 全自主 agent 只适合小而可验证的任务 → context engineering、harness engineering、TDD inside the agent loop。纲领性论点(《I still care about the code》):**LLM 不是编译器而是推断器(inferrer)**,输出是概率性的、幻觉是机制内生的;开发者必须按 影响 × 概率 × 可检测性 持续做风险评估("今晚 on-call 的你,敢部署没读过的 1000 行变更吗")。与之呼应的共识是 **"review is the bottleneck"**:生成不再稀缺,验证成为新瓶颈;调查甚至显示"多数开发者不信任 AI 代码但也不检查它"——信任与验证双重失灵。相关论述还有 Yegge 的 CHOP(chat-oriented programming)悖论:chat 对资深者比对初级者更安全,因为 senior 能识破 LLM 貌似有理的坏设计;以及 Every/Dan Shipper 的 agent-native 三原则(Parity / Granularity / Improvement over time),检验标准是"agent 能否完成你从未显式构建的功能"。

---

## 2. 架构方法论:代码库成为 agent 的环境,四大支柱

多个独立来源(Maintainable Software、Marmelab、Deska、Anthropic)在 2026 年收敛到同一判断:**agent 表现差异的根源在代码库本身,设计良好的代码库比堆 MCP/子 agent 更根本**。共识可归纳为四大支柱:

### 2.1 上下文经济性(context economy)

- 小而内聚的模块与文件;扁平、可预测、语义化的目录结构;避免缩写与重名("代码 SEO")。
- Anthropic 的机制解释:上下文是有限资源(context rot,注意力 n² 约束),因此 just-in-time retrieval 优于预加载,长任务靠 compaction、外置笔记(NOTES.md)、sub-agent 压缩回传。
- Maintainable Software 的判据:好的代码库应"让一个不熟悉的 agent 找到正确上下文、做窄变更并验证,而无需把整个系统装入工作记忆"——七特征:Locality、Blast radius、Boundary integrity、Navigability、窄 rebuild/test scope、Cohesive modules、Ownership-aligned boundaries。

### 2.2 显式契约(explicit contracts)

- 强类型(TS/Go/Rust/type hints)让 API 自文档化;显式边界防止 agent 推断错误契约;消除全局状态、时序耦合、语义耦合;抵制过早抽象。
- ARCHITECTURE.md 点名设计模式(Hexagonal、MVC)可激活模型预训练知识——这是"为 agent 写架构文档"特有的技巧。

### 2.3 机器可消费的文档(docs as interface)

- AGENTS.md 已成跨工具事实标准(OpenAI/Google/Cursor 采用),CLAUDE.md/.cursorrules 是厂商变体;实践形成分层:仓库级 → 目录级 → skills 按需加载,已有实证研究(arXiv 2601.20404)。
- 文档从"给人看的说明"变为 agent 的 API:ADR、自文档化 CLI、Makefile 统一入口都算。
- 粒度存在争议:Anthropic 与 Marmelab 警告文档膨胀反噬(CLAUDE.md 只写"删掉会出错"的内容);另一派主张详尽的 .ai-context 目录。未有定论。

### 2.4 验证优先(verification-first)

- 多来源收敛的新原则:系统应围绕"agent 可自动运行的验证信号"来设计——可快速运行的窄范围测试、lint/typecheck/hooks 作为确定性护栏、CI 门禁、OS 级沙箱。
- Anthropic 把"给 agent 可运行的验证"视为"看守式会话"与"可离开会话"的分水岭;验证可升级为 Stop hook 确定性门禁、对抗性 review subagent、Writer/Reviewer 双会话。
- 总原则:**把非确定性的 agent 包在确定性护栏内**——"AI 提供速度,护栏保证正确"。

**关键洞见**:对人可维护与对 agent 可维护正在收敛,但 agent 对上下文经济性远比人敏感。另一个新架构关注点是 **ACI(Agent-Computer Interface)**,源自 SWE-agent(NeurIPS 2024):为 agent 设计的工具/API 是一门 UX 学科,只是用户是模型——错误信息要可操作、输出要省 token、操作要幂等。

### 2.5 一个被忽视的治理问题:vibe architecting

arXiv 2604.04990《Architecture Without Architects》指出:开发者用自然语言描述需求时,agent 数秒内完成框架选择、基建搭建、集成决策——本质是架构决策却无人评审。案例:仅改 prompt 使聊天机器人代码量增长 5.9 倍(141→827 行),依赖图与故障模式随之改变。结论:**prompt 规范本身是架构制品,应纳入架构评审**。治理重心从"审代码"转向"审 prompt / 审架构决策"。

---

## 3. 遗留系统重构的操作方法论

### 3.1 反对"按钮式现代化"

iSAQB(Harrer)的核心论点:企业代码充满 agent 无法获取的隐性领域知识,agent 不会自己完成现代化。两个重要警告:

- **认知债/意图债**:agent 只知外化知识,快速生成会侵蚀团队对系统的理解;
- **"现代遗留"陷阱**:只在代码层现代化,业务流程照旧,等于制造新的遗留系统。

### 3.2 可操作的方法框架(多来源共识)

1. **Characterization tests 先行铺网**:先记录既有系统的输入输出行为,给 agent 机器可读的回归反馈,再动手改。
2. **Seams(接缝)限定干预点**:给 agent 沙箱化的爆炸半径,与 strangler fig 结合——agent 加速新旧并行期的封套与迁移。
3. **理解优先于重写**:Thoughtworks CodeConcise 路线——先用 LLM+图谱做逆向工程、提取业务规则,再重写。
4. **Campaign 式批量执行**:先在 2–3 个文件上调好 prompt,再全量 fan-out(Claude Code 的 `/batch`、循环 `claude -p`);小步 PR + ratchet 式渐进收紧。
5. **人始终在验证环**:Google 的工业级数据(FSE 2025):定位→LLM 生成→验证三阶段,12 个月 39 次迁移、93,574 处编辑,LLM 生成占约 70–74%、省约 50% 时间——但人工审查从未退出。AWS Transform 的主机现代化同样是 agentic + 人在环。

### 3.3 规模化的现实基线

Anthropic 2026 趋势报告:工程师 60% 的工作用 AI,但**能完全委派的仅 0–20%**;角色从实现者转向 agent 编排者,新技能重心是系统架构、质量评估、问题分解。这与 EvoClaw 的 ≤38% 演化场景成功率互相印证:全自动重构目前不成立,方法论的本质是**把重构任务分解到 agent 可靠区间内,并用验证网兜住**。

---

## 4. 争议与开放问题

| 问题 | 一方 | 另一方 |
|---|---|---|
| spec 是否是新源代码 | Tessl/Spec Kit/Kiro:spec-as-source | Böckeler:重演 MDD 失败,且更糟(僵化+非确定性) |
| 代码的地位 | 可抛弃、可再生的中间产物 | 负债的载体,副作用持久,必须被理解 |
| 单体 vs 微服务 | 模块化单体(vertical slices)上下文集中,对 agent 友好 | 小服务天然限定 blast radius,适合并行多 agent |
| 文档粒度 | 详尽 .ai-context | 极简 CLAUDE.md,能推断的不写 |
| 人可否退出验证环 | AaaS:agent→result 直达 | Google/Anthropic 数据:完全委派比例仍低;iSAQB:业务层重思无法委派 |

## 5. 我的综合判断

1. **最可靠的不变量是"验证优先"**。所有严肃的工业实践(Google、Anthropic、iSAQB、Thoughtworks)都收敛于此;而所有激进主张(AaaS、纯 vibe coding)在长期演化场景都缺乏数据支撑,甚至被自己的基准证伪。做重构决策时应以此为锚。
2. **"为 agent 重构"与"好的软件工程"高度重合但不等价**。模块化、显式契约、测试网是老原则;真正新增的是上下文经济性、机器可消费文档、ACI、prompt 纳入架构评审——这些值得写进架构规范。
3. **重构的优先级顺序**:先铺验证网(characterization tests + CI 门禁),再建 agent 接口层(AGENTS.md/ARCHITECTURE.md/统一命令入口),再做边界重构(seams、vertical slices),最后才谈批量 agent campaign。跳过前两步直接放 agent 进遗留系统,是当前最常见的失败模式。
4. **警惕认知债**。团队对系统理解的流失是 agentic 重构特有的新型风险,值得与技术债并列管理。

---

## 参考文献

**范式层**
- Karpathy, Software Is Changing (Again): http://ikyle.me/blog/2025/andrej-karpathy-software-is-changing-again
- Agentic Software (AaaS 论文): https://arxiv.org/html/2606.05608v2
- Böckeler, Understanding Spec-Driven-Development: https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Böckeler, I still care about the code: https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html
- Exploring Gen AI 系列索引: https://martinfowler.com/articles/exploring-gen-ai/
- Doctorow, Code is a liability: https://pluralistic.net/2026/01/06/1000x-liability/
- Ken Huang, Disposable Code, Durable Side Effects: https://kenhuangus.substack.com/p/disposable-code-durable-side-effects
- Yegge, The Death of the Junior Developer: https://sourcegraph.com/blog/the-death-of-the-junior-developer
- Shipper, Agent-native Architectures: https://every.to/chain-of-thought/agent-native-architectures-how-to-build-apps-after-the-end-of-code
- Osmani, Vibe Coding: https://addyo.substack.com/p/vibe-coding-revolution-or-reckless
- Osmani, Code Review in the Age of AI: https://addyo.substack.com/p/code-review-in-the-age-of-ai
- The Register, 开发者不信任也不检查 AI 代码: https://www.theregister.com/2026/01/09/devs_ai_code/
- SDD 工具综述: https://intuitionlabs.ai/articles/spec-driven-development-spec-kit

**架构与方法论**
- Salomon, Agentic Codebase Principles: https://maintainable.software/agentic-engineering-part-2-agentic-codebase-principles/
- Marmelab, Agent Experience: https://marmelab.com/blog/2026/01/21/agent-experience.html
- Deska, Agent-Friendly Codebase: https://deska.dev/blog/agent-friendly-codebase
- Architecture Without Architects (vibe architecting): https://arxiv.org/html/2604.04990v1
- Anthropic 2026 Agentic Coding Trends Report: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
- Claude Code Best Practices: https://code.claude.com/docs/en/best-practices
- Anthropic, Effective Context Engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- AGENTS.md 规范: https://asdlc.io/practices/agents-md-spec/
- AGENTS.md 实证研究: https://arxiv.org/html/2601.20404v2
- iSAQB, AI Agents Don't Modernize Legacy Code on Their Own: https://www.isaqb.org/blog/ai-agents-dont-modernize-legacy-code-on-their-own/
- Google 大规模 LLM 迁移 (FSE 2025): https://arxiv.org/abs/2504.09691
- AWS Transform 主机现代化: https://aws.amazon.com/blogs/migration-and-modernization/reimagine-your-mainframe-applications-with-agentic-ai-and-aws-transform/
- awesome-agentic-software-modernization: https://github.com/feststelltaste/awesome-agentic-software-modernization
- SWE-agent / ACI: https://arxiv.org/abs/2405.15793
- ACI as UX: https://agentpatterns.ai/tool-engineering/agent-computer-interface/
