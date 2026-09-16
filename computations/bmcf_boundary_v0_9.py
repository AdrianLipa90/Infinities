from __future__ import annotations

import json
import random
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmcf_boundary import (
    absolute_value_polynomial_certificate,
    omega_c_for_polynomial_degree,
    omega_c_for_target,
    polynomial_compose,
    polynomial_degree,
    reciprocal_polynomial_certificate,
)


def random_nonconstant_polynomial(rng: random.Random, degree: int) -> tuple[int, ...]:
    if degree < 1:
        raise ValueError("degree must be positive")
    coefficients = [rng.randint(-5, 5) for _ in range(degree)]
    leading = 0
    while leading == 0:
        leading = rng.randint(-5, 5)
    return tuple([*coefficients, leading])


def composition_trials(seed: int = 20260916, trials: int = 250):
    rng = random.Random(seed)
    max_outer = 0
    max_inner = 0
    max_composed = 0
    for _ in range(trials):
        outer_degree = rng.randint(1, 8)
        inner_degree = rng.randint(1, 8)
        outer = random_nonconstant_polynomial(rng, outer_degree)
        inner = random_nonconstant_polynomial(rng, inner_degree)
        composed = polynomial_compose(outer, inner)
        actual = polynomial_degree(composed)
        expected = outer_degree * inner_degree
        if actual != expected:
            return False, {
                "outer_degree": outer_degree,
                "inner_degree": inner_degree,
                "actual": actual,
                "expected": expected,
            }
        max_outer = max(max_outer, outer_degree)
        max_inner = max(max_inner, inner_degree)
        max_composed = max(max_composed, actual)
    return True, {
        "trials": trials,
        "max_outer_degree": max_outer,
        "max_inner_degree": max_inner,
        "max_composed_degree": max_composed,
    }


def repeated_squaring_trials(max_depth: int = 12):
    rows = []
    ok = True
    for depth in range(max_depth + 1):
        degree = 2**depth
        omega = omega_c_for_polynomial_degree(degree)
        rows.append({"depth": depth, "degree": degree, "omega_C": omega})
        ok = ok and omega == depth
    return ok, rows


def reciprocal_certificates(max_degree: int = 24):
    failures = [
        degree
        for degree in range(max_degree + 1)
        if not reciprocal_polynomial_certificate(degree)
    ]
    return not failures, failures


def absolute_value_certificates(max_degree: int = 24):
    failures = [
        degree
        for degree in range(max_degree + 1)
        if not absolute_value_polynomial_certificate(degree)
    ]
    return not failures, failures


def typed_omega_guard():
    checks = {
        "linear_polynomial": omega_c_for_target("POLYNOMIAL", 1),
        "quadratic_polynomial": omega_c_for_target("POLYNOMIAL", 2),
        "degree_9_polynomial": omega_c_for_target("POLYNOMIAL", 9),
        "reciprocal": omega_c_for_target("RATIONAL_RECIPROCAL"),
        "absolute_value": omega_c_for_target("PIECEWISE"),
    }
    ok = checks == {
        "linear_polynomial": 0,
        "quadratic_polynomial": 1,
        "degree_9_polynomial": 4,
        "reciprocal": None,
        "absolute_value": None,
    }
    return ok, checks


def rational_exact_values():
    points = tuple(Fraction(value) for value in (-5, -2, -1, 1, 2, 5))
    reciprocal = {str(point): str(Fraction(1, 1) / point) for point in points}
    absolute = {str(point): str(abs(point)) for point in points}
    return reciprocal, absolute


def main():
    composition_ok, composition_meta = composition_trials()
    squaring_ok, squaring_rows = repeated_squaring_trials()
    reciprocal_ok, reciprocal_failures = reciprocal_certificates()
    abs_ok, abs_failures = absolute_value_certificates()
    guard_ok, guard = typed_omega_guard()
    reciprocal_values, abs_values = rational_exact_values()

    tests = {
        "univariate_polynomial_composition_degree": {
            "status": "PASS" if composition_ok else "FAIL",
            **composition_meta,
        },
        "repeated_squaring_exact_omega": {
            "status": "PASS" if squaring_ok else "FAIL",
            "rows": squaring_rows,
        },
        "reciprocal_outside_polynomial_degree_bounds": {
            "status": "PASS" if reciprocal_ok else "FAIL",
            "degree_bounds_checked": [0, 24],
            "failures": reciprocal_failures,
            "exact_sample_values": reciprocal_values,
        },
        "absolute_value_outside_polynomial_degree_bounds": {
            "status": "PASS" if abs_ok else "FAIL",
            "degree_bounds_checked": [0, 24],
            "failures": abs_failures,
            "exact_sample_values": abs_values,
        },
        "omega_C_typed_domain_guard": {
            "status": "PASS" if guard_ok else "FAIL",
            "values": guard,
        },
    }
    overall = "PASS" if all(test["status"] == "PASS" for test in tests.values()) else "FAIL"
    result = {
        "schema": "INFINITIES_BMCF_BOUNDARY_RESULT_V0_9",
        "overall_status": overall,
        "tests": tests,
        "claims": {
            "polynomial_composition_preserves_degree_grammar": "YES_UNIVARIATE_Q_WITNESS_AND_THEOREM",
            "repeated_squaring_depth_matches_omega_C": "YES",
            "reciprocal_has_numeric_omega_C": "NO_OUTSIDE_DOMAIN",
            "absolute_value_has_numeric_omega_C": "NO_OUTSIDE_DOMAIN",
            "omega_C_is_universal_nonlinearity_measure": "NO",
            "reciprocal_is_globally_minimal_new_primitive": "NOT_CLAIMED",
            "gate_is_globally_minimal_new_primitive": "NOT_CLAIMED",
            "single_universal_fourth_operator": "NOT_ESTABLISHED",
            "novelty_relative_to_circuit_complexity": "NOT_ESTABLISHED",
            "rh_proof": "NO",
            "collatz_proof": "NO",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if overall != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
