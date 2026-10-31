# subagent-lane-planner

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个**主 Agent 任务推进工作流**：由同一主会话持续掌握目标、下一步行动、关键证据和验收责任；按需加载技能与工具，必要时借助外部执行者，再把结果带回当前任务继续推进。

为保持兼容，保留 `subagent-lane-planner` 标识与安装路径。原名为 `parallel-subagent-planner`；旧仓库地址 `codex-parallel-subagent-planner` 会跳转到当前仓库。

## 核心契约

~~~text
理解目标 → 采取有用行动 → 核对结果 → 修订路径并继续
                              ↘ 达成目标后验收交付
~~~

主 Agent 对结果负责，并根据现场调整路径。规划深度、调查范围、团队结构、执行顺序和重试策略交给模型判断；交付以实际结果与证据为准。

- 以最新需求和约束为准，不机械执行最初的拆分。
- 适合在当前上下文做的调查、实现和验证，就由主会话直接完成；**没有委派时，工作流同样有用**。
- 按需加载已有技能与参考，使用真实可用的工具；并行工具调用不需要额外 Agent。
- 保留影响决策的事实、决定和证据位置，不把所有中间日志塞入主上下文。
- 根据独立推进、上下文隔离和协作成本，自行选择执行者、团队结构与委派深度。
- 对照现场核验外部结果，再采取下一步行动；不把执行者自述当成验收，也不掩盖未完成项。
- 必要验收完成后停止；确有阻塞时说清所缺授权、决定或外部条件。

本 Skill 提供流程指引，不实现调度器、记忆服务、权限边界或后台运行时，不会增加工具、自动续接会话或迁移用户工程规则。

主任务循环可以根据收益和宿主能力，选择直接执行、原生子智能体或独立会话。Codex 桌面的创建和消息工具有各自的条件，参见[会话执行说明](references/codex-chat-execution.md)。

## 调用方式

在 Codex 中：

~~~text
使用 $subagent-lane-planner 完成这项修改。
由主会话持续掌握目标并决定下一步。
按需使用技能、工具或已授权的外部执行者。
~~~

Codex 直接使用仓库根目录的 `SKILL.md` 和 `agents/openai.yaml`，因此不需要额外复制一份 `adapters/codex/`。将完整目录安装到下文列出的位置后，通过 `$subagent-lane-planner` 选择技能，并在同一请求中指定模式：

~~~text
使用 $subagent-lane-planner，启用 goal、boost、teamwork 模式，完成这项修改。
~~~

