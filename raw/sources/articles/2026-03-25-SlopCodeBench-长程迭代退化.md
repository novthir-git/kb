# SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks（中文结构化研究摘录）

- 原文：https://arxiv.org/abs/2603.24755 （全文 HTML：https://arxiv.org/html/2603.24755 ，读取版本 v2）
- 作者：Gabriel Orlanski、Devjeet Roy、Alexander Yun、Changho Shin、Alex Gu、Albert Ge、Dyah Adila、Nicholas Roberts、
  Frederic Sala、Aws Albarghouthi（作者单位含 University of Wisconsin–Madison）
- 发布日期：2026-03-25（arXiv v1）；修订 2026-05-07（v2，本摘录依据）
- 资助：Snorkel AI Open Benchmarks Grants 项目；另有 DARPA 与 NSF 部分资助
- 项目页：https://scbench.ai
- 检索与入库日期：2026-11-05（curl 直连 arXiv abs 与 HTML 全文）
- 存档说明：要点式中文摘录，非翻译或镜像；Table 1、Table 3、Table 6 与正文测量值按原文照录；参考文献与附录题目明细未收录。
- 证据性质：学术团队的基准实验，预印本，未见同行评审信息；只评测 Python 轨道。

## 动机

- 现有 agent 编码基准多为单次评测，只看当前规格下代码对不对，不看代码在未来变更下是否仍可扩展。
- 已有的迭代基准要么把整体解拆成依赖有序的子问题，要么取自成熟开源仓库的提交历史；agent 从不为自己早期的设计决策付代价。
- 作者列出四个必要条件：agent 在自己的先前代码上继续；问题只规定外部行为、不规定内部接口；测试真正隐藏；黑盒契约可用任意语言实现。

## 设计

- 36 个问题、196 个 checkpoint，全部手写。每个 checkpoint 只规定 CLI 或 API 边界上的可观察行为。
- agent 在 C1 从空工作区开始，之后每个 checkpoint 在**自己上一轮的工作区**上扩展；**不提供先前对话上下文**，
  agent 只能从代码当前结构推断。
- **测试不可见**：agent 只看到规格文字与示例，看不到测试套件或其反馈。
- 测试分四类：Core（规格明确提到的功能）、Error（失败模式）、Functionality（穷尽检查正确性的隐藏测试）、
  Regression（之前所有 checkpoint 的测试）。Strict 指全部通过；Iso 指通过本 checkpoint 全部非回归测试；Core 指只通过核心测试；
  Partial 指至少一个 checkpoint 严格通过的问题占比。
- 每个 checkpoint 在全新 Docker 容器中以非 root 用户运行，只有工作目录跨 checkpoint 保留。
- 用各家**原生 harness** 评测（Claude Code、Codex CLI 等），每次运行两小时墙钟上限、无轮次或成本上限，
  默认 just-solve 提示（只要求解题并记录依赖）。详细评测 15 个模型、六家供应商。

## 两个质量指标

- **Structural erosion**：mass(f) = CC(f) × √SLOC(f)；erosion = 圈复杂度 > 10 的函数所占 mass 份额。
  阈值 10 沿用 Radon。含义是复杂度集中在已经很复杂的函数里。
- **Verbosity**：(137 条 AST-Grep 规则命中行 ∪ 结构克隆行) / LOC，取值 [0, 1]。规则来自观察到的冗长写法、最佳实践与社交媒体常见反模式。

## Table 1：15 个模型（照录）

