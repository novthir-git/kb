---
tags: [素材, AI, Agent, Evals, 审计]
created: 2026-08-10
updated: 2026-11-07
sources:
  - "raw/sources/pdfs/2026-A2E-Agent-Auditing-Engine-arXiv-2608.07346.pdf（SHA-256: 97a9829025fd1b33790e68b287c1c67c4d84b3b2e8a0323fc82e4f3cc63558f1）"
  - "https://arxiv.org/abs/2608.07346v1 （v1，即本地 PDF 所存版本；检索于 2026-08-10，2026-11-07 改为固定版本号）"
  - "https://arxiv.org/abs/2608.07346v4 （v4，2026-09-07，现行版；Submission history 检索于 2026-11-07）"
  - "https://arxiv.org/html/2608.07346v4 （检索于 2026-11-07）"
  - "https://github.com/datamllab/A2E （检索于 2026-08-10；GitHub API 复查于 2026-08-31；git 克隆复查于 2026-11-07）"
  - "https://github.com/datamllab/A2E/releases （检索于 2026-11-07）"
---

# A²E《An End-to-End Agent Auditing Engine》源摘要

## 来源信息

- **作者**：Haoning Wang、Mingxun Zhang、Chenyue Yu、Yingjun Shang、Xia Hu、Guanchu Wang、Na Zou（上海人工智能实验室）。
- **版本**：arXiv:2608.07346v1，2026-08-07，18 页预印本。下方「实验与结果」均按 v1；现行版是 v4（2026-09-07），实验已整体替换，见「版本变化」。
- **对象**：A²E（Agent Auditing Engine），面向 agent harness 的任务编排、运行轨迹采集与多维评测引擎。
- **本地存档**：`raw/sources/pdfs/2026-A2E-Agent-Auditing-Engine-arXiv-2608.07346.pdf`。

## 论文解决什么

作者认为，只评基础模型或最终答案，会忽略 prompt 构造、工具表示、上下文管理、执行循环、错误处理与终止策略等 harness 级差异。A²E 因此把 benchmark 适配、原生执行的 trace 采集、结果与过程评分放进同一条管线。

## 三层架构

1. **Task Layer**：内部 [[agent-task-protocol|Agent Task Protocol（ATP）]] 用 `TaskInput`、`AgentBinding`、`AgentRunner`、`TaskTrace` 分离 benchmark 逻辑与 harness 执行，避免为每个 benchmark×harness 组合写适配代码。
2. **Monitor Layer**：用 OpenTelemetry span 与 OpenInference 语义记录 agent、chain、模型、工具和 skill 调用，保留时序、父子因果、状态、耗时、token、错误与制品。
3. **Evaluation Layer**：[[lifecycle-aligned-evaluation|Lifecycle-Aligned Evaluation]] 将指标归到 Reasoning、Action、Final Answer、Runtime Quality 四个阶段；规则、环境 verifier、LLM judge 和统计聚合可以共用统一注册与报告接口。

轨迹、任务结果、指标定义与评分存入结构化数据库。这使新指标、新 judge 或新聚合政策可直接重评历史轨迹，不必重跑 agent。

## 实验与结果（v1）

| 项目 | 设置 / 结果 |
|---|---|
| 主矩阵 | 23 benchmarks × 9 harnesses × 每格 5 tasks = 1,035 runs；同一 DeepSeek-V4-Pro FP4 与对齐配置 |
| 全轨迹子集 | 19 个非 sandbox benchmark，855 条完整轨迹，23 指标，共 19,665 条评分记录 |
| 终点分辨率 | 单轮任务中 9 个 harness 常得到相同最终分；多轮任务差距扩大，如 τ-bench 0–0.6、GDPVal 0–0.6、Traject-Bench 0.2–1.0 |
| 效率差异 | 855 条轨迹中，8 个可观测 harness（CrewAI 的 LLM span 无 token 数，不计）上 correctness 均值仅跨 0.568–0.663、平均 token 差 3.5 倍（2,063–7,319）；按 9 个 harness × 23 个 benchmark 平均（Fig.1），correctness 区间约 0.57–0.68 |
| 案例 | 同一 GLM-5.2 与同一 τ³-bench 任务：LangGraph 成功且用 10,122 tokens；CrewAI 失败且用 96,704 tokens，约 9.6倍 |

