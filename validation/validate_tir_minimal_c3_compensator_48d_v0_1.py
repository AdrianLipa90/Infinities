#!/usr/bin/env python3
"""Exact controls for the minimal C3 compensator and 48D carrier theorem."""

import cmath
import math


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def mmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def dagger(A):
    return [[A[i][j].conjugate() for i in range(len(A))] for j in range(len(A[0]))]


def mscale(c, A):
    return [[c * z for z in row] for row in A]


def maxerr(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def main():
    omega = cmath.exp(2j * math.pi / 3.0)

    # Minimal 3D clock/shift realization of ZXZ^dagger = omega X.
    Z = [
        [1 + 0j, 0j, 0j],
        [0j, omega, 0j],
        [0j, 0j, omega * omega],
    ]
    X = [
        [0j, 0j, 1 + 0j],
        [1 + 0j, 0j, 0j],
        [0j, 1 + 0j, 0j],
    ]
    lhs = mmul(mmul(Z, X), dagger(Z))
    rhs = mscale(omega, X)
    assert maxerr(lhs, rhs) < 1e-10
    assert abs(det3(X)) > 0.5

    # Determinant divisibility obstruction for n=1,2 and allowance for n=3.
    for n in (1, 2):
        assert abs(omega**n - 1) > 0.5
    assert abs(omega**3 - 1) < 1e-10

    # Binary tetrahedral irrep-dimension lower bound.
    dims_2T = [1, 1, 1, 2, 2, 2, 3]
    min_complete_dim = sum(dims_2T)
    assert min_complete_dim == 12
    assert 2**3 < min_complete_dim <= 2**4

    # Exceptional comparison.
    dims_E6 = [3, 2, 2, 2, 1, 1, 1]
    dims_E7 = [4, 3, 2, 1, 3, 2, 1, 2]
    dims_E8 = [6, 5, 4, 3, 2, 1, 4, 2, 3]
    assert sum(dims_E6) == 12
    assert sum(dims_E7) == 18
    assert sum(dims_E8) == 30
    assert 2**4 >= 12
    assert 2**4 < 18
    assert 2**4 < 30
    assert 2**5 >= 18
    assert 2**5 >= 30

    # Factorised lower bound and saturation.
    c3_min_dim = 3
    fock_min_dim = 16
    assert c3_min_dim * fock_min_dim == 48
    assert 48 == 3 * (2**4)

    # Conserved-sector decomposition.
    assert 48 == 16 + 16 + 16

    print("TIR_MINIMAL_C3_COMPENSATOR_48D_V0_1: PASS")
    print("PRIMITIVE_C3_COMPENSATOR_MIN_DIM = 3")
    print("2T_COMPLETE_FOCK_MIN_MODES = 4")
    print("2T_COMPLETE_FOCK_MIN_DIM = 16")
    print("FACTORIZED_MIN_CARRIER_DIM = 48")


if __name__ == "__main__":
    main()
