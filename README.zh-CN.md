# subagent-lane-planner

[English](README.md) | [简体中文](README.zh-CN.md)

原名为 `parallel-subagent-planner`，原仓库地址 `codex-parallel-subagent-planner` 会跳转到当前仓库。

`subagent-lane-planner` 是一层很薄的 Codex 委派策略：判断子智能体是否有用，为每个子任务划定边界，并由主线程完成最终整合。

## 核心契约

```text
判断 → 委派最少且有价值的工作 → 主线程验证
```

- 小任务或单一依赖链默认由主线程执行。
- 独立、只读为主的工作适合并行；写任务只有在范围互不重叠时才并行。
- 每个子任务只需 `Goal`、`Read`、`Write`、`Acceptance`。
- 共享契约或并发编辑的文件只能有一个 owner。
- 子智能体不得继续委派；主线程负责审查结果和全局验证。
- 尊重用户指定的模型与运行环境默认值；根据任务需要和已有的能力、速度或成本证据，按需使用工具支持的模型覆盖，不绑定具体模型名称。
- 指定模型或推理强度不可用时，自动选择合适且受支持的替代项，并简短告知用户，无需中断确认；用户明确禁止回退时不替换。

日常委派使用当前宿主的原生子智能体工具。用户明确要求独立 Codex 聊天时，也可按 [会话执行说明](references/codex-chat-execution.md) 使用宿主的创建、等待、已授权跟进与整合工具。不实现调度器、状态机、角色目录或持久化 Agent 系统。

## 调用方式

在 Codex 中，使用 `$subagent-lane-planner` 并附上任务。在 Cursor 中，请求使用 `subagent-lane-planner`，按 [宿主说明](references/cursor-task-prompt.md) 使用当前会话提供的工具。其他宿主应使用其支持的 Skill 发现机制和子智能体工具。

需要规划产物时，可使用 [可选计划模板](references/plan-artifact-template.md)。实施请求会直接执行有价值的委派，本 Skill 不要求额外审批计划。按需使用，无需把它设为所有任务的强制入口。

## 示例

如果一个请求需要修改两个互不依赖的 package，Codex 可以分别委派；每个子智能体只获得目标、可读文件、写入边界和局部测试。主线程随后审查结果，并按改动影响选择验证范围。

如果只是单文件修复，或后一步依赖前一步产物，Codex 会留在主线程执行。

如果需要侧栏中的独立会话，可明确要求：“为这两个独立项目各创建一个本地聊天，协调它们，并按需向这两个聊天发送跟进。”这授权初始任务和范围内的后续消息。普通“并行推进”仍在有收益时使用原生子智能体。

## 安装

个人安装：

```bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/subagent-lane-planner.git \
  "$HOME/.agents/skills/subagent-lane-planner"
```

项目级安装路径：

```text
<project>/.agents/skills/subagent-lane-planner/
```

行为回放用例和统计口径位于 [`evals/cases.md`](evals/cases.md)。请固定模型配置，分别在启用与禁用 Skill 时重复运行，记录成功率、耗时，并区分缓存与非缓存 token 用量。模型配置变化应另设对照。

真实任务完成后，可以把 [任务复盘提示词](evals/real-task-review.md) 复制到原任务对话中，依据执行记录评测这次委派的实际表现。

## 开源协议

[MIT License](LICENSE) © 2026 manhua-man
