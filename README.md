# subagent-lane-planner (v0.7.0)

[English](README.md) | [简体中文](README.zh-CN.md)

`subagent-lane-planner` is a lightweight **Agent Planning Harness Skill**. It helps decide when to split work into subagent lanes, set safe file scope boundaries, establish execution order, generate clean subagent prompts, and recover from lane failures.

> **Former names:** `parallel-subagent-planner`, repo `codex-parallel-subagent-planner` (GitHub redirects to this repository).

---

## What It Does

- **Split Decision**: Evaluates whether lanes save wall-clock time vs. direct execution, or if a read-only investigation de-risks implementation.
- **File Boundary Isolation**: Enforces disjoint write scopes (`write(A) ∩ write(B) = ∅`) so lanes never overwrite each other's work.
- **Execution Order**: Assigns shared contract files to exactly one owner (main thread or subagent) before dependent consumers read them.
- **Clean Subagent Prompts**: Generates clear prompts specifying goals, read/write file scopes, and acceptance tests.
- **Plan Artifact**: Optional markdown template for user review before spawning subagents.
- **Main Thread Integration**: Merges subagent outputs and runs verification proportionate to the changed scope (not full-repo CI by default).
- **Replan Triggers**: Stop dependent lanes on scope violation, shared-file conflict, or lane failure — replan only affected scope.
- **Custom Agent Guidance**: Suggests saving recurring subagent roles into host-specific agent specs with explicit user approval.

---

## How To Trigger

Install first (see [Installation](#installation)), then invoke in chat when planning a **large or multi-lane** task — not for routine single-file edits.

### Cursor

1. Install to `~/.agents/skills/subagent-lane-planner/` or `<repo>/.agents/skills/subagent-lane-planner/`.
2. Start a **new chat** in the target workspace and say: *「用 subagent-lane-planner 规划这个任务的子 agent lane」*.
3. After the plan artifact looks right, spawn lanes with the `Task` tool — see `references/cursor-task-prompt.md` (multiple calls in **one message**).

### Codex

1. Install to `~/.agents/skills/subagent-lane-planner/` or clone into the workspace `.agents/skills/`.
2. Ask: *「Decide whether subagent lanes help; plan only when scopes are clear and disjoint.」* (matches `agents/openai.yaml` default prompt).
3. Spawn subagents or save a recurring role to `.codex/agents/<name>.toml` only after user approval.

### Claude Code

1. Copy the skill into `~/.claude/skills/` or the project `.claude/skills/` path per your setup.
2. Say: *「Read subagent-lane-planner and output a plan artifact before spawning subagents.」*
3. Use Claude Code's Task/subagent mechanism with the lane `Read`/`Write` blocks from the plan.

---

## Core Cycle

```text
Decide ➔ Split ➔ Isolate ➔ Order ➔ Prompt ➔ Integrate ➔ Replan (if needed)
```

---

## File Structure

```text
subagent-lane-planner/
├─ SKILL.md                          # Router (~50 lines); details in references/
├─ agents/
│  └─ openai.yaml                    # Codex metadata configuration
├─ references/
│  ├─ lane-decomposition.md          # Slicing, isolation, contracts, replan triggers
│  ├─ child-prompts.md               # Subagent prompt templates & host model guidance
│  ├─ cursor-task-prompt.md          # Cursor Task tool: subagent_type, model, parallelism
│  └─ plan-artifact-template.md      # Optional review-before-spawn markdown template
├─ README.md                         # English documentation
├─ README.zh-CN.md                   # Chinese documentation
├─ CHANGELOG.md                      # Release notes
└─ LICENSE                           # MIT License
```

---

**Usage:** on-demand skill when planning subagent lanes. Do not add to a repo root `AGENTS.md` as a mandatory gate.

---

## Installation

### Personal Skill Installation

```bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/subagent-lane-planner.git \
  "$HOME/.agents/skills/subagent-lane-planner"
```

### Project Workspace Installation

```bash
mkdir -p "<target-repo>/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/subagent-lane-planner.git \
  "<target-repo>/.agents/skills/subagent-lane-planner"
```

---

## License

[MIT License](LICENSE) © 2026 manhua-man
