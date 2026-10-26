"""Preview entry point for the evaluation fixture."""

from shared_contract import normalize_amount


def preview_amount(minor_units: int) -> str:
    """Display the amount according to the shared contract."""
    return normalize_amount(minor_units)["display"]
