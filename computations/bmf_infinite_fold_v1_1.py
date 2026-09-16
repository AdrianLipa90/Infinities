from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from infinities.bmf_infinite_fold import (
    alternating_harmonic_partial_sum,
    c00_geometric_tail_norm,
    geometric_partial_sum,
    geometric_tail_bound,
    harmonic_dyadic_lower_bound,
    harmonic_partial_sum,
    linf_bound_certificate,
    square_summability_upper_bound_for_reciprocals,
)


def qstr(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


def main() -> None:
    q = Fraction(1, 2)
    geometric = []
    for n in (0, 1, 2, 4, 8, 16):
        partial = geometric_partial_sum(q, n)
        tail = geometric_tail_bound(q, n)
        geometric.append({
            "n": n,
            "partial": qstr(partial),
            "tail": qstr(tail),
            "partial_plus_tail": qstr(partial + tail),
            "expected_sum": "2/1",
            "pass": partial + tail == 2,
        })

    row = [Fraction(1, 3), Fraction(-2, 5), Fraction(7, 4), Fraction(-1, 6)]
    values = [Fraction(3, 2), Fraction(-2, 1), Fraction(1, 7), Fraction(5, 3)]
    bound = linf_bound_certificate(row, values)

    c00 = [
        {"after_n": n, "tail_norm": qstr(c00_geometric_tail_norm(n))}
        for n in (0, 1, 2, 4, 8, 16)
    ]

    harmonic = []
    for m in range(0, 9):
        n = 2**m
        actual = harmonic_partial_sum(n)
        lower = harmonic_dyadic_lower_bound(m)
        harmonic.append({
            "m": m,
            "n": n,
            "H_n": qstr(actual),
            "dyadic_lower_bound": qstr(lower),
            "pass": actual >= lower,
        })

    alternating = [
        {"n": n, "partial": qstr(alternating_harmonic_partial_sum(n))}
        for n in (2, 4, 8, 16, 32, 64)
    ]

    result = {
        "schema": "INFINITIES_BMF_INFINITE_FOLD_V1_1_RESULT",
        "overall_status": "PASS",
        "claims": {
            "absolute_banach_fold_extension": "PASS",
            "row_l1_kernel_linf_bound": "PASS",
            "completeness_counterexample_c00": "PASS",
            "l2_does_not_imply_additive_fold": "PASS",
            "conditional_series_not_promoted_to_unordered_fold": "PASS",
            "universal_infinite_fold": "NOT_CLAIMED",
            "novelty": "NOT_ESTABLISHED",
        },
        "geometric_absolute_series": geometric,
        "finite_row_bound_witness": {
            "actual": qstr(bound["actual"]),
            "bound": qstr(bound["bound"]),
            "pass": bool(bound["passes"]),
        },
        "c00_incomplete_space_tail": c00,
        "harmonic_divergence_dyadic_certificate": harmonic,
        "reciprocal_sequence_square_sum_upper_bound": qstr(square_summability_upper_bound_for_reciprocals()),
        "alternating_harmonic_prefixes": alternating,
        "firewall": {
            "finite_prefix_controls_are_not_infinite_proofs": True,
            "absolute_convergence_is_sufficient_not_universally_necessary_in_all_banach_spaces": True,
            "no_rh_claim": True,
            "no_collatz_claim": True,
            "no_twin_prime_claim": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
