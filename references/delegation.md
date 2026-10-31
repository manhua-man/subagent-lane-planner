# Delegation as an Execution Capability

Use external work to advance the main task. Choose direct execution, native agents, or independent chats according to their capabilities, useful context, and coordination cost.

## Organize the work

- Choose team size, roles, and delegation depth from the task and available tools. Adapt them as evidence changes, following user and host instructions.
- Coordinate competing writes through ownership, isolation, or sequencing. Agree the interface details that dependent work actually needs; independent work and investigation can proceed while other details evolve.
- Make provisional assumptions explicit and reconcile affected results when they change. Reassign ownership with a clear handoff.

## Describe the assignment

Use these fields when they clarify a handoff; the prompt can remain natural language:

- `Goal`: the outcome and its place in the main task.
- `Read`: useful starting evidence, not an investigation whitelist.
- `Write`: current implementation responsibility and any shared writers to coordinate with.
- `Acceptance`: behavior or evidence that establishes the result.

Include the project, checkout, or source version when needed to identify the work. Executors can adapt their approach and follow evidence beyond the starting files; coordinate changes that affect another writer or the user's requested deliverable.

## Choose tools and models

- Use actually available capabilities and preserve explicit user choices. Where a model or reasoning override is supported, choose it using task needs and available evidence; otherwise inherit configured defaults.
- If a requested choice is unavailable, use a suitable supported fallback and briefly disclose it, unless the user forbids substitution. Distinguish environment or missing-input failures from reasoning limitations when deciding what to change.
- Native agents and independent chats have different lifecycles. For Codex desktop chats, consult the [host guide](codex-chat-execution.md) and current tools; existing authorization remains valid, and this skill adds no separate approval gate.

## Integrate and continue

Keep useful work moving while results are pending. Return concise findings, artifacts, verification, and unresolved issues with enough source identity to assess them.

Compare results with the latest goal and current files, resolve material conflicts, and use them in the next action. When delivery or an executor's status is uncertain, establish what actually happened before resending work or replacing a writer. Retain pending work through the host's supported continuation mechanism and report any required unfinished result accurately.
