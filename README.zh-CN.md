# subagent-lane-planner (v0.7.0)

[English](README.md) | [简体中文](README.zh-CN.md)

`subagent-lane-planner` 是一个轻量级的 **Agent Planning Harness Skill**，用于决策何时切分子 Agent lane、构建安全的文件作用域边界、安排依赖顺序、生成子 Agent 提示词，以及在 lane 失败时恢复。

> **曾用名：** `parallel-subagent-planner`，仓库 `codex-parallel-subagent-planner`（GitHub 会重定向到本仓库）。

---

## 核心功能

- **拆分决策**：评估 lane 是否真能节省时间，或是否需要先只读探索；否则主线程直接执行。
- **文件隔离**：lane 写范围互不重叠 (`write(A) ∩ write(B) = ∅`)。
- **执行顺序**：共享契约文件由唯一 owner 先完成，下游再只读消费。
- **干练提示词**：目标、读写边界、一条定向 Acceptance 命令。
- **规划产物**：可选 markdown 模板，spawn 前给用户审 scope。
- **主线程整合**：按改动范围验证，默认不全仓 CI。
- **Replan 触发**：越界、共享文件冲突、lane 失败时停依赖 lane，只重规划受影响部分。
- **长期 Agent**：重复角色可建议保存为宿主专用 agent 配置，须用户批准。

---

## 怎么触发

先安装（见 [安装方式](#安装方式)），再在**大范围或多 lane** 任务时使用，不要用于改单个文件。

### Cursor

1. 安装到 `~/.agents/skills/subagent-lane-planner/` 或 `<仓库>/.agents/skills/subagent-lane-planner/`。
2. 在目标仓库**新开对话**，说：*「用 subagent-lane-planner 规划这个任务的子 agent lane」*。
3. 规划产物确认后，用 `Task` 工具 spawn — 见 `references/cursor-task-prompt.md`（**同一条消息**里发多个 Task）。

### Codex

1. 安装到 `~/.agents/skills/subagent-lane-planner/` 或工作区 `.agents/skills/`。
2. 说：*「Decide whether subagent lanes help; plan only when scopes are clear and disjoint.」*（与 `agents/openai.yaml` 默认提示一致）。
3. 按 lane spawn 子 agent；重复角色写入 `.codex/agents/<name>.toml` 须先获用户同意。

### Claude Code

1. 按你的环境复制到 `~/.claude/skills/` 或项目 `.claude/skills/`。
2. 说：*「Read subagent-lane-planner and output a plan artifact before spawning subagents.」*
3. 用 Claude Code 的 Task/子 agent 机制，按规划里的 `Read`/`Write` 块执行。

---

## 核心循环

```text
Decide ➔ Split ➔ Isolate ➔ Order ➔ Prompt ➔ Integrate ➔ Replan（如需）
```

---

## 目录结构

```text
subagent-lane-planner/
├─ SKILL.md                          # 路由器（约 50 行）；细节在 references/
├─ agents/
│  └─ openai.yaml                    # Codex 元数据配置
├─ references/
│  ├─ lane-decomposition.md          # 切分、隔离、契约、Replan 触发
│  ├─ child-prompts.md               # 子 Agent 模板与宿主模型指引
│  ├─ cursor-task-prompt.md          # Cursor Task：subagent_type、模型、真并行
│  └─ plan-artifact-template.md      # spawn 前可选审阅的 markdown 模板
├─ README.md
├─ README.zh-CN.md
├─ CHANGELOG.md
└─ LICENSE
```

---

**用法：** 按需 skill。不要写入仓根 `AGENTS.md` 作为必跑门禁。

---

## 安装方式

### 个人安装

```bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/subagent-lane-planner.git \
  "$HOME/.agents/skills/subagent-lane-planner"
```

### 项目 Workspace 安装

```bash
mkdir -p "<target-repo>/.agents/skills"
git clone --depth 1 \
  https://github.com/manhua-man/subagent-lane-planner.git \
  "<target-repo>/.agents/skills/subagent-lane-planner"
```

---

## 开源协议

[MIT License](LICENSE) © 2026 manhua-man
