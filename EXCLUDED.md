# 本压缩包的排除清单（打包于 2026-08-31）

来源仓库：`llm-wiki`（git 主分支 main，提交 59db23b）。
本包为**单向导出物**：不可反向解压覆盖源仓库（会把 symlink 变成实体文件，形成第二事实源）。

## 一、与知识内容无关，完全排除

| 路径 | 大小 | 理由 |
|---|---|---|
| `.git/` | 76M | 版本历史 |
| `.llm-wiki/` | 5.1M | 第三方 App 本机项目状态与 UUID（本就在 .gitignore） |
| `.claude/`、`.agents/` | 684K | 两份完全相同的通用 llm-wiki 工具文档，非知识内容 |
| `.obsidian/` | 24K | Obsidian 本机窗口状态 |
| `.claude/settings.local.json` | 4K | 本机权限白名单，私有配置 |
| `agent-workspace/` | 0B | 空目录 |
| `.DS_Store` | — | macOS 元数据 |

## 二、含内部代号，排除

| 文件 | 理由 |
|---|---|
| `output/罗伯特智能体问答系统方案.html` | 含企业内部代号；按 `wiki/purpose.md` 规定内部代号不得出现在对外产物中 |

注：`wiki/log.md` 中提及该文件的**操作记录**予以保留（append-only 日志不可修改）。

## 三、因体积上限（30M）排除的素材，共 1 个

| 文件 | 大小 | 补回方式 |
|---|---|---|
| `raw/sources/pdfs/2026-A2E-Agent-Auditing-Engine-arXiv-2608.07346.pdf` | 16.2M | https://arxiv.org/abs/2608.07346 |

补回时**必须同名放回 `raw/sources/pdfs/`**，否则 wiki 内 20 处引用断链。
校验 SHA-256 应为 `97a9829025fd1b33790e68b287c1c67c4d84b3b2e8a0323fc82e4f3cc63558f1`。
该 PDF 的内容已完整沉淀在 `wiki/sources/2026-08-07-A2E-Agent-Auditing-Engine-源摘要.md`
及 10 个 wiki 页中，知识层不受影响。

## 四、打包时的改写

- 根目录 `CLAUDE.md`、`purpose.md`、`schema.md` 在源仓库中是 symlink，
  打包时已解引用为实体文件（分别等同于 `AGENTS.md`、`wiki/purpose.md`、`wiki/schema.md`）。
- `wiki/schema.md` 中的本机绝对路径已改为相对路径（源仓库同步修改）。

## 保留内容

`raw/`（除上述 1 个 PDF）、`wiki/`、`briefs/`、`output/`（除上述 1 个 HTML）、
`AGENTS.md`、`CLAUDE.md`、`purpose.md`、`schema.md`、`.gitignore`。