本 Skill 的 `goal` 修饰模式与宿主原生 `/goal` 命令是两种机制。安装本 Skill 不会注册或替换 `/goal`、`/boost`、`/teamwork` 命令；使用上面的普通模式名称，可以避免被命令入口拦截。安装后若未显示，请重启 Codex，并检查技能是否启用、完整目录是否位于可发现的技能路径中。参见官方[技能发现与调用说明](https://developers.openai.com/codex/skills/)和[斜杠命令参考](https://learn.chatgpt.com/docs/reference/slash-commands)。

在 Cursor 中，请求使用 `subagent-lane-planner`，并遵循 [宿主说明](references/cursor-task-prompt.md)。其他宿主使用自身支持的 Skill 发现和执行工具。

适用于需要持续行动与调整的多步任务，不作为所有小请求的强制入口。只要求计划时只交付计划；要求实施时继续执行已授权的实现，不因 Skill 模板多加一道计划审批。

遵守当前宿主的工具和授权规则；Skill 本身不赋予额外权限，也不为所有宿主统一增加“用户必须明确要求”的门槛。

## 可选模式

可以指定模式名称，也可以直接描述所需行为。只读取选中的模式文件；普通任务仍使用基础工作流。

| 模式 | 行为 |
|---|---|
| [`/goal`](modes/goal-mode.md) | 持续推进有用行动和修复，完成相关验收；如实报告阻塞和未验证项。 |
| [`/boost`](modes/boost-mode.md) | 随证据跨模块、跨层调查，检验关键假设并验证所需结果。 |
| [`/teamwork`](modes/teamwork-mode.md) | 自行调整并行分工，协调写入与演进中的接口假设。 |

例如：

~~~text
使用 subagent-lane-planner 的 /goal /boost /teamwork 更新 API 和两个消费者。
并行调查 API 与消费者，协调接口假设，验证整合后的结果。
~~~

多个模式遵循[共同指引](SKILL.md#auxiliary-command-modes)，复用有效证据，并根据新发现调整检查。技能不规定固定重试次数、调查边界、团队结构或执行顺序。用户范围、只交付计划的要求、取消指令和宿主授权继续有效。缺少合适并行任务或必要工具时，继续可行的直接工作并说明限制。模式名称描述 Skill 行为，是否注册原生斜杠命令由宿主决定；若名称被宿主占用，可以直接用自然语言请求对应行为。

## 按需阅读

| 当前需要 | 参考 |
|---|---|
| 选择知识和工具、控制上下文噪声、需求变化或任务续接 | [上下文与能力](references/context-and-capabilities.md) |
| 委派有界任务，或适配已授权的独立会话 | [委派能力](references/delegation.md) |
| 用户要求计划，或长任务确实需要计划记录 | [可修订任务计划](references/plan-artifact-template.md) |
| 对接 Cursor 当前工具能力 | [Cursor 宿主说明](references/cursor-task-prompt.md) |

`Goal` / `Read` / `Write` / `Acceptance` 四字段用于在有帮助时说明任务；`Read` 提供调查起点，不是读取白名单。协调写入与演进中的假设，再验证整合结果。模型选择指引保留在委派参考中。

原生子代理和独立会话不是同一种机制。合适且已获授权的已有会话可以保留有用上下文；临时子代理可承担有界隔离工作。两者都不改变主会话对整个任务的责任。本仓库本地测试不代表各宿主的跨会话通信或自动续接已经验收。

## 示例

预览与提交结果不一致时，主会话读取金额契约、追踪真实消费者、修复并运行验收。若新证据推翻初始判断，就调整实现，不只改计划文字。整个过程不必启动第二个 Agent。

确有独立调查时，可以派出有界工作，同时推进其他有用行动；收回证据并核验后，继续完成接入。单纯转发调查总结不算交付。

当前 Codex 桌面的 `create_thread` 工具要求用户明确提出创建新任务，发送范围内的后续消息也需要用户授权。其他宿主若允许自主创建和协调会话，主任务循环可以在有收益时自行选择这条路径。

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

### 可选宿主适配入口

在上述安装位置保留**完整仓库目录**，包括 `SKILL.md`、`modes/` 和 `references/`。适配文件只提供入口，单独复制适配文件并不等于安装了模式规则。

| 宿主 | 可选入口 |
|---|---|
| Codex | 直接使用完整安装目录中的根入口 [`SKILL.md`](SKILL.md) 与 [`agents/openai.yaml`](agents/openai.yaml)。通过 `$subagent-lane-planner` 调用，在普通文本中请求 `goal`、`boost`、`teamwork` 模式，无需额外适配文件。 |
| Cursor | 将 [`adapters/cursor/`](adapters/cursor/) 下三个 `.mdc` 文件复制到项目的 `.cursor/rules/`，通过宿主的规则控件选择对应规则并请求模式；这些文件本身不注册斜杠命令。 |
| Claude Code | 将 [`adapters/claude/`](adapters/claude/) 下三个 `.md` 文件复制到项目的 `.claude/commands/`，或个人的 `~/.claude/commands/`。保留已有文件，按所需作用范围选择位置。 |
| Antigravity | 将 [`adapters/antigravity/SKILL.md`](adapters/antigravity/SKILL.md) 放入宿主所配置的技能发现位置下的 `lane-modes/` 目录，然后请求对应模式。 |

适配文件沿用已选中的完整安装目录；未指定时，先查找当前项目的 `.agents/skills/subagent-lane-planner/`，再查找 `$HOME/.agents/skills/subagent-lane-planner/`。使用自定义位置时，在请求中指出安装根目录。所有正文路径都相对于该根目录解析，不相对于复制后的适配文件或当前工作目录。缺少文件时如实报告，不悄悄用缩略规则代替。

完整规则由主入口 `SKILL.md` 与选中的 `modes/` 文件维护，适配文件只负责定位。这里提供安装说明，不代表已完成宿主运行验收。

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
