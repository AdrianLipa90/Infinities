from __future__ import annotations

import json
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmf import Semiring
from infinities.bmcf import (
    PolynomialTerm,
    direct_multilinear_transform,
    direct_polynomial_transform,
    multilinear_transform,
    polynomial_transform,
)


@dataclass(frozen=True)
class SparsePoly:
    nvars: int
    terms: tuple[tuple[tuple[int, ...], int], ...]

    @staticmethod
    def from_dict(nvars: int, data: Mapping[tuple[int, ...], int]) -> "SparsePoly":
        clean = tuple(sorted((exp, coeff) for exp, coeff in data.items() if coeff != 0))
        if any(len(exp) != nvars for exp, _ in clean):
            raise ValueError("wrong exponent-vector length")
        return SparsePoly(nvars, clean)

    @staticmethod
    def zero(nvars: int) -> "SparsePoly":
        return SparsePoly(nvars, ())

    @staticmethod
    def one(nvars: int) -> "SparsePoly":
        return SparsePoly.from_dict(nvars, {(0,) * nvars: 1})

    @staticmethod
    def constant(nvars: int, value: int) -> "SparsePoly":
        return SparsePoly.from_dict(nvars, {(0,) * nvars: value})

    @staticmethod
    def variable(nvars: int, index: int) -> "SparsePoly":
        exp = [0] * nvars
        exp[index] = 1
        return SparsePoly.from_dict(nvars, {tuple(exp): 1})

    def as_dict(self) -> dict[tuple[int, ...], int]:
        return dict(self.terms)

    def __add__(self, other: "SparsePoly") -> "SparsePoly":
        if self.nvars != other.nvars:
            raise ValueError("incompatible polynomial dimensions")
        data = self.as_dict()
        for exp, coeff in other.terms:
            data[exp] = data.get(exp, 0) + coeff
        return SparsePoly.from_dict(self.nvars, data)

    def __mul__(self, other: "SparsePoly") -> "SparsePoly":
        if self.nvars != other.nvars:
            raise ValueError("incompatible polynomial dimensions")
        data: dict[tuple[int, ...], int] = {}
        for left_exp, left_coeff in self.terms:
            for right_exp, right_coeff in other.terms:
                exp = tuple(a + b for a, b in zip(left_exp, right_exp))
                data[exp] = data.get(exp, 0) + left_coeff * right_coeff
        return SparsePoly.from_dict(self.nvars, data)

    def degree(self) -> int:
        if not self.terms:
            return -1
        return max(sum(exp) for exp, _ in self.terms)

    def evaluate(self, point: tuple[int, ...]) -> int:
        if len(point) != self.nvars:
            raise ValueError("wrong evaluation point length")
        total = 0
        for exp, coeff in self.terms:
            term = coeff
            for value, power in zip(point, exp):
                term *= value ** power
            total += term
        return total

    def serial(self):
        return [{"exp": list(exp), "coeff": coeff} for exp, coeff in self.terms]


def polynomial_semiring(nvars: int) -> Semiring[SparsePoly]:
    return Semiring(
        add=lambda a, b: a + b,
        mul=lambda a, b: a * b,
        zero=SparsePoly.zero(nvars),
        one=SparsePoly.one(nvars),
    )


def exact_polynomial_fixture():
    nvars = 3
    semiring = polynomial_semiring(nvars)
    values = {f"x{i}": SparsePoly.variable(nvars, i) for i in range(nvars)}
    const = lambda c: SparsePoly.constant(nvars, c)
    outputs = ("p", "q")
    terms = {
        "p": (
            PolynomialTerm(const(3), ()),
            PolynomialTerm(const(2), ("x0",)),
            PolynomialTerm(const(5), ("x1", "x2")),
            PolynomialTerm(const(7), ("x0", "x0", "x2")),
        ),
        "q": (
            PolynomialTerm(const(-1), ()),
            PolynomialTerm(const(1), ("x2", "x2", "x2", "x2")),
            PolynomialTerm(const(4), ("x0", "x1", "x2")),
        ),
    }
    bmcf = polynomial_transform(values, outputs, terms, semiring)
    direct = direct_polynomial_transform(values, outputs, terms, semiring)
    points = ((0, 0, 0), (1, 2, 3), (-2, 1, 2), (3, -1, 1))
    point_checks = {
        str(point): {y: bmcf[y].evaluate(point) for y in outputs}
        for point in points
    }
    return bmcf, direct, point_checks


def deterministic_random_polynomial_trials(seed=20260916, trials=80):
    rng = random.Random(seed)
    nvars = 4
    semiring = polynomial_semiring(nvars)
    values = {i: SparsePoly.variable(nvars, i) for i in range(nvars)}
    const = lambda c: SparsePoly.constant(nvars, c)
    max_degree = 0
    for _ in range(trials):
        outputs = tuple(range(3))
        terms = {}
        for y in outputs:
            ys = []
            for _ in range(rng.randint(0, 12)):
                coeff = 0
                while coeff == 0:
                    coeff = rng.randint(-5, 5)
                degree = rng.randint(0, 6)
                factors = tuple(rng.randrange(nvars) for _ in range(degree))
                ys.append(PolynomialTerm(const(coeff), factors))
                max_degree = max(max_degree, degree)
            terms[y] = tuple(ys)
        left = polynomial_transform(values, outputs, terms, semiring)
        right = direct_polynomial_transform(values, outputs, terms, semiring)
        if left != right:
            return False, max_degree
    return True, max_degree


