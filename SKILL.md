---
name: subagent-lane-planner
description: >-
  Drive multi-step engineering work from the main conversation, adapting actions
  as evidence, requirements, or external results change. Use when work needs
  sustained execution and verification, not just a one-off answer or a subtask plan.
---

# Main-Agent Task Loop

Keep the main conversation responsible for understanding the task, deciding the next useful action, acting, and judging the result. Skills, tools, and external executors serve that loop; delegation is not a required stage. This is a workflow over the host's existing capabilities, not a scheduler or a new agent runtime.

## Keep the goal authoritative

- Work from the latest user goal, constraints, and observable acceptance result. Preserve relevant decisions and user changes; an old plan or external receipt cannot override them.
- Plan only far enough to take useful action. The agent carrying out the work also revises its plan when evidence changes. Do not insert a separate planning or routing agent.
- Honor the requested deliverable: implement when asked to implement; stop at a plan when asked only to plan. Use the optional [task plan](references/plan-artifact-template.md) when a reviewable plan is useful, not for every request.

## Take the next useful action

- Investigate, implement, or verify directly when the current context is the right place for the work. A multi-file task does not by itself require multiple agents.
- Load relevant existing skills or references and use the actual available tools. Parallel tool calls in the same context do not require extra agents.
- Read [context and capabilities](references/context-and-capabilities.md) when selecting specialized knowledge, handling noisy context, changing goals, or resuming a long task. Do not preload unrelated material.
- Delegate only when independent progress, context isolation, or independent verification has clear value. Before doing so, read [delegation](references/delegation.md) for authorization, executor choice, model policy, task boundaries, and result integration. Do not create a fixed team by profession.
- Follow project role restrictions and host permissions. A skill invocation is not permission to create standalone chats, message other chats, or expand external writes. In Cursor, read the [host guide](references/cursor-task-prompt.md) when host-specific adaptation is needed.

## Make results change the work

- Compare tool output and external conclusions with the current goal and actual artifacts. Resolve material conflicts before relying on them; use original evidence when a summary omits something needed for the decision.
- Accept relevant findings into the main task understanding, then take the next action: connect an interface, fix a defect, run a check, revise the approach, or close a resolved item. Receiving a result is not the deliverable.
- If the original approach is disproved, change the action, not only the plan text. Do not repeat already sufficient investigation without a new reason.
- Classify failures before retrying: missing input, unclear scope, environment/tool failure, or an implementation/reasoning problem. Replan only affected work; do not automatically add agents or widen scope.

## Finish the task, not just the turn

- Verify the requested behavior proportionately. Targeted checks come first; expand when shared behavior or actual risk warrants it. Do not repeat successful checks without a relevant change or unresolved risk.
- A plan, dispatch, idle executor, or completion claim is not proof of completion. Check required artifacts, integration, and actual verification; unresolved required work remains incomplete.
- Continue safe, in-scope work while useful actions remain. When progress requires user authority, a decision, or an external condition, report the specific blocker, pending work, and resumption condition.
- If asynchronous work requires ending this turn, retain enough task context to resume and distinguish "waiting" from "done." Use only the host's supported receipt/resumption mechanism; do not invent background execution or automatic wakeups.
- Once the goal and necessary checks are satisfied, stop. Report the result, actual verification, and material unverified items briefly.
