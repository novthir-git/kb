---
tags: [分析, AI, Agent, 软件工程, 开发规范]
created: 2026-07-16
updated: 2026-08-31
sources:
  - "[[Specification-Driven Development]]"
  - "[[论代码与文档漂移解决方案]]"
  - "[[Evals]]"
  - "https://github.com/github/spec-kit （检索于 2026-07-16）"
  - "https://github.github.com/spec-kit/concepts/spec-persistence.html （检索于 2026-07-16）"
  - "https://github.github.com/spec-kit/guides/evolving-specs.html （检索于 2026-07-16）"
  - "https://kiro.dev/docs/specs/feature-specs/ （检索于 2026-07-16）"
  - "https://kiro.dev/docs/specs/bugfix-specs/ （检索于 2026-07-16）"
  - "https://openspec.dev/ （检索于 2026-07-16）"
  - "https://tessl.io/blog/tessl-launches-spec-driven-framework-and-registry/ （检索于 2026-07-16）"
  - "https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/ （检索于 2026-07-16）"
  - "https://www.iso.org/standard/72089.html （检索于 2026-07-16）"
  - "https://www.rfc-editor.org/info/rfc2119/ （检索于 2026-07-16）"
  - "https://arxiv.org/abs/2604.21505 （检索于 2026-07-16）"
  - "https://arxiv.org/abs/2601.03878 （检索于 2026-07-16）"
  - "[[SDD 收益主张的实证赤字]]"
  - "[[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]]"
---

# SDD 开发规范研究

## 核心结论

目前没有统一的 SDD 行业标准。GitHub Spec Kit、Kiro、OpenSpec、Tessl 已在“先规格、再设计与任务、
最后实现和验证”上收敛，但对规格持久化、变更管理、工具绑定和自动生成程度仍有不同选择。

> 综合：团队不应先选工具再接受它的默认流程。应先定义自己的 artifact model、阶段门禁、追溯规则和
> 轻重分级，再选择工具承载。对多数长期维护项目，推荐 **Spec-anchored + Living current spec +
> Flow-forward delta history + retention policy**，而不是直接采用激进的 Spec-as-source，或把所有
> change package 永久堆在工作树里。

> 2026-07-16 生命周期校正：旧版 G5 默认归档全部 change package，与
> [[代码与文档漂移的本质]] / [[论代码与文档漂移解决方案]] 的“过程产物蒸馏后退出”原则冲突。
> 本版将 G5 改为 Reconcile & Retire：先回写长期知识，再按审计/复现政策决定归档或删除。

> ⚠️ 2026-08-27 证据校正：本页 2026-07-16 版的“证据边界”只承认 Orchid 与 CURRANTE 两条，
> 语气为“实证尚早期”。复检发现两份更不利的证据在沉淀时点之前就已存在却未被检索到：
> Scott Logic 的实测（2025-11-26，早 7 个月）与 Hill 的 119 仓库 / 10 万 PR 研究（2026-04-28，
> 早 2.5 个月，结论指向规格与更高缺陷率和返工相关）。**那一版不是谨慎而是偏乐观。**
> 本页的门禁、追溯链与 EARS 写法各有独立依据、不受影响；被修正的是默认收益假设。
> 完整证据表与结构性解释见 [[SDD 收益主张的实证赤字]]。

## 推荐的 SDD 开发规范 v1.0

### 真相不是一个文件，而是按职责分层

- **预期行为的真相**：current spec。
- **实现状态的真相**：代码与部署配置。
- **符合性的证据**：测试、[[Evals|evals]]、CI、运行时验证与验收记录。
- **决策历史的真相**：ADR、版本历史，以及按审计/复现政策保留的证据；change package 默认是工作产物。

> 综合：把“single source of truth”简单理解为“只有 spec 才是真的”会遮蔽运行现实；正确做法是让每类
> artifact 只对自己的问题权威，并用追溯链保持一致。

这一分层为什么比“代码是全局唯一真相源”更能暴露实现与意图的偏差，
见 [[代码与文档漂移的本质]]（其 v2 的四类漂移分类，以及“测试只是证据、不是裁判”的论证，
与本表“符合性的证据”命名一致）。

### 推荐目录

```text
specs/
├── constitution.md
├── current/
│   └── <capability>/spec.md
└── changes/
    └── <change-id>/
        ├── proposal.md
        ├── requirements.md
        ├── design.md
        ├── tasks.md
        ├── verification.md
        └── specs/              # 对 current spec 的 delta
adr/
└── ADR-<id>-<decision>.md
```