def strict_bmf_degree_separation():
    nvars = 3
    x = [SparsePoly.variable(nvars, i) for i in range(nvars)]
    coeffs = [SparsePoly.constant(nvars, c) for c in (-3, -1, 0, 2, 5)]
    max_linear_degree = -1
    for a in coeffs:
        for b in coeffs:
            for c in coeffs:
                value = a * x[0] + b * x[1] + c * x[2]
                max_linear_degree = max(max_linear_degree, value.degree())
    quadratic = x[0] * x[1]
    return max_linear_degree, quadratic.degree(), quadratic


def multilinear_exact_trials(seed=707, trials=50):
    rng = random.Random(seed)
    semiring = Semiring(add=lambda a, b: a + b, mul=lambda a, b: a * b, zero=0, one=1)
    from itertools import product
    for _ in range(trials):
        families = []
        for width in (2, 3, 2):
            families.append({i: rng.randint(-4, 4) for i in range(width)})
        outputs = (0, 1, 2)
        kernel = {}
        for y in outputs:
            for idx in product(*(tuple(family) for family in families)):
                kernel[(y, tuple(idx))] = rng.randint(-3, 3)
        left = multilinear_transform(families, outputs, kernel, semiring)
        right = direct_multilinear_transform(families, outputs, kernel, semiring)
        if left != right:
            return False
    return True


def mat_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def mat_mul(a, b):
    a00, a01, a10, a11 = a
    b00, b01, b10, b11 = b
    return (
        a00 * b00 + a01 * b10,
        a00 * b01 + a01 * b11,
        a10 * b00 + a11 * b10,
        a10 * b01 + a11 * b11,
    )


def noncommutative_word_witness():
    zero = (0, 0, 0, 0)
    one = (1, 0, 0, 1)
    semiring = Semiring(add=mat_add, mul=mat_mul, zero=zero, one=one)
    A = (1, 1, 0, 1)
    B = (1, 0, 1, 1)
    terms = {"word": (PolynomialTerm(one, ("A", "B")),)}
    got = polynomial_transform({"A": A, "B": B}, ("word",), terms, semiring)["word"]
    ab = mat_mul(A, B)
    ba = mat_mul(B, A)
    return got, ab, ba


def main():
    exact, direct, point_checks = exact_polynomial_fixture()
    random_ok, max_degree_seen = deterministic_random_polynomial_trials()
    linear_degree, quadratic_degree, quadratic = strict_bmf_degree_separation()
    multilinear_ok = multilinear_exact_trials()
    word, ab, ba = noncommutative_word_witness()

    tests = {
        "exact_sparse_polynomial_factorization": {
            "status": "PASS" if exact == direct else "FAIL",
            "degrees": {key: value.degree() for key, value in exact.items()},
            "symbolic": {key: value.serial() for key, value in exact.items()},
            "point_checks": point_checks,
        },
        "deterministic_random_polynomial_trials": {
            "status": "PASS" if random_ok else "FAIL",
            "trials": 80,
            "max_generated_monomial_degree": max_degree_seen,
        },
        "strict_bmf_degree_separation": {
            "status": "PASS" if linear_degree <= 1 and quadratic_degree == 2 else "FAIL",
            "max_degree_seen_for_fixed_scalar_linear_forms": linear_degree,
            "couple_quadratic_degree": quadratic_degree,
            "quadratic": quadratic.serial(),
        },
        "finite_multilinear_kernel_factorization": {
            "status": "PASS" if multilinear_ok else "FAIL",
            "trials": 50,
            "arity": 3,
        },
        "ordered_noncommutative_word": {
            "status": "PASS" if word == ab and ab != ba else "FAIL",
            "A_times_B": list(ab),
            "B_times_A": list(ba),
        },
    }
    overall = "PASS" if all(test["status"] == "PASS" for test in tests.values()) else "FAIL"
    result = {
        "schema": "INFINITIES_BMCF_POLYNOMIAL_RESULT_V0_7",
        "overall_status": overall,
        "tests": tests,
        "claims": {
            "finite_word_polynomial_bmcf_factorization": "EXACT_DEFINED_CLASS",
            "commutative_finite_polynomial_factorization": "EXACT_DEFINED_CLASS",
            "finite_multilinear_kernel_factorization": "EXACT_DEFINED_CLASS",
            "bmcf_strictly_extends_fixed_kernel_bmf_on_free_polynomial_witness": "YES",
            "couple_unique_minimal_fourth_operator": "NOT_CLAIMED",
            "bmcf_universal_computation_model": "NOT_CLAIMED",
            "fixpoint_reduced_to_couple": "NOT_CLAIMED",
            "quotient_reduced_to_couple": "NOT_CLAIMED",
            "novelty_relative_to_arithmetic_circuits": "NOT_ESTABLISHED",
            "rh_proof": "NO",
            "collatz_proof": "NO",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if overall != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
