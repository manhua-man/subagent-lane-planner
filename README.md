# parallel-subagent-planner

[English](README.md) | [简体中文](README.zh-CN.md)

`parallel-subagent-planner` is a thin delegation policy for Codex. It helps Codex decide whether subagents are useful, give each subagent a bounded task, and keep final integration in the main thread.

## Core contract

```text
Assess → Delegate the minimum useful work → Verify in the main thread
```

- Default to direct execution for small or sequential tasks.
- Run independent read-heavy work in parallel; parallelize writes only across disjoint scopes.
- Describe each subtask with `Goal`, `Read`, `Write`, and `Acceptance`.
- Give every shared contract or concurrently edited file one owner.
- Keep subagents from delegating further; the main thread reviews and verifies the result.
- Respect user model choices and runtime defaults; use supported overrides when task needs and available capability, speed, or cost evidence justify them. No model names are pinned.
- If a requested model or reasoning level is unavailable, use a suitable supported fallback and briefly notify the user without interrupting for confirmation, unless the user forbids fallback.

The skill uses Codex's native subagent tools. It does not implement a scheduler, state machine, role catalog, or persistent agent system.

## Example

For a request that changes two independent packages, Codex may delegate one package to each subagent. Each receives only its goal, allowed files, write boundary, and local test. The main thread then reviews both results and runs the workspace-wide checks.

For a one-file fix or a task whose steps depend on one another, Codex stays in the main thread.

## Installation

Personal installation:

```bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/codex-parallel-subagent-planner.git \
  "$HOME/.agents/skills/parallel-subagent-planner"
```

For a project-scoped installation, copy the skill to:

```text
<project>/.agents/skills/parallel-subagent-planner/
```

Behavioral replay cases and measurement guidance live in [`evals/cases.md`](evals/cases.md). Compare repeated runs with and without the skill using the same model settings; report success, elapsed time, and cached/non-cached token usage separately. Evaluate model configuration changes in a separate comparison.

For a completed real task, copy the [post-task review prompt (Chinese)](evals/real-task-review.md) into the original task conversation.

## License

[MIT License](LICENSE) © 2026 manhua-man
