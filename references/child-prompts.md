# Subagent Prompts & Custom Agent Guidance

Use this reference when generating child subagent prompts or recommending persistent custom agent specs.

## 1. Subagent Prompt Structure

When spawning a child subagent, provide a clear, self-contained prompt specifying goal, working directories, file boundaries, and verification:

```text
Role: [descriptive role label, e.g., explorer, implementer, reviewer, migrator, docs_writer]
Goal: [single narrow outcome]
Working Directory: [target repository path]
Read: [explicit files or subtrees to inspect]
Write: [exact files or subtrees allowed to edit, or "none"]
Ignore: [node_modules/**, dist/**, .git/**, sibling lane directories]
Acceptance: [one directed pass/fail command, e.g. pnpm test -- --testPathPattern=orders.service]

Directives:
- Work strictly within assigned Write scope.
- Do not edit outside Write scope.
- Run the Acceptance command (or an equivalent lane-local build/lint) before declaring completion.
- Return summary of changes, test results, and handoff notes.
```

Full-workspace CI is the main thread's job when risk warrants it — not the default Acceptance for every child lane.

---

## 2. Standard Directive Examples

### Read-Only Investigation (`explorer` / `reviewer`)
```text
- Do NOT modify any files.
- Inspect files inside Read Scope to gather evidence, trace dependencies, or audit diffs.
- Return structured findings, root cause analysis, or risk notes.
```

### Bounded Implementation (`implementer`)
```text
- Modify code strictly within the assigned Write scope.
- Do NOT perform unrelated refactoring outside Write scope.
- Run the Acceptance command for this lane (directed test, build, or lint) before completing.
```

### Schema & API Migration (`migrator`)
```text
- Maintain backward compatibility for existing API consumers unless breakage is explicitly approved.
- Write reversible migration steps and update dependent DTO types.
- Acceptance: directed tests for the migration module (e.g. --testPathPattern=migration-name), not full-repo CI by default.
```

---

## 3. Persistent Custom Agent Specs (`.toml`)

If a subagent role pattern proves repeatedly useful across multiple tasks (e.g., an API contract reviewer or database migration auditor):

- Recommend saving it as a persistent custom agent spec file:
  - Personal: `~/.codex/agents/<name>.toml`
  - Project: `.codex/agents/<name>.toml`
- **User Approval Rule**: Ask for user approval before writing any `.toml` file.

### Sample Custom Agent Template

```toml
name = "api_contract_reviewer"
description = "Maintains API backward compatibility and verifies route contract invariants."
# Omit model to use host default, or set only after checking the host's current supported list.
model = "<host-supported-model-id>"
sandbox_mode = "read-only"

developer_instructions = """
Review API schema modifications, report backward-incompatible changes, and verify route contracts.
Inspect target schema files and route definitions provided dynamically in the task context.
Do not modify contract specifications or workspace source code without explicit user approval.
"""
```

---

## 4. Host Model & Subagent Selection

**Do not maintain a frozen model catalog in this skill.** Model IDs and subagent types change per host and release. At plan time, use only what the **current host** exposes in context or documentation.

| Role | Selection guidance |
|------|-------------------|
| Read-only explorer / reviewer | Host's fast or read-only subagent when offered; otherwise default / `inherit` |
| Bounded implementer | Default / `inherit` unless the lane is large or high-risk |
| Payment, auth, migration, security | Single sequential owner; use host-named reviewer agents — do not parallelize implementation |

**Rules:**

- If the host injects a supported-model list, cite **only** slugs from that list. If a slug fails, omit `model` and use the host default.
- Do not copy model names from README, old plans, or other repos.
- Re-check when the user changes IDE, CLI, or model tier.

**Host mapping (mechanism only):**

| Host | Spawn mechanism | Persistent role |
|------|-----------------|-----------------|
| Codex | subagent / custom agent | `.codex/agents/<name>.toml` |
| Cursor | `Task` tool + `subagent_type`; optional `model` from host list | See [cursor-task-prompt.md](cursor-task-prompt.md) |
| Claude Code | Task / subagent per host docs | `.claude/agents/` per host docs |
