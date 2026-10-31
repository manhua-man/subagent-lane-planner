# subagent-lane-planner

[English](README.md) | [简体中文](README.zh-CN.md)

A **main-agent task workflow**: keep one conversation responsible for the goal, next action, evidence, and completion. Load skills and tools as needed; use external executors only when they add value, then bring their results back into the same task.

The identifier `subagent-lane-planner` and installation paths are retained for compatibility. Former name: `parallel-subagent-planner`; the old `codex-parallel-subagent-planner` repository URL redirects here.

## Core contract

~~~text
Understand the goal → Take a useful action → Check the result → Adapt and continue
                                                          ↘ Verify and finish
~~~

The main agent owns the outcome and adapts its approach. Planning depth, investigation breadth, team structure, execution order, and retry strategy are left to its judgment; judge delivery by the result and evidence.

- Work from the latest goal and constraints, not an immutable initial decomposition.
- Investigate, implement, and verify in the main conversation when appropriate. The workflow remains useful with **no delegation**.
- Load relevant existing skills/references and use available tools; parallel tool calls do not require extra agents.
- Keep consequential facts, decisions, and evidence locations without copying every intermediate log into the main context.
- Choose external contexts, team structure, and delegation depth according to useful work and coordination cost.
- Check external results against current artifacts, then take the next action. Report required unfinished work rather than accepting completion claims.
- Stop after necessary acceptance, or identify the real authority, decision, or external condition blocking progress.

This skill provides instructions, not a scheduler, memory service, permission boundary, or background runtime. It does not create new tools, automatically continue chats, or migrate your existing project rules.

The main loop can choose direct work, native subagents, or independent chats when they provide value and the host permits them. For Codex desktop, see its [chat execution guide](references/codex-chat-execution.md); its current tools impose specific creation and messaging conditions.

## Invocation

In Codex:

~~~text
Use $subagent-lane-planner to complete this change.
Keep the main conversation responsible for the goal and next action.
Use skills, tools, or authorized external work only as needed.
~~~

Codex uses the repository's root `SKILL.md` and `agents/openai.yaml` directly, so no separate `adapters/codex/` copy is needed. After installing the complete bundle in one of the locations below, select the skill with `$subagent-lane-planner` and name the desired modes in the same request:

~~~text
Use $subagent-lane-planner with goal, boost, and teamwork modes to complete this change.
~~~