| 模型 | Strict | Iso | Core | Partial | $/CKPT | Net $ | Min/CKPT | Erosion | Verbosity |
|---|---|---|---|---|---|---|---|---|---|
| Opus 4.5 | 9.2 | 17.3 | 57.7 | 25.0 | 2.53±1.57 | 492.40 | 7.2±3.7 | 0.70±0.20 | 0.43±0.18 |
| Opus 4.6 | 9.7 | 20.9 | 67.3 | 27.8 | 3.17±2.82 | 620.80 | 13.1±12.9 | 0.75±0.15 | 0.44±0.19 |
| Opus 4.7 | 8.2 | 20.9 | 65.8 | 36.1 | 2.17±1.83 | 425.34 | 6.8±5.0 | 0.76±0.17 | 0.48±0.21 |
| Sonnet 4.6 | 7.1 | 16.8 | 57.7 | 27.8 | 1.96±1.97 | 383.83 | 14.2±14.2 | 0.75±0.20 | 0.44±0.19 |
| GPT 5.2 Codex | 9.7 | 21.9 | 56.1 | 36.1 | 0.85±0.80 | 167.29 | 12.3±9.7 | 0.73±0.18 | 0.50±0.16 |
| GPT 5.3 Codex | 11.2 | 26.0 | 60.7 | 41.7 | 0.66±0.49 | 129.65 | 7.7±4.6 | 0.64±0.19 | 0.46±0.18 |
| GPT 5.3 Spark | 3.1 | 8.2 | 29.1 | 11.1 | 0.20±0.41 | 37.17 | 2.4±4.6 | 0.68±0.19 | 0.48±0.16 |
| GPT 5.4 | 10.7 | 23.5 | 62.8 | 36.1 | 0.72±0.51 | 141.32 | 8.0±4.7 | 0.51±0.19 | 0.33±0.13 |
| GPT 5.4 Mini | 5.1 | 13.8 | 53.1 | 22.2 | 0.45±0.35 | 89.03 | 6.2±3.8 | 0.66±0.17 | 0.42±0.12 |
| GPT 5.5 | 14.8 | 28.1 | 66.8 | 50.0 | 1.51±0.81 | 295.59 | 6.0±2.4 | 0.49±0.20 | 0.32±0.12 |
| Composer 2 | 6.1 | 16.3 | 52.6 | 13.9 | 0.44±0.44 | 86.31 | 8.8±8.3 | 0.72±0.15 | 0.45±0.17 |
| GLM 5.1 | 9.7 | 13.8 | 40.3 | 30.6 | 1.47±1.45 | 288.85 | 31.4±20.0 | 0.71±0.17 | 0.41±0.18 |
| Kimi K2.5 | 4.6 | 9.7 | 39.8 | 19.4 | 0.33±0.25 | 63.21 | 14.5±10.0 | 0.72±0.20 | 0.44±0.20 |
| Kimi K2.6 | 10.7 | 18.9 | 51.0 | 33.3 | 0.74±0.64 | 133.18 | 26.9±20.7 | 0.76±0.20 | 0.51±0.22 |
| MiniMax M2.7 | 2.0 | 4.1 | 28.1 | 8.3 | 0.34±0.23 | 65.79 | 11.9±6.8 | 0.73±0.16 | 0.47±0.17 |

- 没有任何 agent 端到端解完任何一个问题；最佳 Strict 为 GPT 5.5 的 14.8%，Iso 最高 28.1%。
- 正文称"Opus 4.5 achieves the highest core solve rate at 67.3%"，但表中 Opus 4.5 的 Core 为 57.7，67.3 属于 Opus 4.6。照录未改。

## 随问题推进的变化（§3.1）

- Core 与 Iso 通过率之差从 2.5 倍扩大到 5.4 倍；Core 通过率从 64.6% 降到 35.5%。
- Functionality 通过率变化不到 6 点（62.7% → 57.7%）；Error 通过率从 80.1% 降到 62.2%。
- 每 checkpoint 平均成本从开头到结尾增长 2.2 倍；平均相对改动行比例从 97.4% 降到 29.5%。总计 13.18B token。

## 质量退化与人类对照（§3.2–3.3）

- structural erosion 在 77% 的轨迹中上升，verbosity 在 75.5% 的轨迹中上升；两家前沿实验室的模型退化趋势相似。
- 人类对照面板：473 个 Python 仓库（从 <100 星的业余项目到 >10k 星、200 万行的框架），每个随机抽最多 30 个改动源码的提交，
  共 13,667 个；以最新提交作横截面比较，以提交序列类比 agent 轨迹。
- 人类面板平均 verbosity 0.19、erosion 0.34；agent checkpoint 分别高 2.3 倍与 2.0 倍。473 个仓库中只有 18 个超过 agent 的平均 verbosity。
- 每 checkpoint 增量：agent verbosity +0.0144、erosion +0.0264；人类中位数 0.0022 与 0.0053。正文称约 7 倍与 5 倍，
  贡献列表称 6.6 倍与 5.0 倍。erosion 在 77% 的 agent 轨迹中上升，人类仓库为 53%。
