# Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic

- **来源 URL**：https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
- **作者**：Sachin Malhotra（Anthropic）
- **发布日期**：2026-09-14
- **抓取日期**：2026-09-16
- **存档性质**：**结构化摘录，非逐句原文镜像。** 小标题层级与原文一致，所有带数字的陈述均已收录，
  关键论断保留英文原句（引号内为逐字原文，已单独复核）；其余段落压缩为要点。
  原文配图与图注未存档。需要引用原文细节时应回到来源 URL 复核。

---

## 1. AI is evolving CI

自报数据：

- "Anthropic engineers on average ship 8x as much code per quarter as they did from 2021-2025."
- "Claude authors 80% of that code and it also plays a large role in reviewing and approving PRs as well."
- "On top of that, the amount of tests across our codebase grew 10x and we added a nominal amount of engineers."
- "This all led to a 25x increase in CI jobs over a six month period (in case you are trying to do the math,
  not every test runs on every PR as I will explain)."

核心论断：

> "Writing code is no longer the constraint, and once PR review gets accelerated, CI starts feeling the pressure."

## 2. The test impact analysis architecture

一套**确定性**的测试影响分析服务，依据历史表现与包依赖关系决定每个变更该跑哪些测试。两个核心组件：

- **Listener**：记录每次 CI 运行的测试结果。
- **Selector**：读取测试结果历史，决定某个 PR 上跑哪些测试。

问题：当 CI job 达到每秒多个时，listener 开始落后于 PR 队列。落后带来三类风险——坏变更被合入导致测试对所有人
失败；依赖波动造成的不稳定红灯阻塞合并；测试修复或新增测试在 listener 追上之前不会被运行。

> "For example, 20 minutes of listener lag can translate into tens of thousands of test updates not being
> applied to the selector."

架构限制：服务以**单进程**运行，因为 "keeping a running history per test meant a single writer needed to
apply the results"，因此无法水平分片。

## 3. The bumpy road to redesign

### Patch 1: A bigger machine

- 10 月出现问题征兆；把服务核心数翻倍。
- 撑了 **70 天**。

### Patch 2: Sharding

- 2 月开始频繁收到告警页；用内部 Claude Tag 长期会话监控该服务，listener 落后超过 **50,000 个 job**
  时触发通知。
- 改为每个包一个写入器、各自带 worker 的分片。
- 撑了 **29 天**。

### Patch 3: Daily restarts

- 3 月，进程在工作日下午中段触到内存上限。排查只找到 4 个 bug；更换内存分配器无效；
  不愿对已高负载的 singleton 做内存分析。
- 改为每日重启，**撑了不到 1 天**。
- 副作用：日重启让滞后逐步累积，超过 1 小时后大量 job 结果未被记录。

## 4. The redesign

- 为测试选择服务引入数据库 / 内存数据存储；任何 listener worker 都可处理任何结果，**追加写入日志**，
  进程内不保留状态。
- 一个小型独立消费进程每几秒把日志汇总成每个测试的历史记录；selector 直接查询相关结果历史。
- 关键特性：**无状态，因此可水平扩展**。
- 工期：**单名工程师 3 周**完成；作者称一年前同等量级的改动需要"接近一个季度"。
- 效果：切换后服务保持稳定；排队未处理的 job-result 事件从"每天累积积压"变为基本持平。

代价（原文明示）：

> "This distributed architecture is more expensive to run, but it is much easier to scale and memory profile
> than a shaky singleton."

## 5. What I would do differently

1. **Account for the AI exponential**——随着人均 agent 数量增加、PR 批准被进一步加速，CI job 数呈指数增长。
2. **Assume 25x load within two quarters**——只要预算允许，v0 设计就应按感知规模的 10–20 倍来做。
3. **Instrument services as Claude's eyes and ears**——让 Claude 能更快做增量优化；确保"进来的 CI job 数
   等于出去的 job 数"这类不变量可被观测。
4. **Keep state out of the process from the start**——除非能对它和任何金丝雀变更做测量，
   否则不要把关键服务跑成单实例。

结论句：

> "CI is evolving too quickly to proceed any other way."
