# Main-Agent Task Loop: Local Implementation Check

Date: 2026-10-26 (UTC+08:00). Baseline: commit `1f32c093c45f3ec4ed951471c9d207142de47b6c`.

This records local author validation, not a published release or a measured comparison of agent architectures. The candidate is the uncommitted working tree. No extra agent/chat was created, no installed skill or user configuration was changed, and no commit or push was made.

## Environment and baseline

- Fresh local checkout; initial worktree was clean.
- Windows PowerShell, Python 3.13.5, PyYAML 6.0.3 for the bundled skill validator. The fixture itself uses the Python standard library only.
- The original skill passed `skill-creator/scripts/quick_validate.py` before editing. This validates packaging, not baseline model behavior.
- Controlled old/new/no-skill model trajectories, latency, and token measurements were **not collected**. Model settings and per-thread usage for such a comparison remain unknown; this session is not a substitute.

## Executed checks

| Check | Observed result | Meaning |
|---|---|---|
| Bundled `quick_validate.py` on candidate | Passed | Required skill frontmatter/name and scaffold checks |
| UI YAML parsed with PyYAML | Passed; prompt retains `$subagent-lane-planner`, description length valid, invocation policy unchanged | Metadata agrees with the retained identifier |
| Reference fixture acceptance command | 10 test methods passed | Real contract/consumer behavior for fixed valid/invalid inputs and large integer precision |
| Known-bad starter in isolated scratch copy | Exit 1; 10 test methods ran with 30 failed subtests | The acceptance oracle rejects the documented consumer defects; 30 failures are not 30 independent agent cases |
| Repair only the two consumer expressions in scratch | Exit 0; all 10 test methods passed | The documented task can go from red to green without changing contract or tests |
| SHA-256 equality check after repair | README, contract, tests, and both consumers match the reference | No contract/test weakening or unrelated final content change in the scripted check |
| Local document links and fragments | 37 checked across 12 Markdown files | Relative references and requested heading targets resolve |
| Whitespace and working-tree inspection | `git diff --check` passed; tracked and new text files checked for trailing whitespace | No whitespace errors; changes remain local and unstaged |

Acceptance command, from the reference or scratch fixture root:

~~~bash
python -B -m unittest discover -s tests -p 'test_acceptance.py' -v
~~~

The negative control used exactly the starter in [cases](../cases.md#fixed-starter-for-e1-e3): preview returned `f"{minor_units / 100:.1f}"`; commit returned `f"{minor_units}.00"`. For input 105, preview produced `1.1` instead of `1.05`; the starter also failed input validation and agreement checks. Repairing the consumers to use the shared `display` restored all acceptance checks.

The author knew the mutation and solution. This is a **scripted red/green and scope-preservation check**, not an independent forward test, evidence of autonomous replanning, or a skill-vs-baseline win. Temporary scratch artifacts are not the sole evidence: the reproducible starter, commands, observed summaries, and checked-in tests are retained here and in the cases.

## Task-level evidence not yet established

| Scenario | Status |
|---|---|
| E1 direct completion / E2 selective knowledge use | Acceptance oracle and workspace prepared; independent agent trajectory not run |
| E3 evidence-driven plan change | Not independently exercised; no invented hypothesis or replan recorded |
| E4 actual external-result integration | Not run on native-child or independent-chat transport |
| E5 changed user goal | Protocol specified; live event/trajectory not run |
| E6 actual host continuation | Not run; checkpoint instructions do not certify automatic compaction/resumption |
| E7 uncertain delivery / writer replacement | Not run on a real host |
| E8 completion claims and authorization | Protocol specified; independent behavioral validation not run |

## Next evidence before release or performance claims

Run a bounded independent task with the same fixed starter, then representative authorized real tasks under old/new/no-skill conditions with identical tools, permissions, and model settings. Repeat each formal condition at least three times and report per-task failures, median/range, and actual usage. Obtain appropriate authorization before starting extra agents/chats or consequential external actions.

The local implementation is suitable for review and a first real-task trial. No claim is made that it is faster, cheaper, universally better, or verified for cross-chat continuation.
