# Harness engineering for coding agent users（中文结构化研究摘录）

- 原文：https://martinfowler.com/articles/harness-engineering.html
- 作者：Birgitta Böckeler（Thoughtworks）
- 发布日期：2026-04-02；取代 2026-02-17 的初步备忘《Harness Engineering - first thoughts》（原备忘 URL 已重定向至此）
- 检索与入库日期：2026-09-23（WebFetch 返回 403，经直连取得正文）
- 存档说明：要点式中文摘录，非翻译或镜像；保留概念名与作者提出的开放问题，措辞与示例请回查原文。
- 实证跟进：`raw/sources/articles/2026-05-27-Boeckeler-可维护性传感器.md`

## 框架

- 范围：在"使用 coding agent"这一语境里，用户在 agent 内置 harness 之外搭建的**外层 harness**。目标是提高首次做对的
  概率，并在问题到达人眼之前尽量自纠正，从而减少审查苦工与浪费的 token。
- 两个正交维度：
  - **Guides（前馈）vs Sensors（反馈）**。只有反馈，agent 会反复犯同一类错；只有前馈，agent 不知道规则是否奏效。
    为 LLM 消费而写的 sensor 信号（如附带自纠正指令的 lint 消息）尤其有效，作者称之为正面的 prompt injection。
  - **Computational vs Inferential**。前者确定、快、可靠（测试、linter、类型检查、结构分析）；后者是语义分析、
    AI review、LLM-as-judge，更贵且非确定，但能提供语义判断。
- 与 context engineering 的关系：后者是把 guides 与 sensors 交给 agent 的手段。
- **Steering loop**：某类问题重复出现，就改进前馈与反馈控制；也可以让 AI 来写结构测试、起草规则、搭自定义 linter。
- **时机**：按成本把检查分布到提交前、集成后流水线，以及**变更生命周期之外持续运行**的漂移与健康传感器
  （死代码、覆盖质量、依赖扫描），直至运行时反馈。

## 三类调节对象

- **Maintainability harness**：现成工具最多，最容易。计算型 sensor 可靠地抓结构问题（重复、复杂度、缺测试、
  架构漂移）；LLM 能部分处理语义重复、冗余测试、过度设计等，但贵且概率性；问题误诊、不必要的功能、误解指令，
  两者都抓不稳——需求没说清时，正确性不在任何 sensor 的职责内。
- **Architecture fitness harness**：即 fitness functions（性能、可观测性等架构特性）。
- **Behaviour harness**：作者称之为"房间里的大象"。当前普遍做法过度信任 AI 生成的测试，还不够好。

## Harnessability 与模板

- 可被约束性取决于代码库性质：强类型自带类型检查，清晰的模块边界才撑得起架构规则，框架能替 agent 屏蔽细节。
  同事 Ned Letcher 称这类性质为 ambient affordances。遗留系统的难题是：**最需要 harness 的地方最难建 harness**。
- 企业常见的少数服务拓扑可能演化为 **harness 模板**。作者引 Ashby 必要多样性定律：定义拓扑是一次多样性削减，
  使完备的 harness 变得可及；但模板会遇到与服务模板相同的版本脱节问题，且非确定性控制更难测试。
- 人的角色：人带着隐性 harness（约定、对复杂度的痛感、问责、组织记忆），agent 没有。harness 只能部分外化这些；
  目标不是消除人的输入，而是把人的输入引到最重要的地方。

## 开放问题与实践信号（原文列出）

- 开放问题：不断增长的 harness 如何保持连贯、guides 与 sensors 不互相矛盾；信号冲突时能否信任 agent 取舍；
  sensor 从不触发，是质量高还是检测不足；需要评估 harness 覆盖与质量的方法；缺少把各阶段控制作为一个系统来配置与
  推理的工具。
- 实践信号：OpenAI 的分层约束与定期"垃圾回收"、Stripe minions 的反馈左移与 blueprints、变异测试与结构测试复兴、
  LSP 接入 coding agent、Thoughtworks 团队的"janitor army"。
