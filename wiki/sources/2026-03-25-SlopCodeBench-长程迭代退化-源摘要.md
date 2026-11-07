---
tags: [素材, AI, Agent, 软件工程, 代码质量, 基准]
created: 2026-11-05
updated: 2026-11-07
sources:
  - "raw/sources/articles/2026-03-25-SlopCodeBench-长程迭代退化.md"
  - "https://arxiv.org/abs/2603.24755 （v2；检索于 2026-11-05）"
  - "https://arxiv.org/html/2603.24755 （Table 1 图注、Figure 3 图注复核；检索于 2026-11-07）"
---

# 2026-03-25 SlopCodeBench《How Coding Agents Degrade Over Long-Horizon Iterative Tasks》源摘要

**原文**：Gabriel Orlanski 等 10 位作者（单位含 UW–Madison），arXiv 2603.24755，v1 2026-03-25、v2 2026-05-07，预印本；
资助来自 Snorkel AI Open Benchmarks Grants、DARPA、NSF。
**存档**：`raw/sources/articles/2026-03-25-SlopCodeBench-长程迭代退化.md`（要点式中文摘录；Table 1、3、6 照录）。

判断见 [[全AI代码库的治理决策]]；"提示不改退化速率"作为证据行收在 [[Agent 不会自发偿还结构债]]。本页只做忠实摘录与口径标注。

## 一句话

**第一个让 agent 在自己的代码上反复扩展、并逐轮测质量的基准**：36 题、196 个 checkpoint、15 个模型。
77% 的轨迹结构侵蚀上升；agent 代码比 473 个人类仓库冗长 2.3 倍、侵蚀 2.0 倍；质量提示压低初值，但不改退化速率。

## 设计要点

- 每个 checkpoint 只规定 CLI 或 API 的外部行为，内部结构留给 agent；agent 在**自己上一轮的工作区**上继续。
- **不给先前对话上下文、不给可见测试**；每轮在全新容器里跑，只保留工作目录。原生 harness（Claude Code、Codex CLI 等），两小时上限。
- 两个指标：structural erosion（圈复杂度 >10 的函数所占"复杂度质量"份额）与 verbosity（AST-Grep 规则命中行 ∪ 克隆行占 LOC 比）。
- 只评测 Python 轨道。

## 关键数据

| 项 | 数值 |
|---|---|
| 端到端解完的问题 | 0 / 36 |
| 最佳 Strict（GPT 5.5） | 14.8% |
| erosion / verbosity 上升的轨迹 | 77% / 75.5% |
| agent 相对人类仓库 | 冗长 2.3×、侵蚀 2.0× |
| 每 checkpoint 增速相对人类中位数 | verbosity 约 6.6–7×、erosion 约 5× |
| 每 checkpoint 成本，首 → 尾 | ×2.2 |
| Functionality 通过率，首 → 尾 | 62.7% → 57.7% |
| Error 通过率，首 → 尾 | 80.1% → 62.2% |
| 质量提示的成本代价 | 每 checkpoint +12.1% |
| 质量提示的 Strict 代价 | anti-slop −2.4 pp、plan-first −3.6 pp |
| 提示后平均退化速度 | 仍约 1.3 pp / checkpoint |

综合（本 wiki 从 Table 1 读出，原文未作此判断）：代际趋势分化。Opus 4.5→4.6→4.7 的 erosion 为 0.70→0.75→0.76、verbosity 0.43→0.44→0.48，未降；
GPT 5.2 Codex→5.3 Codex→5.4→5.5 的 erosion 为 0.73→0.64→0.51→0.49、verbosity 0.50→0.46→0.33→0.32，erosion 下降约三分之一。
口径：Table 1 报的是各模型最佳 just-solve 运行在已跑 checkpoint 上的水平值（带 ±），不是每 checkpoint 的退化斜率。
原文最接近的表述只有 Figure 3 图注"两家前沿实验室的模型退化趋势相似"。

## 口径与证据边界

- **提示实验只在三个 OpenAI 模型上做**（GPT 5.3 Codex、5.4、5.5）；只有 GPT 5.4 + anti-slop 一例首尾改善。
  论文只测了提示，**没有测 lint/CI 闸门或周期清理**。
- **erosion 几乎不预测下一轮通过率**（r = −0.018），对下一轮成本只有弱正相关（0.167）；**LOC 是最强的成本预测因子**（0.502），
  Max CC 次之（0.356）。所以 2.2 倍的成本增长更可能由代码体量驱动，而不是由侵蚀度驱动。
- 绿地小程序，每题 3–8 个 checkpoint；与人类的比较是跨任务校准面板，不是同任务对照。
- agent 看不到测试、也没有对话上下文，比日常带测试与记忆的工作方式更严苛。

> ⚠️ 矛盾（原文内部）：摘要称质量提示把初始 verbosity 与 erosion "by up to a third" 压低；但 §3.4 测得 anti-slop 下
> erosion 最多降 57.6%，RQ4 小结称 erosion 最多降 62.3%、verbosity 最多降 34.8%（§3.4 的 verbosity 最大值为 35.6%）。
> 引用时以 §3.4 的分模型数字为准。（发现于 2026-11-05）

> ⚠️ 矛盾（原文内部）：正文称 Opus 4.5 的 Core 通过率最高（67.3%），但 Table 1 中 Opus 4.5 为 57.7、67.3 属于 Opus 4.6。（发现于 2026-11-05）
