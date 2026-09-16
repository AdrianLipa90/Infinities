from __future__ import annotations

from fractions import Fraction
from typing import Sequence


def geometric_partial_sum(q: Fraction, n_terms: int) -> Fraction:
    """Exact finite partial sum sum_{k=0}^{n_terms-1} q^k."""
    if n_terms < 0:
        raise ValueError("n_terms must be nonnegative")
    total = Fraction(0, 1)
    power = Fraction(1, 1)
    for _ in range(n_terms):
        total += power
        power *= q
    return total


def geometric_tail_bound(q: Fraction, start: int) -> Fraction:
    """Exact absolute tail sum for 0 <= q < 1: sum_{k=start}^infty q^k."""
    if start < 0:
        raise ValueError("start must be nonnegative")
    if q < 0 or q >= 1:
        raise ValueError("q must satisfy 0 <= q < 1")
    return q ** start / (1 - q)


def finite_kernel_row_action(row: Sequence[Fraction], values: Sequence[Fraction]) -> Fraction:
    if len(row) != len(values):
        raise ValueError("row and values must have equal length")
    return sum((k * x for k, x in zip(row, values)), Fraction(0, 1))


def finite_kernel_row_l1_norm(row: Sequence[Fraction]) -> Fraction:
    return sum((abs(k) for k in row), Fraction(0, 1))


def linf_bound_certificate(row: Sequence[Fraction], values: Sequence[Fraction]) -> dict[str, Fraction | bool]:
    """Finite exact witness of |Kx| <= ||K_row||_1 ||x||_infty."""
    if len(row) != len(values):
        raise ValueError("row and values must have equal length")
    actual = abs(finite_kernel_row_action(row, values))
    f_inf = max((abs(x) for x in values), default=Fraction(0, 1))
    bound = finite_kernel_row_l1_norm(row) * f_inf
    return {"actual": actual, "bound": bound, "passes": actual <= bound}


def c00_geometric_tail_norm(after_n: int) -> Fraction:
    """For a_n=2^{-n} e_n (n>=1), exact l1-tail norm after the first N terms."""
    if after_n < 0:
        raise ValueError("after_n must be nonnegative")
    return Fraction(1, 2**after_n)


def harmonic_partial_sum(n: int) -> Fraction:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0, 1))


def alternating_harmonic_partial_sum(n: int) -> Fraction:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return sum((Fraction(1 if k % 2 else -1, k) for k in range(1, n + 1)), Fraction(0, 1))


def harmonic_dyadic_lower_bound(blocks: int) -> Fraction:
    """Exact lower bound H_{2^m} >= 1 + m/2 for m>=0."""
    if blocks < 0:
        raise ValueError("blocks must be nonnegative")
    return Fraction(1, 1) + Fraction(blocks, 2)


def square_summability_upper_bound_for_reciprocals() -> Fraction:
    """Standard integral-test bound sum_{n>=1} 1/n^2 <= 2."""
    return Fraction(2, 1)


__all__ = [
    "geometric_partial_sum",
    "geometric_tail_bound",
    "finite_kernel_row_action",
    "finite_kernel_row_l1_norm",
    "linf_bound_certificate",
    "c00_geometric_tail_norm",
    "harmonic_partial_sum",
    "alternating_harmonic_partial_sum",
    "harmonic_dyadic_lower_bound",
    "square_summability_upper_bound_for_reciprocals",
]
