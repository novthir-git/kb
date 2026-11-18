---
tags: [素材, AI, Agent, 软件工程, Harness, 验证]
created: 2026-11-18
updated: 2026-11-18
sources:
  - "https://x.com/FinanceYF5/status/2122617964314628121 （推文附带演讲视频；检索于 2026-11-18）"
  - "raw/sources/articles/2026-11-17-poteto-All-Code-Is-Slop-演讲.md"
---

# 2026-11-17 poteto〈All Code Is Slop (Except Yours)〉演讲源摘要

**原文**：poteto（Lauren Tan，SpaceXSI Principal Engineer，Grok Bot 团队）在 AI Engineer Code Summit 的演讲，17:18。
经 @FinanceYF5 于 2026-11-17 转发。
**存档**：`raw/sources/articles/2026-11-17-poteto-All-Code-Is-Slop-演讲.md`（Whisper 转写并校正明显识别错误，
另附幻灯片数字的截帧读数）。

本页只做忠实摘录与口径标注。判断去向见文末，横向整合尚待用户确认。

## 一句话

讲者认为 AI 时代工程师的新本事是"产出暴涨时守住甚至提升质量"。她的办法是投资 agent 的环境，让 agent
默认就做对：**每次纠正 agent，都把纠正写成代码库里的确定性检查，而不是往 rules / AGENTS.md 加一行**；
再用运行时与形式化验证产出可 review 的证据，最后才自动化。

## 论点结构

1. **信任，而非"软件工厂"**：从"agent 写 slop、人来验"的低信任循环，走到"agent 写好代码、agent 自己验"
   的高信任循环。讲者称自己花了 6 个月。
2. **poteto 金字塔**（倒金字塔，越上层越先投入，左侧标 cost）：codebase → static analysis → verification →
   prose（rules、skills、AGENTS.md）→ human review。前两层是确定性的。幻灯片上还有一句 "code is memory"。
3. **代码库是花园 / 有机架构**：代码库是 agent 最大的输入，workaround、反模式、废弃代码会被下一个 agent
   当成既定写法照抄（"each copy makes the next copy more likely"）。约束是骨架，新代码围着它长。
4. **Dune 框架**（"Electron 版 Next.js"）把教训编码成约束：
   - 需要分寸才能用好的 API 会产生 slop：产品代码禁用 `useEffect`，只在 Dune API 内部允许；
   - 目录即上下文：`electron-renderer/` 与 `electron-main/` 互相 import（连类型）由依赖图分析器 + lint 禁止，
     起因是 Cursor 里 agent 把主进程代码引入渲染进程造成卡顿；
   - 文件名即约束：个人项目 `tick.hot.ts` 表示"每 tick 运行、零分配"。
5. **文字是 agent 的逃生口**：agent 用文档、注释、rules、skills 写"不做正确事的理由"，或把一次小纠正
   过度泛化成铁律；注释无法强制执行。Cursor 案例：一个 `setTimeout` 临时修复带着自我辩护的注释，
   9/9 → 10/3 被复制进共享模块 → 10/17 共 183 个定时器。Grok Bot 因此禁掉 99% 的注释，
   改用错误信息指向根因的 lint 规则。
6. **验证是最重要的一步**：code review 缩成看视频、截图、图表、形式化验证结果。
   - 运行时验证：agent 自己跑应用，用 Chrome DevTools Protocol；skill 内含 feature map（功能、入口、证明方式）
     作为人机共享词汇；skill 内置的 CLI/driver 可复用、省 token、可测试。
   - 形式化验证：TLA+ 对跨设备通知等主要流程做模型检查，Lean 证明自研虚拟列表无闪烁/抖动；已发现不少 bug，
     定位为"又一层"而非银弹。
   - UI 属性测试：Bombadil。意图可视化：pstack 插件的 `/statechart` skill。
   - 引用 Cindy Sridharan：2026-05-15 抱怨 AI PR 带微妙 bug 合入；2026-11-05 称问题消失、缺的是验证流程，
     每日 token 70% 用于验证、20–30% 用于生成。讲者称自己的 token 也大部分用在验证上，
     并说"这些都不是新技术，agent 把它们变便宜了，测试与验证进入黄金时代"。
7. **别自动化一个坏循环**：内循环产出 slop 时，自动化只会产出更多 slop、消耗更多 token。顺序：
   纠正时先改代码库 → 先加 lint 阻止新增 → 清理存量 → 做扎实验证 → 再自动化。
8. **外循环**（产品推介段）：X 反馈、Linear 工单、Slack、cron、Datadog/Sentry 告警触发团队共享 Bot。
   例：每次发版自动开 Cursor 项目对整个构建做 fuzz，为每个 bug 开修复 PR 并自动合并。

## 讲者自报数据

| 指标 | 数据 |
|---|---|
| 个人月 PR | 3 月 68 → 10 月 3,127（8 个月累计 10,732） |
| 团队月 PR | 6 月 809 → 10 月 10,926（5 个月累计 23,370） |
| 贡献者 | 6 月 15 → 10 月 227；10 月：1 人 1,000+、22 人 100–999、77 人 10–99、78 人 2–9、49 人 1 个 |
| revert 率（% of commits reverted） | 6 月 0.98% → 7 月 0.61% → 8–10 月 0.47–0.48% |
| 桌面端发版 | 8 月（8/11 上线起）7、9 月 19、10 月 15；间隔中位数 44 h → 25 h → 28 h |
| 注释数 | 7/31 65,824 → 演讲时 1,227 |
| "whenever you correct your agent" 阶梯图 | 7/1–11/1 从 7 升到 167；**纵轴未标注**，推测为累计确定性检查数（综合，置信度中） |
| 性能（5 月 → 现在） | 10 项变快（冷启动 −39%、长对话输入 p90 −65% 等）；5 项变差：打开长对话（冷）+8%、调整窗口 +130%、空闲内存 +12%、空闲 CPU +100%、启动 JS+CSS +285% |
| 一次发版 fuzz | 与 0.79.4 对比，50 个不同 bug：新增 3（0 高 2 中 1 低），既有 47（1 高 9 中 37 低） |

## 口径与边界

- 全部为讲者自报，研究对象是自家产品，无对照组；结尾推介 Grok Bot。
- 综合：若个人 PR 计入团队口径，10 月讲者一人约占团队 PR 的 29%（6 月约 85%）；两个口径的统计范围演讲未说明。
- 综合：revert 率不计入未被 revert 的缺陷；同场展示的 fuzz 报告仍有 47 个既有 bug。
- 综合：口头说"性能多维度变快"，幻灯片显示资源类指标全部退化。
- "大部分产品代码不再需要深度人工 review"、fuzz 修复 PR 自动合并：范围限于产品代码，基础设施/安全代码未提及。
- 推文标题"一个月 3000 个 PR"指讲者个人 10 月数字，团队为 10,926。

## 判断去向（待用户确认后横向整合）

- [[Harness Engineering]]：steering loop"把重复问题编译进环境"的强实例；poteto 金字塔作为按成本排序的版本。
- [[全AI代码库的治理决策]]："每次复制让下次复制更可能"对应长程退化；"治理 + 验证网"路线的正面样本（自报），
  以及 revert 率作为收益度量的局限。
- [[AI编码技术债的三层治理]]：确定性门禁优先于提示词；注释与 prose 作为 agent 的逃生口。
- [[Agent 记忆架构]]："code is memory"，以及 prose 规则被过度泛化的风险。
- [[常驻 AI 同事的竞争格局]]：Grok Bot 团队研发自用数据与外循环定位。
- [[Loop Engineering]]："别自动化一个坏循环"，内/外循环分工。
