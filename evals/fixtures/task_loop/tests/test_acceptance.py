"""Observable fixture behavior, not tests of prompt wording or agent reasoning."""

from pathlib import Path
import sys
import unittest

FIXTURE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FIXTURE_ROOT))

from consumer_a import preview_amount
from consumer_b import commit_amount
from shared_contract import normalize_amount


SAMPLES = (
    (0, "0.00"),
    (1, "0.01"),
    (99, "0.99"),
    (100, "1.00"),
    (105, "1.05"),
    (123456, "1234.56"),
    (100000000000000000005, "1000000000000000000.05"),
)


class SharedContractAcceptance(unittest.TestCase):
    def test_result_preserves_minor_units_and_exact_display(self):
        for minor_units, display in SAMPLES:
            with self.subTest(minor_units=minor_units):
                self.assertEqual(
                    normalize_amount(minor_units),
                    {"minor_units": minor_units, "display": display},
                )

    def test_negative_amount_is_rejected(self):
        for value in (-1, -100):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_amount(value)

    def test_booleans_are_not_amounts(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    normalize_amount(value)

    def test_non_integer_amount_is_rejected(self):
        for value in (1.5, "105", None):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    normalize_amount(value)


class ConsumerAcceptance(unittest.TestCase):
    def test_preview_uses_shared_display(self):
        for value, display in SAMPLES:
            with self.subTest(value=value):
                self.assertEqual(preview_amount(value), display)

    def test_commit_uses_shared_display(self):
        for value, display in SAMPLES:
            with self.subTest(value=value):
                self.assertEqual(commit_amount(value), display)

    def test_entry_points_agree(self):
        for value, _ in SAMPLES:
            with self.subTest(value=value):
                self.assertEqual(preview_amount(value), commit_amount(value))

    def test_both_entry_points_reject_negative_amounts(self):
        for consumer in (preview_amount, commit_amount):
            with self.subTest(consumer=consumer.__name__):
                with self.assertRaises(ValueError):
                    consumer(-1)

    def test_both_entry_points_reject_booleans(self):
        for consumer in (preview_amount, commit_amount):
            for value in (True, False):
                with self.subTest(consumer=consumer.__name__, value=value):
                    with self.assertRaises(TypeError):
                        consumer(value)

    def test_both_entry_points_reject_non_integer_amounts(self):
        for consumer in (preview_amount, commit_amount):
            for value in (1.5, "105", None):
                with self.subTest(consumer=consumer.__name__, value=value):
                    with self.assertRaises(TypeError):
                        consumer(value)


if __name__ == "__main__":
    unittest.main()
