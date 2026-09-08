# Cursor Task Tool Guide

Use this reference when spawning parallel subagents in **Cursor** via the `Task` tool.

## 1. When To Use Task vs Main Thread

| Situation | Use |
|-----------|-----|
| Single file or unclear write scope | Main thread, or **one** `explore` subagent first |
| Disjoint read-only investigations | Parallel `Task` with `subagent_type: explore` |
| Disjoint implementation lanes | Parallel `Task` with `generalPurpose` (or domain subagents) |
| Payment, auth, migration, security | **One** sequential owner; optional named reviewer — no parallel implementers |

## 2. Choosing `subagent_type`

| Type | Use when |
|------|----------|
| `explore` | Fast codebase search, path mapping, read-only dependency tracing. Set thoroughness: `quick` / `medium` / `very thorough`. |
| `generalPurpose` | Bounded implementation or multi-step work inside an assigned `Write` scope. |
| Named reviewers (`payment-security-reviewer`, `nestjs-jest-pattern-reviewer`, `bugbot`, …) | User-named or high-risk diff review. Read-only or review-scoped — not parallel feature lanes. |

Default to `explore` for investigation; `generalPurpose` for code changes. Do not spawn a reviewer as a substitute for an implementer.

## 3. Model Selection

- **Default:** omit `model` or use `inherit` for most lanes.
- **Fast read-only lanes:** host fast model (e.g. when the session lists a fast slug) — only if the host exposes it in the supported-model list.
- **Large or high-risk lane:** stronger model only when the user offers a choice or the lane is clearly too heavy for default.
- **Never** copy model slugs from README, old chats, or other repos. Use only slugs from the current session's supported list.

## 4. True Parallelism In Cursor

Spawn independent lanes in **one assistant message** with multiple `Task` tool calls. Sequential messages that launch one subagent at a time are **not** parallel — they only add latency.

After subagents return, the main thread merges results, resolves conflicts, and runs integration checks (see `SKILL.md` §5).

## 5. Minimal Cursor Task Prompt

Paste the lane block from [plan-artifact-template.md](plan-artifact-template.md), or use:

```text
Role: [explorer | implementer]
Goal: [single narrow outcome]
Working Directory: [absolute repo path]
Read: [explicit paths]
Write: [exact paths or none]
Ignore: [node_modules/**, dist/**, .git/**, sibling lanes]
Acceptance: [one directed command, or "none" for read-only]

Directives:
- Stay inside Write scope.
- Return summary, test output, and handoff notes.
```

Map fields to `Task` parameters: `description` (short title), `prompt` (full block), `subagent_type`, optional `model`.
