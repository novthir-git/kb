# 操作日志（append-only）

## [2026-07-03] research | CoWork 为什么影响 SaaS 资本市场
联网研究 5 个来源（Anthropic Cowork/MCP/building-effective-agents 官方页 + 2 篇 Reuters）。
Reuters 直连被封锁，正文经 Globe and Mail / Euronews / CNBC / Yahoo 等镜像与报道交叉核对后
存档 2 篇到 raw/articles/。沉淀主分析 [[cowork-saas-资本市场冲击]]；
新建实体 [[Anthropic]]、[[Claude Cowork]]，概念 [[MCP]]、[[building-effective-agents]]；
初始化 index.md、overview.md、log.md（本仓库首次沉淀）。

## [2026-07-03] research | 按图片结论重写主文档（纠偏）
上一版自造"光谱/打分卡"框架偏离了用户图片的结论结构。删除 SaaS-agent-替代光谱.md，
按图片的"核心结论 + 7 段"（估值假设/seat 模型/护城河穿透/估值中枢/最危险类型/相对安全类型/范式切换）
忠实重写 [[cowork-saas-资本市场冲击]]，自查跌幅数据仅作佐证。同步 index/overview。

## [2026-07-03] research | 详述连接层 MCP
应用户要求展开连接层：重写 [[MCP]] 页（N×M→M+N 集成爆炸、client-server 三原语、
跨系统保持上下文机制、CoWork 插件=MCP Server 映射、与 SaaS 论题关联）；
主页第 3 节把 MCP 从括号扩为一段正式论述并指向该页。

## [2026-07-03] ingest | Cowork 插件架构图入库
用户确认沉淀（选直接写模式）：生成 Cowork 插件体系架构图。
自包含 SVG 存 raw/assets/cowork-plugins-mcp-architecture.svg；新建承载页 [[cowork-plugins-架构]]
（六层图解 + 对外话术 + 诚实边界）；更新 [[Claude Cowork]]（加命名与对外话术节）、
[[MCP]] 交叉链接、index/overview。

## [2026-07-03] research | 沉淀 Codex 两篇材料（Axios 采用曲线 + arXiv 体验悖论）
Axios 原文 403，经 OpenAI/哥大/杜克/宾大联合报告 + 多篇转述交叉核对还原后存档；
arXiv 2605.23135 缺 PDF 抽取工具，摘要页+PDF 渲染双渠道核对存档（摘要级）。
新建实体 [[Codex]]、分析 [[codex-agent-采用曲线]]、概念 [[生产力-体验悖论]]（含"监督式工程"）；
横向更新 [[Claude Cowork]]、[[building-effective-agents]] 交叉链接；同步 index/overview。
两篇合看：采用爆发 vs 体验下滑，同一范式的两面。

## [2026-07-03] research | Agent 生产级落地的鸿沟（Demo≠生产）
用户澄清关注点为"Agent 热度高但卡点在生产级落地而非 Demo"这一可复用论点（非某家公司新闻）。
联网研究扎克伯格 2026-07-02 内部全员会表态（Reuters 独家被拦，经 TechCrunch 等转载源交叉核实）。
新建主题页 [[agent-生产级落地的鸿沟]]（论点+结构性原因+证据点表，扎克伯格首入），
挂链 [[building-effective-agents]]、[[Claude Cowork]]、[[cowork-saas-资本市场冲击]]、[[codex-agent-采用曲线]]，
留悬空链接 [[Meta]]。更新 index.md（新增"主题"类，页面 10→11）、overview.md（新增板块+活跃线索）。
Reuters 原文抓取受限，未做 raw/ 存档（不以摘要冒充原文），溯源由页面 frontmatter 承担。

## [2026-07-03] research | schema 审视 + 存档 Karpathy 方法论原文
用户要求审视 AGENTS.md 并（举例）本地存档 Karpathy gist。纠偏：该 URL 并非"每次重新下载"，
但仍存档——理由是防链接失效 / 自包含。verbatim 存入 raw/articles/2026-07-03-Karpathy-LLM-Wiki-模式.md，
新建概念页 [[llm-wiki-方法论]]，AGENTS.md 首段改为指向本地存档。
另修 schema 两处矛盾/模糊：sources/ 源摘要页改为"按需不强制 1:1"（解释 sources/ 为何为空）；
新增 analyses/topics/synthesis 选择判据。index.md 计数 raw 5→6、页面 11→12。
遗留待用户拍板：index 概览的分类硬计数是否精简（易漂移、可 ls 派生）。

## [2026-07-03] lint | 精简 index 概览计数
按上次审视结论执行：index.md 概览砍掉分类硬计数（分析/实体/概念…），只留素材总数、页面总数、最后更新。
理由：分类明细手工维护必然漂移、可 ls 派生（违反 DRY）。已在 AGENTS.md「index.md 与 log.md」节写明"不维护分类明细计数"防回潮。

## [2026-07-03] lint | schema 加固：启动仪式 + 5 处漏洞
按用户 6 条建议评估后执行（5 取 1 部分重叠，2 处做了独立改动）：
① 顶部新增「会话启动仪式」（log 尾+index 概览），铁律6 改为指针——但不把 per-question 的"先查wiki"折进来（节奏不同）。
② log 记录规则明确：research/ingest/lint 必记，纯 query 默认不记；query 暴露的空白转入 overview「悬而未决」。
③ lint 清单加"index 计数核对（find|wc -l）"——与上轮"砍分类明细"互补，保留总数。
④ 新增约定"全库文件名唯一"+ lint 查重名（防 Obsidian 双链歧义）。
⑤ 新增约定"重命名/合并必须善后入链（grep 旧名/留 stub）"，区分意外悬链 vs 有意待写悬链。
⑥ 强制"编辑即 bump updated"；证据点表统一表头 |日期|来源|信号|备注|；overview 硬指标 ≤60 行。

## [2026-07-03] lint | 全库健康检查
检查全部 12 个 wiki 页面、index/log/schema、raw 计数、双链、重名、frontmatter、overview 行数、证据表格式与 URL 可达性。
发现主要问题：overview.md 缺 sources frontmatter；[[Meta]] 是未标注待写的断链；
3 个被 ≥2 页引用的 raw 素材尚未建 sources 摘要页；.wiki-schema.md 与现行 AGENTS.md 约定漂移；
Reuters 原文 URL 返回 401、Axios 返回 403（Axios 已标注，Reuters 需补可访问性说明）。

## [2026-07-03] lint | 修复全库健康检查发现项
按上次 lint 建议修复：为 overview.md 补 sources frontmatter；新建 [[Meta]] 解除未标注断链；
为被 ≥2 页引用的 3 个 raw 存档新建 sources 摘要页（使用 `-源摘要` 后缀避免与 raw 文件重名）；
把相关页面的来源双链改指向源摘要页；同步 .wiki-schema.md 到现行 AGENTS.md 约定；
更新 index.md 页面总数 12→16 并新增 sources/Meta 条目。复查结果：wiki 页面 16、raw 素材 6、
无可见重名文件、frontmatter 齐全，剩余 2 个断链均为已标注待写页。

## [2026-07-03] ingest | Andrew Ng 三层产品开发循环
按用户提供的 X post 原文与配图入库：存档 raw/articles/2026-07-01-Andrew-Ng-三层产品开发循环.md，
复制原图到 raw/assets/2026-07-01-Andrew-Ng-3-key-product-development-loops.png。
新建源摘要 [[2026-07-01-Andrew-Ng-三层产品开发循环-源摘要]] 与概念页 [[Loop Engineering]]；
横向更新 [[Codex]]、[[building-effective-agents]]、[[生产力-体验悖论]]、[[agent-生产级落地的鸿沟]]、[[overview]]。
核心沉淀：AI 产品开发的关键资产不是一次 prompt，而是分钟级 coding、小时级开发者反馈、天/周级外部反馈组成的三层闭环。

## [2026-07-16] research | SDD 开发规范研究
联网研究 GitHub Spec Kit、Kiro Specs、OpenSpec、Tessl、NASA / ISO / RFC 要求规范及 2026 年两项学术研究。
新建概念 [[Specification-Driven Development]] 与分析 [[SDD 开发规范研究]]；横向更新 [[Loop Engineering]]、
[[building-effective-agents]]、[[生产力-体验悖论]]、[[agent-生产级落地的鸿沟]]、[[Codex]]、[[overview]]。
核心判断：多数长期项目应采用 Spec-anchored + Living current spec + Flow-forward change history，
以 `REQ → Design → Task → Test/Eval → Evidence` 追溯链约束 agent，同时按 Quick / Standard / Full 控制仪式成本。
网页抓取技能因首次偏好尚未配置而按规则未运行；本次来源均以官方 URL + 2026-07-16 检索日期直接溯源。

## [2026-07-16] query | 代码与文档漂移的本质
将讨论中的因果链沉淀为 [[代码与文档漂移的本质]]，更新 [[Specification-Driven Development]]、
[[SDD 开发规范研究]] 与全局导航。

## [2026-07-16] research | 代码与文档漂移的本质 v2（合并两轮评审重写）
合并 Claude 初评与用户转述的外部评审，经用户确认后重写 [[代码与文档漂移的本质]]：
新增四类漂移分类（表达/符合性/运行/生命周期）与“可调和性取决于共同形式表示”论证；
测试由裁判降为证据层；“同一变更”放宽为“同一交付事务 + 发布门禁”；“完成后归档”改为“蒸馏后删除”；
新增生命周期 GC 与 agent 时代（消费者/生产者两面）两节；补外部锚点（DRY、Hyrum's Law、
ADR/Nygard、K8s reconciliation，URL 均经当日核验）。横向更新 [[SDD 开发规范研究]]、
[[Specification-Driven Development]] 指针，同步 index/overview。

## [2026-07-16] research | 收编修订《论代码与文档漂移解决方案》
用户提交的解法页（原游离于 index/log 之外）经评审后修订收编：修复 T2“双 AI 审查自动删除”与
§六“AI 不得凭置信度删除”的矛盾（改为可程序验证的确定性替代条件）；新增“关系图的元漂移”小节并
收窄范围声明（主治表达 + 生命周期漂移）；四类漂移表与权威表去重改引 [[代码与文档漂移的本质]]，
“教程权威”一行回写 v2 权威表；补先行系统锚点（sphinx-needs、Backstage catalog、Pact、BMAD-METHOD，
URL 均经当日核验）；新增“最小可行版本与采纳分级”一节。互链 v2 与 [[SDD 开发规范研究]]，
index 页面数 21→22。

## [2026-07-16] research | Spec 方法共性回写漂移解决方案
基于 claude-code-best-practice 所列 Spec Kit、OpenSpec、BMAD、GSD、RPI、Superpowers 等工作流的
横向分析，更新 [[论代码与文档漂移解决方案]]：新增“Spec 是 Agent 控制面”一节，将共同内核抽象为
Artifact-Driven Agent Workflow；明确本方案是在现有 SDD 之上补 Continuous Documentation Reconciliation，
不是再造 Spec 流程；将 Framework Adapter 扩展为状态转换事件映射，增加 transition、完成证据、
一致性级别、canonical 回写目标和退役条件；同步 index 与 overview。

## [2026-07-16] lint | 全库健康检查
检查全部 22 个 wiki 页面、8 个有效 raw 素材、index/schema、双链、重名、frontmatter、证据点表、
overview 行数与 33 个外部 URL。结构项均通过；发现 4 类待修：Cowork“插件 = MCP Server”模型已被官方
插件定义推翻且影响 4 页与架构图；MCP 远程传输仍写旧版 HTTP/SSE；SDD 的 change package 永久归档与
漂移治理页“过程产物蒸馏后删除”矛盾；2026-02-03 Reuters 重建稿混入晚于发布日期的数据并传播到 3 页。
另有 1 个普通孤儿页、1 个不可解析本地来源、1 个证据不足的主题强结论，以及 evals 缺少独立概念页。
待用户确认后修复。

## [2026-07-16] lint | 修复全库健康检查发现项
按用户确认完成全部修复：依据 Anthropic 官方说明把 [[cowork-plugins-架构]]、[[MCP]]、[[Claude Cowork]]、
[[cowork-saas-资本市场冲击]] 从“plugin = MCP Server”改为“Plugin（skills/connectors/sub-agents）→
Connector → MCP Server”，旧架构图 SVG 因 raw 只读而标记废弃；MCP 远程传输更新为 Streamable HTTP。
保留受污染的 2026-02-03 raw 原稿并在摘要显式标注时间矛盾，新增
raw/articles/2026-04-14-Reuters-欧洲软件股Q1跌幅.md 与
[[2026-04-14-Reuters-欧洲软件股Q1跌幅-源摘要]] 承接 Q1 数据，Anthropic $9bn→$30bn 改引 4 月官方
run-rate revenue 口径。统一 SDD 生命周期为 G5 Reconcile & Retire，移除不可解析本地 README 来源。
为 [[agent-生产级落地的鸿沟]] 补 Gartner、Deloitte、McKinsey 证据与边界；新建 [[Evals]] 并横向回链，
由 [[代码与文档漂移的本质]] 补入链解除 [[llm-wiki-方法论]] 孤儿。更新 index/overview；复查为
wiki 24 页、有效 raw 9 个、overview 58 行、无重名与意外断链，唯一零入链页为系统页 [[overview]]。

## [2026-07-16] research | IT4IT Agent 知识治理方案评审收编
用户初稿评审收编为 [[基于IT4IT的Agent知识治理]]，补强：权限/ACL 变更事件与同步机制、eval 回归门禁、
评价指标、T0–T4 知识风险分级、实时/索引路由规则、源成熟度前提、Deploy≠Release 暗发布窗口、
"与漂移方法论的关系"（借 Desired/Actual 同构把知识失效改造成运行漂移）。
回链更新 [[论代码与文档漂移解决方案]]、[[代码与文档漂移的本质]]、index、overview；
IT4IT 3.0.1（c24a）与七条价值流引用已联网核实；根目录原稿删除（用户确认不留档）。

## [2026-07-17] research | Agent 自产自审的实证边界
回答“可持续文档代码一致性可行吗（Agent 写、Agent 审）”，联网核实三组实证：自我偏好偏差
（Panickssery et al., NeurIPS 2024）、跨模型错误相关（ICML 2025 + Nine Judges）、
文档-代码不一致检测（DocPrism：开放式审查 98% 标记率/14% 准确率，LCEF 后 94%）。
更新 [[论代码与文档漂移解决方案]]（§七新增“自产自审的实证边界”小节；§九“独立见证”论证被实证
收紧——跨厂商强模型错误同样趋同）、[[Evals]]（补 LLM-as-judge 两类偏差）、
[[SDD 开发规范研究]]（门禁节补交叉引用）；同步 index、overview。

## [2026-07-17] query | 辩论会沉淀：反对观点与组织最小职责
就“借助 AI 持续保障文档-代码一致性的可行性”举行正反辩论并回答“组织做什么”，经用户确认沉淀至
[[论代码与文档漂移解决方案]]：§十一 新增“组织的最小职责”（wiring over willpower、建设/运营/试点
九条职责、“元维护不收敛即机制失败”判定信号）；新增 §十三“反对观点与未决空白”（保障叙事过度信任、
AI 边际贡献归因之争、组织执行力无实证——结论限定为“机制可行已论证，组织可行未验证”）。
同步 index、overview（SDD 试点线索补组织纪律成本）。

## [2026-07-17] lint | 全库健康检查（排除 HTML）
检查全部 25 个 wiki 页面、9 个有效 raw 素材、index/schema、frontmatter、双链/锚点、重名、证据点表、
overview 行数与 50 个外部 URL；本地 `.html` 排除，内容范围内实际无 `.html`。结构项均通过：无重名、
意外断链、普通孤儿页或索引漂移，overview 为 60 行。发现 4 项待修：[[论代码与文档漂移解决方案]]
把 ICSE 2025 论文的 METEOR 89.2 误写成准确率，并写入原文不支持的 5.9% 假阳性率；阶段 0 成本“≈0”
与后文“主要工程量/建设期约数周”矛盾；“关系图完整性”门禁与前文只能验证已声明边的边界表述不一致；
ResearchGate 论文页和 IT4IT 七价值流页受限但缺少替代溯源说明。待用户确认后修复。

