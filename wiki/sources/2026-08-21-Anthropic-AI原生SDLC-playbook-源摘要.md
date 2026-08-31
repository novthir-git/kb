---
tags: [素材, AI, Agent, 软件工程, 治理]
created: 2026-08-27
updated: 2026-08-31
sources:
  - "raw/sources/articles/2026-08-21-Anthropic-AI原生SDLC-playbook.md"
  - "https://claude.com/blog/the-ai-native-sdlc-playbook （检索于 2026-08-27）"
  - "[[2026-07-21-Anthropic-AI原生SDLC-源摘要]]"
---

# The AI-Native SDLC Playbook — 源摘要

## 来源定位

Anthropic Applied AI team 的 Louis Claxton 于 2026-08-21 发布的六阶段操作手册，自述整合了该团队
"for our customers" 的日常实践。综合：它与 [[2026-07-21-Anthropic-AI原生SDLC-源摘要|2026-07-21 的安全博客]]
可视为**同一套实践的两个切面**：那篇是安全视角（威胁模型、身份、SIEM、shadow mode），这篇是流程视角
（六阶段、产物链、度量指标）。库内证据为单向关联——本文在 Deploy 阶段显式回指那篇（同组织出品）；
面向客户的手册与内部 SDLC 是否完全同源未经证实。

**性质判断**：这是**产品营销页面**，不是白皮书或研究报告——全部 13 个 play 绑定 Claude 产品栈，
Claude Security 一节直接写了 seat 与计费要求。方法论层可移植，但原文没有做这个区分。

## 核心主张

**Code is no longer the bottleneck.** 传统 SDLC 的六阶段是为"写代码最耗时最贵"设计的；前提失效后：

1. 瓶颈移到 build 两侧——plan、review/test、deploy 仍以人的速度运行；
2. 控制措施失配到不可行——"Reviewing each line by hand made sense when a person had written it,
   but it can't keep up once agents write most of the diff."；
3. 治理成本上升——例外仍走每周/每月开会的委员会。

安全瓶颈作为示例：安全团队按人的产出配置，agent 放大产出后"either the review queue builds or code
ships under-reviewed. A regulated organization can't accept either outcome."

## 贯穿主线：committed artifact

每个阶段以写一份产物进版本控制结束，下阶段读它开始：
`intent.md → spec.md → plan.md → diff + tests → PR + review findings → incident record`。

> "The chain of commits is also the audit trail: who asked for what, what the agent produced,
> and who approved it."

早期阶段用 `.md`，因为产品负责人和 agent 能读同一个文件；Build 之后产物是代码及其记录。
流程被显式描述为 **loop 而非 linear flow**：Maintain 阶段的产出写回 intent.md 重新入环。

## 六个可复用机制（与本 wiki 关联最强的）

1. **控制带（control bands）**——按信号强度分级授予自主权，检测端完全确定性。
   单独承载于 [[控制带]]。
2. **agent 配置像代码一样做回归测试**——eval 套件在 CI 定时跑，**以及在 CLAUDE.md / skills / hooks
   任何变更时跑**；pass rate 下降的配置变更必须先 review 才能合并；每个生产事故写成一条常驻 eval。
   见 [[Evals]]。
3. **skill 是建议性控制，hook 是它背后的确定性层**——"The skill makes violations rare and the hook
   makes them close to impossible." 一条必须永远成立的政策，需要 skill 背后有确定性的东西。
4. **反馈闭环需要保护自己**——"an agent fixing code must not be able to weaken the check on that
   code"；修复任务期间用 hook 阻断 agent 编辑测试文件；先提交失败测试，再在不能改测试的前提下修复。
5. **plan.md 与实现的同步用 hook 强制**——"When implementation departs from the plan, update plan.md
   in the same commit. Consider using a hook to enforce synchronization between the two."
6. **legacy 事实源的三种配置**——repo 为准 / legacy 系统为准 / **链接作为最低标准**
   （"accepting that there are two sources of truth"）。见 [[基于IT4IT的Agent知识治理]]。

## 权限与身份边界（原文明确）

- **"The agent may act up to the production gate and cannot pass it."**
- "the agent that wrote the code has no way to approve it"——写代码的 agent 无法批准它。
- review findings 本身不批准也不阻断 PR，branch protection 仍要求 code owner 批准。
- 每次非交互运行以 **agent 自己的身份**执行，使流水线日志能区分 agent 与触发它的工程师。
- managed settings 由平台团队下发，工程师不可覆盖；sandbox 无法初始化时 Claude Code 拒绝启动。

## 关键判断边界

- **全文零实证数据。** 每个 play 都给了 leading / lagging indicator，但**没有任何一处实际测量结果**
  ——没有"我们做了之后 X 从 A 变成 B"。它提供的是**度量框架，不是效果证据**。这与
  [[2026-07-21-Anthropic-AI原生SDLC-源摘要|7 月安全博客]]不同，那篇至少给了自报数字
  （80% 代码行归因、review comment 覆盖率 16%→54%）。
- **与实证文献存在方向性张力**：本文主张的路径是"更多结构化产物 + 更多门禁"，而现有最大样本的
  SDD 实证显示规格与更高缺陷率和返工相关。原文未回应此类证据。见 [[SDD 收益主张的实证赤字]]。
- **它是一套 SDD，却从不使用这个词**：产物链 `intent.md → spec.md → plan.md → 代码与测试`
  就是 [[Specification-Driven Development]] 的意图→规格→设计任务→实现→证据。
- **供应商内容**：机制层（控制带、产物链、eval 回归、skill/hook 分层）不依赖厂商，
  但工具层全部绑定 Claude 产品栈。

> ⚠️ 矛盾：原文称 "Humans remain accountable for every decision that requires judgment"，
> 但 Stage 6 的目标是 "A trigger invokes Claude with no person in the invocation path"。
> 两者靠阶段间的 confidence gate 调和，而原文把这个 gate 描述为 "a deterministic check **or** an
> adversarial reviewing agent"。按 [[论代码与文档漂移解决方案]] §七 的实证边界，对抗性审查 agent
> 是置信度信号而非授权来源，与确定性检查不是等价选项。原文在 3σ 层把 Claude 的行动限制为
> "只能开 PR 或触发预批准 runbook"，说明作者也知道 agent 判断不足以授权动作——但那个 "or"
> 的措辞把两者摆平了。（发现于 2026-08-27）

## 关联

- [[Anthropic-AI原生SDLC治理循环]]：安全侧姊妹篇的承载页。
- [[控制带]]：本文最值得独立沉淀的机制。
- [[SDD 收益主张的实证赤字]]：本文作为"主张强、证据无"的一个证据点。
- [[Evals]]：agent 配置回归测试的具体做法。
- [[基于IT4IT的Agent知识治理]]：legacy 事实源过渡期配置。
- [[代码与文档漂移的本质]]：hook 强制 plan.md 同步 = 原则二"同一交付事务"的机制化。
