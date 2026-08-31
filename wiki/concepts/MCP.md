---
tags: [概念, AI, Agent, 协议]
created: 2026-07-03
updated: 2026-08-31
sources:
  - "https://www.anthropic.com/news/model-context-protocol （检索于 2026-07-03）"
  - "https://modelcontextprotocol.io/specification/2025-11-25/basic/transports （检索于 2026-07-16）"
  - "https://modelcontextprotocol.io/specification/latest （检索于 2026-08-31）"
  - "https://blog.modelcontextprotocol.io/posts/2026-07-28/ （检索于 2026-08-31）"
  - "https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ （检索于 2026-08-31）"
  - "https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation （检索于 2026-08-31）"
  - "https://modelcontextprotocol.io/docs/learn/architecture （检索于 2026-07-28）"
  - "[[2026-08-27-Uber-软件工厂成本效率-源摘要]]"
  - "https://support.claude.com/en/articles/13837440-use-plugins-in-claude （检索于 2026-07-16）"
  - "https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp （检索于 2026-07-16）"
---

# MCP（Model Context Protocol）

[[Anthropic]] 于 **2024-11-25** 推出的开放标准，用于在**数据源/工具与 AI 应用之间建立
安全的双向（读+写）连接**。2025-12-09 起 Anthropic 已将 MCP 捐赠给 Linux Foundation 旗下新设的
**Agentic AI Foundation（AAIF）**——联合发起方含 Anthropic、Block、OpenAI，另获 Google、Microsoft、
AWS、Cloudflare、Bloomberg 支持——转入厂商中立治理；官方声明维护者与社区决策模式保持不变
（https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ 、
https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation ，
均检索于 2026-08-31）。它是 [[Claude Cowork]] "插件"能连上 legal/CRM/数据系统的**连接层基础**。

## 1. 它解决的核心问题：N×M 集成爆炸

在 MCP 之前，让 AI 用上外部系统是一场组合爆炸：

- 有 **M 个 AI 应用**（Claude、各家 Copilot、各类 agent），**N 个数据源/工具**
  （Google Drive、Slack、GitHub、Postgres、CRM、合同库……）。
- 每一个"应用×工具"配对都要写一段**定制胶水代码** → 总量是 **M × N**（二次方增长）。
- 后果：每接一个新工具，要对所有应用各集成一遍；每出一个新应用，要把所有工具再接一遍。
  集成又慢又脆、彼此不复用——这也是过去很多软件"集成生态"本身构成的壁垒。

MCP 把它从 **M × N 降为 M + N**（线性）：

- 每个工具只需**暴露一个 MCP Server（写一次）**，任何 MCP 客户端都能用；
- 每个应用只需**做一个 MCP Client（写一次）**，就能接入任何 MCP Server。
- 综合：这就是经典的"协议"打法——如同 **HTTP 之于网页、LSP（Language Server Protocol）之于编辑器**；
  常被类比为"**AI 应用的 USB-C 接口**"：一个标准口，插上就通。

## 2. 架构与三种原语

**角色（client-server）：**
- **Host**：用户直接用的 AI 应用（如 Claude Desktop / [[Claude Cowork]]）。
- **Client**：Host 内部与某个 Server 保持 1:1 连接的连接器。
- **Server**：轻量程序，用标准协议暴露某个系统的能力。

**Server 暴露的三种原语（据 MCP 规范）：**
- **Tools（模型可调用）**：可执行的函数，如 `query_crm`、`create_ticket`、`run_sql`。
- **Resources（应用可读取）**：可作为上下文读入的数据，如文件、数据库记录、文档。
- **Prompts（用户可触发）**：可复用的模板/工作流。

**传输与基础协议：** 当前规范版本为 **2026-07-28**（https://modelcontextprotocol.io/specification/latest ，
检索于 2026-08-31）。两种标准传输不变：本地常用 **stdio**，远程使用 **Streamable HTTP**（该版起要求
请求携带 `Mcp-Method` / `Mcp-Name` 头，便于网关不解析 JSON 即可路由）。该版把基础协议改为
**无状态、自包含请求 + 逐请求能力协商**：废除 `initialize`/`initialized` 握手与 `Mcp-Session-Id`，
server 可部署在普通负载均衡之后；服务端发起的交互（如 elicitation）改走 Multi Round-Trip Requests
（MRTR），不再依赖长开的双向流。旧版 **HTTP+SSE** 传输正式弃用（一年退场期）。消息仍基于
JSON-RPC 2.0。（https://blog.modelcontextprotocol.io/posts/2026-07-28/ ，检索于 2026-08-31）

**Client 侧特性与 Extensions（2026-07-28 版）：** 规范把 **Elicitation**（server 反向向用户征询补充
信息）列为 client feature。核心协议之外另设可选的 **Extensions**——须 client 与 server 双方显式协商
启用：**Tasks**（长任务异步执行：持久任务句柄、轮询、中途补充输入）、**Skills over MCP**（把
[[Agent Skills]] 式的结构化工作流指令经 MCP 发现与消费，不再限于单一厂商 agent）、**MCP Apps**
（server 在对话内渲染交互式 UI，运行于沙箱 iframe）。
（https://modelcontextprotocol.io/specification/latest ，检索于 2026-08-31）

