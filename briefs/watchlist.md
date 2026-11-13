# 关注名单（watchlist）

每日简报「关注动态」与 `tools/ai_watch.py` 生成的 HTML 共用的**唯一名单**。增删人只改本文件。

- 脚本按表头名解析下面三张表：「人物与机构」「订阅源」「手动查看」。改表时**保留表头列名**，可增删行。
- 分组：A = Claude / Anthropic（核心）；B = Agent 工程一线实践者；C = 研究与行业判断。
- 「XNews」列填 xnews.xgrowing.ai 的账号编号（该账号在其 79 个信源之内）；`—` 表示不在。
- 「状态」：`覆盖` = 有免费渠道；`缺口` = 基本只在 X 发言、免费渠道拿不到。
- 推文与订阅源条目都只是**线索**：进 wiki 的论断必须追到原始网页、论文、公告或仓库（见 AGENTS.md）。
- 建立于 2026-11-13；渠道可用性与最近更新日期均为当日实测。X 用户名中，@bcherny、@karpathy、@AndrewYNg、
  @thsottiaux、@DeepSeekHarness 在本库已有引用，XNews 列有编号者经其信源表确认，其余未逐一核实。

## 人物与机构

| 对象 | 组 | X 账号 | XNews | 免费渠道 | 状态 | 备注 |
|---|---|---|---|---|---|---|
| Anthropic 官方 | A | @AnthropicAI | 15 | Anthropic News；Anthropic Engineering | 覆盖 | |
| Claude 官方 | A | @claudeai | 16 | Claude Blog；Claude Code CHANGELOG | 覆盖 | 只在 X 发的零碎更新靠 XNews |
| Cat Wu | A | @_catwu | 38 | — | 覆盖 | Claude Code 与 Cowork 产品经理（XNews 简介） |
| Boris Cherny | A | @bcherny | — | — | 缺口 | Claude Code 负责人；无固定博客 |
| Alex Albert | A | @alexalbert__ | — | — | 缺口 | Claude Relations |
| Jack Clark | A | @jackclarkSF | — | Import AI | 覆盖 | Anthropic 联合创始人 |
| Dario Amodei | A | @DarioAmodei | 140 | darioamodei.com | 覆盖 | 长文无订阅源，手动查看 |
| Simon Willison | B | @simonw | — | Simon Willison | 覆盖 | 大量转述 AI 圈 X 讨论 |
| Birgitta Böckeler / martinfowler.com | B | — | — | martinfowler.com | 覆盖 | Birgitta 主要用 Bluesky；本库引用 14 次 |
| Mitchell Hashimoto | B | @mitchellh | — | Mitchell Hashimoto | 覆盖 | |
| Hamel Husain | B | @HamelHusain | — | Hamel Husain | 覆盖 | evals |
| Addy Osmani | B | @addyosmani | — | Addy Osmani | 覆盖 | |
| Thibault Sottiaux | B | @thsottiaux | — | — | 缺口 | OpenAI Codex 负责人 |
| Peter Steinberger | B | @steipete | — | — | 缺口 | 博客 2026-02-15 后停更 |
| Andrej Karpathy | C | @karpathy | 128 | Karpathy blog | 覆盖 | 博客极低频，主要靠 XNews |
| Andrew Ng | C | @AndrewYNg | 129 | The Batch | 覆盖 | |
| swyx | C | @swyx | — | Latent Space；AINews | 覆盖 | AINews 的 RSS 停在 2026-09-09，看网页 |
| Nathan Lambert | C | @natolambert | — | Interconnects | 覆盖 | |
| Ethan Mollick | C | @emollick | — | One Useful Thing | 覆盖 | |
| Sebastian Raschka | C | @rasbt | — | Ahead of AI | 覆盖 | |
| Sam Altman | C | @sama | 126 | Sam Altman blog | 覆盖 | |
| OpenAI 官方 | C | @OpenAI | 13 | OpenAI News | 覆盖 | |
| DeepSeek Harness 团队 | C | @DeepSeekHarness | — | — | 缺口 | |

## 订阅源

「类型」：`feed` = RSS/Atom；`changelog` = Markdown 版本日志（取最新版本节）。

| 名称 | 组 | 类型 | URL | 备注 |
|---|---|---|---|---|
| Anthropic News | A | feed | https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml | 社区生成（Olshansk/rss-feeds），条目指向官网 |
| Anthropic Engineering | A | feed | https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml | 社区生成 |
| Claude Blog | A | feed | https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_claude.xml | 社区生成 |
| Claude Code CHANGELOG | A | changelog | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | 无日期，按版本号 |
| Import AI | A | feed | https://importai.substack.com/feed | Jack Clark 周报 |
| Simon Willison | B | feed | https://simonwillison.net/atom/everything/ | 量大，脚本按条数截断 |
| martinfowler.com | B | feed | https://martinfowler.com/feed.atom | |
| Mitchell Hashimoto | B | feed | https://mitchellh.com/feed.xml | |
| Hamel Husain | B | feed | https://hamel.dev/index.xml | |
| Addy Osmani | B | feed | https://addyo.substack.com/feed | |
| Latent Space | C | feed | https://www.latent.space/feed | swyx |
| Interconnects | C | feed | https://www.interconnects.ai/feed | Nathan Lambert |
| One Useful Thing | C | feed | https://www.oneusefulthing.org/feed | Ethan Mollick |
| Ahead of AI | C | feed | https://magazine.sebastianraschka.com/feed | Sebastian Raschka |
| Sam Altman blog | C | feed | https://blog.samaltman.com/posts.atom | |
| OpenAI News | C | feed | https://openai.com/news/rss.xml | 量大，脚本按条数截断 |
| Karpathy blog | C | feed | https://karpathy.github.io/feed.xml | 极低频 |

## 手动查看

没有可用订阅源、或需要在网页上看的入口。

| 名称 | 组 | URL | 说明 |
|---|---|---|---|
| XNews（X 上 79 个 AI 账号的中文聚合） | A | https://xnews.xgrowing.ai/zh | 覆盖 @claudeai、@AnthropicAI、@_catwu、@karpathy 等；第三方服务 |
| darioamodei.com | A | https://www.darioamodei.com/ | Dario Amodei 长文 |
| The Batch | C | https://www.deeplearning.ai/the-batch/ | Andrew Ng 周报 |
| AINews | C | https://news.smol.ai/ | AI 圈 X/Reddit/Discord 每日汇总；RSS 已停更 |

## 已排除

- @heynavtoor：本库引用 10 次，均作为「AI 方法论去机制化失真」的反例（二手转写），不作信源。
- Lilian Weng 博客：最近一篇 2026-07-04，频率过低。
