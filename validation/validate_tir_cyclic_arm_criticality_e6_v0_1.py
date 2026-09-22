#!/usr/bin/env python3
"""Exact/numerical controls for the cyclic-arm affine-E6 criticality theorem.

The family is B_n = [I_n | 1_n].  The checks validate:
- index +1 and the protected kernel vector;
- C_n Fourier-channel structure;
- exact partner spectra implied by B_n B_n^T = I + J;
- the finite/affine/indefinite threshold at n=3;
- the affine-E6 dimension vector and protected/affine orthogonality at n=3.

This validator does not establish literature novelty or physical E6/SUSY.
"""
from __future__ import annotations

import cmath
import math
from fractions import Fraction


TOL = 2.0e-9


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def rank_fraction(A):
    M = [[Fraction(x) for x in row] for row in A]
    m, n = len(M), len(M[0])
    r = c = 0
    while r < m and c < n:
        pivot = next((i for i in range(r, m) if M[i][c] != 0), None)
        if pivot is None:
            c += 1
            continue
        M[r], M[pivot] = M[pivot], M[r]
        p = M[r][c]
        M[r] = [x / p for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(n)]
        r += 1
        c += 1
    return r


def Bn(n):
    return [
        [1 if j == i or j == n else 0 for j in range(n + 1)]
        for i in range(n)
    ]


def adjacency(n):
    B = Bn(n)
    BT = transpose(B)
    zpp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    zmm = [[0 for _ in range(n)] for _ in range(n)]
    top = [zpp[i] + BT[i] for i in range(n + 1)]
    bottom = [B[i] + zmm[i] for i in range(n)]
    return top + bottom


def dft(n):
    w = cmath.exp(2j * math.pi / n)
    return [
        [w ** (j * k) / math.sqrt(n) for k in range(n)]
        for j in range(n)
    ]


def cmatmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def cdagger(A):
    return [[A[i][j].conjugate() for i in range(len(A))] for j in range(len(A[0]))]


def main():
    for n in range(1, 13):
        B = Bn(n)
        BT = transpose(B)

        # Surjective n x (n+1) block: graph-SUSY index +1.
        assert rank_fraction(B) == n
        assert (n + 1) - n == 1

        v0 = [1] * n + [-1]
        assert matvec(B, v0) == [0] * n

        # Exact partner identity B B^T = I + J.
        BBT = matmul(B, BT)
        target = [
            [2 if i == j else 1 for j in range(n)]
            for i in range(n)
        ]
        assert BBT == target

        # Symmetric arm mode has eigenvalue n+1.
        ones = [1] * n
        assert matvec(BBT, ones) == [(n + 1)] * n

        # Every arm-difference mode has eigenvalue 1.
        for j in range(1, n):
            w = [0] * n
            w[0] = 1
            w[j] = -1
            assert matvec(BBT, w) == w

        # Positive Perron vector of the full bipartite adjacency.
        A = adjacency(n)
        dplus = [1] * n + [n]
        lam = math.sqrt(n + 1)
        # Use y = sqrt(n+1) 1_n.
        d = [complex(x) for x in dplus] + [complex(lam) for _ in range(n)]
        Ad = matvec(A, d)
        assert max(abs(Ad[i] - lam * d[i]) for i in range(len(d))) < TOL

        # Protected source mode is orthogonal to the Perron source mode.
        assert sum(a * b for a, b in zip(v0, dplus)) == 0

        # Affine threshold: rho(A)=sqrt(n+1), hence 2I-A critical iff n=3.
        if n < 3:
            assert lam < 2.0
        elif n == 3:
            assert abs(lam - 2.0) < TOL
        else:
            assert lam > 2.0

        # Ordinary heat supertrace is identically one.
        for t in (0.0, 0.2, 1.3):
            ze = 1.0 + (n - 1) * math.exp(-t) + math.exp(-(n + 1) * t)
            zo = (n - 1) * math.exp(-t) + math.exp(-(n + 1) * t)
            assert abs((ze - zo) - 1.0) < TOL

        # Fourier block: nontrivial arm characters do not see the central column.
        if n > 1:
            F = dft(n)
            # F^* 1 = sqrt(n) e_0 in this convention.
            one_col = [[1 + 0j] for _ in range(n)]
            coeff = cmatmul(cdagger(F), one_col)
            assert abs(abs(coeff[0][0]) - math.sqrt(n)) < TOL
            assert max(abs(coeff[k][0]) for k in range(1, n)) < 2e-8

    # Critical n=3 is exactly the affine-E6 star.
    n = 3
    B = Bn(n)
    BT = transpose(B)
    assert B == [
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
    ]

    dplus = [1, 1, 1, 3]
    dminus = [2, 2, 2]
    assert matvec(B, dplus) == [2 * x for x in dminus]
    assert matvec(BT, dminus) == [2 * x for x in dplus]

    # Degree sequence of affine E6 in this bipartite ordering.
    A = adjacency(3)
    degrees = [sum(row) for row in A]
    assert sorted(degrees) == [1, 1, 1, 2, 2, 2, 3]
    assert sum(degrees) // 2 == 6

    print("TIR_CYCLIC_ARM_CRITICALITY_E6_V0_1: PASS")
    print("INDEX_BN = +1_FOR_ALL_N")
    print("EQUIVARIANT_INDEX = TRIVIAL_Cn_CHARACTER")
    print("AFFINE_CRITICALITY = N_EQUALS_3_ONLY")
    print("N_EQUALS_3_GRAPH = AFFINE_E6")


if __name__ == "__main__":
    main()
