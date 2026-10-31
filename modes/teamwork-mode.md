# Mode: /teamwork (Parallel Work with Owned Writes)

Use when the user requests `/teamwork` or parallel execution. Apply the shared mode rules in [SKILL.md](../SKILL.md#auxiliary-command-modes) and read [delegation](../references/delegation.md) before dispatching work.

## Choose useful parallel work

- Identify work that benefits from independent progress, context isolation, or verification. A large task or several files alone does not establish useful parallelism.
- If the task is tightly coupled or authorized delegation tools are unavailable, explain the constraint and continue directly where feasible. Do not invent a team or independent chats to satisfy the mode name.
- Use the delegation reference's bounded task contract and source/checkout identity. Stable reads may overlap; concurrent write scopes must be disjoint in the actual working files.

## Stabilize dependencies and assign ownership

- Give each concurrently edited file one owner. A shared contract, schema, configuration, or entry point may belong to the main agent or one explicitly assigned executor; all other executors report needed changes to that owner.
- Finalize required shared contracts before starting dependent implementation. The owner may edit a shared file whenever its dependents need an accepted version; shared files are not reserved for the final phase.
- For example, agree and verify an API type change first, then let two consumers update against that accepted type in parallel. Final routing or registration can follow when the consumers are ready.
- If a contract changes after dependent work starts, stop or redirect the affected work, accept the revised contract, and recheck its consumers. Confirm an old writer has stopped before transferring ownership.

## Integrate and verify

- Verify returned artifacts against the current goal and accepted inputs, then connect shared entry points as needed. The main agent remains responsible for the integrated result regardless of who owned individual files.
- Run relevant checks across the changed interfaces and affected modules. Expand verification when shared behavior or actual findings warrant it; parallel execution alone does not require unrelated full-repository checks.
- Claim completion only after required work is integrated and acceptance is satisfied. A finished lane, idle executor, or successful local check alone is insufficient.
