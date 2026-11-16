---
tags: [素材, AI, Agent, 记忆]
created: 2026-11-16
updated: 2026-11-16
sources:
  - "https://www.anthropic.com/research/components-of-agent-memory （检索于 2026-11-16）"
  - "raw/sources/articles/2026-11-06-Anthropic-Agent记忆的组成.md"
---

# 2026-11-06 Anthropic《The components of agent memory》源摘要

**原文**：Anthropic Research（Engineering 团队），2026-11-06，作者 Lance Martin。
**存档**：`raw/sources/articles/2026-11-06-Anthropic-Agent记忆的组成.md`（中文结构化摘录；图中数字取自图片 alt 文本）。

判断去向：记忆层级与 dreaming 的概念归位见 [[Agent 记忆架构]]；对本 wiki 方法论的外部实证见
[[llm-wiki-方法论]]。本页只做忠实摘录与口径标注。

## 一句话

Anthropic 把 agent memory 定义为**从经验中获得、跨会话保留、以可读上下文保存的知识**，给出四层记忆层级，
并用五组自家实验论证：前沿模型已能自行判断"什么值得记"，而离线的 **dreaming** 负责纠错、建 wiki、
上浮常驻内容、补会话留下的空白。

## 定义与边界

- 是：经验（用户互动 + 被分配的任务）→ 跨会话保留 → 存为日后可读的上下文。
- 不是：权重变化、in-context learning、compaction。

## 四层记忆层级（自下而上）

| 层 | 内容 | 谁写 / 何时读 |
|---|---|---|
| Transcripts | 可搜索的事件日志 | 运行时自动产生；dreaming 的 ground truth |
| Memory notes | Claude 写下的显著观察 | 会话内按 salience 写；dreaming 可纠正 |
| Memory representations | 如 wiki：按主题聚合并互链的页面 | 主要由 dreaming 构建与修剪 |
| Injected context | 每次会话开始预加载 | 必须小；dreaming 负责把细节下移、留链接 |

## 实验与数字

| 实验 | 结果 | 口径边界 |
|---|---|---|
| CL-Bench 1.0 数据库任务 | mean reward 无记忆→有记忆：Opus 5.5 0.655→0.838；Opus 5 0.564→0.828；Opus 4.7 0.383→0.700；Sonnet 4.6 0.330→0.364 | 单一任务；Opus 5 是第一个"闭环"（规则 + 依据 + 陷阱）的模型 |
| 写入规则消融 | "只记失败"使记忆增益下降：Opus 5 −0.234、Opus 4.7 −0.150 | 强模型自由判断优于预设规则；对旧模型反之（Sonnet 4.6 加引导 0.364→0.641） |
| Pokémon Red（各一次运行，约 10,000 步） | Sonnet 3.7：413 文件 / 977,930 字符 / 1 徽章；Fable 5：10 文件 / 43,406 字符 / 4 徽章 | 单次运行对比；机理：屏幕可读信息存了冗余且持续过时 |
| Mt. Moon（dreaming 纠错） | 改正笔记后第 1,935 步抵达 Cerulean；未改正与无记忆均未抵达 | 单一情境的演示 |
| Stainless 语料（约 420M tokens，25 题） | wiki only 13%→48%；wiki+search 54%→61%；search only 53%；wiki+search 每题省约 2 万 tokens | 128 次会话 dreaming 建库，靠 shared log 协调；25 题小样本 |
| Harvey LAB 并购 24 题 | wiki 87% vs search 73% | 增益集中在跨文档、需判断/计算的题 |
| LAB 单文档可检索任务 | wiki 无明显增益 | — |
| LAB wiki 膨胀 | 10 份文档 115 KB → wiki 203 KB（1.77×） | "effectively abstracted nothing" |
| 合同条款任务 | 多 agent 并发写共享表：41/57（72%）；改为每合同一页、单 agent、逐字引用：57/57（100%） | 失败原因：互相覆盖 + 概括失真 |
| 第二轮 dreaming 补空白 | 9 条悬空链接改指已有页，新增 3 页（含 index） | — |

全部为 Anthropic 自家实验、自家模型，无第三方复现；多数实验题量小（25、24 题）或为单次运行对比。

## 机制主张

1. **记忆是预测**：写下规则 = 预测该模式会再相关；写下已验证事实 = 预测未来可免复核依赖它。
2. **告诉它记忆用来干什么，别规定怎么用**：前沿模型默认只给简单指引；固定写入规则可能有害。
3. **只记世界没告诉你的东西**：可随时重新观察的状态不入记忆；策略、计划、经检验的规则才入。
4. **常驻层必须小**：注入记忆占 token，错误笔记会被带进每次会话；Claude Code auto memory 只加载
   `MEMORY.md` 前 200 行或 25 KB，作为"我知道什么、在哪找"的索引。
5. **wiki 是检索的补充而非替代**：wiki + 搜索最好；纯 wiki 在该实验里低于纯搜索（48% vs 53%）。

## 开放问题（原文自承）

何时写记忆（在线写分心 vs 后台 dreaming 有延迟）；如何保鲜（dreaming 耗算力，或按易变性 / 访问频率调节奏）；
是否以 transcript 搜索为底座、再叠 wiki 表示（维护表示要算力，且要防累积错误与幻觉）。

## 口径与利益提示

- 厂商研究博客，同时服务 Managed Agents 的 memory / dreams 产品与 cookbook 推广。
- 文中"longer instruction files reduce adherence"引的是 Claude Code 自家文档，不是本文新测量
  （与 McMillan 实验的矛盾见 [[AI编码技术债的三层治理]]）。
