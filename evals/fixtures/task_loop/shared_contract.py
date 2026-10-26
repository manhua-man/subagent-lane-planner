"""Reference contract for the task-loop evaluation fixture.

This is test material, not a payment implementation or a skill runtime.
"""


def normalize_amount(minor_units: int) -> dict[str, int | str]:
    """Return an integer minor-unit amount and its exact two-place display.

    Accept non-negative integers only. Booleans are not amounts.
    """
    if type(minor_units) is not int:
        raise TypeError("minor_units must be an integer, not a boolean")
    if minor_units < 0:
        raise ValueError("minor_units must be non-negative")
    return {
        "minor_units": minor_units,
        "display": f"{minor_units // 100}.{minor_units % 100:02d}",
    }
