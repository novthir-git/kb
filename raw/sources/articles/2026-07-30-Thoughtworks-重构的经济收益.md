# The Economic Benefit of Refactoring（中文结构化研究摘录）

- 原文：https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html
- 作者：Giles Edwards-Alexander（Thoughtworks）；martinfowler.com「Exploring Gen AI」系列
- 发布日期：2026-07-30
- 检索与入库日期：2026-09-23（WebFetch 返回 403，经直连取得正文）
- 存档说明：要点式中文摘录，非翻译或镜像；结果表的测量值按原文照录（事实数据）；附录只保留重构步骤清单，
  未收录原始提示词。
- 证据性质：单个实验、单个 greenfield 应用、单名开发者；作者自称这只是"第一步"。

## 背景

- 约 15 万行的应用（Rust 约 12 万行，其余为 TypeScript 与 Terraform），全部由 agent 编写（主要 Claude Code，部分 Cursor），
  作者基本不读、不审代码。
- 数据访问层长成单个 17,155 行的 Rust 文件：每个查询重复同样的 HTTP 请求与 JSON 编解码样板，无去重、几乎无提取；
  但边界清晰、接口需保持，是理想的重构对象。

## 实验设计

- 假设：对 agent 代码库重构，就是现在花 token，换取以后每次变更更省 token。
- 利用"agent 不会学习"：每完成一步重构，就让全新 sub-agent 执行**完全相同**的代表性变更（在 Firestore 层新增一个
  三方法的 trait，并为假实现与真实实现各写一份），记录 token 与耗时后丢弃该变更。
- Token 用 sub-agent 报告的字符数 ÷ 4 近似（作者称 Claude 当时没有可靠的实时计数）。

## 结果（测量值照录）

| 步骤 | 数据访问层行数 | 最大文件行数 | Rust 总行数 | 每次变更输入 token | 每次变更输出 token | 每次变更耗时（秒） |
|---|---|---|---|---|---|---|
| 基线 | 17,155 | 17,155 | 50,359 | 159,564 | 1,705 | 342 |
| 1 FirestoreClient | 16,706 | 16,706 | 49,910 | 155,205 | 1,723 | 530 |
| 2 extract_doc_id, new_link | 16,562 | 16,562 | 49,766 | 159,227 | 2,105 | 574 |
| 3 link-query helpers | 16,567 | 16,567 | 49,771 | 154,054 | 2,105 | 524 |
| 4 FakeStore predicates | 16,577 | 16,577 | 49,781 | 154,146 | 2,060 | 654 |
| 5 value ctors | 16,469 | 16,469 | 49,673 | 171,251 | 2,036 | 1,353 |
| 6 FieldsBuilder | 16,469 | 16,469 | 49,673 | 171,251 | 2,036 | 1,353 |
| 7 queries.rs | 16,474 | 15,670 | 49,678 | 151,850 | 1,800 | 587 |
| 8 traits.rs | 16,508 | 13,845 | 49,712 | 132,558 | 1,723 | 446 |
| 9 traits/ split | 16,508 | 13,845 | 49,712 | 132,558 | 1,723 | 446 |
| 10 codec.rs | 16,521 | 12,846 | 49,725 | 131,871 | 1,750 | 540 |
| 11 fake_store.rs | 16,535 | 11,122 | 49,739 | 133,016 | 2,460 | 600 |
| 12 store/ split | 16,550 | 9,269 | 49,754 | 104,080 | 2,050 | 490 |
| 13 co-locate tests | 16,550 | 9,269 | 49,754 | 104,080 | 2,050 | 490 |
| 14 complete fake_store.rs | 16,553 | 7,225 | 49,757 | 107,205 | 2,453 | 523 |
| 15 store/ split | 16,608 | 3,695 | 49,812 | 27,360 | 2,113 | 454 |

注：第 5/6、8/9、12/13 步的测量值原文即完全相同，照录未改。

## 作者的发现

- 同一变更的输入 token 从 159,564 降到 27,360（−132,204，约 83%），此后每个触及该层的变更都持续受益；
  按撰文时 Sonnet 5 每百万 token 3 美元计，单次节省约 39.7 美分。
- 机制：数据访问层总行数基本不变（最终拆成 19 个文件），节省来自 **agent 能找到并只读所需的最小文件子集**；
  随机把文件切小不会有同等效果。前几步的去重为最后的拆分铺路，这符合重构的常规推进顺序。
- 输出 token 基本不变：重构没有让变更本身变小；能否降低输出 token，要用更复杂的样例变更才能看出。

## 过程观察

- Claude **不擅长选择**重构，需要人主动引导；开发 harness 里原有的显式重构步骤从未促使它处理这个文件。
  制定计划时，Claude.ai 看出应抽出整个 client 类，Claude Code 只提出 Extract Function。
- 也**不擅长执行**：用 Python 脚本调 grep / sed 做机械改写，常被缩进搞乱；价值最大的一步（拆分 store）首轮被跳过，事后补做。
- 全程约 8 小时，基本无人值守，只在 6 小时 40 分时人工重新引导过一次。

## 局限

- 重构本身的 token 成本没有精确计量，作者只能给出上界 500 万 token（其中还含两次制定计划与实验设计等工作）。
- 单实验、greenfield、单开发者。作者建议后续研究更复杂的变更、更大范围与持续的重构，以及不同重构方法的相对价值。

## 附录摘要：重构步骤（Fowler《重构》第 2 版手法）

计划提示以"可证明保持正确性的编辑序列"为严格定义，且不改变接口；每步都可单独测试，也都单独测试过。

1. Extract Class（FirestoreClient，分离 HTTP 传输职责）+ Extract Function
2. Extract Function：两处高频样板（分别出现在 20 个解析函数中、共 62 处）
3. Extract Function：link 查询辅助函数
4. Extract Function：FakeStore 的 link 谓词
5. Replace Inline Code with Function Call：128 处以上的 JSON 值构造
6. Extract Class：FieldsBuilder
7–12. Move Function：依次拆出 queries、traits（再按领域分成 4 个文件）、codec、fake_store、store/（每个 trait 一个文件）
13. Move Function：测试与其模块同置
