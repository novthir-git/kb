---
tags: [分析, AI, Agent, 软件工程, 文档治理, BMAD]
status: draft
created: 2026-08-07
updated: 2026-08-31
sources:
  - "[[代码与文档漂移的本质]]"
  - "[[论代码与文档漂移解决方案]]"
  - "[[SDD 开发规范研究]]"
  - "[[Specification-Driven Development]]"
  - "两位独立 Agent 专家的文档治理评审、BMAD 落地反方审查与交叉质询（2026-08-07）"
  - "https://www.npmjs.com/package/bmad-method （检索于 2026-08-07）"
  - "https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.10.0/docs/how-to/project-context.md （检索于 2026-08-07）"
  - "https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.10.0/docs/reference/workflow-map.md （检索于 2026-08-07）"
  - "https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/how-to/project-context.md （检索于 2026-08-07；**2026-08-31 复核已 404**——upstream 重构 docs，`docs/how-to/` 目录整体消失，`docs/reference/` 下亦无此文件。URL 保留以标明当时引用的正是 main 分支状态；不改指 v6.10.0，因为那会把"当时 main 的做法"悄悄换成"某个 tag 的做法"）"
  - "https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/reference/workflow-map.md （检索于 2026-08-07；**2026-08-31 复核已 404**——upstream 重构 docs，`docs/how-to/` 目录整体消失，`docs/reference/` 下亦无此文件。URL 保留以标明当时引用的正是 main 分支状态；不改指 v6.10.0，因为那会把"当时 main 的做法"悄悄换成"某个 tag 的做法"）"
  - "https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/start/install-bmad.md （检索于 2026-08-31；原路径 docs/how-to/install-bmad.md 已迁移）"
  - "https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.10.0/docs/how-to/established-projects.md （检索于 2026-08-07）"
renders: []
---

# BMAD 项目文档治理实施方案

> 状态：草案。适用于已经使用 BMAD、文档与代码持续增长的单仓库项目。
> 正式执行前，须先核对项目实际安装的 BMAD 版本、目录和发布方式。

## 一、要解决什么问题

BMAD 会持续产生 PRD、SPEC、Architecture、Epic、Story、Plan、Sprint 状态、评审记录和 Agent context。
这些文件在开发阶段很有用，但随着项目演进，通常会出现四类问题：

- 已完成的 Story、Plan 和中间稿仍被 Agent 默认读取，旧上下文干扰新任务；
- PRD、Architecture、代码和用户文档重复描述同一事实，却不知道谁是当前版本；
- 实现已经改变，长期文档没有更新；
- 文件只增加不退出，团队无法判断哪些仍然有效。

本方案不要求补齐所有文档，也不以整理目录为目标。治理后的结果应该是：

1. 项目成员知道每类问题应查哪个文件；
2. Agent 默认只读取当前有效、与任务相关的内容；
3. 临时产物完成后退出默认上下文；
4. 可从代码生成的内容不再手工维护；
5. 删除前有检查和恢复路径。

## 二、治理后的文档分工

项目中的内容分为四类。分类依据是用途，不是文件所在目录。

| 类别 | 典型内容 | 怎么维护 | 何时退出 |
|---|---|---|---|
| Agent 常驻上下文 | `AGENTS.md`、BMAD project context | 只放 Agent 无法从代码推导、必须遵守的规则 | 规则失效或已能从代码稳定推导时删除 |
| 长期项目文档 | 当前产品约束、架构概览、ADR、用户文档、Runbook | 描述当前有效状态或长期决策 | 被替代后指向新文档，再退出默认导航 |
| BMAD 工作产物 | PRD、SPEC、Epic、Story、Plan、Sprint、评审和调研稿 | 服务当前需求和交付 | Epic/项目关闭后蒸馏，随后 depublish |
| 机器派生文档 | OpenAPI、Schema、CLI 帮助、配置参考 | 从代码或配置生成，禁止手改 | 生成源消失时一起删除 |

这里的 **depublish** 是指：文件可以暂时保留，但从 `docs/index.md`、Agent 默认上下文和日常检索入口中移除。
试点阶段不自动删除文件。

## 三、每种问题去哪里找答案