- 人类仓库 2024 年之后比之前略更侵蚀，作者称与 agent 辅助普及后人类代码出现小幅"slop"上升一致，但远低于 agent 单个 checkpoint 的累积量。

## 提示干预（§3.4，Table 3 照录）

两种提示与 just-solve 基线对比：anti-slop 列举应避免的冗长与过度工程模式；plan-first 要求先写计划再写代码。**只在三个 OpenAI 模型上测试。**

| 模型 | 提示 | Strict | Iso | Core | Erosion | Verbosity | Cost |
|---|---|---|---|---|---|---|---|
| GPT 5.3 Codex | Just-Solve | 11.2 | 26.0 | 60.7 | 0.64 | 0.46 | 0.66 |
| | Anti-Slop | 11.2 (+0.0) | 23.5 (−2.6) | 57.1 (−3.6) | 0.42 (−0.22) | 0.31 (−0.15) | 0.73 (+0.07) |
| | Plan-First | 8.2 (−3.1) | 21.4 (−4.6) | 62.2 (+1.5) | 0.55 (−0.10) | 0.40 (−0.06) | 0.68 (+0.02) |
| GPT 5.4 | Just-Solve | 10.7 | 23.5 | 62.8 | 0.51 | 0.33 | 0.72 |
| | Anti-Slop | 9.2 (−1.5) | 25.5 (+2.0) | 61.2 (−1.5) | 0.28 (−0.23) | 0.24 (−0.09) | 0.90 (+0.18) |
| | Plan-First | 9.7 (−1.0) | 25.0 (+1.5) | 63.3 (+0.5) | 0.39 (−0.11) | 0.30 (−0.02) | 0.83 (+0.11) |
| GPT 5.5 | Just-Solve | 14.8 | 28.1 | 66.8 | 0.49 | 0.32 | 1.51 |
| | Anti-Slop | 9.2 (−5.6) | 24.0 (−4.1) | 63.3 (−3.6) | 0.21 (−0.28) | 0.21 (−0.11) | 1.68 (+0.17) |
| | Plan-First | 8.2 (−6.6) | 24.0 (−4.1) | 67.3 (+0.5) | 0.29 (−0.21) | 0.25 (−0.06) | 1.61 (+0.11) |

- anti-slop 下 verbosity 比基线低 27.5%（GPT 5.4）、35.6%（GPT 5.5）、32.8%（GPT 5.3 Codex）；erosion 低 45.1%、57.6%、34.3%。
- 只有 GPT 5.4 + anti-slop 一例出现质量从首到尾改善。
- 基线的 Strict 最好：anti-slop 平均 −2.4 pp，plan-first 平均 −3.6 pp；plan-first 的 Core 平均 +0.8 pp。两种提示的每 checkpoint 成本平均 +12.1%。
- RQ4 小结原话："Better prompts can reduce initial structural erosion by up to 62.3% and verbosity by up to 34.8%, but do not stop iterative degradation. The average quality velocity remains 1.3 percentage points per checkpoint."
- 摘要原话："Explicit quality guidance reduces initial verbosity and erosion by up to a third, without affecting degradation rates."
  与上面正文的 erosion 降幅（最高 57.6% 或 62.3%）不一致，照录未改。

## Table 6：erosion 指标敏感性（照录）

与下一 checkpoint 通过率、成本的预测相关：

| 指标 | 通过率 | 成本 |
|---|---|---|
| Reported erosion | −0.018 | 0.167 |
| Best variant (CC > 12 + Linear SLOC) | −0.136 | 0.095 |
| LOC | −0.212 | 0.502 |
| Mean CC | −0.046 | 0.218 |
| Max CC | −0.117 | 0.356 |
| Clone Ratio | −0.042 | 0.114 |
| AST-grep hits / LOC | −0.052 | 0.151 |

- 原文：九个阈值与体量项变体下结论稳定——与下一轮通过率的预测相关接近零，与下一轮成本的预测相关为正；
  "Size-heavy baselines such as LOC and max CC remain stronger raw cost predictors"。

## 结论原话要点

- "agents pass checkpoints while producing code that erodes and bloats with each turn."
- 提示干预能改善初始质量问题，但"cannot stop the eroding behavior"。
