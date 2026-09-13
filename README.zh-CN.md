# parallel-subagent-planner

[English](README.md) | [简体中文](README.zh-CN.md)

`parallel-subagent-planner` 是一层很薄的 Codex 委派策略：判断子智能体是否有用，为每个子任务划定边界，并由主线程完成最终整合。

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

本 Skill 使用 Codex 原生子智能体工具，不实现调度器、状态机、角色目录或持久化 Agent 系统。

## 示例

如果一个请求需要修改两个互不依赖的 package，Codex 可以分别委派；每个子智能体只获得目标、可读文件、写入边界和局部测试。主线程随后审查结果并运行工作区级验证。

如果只是单文件修复，或后一步依赖前一步产物，Codex 会留在主线程执行。

## 安装

个人安装：

```bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/codex-parallel-subagent-planner.git \
  "$HOME/.agents/skills/parallel-subagent-planner"
```

项目级安装路径：

```text
<project>/.agents/skills/parallel-subagent-planner/
```

行为回放用例和统计口径位于 [`evals/cases.md`](evals/cases.md)。请固定模型配置，分别在启用与禁用 Skill 时重复运行，记录成功率、耗时，并区分缓存与非缓存 token 用量。模型配置变化应另设对照。

## 开源协议

[MIT License](LICENSE) © 2026 manhua-man