| 想知道什么 | 应查哪里 |
|---|---|
| 正在计划做什么 | 当前 active PRD、SPEC、Story 或 change |
| 用户现在能使用什么 | 已发布的产品说明、API 契约和 Release Note |
| 代码当前怎么实现 | 代码、配置和构建产物 |
| 线上实际运行什么 | 部署配置、日志、指标和业务数据 |
| 为什么采用这个方案 | ADR；小决策可以留在相关 Architecture 小节 |
| 是否已经正确实现 | 测试、CI、验收和运行证据 |
| 如何部署、排障和恢复 | Runbook |

同一项事实只保留一个人工维护的权威来源。其他地方可以链接或自动生成，不应复制一份再独立修改。

例如：

- API 字段以 Schema 为准，API 文档由 Schema 生成；
- 技术选择的理由写在 ADR，`project-context` 只写“必须遵守什么”并链接 ADR；
- Story 中新增的长期业务规则，在功能发布时写回当前产品说明，Story 随后退出默认上下文。

## 四、建议的最小目录

先使用最小结构，不要为了治理预建一批空目录：

```text
project/
├── AGENTS.md                         # Agent 的仓库级入口和少量强制规则
├── _bmad/                            # BMAD 安装内容；不手工改造其结构
├── _bmad-output/
│   ├── project-context.md            # stable 6.10 使用；保持精简
│   ├── planning-artifacts/           # 当前仍在进行的规划产物
│   └── implementation-artifacts/     # 当前仍在进行的实现产物
├── docs/
│   ├── index.md                      # 只做当前文档导航
│   ├── product.md                    # 确有长期业务规则时才建立
│   ├── architecture.md               # 当前架构概览，不堆历史方案
│   ├── adr/                          # 重要且长期的设计决策
│   └── runbooks/                     # 部署、排障、恢复
├── src/
└── tests/
```

说明：

- 如果项目使用 BMAD main/next，应沿用 `bmad-project-context` 生成的 kernel + bundle，不再新建
  `project-context.md`；详见附录。
- 已有目录若能回答同样的问题，不必为了符合本图而搬迁。
- `docs/index.md` 只列当前有效文档和一句用途，不复制正文摘要。
- 没有实际读者的 `product.md`、ADR 或 Runbook 不必创建。

## 五、现有 BMAD 文件怎么处理

### 1. Project Context

保留，但必须瘦身。只写：

- 项目特有且容易违反的技术约束；
- 禁止触碰的区域；
- 非显然的测试、错误处理和安全规则；
- 指向长期权威文档的链接。

删除：技术栈常识、可从配置读取的版本、目录清单、完整架构说明、编码领域的通用口号。

### 2. PRD / SPEC

- 正在实施：保留为目标状态的权威输入；
- 已实现但未发布：保留，明确标记尚未发布；
- 已发布：把仍长期有效的业务规则写回当前产品/API 文档；
- 全部信息已写回后：从 Agent 默认上下文移除；有审计要求才归档。

不能因为文件位于 `_bmad-output` 就直接删除。PRD 或 SPEC 可能仍是唯一的产品意图来源。

### 3. Architecture

- 描述当前系统结构的部分，保留在 `docs/architecture.md` 或已有等价页面；
- 重要设计理由写入 ADR；
- 已否决方案、实现计划和讨论过程不进入当前架构文档；
- 旧架构被替代后，迁移引用并退出当前导航。

### 4. Epic / Story / Plan / Sprint

- 进行中：保留并只加载当前任务相关文件；
- Story Done：记录验收证据和可能需要回写的长期信息，不删除；
- Epic Close：汇总仍有效的业务规则、设计决策和运行经验，生成退休候选清单；
- Release 完成且回写确认后：从默认上下文 depublish；
- 后续通过独立 cleanup 变更决定删除或归档。

### 5. 调研、评审和 Retrospective

- 会改变后续工程行为的稳定结论，写入 project context、ADR 或 Runbook；
- 仅解释本次任务的内容保留在 Git/PR 历史即可；
- 没有复用价值的中间推理和生成稿不进入长期文档。

### 6. 自动生成文档

- 固定生成工具版本；
- CI 中重新生成并检查差异；
- 文件头标明生成来源和“请勿手改”；
- 没有离线阅读或发布需要时，可以只在 CI/发布阶段生成，不必提交仓库。

## 六、以后每次开发怎么维护

文档治理嵌入现有交付事件，不新建一条独立流程。

### 开始需求时

