"""Exact and numerical primitives for Infinities v0.1.

This module deliberately separates established mathematics from research bridges.
No function here claims to prove RH, Collatz, Twin Primes, or another open problem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Sequence


@dataclass(frozen=True)
class Compactified:
    q: float
    eta: float
    B: float


def compactify_positive(x: float) -> Compactified:
    """Map x>0 to q=x/(1+x), eta=(x-1)/(x+1), B=log(x)."""
    if not math.isfinite(x) or x <= 0:
        raise ValueError("x must be finite and positive")
    return Compactified(x / (1.0 + x), (x - 1.0) / (x + 1.0), math.log(x))


def invert_positive(x: float) -> float:
    if not math.isfinite(x) or x <= 0:
        raise ValueError("x must be finite and positive")
    return 1.0 / x


def complement_q(q: float) -> float:
    if not 0.0 <= q <= 1.0:
        raise ValueError("q must lie in [0,1]")
    return 1.0 - q


def shannon_entropy(probabilities: Sequence[float], *, base: float = math.e) -> float:
    if base <= 0 or base == 1:
        raise ValueError("invalid logarithm base")
    if not probabilities:
        raise ValueError("empty probability vector")
    if any(p < 0 for p in probabilities):
        raise ValueError("negative probability")
    total = sum(probabilities)
    if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("probabilities must sum to one")
    return -sum(p * (math.log(p) / math.log(base)) for p in probabilities if p > 0)


def cantor_dimension() -> float:
    return math.log(2.0) / math.log(3.0)


def cantor_dimension_from_shannon() -> float:
    return shannon_entropy((0.5, 0.5)) / math.log(3.0)


def telescoping_product(N: int) -> Fraction:
    """Return prod_{n=2}^N (1-1/n) exactly."""
    if N < 2:
        raise ValueError("N must be >= 2")
    out = Fraction(1, 1)
    for n in range(2, N + 1):
        out *= Fraction(n - 1, n)
    return out


def continued_fraction_sqrt2(iterations: int) -> Fraction:
    """Finite convergent of 1 + 1/(2 + 1/(2 + ...))."""
    if iterations < 1:
        raise ValueError("iterations must be >=1")
    tail = Fraction(0, 1)
    for _ in range(iterations):
        tail = Fraction(1, 2 + tail)
    return 1 + tail


def v_p(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("valuation of zero is infinite and intentionally not encoded")
    if p < 2:
        raise ValueError("p must be >=2")
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def p_adic_norm_fraction(x: Fraction | int, p: int) -> Fraction:
    x = Fraction(x)
    if x == 0:
        return Fraction(0, 1)
    exponent = v_p(x.numerator, p) - v_p(x.denominator, p)
    if exponent >= 0:
        return Fraction(1, p**exponent)
    return Fraction(p**(-exponent), 1)


def two_adic_geometric_partial(N: int) -> int:
    """S_N=1+2+...+2^N=2^(N+1)-1."""
    if N < 0:
        raise ValueError("N must be >=0")
    return 2 ** (N + 1) - 1


def accelerated_odd_collatz(n: int) -> tuple[int, int]:
    """Return (U(n), a) where U(n)=(3n+1)/2^a and a=v_2(3n+1)."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    m = 3 * n + 1
    a = v_p(m, 2)
    return m // (2**a), a


def collatz_q(n: int) -> Fraction:
    if n <= 0:
        raise ValueError("n must be positive")
    return Fraction(n, n + 1)


def collatz_B(n: int) -> Fraction:
    if n <= 0:
        raise ValueError("n must be positive")
    return Fraction(n - 1, n + 1)


def collatz_mobius_B(B: Fraction, a: int) -> Fraction:
    """Exact compactified branch T_a(B), c=2^(a-1)."""
    if a < 1:
        raise ValueError("a must be >=1")
    c = 2 ** (a - 1)
    return ((2 - c) + (1 + c) * B) / ((2 + c) + (1 - c) * B)


def gabriel_volume_converges(p: float) -> bool:
    return p > 0.5


def gabriel_area_converges(p: float) -> bool:
    return p > 1.0


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for k in range(2, int(n**0.5) + 1):
        if sieve[k]:
            sieve[k*k:n+1:k] = [False] * (((n - k*k)//k) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def zeta_dirichlet_partial(s: float, N: int) -> float:
    if s <= 1 or N < 1:
        raise ValueError("require s>1, N>=1")
    return sum(n ** (-s) for n in range(1, N + 1))


def euler_product_partial(s: float, prime_limit: int) -> float:
    if s <= 1:
        raise ValueError("require s>1")
    out = 1.0
    for p in primes_up_to(prime_limit):
        out *= 1.0 / (1.0 - p ** (-s))
    return out


def hilbert_shift_defect_rank(k: int = 1) -> int:
    """For unilateral shift U^k, rank(I-U^k U*^k)=k."""
    if k < 0:
        raise ValueError("k must be >=0")
    return k


def hilbert_shift_fredholm_index(k: int = 1) -> int:
    if k < 0:
        raise ValueError("k must be >=0")
    return -k
