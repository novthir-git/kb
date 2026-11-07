---
tags: [实体, AI, Agent, 软件工程, 工具]
created: 2026-11-07
updated: 2026-11-07
sources:
  - "https://github.github.com/spec-kit/ （检索于 2026-11-07）"
  - "https://raw.githubusercontent.com/github/spec-kit/main/README.md （检索于 2026-11-07）"
  - "https://github.github.com/spec-kit/reference/agentic-sdd.html （检索于 2026-11-07）"
  - "https://github.github.com/spec-kit/how-to/persisting-specs.html （检索于 2026-11-07）"
  - "https://github.github.com/spec-kit/how-to/evolving-specs.html （检索于 2026-11-07）"
  - "https://github.github.com/spec-kit/overview/history.html （检索于 2026-11-07）"
  - "https://raw.githubusercontent.com/github/spec-kit/main/CHANGELOG.md （检索于 2026-11-07）"
  - "https://github.com/github/spec-kit （提交历史经 git clone 核验；检索于 2026-11-07）"
  - "https://arxiv.org/html/2605.01160 （SGM 研究 §7.4；检索于 2026-11-07）"
  - "[[SDD 开发规范研究]]"
  - "[[Specification-Driven Development]]"
  - "[[SDD 收益主张的实证赤字]]"
  - "[[2026-09-23-agentic-se-refactoring-methodology-源摘要]]"
---

# GitHub Spec Kit

GitHub 的开源（MIT）[[Specification-Driven Development|SDD]] 工具包。Specify CLI（`specify`）负责初始化项目、
管理集成与扩展；流程命令 `/speckit.*` 在 coding agent 里运行，不在终端里。2025-08-21 首次提交，2026-08-21 发布
1.0.0；2026-11-07 时最新版本为 v1.3.2（2026-11-06）（README、CHANGELOG、History 页，均检索于 2026-11-07）。

## 当前形态（2026-11-07 复核）

- **三个独立入口，不是强制阶段**：Spec-Driven Development（core 自带）、Bug fixing、Idea assessment（后两个是随附的
  可选扩展）——"These are independent entry points, not mandatory phases."（README）
- **SDD 命令链**：`/speckit.constitution → specify → clarify → plan → checklist → tasks → analyze → implement → converge`。
  只有 specify 是 plan 的硬前置；clarify、checklist、analyze 是可选质量门（Agentic SDD 命令参考）。
- **converge 闭合交付回路**（2026-06 加入）：对照 spec / plan / tasks 评估实现，只往 tasks.md 追加剩余任务
  （append-only），不改写规格去迁就代码。所有持久化模型共用 specify → plan → tasks → implement → converge。
- **调和不归 core**：core 没有自动调和 spec.md / plan.md / tasks.md 差异的命令，`/speckit.analyze` 只报告不修改，
  调和靠人或扩展（Evolving specifications 页）。
- **持久化四种模型**：Flow-back、Flow-forward、Living spec，以及 2026-11-06 新增的 Constitution-only（交付后只留
  constitution，feature 产物退出，退出前先把持久知识迁到约定的家）；"None is the default, and none is required"。
  规格寿命三层级引用的是 [[Birgitta Böckeler]] 的 martinfowler.com 文章。Spec Kit 自己的仓库用 Constitution-only：
  只跟踪 `.specify/memory/constitution.md`，`specs/` 被 gitignore（Persisting specifications 页）。
- **可组合**：integrations、extensions、presets、workflows、workflow steps 五种原语，加上把它们打包的 bundles
  （History 页）。
- **文档站迁移**：2026-11-03（upstream #5230）把使用指南整体移到 `how-to/`，旧 `concepts/sdd.html`、
  `concepts/spec-persistence.html`、`guides/evolving-specs.html` 均 404；2026-11-06（#5299）又把
  `how-to/spec-persistence.html` 改名为 `how-to/persisting-specs.html`。综合：引用这个站点应带检索日期，
  且按"内容现址"并列新 URL，而不是只换链接。

> 综合：两点与本库判断直接相关。其一，Constitution-only 是 [[代码与文档漂移的本质]] 原则三"临时产物蒸馏后删除"
> 在工具内的版本。其二，"core 不做调和、analyze 只报告"说明 Spec Kit 本身不提供 [[SDD 收益主张的实证赤字]]
> 所说的那层调和机制，要团队自己或扩展补上——这正是 [[论代码与文档漂移解决方案]] 定位的那一层。

## 本库用它做研究对象的页

- [[SDD 开发规范研究]]：推荐目录与门禁参照了它的 constitution / spec / plan / tasks / analyze 流程；工具选择表。
- [[Specification-Driven Development]]：SDD 的定义引用、持久化模型（artifact mutation model）。
- [[SDD 收益主张的实证赤字]]：两项针对它的实测——Scott Logic 单案例（2025-11-26，GitHub Copilot + Claude
  Sonnet 4.5）与 SGM 研究里"Spec Kit under the SGM"的四个月试点（arXiv 2605.01160 §7.4，3 个团队）。
- [[Agentic SE 时代的系统重构]]：spec 是否是新源代码——方法论文档理念上接近 spec-as-source，工具实际形态是 spec-first。
- [[论代码与文档漂移解决方案]]：Artifact-Driven Agent Workflow 的代表之一。
- [[AI工程方法论的耐久度]]：分步 markdown 流程被归为会贬值的"仪式"。
- [[2026-09-23-agentic-se-refactoring-methodology-源摘要]]：三入口与 converge 的核验。

## 历史

- **2025-08—2026-01**：Den Delimarsky 与 John Lam 创立；2026-01-22 起 Manfred Riem 任 lead maintainer（History 页）。
- **2025-09**：Böckeler 试用后把它与 Kiro 一起归为 spec-first 工具（见 [[Specification-Driven Development]]）。
- **2026-07-16（本库首次调研时）**：README 只呈现单一 SDD 流程，核心命令为 constitution → specify → plan → tasks →
  implement，另有 converge 与 taskstoissues，可选 clarify / analyze / checklist。持久化文档在
  `concepts/spec-persistence.md`，列三种模型（Flow-back / Flow-forward / Living spec），已写明"None is the default"；
  `guides/evolving-specs.md` 有 Living Spec 一节，要求改 spec.md 后重新对齐 plan / tasks，并在恢复实现前运行
  `/speckit.analyze`（2026-07-16 时的仓库版本，经 git 历史核验）。bug 扩展已于 0.9.5（2026-06-05）随附，但 README
  未把它列为入口；assess 扩展 0.13.0 于 2026-07-17 才发布。
- **2026-09-23**：本库核验到三入口与 converge，见 [[2026-09-23-agentic-se-refactoring-methodology-源摘要]]。