**预置 Server（公告示例）：** Google Drive、Slack、GitHub、Git、Postgres、Puppeteer。
**早期采用者：** Block、Apollo、Zed、Replit。

## 3. 支持跨系统上下文，但不自动保证

MCP 的价值是把不同系统的能力统一为可发现、可调用、可返回结构化结果的协议原语。Host 可以把多个
Server 返回的 Resources 或 Tool 结果组装进同一工作上下文，例如读合同、查 CRM、汇总邮件后生成 Brief。

但 MCP 官方架构也明确限定了范围：**MCP 只负责上下文交换协议，不规定 AI 应用怎样使用 LLM 或管理上下文**。
因此它不自动解决：

- 哪些结果应进入、保留或退出上下文；
- 不同工具返回值的业务语义如何对齐；
- 长任务的状态、checkpoint、重试与补偿（2026-07-28 起 Tasks extension 提供任务句柄与轮询原语，
  但属 opt-in，重试与补偿语义仍在协议之外）；
- 哪个 Agent 或 Worker 应在何时调用哪个工具；
- 高风险写操作是否需要人工批准。

统一接口会减少逐系统的连接胶水，但每个 Tool 仍需清晰 Schema、权限和语义说明。
综合：MCP 使“跨系统、带上下文执行任务”更容易实现，**并不保证它自然成立**。

### 3.1 规模化后的代价：上下文膨胀

M+N 的收益在连接层，但每个 Server 独立设计、彼此不知道对方存在，**聚合成本被推给客户端**：
标准 MCP 把所有工具 schema 预加载进每个 session，且随历史每轮重发。Uber 实测装 100+ 工具时开场
约 **50K–70K token** 纯 schema 开销；某第三方办公套件单 server 打包 49 个工具、约 22K token
（[[2026-08-27-Uber-软件工厂成本效率-源摘要]]）。协议 2026-07-28 版的逐请求能力协商与 Extensions
解决的是状态与分发，**schema 预加载仍在默认路径上**；当前有效解法（按需检索、CLI 投影、code-mode）
都在客户端与网关侧。机制与解法详见 [[Agent 工具上下文膨胀]]。

## 4. Cowork 的 Plugin、Connector 与 MCP 如何分工

Anthropic 2026-05 的官方定义已澄清：**Plugin 是 [[Agent Skills|skills]]、connectors、sub-agents 的组合包**，
不是 MCP Server 的别名。Connector 才承担外部服务连接；custom connector 指向 remote MCP server，
plugin 也可能携带 local MCP server。

一个“客户 Brief”任务可以经过多个 connector，而 connector 背后可使用 MCP server：

```
查阅 CRM（CRM Server）
+ 汇总飞书/邮件（邮箱/IM Server）
+ 读取合同（文件/legal Server）
→ 生成 Brief → 写入信息系统（system-of-record Server） → 通知负责人（IM Server）
```

- **双向**很关键：agent 不只读，还可能按 connector 权限写回 system of record。是否要求逐次确认
  取决于具体工具、授权和组织策略，不能从 MCP 协议本身推出。

## 5. 与本 wiki SaaS 论题的关联

- MCP 是把"agent 理论上能替代工作流"变成"agent 真能伸进工作发生的系统里"的那一环。
  **它把'连接层'商品化**——过去 SaaS 厂商赖以设租的"集成难、切换贵"被大幅削弱。
- 因此连接层恰恰是资本市场论题的关键：它移除了"AI 到底能不能插进我们所有系统"这个现实障碍，
  让"替代"从空谈变得**可信**。详见 [[cowork-saas-资本市场冲击]]（第 3 节·护城河穿透 / 第 7 节·范式切换）。
- 同时，被 agent"必须调用"的 system of record（[[cowork-saas-资本市场冲击]] 第 6.1 节）
  反而因 MCP 而更被需要——这是同一枚硬币的两面。

## 6. 协议边界

MCP 位于 [[从知识图谱到 Agent 编排]] 的“集成与行动层”，不是：

- [[GraphRAG 与 Vector RAG|检索策略]]；
- [[Agent 记忆架构|长期记忆系统]]；
- [[building-effective-agents|Workflow / Agent 编排器]]；
- 业务授权和风险接受机制。

传输层可以承载认证，Server 可以执行受控工具；但“模型此刻是否应该调用”“调用结果是否满足业务约束”
以及“是否需要确认”仍是 Host、Server 与组织策略共同承担的治理问题。

## 相关
- 实体：[[Anthropic]]、[[Claude Cowork]]
- 概念：[[building-effective-agents]]（能力层，编排依赖 MCP 的统一接口）
- 架构图解：[[cowork-plugins-架构]]（Plugin / Connector / MCP Server 校正后的分层图）
- 规模化代价：[[Agent 工具上下文膨胀]]（schema 预加载、每轮重发与三条解法）
- 总体边界：[[从知识图谱到 Agent 编排]]
- 母题：[[cowork-saas-资本市场冲击]]