1. 确认当前使用的 PRD、SPEC 或 Story；
2. 只加载当前任务、project context 和必要的长期文档；
3. 若发现多个文件都声称是当前版本，先指定本次变更采用哪一个。

### PR / Merge 时

提交者只回答四个问题：

```text
Document impact: none | product | decision | operations | generated
Canonical target:
Verification evidence:
Retirement candidates:
```

- `none` 写一句理由；
- 有用户行为变化，指出产品/API 文档；
- 有长期技术取舍，指出 ADR；
- 有部署或故障处置变化，指出 Runbook；
- 能生成的文档，更新生成源而不是手改结果。

### Release / Deploy 时

1. 确认哪些目标行为已经真正对用户生效；
2. 更新产品说明、API 契约、Release Note 和 Runbook；
3. 未发布、灰度中或受 feature flag 控制的行为，不写成全局当前状态；
4. 若发生回滚，同步回退对外说明和运行指引。

### Epic / 项目关闭时

1. 汇总 Story 中仍长期有效的信息；
2. 回写产品文档、ADR、Runbook 或 project context；
3. 将已完成工作产物从默认上下文和导航移除；
4. 形成单独的 cleanup 清单；
5. 不在同一步自动删除。

## 七、第一次治理现有存量

### 第一步：建立安全基线

- 确认所有待处理文件已经提交；
- 创建可识别的 cleanup 分支、commit 或 tag；
- 未提交文件、附件和外部输入单独列出；
- 不在盘点阶段删除或移动文件。

### 第二步：给现有文件分四类

对每个文件只记录：

```text
文件：
用途：Agent context | 长期文档 | 工作产物 | 机器派生
状态：当前有效 | 进行中 | 已完成 | 被替代 | 不确定
回答的问题：
替代文件（如有）：
建议：保留 | 精简 | 回写后 depublish | 生成化 | 待人工判断
```

### 第三步：先解决三种高价值问题

优先处理：

1. 同一事实存在两份以上人工维护版本；
2. 已完成或被替代的文件仍被 Agent 默认加载；
3. 可以从代码生成、目前却在手工维护的内容。

不要一开始处理格式、命名和目录美化。

### 第四步：建立当前入口

- `AGENTS.md` 告诉 Agent project context 和长期文档在哪里；
- `docs/index.md` 只列当前有效文档；
- Agent 的默认检索排除 completed、superseded、archive 和生成物副本；
- 当前活跃 PRD、SPEC、Epic 和 Story 按任务显式加载。

### 第五步：第一次清理只 depublish

- 将退休候选移出默认导航和 Agent 上下文；
- 运行一个发布周期，观察是否仍有人或 Agent 需要它们；
- 确认信息迁移、引用处理、保留义务和恢复路径后，再提交独立删除方案。

## 八、两周实施计划

| 时间 | 工作 | 产出 |
|---|---|---|
| 第 1 天 | 核对 BMAD 版本、实际目录和发布方式 | `BMAD 基线记录` |
| 第 2–3 天 | 盘点一个活跃产品域的文档 | 分类清单与重复/过期问题列表 |
| 第 4 天 | 确认每类问题的权威来源 | 一页“问题 → 文件”映射 |
| 第 5 天 | 精简 Agent context，建立当前文档入口 | 精简 context、`docs/index.md` |
| 第 2 周 | 在真实变更中试运行影响声明、Release 回写和 Epic Close | 试点记录、depublish 清单、改进建议 |

第一周不删除文件，第二周不建设复杂自动化。

## 九、第一阶段自动检查

只让以下可确定问题阻断 CI：

- 仓库内部链接或声明的目标文件不存在；
- 已提交生成物无法从固定版本的生成源重建；
- 高风险路径发生变化，却没有完成文档影响确认或指定审核。

以下只提示，不阻断：

- AI 判断文档语义可能过时；
- AI 建议合并重复页面；
- 外部链接暂时不可访问；
- AI 建议删除或归档文件。

路径变化只能证明“需要确认”，不能自动证明某份文档必须更新。AI 也不能单独授权删除。

## 十、完成标准

试点完成时，应满足：

- 团队能明确回答产品行为、实现状态、设计理由、验证证据和运行状态分别去哪里查；
- Agent 常驻上下文只包含当前有效、不可从代码推导的规则；
- 完成和被替代的工作产物不再默认加载；
- 活跃 PRD / SPEC 与已发布行为能够区分；
- 生成文档可以稳定重建；
- 当前文档入口没有内部断链；
- 完成一次 depublish 和恢复演练；
- 新增治理劳动没有演变成机械填写和长期异常队列。

