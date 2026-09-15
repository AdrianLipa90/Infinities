from __future__ import annotations

import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmcf_obstruction import (
    balanced_couple,
    couple_activation_required,
    degree_upper_bound_from_couple_depth,
    minimal_binary_product_depth_dp,
    minimal_couple_depth_for_degree,
)


def mat_mul(a, b):
    a00, a01, a10, a11 = a
    b00, b01, b10, b11 = b
    return (
        a00 * b00 + a01 * b10,
        a00 * b01 + a01 * b11,
        a10 * b00 + a11 * b10,
        a10 * b01 + a11 * b11,
    )


def left_product(values, mul, one):
    acc = one
    for value in values:
        acc = mul(acc, value)
    return acc


def main():
    depth_dp = {}
    for degree in range(0, 129):
        formula = minimal_couple_depth_for_degree(degree)
        dp = minimal_binary_product_depth_dp(degree)
        depth_dp[str(degree)] = {"formula": formula, "dp": dp}
    depth_dp_ok = all(v["formula"] == v["dp"] for v in depth_dp.values())

    activation = {str(d): couple_activation_required(d) for d in range(-1, 9)}
    activation_ok = all(activation[str(d)] == (d > 1) for d in range(-1, 9))

    bound_ok = all(
        degree_upper_bound_from_couple_depth(depth) == 2**depth
        for depth in range(0, 9)
    )

    monomial_ok = True
    monomial_depths = {}
    for degree in range(0, 65):
        got, depth = balanced_couple([2] * degree, lambda a, b: a * b, 1)
        monomial_depths[str(degree)] = depth
        if got != 2**degree or depth != minimal_couple_depth_for_degree(degree):
            monomial_ok = False

    A = (1, 1, 0, 1)
    B = (1, 0, 1, 1)
    C = (2, 1, 1, 1)
    D = (1, 2, 3, 4)
    E = (0, 1, 1, 0)
    one = (1, 0, 0, 1)
    word = [A, B, C, D, E]
    balanced, word_depth = balanced_couple(word, mat_mul, one)
    left = left_product(word, mat_mul, one)
    order_ok = balanced == left and word_depth == minimal_couple_depth_for_degree(len(word))

    rng = random.Random(20260916)
    random_depth_ok = True
    for _ in range(200):
        degree = rng.randint(0, 128)
        required = minimal_couple_depth_for_degree(degree)
        if degree >= 2 and degree <= degree_upper_bound_from_couple_depth(required - 1):
            random_depth_ok = False
        if degree > degree_upper_bound_from_couple_depth(required):
            random_depth_ok = False

    tests = {
        "conditional_activation_by_degree": {
            "status": "PASS" if activation_ok else "FAIL",
            "values": activation,
        },
        "minimal_depth_formula_vs_independent_dp_0_128": {
            "status": "PASS" if depth_dp_ok else "FAIL",
            "checked_degrees": 129,
        },
        "degree_upper_bound_2_pow_depth": {
            "status": "PASS" if bound_ok else "FAIL",
            "checked_depths": 9,
        },
        "balanced_monomial_construction_0_64": {
            "status": "PASS" if monomial_ok else "FAIL",
            "depths": monomial_depths,
        },
        "noncommutative_order_preserved_under_balancing": {
            "status": "PASS" if order_ok else "FAIL",
            "word_length": len(word),
            "depth": word_depth,
        },
        "random_degree_obstruction_trials": {
            "status": "PASS" if random_depth_ok else "FAIL",
            "trials": 200,
        },
    }
    overall = "PASS" if all(t["status"] == "PASS" for t in tests.values()) else "FAIL"
    result = {
        "schema": "INFINITIES_BMCF_COUPLE_OBSTRUCTION_RESULT_V0_8",
        "overall_status": overall,
        "tests": tests,
        "claims": {
            "strict_bmf_degree_le_one_in_polynomial_grammar": "EXACT_THEOREM",
            "couple_required_for_degree_gt_one": "EXACT_THEOREM_DEFINED_CLASS",
            "minimal_binary_couple_depth_for_degree_d": "CEIL_LOG2_D_EXACT_DEFINED_CLASS",
            "couple_unique_nonlinear_primitive": "NOT_CLAIMED",
            "bmcf_universal_computation_model": "NOT_CLAIMED",
            "novelty_relative_to_arithmetic_circuit_depth_results": "NOT_ESTABLISHED",
            "rh_proof": "NO",
            "collatz_proof": "NO",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if overall != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
