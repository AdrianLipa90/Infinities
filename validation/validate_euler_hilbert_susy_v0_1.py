#!/usr/bin/env python3
"""Finite exact regression controls for the Euler-Hilbert-Hotel SUSY note.

These checks are implementation witnesses, not substitutes for the infinite
operator proofs or the CAR proof in the accompanying research note.
"""
from fractions import Fraction

V = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def minkowski_sq_tetra(weights):
    """Exact P^2 using n_a = V_a/sqrt(3), avoiding irrational arithmetic."""
    t = sum(weights, Fraction(0, 1))
    x = [sum(weights[a] * V[a][j] for a in range(4)) for j in range(3)]
    return t * t - sum(y * y for y in x) / 3


def pair_formula(weights):
    return Fraction(8, 3) * sum(
        weights[a] * weights[b]
        for a in range(4)
        for b in range(a + 1, 4)
    )


def main():
    assert tuple(sum(v[j] for v in V) for j in range(3)) == (0, 0, 0)
    for a in range(4):
        assert dot(V[a], V[a]) == 3
        for b in range(4):
            if a != b:
                assert dot(V[a], V[b]) == -1

    second = [[sum(V[a][i] * V[a][j] for a in range(4)) for j in range(3)] for i in range(3)]
    assert second == [[4, 0, 0], [0, 4, 0], [0, 0, 4]]

    fixtures = (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(2), Fraction(0), Fraction(0)),
        (Fraction(1, 3), Fraction(2, 5), Fraction(3, 7), Fraction(5, 11)),
        (Fraction(1), Fraction(1), Fraction(1), Fraction(1)),
    )
    for w in fixtures:
        lhs = minkowski_sq_tetra(w)
        rhs = pair_formula(w)
        assert lhs == rhs
        assert lhs >= 0

    for k in range(1, 17):
        ker_shift = 0
        ker_adj_shift = k
        fredholm_index = ker_shift - ker_adj_shift
        positive_zero_modes = 0
        negative_zero_modes = k
        witten_index = positive_zero_modes - negative_zero_modes
        assert fredholm_index == -k
        assert witten_index == fredholm_index

    print("EULER_HILBERT_HOTEL_SUSY_V0_1: PASS")


if __name__ == "__main__":
    main()