试点阶段可以记录以下参考指标，但不把它们当作行业标准：

- 每个变更增加的文档治理时间；
- CI 告警的误报和被忽略比例；
- 重复、失效和默认加载的历史文档数量；
- 因旧文档导致的返工或 Agent 错误行动次数；
- 定位五个常见项目问题所需的时间。

## 十一、风险与回退

| 风险 | 控制措施 |
|---|---|
| 过早删除长期意图 | 第一阶段只 depublish；删除使用独立变更 |
| 文档领先于生产 | 区分已计划、已实现未发布和已发布 |
| Agent 读取历史目标态 | 默认上下文使用白名单，历史文件按任务显式加载 |
| 治理变成新仪式 | 只保留三个确定性检查；语义审查先提示 |
| BMAD 升级破坏流程 | 试点期间固定版本；升级单独评估 |
| 清理后无法恢复 | cleanup 前提交/tag，并实际演练恢复 |

出现以下任一情况时，应暂停扩大范围：

- 团队普遍机械填写 `none`；
- CI 提示大多被忽略；
- Agent context 继续膨胀；
- 维护治理规则的时间超过原来的文档查找和返工成本；
- 清理过程中丢失验收、发布或设计依据。

## 十二、开始前需要项目负责人确认

1. 当前安装的 BMAD exact version 和 channel；
2. 项目是 merge 即发布、定期发布、灰度还是多版本并行；
3. 哪些 PRD / SPEC 仍是当前产品意图来源；
4. 是否有法规、客户、事故或审计保留要求；
5. 首次试点选择哪个产品域或 Epic；
6. 谁负责处理“不确定保留还是退出”的少量异常。

这六项没有确认前，可以做只读盘点，但不执行目录迁移或删除。

## 附录 A：BMAD 版本差异

截至 2026-08-07：

- npm `latest` 6.10.0 使用单个 `_bmad-output/project-context.md`，实现流程包含 Story 与 Quick Flow；
- main/next 已转向 `bmad-project-context` 管理 kernel + bundle，并让各类输入收敛到 `bmad-build`；
- 因此不能照搬官网 main 文档治理 stable 项目，也不能假设所有变更都有 Story。

来源：
[npm](https://www.npmjs.com/package/bmad-method)、
[v6.10.0 Project Context](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.10.0/docs/how-to/project-context.md)、
[v6.10.0 Workflow Map](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.10.0/docs/reference/workflow-map.md)、
[main Project Context](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/how-to/project-context.md)、
[main Workflow Map](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/reference/workflow-map.md)
（均检索于 2026-08-07）。

> ⚠️ 链接状态：上面两条 **main 分支链接自 2026-08-31 复核起已 404**——upstream 重构了 `docs/`，
> `docs/how-to/` 目录整体消失。**本节关于 main/next 的论断因此不再可直接溯源**，
> 应视为 2026-08-07 的快照观察，重新采信前须回查 upstream 当前文档。
> 保留原 URL 而不改指 v6.10.0：两者引用的是不同对象（"当时 main 的做法" vs "某个 tag 的做法"），
> 改指会悄悄替换论断的时间语义。同页 v6.10.0 固定版链接全部仍然有效。
> 综合：**引用 upstream 文档应优先 pin tag/commit**——本页 24 天内 main 链接失效、tag 链接存活，
> 是同一现象的直接样本（另见本页 `install-bmad.md` 已迁移的先例）。

项目应先读取实际安装内容和 `_bmad/_config/manifest.yaml`，试点期间固定版本。官方安装文档说明，stable
会在重新安装时解析到当时最新 tag，跨机器复现应显式 pin 外部模块
（[安装与版本固定](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/start/install-bmad.md)，
检索于 2026-08-31，原路径已迁移）。

## 附录 B：设计依据

- [[代码与文档漂移的本质]]：问题级权威、派生视图与生命周期 GC。
- [[论代码与文档漂移解决方案]]：事件调和、风险分级和自动删除边界。
- [[SDD 开发规范研究]]：current spec、change delta 与 Reconcile & Retire。
- [[Specification-Driven Development]]：规格作为持续演化的意图接口。

