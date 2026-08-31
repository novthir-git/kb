---
tags: [素材, AI, Agent, Evals, 审计]
created: 2026-08-10
updated: 2026-08-31
sources:
  - "raw/sources/pdfs/2026-A2E-Agent-Auditing-Engine-arXiv-2608.07346.pdf（SHA-256: 97a9829025fd1b33790e68b287c1c67c4d84b3b2e8a0323fc82e4f3cc63558f1）"
  - "https://arxiv.org/abs/2608.07346 （检索于 2026-08-10）"
  - "https://github.com/datamllab/A2E （检索于 2026-08-10；GitHub API 复查于 2026-08-31）"
renders: []
---

# A²E《An End-to-End Agent Auditing Engine》源摘要

## 来源信息

- **作者**：Haoning Wang、Mingxun Zhang、Chenyue Yu、Yingjun Shang、Xia Hu、Guanchu Wang、Na Zou（上海人工智能实验室）。
- **版本**：arXiv:2608.07346v1，2026-08-07，18 页预印本。
- **对象**：A²E（Agent Auditing Engine），面向 agent harness 的任务编排、运行轨迹采集与多维评测引擎。
- **本地存档**：`raw/sources/pdfs/2026-A2E-Agent-Auditing-Engine-arXiv-2608.07346.pdf`。

## 论文解决什么

作者认为，只评基础模型或最终答案，会忽略 prompt 构造、工具表示、上下文管理、执行循环、错误处理与终止策略等 harness 级差异。A²E 因此把 benchmark 适配、原生执行的 trace 采集、结果与过程评分放进同一条管线。

## 三层架构

1. **Task Layer**：内部 [[agent-task-protocol|Agent Task Protocol（ATP）]] 用 `TaskInput`、`AgentBinding`、`AgentRunner`、`TaskTrace` 分离 benchmark 逻辑与 harness 执行，避免为每个 benchmark×harness 组合写适配代码。
2. **Monitor Layer**：用 OpenTelemetry span 与 OpenInference 语义记录 agent、chain、模型、工具和 skill 调用，保留时序、父子因果、状态、耗时、token、错误与制品。
3. **Evaluation Layer**：[[lifecycle-aligned-evaluation|Lifecycle-Aligned Evaluation]] 将指标归到 Reasoning、Action、Final Answer、Runtime Quality 四个阶段；规则、环境 verifier、LLM judge 和统计聚合可以共用统一注册与报告接口。

轨迹、任务结果、指标定义与评分存入结构化数据库。这使新指标、新 judge 或新聚合政策可直接重评历史轨迹，不必重跑 agent。

## 实验与结果

| 项目 | 设置 / 结果 |
|---|---|
| 主矩阵 | 23 benchmarks × 9 harnesses × 每格 5 tasks = 1,035 runs；同一 DeepSeek-V4-Pro FP4 与对齐配置 |
| 全轨迹子集 | 19 个非 sandbox benchmark，855 条完整轨迹，23 指标，共 19,665 条评分记录 |
| 终点分辨率 | 单轮任务中 9 个 harness 常得到相同最终分；多轮任务差距扩大，如 τ-bench 0–0.6、GDPVal 0–0.6、Traject-Bench 0.2–1.0 |
| 效率差异 | 855 条轨迹中，correctness 均值仅跨 0.568–0.663，8 个 token 可观测 harness 的平均 token 差 3.5倍（2,063–7,319） |
| 案例 | 同一 GLM-5.2 与同一 τ³-bench 任务：LangGraph 成功且用 10,122 tokens；CrewAI 失败且用 96,704 tokens，约 9.6倍 |

作者明确提醒：每格仅 5 个任务，得分粒度为 0.20、方差高，表格不用于给 framework 排总榜。

## 可复用部分与边界

- **可复用的是方法契约**：任务边界、统一 trace 语义、outcome/process/lifecycle 分层、轨迹与指标版本分离。
- **不应复用论文排名作选型结论**：样本过小，且不同 benchmark 的前沿 harness 不同。
- **过程分不代替结果验证**：某些 instrumentation-derived 指标不能解读为 harness 行为；LLM-as-judge 也继承 [[Evals]] 中的自偏好与错误相关风险。
- **代码仍是早期参考实现**：2026-08-31 复查，GitHub 项目仍无 release、无 tag，最近提交 2026-08-18；许可已补齐——仓库 2026-08-12 加入 MIT LICENSE（Copyright (c) 2026 Shanghai AI Lab），故 2026-08-10 记录的「未声明 license，不应默认具有再分发或衍生使用权」不再成立（GitHub API `repos/datamllab/A2E`，检索于 2026-08-31）。

## 与 Wiki 的连接

- [[Agent 全轨迹评测与审计]]：将论文抽象成可落地的四类契约和最小闭环。
- [[agent-auditing]]：审计对象与证据边界。
- [[Evals]]：终点结果、过程 trace 与生命周期指标的关系。
- [[agent-生产级落地的鸿沟]]：把可观测、成本、终止和失败恢复纳入生产成熟度。