## [2026-07-23] research | Anthropic AI 原生 SDLC 治理循环
通读并交叉核验 Anthropic 公开 SDLC、Code Review、Agent identity / Zero Trust 资料；存档结构化研究摘录，
新建 [[2026-07-21-Anthropic-AI原生SDLC-源摘要]] 与 [[Anthropic-AI原生SDLC治理循环]]。将 80% 代码行归因
与自主度、生产力、安全结果区分；沉淀身份与委托图、风险门禁、shadow mode、自动批准抽样、SIEM 和事故
反馈闭环。横向更新 [[Anthropic]]、[[Evals]]、[[agent-生产级落地的鸿沟]]、
[[论代码与文档漂移解决方案]]、index 与 overview。

## [2026-07-23] lint | 全库健康检查（Anthropic SDLC 沉淀后）
检查全部 27 个 wiki 页面、10 个有效 raw 素材、index/schema、frontmatter、双链/锚点、附件、重名、孤儿页、
主题证据表、overview 行数与 55 个外部 URL。结构项均通过：index 计数和页面覆盖一致，无重名、意外断链、
坏锚点、缺失附件或普通孤儿页；overview 为 60 行。新沉淀未引入问题。仍有 4 项既有待修：
[[论代码与文档漂移解决方案]] 将论文的 METEOR 89.2 误写为准确率并加入来源不支持的 5.9% 假阳性率；
阶段 0 成本“≈0”与后文主要工程量/数周建设期矛盾；“关系图完整性”门禁未明确限定为已声明边；
ResearchGate 引用当前返回 403，且缺少可免费核验的替代来源。上次受限的 IT4IT 七价值流官方页本次已恢复 200。
待用户确认后修复。

## [2026-07-27] schema | 定义 output/ HTML 呈现层
新增 `output/` 约定并写入 AGENTS.md、同步 `.wiki-schema.md` 目录树。定位为 wiki 的**派生视图层**
（可重复展示、不得独立维护第二事实源），按用途分 `personal/`（稳定文件名、可原地重渲染）与
`shared/`（`<slug>-YYYY-MM-DD.html`、发出即冻结、脱敏、双链展开）；要求 canonical-source/generated
双 meta + 页脚溯源、原创稿回灌 wiki、wiki 页加可选 `renders:` 字段；lint 增两项确定性检查
（来源页是否存在、wiki `updated` 是否晚于 HTML `generated`）；log 前缀扩展为
research|ingest|lint|output|schema。存量 4 份 HTML 按"来源不明即已发出"处理，未移动未改写，待用户分类。

## [2026-07-27] lint | 修复漂移方案页数据错误与阶段 0 口径
联网复核 [[论代码与文档漂移解决方案]] §七 实证③ 的争议数字，修复 2026-07-23 lint 的两项待修。
（1）"89.2% 准确率、5.9% 假阳性率"两数均无法证实：C4RLLaMA 论文摘要不含 89.2；第三方比较表
（CCISolver 表 V）给出 accuracy 87.82%、precision 89.67%/92.67%、F1 87.45/90.63；5.9% 疑由摘要中
55.9%（post hoc 人工评估正确改写比例）讹变，且与 precision 反推的约 10% 假阳性不符。已替换为可核验值，
403 的 ResearchGate 链接换成 ACM 原始论文 + CCISolver arXiv。
（2）补 DocPrism 跨语言真实评测：标记率 15%、precision 0.62——原页只引消融实验的 94%，系统性偏乐观；
已写入"不能拿消融值做规划基准"。
（3）阶段 0 成本"≈0"改为"建设期数周（生成化改造）+ 建成后持续≈0"，消除与 §十一"建设期约数周"的矛盾。
另核实 ai-doc-consistency.html 中三处 wiki 无记载的数据（LCEF 后标记率 14%、跨语言 precision 0.62、
Monperrus arXiv:2606.13175）全部属实，来源为 DocPrism 摘要与该论文本身——是 wiki 沉淀缺口，非该页错误。
output/可持续文档代码一致性方案.html 补页首快照说明 + canonical-source/generated 双 meta（未重渲染，仅追加）。

## [2026-07-27] research | 叙事与故事结构方法论
基于 Aristotle、Kenn Adams、Joseph Campbell、Barbara Minto、Randy Olson、Nancy Duarte、
Liberating Structures、STAR(R) 与 Toulmin 等来源，新建 [[叙事与故事结构方法论]]。
区分故事、说服、案例、复盘和论证五类任务，沉淀方法选型表、混合骨架、Agent 案例、证据边界与失败模式；
同步更新 index 与 overview。

## [2026-07-27] lint | 全库健康检查（叙事方法论沉淀后）
检查全部 28 个 wiki 页面、10 个有效 raw 素材、346 条页内双链、index/schema/frontmatter、附件与锚点、
topics 证据表、overview 行数、66 个外部 URL 和 4 份 output HTML。结构项通过：计数与索引一致，
无内容目录重名、意外断链、普通孤儿页、坏锚点或缺失附件；overview 为 60 行。
发现 5 组待修：[[Claude Cowork]] 的可用性落后于官方 web/mobile/remote 状态，且
`output/cowork-cloud-mode.html` 的原创信息未回灌 wiki；3 份 HTML 缺 canonical-source/generated，
另 1 份派生视图已过期且缺 renders 回链；该视图还保留 4 个外部不可解析的双链/错误相对路径；
[[叙事与故事结构方法论]] 的 ABT 来源证书失效、Pixar 采用断言缺直接出处且部分综合未标注；
[[llm-wiki-方法论]] 将“LLM 不会漏更、维护成本趋零”当作事实，未标为 Karpathy 的主张或补实证边界。
66 个 URL 中 54 个直连成功，11 个受限但有替代溯源或可经网页读取，1 个 ABT 旧站为实质失效。
本次仅报告并记日志，待用户确认后修复。

## [2026-07-27] research | 叙事系统七层模型
根据用户对“框架分散、缺少系统总结”的反馈，重构 [[叙事与故事结构方法论]]：
以 narratology 的 Story–Discourse 区分为骨架，加入 Situation、Audience Effect 与事实叙事的 Evidence，
形成从叙事情境、故事世界、因果变化、叙事话语、意义体验、真实性论证到交付结构的七层模型；
明确区分描述性理论、生成/诊断方法和表达模板，并将 Story Spine、Hero's Journey、Story Grid、
ABT、SCQA、STAR、W3 与 Toulmin 归位到对应层。补系统阅读路径，修复 ABT 失效链接，
用 Pixar in a Box 课程校正 Story Spine 的来源表述；同步更新 index 与 overview。

## [2026-07-27] research | 书与 AI 的优势边界及家庭组合
基于 OECD、UNESCO、儿童纸质/数字阅读与词汇学习元分析、AAP 家庭媒体建议及图书来源，
新建 [[书与AI的优势边界及家庭组合]]。区分一般意义上的书、AI、手机与阅读，
形成“书建骨架—独立思考—实践验证—AI 反馈—孩子复述”的家庭组合，并整理 8 本工程手工书、
四周实践计划、手机条件规则与工程安全底线；同步更新 index 与 overview。

## [2026-07-27] output | 工程手工书推荐与书 vs AI 对比（对外 HTML）
由 [[书与AI的优势边界及家庭组合]] 生成
`output/shared/工程手工书推荐与书vsAI对比-2026-07-27.html` 冻结版。
采用 thariq-html editorial research explainer：结论先行、书/AI 对比表、可筛选书单、
四周工程计划与家庭媒体规则；已完成脱敏、零外部运行时请求、控制台无错误及桌面/移动端无页面溢出检查。

## [2026-07-28] query | 从知识图谱到 Agent 编排结构化内容草稿
按用户明确要求，将基于飞书视频逐字稿形成的系统性内容冻结保存为
`raw/notes/2026-07-28-从知识图谱到Agent编排-结构化内容草稿.md`。
文件已标明 AI 派生稿、非一级来源及正式沉淀前的原始资料补证要求；同步更新 index 的 raw 计数与条目，
尚未生成 wiki 摘要页或分析页。

## [2026-07-28] research | 从知识图谱到 Agent 编排正式沉淀
复核冻结草稿并回查 Microsoft GraphRAG / BenchmarkQED、Neo4j GraphRAG、CoALA、Agent Skills、
MCP、Anthropic 与 IBM RPA 一手资料；确认草稿存在 GraphRAG 与 Text2Cypher 混称、把 Skills 等同全部
程序记忆、把 MCP 当编排层及 Agent/RPA 二选一等边界问题。新建 [[从知识图谱到 Agent 编排]]、
[[知识图谱]]、[[GraphRAG 与 Vector RAG]]、[[Agent 记忆架构]]、[[RPA]]；横向更新 [[MCP]]、
[[building-effective-agents]]、[[基于IT4IT的Agent知识治理]] 与 [[llm-wiki-方法论]]，
同步更新 index 和 overview。raw 草稿保持不可变，未直接改名覆盖。

## [2026-07-28] research | Knowledge Catalog 与 Open Knowledge Format
归档 GoogleCloudPlatform/knowledge-catalog 根 README、OKF README 与 v0.2 SPEC 三份原文；
新建 [[2026-07-28-GoogleCloudPlatform-Knowledge-Catalog与OKF-源摘要]]、[[Open Knowledge Format]]
和 [[OKF 与 llm-wiki 的关系]]。核心判断：Knowledge Catalog 是托管元数据治理面，OKF 是宽松的
可携带知识制品格式，Reference Agent 是编译器 PoC，Attested Computation 是确定性运行证明契约；
OKF 不是正式知识图谱、记忆系统或 Agent 编排器。横向更新 [[知识图谱]]、[[Agent 记忆架构]]、
[[llm-wiki-方法论]]、[[从知识图谱到 Agent 编排]]、[[基于IT4IT的Agent知识治理]]、index 与 overview；
当前决定保留 llm-wiki 作为严格内部模型，只在未来有真实消费者时试验单向 OKF 导出。

## [2026-07-28] lint | 全库健康检查（Knowledge Catalog / OKF 沉淀后）
检查全部 37 个 wiki 页面、14 个 raw 素材、index/schema/frontmatter、双链、附件、重名、孤儿页、
topics 证据表、overview、110 个外部 URL，以及 5 份 HTML 和 1 份 output/personal Markdown。
结构项通过：index 计数与页面覆盖一致，无重名、意外断链、缺失附件、普通孤儿页或 frontmatter 缺项；
overview 为 58 行。外链无确认的 404/410；77 个直连返回 200，11 个返回 401/403，22 个超时或受限，
后 33 个只能视为“未证实失效”，不能当作坏链。
发现 5 组待修：（1）[[Claude Cowork]] 仍写成桌面端产品，落后于官方 web/mobile beta、云端续跑、
定时任务和并行执行状态；`output/cowork-cloud-mode.html` 的较新信息未回灌 wiki；
（2）output 层有 3 份 HTML 缺 canonical-source/generated，`output/可持续文档代码一致性方案.html`
已落后于源页且缺 renders 回链、保留 4 个不可解析的内部双链路径；`output/ai-doc-consistency.html`
仍展示已被 wiki 纠正的“89–94% 准确率 / 5.9% 假阳性率”；`output/罗伯特智能体问答系统方案.html`
按存量文件规则视为已分享件却含内部代号；另有 1 份 Markdown 滞留在 output/personal，形成第二事实源风险；
（3）[[MCP]] 未记录 2025-12 捐赠给 Linux Foundation / AAIF 后的中立治理；当前官网仍把
2025-11-25 标作 current，但破坏性变更版 2026-07-28 计划于今日发布，需在正式切换后复核；
（4）Attested Computation、Google Cloud Knowledge Catalog 被多页反复引用却无独立页面，
System of Record 已是显式待写悬链；（5）[[论代码与文档漂移解决方案]] 已达 638 行，偏离“精炼小页”
约定；overview 距 60 行上限仅余 2 行。此次只报告并记日志，未修改 wiki 或 output，待用户确认后修复。

## [2026-07-29] research | STORM 方法论移植为 Claude 研究提示词组
联网研究 Stanford OVAL 的 STORM（NAACL 2024）与 Co-STORM（EMNLP 2024）：读 GitHub 仓库、
两篇论文摘要、knowledge_curation.py 与 collaborative_storm/engine.py 源码，核对 release 与 commit 历史。
沉淀 [[STORM-研究提示词组]]（六阶段 + 快速版），更新 [[llm-wiki-方法论]]、[[building-effective-agents]]、[[Evals]] 共 3 页。

关键判断：
（1）该项目已停滞——最后 commit 2025-09-30、最后 release v1.1.0（2025-01-23），
在 OpenAI Deep Research（2025-02）与 Gemini Deep Research Max（2026-04，DeepSearchQA 93.3%）
之后事实上被商品化浪潮吞没；30.4k star 是历史存量非活跃度。
（2）真正可复用的内核是"用结构制造多样性，而非用指令请求多样性"——persona 由检索语料反推得出，
不是固定角色表；以及 Co-STORM 的 Moderator（专问"检索到但没被用上"的信息）作为 unknown unknowns 引擎。
（3）分析了知乎《Stanford STORM 方法》（https://zhuanlan.zhihu.com/p/2051623683756766563 ，
编辑于 2026-06-21，转写自 x.com/heynavtoor 推文）：该文抽掉 Retrieval 与检索驱动的视角发现，
改为无联网的固定五角色扮演，却保留原论文 25%/10% 数字背书——而该数字的成立前提是
"带检索的 STORM 打赢另一个带检索的 baseline"。其"STORM 不会主动批判自己"属杜撰
（论文自述局限为 source bias transfer 与 over-association），"5 分钟博士级研究"与论文
"仅在 pre-writing 阶段有帮助"直接冲突。本次沉淀刻意保留被抽掉的三环节。
（4）该文推荐的"让 Claude 给自己打分"恰好踩中 [[Evals]] 已记录的 LLM-as-judge 自我偏好偏差，
提示词组据此改用引用抽验 / 反证检索 / 来源结构检查三项可证伪的异源检查。

## [2026-07-29] research | STORM 知识策展系统分析（补全）
补全上一条留下的悬空页 [[STORM-知识策展系统分析]]，填补 [[STORM-研究提示词组]] 的证据底座。
存档 [[2026-06-21-知乎-Stanford-STORM方法]]（摘录存档，非全文）到 raw/articles/——
该文被本页作为"去机制化失真"样本引证，原文可能被改删，无存档则论断不可核验。
更新 [[overview]]（新增"AI 知识策展与研究方法论"板块 + 1 条活跃线索）、index.md（页面 28→29、素材 10→11）。

页面要点：
（1）四个可复用机制及关键参数：perspective-guided question asking（persona 由检索语料反推）、
ConvSimulator 对话式检索（历史截断 2500 词、snippet 上限 1000 词）、
Co-STORM Moderator 与防收敛阈值（moderator_override_N_consecutive_answering_turn=3）、mind map 共享概念空间。
（2）架构定位：STORM 四模块是预定义代码路径，属 prompt chaining + parallelization，
是 workflow 而非 agent；Co-STORM 的 DiscourseManager 亦为规则分支。2024 年是正确取舍，
但"流程写死意味着模型变强时系统不跟着变强"，构成 Simplicity 原则的反面边界。
（3）停滞判断：最后 commit 2025-09-30、最后 release v1.1.0（2025-01-23）；对照
OpenAI Deep Research（2025-02-03）与 Gemini Deep Research Max（2026-04-21，DeepSearchQA 93.3%）。
（4）本 wiki 补充的局限"二次失真"：TopicExpert 答案基于 snippet 生成而非原文，
大纲与正文再基于该答案生成——成稿与原始来源之间隔两层 LLM 转述，而引用仍指向最初 URL，
引用形式上可溯源、中间损耗不可见。
（5）评估数字语境已校正：25%/10% 是相对作者自建单一基线的绝对百分点提升，无"第二名"。

