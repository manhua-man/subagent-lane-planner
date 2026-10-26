# Task Loop Fixture

This is a small **correct reference workspace**, not a production component or a measured agent benchmark. Its tests should pass as checked in. Prepare a separate scratch copy with the fixed mutations in [replay cases](../../cases.md#task-loop-cases) before giving it to an evaluating agent; do not hand over a finished workspace and count its green tests as a successful repair.

## Amount contract

An amount is an integer number of minor units; 100 minor units equal one major unit. Both preview and commit return the same exact two-decimal string:

| Input | Display |
|---|---|
| 0 | 0.00 |
| 1 | 0.01 |
| 99 | 0.99 |
| 100 | 1.00 |
| 105 | 1.05 |
| 100000000000000000005 | 1000000000000000000.05 |

Reject negative integers with `ValueError`. Reject booleans, floats, strings, and `None` with `TypeError`. Keep the integer input in the shared result's `minor_units` field and the string in `display`. This reference is intentionally small enough to inspect on demand.

## Checks

From this directory, using Python 3.10 or later and no third-party dependencies:

~~~bash
python -m unittest discover -s tests -p 'test_acceptance.py' -v
~~~

Tests verify real contract/consumer outputs, invalid inputs, precision, and agreement between entry points. They do not verify skill choice, plan adaptation, message delivery, or permissions; those require trajectory and artifact evidence. This tiny fixture cannot establish latency or token savings.
