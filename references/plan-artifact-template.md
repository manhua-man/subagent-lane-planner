# Optional Subagent Plan

Use when the user requests a plan or a reviewable scope proposal. For an implementation request, proceed with useful delegation and integration within the authorized scope; do not stop solely to obtain approval for this template.

```markdown
**Decision:** [direct execution, investigate first, parallel subagents, or explicitly requested independent chats] — [reason]

**Order:** [dependencies that must finish first, or none]

**Subtask:** [short label; repeat only for useful independent work]
- Goal: [one narrow outcome]
- Read: [stable files or subtrees]
- Write: [exact files or directories, or none]
- Acceptance: [targeted command or concrete evidence to return]

**Integration:** [main-thread result review and checks proportionate to the change]
```

Add model overrides, roles, working directories, or ignore paths only when needed. Apply the [core policy](../SKILL.md) for model selection, ownership, failure handling, and completion.
