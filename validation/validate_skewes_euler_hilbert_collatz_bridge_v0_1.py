"""Finite exact checks for the Skewes–Euler–Hilbert–Collatz bridge v0.1.

This validator checks only algebraic/local identities. It does not test
Littlewood's theorem, locate a Skewes crossing, prove RH, or prove Collatz.
"""

from __future__ import annotations

import cmath
import math


def affine(q: float, c: float, x: float) -> float:
    return q * x + (q - 1.0) * c


def accelerated_odd_collatz(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    x = 3 * n + 1
    a = 0
    while x % 2 == 0:
        x //= 2
        a += 1
    return x, a


def predecessor(m: int, a: int) -> int:
    num = (1 << a) * m - 1
    if num % 3:
        raise ValueError("inadmissible exponent")
    return num // 3


def odd_part_address(p: int) -> tuple[int, int]:
    x = p + 1
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return x, k


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    d = 3
    while d <= r:
        if n % d == 0:
            return False
        d += 2
    return True


def main() -> None:
    # General affine conjugacy: h_c(F(x)) = q h_c(x).
    for q, c in ((2.0, 1.0), (4.0, 1.0 / 3.0), (3.5, -0.2)):
        for x in (-7.0, -1.25, 0.0, 2.5, 19.0):
            lhs = affine(q, c, x) + c
            rhs = q * (x + c)
            assert math.isclose(lhs, rhs, rel_tol=0.0, abs_tol=1e-12)

    # On-Primes fibre law and exact log-step.
    for a in range(1, 30, 2):
        for k in range(0, 10):
            x = a * (1 << k) - 1
            tx = 2 * x + 1
            assert tx == a * (1 << (k + 1)) - 1
            assert math.isclose(
                math.log(tx + 1) - math.log(x + 1),
                math.log(2.0),
                rel_tol=0.0,
                abs_tol=1e-12,
            )

    # Complete local Collatz reverse-fibre law on a finite window.
    for m in range(1, 1000, 2):
        if m % 3 == 0:
            # No exponent can satisfy 2^a m == 1 mod 3.
            for a in range(1, 12):
                assert ((1 << a) * m - 1) % 3 != 0
            continue

        a0 = 2 if m % 3 == 1 else 1
        prev = None
        for j in range(0, 7):
            a = a0 + 2 * j
            n = predecessor(m, a)
            assert n > 0 and n % 2 == 1
            target, valuation = accelerated_odd_collatz(n)
            assert target == m
            assert valuation == a
            if prev is not None:
                assert n == 4 * prev + 1
                assert math.isclose(
                    math.log(n + 1.0 / 3.0) - math.log(prev + 1.0 / 3.0),
                    math.log(4.0),
                    rel_tol=0.0,
                    abs_tol=2e-12,
                )
            prev = n

    # Exact dyadic phase factorisation at prime samples.
    gammas = (0.125, 1.0, math.pi, 14.0, 37.25)
    for p in range(2, 5000):
        if not is_prime(p):
            continue
        a, k = odd_part_address(p)
        delta = math.log1p(1.0 / p)
        assert a * (1 << k) == p + 1
        assert math.isclose(
            math.log(p),
            math.log(a) + k * math.log(2.0) - delta,
            rel_tol=0.0,
            abs_tol=2e-14,
        )
        for gamma in gammas:
            lhs = cmath.exp(1j * gamma * math.log(p))
            rhs = (
                cmath.exp(1j * gamma * math.log(a))
                * cmath.exp(1j * k * gamma * math.log(2.0))
                * cmath.exp(-1j * gamma * delta)
            )
            assert abs(lhs - rhs) < 2e-11

    # Weyl phase relation on basis indices:
    # D_w S |k> = exp(i w) S D_w |k>.
    for omega in (0.0, 0.3, math.pi / 2.0, math.pi, 5.7):
        for k in range(0, 100):
            lhs = cmath.exp(1j * (k + 1) * omega)
            rhs = cmath.exp(1j * omega) * cmath.exp(1j * k * omega)
            assert abs(lhs - rhs) < 2e-12

    print(
        {
            "schema": "SKEWES_EULER_HILBERT_COLLATZ_BRIDGE_V0_1",
            "affine_conjugacy": "PASS",
            "dyadic_log_step": "PASS",
            "collatz_reverse_fibres": "PASS",
            "collatz_reverse_log_step": "PASS",
            "dyadic_phase_factorisation": "PASS",
            "weyl_phase_relation": "PASS",
            "littlewood_skewes_claim": "STANDARD_NOT_COMPUTATIONALLY_TESTED",
            "rh_claim": False,
            "collatz_global_claim": False,
        }
    )


if __name__ == "__main__":
    main()
