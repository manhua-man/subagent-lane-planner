# subagent-lane-planner

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个**主 Agent 任务推进工作流**：由同一主会话持续掌握目标、下一步行动、关键证据和验收责任；按需加载技能与工具，必要时借助外部执行者，再把结果带回当前任务继续推进。

为保持兼容，保留 `subagent-lane-planner` 标识与安装路径。原名为 `parallel-subagent-planner`；旧仓库地址 `codex-parallel-subagent-planner` 会跳转到当前仓库。

## 核心契约

~~~text
理解目标 → 采取有用行动 → 核对结果 → 修订路径并继续
                              ↘ 达成目标后验收交付
~~~

写计划的主 Agent 也负责执行和修改计划。生成计划、派出任务、收到回执，都不等于完成。

- 以最新需求和约束为准，不机械执行最初的拆分。
- 适合在当前上下文做的调查、实现和验证，就由主会话直接完成；**没有委派时，工作流同样有用**。
- 按需加载已有技能与参考，使用真实可用的工具；并行工具调用不需要额外 Agent。
- 保留影响决策的事实、决定和证据位置，不把所有中间日志塞入主上下文。
- 独立推进、隔离噪声或独立验证有明确价值时，才借助其他执行者；不按专业建立固定团队。
- 对照现场核验外部结果，再采取下一步行动；不把执行者自述当成验收，也不掩盖未完成项。
- 必要验收完成后停止；确有阻塞时说清所缺授权、决定或外部条件。

本 Skill 提供流程指引，不实现调度器、记忆服务、权限边界或后台运行时，不会增加工具、自动续接会话或迁移用户工程规则。

## 调用方式

在 Codex 中：

~~~text
使用 $subagent-lane-planner 完成这项修改。
由主会话持续掌握目标并决定下一步。
按需使用技能、工具或已授权的外部执行者。
~~~

在 Cursor 中，请求使用 `subagent-lane-planner`，并遵循 [宿主说明](references/cursor-task-prompt.md)。其他宿主使用自身支持的 Skill 发现和执行工具。

适用于需要持续行动与调整的多步任务，不作为所有小请求的强制入口。只要求计划时只交付计划；要求实施时继续执行已授权的实现，不因 Skill 模板多加一道计划审批。

调用 Skill 不构成创建独立会话、跨会话发消息、修改配置或扩大外部操作的授权。

## 按需阅读

| 当前需要 | 参考 |
|---|---|
| 选择知识和工具、控制上下文噪声、需求变化或任务续接 | [上下文与能力](references/context-and-capabilities.md) |
| 委派有界任务，或适配已授权的独立会话 | [委派能力](references/delegation.md) |
| 用户要求计划，或长任务确实需要计划记录 | [可修订任务计划](references/plan-artifact-template.md) |
| 对接 Cursor 当前工具能力 | [Cursor 宿主说明](references/cursor-task-prompt.md) |

委派继续保留 `Goal` / `Read` / `Write` / `Acceptance` 四字段合同、共享写入单一 owner、输入就绪顺序、适度验证和不绑定模型名称的选择策略。模型细则下沉到委派参考，需要委派时才读取。

原生子代理和独立会话不是同一种机制。合适且已获授权的已有会话可以保留有用上下文；临时子代理可承担有界隔离工作。两者都不改变主会话对整个任务的责任。本仓库本地测试不代表各宿主的跨会话通信或自动续接已经验收。

## 示例

预览与提交结果不一致时，主会话读取金额契约、追踪真实消费者、修复并运行验收。若新证据推翻初始判断，就调整实现，不只改计划文字。整个过程不必启动第二个 Agent。

确有独立调查时，可以派出有界工作，同时推进其他有用行动；收回证据并核验后，继续完成接入。单纯转发调查总结不算交付。

## 安装

个人安装：

~~~bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/subagent-lane-planner.git \
  "$HOME/.agents/skills/subagent-lane-planner"
~~~

项目级安装路径：

~~~text
<project>/.agents/skills/subagent-lane-planner/
~~~

本次升级不要求改名、安装第二套入口或自动迁移。

## 验证与评测

[参考夹具](evals/fixtures/task_loop/README.md) 使用 Python 3.10 及以上版本，只依赖标准库。在仓库根运行：

~~~bash
python -m unittest discover -s evals/fixtures/task_loop/tests -p 'test_acceptance.py' -v
~~~

这些测试验证夹具的实际输出，不验证 Agent 推理、宿主通信或开发效率。[回放用例](evals/cases.md) 定义错误起点、任务级观察和旧版/原生执行对照。固定模型配置、重复运行，逐项披露失败，区分缓存与非缓存用量。

已执行与未验证内容见 [试点记录](evals/results/pilot.md)。真实任务完成或明确阻塞后，可在原对话使用 [任务复盘提示词](evals/real-task-review.md)。不要用夹具测试声称提速或省费。

## 设计参考

- [Anthropic：When to fold subagents into your main agent loop](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop)：共享上下文、渐进加载，依据证据收敛分工。
- [LangChain：Choosing the Right Multi-Agent Architecture](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture)：先用简单结构，根据上下文和协调需求选择能力，而非照搬组织架构。

## 开源协议

[MIT License](LICENSE) © 2026 manhua-man
