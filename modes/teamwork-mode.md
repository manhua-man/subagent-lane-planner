# Mode: /teamwork (Adaptive Parallel Execution)

Use for `/teamwork` or parallel execution. Apply the [main task loop](../SKILL.md#auxiliary-command-modes) and [delegation guidance](../references/delegation.md).

- Choose the number, composition, and depth of executors from useful parallelism and coordination cost, using the host's available capabilities. Adjust the decomposition as the task develops; direct work remains an option.
- Coordinate writes with ownership, isolated checkouts, or sequencing so competing edits do not overwrite each other. The main agent or an assigned executor can own shared files, with ownership adjusted as needed.
- Manage dependencies locally rather than freezing the whole task. Research, contract proposals, experiments, and independent implementation can proceed together; work that relies on an unsettled interface can use an explicit provisional assumption and be reconciled as that interface settles.
- For example, explore an API change and inspect both consumers in parallel, agree the necessary interface details as they emerge, then update and verify the affected consumers. Other work need not wait for the entire contract to be finalized.
- Bring results into the current task, reconcile changed assumptions, and verify the integrated behavior. Completion is judged by the requested result, regardless of the team structure used.
