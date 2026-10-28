# subagent-lane-planner

[English](README.md) | [简体中文](README.zh-CN.md)

A **main-agent task workflow**: keep one conversation responsible for the goal, next action, evidence, and completion. Load skills and tools as needed; use external executors only when they add value, then bring their results back into the same task.

The identifier `subagent-lane-planner` and installation paths are retained for compatibility. Former name: `parallel-subagent-planner`; the old `codex-parallel-subagent-planner` repository URL redirects here.

## Core contract

~~~text
Understand the goal → Take a useful action → Check the result → Adapt and continue
                                                          ↘ Verify and finish
~~~

The agent writing the plan is also responsible for carrying it out and revising it. Planning, dispatching, and collecting receipts are not completion.

- Work from the latest goal and constraints, not an immutable initial decomposition.
- Investigate, implement, and verify in the main conversation when appropriate. The workflow remains useful with **no delegation**.
- Load relevant existing skills/references and use available tools; parallel tool calls do not require extra agents.
- Keep consequential facts, decisions, and evidence locations without copying every intermediate log into the main context.
- Use another context for justified independent work, noisy investigation, or independent verification; do not build a fixed team by profession.
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

In Cursor, ask it to use `subagent-lane-planner` with the [host guide](references/cursor-task-prompt.md). Other hosts must use their own supported skill discovery and execution tools.

Use it for multi-step work that needs continued action and adaptation, not as a mandatory gate for every small request. A plan-only request still produces a plan only; an implementation request continues into authorized implementation without a skill-imposed plan approval step.

Apply the current host's tool and authorization rules; the skill does not create permissions or impose a separate explicit-request gate across all hosts.

## Progressive detail

| Need | Read |
|---|---|
| Select knowledge/tools, handle noisy context, change goals, or resume work | [Context and capabilities](references/context-and-capabilities.md) |
| Delegate a bounded piece of work or adapt an authorized independent chat | [Delegation](references/delegation.md) |
| Produce a requested or useful saved plan | [Living task plan](references/plan-artifact-template.md) |
| Adapt to Cursor's actual tool surface | [Cursor host guide](references/cursor-task-prompt.md) |

Delegation retains the four-field `Goal` / `Read` / `Write` / `Acceptance` contract, single ownership of shared writes, stable input ordering, proportional verification, and model-neutral selection. Model policy lives in the delegation reference and is loaded when delegation is needed.

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