作者明确提醒：每格仅 5 个任务，得分粒度为 0.20、方差高，表格不用于给 framework 排总榜。

## 版本变化（2026-11-07 复查）

arXiv abs 页的 Submission history：v1 2026-08-07、v2 08-10、v3 09-04、v4 09-07（检索于 2026-11-07）。v2 的 HTML 仍是上表的实验；**v3 起实验被整体替换**，v4 沿用：

- **新设计**：9 个 harness × 两个底座（gpt-5.6-sol、glm-5.3）× 4 个前沿 benchmark 族（DeepSearchQA、GDPval、τ 系列、Terminal-Bench 2.1），按各 benchmark 官方协议评分；23 个 benchmark 仍在引擎 registry 里，只是不再报告。作者仍声明结果表"not intended as a leaderboard"。
- **v4 主要结论**：harness、benchmark 与模型强交互，"rather than a universal winner"；DeepSearchQA 与 GDPval 上，强底座下 harness 差异小，换 glm-5.3 后变大；τ 系列跨 harness 分化最大；Terminal-Bench 2.1 有明显的模型效应（68.3% vs 48.1%）。
- **案例换了**：同一 GPT-5.6-sol、同一 Terminal-Bench 2.1 任务，Google-ADK 与 LangGraph 两条轨迹都失败（correctness = 0），诊断指标把前者判为早期规划失败、后者判为末段验证与工具调用失败。
- **不再出现**：1,035 runs、855 条轨迹、0.568–0.663、3.5 倍 token 差、"单轮任务看不出差异"、GLM-5.2 的 9.6 倍案例。Fig.1（仍是 DeepSeek-V4-Pro × 9 harness 的 Lifecycle-Aligned 评分）的 correctness 区间改为约 0.42–0.77。
- **保留**：摘要与引言仍写"endpoint correctness alone has limited resolution for distinguishing harnesses"与"no single combination consistently outperforms all others"；ATP、Monitor、Lifecycle-Aligned Evaluation 三层架构不变。v4 作者增加 Xing Xie。

综合："必须评整个系统""终点分辨率有限""没有通吃的组合"这几条上层判断在 v4 仍成立；变的是具体数字和"单轮无差异"这条证据。引用上表数字须注明 v1。

## 可复用部分与边界

- **可复用的是方法契约**：任务边界、统一 trace 语义、outcome/process/lifecycle 分层、轨迹与指标版本分离。
- **不应复用论文排名作选型结论**：v1 样本过小；v4 也显示领先 harness 随 benchmark 与底座而变。
- **过程分不代替结果验证**：某些 instrumentation-derived 指标不能解读为 harness 行为；LLM-as-judge 也继承 [[Evals]] 中的自偏好与错误相关风险。
- **代码仍是早期参考实现**：2026-11-07 复查（克隆 origin/main），仍无 release、无 tag（`git ls-remote --tags` 为空，Releases 页 "There aren't any releases here"）；main 持续开发到 2026-10-09（共 61 个提交，当日 README 记 "Added Jev as Judge"，为四个事实类指标并列写 `*_jev` 分数），2026-08-31 复查时的"最近提交 2026-08-18"已过时。2026-09-04 的提交 6f92413 反转了 hallucination 指标极性（1 = 幻觉，`higher_is_better=false`），**同名指标在不同 commit 下语义相反、评分不可直接比较**。综合：POC 应 pin 到具体 commit。许可已补齐——仓库 2026-08-12 加入 MIT LICENSE（Copyright (c) 2026 Shanghai AI Lab），故 2026-08-10 记录的「未声明 license，不应默认具有再分发或衍生使用权」不再成立（GitHub API `repos/datamllab/A2E`，检索于 2026-08-31）。

## 与 Wiki 的连接

- [[Agent 全轨迹评测与审计]]：将论文抽象成可落地的四类契约和最小闭环。
- [[agent-auditing]]：审计对象与证据边界。
- [[Evals]]：终点结果、过程 trace 与生命周期指标的关系。
- [[agent-生产级落地的鸿沟]]：把可观测、成本、终止和失败恢复纳入生产成熟度。
