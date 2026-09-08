# parallel-subagent-planner (v0.6.3)

[English](README.md) | [简体中文](README.zh-CN.md)

`parallel-subagent-planner` is a lightweight **Agent Planning Harness Skill** for Codex. It helps Codex decide when to split work into subagents, set safe file scope boundaries, establish execution order, generate clean subagent prompts, and recommend reusable custom agent roles.

---

## What It Does

- **Split Decision**: Evaluates whether splitting into subagents saves wall-clock time vs. direct execution, or if a read-only investigation de-risks implementation.
- **File Boundary Isolation**: Enforces disjoint write scopes (`write(A) ∩ write(B) = ∅`) so parallel subagents never overwrite each other's work.
- **Execution Order**: Assigns shared contract files to exactly one owner (main thread or subagent) before dependent consumers read them.
- **Clean Subagent Prompts**: Generates clear prompts specifying goals, read/write file scopes, and acceptance tests.
- **Main Thread Integration**: Merges subagent outputs and runs verification proportionate to the changed scope (not full-repo CI by default).
- **Custom Agent Guidance**: Suggests saving recurring subagent roles into `.codex/agents/<name>.toml` specs with explicit user approval when repeated evidence exists.

---

## Core Cycle

```text
Decide ➔ Split ➔ Isolate ➔ Order ➔ Prompt ➔ Integrate
```

---

## File Structure

```text
parallel-subagent-planner/
├─ SKILL.md                          # Router (~50 lines); details in references/
├─ agents/
│  └─ openai.yaml                    # Codex metadata configuration
├─ references/
│  ├─ lane-decomposition.md          # Slicing heuristics, scope isolation & execution order
│  └─ child-prompts.md               # Subagent prompt templates & custom agent guidance
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

Copy the repository contents into a target workspace:

```text
<target-repo>/.agents/skills/parallel-subagent-planner/
```

---

## License

[MIT License](LICENSE) © 2026 manhua-man
