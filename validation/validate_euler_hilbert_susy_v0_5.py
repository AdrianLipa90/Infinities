#!/usr/bin/env python3
"""Exact finite controls for Euler-Hilbert-Hotel SUSY v0.5.

This script validates the finite representation-ring and McKay-incidence
identities used in the v0.5 theorem package. It does not establish novelty.
"""
from collections import Counter
from fractions import Fraction


def add_rep(*terms):
    out = Counter()
    for term in terms:
        out.update(term)
    return out


def one(i):
    return ("1", i % 3)


def two(i):
    return ("2", i % 3)


THREE = ("3", 0)


def irrep_dim(x):
    if x[0] == "1":
        return 1
    if x[0] == "2":
        return 2
    if x[0] == "3":
        return 3
    raise ValueError(x)


def tensor_irrep(a, b):
    ta, ia = a
    tb, ib = b

    if ta == "1" and tb == "1":
        return Counter({one(ia + ib): 1})

    if ta == "1" and tb == "2":
        return Counter({two(ia + ib): 1})

    if ta == "2" and tb == "1":
        return Counter({two(ia + ib): 1})

    if (ta == "1" and tb == "3") or (ta == "3" and tb == "1"):
        return Counter({THREE: 1})

    if ta == "2" and tb == "2":
        return Counter({one(ia + ib): 1, THREE: 1})

    if (ta == "2" and tb == "3") or (ta == "3" and tb == "2"):
        return Counter({two(0): 1, two(1): 1, two(2): 1})

    if ta == "3" and tb == "3":
        return Counter({one(0): 1, one(1): 1, one(2): 1, THREE: 2})

    raise ValueError((a, b))


def tensor(A, B):
    out = Counter()
    for a, ma in A.items():
        for b, mb in B.items():
            for c, mc in tensor_irrep(a, b).items():
                out[c] += ma * mb * mc
    return out


def exterior_doublet(i):
    """Lambda^bullet(eta^i V) = 1 + eta^i V + eta^{-i}."""
    out = Counter()
    out[one(0)] += 1
    out[two(i)] += 1
    out[one(-i)] += 1
    return out


def fock_for_K(j):
    """K_j = V + eta^j V, hence K_j^* = V + eta^{-j} V."""
    return tensor(exterior_doublet(0), exterior_doublet(-j))


def rep_dimension(rep):
    return sum(irrep_dim(k) * m for k, m in rep.items())


def matmul(A, B):
    rows = len(A)
    cols = len(B[0])
    inner = len(B)
    return [
        [sum(A[i][k] * B[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def rank_fraction(A):
    M = [[Fraction(x) for x in row] for row in A]
    m = len(M)
    n = len(M[0])
    r = 0
    c = 0
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


def main():
    all_irreps = {one(0), one(1), one(2), two(0), two(1), two(2), THREE}

    # v0.5 twist-completeness theorem.
    F0 = fock_for_K(0)
    F1 = fock_for_K(1)
    F2 = fock_for_K(2)

    assert rep_dimension(F0) == 16
    assert rep_dimension(F1) == 16
    assert rep_dimension(F2) == 16

    assert set(F0) == {one(0), two(0), THREE}
    assert set(F1) == all_irreps
    assert set(F2) == all_irreps

    assert F0 == Counter({one(0): 5, two(0): 4, THREE: 1})

    expected_F1 = Counter(
        {
            one(0): 2,
            one(1): 2,
            one(2): 1,
            two(0): 1,
            two(1): 1,
            two(2): 2,
            THREE: 1,
        }
    )
    expected_F2 = Counter(
        {
            one(0): 2,
            one(1): 1,
            one(2): 2,
            two(0): 1,
            two(1): 2,
            two(2): 1,
            THREE: 1,
        }
    )
    assert F1 == expected_F1
    assert F2 == expected_F2

    # Minimal mode lower bound and exceptional thresholds.
    dims_E6 = (3, 2, 2, 2, 1, 1, 1)
    dims_E7 = (4, 3, 2, 1, 3, 2, 1, 2)
    dims_E8 = (6, 5, 4, 3, 2, 1, 4, 2, 3)
    assert sum(dims_E6) == 12
    assert sum(dims_E7) == 18
    assert sum(dims_E8) == 30
    assert 2**3 < 12 <= 2**4
    assert 2**4 < 18 <= 2**5
    assert 2**4 < 30 <= 2**5

    # Affine-E6 central-parity incidence matrix.
    B = [
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
    ]
    BT = transpose(B)

    assert rank_fraction(B) == 3

    zero_mode = [1, 1, 1, -1]
    assert matvec(B, zero_mode) == [0, 0, 0]

    # No cokernel: B has full row rank.
    assert rank_fraction(BT) == 3

    # Exact SUSY partner matrices.
    BBT = matmul(B, BT)
    BTB = matmul(BT, B)
    assert BBT == [
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2],
    ]

    # Exact eigenvector checks giving nonzero spectra {1,1,4}.
    assert matvec(BBT, [1, 1, 1]) == [4, 4, 4]
    assert matvec(BBT, [1, -1, 0]) == [1, -1, 0]
    assert matvec(BBT, [1, 0, -1]) == [1, 0, -1]

    # BTB has the same nonzero spectrum plus one protected zero mode.
    assert matvec(BTB, zero_mode) == [0, 0, 0, 0]

    # Affine E6 dimension-vector relation.
    d_plus = [1, 1, 1, 3]
    d_minus = [2, 2, 2]
    assert matvec(B, d_plus) == [2 * x for x in d_minus]
    assert matvec(BT, d_minus) == [2 * x for x in d_plus]

    # Full adjacency has eigenvalue 2 on the affine dimension vector.
    D = [
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
    ]
    d = d_plus + d_minus
    assert matvec(D, d) == [2 * x for x in d]

    print("EULER_HILBERT_HOTEL_SUSY_V0_5: PASS")


if __name__ == "__main__":
    main()
