# Parallel Plan Artifact (Optional)

Use this template when the main thread finishes planning and the user should review scope **before** spawning subagents. Copy, fill in, and paste into chat or a scratch file. No JSON schema or state machine — plain markdown only.

```markdown
## Parallel plan

**Task:** [one-line user goal]

**Decision:** [direct | investigate first | parallel subagents] — [one brief reason]

**Order:** [sequential steps before parallel work, or "none"]

### Lane A — [short label]
- **Role:** [explorer | implementer | reviewer]
- **Goal:** [single narrow outcome]
- **Working Directory:** [path]
- **Read:** [paths or subtrees]
- **Write:** [exact paths, or `none`]
- **Ignore:** [noise + sibling lanes]
- **Acceptance:** [one directed command, or `none` for read-only]

### Lane B — [short label]
- **Role:** …
- **Goal:** …
- **Working Directory:** …
- **Read:** …
- **Write:** …
- **Ignore:** …
- **Acceptance:** …

*(add Lane C, D only when scopes are truly disjoint)*

**Integration (main thread):**
- Merge: [what to combine]
- Verify: [directed test/build/lint commands; expand only if payment/DB/migration/cross-module]
```

After the user approves the plan (or scope is obvious from the task), spawn subagents. If a lane fails or violates scope, see [lane-decomposition.md §4](lane-decomposition.md#4-replan-triggers) — replan only affected lanes.
