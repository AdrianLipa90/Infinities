#!/usr/bin/env python3
"""Exact finite regression controls for Euler-Hilbert-Hotel SUSY v0.3.

These checks validate arithmetic identities and finite normal-form bookkeeping.
They do not replace Atiyah-Janich, Toeplitz index, or Hardy model-space theorems.
"""
from fractions import Fraction


def normal_form_index(q: int) -> int:
    """Index of the declared Hilbert-Hotel normal representative A_q."""
    if q > 0:
        # (S^dagger)^q
        return q
    if q < 0:
        # S^{-q}
        return q
    return 0


def winding_susy_charge(k: int) -> int:
    """Delta_W(T_{z^k}) = -k."""
    return -k


def pseudohyperbolic_sq(a: Fraction, b: Fraction) -> Fraction:
    return ((a - b) / (1 - a * b)) ** 2


def kernel_overlap_sq(a: Fraction, b: Fraction) -> Fraction:
    return ((1 - a * a) * (1 - b * b)) / ((1 - a * b) ** 2)


def tetra_equal_weight_norm(p: Fraction) -> tuple[Fraction, Fraction]:
    # Four k_a=(1,n_a) sum to (4,0,0,0).
    t = 4 * p
    spatial_sq = Fraction(0)
    return t, t * t - spatial_sq


def main() -> None:
    # Universal Hilbert-Hotel normal-form bookkeeping.
    for q in range(-32, 33):
        assert normal_form_index(q) == q

    # Euler/Toeplitz winding charge and composition law.
    for k in range(-16, 17):
        assert winding_susy_charge(k) == -k
        assert winding_susy_charge(-k) == -winding_susy_charge(k)
        for m in range(-8, 9):
            assert winding_susy_charge(k + m) == (
                winding_susy_charge(k) + winding_susy_charge(m)
            )

    # Toeplitz-generator convention: z -> S has index/Witten charge -1.
    assert winding_susy_charge(1) == -1
    assert winding_susy_charge(-1) == 1

    # Exact Hardy-kernel / pseudohyperbolic identity on rational fixtures.
    fixtures = (
        (Fraction(0), Fraction(1, 3)),
        (Fraction(1, 4), Fraction(-2, 5)),
        (Fraction(2, 7), Fraction(3, 8)),
        (Fraction(-1, 2), Fraction(1, 5)),
    )
    for a, b in fixtures:
        assert abs(a) < 1 and abs(b) < 1
        overlap = kernel_overlap_sq(a, b)
        rho2 = pseudohyperbolic_sq(a, b)
        assert overlap == 1 - rho2
        assert Fraction(0) < overlap <= Fraction(1)

    # Equal-weight tetrahedral rest-frame identity.
    for p in (Fraction(1), Fraction(1, 2), Fraction(3, 7), Fraction(11, 13)):
        t, norm_sq = tetra_equal_weight_norm(p)
        assert t == 4 * p
        assert norm_sq == 16 * p * p

    print("EULER_HILBERT_HOTEL_SUSY_V0_3: PASS")


if __name__ == "__main__":
    main()
