# Delegation as an Execution Capability

Read before delegating. The main agent still owns the user conversation, current goal, coordination decisions, and final verification. Do not establish a permanent role hierarchy, scheduling system, or agent registry.

## Decide by context and value

- Delegate only when independent progress, isolating noisy work, or independent verification justifies another context and a handoff. Keep tightly coupled reasoning or a single dependent chain together.
- Stable reads may overlap. Parallelize writes only across disjoint scopes with stable inputs; file separation alone is not proof that delegation is useful.
- Give every shared contract or concurrently edited file one owner. Consumers wait for the actual accepted contract rather than guessing a signature.
- Start the minimum useful number of executors. Delegated executors must not delegate further or expand their own ownership.

## Use an authorized, available executor

A native child agent and a standalone chat are different mechanisms. Either may provide work to the main loop; neither changes who owns the task.

- For a bounded fresh-context task, use native subagent tools when allowed by the active runtime and applicable user/project instructions.
- Reuse an independent chat only when the host supports it, authorization covers messaging that target, and its current context fits the task. Check task fit and relevant current facts, not only the title or past expertise.
- Creating a standalone chat requires its own applicable authorization. Implementation intent alone does not authorize new chats, cross-chat messages, automatic archiving, or recurring monitoring.
- Follow the active tool schema, supported models, and project role rules. Do not assume another host's tool names or automatic reply behavior. If the requested carrier is unavailable, continue by another authorized means when feasible and disclose the limitation.

Task-specific write instructions are coordination boundaries, not a separate read-only sandbox. Host permissions and user authorization remain authoritative.

## Choose executor models

- Honor available explicit user model and reasoning choices independently. For unspecified fields, inherit the runtime defaults unless an allowed override has a clear task-specific benefit; this policy permits such overrides only when supported by the active tool and higher-priority instructions.
- If a requested model or reasoning level is unavailable, automatically use a suitable supported alternative, preferring the runtime default when suitable, and continue without requesting confirmation. Briefly tell the user what was requested, what was used, and why. Preserve any supported requested field; do not substitute if the user explicitly forbids fallback. If no suitable alternative is available, report the blocker.
- Choose only actually available models and reasoning levels, using declared capabilities or measured task results. Do not infer price, speed, or quality from names; keep the default when comparative evidence is missing.
- For bounded routine work with objective acceptance, prefer a known faster or lower-cost option that meets the task's needs. For ambiguous root-cause analysis, architecture, or high-risk review, prioritize demonstrated reasoning ability and required tools/context. Do not hardcode role/model pairs or always choose maximum effort.
- Before escalation, separate missing context, unclear scope, and environment/tool failures from a reasoning limitation. The main agent may choose a more capable available model when evidence supports it; executors report blockers rather than changing their own model.

## Give a narrow contract

- `Goal`: one bounded outcome in the current task.
- `Read`: the files or subtrees needed to establish it.
- `Write`: exact allowed files/directories, or `none`.
- `Acceptance`: an objective check or concrete evidence to return.

Add a working directory, task identifier, applicable baseline, return target, model override, or other directives only when needed. Asynchronous receipts must be distinguishable from results for earlier work.

Return concise findings, relevant artifact/symbol references, actual checks and their limits, and blockers. Include raw evidence when necessary to judge the conclusion. Report out-of-scope contract/ownership changes before making them; disclose unfinished writes when handing off.

## Bring results back into the task

- Continue useful independent work while an executor runs. Do not start consumers against unfinished inputs.
- Check each result against the current goal, applicable baseline, actual files, and acceptance evidence. An idle chat or a completion message alone is not acceptance.
- Resolve contradictions, stale assumptions, or missing integration, then act on the result in the main loop. Do not merely forward summaries or re-investigate already adequate evidence.
- If a required subtask fails or violates scope, stop dependent work and replan only the affected portion. Recover required work or explicitly report it as incomplete before claiming the whole task is done.

## Handle asynchronous uncertainty

- Use only supported receipt and resumption mechanisms. If a turn must end, retain the pending goal and next action; waiting is not completion.
- On a send failure or uncertain delivery, inspect available evidence before retrying. Do not blindly duplicate a task that may still be writing.
- Do not integrate a stale receipt into a changed goal or apply the same result twice. Recheck relevant artifacts and continue from accepted evidence.
- If replacing an executor, confirm that the old one stopped writing before allowing overlapping writes; otherwise restrict the replacement to read-only investigation.
- Do not add polling loops, scheduled wakeups, new chats, or permission changes to mask an unsupported continuation path. Report the specific limitation and required next step.
