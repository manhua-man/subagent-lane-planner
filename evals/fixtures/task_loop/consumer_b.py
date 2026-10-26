"""Commit entry point for the evaluation fixture."""

from shared_contract import normalize_amount


def commit_amount(minor_units: int) -> str:
    """Display the amount according to the same contract as preview."""
    return normalize_amount(minor_units)["display"]