该结构综合了 GitHub Spec Kit 的 constitution / spec / plan / tasks / analyze / implement 流程与
OpenSpec 的 current specs + change deltas。后者让评审者先看到“意图如何变化”，而不是从代码 diff 反推需求
（[Spec Kit](https://github.com/github/spec-kit)、[OpenSpec](https://openspec.dev/)，检索于 2026-07-16）。

### 产物与门禁

| Gate | 必须产物 | MUST 满足的条件 |
|---|---|---|
| G0 变更分级 | issue / proposal | 明确问题、目标、范围、非目标、负责人、风险等级 |
| G1 Spec Ready | requirements | 需求有唯一 ID、可测试场景、异常/边界、非功能约束；无未治理歧义 |
| G2 Design Ready | design / ADR | 每条需求有设计覆盖；接口、数据、安全、观测、兼容、迁移、回滚已说明 |
| G3 Implementation Ready | tasks | 任务有依赖、文件/组件边界和完成条件；`REQ → Design → Task` 可追溯 |
| G4 Merge Ready | code / tests / verification | `REQ → Test/Eval → Evidence` 完整；CI、运行验证、范围检查通过 |
| G5 Reconcile & Retire | current spec / ADR / retention decision | delta 已合并；长期理由已蒸馏；引用已迁移；需审计/复现的 change 归档，否则宽限期后从工作树删除 |

GitHub Spec Kit 将澄清放在技术计划之前，并提供跨产物 analyze、质量 checklist 与完成度 converge；
这说明“生成了文档”不是门禁，**一致性和覆盖度检查**才是门禁
（[Spec Kit commands](https://github.com/github/spec-kit)，检索于 2026-07-16）。
AI 审查为何只能作证据、不能作唯一门禁（自我偏好、跨模型错误相关、开放式一致性检查的高假阳性），
实证见 [[论代码与文档漂移解决方案]]“自产自审的实证边界”。

## 需求写作规范

Kiro 使用 EARS 形式 `WHEN [condition] THE SYSTEM SHALL [behavior]`；Bugfix Specs 进一步要求分别写出
Current、Expected、Unchanged Behavior，从而把回归边界显式化
（[Feature Specs](https://kiro.dev/docs/specs/feature-specs/)、
[Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/)，检索于 2026-07-16）。

```md
### REQ-AUTH-001 [MUST]

WHEN 未认证用户访问受保护接口
THE SYSTEM SHALL 返回 HTTP 401，且不得泄露资源是否存在。

验证方式：自动化接口测试 tests/auth/unauthorized.spec.ts
不变行为：已认证用户的现有授权流程 MUST 保持不变。
来源/理由：SEC-003
```

每条 requirement MUST：

- 只表达一个行为，有稳定且唯一的 ID。
- 说明触发条件、系统主体、可观察结果和验证方法。
- 使用可测量的阈值描述性能、容量、可用性和时限。
- 把异常、边界、权限失败与必须保持不变的行为写明。
- 将理由、假设与需求正文分开；设计选择进入 design/ADR，不能伪装成产品需求。
- 避免“快速、友好、适当、尽量、正常情况下”等不可验证词。
- `TBD/TBR` 必须附负责人、截止日期、解除条件；否则不得通过 G1。

NASA 的要求检查表同样强调一个 statement 只表达一个 thought、避免实现细节、消除歧义并保证可验证
（[NASA](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)，检索于 2026-07-16）。
高合规项目可进一步对齐
[ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) 的需求工程过程与信息项；
规范中的 MUST / SHOULD / MAY 可采用 [RFC 2119](https://www.rfc-editor.org/info/rfc2119/) 语义
（均检索于 2026-07-16）。

## 追溯与变更规则

最小追溯链为：

`REQ-ID → Design section / ADR → TASK-ID → Test/Eval-ID → CI 或验收证据`

- PR MUST 声明覆盖和改变的 REQ-ID；无法关联需求的行为变化视为 scope leakage。
- 实现发现需求错误时 MUST 回到规格层处理，不得只在代码里“顺手修正”。
- 需求变化 MUST 生成 spec delta；合并后把 delta 应用到 current spec，再执行 retention policy：
  有审计、法规或长期复现义务的 change package 归档；普通过程包在理由蒸馏、引用迁移和宽限期结束后删除，
  由 Git 历史保留恢复能力。
- 计划和任务被重新生成前 MUST 把仍然有效的技术理由移入 ADR，避免生成覆盖掉决策历史。
- 规格、设计、任务或代码先发生合理变化时，可以 flow-back，但 PR 合并前 MUST 恢复一致。

GitHub 的 brownfield 指南也要求 living spec 在修改 `spec.md` 后重新对齐 plan/tasks，并在继续实现前运行
跨产物分析
（[Evolving Specs](https://github.github.com/spec-kit/guides/evolving-specs.html)，检索于 2026-07-16）。

## 轻重分级

| Profile | 适用场景 | 最小要求 |
|---|---|---|
| Quick | 拼写、注释、机械配置，或不改变外部行为的明显局部修复 | issue + diff + 验证证据 |
| Standard | 用户可见行为、多文件或跨模块变更 | proposal + requirements + tasks + verification |
| Full | 公共 API、数据迁移、权限、安全、计费、合规或不可逆操作 | 全部产物 + ADR + 人工阶段审批 + 回滚演练 |

探索性 spike 可以跳过完整规格，但 MUST 设时间盒、隔离分支和“不得直接发布”的停止条件；探索结果进入
正式实现前，仍需回到对应 profile 的 G1。

## 工具选择

| 工具 | 更适合 | 主要权衡 |
|---|---|---|
| GitHub Spec Kit | 绿地、复杂功能、需要 constitution 与阶段审计的团队 | 流程完整，产物和仪式也相对重 |
| OpenSpec | 存量系统、跨会话协作、强调 current spec + change delta | 轻量、agent 无关；组织治理需团队自行补充 |
| Kiro Specs | 希望在同一产品内完成 EARS、Feature/Bug、Requirements/Design-first 流程 | 体验集成度高，但工作流依赖 Kiro 生态 |
| Tessl | 试验组件规格、usage spec 与更强的 spec-to-code | 更接近 Spec-as-source，适用边界和成熟度需单独验证 |

> 综合：以上是各产品官方文档所呈现的定位，不是独立基准测试。团队应先用相同任务做小规模对照，
> 再决定工具，不应把 stars、市场宣传或文档完整度等同于工程效果。

## 证据边界与试点指标

Orchid 的 1,304 个函数级任务显示，需求歧义会稳定降低受测 LLM 的代码生成表现，而且模型经常无法可靠地
自行发现或解决歧义；这为 G1 澄清门禁提供了直接证据
（[arXiv 2604.21505](https://arxiv.org/abs/2604.21505)，检索于 2026-07-16）。

但完整 SDD 的公开实证仍早期：SANER 2026 的 CURRANTE 研究截至当前是 Stage 1 Registered Report，
即实验方案已评审，尚不能拿它证明组织级 ROI
（[arXiv 2601.03878](https://arxiv.org/abs/2601.03878)，检索于 2026-07-16）。

**而已有的大样本证据指向反面**（2026-08-27 补）。Brenn Hill 对 119 个开源仓库、100,247 个 PR 做的
SZZ 缺陷追溯 + within-author 固定效应分析，从厂商主张推导的五个假设无一得到支持：规格与更高缺陷率
（+1.4pp, p=0.056——缺陷率一项严格说不显著，仅方向为正）和更高返工（+5.0pp, p<0.001）相关，
规格质量对返工零效应（p=0.997）
（[SSRN 6515898](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6515898)，检索于 2026-08-27；
直连返回 403，细节经检索摘要核验，证据强度相应降级）。Scott Logic 的单案例实测则给出成本侧的量级：
Spec Kit 第一增量产出 689 行代码却生成 2,577 行 markdown，人工 review 3.5 小时，而同一工作用迭代提示
总计约 32 分钟且无 bug
（[Scott Logic](https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html)，
检索于 2026-08-27）。

> 综合：这不推翻本规范的门禁与追溯链设计（Hill 研究并未测试这些具体成分），但推翻了默认收益假设。
> 结构性解释见 [[代码与文档漂移的本质]]“SDD 与漂移的转化关系”：规格把难治的符合性漂移换成了
> 好治的表达漂移与生命周期漂移，**成本立刻发生，收益取决于是否真的建了调和机制**。
> 因此下面这组试点指标的用途也随之改变——它们不再是“验证收益有多大”，
> 而是**先验证成本是否被抵消**。完整证据表见 [[SDD 收益主张的实证赤字]]。

因此试点 SHOULD 同时跟踪：

- 从需求提出到合并的 lead time，以及其中规格阶段耗时。
- 澄清轮数、实现中需求返工次数、scope leakage 数量。
- 首次 CI 通过率、缺陷逃逸率、回滚率。
- 人工 review 时长与 agent 中断/接管次数。
- 合并后 spec drift 数量。
- 工程师认知负荷与主观体验，避免只优化产出而加剧 [[生产力-体验悖论]]。

## 与现有知识版图的关系

- [[Specification-Driven Development]] 给出概念、持久化模型及与 TDD/BDD 的边界。
- [[Loop Engineering]] 解释规格/[[Evals|evals]] 如何进入分钟级 coding loop、小时级开发者反馈和外部反馈循环。
- [[building-effective-agents]] 提供 workflow checkpoint、透明规划、测试与护栏的底层模式。
- [[agent-生产级落地的鸿沟]] 说明为什么 Demo 成功不等于生产可控；本规范提供一组流程侧补强手段。
- [[Codex]] 等 coding agent 是 SDD 的执行器，但产品意图、风险接受与验收责任仍属于人。
- [[论代码与文档漂移解决方案]] — 文档侧的调和治理架构（关系契约、一致性分级、生命周期 GC），与本规范的门禁和追溯链互补。
- [[SDD 收益主张的实证赤字]] — 本规范收益主张的实证状态：现有最大样本结论反向，主张与证据的赤字。
- [[2026-08-21-Anthropic-AI原生SDLC-playbook-源摘要]] — Anthropic 的同类六阶段手册；其 intent.md →
  spec.md → plan.md 产物链与本规范同构，且用 hook 强制 plan 与实现同步，但未提供任何效果数据。
