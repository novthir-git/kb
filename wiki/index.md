# Wiki 内容索引

## 概览
- 素材（raw）：32（含 2 个 asset）
- 页面（wiki）：61
- 最后更新：2026-08-31

## 分析（analyses）
- [[cowork-saas-资本市场冲击]] — Cowork 对 SaaS 估值锚、seat 模型与 UI/工作流租金的冲击；价格信号与风险分类已区分，Q1 数据完成时间校正。
- [[cowork-plugins-架构]] — 官方机制校正版：Plugin（skills/connectors/sub-agents）→ Connector → MCP Server；旧架构图 SVG 已标记废弃。
- [[codex-agent-采用曲线]] — OpenAI Codex 2026 采用数据：周活 5×、非开发者百倍增长、99 分位单日 60+ 小时 agent turns；与体验成本的张力。
- [[SDD 开发规范研究]] — 面向 coding agent 的 SDD v1.0：current spec + change delta、六道门禁、追溯链、Reconcile & Retire 与试点指标。
- [[BMAD 项目文档治理方案]] — 面向实施人员的草案：明确各类 BMAD 文档的保留、回写、depublish 与生成规则，并给出存量清理和两周试点步骤。
- [[代码与文档漂移的本质]] — v2 四类漂移统一模型（表达/符合性/运行/生命周期）：本质是调和机制缺失；测试只是证据不是裁判；含 agent 时代漂移经济学与文档 GC。
- [[论代码与文档漂移解决方案]] — 在 Artifact-Driven Agent Workflow 之上补持续调和层：Spec 控制面、关系契约、事件 Adapter、AI 调和 + 确定性门禁、自动退役与采纳分级；含自产自审实证边界、组织最小职责与反对观点。
- [[基于IT4IT的Agent知识治理]] — 用 IT4IT Digital Product Backbone 治理企业统一 Agent 知识：Desired–Actual 调和、原子发布、权限与生命周期；新增 Knowledge Catalog 控制面与 OKF 发布制品映射。
- [[从知识图谱到 Agent 编排]] — 将权威事实、派生表示、检索、记忆、编排、外部行动与验证调和重构为七层闭环，并校正 GraphRAG、MCP、Skills、RPA 与 OKF 的边界。
- [[Anthropic-AI原生SDLC治理循环]] — Anthropic 高比例 AI 代码生产实践：控制单元从逐项审查上移到身份、委托、风险门禁、可观测与事故反馈组成的治理循环；区分 80% 代码归因与安全效果证据。
- [[Claude Tag 驱动的团队研发流程]] — 从 Claude Tag 团队协作实践推导的端到端研发流程：频道事件入口、意图固化、Agent 路由、证据化验证、风险分层放权、内部试用与事故回灌。
- [[AI编码技术债的三层治理]] — 以企业 / 成熟仓库 RCT、生产遥测、安全冲突和标准为证据，将 AI 编码治理重构为意图、证据、责任三层闭环。
- [[叙事与故事结构方法论]] — 以 Situation × Story × Discourse → Audience Effect（事实叙事外加 Evidence）建立七层体系，并将 Story Spine、ABT、SCQA、Toulmin 等方法归位到对应层。
- [[书与AI的优势边界及家庭组合]] — 区分书、AI、手机与阅读，以“书搭骨架、AI 做反馈、实践做验证”组织儿童学习，并附工程手工书选购与家庭规则。
- [[STORM-知识策展系统分析]] — Stanford STORM/Co-STORM 的四个可复用机制、workflow 而非 agent 的架构定位、2025-09 后停滞并被商业 deep research 吞没的判断；含二次失真局限与"去机制化失真"样本。
- [[Agent 全轨迹评测与审计]] — 将 Agent 评测从最终答案扩展为任务、Trace、指标与历史重评四类契约；区分 outcome 主证据与 process 归因证据。
- [[Uber-软件工厂的成本工程]] — Uber 公开的 agent 成本工程：六项成本方程、"agent 替自己多干的活"作为浪费定义、五层度量与四类杠杆；含"可计价者被优化"的张力与自报口径边界。

