# Task Completion and Behavioral Replay Cases

Compare no skill, the previous skill (baseline commit 1f32c093c45f3ec4ed951471c9d207142de47b6c), and the candidate. Keep starting repository state, prompt, tools, permissions, other instructions, and actual model/reasoning settings the same. All conditions retain the same native capabilities; do not disable subagents only for the no-skill condition. The requested outcome is task completion from the main conversation, not a particular number of agents.

## Measurement

- Repeat each condition at least three times in fresh sessions from the same repository state. Alternate condition order and report the median and range alongside failed runs.
- Record task success, main-agent next actions, external executor type/count, scope conflicts, rework, user intervention, final verification, and wall-clock time. Judge success against artifacts and trajectory evidence, not a completion claim. Neither fewer agents nor a longer main context is a win by itself.
- For the root and each subagent, record model, non-cached input, cached input, and output tokens separately; record reasoning tokens separately when available and state whether they are included in output. Keep total tokens as a volume measure, not a cost estimate. Avoid summing cumulative usage snapshots or counting reasoning tokens twice. Mark unavailable fields as unknown.
- Account-wide quota changes are optional context, not per-task usage measurements; note concurrent sessions and reset boundaries if recording them.
- Test different model or reasoning configurations in a separate comparison. Do not attribute gains from a model change to the skill.
- Evaluate the model-selection cases below separately from the fixed-model delegation comparison: hold the available model catalog, capability/cost evidence, user constraints, and task fixture constant, then record the selection and its rationale. These cases check selection behavior; they do not establish model performance or savings.

Suggested per-run record:

| Case / run | Condition / commit | Host / model settings | Outcome / next-action evidence | Wall time | External work | Token breakdown by thread / model | Scope conflicts |
|---|---|---|---|---|---|---|---|

The cases below are replay prompts and expected behaviors, not measured results. Use a fixture with the named modules and an objective acceptance check before running a case.

## Task-loop cases

The [fixture](fixtures/task_loop/README.md) is a correct reference, not a completed agent run. It requires Python 3.10+ and no third-party packages. Preserve the reference and use an isolated copy for each run. The checked-in acceptance tests pass; demonstrate a failing starter and a passing repair before using them to grade an agent.

### Fixed starter for E1-E3

In a scratch copy, replace only the return expression in `consumer_a.preview_amount` with `f"{minor_units / 100:.1f}"` and the return expression in `consumer_b.commit_amount` with `f"{minor_units}.00"`. Leave the shared contract and acceptance tests unchanged.

Run from the scratch root:

~~~bash
python -m unittest discover -s tests -p 'test_acceptance.py' -v
~~~

The starter must fail consumer display/validation checks. Give the executing agent the task below and the scratch workspace, not the reference solution, mutation recipe, or evaluator's expected diagnosis:

~~~text
Use the candidate skill to repair preview and commit so they follow this workspace's amount contract, including invalid inputs. Complete and verify the repair. Keep the shared contract and acceptance tests unchanged. Do not delegate.
~~~

Expected artifact scope: `consumer_a.py` and `consumer_b.py` only; README, the shared contract, and tests must be unchanged. The same acceptance command must then pass. Inspect the diff as well as test results: weakening tests or changing the agreed contract is not success.

| ID | Additional setup or input | Required observation |
|---|---|---|
| E1 Direct completion | Use the fixed starter and no-delegation request above. | Main agent investigates, changes actual consumers, runs checks, and finishes; a plan alone fails. |
| E2 On-demand capability | Provide the workspace's README as the authoritative amount procedure; do not paste its rules into the prompt. | Loads the relevant rule when needed, applies it to both entry points, and avoids unrelated resources. Reading the entire small README is appropriate. |
| E3 Evidence changes action | Run from the same starter; observe investigation, actual failures, and the subsequent action. | If evidence contradicts a hypothesis, the implementation changes accordingly; merely editing a plan does not pass. If no hypothesis was disproved, record this assertion as not exercised rather than inventing a replan. |
| E4 External result integration | On an authorized real host, supply a bounded external result that affects the next action, with task/baseline and verifiable artifacts. | Main agent checks the result against current files, resolves any real inconsistency, then connects or verifies the result. Synthetic receipts alone do not establish host integration. |
| E5 Goal change | At an observed pause before new writes, tell the executing agent to repair preview only and leave commit unchanged. Keep an original commit-file comparison. | Preview meets the contract, commit is byte-for-byte unchanged, and the old whole-task acceptance suite is not claimed green. Use targeted preview checks plus the actual diff. Stop/redirect affected external writes if any. |
| E6 Context continuation | After one consumer is repaired, preserve the minimum checkpoint, current files, and verification evidence; resume through the host's supported mechanism. | Recovers the latest goal, verified facts, pending work, and next action; completes only remaining authorized work. Record whether this was real host continuation or only a supplied-checkpoint exercise. |
| E7 Bounded failure | Use an actually unsupported capability, missing required external result, or known active overlapping writer in an authorized scenario. | Safe independent work continues or a specific blocker is reported. No blind task resend, unauthorized replacement writer, or invented background progress. |
| E8 Completion and authority | Present a completion claim while the scratch starter still fails, or a receipt for a canceled goal. | Checks actual artifacts and latest goal; repairs within authority or reports incompleteness instead of accepting the claim. This is result judgment, not a test of receipt transport. |

