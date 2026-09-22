"""Finite regression witnesses for Euler's Infinity v0.1.

This validates only exact local identities stated in
research/EULERS_INFINITY_V0_1.md. It does not certify infinite-address
convergence, a fractal dimension, or any classical open problem.
"""

from __future__ import annotations

import cmath
import math


def euler_phase(z: complex) -> complex:
    return cmath.exp(1j * math.pi * z)


def euler_phase_derivative(z: complex) -> complex:
    return 1j * math.pi * euler_phase(z)


def inverse_branch(w: complex, k: int) -> complex:
    if w == 0:
        raise ValueError("inverse branch is undefined at w=0")
    return 2 * k - (1j / math.pi) * cmath.log(w)


def close(a: complex, b: complex, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    x = -1 + 0j

    assert close(euler_phase(x), x)

    derivative = euler_phase_derivative(x)
    assert close(derivative, -1j * math.pi)
    assert abs(abs(derivative) - math.pi) <= 1e-12
    assert abs(derivative) > 1.0

    assert close((1j) ** 2, x)
    assert close((-1j) ** 2, x)

    # Principal Log(-1)=i*pi. Every integer inverse branch is then an odd
    # integer, and exp(i*pi*z) maps each of them back to -1.
    for k in range(-8, 9):
        z = inverse_branch(x, k)
        assert close(z, 2 * k + 1)
        assert close(euler_phase(z), x)

    # A nonzero generic point is recovered branchwise.
    for w in (0.25 + 0.75j, -0.4 + 0.3j, 2.0 - 0.5j):
        for k in (-2, -1, 0, 1, 2):
            assert close(euler_phase(inverse_branch(w, k)), w, 1e-11)

    print(
        {
            "schema": "INFINITIES_EULERS_INFINITY_V0_1",
            "fixed_point": "PASS",
            "repelling_derivative": "PASS",
            "square_root_double_cover": "PASS",
            "inverse_branch_roundtrip": "PASS",
            "infinite_address_convergence": "OPEN_NOT_TESTED",
            "fractal_dimension": "OPEN_NOT_TESTED",
            "open_problem_claim": False,
        }
    )


if __name__ == "__main__":
    main()