## 实体（entities）
- [[Anthropic]] — Claude 系列与 MCP 的开发者；既是技术实体也是商业研究标的。
- [[Claude Cowork]] — 面向非技术知识工作者、围绕"结果"设计的 agent 产品。
- [[Codex]] — OpenAI 的 agentic 编码/工作平台，从开发者外溢到非开发者。
- [[Claude Code]] — Anthropic 面向开发者的 agentic 编码工具；沿加速器、SDLC 载体、本库维护工具三条线追踪。
- [[Meta]] — Facebook/Instagram/WhatsApp 母公司；当前作为 agent 生产级落地节奏的证据信号来源。
- [[a2e-agent-auditing-engine|A²E（Agent Auditing Engine）]] — 上海 AI Lab 的 agent harness 评测引擎预印本与参考实现；当前代码许可与成熟度有明确边界。

## 概念（concepts）
- [[Loop Engineering]] — 围绕 AI agent 设计反馈闭环的方法论；Andrew Ng 三层产品开发循环：coding 分钟级、开发者反馈小时级、外部反馈天/周级。
- [[Evals]] — AI/Agent 评估的 task、trial、grader、trace、outcome 与 suite；区分 capability/regression eval 及证据边界；含 LLM-as-judge 自我偏好与错误相关实证。
- [[MCP]] — Model Context Protocol，agent↔数据/工具的开放连接标准（2024-11）。
- [[building-effective-agents]] — Anthropic 的 agent vs workflow 设计范式与模式分类。
- [[Agent 记忆架构]] — CoALA 的工作、情景、语义、程序记忆及内外部行动与循环决策；区分 Skills、日志和长期记忆。
- [[Agent Skills]] — 把流程知识打包成可安装文件夹的开放格式；收拢程序记忆载体、plugin 组件、SDLC 回灌目标三种语境。
- [[Open Knowledge Format]] — Markdown + YAML 的开放知识交换格式；区分可携带制品、托管目录、知识图谱、记忆与编排，并分析 provenance、trust、freshness 和 Attested Computation。
- [[知识图谱]] — 实体与有类型关系的知识表示；区分知识图谱、图数据库和图检索，并强调来源、时间与派生视图治理。
- [[RPA]] — Robotic Process Automation：面向稳定重复界面任务的软件机器人；与 Workflow、Agent、API/MCP 的互补边界。
- [[生产力-体验悖论]] — 区分感知速度、实际任务速度、活动产出、维护负担与 release 价值，解释 AI 编码的多层背离。
- [[llm-wiki-方法论]] — Karpathy LLM Wiki 模式：知识只编译一次、持续保鲜；三层架构 + 三大操作。本仓库方法论源头。
- [[Specification-Driven Development]] — 以规格为开发契约的 AI 软件工程范式；区分规格保留层级与 artifact mutation model。
- [[控制带]] — 按信号强度分级授予 agent 自主权（1σ 记录 / 2σ 只读诊断 / 3σ 受限行动），检测端完全确定性；与 T0–T4 产物风险分级正交。
- [[STORM-研究提示词组]] — 把 Stanford STORM/Co-STORM 移植成 Claude 可执行的六阶段研究提示词；坚持检索驱动视角发现、Moderator 挖 unknown unknowns、以异源校验替代自评。
- [[agent-auditing|Agent Auditing]] — 对 Agent 的 outcome、执行轨迹和运行边界进行可重复检查，形成可追溯证据链。
- [[agent-task-protocol|Agent Task Protocol（ATP）]] — A²E 用于分离 benchmark 适配与 harness 执行的内部软件接口协议。
- [[lifecycle-aligned-evaluation|Lifecycle-Aligned Evaluation]] — 按 Reasoning、Action、Final Answer 与 Runtime Quality 组织 Agent 评测指标。
- [[harness-vs-model|Harness 不是轻量 Wrapper]] — 同模型在不同 harness 上可产生不同的成功率、轨迹、成本和终止行为。
- [[Agent 工具上下文膨胀]] — 工具接入方式决定 agent 开场即背的固定上下文，且每轮重发；按需检索、CLI 投影、code-mode 三条解法及其代价。

