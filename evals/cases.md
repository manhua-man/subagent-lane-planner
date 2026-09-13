# Behavioral Replay Cases

Run each prompt with and without the skill. Keep the starting repository state, prompt, available tools, other instructions, and root/subagent model and reasoning settings the same. Record the Codex version and actual model overrides. Both conditions should have access to native subagents so the comparison isolates this skill's contribution.

## Measurement

- Repeat each condition at least three times in fresh sessions from the same repository state. Alternate condition order and report the median and range alongside failed runs.
- Record task success, wall-clock time, subagent count, scope conflicts, and final verification. Judge success against the requested behavior and evidence, not an agent's completion claim. Do not treat fewer agents as a win unless the task still succeeds.
- For the root and each subagent, record model, non-cached input, cached input, and output tokens separately; record reasoning tokens separately when available and state whether they are included in output. Keep total tokens as a volume measure, not a cost estimate. Avoid summing cumulative usage snapshots or counting reasoning tokens twice. Mark unavailable fields as unknown.
- Account-wide quota changes are optional context, not per-task usage measurements; note concurrent sessions and reset boundaries if recording them.
- Test different model or reasoning configurations in a separate comparison. Do not attribute gains from a model change to the skill.
- Evaluate the model-selection cases below separately from the fixed-model delegation comparison: hold the available model catalog, capability/cost evidence, user constraints, and task fixture constant, then record the selection and its rationale. These cases check selection behavior; they do not establish model performance or savings.

Suggested per-run record:

| Case / run | Skill enabled | Version / model settings | Success / verification | Wall time | Subagents | Token breakdown by thread / model | Scope conflicts |
|---|---|---|---|---|---|---|---|

The cases below are replay prompts and expected behaviors, not measured results. Use a fixture with the named modules and an objective acceptance check before running a case.

## Cases

1. **Direct** — `Rename one README heading and change nothing else.` Expected: main thread only.
2. **Parallel reads** — `Audit authentication and billing independently; return evidence with file paths.` Expected: the minimum useful parallel read-only delegation.
3. **Disjoint writes** — `Update package-a and package-b independently and run each package's tests.` Expected: parallel work only when their write scopes are disjoint.
4. **Shared contract** — `Change the API schema, then update two consumers.` Expected: one contract owner; consumers wait for the accepted contract.
5. **Unclear boundary** — `Find where export behavior is owned, then fix it.` Expected: direct inspection or one read-only explorer before implementation, whichever has clear value.
6. **Dependent docs** — `Change CLI output and update docs to match it.` Expected: no concurrent task reads unfinished CLI text.
7. **Implementation** — `Use subagents if useful and complete the requested refactor.` Expected: implementation and integration, not a plan-only response.
8. **Delegation depth** — `Review three independent modules in parallel.` Expected: subagents do not delegate further.
9. **Evidence return** — `Investigate two independent failing test suites and return the cause and supporting evidence.` Fixture: each suite produces a long log with a small relevant failure. Expected: concise findings with file or symbol references and verification evidence; full logs are returned only when needed to assess the cause.
10. **Boundary escalation** — `Update package-a within its directory; the main thread owns the shared schema.` Fixture: the requested behavior requires a shared-schema change. Expected: the subagent reports the dependency before editing the schema; the main thread resolves ownership and order.
11. **Incomplete or conflicting results** — `Complete fixes in two independent packages and verify both.` Fixture: one subagent fails a required check, or the agents return conflicting findings about a stable shared input. Expected: the main thread resolves the failure or conflict and verifies the integrated result, or explicitly reports incomplete work; it does not claim success while required work remains unfinished.

## Model-selection cases

12. **Multiple available models** — `Delegate independent routine fixes and a high-risk review; choose suitable available models.` Fixture: at least three supported models with supplied task-relevant capability, speed, and cost evidence. Expected: choices follow task needs and evidence, use valid model/effort combinations, and are not limited to a hardcoded pair or role mapping.
13. **User choice or missing evidence** — `Use the configured model for all agents while fixing two independent packages.` Expected: no model override. Repeat without that user constraint and with no comparative model evidence: expected default inheritance without invented pricing or capability rankings.
14. **Failure classification** — `Recover the failed delegated task and finish verification.` Fixture variants: a missing test dependency, an incomplete task contract, or a demonstrated reasoning limitation with a suitable stronger model available. Expected: fix the environment or contract in the first two variants; consider a supported model escalation with a stated reason in the third, followed by verification.
15. **Unavailable requested model or effort** — `Use model-X for the independent subtask.` Fixture: model-X is unavailable and the runtime default is suitable and supported. Expected: use the supported fallback, continue without a confirmation request, and briefly disclose the requested model, actual model, and reason. Repeat with an unavailable reasoning level: preserve the requested model if it supports a suitable alternative level. With an explicit no-fallback instruction or no suitable alternative, report the blocker instead of substituting. A missing dependency or unrelated tool error must not be treated as evidence that a model is unavailable.
