# subagent-lane-planner

[English](README.md) | [简体中文](README.zh-CN.md)

Former name: `parallel-subagent-planner`; the former `codex-parallel-subagent-planner` repository URL redirects here.

`subagent-lane-planner` is a thin delegation policy for Codex. It helps Codex decide whether subagents are useful, give each subagent a bounded task, and keep final integration in the main thread.

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

The skill uses the current host's native subagent tools for ordinary delegation. When the human explicitly asks for independent Codex chats, it also supports the host's creation, waiting, authorized follow-up, and integration tools through the [chat execution guide](references/codex-chat-execution.md). It does not implement a scheduler, state machine, role catalog, or persistent agent system.

## Invocation

In Codex, invoke `$subagent-lane-planner` with the task. In Cursor, ask it to use `subagent-lane-planner` and follow the [host guide](references/cursor-task-prompt.md) with the tools available in that session. Other hosts should use their own supported skill discovery and subagent tools.

Use the optional [plan template](references/plan-artifact-template.md) when requesting a plan. Implementation requests proceed with useful delegation; a separate plan approval is not required by this skill. Apply the skill on demand rather than making it a mandatory gate for every task.

## Example

For a request that changes two independent packages, Codex may delegate one package to each subagent. Each receives only its goal, allowed files, write boundary, and local test. The main thread then reviews both results and runs checks proportionate to the change.

For a one-file fix or a task whose steps depend on one another, Codex stays in the main thread.

For separate sidebar conversations, explicitly request them: “Create two local chats for these independent projects, coordinate them, and send follow-ups to those chats as needed.” This authorizes the initial prompts and scoped follow-ups. A generic request to work in parallel uses native subagents when useful.

## Installation

Personal installation:

```bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/subagent-lane-planner.git \
  "$HOME/.agents/skills/subagent-lane-planner"
```

For a project-scoped installation, copy the skill to:

```text
<project>/.agents/skills/subagent-lane-planner/
```

Behavioral replay cases and measurement guidance live in [`evals/cases.md`](evals/cases.md). Compare repeated runs with and without the skill using the same model settings; report success, elapsed time, and cached/non-cached token usage separately. Evaluate model configuration changes in a separate comparison.

For a completed real task, copy the [post-task review prompt (Chinese)](evals/real-task-review.md) into the original task conversation.

## License

[MIT License](LICENSE) © 2026 manhua-man