## 对比（comparisons）
- [[GraphRAG 与 Vector RAG]] — 区分 Vector RAG、Text2Cypher、Microsoft GraphRAG Global 与混合检索，按局部、关系、全局和实时事实路由。
- [[OKF 与 llm-wiki 的关系]] — 将 OKF 定位为宽松交换格式、llm-wiki 定位为严格维护系统；当前保留内部模型，只建议未来做单向导出 Profile。

## 主题（topics）
- [[agent-生产级落地的鸿沟]] — 论点：Agent 试验渗透显著高于规模化价值；证据点覆盖 Gartner、Deloitte、McKinsey、Meta 与方法论边界；08-31 增 Uber 规模化正向案例（其依赖项无一来自"模型更强"）。
- [[AI方法论的去机制化失真]] — 论点：权威锚点保留、核心机制被抽掉的二次传播；9 样本证据表（含已确证上游）显示四特征可分离，固定五角色传播最广、"杜撰缺陷+自评补丁"唯一零反例；08-27 增第二观测对象（SDD 主题，载体为检索自动摘要）；同批提出的 M5 引文归属漂移唯一样本 08-31 复查证伪，降为待观察形态。
- [[SDD 收益主张的实证赤字]] — 论点：SDD 的缺陷/返工下降主张与实证支持存在系统性赤字；7 条证据显示最大样本结论反向，主张最强处证据最弱。

## 综合（synthesis）
- [[overview]] — 全局知识版图与活跃线索。

## 素材摘要（sources）
- [[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]] — Andrew Ng 将 0-to-1 产品开发拆成三层 loop：agentic coding、developer feedback、external feedback；强调 evals 与人类 context advantage。
- [[2026-02-03-Reuters-AI担忧重挫欧洲软件股-源摘要]] — Reuters 2 月初欧洲软件股抛售触发因素；已标注 raw 重建稿混入后期数据的时间矛盾。
- [[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要]] — Reuters 全球软件股 "wake-up call" 报道摘要：软件估值锚被 AI agent 叙事重估。
- [[2026-06-25-Axios-Codex-agent-用量增长-源摘要]] — Axios/Codex 采用曲线摘要：周活 5×、非开发者百倍增长、并行 agent 使用增强。
- [[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]] — Reuters 署名转载：欧洲软件与 IT 服务股 Q1 跌 27%、截至 3 月过去一年跌 38%；承接旧源的后期数据。
- [[2026-07-21-Anthropic-AI原生SDLC-源摘要]] — Anthropic 公开 AI 原生 SDLC：80% 代码行归因、风险分级、多层审查、独立身份、SIEM 与事故反馈闭环；附自报指标和多 agent 偏差边界。
- [[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]] — Claude Code 团队访谈的中文结构化整理：Claude Tag 团队协作、分层审查、eval 驱动放权、精简提示、工具设计与文件化共享记忆。
- [[2026-08-07-AI编码技术债三层治理-用户研究草稿-源摘要]] — 对用户多源草稿逐项核验：保留 toil shift 与三债模型，校正来源等级、工具配置、复杂度与重复率门槛。
- [[2026-08-07-AI编码治理高质量证据包-源摘要]] — 汇总企业与成熟仓库 RCT、GitHub 生产遥测、维护 / 安全研究及 NIST、DORA、OpenSSF、GitHub 官方治理材料，显式保留矛盾与外推边界。
- [[2026-07-28-GoogleCloudPlatform-Knowledge-Catalog与OKF-源摘要]] — 区分托管 Knowledge Catalog、GitHub 工具仓与 OKF v0.2；汇总 Bundle、信任/保鲜、Reference Agent、Attested Computation 及证据边界。
- [[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]] — A²E 论文的三层架构、1,035 次受控运行、轨迹审计方法、实验限制与代码复用边界。
- [[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]] — Anthropic 六阶段 AI 原生 SDLC 操作手册：committed artifact 产物链、控制带、eval 回归、skill/hook 分层；标注其零实证数据与产品营销性质。
- [[2026-08-27-Uber-软件工厂成本效率-源摘要]] — Uber 软件工厂的成本方程、五层度量表、四类优化杠杆与全部自报数据；含七条口径与证据边界。