The skill's `goal` modifier is distinct from the host's native `/goal` command. Installing this skill does not register or replace `/goal`, `/boost`, or `/teamwork` commands. Use the plain mode names above to avoid command interception. If the skill does not appear after installation, restart Codex and check that it is enabled and that the complete bundle is in a discovered skill directory. See the official [skill discovery and invocation guide](https://developers.openai.com/codex/skills/) and [slash-command reference](https://learn.chatgpt.com/docs/reference/slash-commands).

In Cursor, ask it to use `subagent-lane-planner` with the [host guide](references/cursor-task-prompt.md). Other hosts must use their own supported skill discovery and execution tools.

Use it for multi-step work that needs continued action and adaptation, not as a mandatory gate for every small request. A plan-only request still produces a plan only; an implementation request continues into authorized implementation without a skill-imposed plan approval step.

Apply the current host's tool and authorization rules; the skill does not create permissions or impose a separate explicit-request gate across all hosts.

## Optional modes

Request a mode by name or describe its behavior. Read only the selected mode files; ordinary tasks still use the base workflow.

| Mode | Behavior |
|---|---|
| [`/goal`](modes/goal-mode.md) | Continue useful work and repairs through relevant acceptance; report genuine blockers and unverified results accurately. |
| [`/boost`](modes/boost-mode.md) | Follow evidence across modules or layers, challenge assumptions, and verify the requested result. |
| [`/teamwork`](modes/teamwork-mode.md) | Adapt parallel work and coordinate writes and evolving interface assumptions. |

For example:

~~~text
Use subagent-lane-planner with /goal /boost /teamwork to update the API and both consumers.
Explore the API and consumers in parallel, coordinate interface assumptions, and verify the integrated result.
~~~

Modes combine under the [shared guidance](SKILL.md#auxiliary-command-modes), reuse valid evidence, and evolve checks as findings warrant. There is no fixed retry count, investigation boundary, team shape, or required execution sequence. They preserve user scope, plan-only requests, cancellation, and host authorization. When useful parallelism or required tools are unavailable, continue feasible direct work and disclose the limitation. Mode names describe skill behavior; native slash-command registration depends on the host. Use a plain-language request if the host reserves a command name.

## Progressive detail

| Need | Read |
|---|---|
| Select knowledge/tools, handle noisy context, change goals, or resume work | [Context and capabilities](references/context-and-capabilities.md) |
| Delegate a bounded piece of work or adapt an authorized independent chat | [Delegation](references/delegation.md) |
| Produce a requested or useful saved plan | [Living task plan](references/plan-artifact-template.md) |
| Adapt to Cursor's actual tool surface | [Cursor host guide](references/cursor-task-prompt.md) |

The `Goal` / `Read` / `Write` / `Acceptance` fields help describe assignments when useful; `Read` gives investigation starting points rather than an access whitelist. Coordinate writes and evolving assumptions, then verify the integrated outcome. Model guidance lives in the delegation reference.

Native child agents and independent chats are different mechanisms. A fitting, authorized existing chat may retain useful context; a fresh child may suit bounded isolated work. Neither changes ownership of the main task. Host-specific cross-chat delivery and resumption are not certified by this repository's local tests.

## Example

For a failing preview/commit flow, the main agent reads the relevant amount contract, traces the real consumers, repairs them, and runs their acceptance checks. If evidence disproves the first hypothesis, it changes the implementation, not only its plan. No second agent is required.

For genuinely independent investigations, it may dispatch bounded work, continue another useful action, verify the returned evidence, and use it to complete the next integration step. Merely forwarding the investigators' summaries is not the final result.

For separate Codex desktop sidebar conversations, its current `create_thread` tool requires a human request to create new tasks; scoped follow-up messages also need human authorization. Other hosts may permit autonomous chat creation and coordination, in which case the main loop can choose that route when useful.

## Installation

Personal installation:

~~~bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/subagent-lane-planner.git \
  "$HOME/.agents/skills/subagent-lane-planner"
~~~

Project-scoped installation:

~~~text
<project>/.agents/skills/subagent-lane-planner/
~~~

No skill rename, duplicate entry point, or automatic migration is required for this update.

### Optional host adapters

Keep the **complete repository bundle** at the installation path above, including `SKILL.md`, `modes/`, and `references/`. The adapters are thin entry points; copying an adapter alone does not install its rules.

| Host | Optional entry point |
|---|---|
| Codex | Use the root [`SKILL.md`](SKILL.md) and [`agents/openai.yaml`](agents/openai.yaml) from the complete installed bundle. Invoke `$subagent-lane-planner` and request `goal`, `boost`, or `teamwork` modes in plain text; no extra adapter is required. |
| Cursor | Copy the three `.mdc` files from [`adapters/cursor/`](adapters/cursor/) into the project's `.cursor/rules/`. Select the relevant rule through the host's rule controls and request the mode; these files do not themselves register slash commands. |
| Claude Code | Copy the three `.md` files from [`adapters/claude/`](adapters/claude/) into the project's `.claude/commands/` for project commands, or `~/.claude/commands/` for personal commands. Preserve existing files and choose the intended scope. |
| Antigravity | Place [`adapters/antigravity/SKILL.md`](adapters/antigravity/SKILL.md) in a `lane-modes/` directory under the host's configured skill discovery location, then request the corresponding mode. |

Each adapter uses the already selected bundle. If none is selected, it looks in the current project's `.agents/skills/subagent-lane-planner/`, then `$HOME/.agents/skills/subagent-lane-planner/`. For a custom installation, identify its root in the request. All canonical rule paths are relative to that root, never to the copied adapter or current working directory. Missing files are reported rather than silently replaced with an abbreviated policy.

The canonical `SKILL.md` and selected `modes/` files own the rules; adapters only locate them. These are installation instructions, not evidence of a completed host runtime test.

## Validation and evaluation

The [reference fixture](evals/fixtures/task_loop/README.md) uses Python 3.10+ and the standard library only. From the repository root:

~~~bash
python -m unittest discover -s evals/fixtures/task_loop/tests -p 'test_acceptance.py' -v
~~~

These tests verify fixture outputs, not agent reasoning, host messaging, or productivity. [Replay cases](evals/cases.md) specify failing starter preparation, task-level observations, and controlled comparisons against the previous version and native execution. Keep model settings fixed, repeat conditions, and report failures and cached/non-cached usage separately.

See the [pilot record](evals/results/pilot.md) for what has actually run and what remains unverified. For a real completed or blocked task, use the [post-task review prompt (Chinese)](evals/real-task-review.md) in its original conversation. Do not claim speed or cost gains from fixture tests.

## Design references

- [Anthropic: When to fold subagents into your main agent loop](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop): shared context, progressive disclosure, and evidence-based consolidation.
- [LangChain: Choosing the Right Multi-Agent Architecture](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture): start simple and match context/coordination needs to capabilities, not a fixed organization chart.

## License

[MIT License](LICENSE) © 2026 manhua-man
