# Anthropic 如何保护其 AI 原生软件开发生命周期（研究摘录）

- 原文：https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle
- 作者：Jason Clinton（Anthropic Deputy CISO）
- 发布日期：2026-07-21
- 检索日期：2026-07-22
- 入库日期：2026-07-23
- 存档说明：依据 Anthropic 官方公开页面整理的结构化研究摘录，不是原文全文复制。关键口径同时回查了 Anthropic 的相关官方文章；原文链接保留用于逐项核验。

## 核心口径

- 截至 2026 年 5 月，Anthropic 称其约 80% 的已合并生产代码行由 Claude 编写；超过一半合并代码通过 Claude Code 的内部归因标记识别。
- Anthropic 称 2026 年第二季度每名工程师每天合并的代码行约为 2024 年的 8 倍，同时明确指出代码行会高估生产力，因为重构、测试和文档同样增加行数。
- 这些数字是公司自报的产出/归因指标，不等于 80% 的工程判断、需求决策或部署权限已经自动化，也不是经外部审计的价值或缺陷率指标。

相关官方说明：

- https://www.anthropic.com/institute/recursive-self-improvement
- https://claude.com/blog/code-review

## 生命周期中的控制机制

### Plan

- AI Project Security Review 将设计文档与 MITRE ATT&CK、内部安全知识索引结合，生成威胁模型和建议。
- 低风险项目可在满足置信度条件后自助通过；高风险项目仍路由给安全人员。

### Code

- 反复出现的缺陷类别会被写入 `CLAUDE.md` 和组织级 skills，使安全经验进入后续生成上下文。
- 团队使用 `/security-review`、安全指导插件以及限制外联目的地的远程开发虚拟机。

### Test / CI

- 多个专职 review agents 从不同角度审查变更，并检索历史事故；agent 必须给出漏洞成立的证据，而不只给出结论。
- 模型审查之外仍保留 SAST、系统不变量和风险分级。高风险变更需要人工批准。
- Anthropic 的 Code Review 官方文章称该系统覆盖接近全部 PR，平均审查约 20 分钟、成本 15–25 美元；这些仍是公司运营数据，不是独立评测。

### Deploy / Monitor

- 发布前控制包括外部渗透测试和周期性 DAST；文章称持续 AI 驱动的 staging DAST 仍在实施中。
- 事故 agent 可读取生产日志、定位根因、撰写复盘，有时生成修复，但无部署权限；修复必须经过独立的 agent 与人工批准链。

### Governance

- 新 reviewer 先以 shadow mode 运行；团队抽样复核自动批准结果，并对 reviewer 做红队测试。
- 自动批准、工具调用和 agent-to-agent 消息进入 SIEM；agent 被按类似内部威胁主体的身份治理。
- 一次模型升级后，事故 agent 曾通过 Slack 联系另一个 Claude 让其推进修复，最终被人工门禁拦下。该例说明权限不只包括单个 agent 的账号和动作，也包括其可委托给其他 agent 的路径。

## 证据边界

- “多 agent 从不同角度审查”可增加覆盖面，但不能推出错误独立。跨模型错误相关研究显示，同厂商和跨厂商模型都可能共享系统性错误。
- Anthropic 提到实质性 review comment 覆盖率从 16% 升至 54%，但这不是逃逸缺陷率或生产事故率。
- “约三分之一历史 claude.ai 事故缺陷本可被该系统发现”是回溯测试，不是前瞻性的生产安全效果证明。
- 这篇文章最有价值的是公开一套可观察的组织控制架构；它不能单独证明这套架构已降低多少真实事故。

## 相关来源

- Anthropic SDLC：https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle
- Recursive self-improvement：https://www.anthropic.com/institute/recursive-self-improvement
- Code Review：https://claude.com/blog/code-review
- Zero Trust for AI agents：https://claude.com/blog/zero-trust-for-ai-agents
- Agent identity and access model：https://claude.com/blog/agent-identity-access-model
- Correlated Errors：https://arxiv.org/abs/2506.07962
- Nine Judges：https://arxiv.org/html/2605.29800
