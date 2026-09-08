# parallel-subagent-planner (v0.6.5)

[English](README.md) | [简体中文](README.zh-CN.md)

`parallel-subagent-planner` is a lightweight **Agent Planning Harness Skill**. It helps decide when to split work into subagents, set safe file scope boundaries, establish execution order, generate clean subagent prompts, and recover from lane failures.

---

## What It Does

- **Split Decision**: Evaluates whether splitting into subagents saves wall-clock time vs. direct execution, or if a read-only investigation de-risks implementation.
- **File Boundary Isolation**: Enforces disjoint write scopes (`write(A) ∩ write(B) = ∅`) so parallel subagents never overwrite each other's work.
- **Execution Order**: Assigns shared contract files to exactly one owner (main thread or subagent) before dependent consumers read them.
- **Clean Subagent Prompts**: Generates clear prompts specifying goals, read/write file scopes, and acceptance tests.
- **Plan Artifact**: Optional markdown template for user review before spawning subagents.
- **Main Thread Integration**: Merges subagent outputs and runs verification proportionate to the changed scope (not full-repo CI by default).
- **Replan Triggers**: Stop dependent lanes on scope violation, shared-file conflict, or lane failure — replan only affected scope.
- **Custom Agent Guidance**: Suggests saving recurring subagent roles into host-specific agent specs with explicit user approval.

---

## How To Trigger

Install first (see [Installation](#installation)), then invoke in chat when planning a **large or parallel** task — not for routine single-file edits.

### Cursor

1. Install to `~/.agents/skills/parallel-subagent-planner/` or `<repo>/.agents/skills/parallel-subagent-planner/`.
2. Start a **new chat** in the target workspace and say: *「用 parallel-subagent-planner 规划这个任务的并行子 agent」*.
3. After the plan artifact looks right, spawn lanes with the `Task` tool — see `references/cursor-task-prompt.md` (parallel calls in **one message**).

### Codex

1. Install to `~/.agents/skills/parallel-subagent-planner/` or clone into the workspace `.agents/skills/`.
2. Ask: *「Decide whether subagents help; plan lanes only when scopes are disjoint.」* (matches `agents/openai.yaml` default prompt).
3. Spawn subagents or save a recurring role to `.codex/agents/<name>.toml` only after user approval.

### Claude Code

1. Copy the skill into `~/.claude/skills/` or the project `.claude/skills/` path per your setup.
2. Say: *「Read parallel-subagent-planner and output a plan artifact before spawning subagents.」*
3. Use Claude Code's Task/subagent mechanism with the lane `Read`/`Write` blocks from the plan.

---

## Core Cycle

```text
Decide ➔ Split ➔ Isolate ➔ Order ➔ Prompt ➔ Integrate ➔ Replan (if needed)
```

---

## File Structure

```text
parallel-subagent-planner/
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

**Usage:** on-demand skill when planning parallel subagents. Do not add to a repo root `AGENTS.md` as a mandatory gate.

---

## Installation

### Personal Skill Installation

```bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/codex-parallel-subagent-planner.git \
  "$HOME/.agents/skills/parallel-subagent-planner"
```

### Project Workspace Installation

```bash
mkdir -p "<target-repo>/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/codex-parallel-subagent-planner.git \
  "<target-repo>/.agents/skills/parallel-subagent-planner"
```

---

## License

[MIT License](LICENSE) © 2026 manhua-man
