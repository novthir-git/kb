---
tags: [素材, AI, Agent, 软件工程, CI]
created: 2026-09-16
updated: 2026-09-16
sources:
  - "https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic （检索于 2026-09-16）"
  - "raw/sources/articles/2026-09-14-Anthropic-CI规模化压力.md"
---

# 2026-09-14 Anthropic《Agentic coding is straining CI》源摘要

**原文**：Anthropic 官方工程博客，2026-09-14，作者 Sachin Malhotra。
**存档**：`raw/sources/articles/2026-09-14-Anthropic-CI规模化压力.md`（结构化摘录，非逐句原文镜像）。

判断与跨源综合见 [[Anthropic-AI原生SDLC治理循环]]、[[agent-生产级落地的鸿沟]]；
实体侧状态见 [[Anthropic]]。本页只做忠实摘录与口径标注。

## 一句话

一篇**下游代价**的一手账本：当 Claude 写掉 80% 的代码、人均季度出码量涨 8 倍之后，瓶颈不在写代码、
也不在评审，而是移到了 CI——6 个月内 CI job 涨 25 倍，把决定"每个 PR 该跑哪些测试"的测试影响分析服务压垮。

> "Writing code is no longer the constraint, and once PR review gets accelerated, CI starts feeling the pressure."

## 自报数据（全部为 Anthropic 内部口径，无第三方审计）

| 指标 | 值 | 原文口径 |
|---|---|---|
| 人均季度出码量 | 8×（对比 2021–2025） | "ship 8x as much code per quarter as they did from 2021-2025"；**基线是 2021–2025 这段时期，不是某一年** |
| Claude 撰写占比 | 80% | "Claude authors 80% of that code"；同时"plays a large role in reviewing and approving PRs" |
| 代码库测试总量 | 10× | 与出码增长同期 |
| CI job 数 | **25×（6 个月内）** | 明确注明并非每个测试都在每个 PR 上跑 |
| 工程师人数 | "a nominal amount" 的增加 | **未给具体数字或比例** |
| listener 告警阈值 | 落后 50,000 个 job | 内部 Claude Tag 长期会话监控 |
| 20 分钟滞后的后果 | 数万条测试更新未落到 selector | 原文举例口径 |
| 三次临时补丁存活期 | 70 天 / 29 天 / 不到 1 天 | 依次为：加大机器、分片、每日重启 |
| 架构重写工期 | 单人 3 周 | 作者称一年前同等改动需"接近一个季度" |

## 机制：为什么会被压垮

测试影响分析是一套**确定性**服务（不含模型），由 **Listener**（记录每次 CI 运行的测试结果）与
**Selector**（读历史、决定某 PR 跑哪些测试）两部分组成。它跑成单进程，原因是
"keeping a running history per test meant a single writer needed to apply the results"——
每个测试要维护一份运行历史，就需要单一写入者，于是**无法水平分片**。

重写做了三件事：引入内存数据存储卸载状态；listener worker 改为无状态、只追加写日志，因而可水平扩展；
另起一个小消费进程每几秒把日志汇总成每测试历史。

## 原文自陈的代价与边界

- **新架构更贵**：
  > "This distributed architecture is more expensive to run, but it is much easier to scale and memory
  > profile than a shaky singleton."
- **过渡期是有损的**：每日重启期间滞后逐步累积，超过 1 小时后大量 job 结果未被记录；
  滞后期间测试选择用的是过期数据。
- 全文是**单一公司的自报案例**，没有第三方审计，也没有给出逃逸缺陷率、事故率等结果指标——
  它证明的是"基建被压垮并被重写"，不是"重写后质量更好"。

## 四条可复用设计判断（原文 "What I would do differently"）

1. **Account for the AI exponential**：人均 agent 数上升 + PR 批准加速 ⇒ CI job 数呈指数增长，
   容量规划要按指数而非线性做。
2. **Assume 25x load within two quarters**：预算允许时，v0 就按当前感知规模的 10–20 倍设计。
3. **Instrument services as Claude's eyes and ears**：把服务的可观测性当成"给 Claude 装眼睛"，
   让增量优化能由 agent 更快完成；并守住"进来的 job 数 = 出去的 job 数"这类不变量。
4. **Keep state out of the process from the start**：除非能对它及其金丝雀变更做测量，
   否则不要把关键服务跑成有状态单实例。

> 综合：第 1、2 条是本源最可复用的部分——它把"AI 提高出码量"从产出侧的好消息，
> 翻译成了基建侧的**容量规划参数**。但 25× / 两个季度这个具体数字来自 Anthropic 单点经验，
> 且 Anthropic 是 AI 出码密度的极端值（80%），其它团队不应直接照搬倍数，只应照搬"按指数而非线性规划"。

## 口径提示：与 7 月来源的 "8×" 不是同一个指标

[[2026-07-21-Anthropic-AI原生SDLC-源摘要]] 记录的是"每名工程师**每日合并代码行**约为 **2024 年**的 8 倍"，
本源记录的是"人均**季度出码量**为 **2021–2025** 的 8 倍"。两者分母与基线都不同却同为 8×，
引用时必须带上各自口径，不可互相替换或叠加。详见 [[Anthropic]] 该处的矛盾标注。