## 素材（raw）
- sources/articles/2026-07-01-Andrew-Ng-三层产品开发循环 — Andrew Ng 关于 Loop Engineering 与三层产品开发循环的 X/The Batch post（源摘要 [[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]）。
- sources/articles/2026-07-03-Karpathy-LLM-Wiki-模式 — Karpathy 的 LLM Wiki 模式 gist 原文 verbatim 存档（承载页 [[llm-wiki-方法论]]）。
- sources/articles/2026-06-25-Axios-Codex-agent-用量增长 — Axios/OpenAI 报告：Codex 采用曲线与非开发者外溢（源摘要 [[2026-06-25-Axios-Codex-agent-用量增长-源摘要]]）。
- sources/articles/2026-05-25-arXiv-2605.23135-AI编码助手对软件工程的影响 — Vella & Blincoe 纵向研究：生产力-体验悖论。
- sources/articles/2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击 — Reuters：万亿美元软件股抛售的"警钟"（源摘要 [[2026-02-04-Reuters-全球软件股遭Anthropic警钟冲击-源摘要]]）。
- sources/articles/2026-02-03-Reuters-AI担忧重挫欧洲软件股 — 2 月初 Reuters 重建稿；混入后期数据，已在 [[2026-02-03-Reuters-AI担忧重挫欧洲软件股-源摘要]] 标注矛盾。
- sources/articles/2026-04-14-Reuters-欧洲软件股Q1跌幅 — Reuters 署名转载的 Q1 板块跌幅与 UBS 观点（源摘要 [[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]]）。
- sources/articles/2026-07-21-Anthropic-AI原生SDLC — Anthropic AI 原生软件开发生命周期的结构化研究摘录（源摘要 [[2026-07-21-Anthropic-AI原生SDLC-源摘要]]）。
- sources/articles/2026-07-21-Simon-Willison-Claude-Code团队访谈 — Simon Willison 对 Claude Code 团队访谈的中文结构化研究摘录，非逐句翻译或原文镜像（源摘要 [[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]）。
- sources/articles/2026-07-28-GoogleCloudPlatform-Knowledge-Catalog-README — Knowledge Catalog 工具与样例仓库 README verbatim 存档；含非官方产品免责声明。
- sources/articles/2026-07-28-Open-Knowledge-Format-README — OKF 定位、Reference Agent、样例 Bundle 与 Viewer README verbatim 存档。
- sources/articles/2026-07-28-Open-Knowledge-Format-v0.2-SPEC — OKF v0.2 规范 verbatim 存档（承载页 [[Open Knowledge Format]]）。
- sources/articles/2026-06-17-heynavtoor-Stanford-STORM四提示词长文 — [[AI方法论的去机制化失真]] 传播链已确证上游节点的一级存档（fxtwitter 抓取，2026-08-11）。
- sources/articles/2026-08-21-Anthropic-AI原生SDLC-playbook — Anthropic《The AI-Native SDLC Playbook》结构化存档，保留六阶段全部 play、配置示例与度量指标（源摘要 [[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]]）。
- sources/articles/2026-08-27-Uber-软件工厂成本效率 — Uber 工程博客《Running a Software Factory Efficiently at Uber Scale》正文结构化存档；Figure 1–12 为图片未存档（源摘要 [[2026-08-27-Uber-软件工厂成本效率-源摘要]]）。
- sources/notes/2026-07-28-从知识图谱到Agent编排-结构化内容草稿 — 用户确认冻结的 AI 结构化派生稿；基于飞书视频逐字稿，非一级来源，正式沉淀前须回查原始资料。
- sources/notes/2026-08-07-AI编码技术债三层治理-用户研究草稿 — 用户提供的多源综合草稿；含未经核验的来源分级、工具配置与指标阈值，校正版见 [[AI编码技术债的三层治理]]。
- sources/pdfs/2026-From-Technical-Debt-to-Cognitive-and-Intent-Debt-arXiv-2603.22106.pdf — Storey 提出的 technical / cognitive / intent debt 概念论文；ACM Queue 实践者文章的作者版本，属概念框架而非实证研究。
- sources/pdfs/2026-Twelve-Quick-Tips-for-AI-Assisted-Coding-in-Science-PLOS.pdf — PLOS Computational Biology 同行评审实践指南；覆盖科研场景的 AI 辅助编码、测试、验证与人类责任。
- sources/pdfs/2026-Cui-Generative-AI-Three-Field-Experiments-Software-Developers.pdf — Microsoft、Accenture 与 Fortune 100 企业、合计 4,867 名开发者的随机现场试验；短期任务 / PR 活动量提高 26.08%。
- sources/pdfs/2024-Google-AI-Development-Speed-RCT-arXiv-2410.12944.pdf — Google 96 名工程师、单个复杂企业任务的 RCT；测得约 21% 的完成时间缩短，未评估代码质量。
- sources/pdfs/2025-METR-Experienced-OSS-Developer-Productivity-arXiv-2507.09089.pdf — 16 名资深开源维护者、246 个成熟仓库任务的 RCT；AI 组实际慢 19% 而主观仍感觉更快。
- sources/pdfs/2026-NBER-Writing-Code-vs-Shipping-Code-w35275.pdf — 超过 10 万名 GitHub 开发者的事件研究；代码 / commit 增长在 project、release 与用户采用层逐级衰减。
- sources/pdfs/2026-Xu-AI-Programming-Maintenance-Burden-arXiv-2510.10165.pdf — 37,334 名开源贡献者的 Difference-in-Differences；外围产出增加、核心维护者 review 与返工负担上升。
- sources/pdfs/2023-Perry-Insecure-Code-with-AI-Assistants-ACM-CCS.pdf — 47 人、五个安全任务的 ACM CCS 用户研究；多数任务更不安全且 AI 组信心更高。
- sources/pdfs/2023-Sandoval-Lost-at-C-USENIX-Security.pdf — 58 人、一个 C 任务的 USENIX Security 随机研究；功能正确性提高，未发现严重安全缺陷显著上升。
- sources/pdfs/2025-DORA-Impact-of-Generative-AI-in-Software-Development-v2025.2.pdf — DORA 基于 2024 调查的统计分析；局部 flow / 代码质量收益与交付吞吐 / 稳定性下降并存，非因果试验。
- sources/pdfs/2022-NIST-SP-800-218-SSDF-v1.1.pdf — NIST Secure Software Development Framework 1.1；与代码来源无关的安全 SDLC 权威基线。
- sources/pdfs/2026-A2E-Agent-Auditing-Engine-arXiv-2608.07346.pdf — A²E 原始预印本；以 ATP、OpenTelemetry trace 和生命周期分层评估 harness 执行。
- assets/2026-07-01-Andrew-Ng-3-key-product-development-loops.png — Andrew Ng 三层产品开发循环原图截图（承载页 [[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]]）。
- assets/cowork-plugins-mcp-architecture.svg — 旧版 Cowork 插件架构图，因“plugin = MCP Server”错误已废弃；只读保留供追溯（见 [[cowork-plugins-架构]]）。
