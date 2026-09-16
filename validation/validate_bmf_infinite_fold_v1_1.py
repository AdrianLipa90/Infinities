from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infinities"))

from bmf_infinite_fold import (
    alternating_harmonic_partial_sum,
    c00_geometric_tail_norm,
    geometric_partial_sum,
    geometric_tail_bound,
    harmonic_dyadic_lower_bound,
    harmonic_partial_sum,
    linf_bound_certificate,
    square_summability_upper_bound_for_reciprocals,
)


def main() -> None:
    q = Fraction(1, 2)
    for n in range(0, 33):
        assert geometric_partial_sum(q, n) + geometric_tail_bound(q, n) == 2

    row = [Fraction(1, 3), Fraction(-2, 5), Fraction(7, 4), Fraction(-1, 6)]
    values = [Fraction(3, 2), Fraction(-2, 1), Fraction(1, 7), Fraction(5, 3)]
    assert linf_bound_certificate(row, values)["passes"] is True

    for n in range(0, 33):
        assert c00_geometric_tail_norm(n) == Fraction(1, 2**n)
    assert c00_geometric_tail_norm(32) < Fraction(1, 10**9)

    for m in range(0, 11):
        assert harmonic_partial_sum(2**m) >= harmonic_dyadic_lower_bound(m)
    assert harmonic_dyadic_lower_bound(100) == 51

    assert square_summability_upper_bound_for_reciprocals() == 2
    assert harmonic_partial_sum(256) > harmonic_partial_sum(128)
    assert alternating_harmonic_partial_sum(64) != 0

    result_path = ROOT / "results" / "bmf_infinite_fold_v1_1_result.json"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    assert result["schema"] == "INFINITIES_BMF_INFINITE_FOLD_V1_1_RESULT"
    assert result["overall_status"] == "PASS"
    assert result["claims"]["absolute_banach_fold_extension"] == "PASS"
    assert result["claims"]["universal_infinite_fold"] == "NOT_CLAIMED"
    assert result["claims"]["novelty"] == "NOT_ESTABLISHED"
    assert result["firewall"]["finite_prefix_controls_are_not_infinite_proofs"] is True

    print("PASS BMF v1.1 absolute-fold controls")


if __name__ == "__main__":
    main()
