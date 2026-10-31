---
name: subagent-lane-planner
description: >-
  Drive multi-step engineering work from the main conversation, adapting actions
  as evidence, requirements, or external results change. Use when work needs
  sustained execution and verification, not just a one-off answer or a subtask plan.
---

# Main-Agent Task Loop

Keep the main conversation responsible for the goal, useful action, and final result. Choose the planning depth, investigation breadth, tools, executors, and execution order that best serve the task; revise them as evidence changes.

## Advance the task

- Work from the latest user request and relevant project requirements. Plan, investigate, implement, and verify in whatever order the current evidence supports; carry implementation requests through to delivery.
- Use available skills, tools, and executors where they help. Read [context and capabilities](references/context-and-capabilities.md) for knowledge selection or continuity, and [delegation](references/delegation.md) when coordinating external work.
- Investigate as broadly as needed to understand the problem. Decide changes against the requested outcome; a discovery can change the approach without automatically becoming another deliverable.
- Compare results with actual artifacts and use them to decide the next action. Resolve consequential conflicts, repair failures, and revise assumptions rather than merely forwarding reports.
- Continue while useful progress is possible. Choose retries and alternative approaches from evidence, expected benefit, and cost. If progress requires an unavailable input or decision, explain what remains and what would enable it.

## Coordinate and finish

- Keep concurrent work coherent through clear ownership, isolation, or sequencing. Integrate external results against the current task and source version.
- Verify the requested outcome with appropriate tests or other observable evidence. Expand or revise checks when findings warrant it, and reuse evidence that remains valid.
- Report the result, actual verification, and material unfinished work accurately. Adapt to user redirection or cancellation.

Use the optional [living task plan](references/plan-artifact-template.md) when a saved record helps. In Cursor, consult the [host guide](references/cursor-task-prompt.md); for independent Codex desktop chats, consult the [chat execution guide](references/codex-chat-execution.md). Existing user instructions and host tool rules apply; this skill adds no approval gates or execution permissions.

## Auxiliary Command Modes

Read the requested modifiers and combine them as useful:

- `/goal`: [Persistent execution and acceptance](modes/goal-mode.md).
- `/boost`: [Deeper investigation and review](modes/boost-mode.md).
- `/teamwork`: [Adaptive parallel execution](modes/teamwork-mode.md).

These modes emphasize persistence, depth, or collaboration without prescribing a fixed sequence, retry count, investigation boundary, or team structure. Share and evolve acceptance evidence across modes.

In Codex, select `$subagent-lane-planner` and request `goal`, `boost`, or `teamwork` modes in plain text. These labels do not register host commands; the skill's `goal` modifier is separate from a host-native persistent goal. Use the host's available execution and continuation mechanisms.
