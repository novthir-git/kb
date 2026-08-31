---
tags: [概念, 自动化, Agent]
created: 2026-07-28
updated: 2026-07-28
sources:
  - "https://www.ibm.com/think/topics/rpa （检索于 2026-07-28）"
  - "https://www.ibm.com/think/topics/rpa-types （检索于 2026-07-28）"
  - "https://www.anthropic.com/engineering/building-effective-agents （检索于 2026-07-28）"
  - "[[MCP]]"
  - "[[building-effective-agents]]"
---

# RPA（Robotic Process Automation）

RPA 全称 **Robotic Process Automation**，中文通常译为“机器人流程自动化”。这里的“机器人”
不是实体机器人，而是模仿人在电脑界面上操作的软件机器人：打开应用、复制数据、填表、点击按钮、
移动文件或跨系统录入。

## 擅长与不擅长

| RPA 擅长 | RPA 不擅长 |
|---|---|
| 高频、重复、规则清晰的任务 | 目标含糊、路径需要动态规划 |
| 稳定界面上的固定操作 | 界面频繁变化且缺少可靠定位 |
| 旧系统没有 API 时的自动录入 | 依赖常识、解释和复杂权衡的判断 |
| 有明确输入、输出和异常分支 | 跨多人、多系统的端到端业务治理 |

IBM 对 RPA 的界定强调规则驱动的重复办公任务，并指出有 API 时，API 集成通常比界面自动化更可靠、
可扩展；复杂的端到端流程还需要 Workflow / BPM 等编排能力。

## 与 Agent、Workflow、MCP 的关系

- **Workflow** 固化可预测的步骤与控制流；
- **RPA** 是 Workflow 可调用的一种界面执行手段；
- **Agent** 在路径难以预定义时负责理解、规划或选择；
- **[[MCP]] / API** 为 Agent 或 Workflow 提供结构化工具接口；
- **人工审批**承担高风险决策的最终授权。

综合：它们不是替代关系。常见组合是：

```text
Agent 读取非结构化需求并作出建议
→ 确定性规则校验
→ 人工批准高风险动作
→ API / MCP 执行
→ 若旧系统无接口，则由 RPA 完成界面操作
```

## 选型原则

1. 有可靠 API 时优先 API / [[MCP]] 工具；
2. 路径稳定、只有 UI 时使用 RPA；
3. 只有在输入或步骤不可预定义时引入 Agent；
4. 不因引入 Agent 而取消幂等、权限、审批、重试和补偿；
5. 不让 RPA 脚本承担它无法证明的业务判断。

总体位置见 [[从知识图谱到 Agent 编排]]。