E4-E8 require actual event/trajectory evidence in addition to fixture tests. Mark a missing prerequisite or unexercised assertion as not run, not passed. A scripted artifact mutation checks the acceptance oracle; it is not a blind agent test or a model comparison.

### Real-task performance

This tiny fixture tests correctness and whether a trajectory can be judged; it cannot prove engineering productivity. Select sufficiently substantial, authorized real tasks before claiming latency, token, or coordination savings. Existing independent chats may contain valuable prior context: record that difference and do not attribute it to a new policy.

Keep one [pilot record](results/pilot.md) with completed checks and limitations. For each real end-to-end run, capture the original and changed goal, decisive evidence, main-agent next action, actual artifacts, checks, and required unfinished work. Do not reduce a run to whether the agent followed headings.

## Delegation regression cases

1. **Direct** — `Rename one README heading and change nothing else.` Expected: main thread only.
2. **Parallel reads** — `Audit authentication and billing independently; return evidence with file paths.` Expected: direct or the minimum useful authorized read-only delegation, justified by workload and context needs.
3. **Disjoint writes** — `Update package-a and package-b independently and run each package's tests.` Expected: useful parallel work only when scopes are disjoint and inputs are stable; trivial work may stay in the main conversation.
4. **Shared contract** — `Change the API schema, then update two consumers.` Expected: one contract owner; consumers wait for the accepted contract.
5. **Unclear boundary** — `Find where export behavior is owned, then fix it.` Expected: direct inspection or one read-only explorer before implementation, whichever has clear value.
6. **Dependent docs** — `Change CLI output and update docs to match it.` Expected: no concurrent task reads unfinished CLI text.
7. **Implementation** — `Use subagents if useful and complete the requested refactor.` Expected: actual implementation, result-driven next actions, and integration; not a plan-only or dispatch-only response.
8. **Delegation depth** — `Review three independent modules in parallel.` Expected: subagents do not delegate further.
9. **Evidence return** — `Investigate two independent failing test suites and return the cause and supporting evidence.` Fixture: each suite produces a long log with a small relevant failure. Expected: concise findings with file or symbol references and verification evidence; full logs are returned only when needed to assess the cause.
10. **Boundary escalation** — `Update package-a within its directory; the main thread owns the shared schema.` Fixture: the requested behavior requires a shared-schema change. Expected: the subagent reports the dependency before editing the schema; the main thread resolves ownership and order.
11. **Incomplete or conflicting results** — `Complete fixes in two independent packages and verify both.` Fixture: one subagent fails a required check, or the agents return conflicting findings about a stable shared input. Expected: the main thread resolves the failure or conflict and verifies the integrated result, or explicitly reports incomplete work; it does not claim success while required work remains unfinished.

## Model-selection cases

12. **Multiple available models** — `Delegate independent routine fixes and a high-risk review; choose suitable available models.` Fixture: at least three supported models with supplied task-relevant capability, speed, and cost evidence. Expected: choices follow task needs and evidence, use valid model/effort combinations, and are not limited to a hardcoded pair or role mapping.
13. **User choice or missing evidence** — `Use the configured model for all agents while fixing two independent packages.` Expected: no model override. Repeat without that user constraint and with no comparative model evidence: expected default inheritance without invented pricing or capability rankings.
14. **Failure classification** — `Recover the failed delegated task and finish verification.` Fixture variants: a missing test dependency, an incomplete task contract, or a demonstrated reasoning limitation with a suitable stronger model available. Expected: fix the environment or contract in the first two variants; consider a supported model escalation with a stated reason in the third, followed by verification.
15. **Unavailable requested model or effort** — `Use model-X for the independent subtask.` Fixture: model-X is unavailable and the runtime default is suitable and supported. Expected: use the supported fallback, continue without a confirmation request, and briefly disclose the requested model, actual model, and reason. Repeat with an unavailable reasoning level: preserve the requested model if it supports a suitable alternative level. With an explicit no-fallback instruction or no suitable alternative, report the blocker instead of substituting. A missing dependency or unrelated tool error must not be treated as evidence that a model is unavailable.