维护动作：overview.md 原为 61 行（超 AGENTS.md 的 ≤60 上限），本次新增内容同时压缩 SDD 段落，
保留全部双链与论断，仅收紧行文。当前 63 行，仍略超，建议下次 lint 做一次整体瘦身。

## [2026-07-29] lint | overview.md 行数超标溯源与瘦身
承上条：上条日志所记"当前 63 行"为估算失误，实测 69 行，特此更正（log 只追加不修改）。
已压缩正文三处（AI Agent 板块、SaaS 再定价线索、Demo→生产线索），保留全部双链与论断。
瘦身后总行数 66、正文 39 行，仍超 AGENTS.md 的 ≤60。

溯源结论：超标主因不是正文，而是 frontmatter 的 sources 列表已达 21 行——
它逐条罗列 overview 引用的每个 wiki 页，而这些页在正文里全部已有双链、在 index.md 里亦有权威清单。
这是**同一事实的第三份副本**，每加一页就要三处同步，正是 [[代码与文档漂移的本质]] 所述的漂移温床。
建议 schema 层面处理（需用户确认）：overview.md 的 sources 改为不再罗列内部页面，
仅保留外部 URL；内部关联由正文双链承载。未经确认，本次不擅自删除。

更正（同批次）：上段"总行数 66、正文 39 行"系我在脚本里写死估算值而非代入实测，实为**总 67 行、正文 40 行**。
结论不变（正文非超标主因，frontmatter sources 占 27 行才是）。已改用实测值记录，不再手写估算。

## [2026-07-29] schema | 布局适配 nashsu/llm_wiki 桌面应用
经用户确认执行布局迁移，使本仓库可直接作为 [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)
桌面应用的 project 打开（图谱、社区检测、hybrid 检索），同时保持 Claude Code 为 `wiki/` 的唯一写手。
改动：（1）`raw/articles`、`raw/notes` → `raw/sources/articles`、`raw/sources/notes`（该 App 硬编码
`raw/sources/` 为素材根，子目录名被用作分类上下文）；`raw/assets` 原本已匹配，未动；文件内容一律未改。
（2）`index.md`、`log.md` 移入 `wiki/`（该 App 硬编码 `wiki/index.md`、`wiki/log.md`、`wiki/overview.md`；
不移则它会另建一套，形成第二事实源）；`.wiki-schema.md` → `wiki/schema.md`。
（3）新建 `wiki/purpose.md`——目标、关键问题、范围 in/out、6 条演化中的核心论断；它与 AGENTS.md（怎么运作）、
overview.md（现在有什么）三者分工写入 AGENTS.md 新增的「配置三件套」小节。purpose 成为沉淀 gate 的判据。
（4）根目录 `purpose.md`、`schema.md` 两个 symlink 指向 wiki/ 下真身——该 App 一条摄入路径从项目根读、
另一条从 `wiki/` 读，上游自身不一致。（5）AGENTS.md 与 `wiki/schema.md` 同步改写：目录结构、启动仪式 grep 路径、
lint 计数命令（排除 4 个聚合/配置文件）、新增路径引用有效性检查、新增「第三方工具兼容」小节（禁止用该 App 的
ingest 写 wiki——它会重写页面、丢弃 `renders:` 字段、整篇覆写 overview，且「每源必建 source 页」与本仓库
「事件是证据，论点才是资产」相反；开启其 source 监听须排除 output/briefs 并去掉 html 扩展）；
修正「本仓库不是 git 仓库」的过时表述；`updated` bump 规则新增纯机械迁移例外。
（6）`.gitignore` 加 `.llm-wiki/`。涉及 9 个 wiki 页面的 `raw/sources/...` 路径改写，按新例外条款未 bump
`updated`（避免把 5 份 output/ 派生视图集体错标为过期）。本条之前的 log 条目中的 `raw/articles/...` 路径
按旧布局理解——log 只追加不修改。页面数与素材数不变（37 / 14）。

## [2026-07-29] schema | 重排 AGENTS.md 结构并统一 frontmatter 写法
只动组织与表述，不新增或删除任何规范条目（已用关键词全量比对验证：旧版全部规范性表述在新版均有对应）。
（1）**顺序重排**：铁律从文末提到开头（7 条，原 6 条——把"论断必有出处"与"不虚构"合并，
新增"沉淀判断不沉淀事件"和"不得出现第二事实源"两条）；核心操作三节从第 173 行提前到第 95 行，
`briefs/`、`output/` 两个长约定层从中部移到文末——每次会话必读的内容不再被它们挤到后面。
（2）**去重**：删除只剩一条操作规则的「领域说明」小节（范围定义权威已在 `wiki/purpose.md`，
那条"同一实体横跨领域用一个 entity 页 + 多标签"并入「页面约定」）；briefs 的晋升流程不再重述
research 沉淀流程，改为引用铁律 4 与核心操作 1；页面类型选择规则集中到「页面类型怎么选」一处。
（3）**修正三处不一致**：frontmatter 模板的 `sources` 从行内数组改为块状列表——行内写法会被第三方
解析器在第一个 `]` 处截断丢条目，且全库 37 页实际都用块状列表，模板此前与实际不符；模板补上
`renders:` 字段；Ingest 步骤 3 补上 `-源摘要` 后缀（原表述"文件名与 raw 文件同名"与"全库文件名唯一"
自相矛盾）；lint 计数命令统一为一条（原有 `find` 与 `ls wiki/**/*.md` 两个口径，后者会误算聚合文件）。
（4）**表格化**：log 前缀的六类含义与必记规则改为表格；lint 检查拆分为"需要判断"与"确定性"两组。
`wiki/schema.md` 同步 frontmatter 示例。行数 300 → 319：去重省下的部分被新增的 log 前缀表、
`sources` 写法说明和 lint 分组抵消，净增 19 行。


## [2026-07-29] schema | 合并 storm-project-analysis worktree 分支
把 worktree 分支 `claude/storm-project-analysis-7d24c3`（1 个提交 `bb5d719`，分叉于 `24e691d`）合并进 main。
它基于布局迁移之前的旧结构，故 6 处冲突全部与迁移相关，逐项解法如下：
（1）新增的 `2026-06-21-知乎-Stanford-STORM方法.md` 被 git 的目录改名检测自动落到新路径
`raw/sources/articles/`——上面两条 STORM 日志里写的 `raw/articles/` 按旧布局理解（log 只追加不修改）。
（2）`index.md`、`log.md` 的 rename/modify 冲突：保留 main 的新位置与新路径前缀，并入对方新增的
3 个条目（STORM 两页 + STORM 存档），计数改为页面 39、素材 15。
（3）log 按真实时间顺序排列：对方三条（今日 12:34 前完成）置于我今日两条 schema 之前。
（4）`overview.md`、`building-effective-agents.md`、`llm-wiki-方法论.md` 的内容冲突按"main 的较新版本
+ 并入对方独有内容"解：正文取 07-28 已校正过的版本（对方版本基于 07-27 的旧文），
新增对方的「AI 知识策展与研究方法论」板块、STORM 相关的 Simplicity 反面边界与互补关系表。
（5）对方新增文本中的半角标点已统一为全角，与全库中文正文一致。
两个新页 `sources` 均为块状列表，符合当日新规，无需改写。
遗留：`overview.md` 现 65 行（frontmatter 21 + 正文 44），超 AGENTS.md 的 ≤60 上限——
对方 lint 条目已溯源为 frontmatter `sources` 罗列内部页面构成第三份副本，该 schema 改动待用户确认，本次未动。

## [2026-07-29] schema | 移除知乎 STORM 存档并降级相关论断
用户判定该存档质量不足，明确要求移除，遂删 `raw/sources/articles/2026-06-21-知乎-Stanford-STORM方法.md`。
移除理由（三条叠加）：二手转写（自述转自 `x.com/heynavtoor` 推文）、非全文 verbatim 只是摘录、
原 URL 本机实测不可达（curl 裸请求与浏览器 UA 均 HTTP 000，而 DNS 解析与 443 连通均正常，
故属"受限未证实"而非确认失效）。内容仍可从 git 取回：
`git show 88c8ad8:"raw/sources/articles/2026-06-21-知乎-Stanford-STORM方法.md"`。

善后：（1）[[STORM-知识策展系统分析]] 的 `sources` 用 URL + 检索日期替代原双链；该页
「二次传播中的"去机制化失真"」小节加显式降级说明——核对表的逐条对照是基于已移除的存档做出的，
重新引证须改用活样本。论断与核对表未删，只标注证据强度下降。
（2）同批检索发现该失真不止 1 个样本：英文侧至少 6 个同源内容（note.com、两个 substack、
GitHub 仓与 gist、Medium）复现同一组特征——固定五角色、"不需要任何软件"、
"25% 优于 the best alternative method"（那个不存在的"第二名"）、"5 分钟 vs 40–60 小时"。
已作为**待核验线索**列入该页（仅见检索标题与摘要，未逐篇实读，故不充当证据）。
（3）[[overview]] 活跃线索改为"英文侧已见 6 个同源样本，升格条件已满足，待逐篇实读后建 topics/ 页"。
（4）index 删 raw 条目，素材计数 15→14；页面数 39 不变。
（5）AGENTS.md 铁律 1 补一句：raw/ 的删除或移动仅在用户明确要求时执行、须记 log 并善后引用，
agent 不得自行发起。

遗留：本 log 早前条目里的 `[[2026-06-21-知乎-Stanford-STORM方法]]` 双链自此悬空——log 只追加不修改，
这是历史记录的正常代价，不算意外悬链。`overview.md` 仍为 65 行（超 ≤60），frontmatter sources 的
第三份副本问题仍待你决定。

## [2026-07-29] schema | overview sources 去内部副本，清理已合并 worktree
（1）**schema 变更**：`wiki/overview.md` 的 `sources` 不再罗列内部页面，只列外部 URL；当前无外部来源，
写作 `sources: []`。理由是 [[STORM-知识策展系统分析]] 沉淀时那次 lint 的溯源结论：罗列内部页会让
"正文双链 / index 条目 / frontmatter" 成为同一事实的三份副本，每加一页要三处同步——正是
[[代码与文档漂移的本质]] 所述漂移温床。内部关联由正文双链 + `wiki/index.md` 承载，不丢可溯源性。
直接效果：overview 从 65 行降到 49 行，回到 AGENTS.md 的 ≤60 以内（此前连续两次日志都在报超标）。
规则已同步写入 AGENTS.md「页面约定」与 `wiki/schema.md`。
（2）**清理 worktree**：`git worktree remove .claude/worktrees/storm-project-analysis-7d24c3`，
并 `git branch -d claude/storm-project-analysis-7d24c3`（用 -d 而非 -D，删除成功即证明内容已全部
合入 main）。该副本是布局迁移前的旧结构，留着会让任何全库 grep 同时命中新旧两套路径。
（3）体检确认：页面 39 / 素材 14 与 index 一致，无冲突标记，三个 symlink 可解析，wiki 页内无旧路径残留。

## [2026-07-29] research | 去机制化失真：7 个样本实读取证并升格为论点页
承接上一条留下的待核验线索：逐篇抓取实读 7 个英文/日文样本（gist thevillagehacker、
secondbrainn.substack、linas.substack、note.com Claude Code研究所、medium Yanli Liu、
mikareyes.com、github hadufer/claude-storm），按四个失真标记逐条核对，新建
[[AI方法论的去机制化失真]]（8 行证据点表，含已移出 raw 的知乎样本）。

关键结论：
（1）**论点成立且比原判断更精确**。原判断（[[STORM-知识策展系统分析]]）认为失真是"保留名字数字 →
抽掉机制 → 包装可复现"的三步打包模式；实读后修正为**四个特征可分离、各自独立传播**。
（2）**M4「杜撰缺陷 + 自评补丁」传播力最强且零反例**：4 个样本明确出现，包括那个把检索
真正实装回去的 GitHub 项目也照抄了"the system does not critique itself"。综合：
M4 是四项里唯一给出**可执行动作**的，其余三项只是描述——能被复制粘贴的错误比只能被相信的错误传得更远。
该自评步骤恰好踩中 [[Evals]] 记录的 LLM-as-judge 自我偏好偏差。
（3）**出现三个反例，二次传播不等于必然失真**：linas.substack 把 25/10 的比较对象准确写成
"outline-driven retrieval-augmented baselines"；mikareyes.com 明确披露官方 STORM 会联网检索；
hadufer/claude-storm 用 subagent + 真实 web search 把机制装了回去。故正确表述是
**"失真沿最省力的路径发生"**——需要工程实现的环节最容易被砍，只需复制一句话的最难拦。
（4）**传播链形态**：样本集中在 2026-06-18 → 07-08 三周内，跨中日英三语、六个平台；
同一杜撰措辞在四种语言里同构出现（next best method / best alternative method / 第二名 / 次点の手法），
指向共同上游而非各自读错。最早观测样本是 06-18 的 gist，与知乎版自述"转写自 X 推文"的时间吻合。

横向更新：[[STORM-知识策展系统分析]]（待核验线索段替换为已核验结论 + 指向论点页）、
[[Evals]]（补自评不可靠的传播学证据）、[[代码与文档漂移的本质]]（补一条：表达漂移在公共知识
传播链上的形态，且仓库内的派生生成手段在跨主体传播中失效，只能靠接收端识别方法兜底）、
[[overview]]（活跃线索改为已沉淀 + 知识策展板块补链接）、index（页面 39→40）。

证据边界：3 个样本（secondbrainn、linas、medium）有付费墙，只能确认可见部分，证据表已逐条标注
"未确认"；引语经抓取工具提取，未逐字人工校对，结论建立在多样本一致性而非单条措辞上。
未把这些网页存入 raw/：均为活链接可随时复核，关键措辞已逐条记入证据表——与知乎样本不同，
那篇是原文本身已不可达才需要存档（而该存档因二手转写、非全文，已按质量要求移除）。

## [2026-07-29] lint | 全库健康检查（布局迁移 + STORM 沉淀后）
ingest 无操作：`raw/` 14 个素材全部已处理（3 份 OKF 文件合并为 1 个源摘要页；Karpathy 原文与 arXiv
论文按"sources 按需"规则由承载页溯源），无新投喂。

**确定性项全部通过**：页面 40 / 素材 14 与 index 一致；40 页 frontmatter 四字段齐全；孤儿页 0；
意外悬链 0（仅 2 个有意待写页 [[per-seat 定价的黄昏]]、[[system-of-record 与专有数据护城河]]）；
overview 50 行（迁移前 65）；两个 topics 页表头统一；三个 symlink 可解析；5 份 HTML 均零外部资源加载。

**外链 132 个**：108 × 200；16 × 403、3 × 401、1 × 429、1 × 412、1 × 406 属反爬或付费墙；
2 × 000（McKinsey agentic AI 报告、当当书页）本机 GET/HEAD 均不可达。**无一个 404/410**，
按既有口径不计死链。附带修正：知乎 STORM 文 URL 本次返回 **403**（昨日为 000）——
403 说明服务器响应后拒绝，比"不可达"更支持"页面可能存在、只是拦爬虫"，应据此精确
[[AI方法论的去机制化失真]] 证据表的备注。

**本次新发现 7 项**：
（1）**[[MCP]] 页版本过时（上次 lint 预留的复核项已确认）**：官网 `/specification/latest` 的 schema
路径与全部子页链接均已切到 **2026-07-28**，而本页第 47 行仍写"规范版本 2025-11-25 定义两种标准传输"。
新版还引入 Extensions 机制（Tasks / Skills over MCP / MCP Apps）、Elicitation 作为 client feature、
"stateless self-contained requests + per-request capability negotiation"——直接触及
[[从知识图谱到 Agent 编排]] 关于"MCP 不是编排层"的判断、[[Agent 记忆架构]] 的 Skills 定位与
[[building-effective-agents]]。需一次小 research 后横向更新。
（2）**lint 规则与 symlink 冲突（本次迁移引入）**：文件名唯一性检查按 basename 判定，把根目录
`purpose.md`/`schema.md` 两个 symlink 报成与 `wiki/` 下真身重名。实际风险低（全库无 `[[purpose]]`／
`[[schema]]` 双链），但规则应显式排除 symlink，否则每次体检假报 2 条。同理 `http://www.w3.org/2000/svg`
是 SVG 命名空间 URI 而非文档链接，应从外链检查排除。
（3）**`output/` 根目录有 4 份存量 HTML 不在 personal/ 或 shared/**：ai-doc-consistency、
cowork-cloud-mode、可持续文档代码一致性方案、罗伯特智能体问答系统方案。schema 只定义两个子目录，
这 4 份按"存量或来源不明一律视为已对外发出"处理：不覆盖、不删除、不改写，待用户决定归位方式。
（4）**1 份派生视图确定性过期**：`output/可持续文档代码一致性方案.html` generated 2026-07-16，
源页 [[论代码与文档漂移解决方案]] updated 2026-07-27。因该文件属存量件，重渲染不能原地覆盖，
需另存带日期新文件，待用户决定。
（5）**3 份 HTML 缺 canonical-source + generated**（上次已报未修）：补 meta 需改文件，与存量件
冻结原则冲突，需用户裁定优先哪一条。
（6）**4 份 HTML 无任何 wiki 页 `renders:` 声明**，仅工程手工书那份有。违反"wiki 页要知道自己有
哪些派生视图"，且这是纯改 wiki 页即可补齐的低风险项。
（7）`output/personal/工程手工书推荐与书vsAI对比.md` 仍滞留（上次已报未修）——`output/` 只应放
渲染结果，Markdown 留此构成第二事实源。

**旧项仍开放 3 组**：
（8）[[Claude Cowork]]（updated 2026-07-16）仍写"运行在桌面端""在所有付费计划的桌面应用中提供"，
而仓库内 `output/cowork-cloud-mode.html` 讲的正是云模式，sources 里还有一条 softonic
"Cowork comes to mobile and the web"。**同一事实在 HTML 里比 wiki 页新**——生命周期漂移的活标本，
07-27、07-28 两次 lint 均已报。
（9）[[论代码与文档漂移解决方案]] 638 行，为第二长页（280 行）的 2.3 倍，偏离"宁可多建小页"约定。
（10）三个概念被多页引用却无独立页：Attested Computation（6 页）、Knowledge Catalog（6 页）、
System of Record（4 页 + 3 页小写形式，且已是显式待写悬链）。

本次只报告并记日志，未修改任何 wiki 页或 output 文件，待用户确认后分批修复。
## [2026-07-30] external delete | articles/2026-06-21-知乎-Stanford-STORM方法.md

Deleted 1 source file and 0 wiki pages.

## [2026-08-03] ingest | Simon Willison 对 Claude Code 团队的访谈
依据公开可读的编辑版访谈，新增中文结构化研究摘录
`raw/sources/articles/2026-07-21-Simon-Willison-Claude-Code团队访谈.md` 与
[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]；采用逐节转述，不复制或逐句翻译整篇原文。

关键沉淀：Claude Tag 的 65% 仅指 Claude Code 产品工程团队提交的 PR；核心区仍由 code owner 人工批准，
外围区经过六个多月对照验证后才逐步自动 review；事故 PR 和用户反馈被编译进能力 / 行为 eval；最前沿模型的
系统提示缩短 80% 是模型特定结果；团队记忆当前为每频道一个 Markdown 文件。安全效果、65% PR 与体验改善
均属公司员工自报，缺少外部审计或结果对照。

横向更新 [[Anthropic-AI原生SDLC治理循环]]、[[Evals]]、[[Agent 记忆架构]]、[[生产力-体验悖论]]、
[[Anthropic]]、[[agent-生产级落地的鸿沟]] 与 [[overview]]；index 素材 14→15、wiki 页面 40→41。

## [2026-08-03] ingest | articles/2026-07-21-Simon-Willison-Claude-Code团队访谈.md

## [2026-08-04] research | Claude Tag 驱动的团队研发流程
基于 [[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]、[[Anthropic-AI原生SDLC治理循环]]、
[[Loop Engineering]]、[[Specification-Driven Development]]、[[Evals]] 与 [[Agent 记忆架构]]，新建
[[Claude Tag 驱动的团队研发流程]]。

综合结论：团队协作频道应作为事件入口而非规格真相源；Claude Tag 承担常驻协调与常规异步执行，Claude Code
承担复杂交互式实现；变更以规格、代码、测试 / eval、演示、风险和审批组成证据包；核心区保留 owner 人工审批，
外围区经 shadow mode 和历史失败覆盖后按风险逐步放权；内部试用与生产事故最终回灌测试、eval、规则、Skills
和团队记忆。流程是跨页综合推断，不是 Anthropic 发布的正式 SOP。

横向更新 [[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]、[[Loop Engineering]]、
[[Specification-Driven Development]]、[[Anthropic-AI原生SDLC治理循环]]、[[Agent 记忆架构]] 与 [[overview]]。
同时发现外部自动化已生成未索引的重复页
[[8-articles--41-2026-07-21-simon-willison-claude-code团队访谈--12vp8xo]]；未修改或删除该页，index 将其标为
非权威待处理。因此本次 index 页面计数 41→43（新增 1 个分析页 + 补记 1 个既有外部重复页），raw 仍为 15。

## [2026-08-04] lint | 全库结构、链接、事实保鲜与派生视图体检
检查全部 15 份 raw 素材与 43 个 wiki 页面，并按最近 10 页 + 固定随机 10 页抽查内容；核验 125 个外链、
5 份 HTML 和 1 份 `output/personal/` Markdown。

通过项：index 计数与实际一致、无重名 wiki 文件、index 无漏页或失效条目；除下述外部重复页外，页面 frontmatter
符合约定；全库仅有 [[per-seat 定价的黄昏]] 与 [[system-of-record 与专有数据护城河]] 两个已明确标注的待写悬链；
新建的 [[Claude Tag 驱动的团队研发流程]] 有多条入链。`wiki/overview.md` 为 51 行，两个 `topics/` 页表头统一，
根目录 symlink 均有效。125 个外链未发现确定的 404/410；48 个返回 200、54 个返回 206、14 个返回 403，
另有 note.com、当当与 3 条 Reuters 链接因访问限制仍无法判定。5 份 HTML 均无外部资源依赖。

发现项：
（1）[[8-articles--41-2026-07-21-simon-willison-claude-code团队访谈--12vp8xo]] 与
[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]] 内容重复，且前者为孤儿页、使用行内 `sources`、
空标签和错误 raw 路径；它是外部工具写入的第二事实源，违反唯一写手约定。
（2）[[Claude Cowork]] 仍写成仅桌面端、仅付费桌面应用可用；Anthropic 2026-07-07 官方资料与当日帮助中心已说明
Cowork 可在 web / mobile 运行云端会话，部分本地能力才依赖 desktop bridge。当前 `cowork-cloud-mode.html` 的事实
反而新于 canonical wiki，出现派生视图倒挂。
（3）[[MCP]] 仍把 2025-11-25 写作当前协议版本；官方 latest 已指向 2026-07-28，并新增逐请求能力协商、
Elicitation 及 Tasks / Skills over MCP / MCP Apps 扩展。其“MCP 不是编排层”的核心边界仍成立。
（4）`output/` 根目录 4 份来源不明的 HTML 未归入 personal/shared、均未登记在 `renders:`；其中 3 份缺少
`canonical-source` 与 `generated`，`可持续文档代码一致性方案.html` 的 canonical 页已晚于 2026-07-16 生成日期。
`output/personal/工程手工书推荐与书vsAI对比.md` 仍是呈现层中的第二份可编辑正文。
（5）[[STORM-知识策展系统分析]] 与 [[AI方法论的去机制化失真]] 仍把知乎源状态写为 HTTP 000；当前为 403。
前者保留了已删除 raw 文件的恢复命令，严格路径检查会持续将它报告为失效路径，但它不是现行事实引用。
（6）[[论代码与文档漂移解决方案]] 仍有 638 行，显著长于其他页面；Claude Code 已在 18 个文件出现，现已达到
独立实体页候选标准。System of Record 仍是优先级较高的待写概念；Attested Computation、Knowledge Catalog
已有跨页覆盖，独立建页优先级较低。
（7）日志中仍有不符合前缀规范的 `external delete` 条目，以及一条无正文的重复 ingest 条目；日志 append-only，
本次不回写历史。

本次只报告并追加日志，未修复、删除、重渲染或改动任何知识页面。

## [2026-08-07] ingest | AI 编码技术债三层治理用户研究草稿
将用户提供的多源综合草稿原样存入
`raw/sources/notes/2026-08-07-AI编码技术债三层治理-用户研究草稿.md`，新增
[[2026-08-07-AI编码技术债三层治理-用户研究草稿-源摘要]]。逐项回查 Sonar、Janea Systems、
ACM Queue / arXiv、Matt Pocock 仓库、Medium 及工具官方文档；明确草稿是研究线索而非一级事实源。

关键校正：Janea 来源是企业博客而非白皮书；Storey 原文没有 Automated / Assistance / Control 分层；
`.cursorrules` 已是 Cursor legacy，Claude Code 使用 `CLAUDE.md`，未核验到 `.claudeprotocol`；15 通常指
单函数 Cognitive Complexity，而非通用圈复杂度；Sonar way 的新代码重复率默认门槛是 3%。

## [2026-08-07] research | AI 编码技术债的三层治理
新增 [[AI编码技术债的三层治理]]，把“规则前置、机器卡点、人工收拢”重构为意图、证据、责任三层闭环：
确定性门禁负责底线，概率型 AI review 作为辅助证据，人按风险保留架构、批准和异常处置权；同时引入
technical / cognitive / intent debt 三债模型，强调自动生成文档不能替代真实的系统理解。

横向更新 [[Specification-Driven Development]]、[[生产力-体验悖论]]、[[Anthropic-AI原生SDLC治理循环]]
与 [[overview]]；index 素材 15→16、wiki 页面 43→45。


## [2026-08-07] ingest | AI编码技术债三层治理用户研究草稿

- 摄入 `raw/sources/notes/2026-08-07-AI编码技术债三层治理-用户研究草稿.md`（用户多源研究草稿，只读存档）。
- 生成源摘要页 [[2026-08-07-AI编码技术债三层治理-用户研究草稿-源摘要]]，逐项校正来源等级：SonarSource、Janea Systems、ACM Queue、arXiv 均无可核验 URL/作者/年份，标注"来源不可核验"；Matt Pocock 与 Medium 文章有链接，可核验。
- 新建实体页：Sonar、Janea Systems、Skills for Real Engineers、Matt Pocock、SonarQube、CodeRabbit。
- 新建概念页：大苦工转移、认知债与意图债、[[Automated Gates + Human Judgment]]、规则前置机器卡点人工收拢。
- 明确标注：圈复杂度 >15、重复率 >5% 为用户自拟门槛，非权威标准；"最昂贵的代码是几乎可以运行的代码"无出处，不作为可溯源论断。
- 待办：SonarSource 53% 数据、Janea Systems 白皮书、ACM Queue 论文、arXiv 论文是否值得联网检索补全；认知债与意图债是否需要独立概念页（当前并入 认知债与意图债）。

## [2026-08-07] schema | 隔离外部自动摄入的重复页面
新增 raw note 后，第三方 llm-wiki 文件夹监听器未经授权写入 1 个重复 source 页、6 个一次性 entity 页、
4 个拆得过细的 concept 页，并向 index 追加非本仓库格式的 `Recently Updated`；同时追加了上一条 ingest 日志。

这些页面把已完成联网核验的来源误报为“不可核验”，与
[[2026-08-07-AI编码技术债三层治理-用户研究草稿-源摘要]] 和 [[AI编码技术债的三层治理]] 冲突，构成第二事实源。
本次删除上述 11 个尚未提交的外部生成 wiki 页并移除错误 index 区块；不修改 append-only 的外部日志原条目，
以本条声明其内容及所列新建页面作废。raw 用户草稿未改动。

## [2026-08-07] ingest | AI 辅助编码的两篇学术原始论文
按用户要求仅归档原始 PDF，不生成源摘要页或继续改写知识页面：

- `raw/sources/pdfs/2026-From-Technical-Debt-to-Cognitive-and-Intent-Debt-arXiv-2603.22106.pdf`：
  Margaret-Anne Storey，作者版本来自 https://arxiv.org/pdf/2603.22106 （检索于 2026-08-07）；
  对应 DOI https://doi.org/10.1145/3807966。该文提出三债概念模型，未提供实证研究设计。
- `raw/sources/pdfs/2026-Twelve-Quick-Tips-for-AI-Assisted-Coding-in-Science-PLOS.pdf`：
  Bridgeford 等，PLOS Computational Biology，正式版本来自
  https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1014428&type=printable
  （检索于 2026-08-07），DOI https://doi.org/10.1371/journal.pcbi.1014428；属于同行评审的实践指南，
  不是治理效果的实验性验证。

两份 PDF 均已完成文件类型、页数、首页元数据和逐页渲染检查；index 素材 16→18，wiki 页面仍为 45。


## [2026-08-07] ingest | From Technical Debt to Cognitive and Intent Debt (arXiv:2603.22106)

- 摄入源：`pdfs/2026-From-Technical-Debt-to-Cognitive-and-Intent-Debt-arXiv-2603.22106.pdf`（Margaret-Anne Storey，University of Victoria）。
- 新建源摘要：`wiki/sources/4-pdfs--69-2026-from-technical-debt-to-cognitive-and-intent-debt-arxiv-260322106--1k0i5ya.md`。
- 新建概念页：kognitive-schuld、intent-schuld、cognitive-surrender、triple-debt-modell。
- 新建实体页：margaret-anne-storey。
- 横向连接：[[AI编码技术债的三层治理]]（Triple-Debt-Modell 与三层治理模型的关系待用户决策）、[[代码与文档漂移的本质]]（意图债作为第三层）、[[Specification-Driven Development]]（Intent-first workflows）、[[生产力-体验悖论]]（Cognitive Surrender 机制）、[[agent-生产级落地的鸿沟]]（意图债解释生产失败）、[[2026-07-21-Simon-Willison-Claude-Code团队访谈-源摘要]]（Willison 被引用）。
- 待办：Triple-Debt-Modell 与 [[AI编码技术债的三层治理]] 是替代还是补充；是否显式记录与其他 "Cognitive Debt" 用法的区分；是否深化与 [[Open Knowledge Format]] 的连接。

## [2026-08-07] ingest | Twelve Quick Tips for AI-Assisted Coding in Science (PLOS)

Ingest do PDF `pdfs/2026-Twelve-Quick-Tips-for-AI-Assisted-Coding-in-Science-PLOS.pdf` (Bridgeford et al., PLOS Comput Biol 22(7): e1014428, 2026-07-27).

Criados:
- `wiki/sources/4-pdfs--61-2026-twelve-quick-tips-for-ai-assisted-coding-in-science-plos--1lsjo1l.md` — resumo do artigo.
- `wiki/concepts/paper-tests.md` — modo de falha de testes gerados por IA.
- `wiki/concepts/context-rot.md` — degradação de desempenho do LLM com contexto longo.
- `wiki/entities/eric-bridgeford.md` — autor principal.
- `wiki/entities/russell-poldrack.md` — autor sênior; recurso "Better Code, Better Science".

Conexões identificadas (para atualização futura de páginas existentes):
- [[produtividade-experiencia-paradoxo]]: evidência de RCTs (Becker & Rush 2025) e GitClear (200M+ linhas) — fonte revisada por pares.
- [[specification-driven-development]]: Tips 4 e 7; cita GitHub Spec Kit.
- [[anthropic-ai-nativo-sdlc]]: Seção 3.3 (guardrails para agentes autônomos).
- [[evals]]: paper tests como modo de falha.
- [[agent-memoria-arquitetura]]: externally-managed context files.
- [[llm-wiki-metodologia]]: padrão CLAUDE.md/AGENTS.md validado via referência [10] (Perrone).

Nota: artigo é guia de práticas baseado em experiência, não estudo empírico de eficácia. Tensão potencial com [[ai-codigo-tecnica-divida-tres-camadas]]: artigo foca responsabilidade individual, wiki tem visão mais sistêmica.

## [2026-08-07] research | AI 编码治理的高质量证据地图
围绕“AI 编码是否提效、是否转移技术债以及如何治理”补充跨方法证据，新增
[[2026-08-07-AI编码治理高质量证据包-源摘要]]，横向更新 [[AI编码技术债的三层治理]]、
[[生产力-体验悖论]] 与 [[overview]]。

归档 9 份关键原始 PDF：Cui 等三家企业 4,867 人随机现场试验、Google 企业任务 RCT、METR 成熟开源仓库
RCT、NBER 超 10 万开发者生产遥测、Xu 等维护负担准实验、Perry / Sandoval 两项结论不同的安全用户研究、
DORA 生成式 AI 影响报告与 NIST SSDF 1.1。另核验 DORA 2025 AI Capabilities Model、OpenSSF AI 代码助手
安全指令指南和 GitHub Copilot Responsible Use / Code Review 官方边界。

核心校正：短期企业任务约 21%–26% 的加速与成熟仓库 19% 的减速可同时成立；代码 / commit 增长不会等比例
转化为 release 或用户采用；安全研究结果受任务、模型、界面和被试影响。由此把结论从“AI 必然制造技术债”
收紧为条件命题，并把本地试点指标扩展到感知—任务—PR—release—维护负担全链路。index 素材 18→27，
wiki 页面 45→46。

## [2026-08-07] ingest | NIST SP 800-218 SSDF v1.1 源摘要与概念沉淀

- 摄入 `pdfs/2022-NIST-SP-800-218-SSDF-v1.1.pdf`（NIST SP 800-218 v1.1，2022-02）。
- 新建源摘要页 `wiki/sources/4-pdfs--29-2022-nist-sp-800-218-ssdf-v11--1j09vnj.md`。
- 新建实体页：`wiki/entities/nist.md`、`wiki/entities/ssdf.md`。
- 新建概念页：`wiki/concepts/shifting-left.md`、`wiki/concepts/secure-by-design.md`、`wiki/concepts/root-cause-分析.md`。
- 横向关联：SSDF 的 shifting left 与 artifact-即证据定义关联 [[代码与文档漂移的本质]]；lessons learned 入 wiki 的要求关联 [[llm-wiki-方法论]]；与 [[Specification-Driven Development]] 建立互补关系。
- 待办：SSDF 与 AI-native SDLC 治理（[[Anthropic-AI原生SDLC治理循环]]）的对照分析尚未沉淀，PW.7 代码评审 vs 治理循环、RV.3 根因分析 vs 自动检测为开放问题。


## [2026-08-07] ingest | Perry 等 ACM CCS 2023：AI 编码助手安全实证研究

- 摄入源：`pdfs/2023-Perry-Insecure-Code-with-AI-Assistants-ACM-CCS.pdf`
- 新建页面：
  - `wiki/sources/4-pdfs--51-2023-perry-insecure-code-with-ai-assistants-acm-ccs--1bodlj6.md`（源摘要）
  - `wiki/analyses/ai-coding-安全实证.md`（分析）
  - `wiki/concepts/过度信任效应.md`（概念）
  - `wiki/concepts/prompt-交互模式.md`（概念）
  - `wiki/concepts/错误来源归因.md`（概念）
- 横向关联：[[Anthropic-AI原生SDLC治理循环]]、[[生产力-体验悖论]]、[[Evals]]、[[agent-生产级落地的鸿沟]]、[[AI编码技术债的三层治理]]、[[Loop Engineering]]
- 记录矛盾：与 Pearce et al. [21] 关于 AI 助手安全影响的分歧（多语言 vs 仅 C）

## [2026-08-07] schema | 再次隔离 PDF 监听器的越权写入
研究归档新增 PDF 后，第三方文件夹监听器再次绕过本仓库 schema，自动追加 NIST / Perry 两条 ingest 日志、
`Recently Updated` 区块，并生成 2 个 source、1 个 analysis、5 个 concept、2 个 entity 页面及 Sandoval 的
2 张中间图片。这些内容与本次人工核验的统一证据包重复，且会把 wiki 变成第二事实源。

本次删除上述 11 个未提交页面、错误 index 区块和 2 张可再生中间图片；遵守 append-only 约定，不改写外部追加的
两条 ingest 日志，以本条声明其“新建页面”和“横向关联”记录全部作废。9 份 raw PDF 原始存档保持不变。


## [2026-08-07] ingest | Sandoval et al. USENIX Security 2023 源摘要与概念页

- 新增源摘要页 [[sources/4-pdfs--39-2023-sandoval-lost-at-c-usenix-security--1187ww8]]：N=58 随机化用户研究，AI 辅助未显著增加 severe CWEs（非劣效性 δ=10%，p=0.04），63% 缺陷来自人类代码。
- 新增概念页 [[concepts/非劣效性检验]]、[[concepts/错误来源归因]]、[[concepts/过度信任效应]]、[[concepts/prompt-交互模式]]。
- 新增分析页 [[analyses/ai-coding-安全实证]]：对比 Sandoval et al. 与 Perry et al. 的矛盾与解释。
- 标注与 Perry et al. (ACM CCS 2023) 的矛盾：40% 建议含缺陷 vs 人类介入后风险小。

## [2026-08-07] ingest | Google AI 开发速度 RCT（arXiv:2410.12944）入库

- 新增源摘要页 [[2024-Google-AI-Development-Speed-RCT-源摘要]]：96 名 Google 工程师企业级 RCT，约 21% 速度提升（控制协变量后失去显著性 p=.086）；含与 Peng et al.（56%）和 Cui et al.（26%）的对比。
- 新增实体页 [[Google]]：作为企业级 AI 编码实证研究来源与对比基准。
- 新增概念页 [[Time on Task]]：生产力度量，与 [[Evals]]、[[生产力-体验悖论]] 关联。
- 横向关联：[[AI编码技术债的三层治理]]（生产力收益证据）、[[agent-生产级落地的鸿沟]]（企业环境效应量谨慎立场）、[[2026-08-07-AI编码治理高质量证据包-源摘要]]（已含该研究）。
- 注意：该研究未评估代码质量；与 METR 研究（资深维护者更慢）存在张力，需按任务类型区分。

## [2026-08-07] ingest | DORA 2025.2 生成式AI对软件开发的影响
- 摄入源：`pdfs/2025-DORA-Impact-of-Generative-AI-in-Software-Development-v2025.2.pdf`
- 新建源摘要：[[2025-DORA-生成式AI对软件开发的影响-源摘要]]
- 新建实体：[[DORA]]
- 新建概念：[[真空假说]]、[[小批量原则]]、[[对生成式ai的信任]]、[[ai采用学习曲线]]、[[可接受使用政策]]、[[反馈回路]]、[[DORA Core 模型 v2.0.0]]
- 新建主题：[[ai采用对软件交付的混合影响]]、[[ai采用规模化策略]]
- 新建分析：[[真空假说与价值悖论]]、[[dora-core模型v2与生成式ai测量框架]]
- 新建对比：[[个体流程收益与交付绩效下降]]、[[采用策略有效性]]
- 横向关联：[[生产力-体验悖论]]、[[agent-生产级落地的鸿沟]]、[[AI编码技术债的三层治理]]、[[Loop Engineering]]、[[Anthropic-AI原生SDLC治理循环]]、[[2025-METR-Experienced-OSS-Developer-Productivity-arXiv-2507.09089]]、[[2026-NBER-Writing-Code-vs-Shipping-Code-w35275]]、[[2026-Xu-AI-Programming-Maintenance-Burden-arXiv-2510.10165]]
- 记录矛盾：流程指标改善与交付绩效下降并存（报告自身标注意外）；有价值工作时间下降与福祉改善并存（真空假说未证实）；安全/隐私指南与可接受使用政策的影响方向张力。

## [2026-08-07] ingest | METR 资深OSS开发者生产力RCT

- 摄入源：`pdfs/2025-METR-Experienced-OSS-Developer-Productivity-arXiv-2507.09089.pdf`
- 新建源摘要页：[[4-pdfs--64-2025-metr-experienced-oss-developer-productivity-arxiv-250709089--b39c7s]]
- 新建实体页：[[metr]]、[[cursor-pro]]
- 新建概念页：[[ai-slowdown-σε-έμπειρους-προγραμματιστές]]、[[χάσμα-αντιληπτής-πραγματικής-παραγωγικότητας-ai]]、[[αντιστάθμιση-ταχύτητας-ευκολίας]]
- 新建对比页：[[σύγκριση-μελετών-παραγωγικότητας-ai]]
- 核心发现：AI 使资深开发者完成时间增加 19%（稳健性 14–25%），与开发者/专家预测的加速相反；21 因素分析（5 促成、10 模糊、6 排除）。
- 横向关联：[[生产力-体验悖论]]、[[AI编码技术债的三层治理]]、[[agent-生产级落地的鸿沟]]

## [2026-08-07] ingest | Cui et al. (2025) — Τρία Πειράματα Πεδίου με Προγραμματιστές

Εισήχθη το PDF `pdfs/2026-Cui-Generative-AI-Three-Field-Experiments-Software-Developers.pdf` (Cui, Demirer, Jaffe, Musolff, Peng, Salz — Φεβρουάριος 2025). RCT με 4.867 προγραμματιστές σε Microsoft, Accenture και Anonymous Fortune 100· κύριο εύρημα +26,08% στα pull requests (W-IV). Δημιουργήθηκαν:
- `wiki/sources/4-pdfs--66-2026-cui-generative-ai-three-field-experiments-software-developers--xkgtyu.md` — σελίδα πηγής
- `wiki/entities/github-copilot.md` — νέα οντότητα
- `wiki/entities/microsoft.md` — νέα οντότητα
- `wiki/concepts/weighted-iv-μεθοδολογία.md` — νέα έννοια

Σημειώσεις: Τα ευρήματα ετερογένειας αφορούν μόνο τη Microsoft και δεν είναι στατιστικά σημαντικά· το απορριφθέν πείραμα Accenture #1 έχει σοβαρά ζητήματα ποιότητας δεδομένων. Συνδέσεις με [[生产力-体验悖论]], [[agent-生产级落地的鸿沟]], [[Evals]], [[AI编码技术债的三层治理]], [[codex-agent-采用曲线]].

## [2026-08-07] ingest | NBER Writing Code vs. Shipping Code

Εισήχθη το NBER Working Paper No. 35275 (Demirer, Musolff, Yang, Μάιος 2026) "Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools".

Δημιουργήθηκαν:
- [[sources/4-pdfs--46-2026-nber-writing-code-vs-shipping-code-w35275--1u3zt81]] — πηγή σύνοψης
- [[analyses/nber-writing-code-vs-shipping-code]] — ανάλυση
- [[concepts/weak-link-υπόθεση]] — έννοια
- [[concepts/ιεραρχία-παραγωγής-λογισμικού]] — έννοια
- [[concepts/nested-ces-παραγωγή]] — έννοια
- [[entities/github-copilot]] — ενημέρωση
- [[entities/github-copilot-agent-mode]] — οντότητα
- [[entities/claude-code]] — οντότητα
- [[entities/openai-codex]] — οντότητα
- [[entities/nber]] — οντότητα
- [[entities/mert-demirer]], [[entities/leon-musolff]], [[entities/liyuan-yang]] — συγγραφείς
- [[entities/github-async-agent]], [[entities/github-pro]], [[entities/docker]] — εργαλεία/placebo
- [[entities/gharchive]], [[entities/similarweb]], [[entities/chrome-stats]], [[entities/sourceforge]], [[entities/fixest]], [[entities/jones-2026]] — υποστηρικτικές οντότητες

Κεντρικό εύρημα: τα κέρδη παραγωγικότητας εξασθενούν κατά μήκος της ιεραρχίας παραγωγής (commits 40%→140%→180%, releases 10%→20%→30%), συνεπές με weak-link υπόθεση και ελαστικότητα υποκατάστασης 0,25.

Σημειώθηκε αντίφαση με Becker et al. (2025) που βρίσκει μείωση παραγωγικότητας 19% σε RCT έμπειρων προγραμματιστών.

## [2026-08-07] ingest | Xu et al. (2026) — AI-Assisted Programming Maintenance Burden

Εισήχθη η μελέτη Xu et al. (Tilburg University, arXiv:2510.10165) για την επίδραση του GitHub Copilot στην παραγωγικότητα και το τεχνικό χρέος σε OSS έργα της Microsoft.

**Νέα αρχεία:**
- `wiki/sources/4-pdfs--57-2026-xu-ai-programming-maintenance-burden-arxiv-251010165--1pigsg2.md` — περίληψη πηγής
- `wiki/entities/github-copilot.md` — ενημέρωση με ευρήματα της μελέτης
- `wiki/entities/tilburg-university.md` — νέο
- `wiki/entities/feiyang-xu.md` — νέο
- `wiki/entities/poonacha-medappa.md` — νέο
- `wiki/entities/murat-tunc.md` — νέο
- `wiki/entities/martijn-vroegindeweij.md` — νέο
- `wiki/entities/jan-fransoo.md` — νέο
- `wiki/entities/curl.md` — νέο
- `wiki/entities/openssl.md` — νέο
- `wiki/concepts/pr-rework.md` — νέο
- `wiki/concepts/core-vs-peripheral-contributors.md` — νέο
- `wiki/concepts/vibe-coding.md` — νέο
- `wiki/concepts/speed-quality-paradox.md` — νέο
- `wiki/concepts/technical-debt-oss.md` — νέο
- `wiki/concepts/did-language-proxy.md` — νέο
- `wiki/analyses/xu-ai-programming-maintenance-burden.md` — βαθιά ανάλυση

**Κύρια ευρήματα:** Αύξηση παραγωγικότητας κυρίως από περιφερειακούς συνεισφέροντες (+43,5% commits), πτώση core contributors (−19% έως −42,9% commits), αύξηση PR rework (+2,4%) ως ένδειξη τεχνικού χρέους.

**Καταγεγραμμένες αντιφάσεις:** Με Peng et al. (2023) για καθαρά κέρδη παραγωγικότητας· με Hoffmann et al. (2025) για την κατεύθυνση ανακατανομής προσπάθειας.

## [2026-08-07] ingest | Vella & Blincoe (2026) — AI Coding Assistants Longitudinal Study

Ενσωμάτωση του πηγαίου PDF `pdfs/2026-05-25-arXiv-2605.23135-AI编码助手对软件工程的影响.pdf`:

- Δημιουργήθηκε η σελίδα πηγής [[sources/4-pdfs--41-2026-05-25-arxiv-260523135-ai编码助手对软件工程的影响--vuz1s]].
- Δημιουργήθηκε η ανάλυση [[ai-coding-παράδοξο-παραγωγικότητας-εμπειρίας]] με τα διαχρονικά δεδομένα του παραδόξου παραγωγικότητας-εμπειρίας.
- Δημιουργήθηκαν οι έννοιες [[supervisory-engineering-work]], [[productivity-experience-paradox]], [[trust-calibration]].
- Δημιουργήθηκαν οι οντότητες [[annie-vella]], [[kelly-blincoe]], [[university-of-auckland]], [[westpac-new-zealand]], [[royal-society-te-aparangi]], [[gemini]], [[stack-overflow]].
- Η μελέτη παρέχει διαχρονική τεκμηρίωση για το [[生产力-体验悖论]] και συνδέεται με [[agent-生产级落地的鸿沟]], [[Loop Engineering]], [[AI编码技术债的三层治理]], [[Evals]].
- Σημειώθηκε η μεροληψία επιβίωσης (84% αφορά συνεχιζόμενους χρήστες) και οι απειλές εγκυρότητας (δείγμα 85% άνδρες, αγγλόφωνοι, ενεργοί χρήστες AI).

## [2026-08-07] research | BMAD 项目文档治理方案草案

基于两位独立 Agent 专家的两轮评审与交叉质询，并复核 BMAD npm stable 6.10.0、main/next 的
Project Context、Workflow Map 与安装固定规则，新建 [[BMAD 项目文档治理方案]]。核心校正：不按文件名
静态分类 PRD/Architecture；区分计划、已实现未发布、已发布与回滚；Story Done 只捕获信息，Merge、
Release、Epic Close 分担调和与退役；先做两个 Sprint 的 depublish 试点，只让确定性检查阻断。
同步更新 [[论代码与文档漂移解决方案]] 的 BMAD 版本边界与指针，以及 index、overview。

## [2026-08-07] research | BMAD 文档治理草案重写为实施方案

根据用户审阅反馈，确认原稿混合了研究结论、专家评审和设计约束，不是一份易执行的方案文档。
原路径直接重写 [[BMAD 项目文档治理方案]]，正文改为问题、文档分工、逐类处理规则、交付事件、
存量清理、两周计划、完成标准与回退；BMAD stable/main 差异和设计依据移入附录。同步更新 index 与 overview，
未创建第二份事实源。


## [2026-08-10] ingest | A2E Agent Auditing Engine (arXiv:2608.07346)

- 摄入 PDF：`pdfs/2026-A2E-Agent-Auditing-Engine-arXiv-2608.07346.pdf`
- 创建源摘要页：sources/4-pdfs--46-2026-a2e-agent-auditing-engine-arxiv-260807346--hc32ar
- 创建概念页：agent-auditing
- 创建实体页：a2e-agent-auditing-engine
- ⚠️ 全文未完整提取：方法论、评估与结果部分缺失；实体/概念页基于有限内容，标注待全文审阅后更新
- 关联现有页面：[[agent-生产级落地的鸿沟]]、[[Anthropic-AI原生SDLC治理循环]]、[[Evals]]、[[从知识图谱到 Agent 编排]]、[[代码与文档漂移的本质]]

## [2026-08-10] ingest | A2E — Agent Auditing Engine (arXiv:2608.07346)

Εισήχθη το PDF `pdfs/2026-A2E-Agent-Auditing-Engine-arXiv-2608.07346.pdf` (A2E — Agent Auditing Engine, Shanghai Artificial Intelligence Laboratory).

Δημιουργήθηκαν:
- `wiki/sources/4-pdfs--46-2026-a2e-agent-auditing-engine-arxiv-260807346--hc32ar.md` — πηγή σύνοψης
- `wiki/entities/a2e-agent-auditing-engine.md` — ενημέρωση οντότητας με πλήρες τεχνικό περιεχόμενο
- `wiki/concepts/agent-task-protocol.md` — νέο concept (ATP)
- `wiki/concepts/lifecycle-aligned-evaluation.md` — νέο concept (μεθοδολογία 4 σταδίων)
- `wiki/concepts/harness-vs-model.md` — νέο concept (harness ≠ wrapper)
- `wiki/concepts/agent-auditing.md` — ενημέρωση με το A2E ως συγκεκριμένο εργαλείο
- `wiki/comparisons/agent-harness-αξιολόγηση.md` — σύγκριση A2E vs Inspect AI vs Phoenix

Βασικά ευρήματα: κανένα harness δεν κυριαρχεί παγκοσμίως· το correctness έχει περιορισμένη διακριτική ικανότητα (0.568–0.663) ενώ το token cost κυμαίνεται 3.5×· το harness δεν είναι ελαφρύ wrapper (case study LangGraph 10.122 tokens vs CrewAI 96.704 tokens).

Μεθοδολογικοί περιορισμοί που καταγράφηκαν: 5 tasks ανά κελί (resolution 0.20), οι συγγραφείς αποποιούνται την κατάταξη, ορισμένες μετρικές ορίζονται από το instrumentation όχι από τον agent.

## [2026-08-10] ingest | A²E 全轨迹评测与审计（全文校正）

下载并校验 arXiv:2608.07346v1 原始 PDF（18 页，SHA-256 `97a9829025fd1b33790e68b287c1c67c4d84b3b2e8a0323fc82e4f3cc63558f1`），逐页检查全文、图表与方法限制。新建 [[2026-08-07-A2E-Agent-Auditing-Engine-源摘要]] 与 [[Agent 全轨迹评测与审计]]，更新 [[Evals]]、[[从知识图谱到 Agent 编排]]、[[agent-生产级落地的鸿沟]]、[[agent-auditing]]、[[a2e-agent-auditing-engine]]、[[agent-task-protocol]]、[[lifecycle-aligned-evaluation]] 与 [[harness-vs-model]]。

下载时外部监听器自动生成了上方两条摄入日志及非中文页；本次已将其改为符合 schema 的中文页，把重复源页与未独立复核的横评页保留为已并入 stub。前两条日志为 append-only 追溯记录，其“全文未完整提取”与文件路径以本条校正为准。同步更新 index 与 overview。

## [2026-08-10] lint | 全库体检：外部自动摄入污染与链接一致性

检查范围为最近更新 10 页 + 固定随机种子抽查 10 页，并对 140 个 wiki 页、30 个 raw 文件、5 份 HTML 派生视图和全库外部 URL 执行确定性扫描。本次只报告，未修复内容。

- **通过**：全库无重名文件；index 页面数 140 / raw 数 30 与实际一致，无缺失或过期索引条目；`overview.md` 57 行；两个根目录 symlink 正常；topics 证据表头正常；frontmatter 均可解析。
- **P0 schema 污染**：85 页具有同一外部自动摄入特征（`type` / `related` + 非空行内 `sources: [...]`），且来源路径写成不存在的 `pdfs/...` 或 `articles/...`；其中 60 页正文大量使用希腊语，违反中文正文约定。
- **P1 链接结构**：排除 index / log 后有 44 个内容孤儿页（analyses 4、comparisons 3、concepts 6、entities 20、sources 9、topics 2）；发现 20 个可操作断链（含 `codex` / `evals` 大小写不一致），另有 4 处已明示标记的待写链接，不视为意外断链。
- **P1 派生视图**：`output/可持续文档代码一致性方案.html` 晚于源页；`ai-doc-consistency.html`、`cowork-cloud-mode.html`、`罗伯特智能体问答系统方案.html` 缺 `canonical-source` 和 `generated` meta。`output/shared/工程手工书推荐与书vsAI对比-2026-07-27.html` 通过。
- **P2 内容保鲜**：抽查页 `8-articles--41-2026-07-21-simon-willison-claude-code团队访谈--12vp8xo` 仍称“Claude Code 没有 entity 页、entities 不建人物页”，已与当前仓库状态冲突；属外部重复页过时，不是新论断冲突。
- **URL**：清理中文标点后未确认 404；4 个 URL 在 12 秒重试后仍无响应（Cursor rules、当当商品页、secondbrainn Substack、McKinsey Agentic AI 文章），需浏览器人工复核；401/403 按访问控制处理，未直接判为死链。

## [2026-08-10] lint | 全库复检：索引分类污染与元数据漂移

检查最近更新 10 页 + 固定随机种子抽查 10 页，并对 140 个 wiki 页面、raw、5 份 HTML 派生视图与
159 个清洗后的外部 URL 执行确定性扫描。本次只报告并追加日志，未修复、删除或重渲染。

- **通过**：无重名 wiki 文件；140 页均能在 index 某处找到；frontmatter 全部可解析；`overview.md`
  57 行；根目录两个 symlink 正常；4 个 topics 证据点表头统一；外链未确认 404/410。
- **P0 外部摄入污染**：85 页仍具有 `type` / `related` + 非空行内 `sources: [...]` 特征，合计 87 条
  source 路径写成不存在的 `pdfs/...` / `articles/...`；60 页正文大量使用希腊语。84 页只挂在 index 的
  非 schema `Recently Updated` 节，而未归入相应分类节。
- **P1 计数与保鲜**：index 把 `.DS_Store` 算入素材后写成 raw 30；排除系统文件后实际为 29（12 articles、
  2 notes、13 PDFs、2 assets）。`overview.md` 已加入 2026-08-10 的 A²E 内容，frontmatter `updated`
  仍为 2026-08-07。
- **P1 链接结构**：内容层有 44 个孤儿页（analyses 4、comparisons 3、concepts 6、entities 20、
  sources 9、topics 2）；8 个缺失目标 + 4 个大小写不一致目标，共 30 处链接；另有 2 个明确标注的待写页，
  不视为意外断链。`harness-vs-model` 是本轮 recent 抽查中的孤儿核心概念，主分析未回链。
- **P1 派生视图**：3 份根目录 HTML 缺 `canonical-source` / `generated`；
  `可持续文档代码一致性方案.html` 落后于 canonical 页；4 份根目录 HTML 均未登记 `renders:`；
  `output/personal/工程手工书推荐与书vsAI对比.md` 仍是第二份可编辑正文。shared 冻结版通过。
- **P2 内容与日志**：外部重复页仍声称 Claude Code 没有 entity 页、entities 不建人物页，与当前库状态冲突；
  log 仍有 1 条非法 `external delete` 前缀及 1 条空正文 ingest 记录。被删除 STORM raw 路径仅出现在明确标注
  的历史恢复说明中，按严格路径检查仍会报失效。
- **URL**：直接请求得到 133 个 200/206、19 个 401/403、7 个环境性 000；网页索引复核确认其中 Cursor、
  Linas Substack、Open Group、Anthropic、McKinsey 原页仍在，旧 `au.investing.com/...4361415` 有同文新 URL，
  当当商品页仍无法确认。未把访问控制或单次网络失败判为死链。

## [2026-08-11] lint | 全库深检：多智能体分簇复核，14 项判断类新发现

确定性扫描覆盖 140 个 wiki 页、29 个 raw 文件（不含 .DS_Store）、6 份 HTML；判断类检查由 7 个
检查员按知识簇分片深读、每条发现经独立怀疑者对抗复核（17 条原始发现 → 14 条成立、2 条驳回、
1 对重复合并）。本次只报告，未修复任何内容。

- **污染冻结确认**：85 个外部摄入污染页、44 个孤儿页、index `Recently Updated` 节均与 08-10 基线
  一致，08-10 14:04 后无任何文件变动；13 个已修改 wiki 文件经 diff 抽查均为本人历史会话的正当改动。
  已知问题（raw 计数 30→29、overview updated 滞后、output HTML meta 缺失、personal 第二正文、
  harness-vs-model 孤儿）全部维持原状，等用户决策。
- **新发现（确定性）**：`wiki/media/` 下有外部 App 于 08-07 生成的 7 个子目录、65 张 PNG（从摄入
  PDF 抽取），无任何页面引用，此前两次 lint 均未记录——属外部污染的遗漏部分。
- **P1 内容矛盾（2 项，复核确认）**：① [[AI方法论的去机制化失真]]「分特征统计」表 M2 行与证据点表
  自相矛盾（确认数应为 6 非 5，行总和 7≠8，linas 写在反例格却计 0）；② [[STORM-知识策展系统分析]]
  「停滞与商品化」节 OpenAI/Google Deep Research 的一组日期与数字完全无出处，违反铁律 3。
- **P2 内容问题（复核确认）**：③ 同页「三种语言/四种语言」同段自相矛盾且被 STORM 分析页复制；
  ④ [[a2e-agent-auditing-engine|A²E]] 实体页「开源」与同页「无 license」证据边界冲突；
  ⑤ [[Anthropic-AI原生SDLC治理循环]] 与其源摘要把原文「claude.ai 事故」限定词丢失，放大为全部
  历史事故；⑥ [[论代码与文档漂移解决方案]] §十指向 [[BMAD 项目文档治理方案]] 的描述仍是第一版
  草案内容（三容器/状态模型已不在现行页）；⑦ [[GraphRAG 与 Vector RAG]] 第 25 行「原视频」论断
  零溯源（视频出处只在 [[从知识图谱到 Agent 编排]] frontmatter）。
- **P2 缺失交叉引用（复核确认）**：⑧ [[cowork-saas-资本市场冲击]] 未回链自称其「必要对照」的
  [[agent-生产级落地的鸿沟]]；⑨ [[AI编码技术债的三层治理]] 与鸿沟页互不链接（源摘要关联页面已
  声明未落实）；⑩ [[Anthropic]] 实体页与 [[Claude Tag 驱动的团队研发流程]] 互不直链；
  ⑪ arXiv 2510.22254 与 PLOS pcbi.1014428 系同一论文（预印本/正式版，WebFetch 复核确认）被当两个
  文献分别引用，全簇无版本关系说明。
- **P2 概念缺页（复核确认）**：⑫ Claude Code 被 17 个正当页面提及却无正当实体页（唯一同名页是
  希腊语污染页，08-04 lint 已列为建页候选未落地，需与污染清理联动决策）；⑬ Agent Skills 三种语境
  （程序记忆/Plugin 组件/SDLC 回灌）14+ 页反复使用、零 [[Skills]] 双链、无独立页。
- **数据空白（未复核额度内，保留待判断）**：去机制化失真页推定的污染上游（x.com/heynavtoor 推文）
  零抓取记录，值得联网补查以核实"单点污染"结论与最早样本时间。
- **驳回（2 项）**：synthesis/ 目录缺失属 git 不存空目录的机械必然；ATP 页末句实为论文 p8 原文
  （"Registry support does not imply…end-to-end validation"），非未标注推断。
- **URL**：164 条清洗后 URL 中 138 条 200；22 条 401/403/406 全部为访问控制/反爬（含 Reuters、
  ACM/DOI、Gartner、Axios、知乎），维持不判死链；kubernetes.io 复试恢复；当当商品页仍无法程序化
  确认，且其移动域名 product.m.dangdang.com 证书只覆盖 *.dangdang.com（证书配置错误），建议改用
  出版社/ISBN 引用。McKinsey 维持"环境性不可达、网页索引确认存活"原判。


## [2026-08-11] ingest | Nav Toor STORM 四提示词长文（去机制化失真上游节点）

- 存档源：articles/2026-06-17-heynavtoor-Stanford-STORM四提示词长文.md（X 长文，2026-06-17 发布，2026-08-11 经 fxtwitter API 抓取）
- 新建源摘要页：[[8-articles--42-2026-06-17-heynavtoor-stanford-storm四提示词长文--afdfzq]]
- 更新 [[AI方法论的去机制化失真]]：证据表新增 2026-06-17 上游节点（早于 gist 样本一天；hadufer/claude-storm 署名来源；同作者 6-02 线程作为"主动删减"对照证据）
- 更新 [[STORM-知识策展系统分析]]：补充本文作为"去机制化失真"典型样本，强化"二次失真局限"论点
- 未新建实体页：Nav Toor 作为个人账号，价值仅在传播链中，不值得单独建页
- 开放问题：本文 4 个提示词全文未在存档中（Draft.js blocks 转 markdown 后提示词内容缺失），如需分析提示词质量需回查原文
## [2026-08-11] research | STORM 失真传播链上游节点取证 + Deep Research 论断核实

- **上游节点定案**：多渠道检索定位 Nav Toor（@heynavtoor）2026-06-17 X 长文本体（fxtwitter API 抓取，
  305 万 views），M1–M4 四特征逐项核验齐全，早于 gist 样本一天；hadufer/claude-storm README 署名直证
  上下游关系。同作者 2026-06-02 线程描述准确，证明失真是主动删减。因 Wayback/archive.today 等均无快照，
  按"研究中重要网页"存档 `raw/sources/articles/2026-06-17-heynavtoor-Stanford-STORM四提示词长文.md`。
  更新 [[AI方法论的去机制化失真]]（证据表 +上游行、统计并入第 9 样本、传播链形态改写）、
  [[STORM-知识策展系统分析]]、[[overview]]（上游悬念关闭）。
- **Deep Research 论断补源**：OpenAI 2025-02-02 发布（东京当地 02-03）、2026-02-10 GPT-5.2/MCP/可信站点/
  实时进度升级、Google 2026-04-21 Gemini API 公开预览 Deep Research/Max（93.3% DeepSearchQA 归属 Max）
  ——逐条核实并在 [[STORM-知识策展系统分析]] 补 URL+检索日期。

## [2026-08-11] lint | 体检修复执行（14 项全修）+ 外部 App 二次污染事件

执行 08-11 体检报告全部修复：① P1×2（[[AI方法论的去机制化失真]] 统计表重算 6/1/1 并纳入上游为 9 样本、
[[STORM-知识策展系统分析]] Deep Research 段补出处）；② P2 内容×5（三/四种语言矛盾两页同步修正、
[[a2e-agent-auditing-engine|A²E]] 去"开源"表述、claude.ai 限定词两页补回、[[论代码与文档漂移解决方案]]
§十 BMAD 指针更新、[[GraphRAG 与 Vector RAG]] 原视频补源）；③ 交叉链接×4（cowork-saas↔鸿沟、
三层治理↔鸿沟、[[Anthropic]]↔[[Claude Tag 驱动的团队研发流程]]、arXiv 2510.22254=PLOS pcbi.1014428
版本关系三页说明）；④ 新建 [[Claude Code]]、[[Agent Skills]] 两页并在 9 处裸文本补双链；
⑤ 当当失效链接换 megbook（户外篇 proID=4131466，已验证）；⑥ index raw/页面计数与 overview updated 校正。
共编辑 23 页 + 新建 2 页 + 存档 1 个 raw 文件。

**外部 App 二次污染事件（19:08–19:35）**：LLM Wiki App 的自动监听把本次新增 raw 存档自动摄入，
生成污染源页 `8-articles--42-...--afdfzq`，并整页重写 [[AI方法论的去机制化失真]] 与
[[STORM-知识策展系统分析]]（毁掉本会话修复），向本 log 追加一条非本维护者所写的 `ingest` 条目
（"Nav Toor STORM 四提示词长文"），并向 index Recently Updated 节添加条目。已从该 App 自身的
`.llm-wiki/page-history/` 快照完整恢复两页并重放全部修复。遗留待用户决策：污染源页 afdfzq、
App 伪造 log 条目、Recently Updated 新增行——与既有 85 页污染一并处置。**已建议用户关闭该 App
的 source 自动监听（按 AGENTS.md 第三方工具兼容节要求配置 excludeDirs）。**

## [2026-08-11] lint | 外部污染全量清理（经用户确认）

用户确认已关闭 LLM Wiki App 的 source 自动监听，并明确要求清理全部污染。执行：

- **删除 88 个 wiki 页**：86 个带外部摄入特征（frontmatter `type`/`related` 键 + 行内 sources）的
  污染页（entities 37、concepts 28、sources 10、analyses 6、comparisons 3、topics 2，含 08-03 的
  `8-articles--41...12vp8xo`、08-07 批次 84 页与今日的 `8-articles--42...afdfzq`），以及 2 个因污染
  处置而存在的已并入追溯 stub（`agent-harness-αξιολόγηση`、`4-pdfs--46...hc32ar`）。
- **删除 `wiki/media/` 整目录**：外部 App 从摄入 PDF 抽取的 65 张 PNG、7 个子目录，无任何页面引用。
- **index 善后**：移除非 schema 的 `Recently Updated` 整节及 3 条指向已删页的条目；页面计数 143 → 55；
  失真页描述行同步 9 样本新口径。
- **顺手清孤儿**：[[Agent 全轨迹评测与审计]] 补回链 [[harness-vs-model]]（两次 lint 点名的孤儿概念页归零）。
- **终检**：已删页在 log 外零残留引用；断链仅剩 2 处已标注待写标记；孤儿页清零；无重名；
  raw 30 / 页面 55 与 index 一致。
- **可恢复性**：被删文件均未入 git，不可从 git 恢复；App 侧 `.llm-wiki/`（lancedb、page-history）
  仍留有其自建副本；media 图片可从 raw PDF 重新抽取。log 中该 App 的 1 条伪造 `ingest` 条目与
  1 条历史 `external delete` 条目按"log 只追加"保留并已标注。

## [2026-08-27] research | SDD 收益主张的实证赤字
用户追问"SDD 的局限性 + 代码文档漂移"，联网研究后发现本库 SDD 线的证据基础偏乐观。
新建 [[SDD 收益主张的实证赤字]]（topics，7 条证据点表）：Brenn Hill 的 119 仓库 / 100,247 PR
within-author 分析显示五个厂商假设无一成立、规格与更高缺陷率（+1.4pp）和返工（+5.0pp）相关；
Scott Logic 单案例实测给出成本量级；arXiv 2605.01160 的 SGM 研究结论相反但方法学弱（无对照组、
排除初级开发者），矛盾已显式标注。
**校正本库既有偏差**：Scott Logic（2025-11-26）与 Hill（2026-04-28）均早于 [[SDD 开发规范研究]]
的沉淀时点（2026-07-16）却未被检索到——该页原"证据边界"不是谨慎而是偏乐观，已加修订说明并回填。
[[Specification-Driven Development]] 证据边界同步回填。
**新增原创综合**：[[代码与文档漂移的本质]] 加"SDD 与漂移的转化关系"一节——规格与代码之间同样没有
共同形式表示，故 SDD 未消除符合性漂移而是把它向上位移一层（代码偏离意图→规格偏离意图，并附赠
虚假合规证据），并部分转化为表达 + 生命周期漂移；价值主张应重述为"把难治的漂移换成好治的漂移"，
该交换只在配套建了调和机制时才划算。
[[AI方法论的去机制化失真]] 追加第二观测对象（2 个样本 + 新标记 M5 引文归属漂移）：本次检索工具的
自动摘要把 Scott Logic 的 10x 口径混淆（33.5/8≈4x，十倍实为含 review 的总时长），并归给 Kent Beck
一句其原文中不存在的引语。**失真载体从人写博客变为自动摘要**，原页"找上游节点"的结论在此失效。
更新 [[overview]] 的 SDD 板块、两条活跃线索与悬而未决（原问法预设了已被否定的前提）。

## [2026-08-27] research | Anthropic《The AI-Native SDLC Playbook》摄入
用户要求通读 https://claude.com/blog/the-ai-native-sdlc-playbook （Louis Claxton，2026-08-21）。
存档 `raw/sources/articles/2026-08-21-Anthropic-AI原生SDLC-playbook.md`（结构化存档，保留六阶段
13 个 play 的核心表述、全部配置/代码示例与全部度量指标），建 [[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]]。
新建 [[控制带]]（concepts）：按 σ 分层授予 agent 自主权、检测端完全确定性；本库补充其与 T0–T4
产物风险分级**正交**，组合成二维授权矩阵（产物风险问"做错了后果多大"，信号强度问"现在有多确定出事了"）。
更新 [[Anthropic-AI原生SDLC治理循环]]（补流程侧姊妹篇，两文是同一实践的安全切面与流程切面，
原文互相交叉引用）、[[Evals]]（新增"Agent 配置也要做回归测试"——CLAUDE.md/skills/hooks 变更触发
eval 套件并作为合并门禁，这是本库反复出现的"控制面自身会漂移"隐患的首个可操作机制）、
[[基于IT4IT的Agent知识治理]]（新增过渡期事实源三配置；"链接为最低标准"显式承认双事实源，
与铁律 7 不冲突因其要求关系可程序验证，但须约定收敛期限否则会稳定成永久双写）。
**边界标注**：全文零实证数据——每个 play 都有 leading/lagging indicator 但无任何测量值，
是度量框架而非效果证据；产品营销性质，全部 play 绑定 Claude 产品栈。已标注一处内部矛盾：
原文称人对每个判断决策问责，但 Stage 6 目标是调用路径上无人，且把 confidence gate 描述为
"确定性检查 **or** 对抗性审查 agent"——后者按本库实证边界是置信度信号而非授权来源，两者不等价。
本次共新增 3 页、1 个 raw 素材，更新 6 页（合并重算后全库：58 页、31 个素材）。

## [2026-08-27] schema | 全库清除自定义别名，统一使用官方名 Cowork
用户两次明确要求：仓库内不得出现该自定义别名，log 亦不例外。据此执行——
（a）wiki 页：[[Claude Cowork]] 的命名节改写为「命名与对外话术」，[[cowork-plugins-架构]] 的
mermaid、分层解释与历史资产告警去别名，两页因论断变化 bump `updated`；
（b）raw 资产：经用户明确授权，`raw/assets/` 下架构图 SVG 图内 3 处文字改为 Cowork，文件更名为
`cowork-plugins-mcp-architecture.svg`（**这是本仓库对 raw/ 内容的第二次授权改动，此前铁律 1 为只读**）；
（c）log：改写 2026-07-03 ingest 与 2026-07-16 lint 两条既有条目中的别名与旧路径，
并以本条替换 2026-08-27 首版条目——**append-only 约定被用户指令覆盖**；
（d）`wiki/index.md` 相关描述与资产路径同步。
可恢复性：全部改动均在 git 版本历史中可追溯与还原。
未发现 LiCloud / 融合云 相关内容。

## [2026-08-27] schema | 三工作区状态合一（lint 前置）
lint 启动时发现全库状态分裂：main 主 checkout 有 54 项未提交改动（07-30~08-27：A²E 摄入、外部污染
清理、STORM 上游取证、每日简报），两个 worktree 分支各有当日未提交工作（SDD 赤字研究 + playbook
摄入；别名清理），三方重叠修改 index / log / overview 同批文件——铁律 7 在并行 worktree 布局下被
事实破坏。经用户确认全部合一：主工作区先提交，两分支各自提交后依次合并进 main；11 处冲突逐项手工
解（updated 取新、sources 取并集、log 按真实时间序插入、index 计数重算 58 页 / 31 素材、overview
融合两侧新增并瘦身回 60 行）；按 07-29 合并先例校正被并条目中的过时计数。合并后全库复查别名零残留。
善后：合并时误将 tmp/ 临时目录纳入跟踪，已移出并加入 .gitignore（tmp/ 内有一份未摄入的
sonar-state-of-code-2026.pdf，待用户决定是否投喂）。

## [2026-08-31] lint | 全库体检（合一后）：确定性全绿，37 项判断类发现
确定性扫描：58 页 / 31 素材与 index 一致；frontmatter 四字段齐全且 sources 均块状列表；无重名、
无孤儿页、悬链仅 2 个有意待写；overview 60 行；3 个 topics 表头统一；2 个根 symlink 正常。
外链 170 条：141 通过；26 条 401/403/406 按访问控制不判死链；McKinsey 维持「环境性不可达」原判；
**首个确认 404**：BMAD 项目文档治理方案 sources 中 docs/how-to/install-bmad.md——已定位文档移至
docs/start/install-bmad.md，待修。派生视图：可持续文档代码一致性方案.html 仍过期（generated 07-16 <
源页 08-11）；**新增过期**：output/shared/工程手工书…-2026-07-27.html 落后于源页（书与AI 08-11 因
链接修复 bump）——shared 冻结件，如需更新须另存新日期文件，待用户裁定。

判断类（7 检查员分簇深读 + 逐簇对抗复核；37 项存留 / 0 项驳回）：
**P1×3**：① [[代码与文档漂移的本质]]「后两类可治理度高」与同页四类表（生命周期=中）矛盾，口径已
扩散到 [[SDD 收益主张的实证赤字]] 推论 3；② [[Anthropic-AI原生SDLC治理循环]] 正文称 playbook
「覆盖本页没有的 Plan/Design 阶段」，但本页控制面表首行即 Plan；③ [[基于IT4IT的Agent知识治理]]
把铁律 7 转述为「禁止的是未声明、无调和机制的第二事实源」——原文为无条件禁令，属对规则的重写。
**P2×16**：[[Claude Cowork]] 桌面端论断第四次报告未修（且 08-27 别名清理 bump 掩盖其过时）；
财报季跟踪线索已跨 Q1、Q2 两窗口未跟进；[[codex-agent-采用曲线]]←鸿沟/Meta 单向对照；
[[论代码与文档漂移解决方案]] 未反映 SDD 赤字且 §四 乐观表述残留；「实践者反复报告的失败模式」句
两页零出处；playbook 横向整合漏 [[Agent Skills]] 与 [[AI编码技术债的三层治理]]；
[[a2e-agent-auditing-engine]] 仅 1 条入链、三个 A²E 小概念页正文零双链；[[Evals]] 新节未内联
playbook 源摘要；[[MCP]] 规范版本第三次报告未修（2025-11-25 → 2026-07-28 版含 Extensions）；
失真页「六个平台」实为 7；[[llm-wiki-方法论]] 自引失实（「本页开头批评」应为 Karpathy 批评）；
[[STORM-研究提示词组]]↔失真页零互链；赤字页←失真页、←鸿沟页单向；overview 缺 Claude Code/Skills
入口；[[purpose|purpose.md]]「当前重心」未随 SDD 赤字更新；鸿沟页证据表未吸附 08 月新信号。
**P3×18**：shadow mode（11 页提及）与「调和机制」（11 文件）两个建页候选；cowork-plugins-架构
双页面类型标签；SDD 概念/规范页转述丢失 p=0.056 限定；赤字页日期列混用发表/检索日期；
playbook「同一实践两切面」与 A²E「隔离 POC」判断未标综合；[[控制带]]←解决方案页单向；
lifecycle 术语双义项未区分；失真页 M5 未进可操作清单、M4「5/5」口径、M5 悬置样本待检索、
STORM 分析页未反映第二观测对象、其「还剩什么价值」推断未标注；「Almost Works」引语待核验；
A²E license 快照已 17 天待复查；OKF v0.2 检索停在 07-28 待复核。
**旧项维持开放**：output 根目录 4 份存量 HTML（归位/meta/renders）、personal 第二正文 .md、
解决方案页 649 行、Attested Computation / Knowledge Catalog / System of Record 缺页。
本次只报告并记日志，未修复任何内容，待用户确认后分批执行。

## [2026-08-31] lint | 体检修复执行：批次一二三（31 项修复 + 1 项论断撤销）
按用户勾选执行批次一（库内修正）、二（链接与整合）、三（联网复查），共修复 31 项，改动 31 页。
执行方式：4 个分区修复者按页面所有权分区并行 + 6 个联网执行者，避免并发写同页。

**批次一（内容修正）**：P1×3 全修——[[代码与文档漂移的本质]]「可治理度」口径与四类表对齐（表达高/
生命周期中/符合性低，重述为「换成可治理度更高的漂移」）并同步 [[SDD 收益主张的实证赤字]] 推论 3；
[[Anthropic-AI原生SDLC治理循环]]「playbook 覆盖本页没有的 Plan/Design」改为与控制面表一致的表述；
[[基于IT4IT的Agent知识治理]] 停止转述弱化铁律 7，改为声明其无条件性与本仓库辖域、企业过渡配置援引
[[代码与文档漂移的本质]] 的调和原则作对照。另修：[[Claude Cowork]] 可用性更新（web/mobile 云端会话，
旧状态入「历史」小节，第四次报告终于落地）、「实践者反复报告」句两页改写为推断并挂接 Scott Logic、
失真页「六个平台」改七、[[llm-wiki-方法论]] 自引失实改归 Karpathy 原文、M4 统计口径言明、
M5 进可操作清单、赤字页日期列改发表日期、3 处推断补「综合：」、BMAD 失效 URL 换 docs/start 新路径、
cowork-plugins-架构 去掉多余的「素材」页面类型标签。

**批次二（链接与整合）**：补 7 组单向链接（codex 采用曲线←鸿沟/Meta、赤字页←失真页、鸿沟页←赤字页、
提示词组↔失真页、控制带←解决方案页、A²E 实体页←三个小概念页、全轨迹页↔实体页）；
[[论代码与文档漂移解决方案]] 补 SDD 赤字实证并给 §四乐观论断加限定；playbook 横向整合补
[[Agent Skills]] 与 [[AI编码技术债的三层治理]]；[[Evals]] 新节内联源摘要双链；lifecycle 双义项在
两页显式区分；overview 补 [[Claude Code]]/[[Agent Skills]] 入口；purpose.md 当前重心改为 SDD 收益
假设被推翻后的新问法；鸿沟页证据表补 08-27 方法论层反例行。

**批次三（联网复查，6 项）**：
（1）[[MCP]] 规范更新至 2026-07-28 版（无状态自包含请求 + 逐请求能力协商、Mcp-Method/Mcp-Name 头、
HTTP+SSE 一年退场期），新增 Extensions 段（Tasks / Skills over MCP / MCP Apps 均 opt-in）与
2025-12-09 捐赠 Linux Foundation / AAIF 的中立治理；横向核对 [[从知识图谱到 Agent 编排]]、
[[Agent 记忆架构]]、[[building-effective-agents]] 三页论断在新版下仍准确，故未改。
（2）财报季线索闭合：[[cowork-saas-资本市场冲击]] 新增 §4.1，SAP/Dassault Q1+Q2 实际财报与 08-28
股价。**UBS 提示的订单与许可收入风险未在报表兑现**（SAP cloud backlog 连续两季 +25%/+26% cc、
Dassault 两度确认全年目标），兑现的是估值端；风险叙事已从「被 Agent 替代」转为「在位者交付太慢」。
执行者剔除 2 条无法核实的 URL，并明确不采信与已核实价格数据互斥的检索合成数字。
（3）A²E license 快照复查有实质变化：仓库 2026-08-12 已补 MIT LICENSE，「无 license 不应默认获得
再分发权」的判断作废（三页同步修正），但仍无 release/tag，「宜隔离 POC」结论保留。
（4）OKF 复核：版本仍为 v0.2，但权威仓库已迁至 GoogleCloudPlatform/open-knowledge-format（旧
knowledge-catalog/okf 自标 frozen snapshot），且 **v0.2 于 08-21 被原地修订**（时间戳字段须带显式
UTC 偏移）——「版本号不变而规范文本已变」比原「规范尚早期」是更强的边界，已写入两页。
（5）**M5 论断撤销**：定向复查证明那句被指为「归属漂移」的 Kent Beck 引语**确为其原话**——
Martin Fowler《Fragments: January 8》(2026-01-08) 逐字引用并链接其 LinkedIn 原帖。08-27 判「未见此句」
是因为只核对了 Beck 的一篇 newsletter，检索范围不足。**本条撤销 2026-08-27 research 条目中把该引语
记作失真案例的判断**（log 只追加不修改，以本条为准）。M5 作为检查方法保留，但**无确认样本、降为
待观察形态**，已在失真页、[[STORM-知识策展系统分析]]、overview、index 四处同步收窄。
该复查还暴露方法缺口：**「未在原文找到」不蕴含「归属有误」**，只核对一篇就下结论会把真引语误判为
漂移——失真页检查方法已据此收紧。
（6）「Almost Works」引语 8 组检索未果，从「未核验」正式降级为已放弃线索，禁止充当一级来源；
执行者明确拒绝用邻近但不同主张的 Stack Overflow 2025 调查数据把它洗成有源。

**终检**：58 页 / 31 素材与 index 一致；无重名、无孤儿、无新增悬链（仍仅 2 个有意待写）；
frontmatter 全齐且 sources 均块状；overview 60 行；3 个 topics 表头统一；30 页 bump 至 2026-08-31。
新增 22 条外链验证：15×200，4 条 investing.com 403 与 1 条 LinkedIn 451 为访问限制（页内已标注
无法直连核验），2 条 GitHub 429 属限流、串行复试为 200，**无一 404**。

**批次四（未执行，待用户决策）**：shadow mode（11 页提及）与「调和机制」（11 文件引用）建页；
output 根目录 4 份存量 HTML 归位/补 meta/登记 renders；2 份派生视图过期（其中 shared 冻结件需另存
新日期文件）；output/personal 下的 .md 第二正文；[[论代码与文档漂移解决方案]] 649 行拆分；
Attested Computation / Knowledge Catalog / System of Record 缺页；tmp/ 下未摄入的
sonar-state-of-code-2026.pdf 是否投喂。
**外溢线索（本次未采信，留待判断）**：OKF 新仓库 issue #9 提议允许 [[concept]] 双链语法，与
[[OKF 与 llm-wiki 的关系]] 的 wikilink 映射缺口直接相关，但仍是提案；knowledge-catalog #323 自述
okf aspect 六个时间戳字段已改 Dataplex 原生 datetime 且 acme_retail 往返无损，属提交信息作者自述、
未独立核验，[[基于IT4IT的Agent知识治理]] 是否吸收待定。

## [2026-08-31] research | Uber《Running a Software Factory Efficiently at Uber Scale》沉淀

用户投喂 @ubereng 推文（X 直连 402），正文取自 uber.com 原文
（https://www.uber.com/us/en/blog/efficient-software-factory/ ，2026-08-27 发布，
作者 Uday Kiran Medisetty）。

**新增 3 页**：
- `analyses/Uber-软件工厂的成本工程` —— 主体判断页。十节：把"agent 替自己多干的活"作为**可操作的浪费
  定义**；六项成本方程（图片未给名称，本页重建并标注为综合推断）；driver decomposition 不留残差；
  控制单元从"人"上移到"托管 agent 队伍"（与 [[Anthropic-AI原生SDLC治理循环]]、[[控制带]] 同源运动）；
  选型双约束（比模型固定 harness / 测自身收益固定模型）；接地取代搜索；成本治理照搬控制带形状；
  **本 wiki 提出的张力：可计价者被优化、不可计价者被牺牲**（原文未讨论）；对鸿沟论题的意义；
  按投入排序的可迁移表。
- `concepts/Agent 工具上下文膨胀` —— 三个叠加成本面（schema 预加载 / 每轮重发 / 选择准确率下降）、
  三条解法及代价（tool search / CLI 投影 / code-mode）、"这不是 MCP 缺陷而是分层副作用"、
  **Skills 的 progressive disclosure 是同一原则的独立实现**、可确定性检测的反模式。
- `sources/2026-08-27-Uber-软件工厂成本效率-源摘要` —— 忠实摘录 + 七条口径边界。

**新增素材**：`raw/sources/articles/2026-08-27-Uber-软件工厂成本效率.md`（正文结构化存档；
Figure 1–12 为图片未存档，四层与六项方程的具体名称因此缺失，已在两处标注）。

**横向更新 7 页**：[[agent-生产级落地的鸿沟]]（新增 2026-08-27 证据行 + 待追踪问题部分回答：
Uber 公开了成本侧方法论但**质量侧结果仍空白**）、[[MCP]]（新增 §3.1 规模化代价）、
[[Agent Skills]]（progressive disclosure 与工具膨胀的对应 + 3,600 skills 规模数据 +
"自动生成 skill 更新"属高风险写入的提醒）、[[harness-vs-model]]（新增"想比较谁就把另一个钉死"）、
[[Evals]]（新增"任务从哪来 + 记分卡第二根轴"）、[[知识图谱]]（新增 agent 场景的成本论证）、
[[控制带]]（关联新增成本维度同构，并记下"明确不设硬上限"的差异）、[[Claude Code]]（线 1 补
harness 默认值即成本控制面的外部企业证据）。

**口径立场**：全部数据为 Uber 自报无第三方审计；"70% PR 归因"未定义归因规则；
**降的是单位成本（−34% / −52%，固定模型），总支出只是持平**；code-mode 对照表 N=1；
"托管 agent 天然更划算"是主张非实测；接地对照为精选单例。以上六条在源摘要与分析页均已显式标注。

index 概览更新为 32 素材 / 61 页；overview 新增「Agent 的单位经济学」板块并压缩四处旧条目
以守住 60 行上限（现 57 行）。无重名、无新增悬链。

## [2026-08-31] lint | 沉淀后全库体检：1 项确定性红（已修）、外链全量复核、5 项判断类发现

**确定性检查**
1. **重名**：wiki/ 内无重名；全库 `.md` 仅 `purpose.md` / `schema.md` 各两份，是根目录指向 `wiki/` 的
   两个 symlink（第三方工具兼容所需），非真重名。
2. **index 概览计数：红 → 已修。** 本日 research 条目声称"更新为 32 素材 / 61 页"，
   实际未生效——该次替换未加断言，匹配串里带了旧日期 `最后更新：2026-08-27`（文件当时已是 08-31），
   静默失败。**本次已改为 32 / 61。**（更正上一条 log 的该句陈述；log 只追加不修改，故在此声明。）
   教训已生效：本次对沉淀声明的 17 项改动逐条复核，其余全部落地。
3. **路径引用**：wiki 页内 `raw/` / `output/` / `briefs/` 引用全部有效（4 处初检告警经复核均为
   正则误报：schema 的占位示例、`_bmad-output/` 前缀被截、git 恢复命令内的已删档、SHA-256 括号粘连）。
   根目录两个 symlink 可解析。
4. **output/ 派生视图**：5 份 HTML。`shared/工程手工书…-2026-07-27.html` 与
   `output/可持续文档代码一致性方案.html` 的 canonical wiki 页 `updated` 均晚于 `generated` → **过期**；
   `ai-doc-consistency.html`、`cowork-cloud-mode.html`、`罗伯特智能体问答系统方案.html` **缺
   canonical-source / generated meta**；4 份未被任何页 `renders:` 登记。均属 08-31 早前体检
   「批次四·待用户决策」的存量项，**本次仍未执行**。

**外链全量复核（190 条，本库首次全量而非仅新增）**：150 条 200；37 条为反爬/限流
（403/401/451/406，含 Reuters、Gartner、investing.com、ACM/Wiley/SSRN、知乎等，页内多已标注
无法直连）；3 条并发超时经串行复试为 200（eric.ed.gov、gigazine、另 GitHub 429×4 复试 200）；
McKinsey 一条仍超时，与页内既有标注一致。
**真失效 2 条（判断类，待决策）**：
`github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/how-to/project-context.md` 与
`.../blob/main/docs/reference/workflow-map.md` 已 404——upstream 在 2026-08-07 检索后重构 docs，
`docs/how-to/` 目录整体消失。同页引用的 **v6.10.0 固定版 URL 全部 200**。
影响 [[BMAD 项目文档治理方案]]（4 处）与 [[论代码与文档漂移解决方案]]（2 处）。

**其它判断类发现**
- 孤儿页 0；入链数为 1 的页 4 个（overview / agent-auditing / 叙事与故事结构方法论 /
  2026-08-07-AI编码技术债三层治理-用户研究草稿-源摘要），均有合理归属，不作处理。
- frontmatter 全齐；`sources` 块状列表无一例外（overview 的 `sources: []` 是 schema 明文允许的空值）。
- `topics/` 三页证据点表表头统一为 `| 日期 | 来源 | 信号 | 备注 |`；失真页另两张表用途不同，不属该规范。
- `overview.md` 57 行（≤ 60）。schema.md 与 AGENTS.md 无冲突；无 wiki 页把 `briefs/` 当一级来源。
- `briefs/` 19 份，其中 **8 份早于 2026-08-01**（07-20 至 07-31）已超 30 天滚动窗口；今日为月末，
  按约定提醒用户确认删除或转入 `briefs/archive/2026-07/`——**未执行任何删除**。

本次除 index 计数修正外，未改动任何知识内容。

## [2026-08-31] lint | 体检修复：BMAD 两条 main 死链标注（用户决策）

用户决定：**保留原 URL 并标注 upstream 已重构**，不改指 v6.10.0 固定版。
理由（记入以备后查）：两者引用的是不同对象——原文引的是"当时 main 分支的做法"，
改指 tag 会把论断的时间语义悄悄换成"某个版本的做法"。

- [[BMAD 项目文档治理方案]]：frontmatter 两条 main URL 加 404 复核标注；附录 A 加 ⚠️ 链接状态块，
  明确**该节关于 main/next 的论断不再可直接溯源，应视为 2026-08-07 快照**，重新采信前须回查 upstream。
  `updated` 2026-08-07 → 2026-08-31（`renders: []`，不影响派生视图新鲜度比对）。
- [[论代码与文档漂移解决方案]]：frontmatter 同两条 URL 加同样标注（`updated` 已是 2026-08-31）。

**沉淀出的引用纪律（本次实证）**：引用 upstream 仓库文档应优先 pin tag/commit——
同页 v6.10.0 固定版链接 24 天后全部 200，指向 `main` 的两条已 404；
同页 `install-bmad.md` 早前也已因迁移改指新路径。是否写入 `AGENTS.md` 页面约定待用户决定。

（另：`briefs/` 8 份超 30 天简报按用户指示移入 `briefs/archive/2026-07/`。
按 schema「briefs 不写入 wiki/log.md」，此处仅作一句旁注，不计入 lint 范围。）

## [2026-08-31] schema | output/ 退出知识层与 lint 范围；renders: 字段废止

用户裁定（方案 A）：**`output/` 是对外分享的交付层，不作为知识**。据此改 `AGENTS.md` 与 `wiki/schema.md`：

**删除的义务**
- lint 确定性检查第 4 项（`output/` 派生视图新鲜度：`canonical-source` 存在性 + `updated` vs `generated`）
  整条移除；lint 范围收缩为 `wiki/` 与 `raw/`，并加一行显式声明 output 不在范围内。
- `renders:` 登记要求废止——不再新增、不再校验、不再据其触发重渲染。frontmatter 模板已去掉该字段。
  **存量 `renders:` 字段保留不动**（一处有值：[[书与AI的优势边界及家庭组合]]；其余为 `renders: []`），
  下次编辑各页时顺手删即可；不做批量机械迁移，避免无收益的大 diff。
- `canonical-source` / `generated` meta 从**必须**降为**建议**，明确 lint 不检查。
- lint 收尾句去掉"不自动重渲染"（已无重渲染义务）。
- bump `updated` 例外条中"lint 用它与 HTML 的 `generated` 比对"的理由随之删除，改述为避免噪音。

**保留的义务**（方向朝内，保护的是 wiki 不是 output）
- **原创稿必须回灌 wiki**：对外稿内容量超出现有沉淀时，可复用论点必须回写成 wiki 页；
  条文已改写以点明方向——防止知识只住在一份无人维护的交付物里，而非把 output 纳入知识管理。
- 不手改 HTML（避免同一内容出现两个版本）；`output/shared/` 发出即冻结；
  存量或来源不明的 HTML 一律按"已对外发出"处理；删除仍须先问用户；shared 的生成/更新仍记 `output` 日志。

**铁律 7** 改为："`output/` 是**交付层不是知识层**——派生视图不是权威，不进 lint、不计数、不登记。"
第三方工具兼容节里"`renders:` 不在其保护字段内会被丢弃"改为泛指未知 frontmatter 字段。

**连带结果**：上一条 lint 里「批次四·output 存量项」（4 份缺 meta / 未登记，2 份视图过期）
**自此不再是待办**，从体检清单中永久移除。
