#!/usr/bin/env python3
"""Audit the TIR C3-untwisted Naimark-complement doubled rest-frame superalgebra.

This validator proves a restricted statement:
- the conjugate tetrahedral Naimark outcome carrier splits as rho + rho*chi^2;
- the exact TIR-style C3 character carrier supplies a unitary shift X with
  D(g) X D(g)^* = chi(g) X;
- the two orthogonal CAR doublets then generate an exact doubled/N=2-form
  supertranslation algebra at the equal-weight rest frame;
- after the C3 compensator, both doublets carry the same 2T spinor character.

It does NOT prove a full Lorentz-covariant 3+1D N=2 theory away from the
discrete 2T subgroup or away from the rest-frame/equal-weight sector.
"""
from __future__ import annotations

import math

from validate_tir_naimark_mckay_e6_v0_1 import (
    TOL,
    analysis_map,
    cinner,
    dagger,
    det4,
    eye,
    generate_2t,
    madd,
    matrix_key,
    mmul,
    mscale,
    msub,
    outcome_rep,
    rank,
    spinor_from_bloch,
    tetra_vectors,
    trace,
    vdot,
    zeros,
)
from validate_tir_sic_naimark_car_susy_v0_1 import (
    anticommutator,
    creation,
)


def conjugate_matrix(a):
    return [[z.conjugate() for z in row] for row in a]


def column(a, j):
    return [a[i][j] for i in range(len(a))]


def set_column(a, j, v):
    for i, z in enumerate(v):
        a[i][j] = z


def vsub(u, v):
    return [a - b for a, b in zip(u, v)]


def vscale(c, u):
    return [c * x for x in u]


def gram_schmidt_complement(a_iso):
    """Return a 4x2 isometry B orthogonal to 4x2 isometry A."""
    a_cols = [column(a_iso, j) for j in range(2)]
    b_cols = []
    for k in range(4):
        u = [0j] * 4
        u[k] = 1 + 0j
        for q in a_cols + b_cols:
            u = vsub(u, vscale(vdot(q, u), q))
        n2 = vdot(u, u).real
        if n2 > 1e-12:
            u = vscale(1.0 / math.sqrt(n2), u)
            b_cols.append(u)
        if len(b_cols) == 2:
            break
    assert len(b_cols) == 2
    b = zeros(4, 2)
    for j, v in enumerate(b_cols):
        set_column(b, j, v)
    return b


def linear_creation(coeffs, creators):
    out = zeros(16, 16)
    for a, z in enumerate(coeffs):
        out = madd(out, mscale(z, creators[a]))
    return out


def kron(a, b):
    ar, ac = len(a), len(a[0])
    br, bc = len(b), len(b[0])
    out = zeros(ar * br, ac * bc)
    for i in range(ar):
        for j in range(ac):
            for r in range(br):
                for c in range(bc):
                    out[i * br + r][j * bc + c] = a[i][j] * b[r][c]
    return out


def maxabs(a):
    return max(abs(z) for row in a for z in row)


def assert_close(a, b, tol=5e-8):
    err = maxabs(msub(a, b))
    assert err < tol, err


def diag3(a, b, c):
    out = zeros(3, 3)
    out[0][0] = a
    out[1][1] = b
    out[2][2] = c
    return out


def main():
    lambdas = [spinor_from_bloch(n) for n in tetra_vectors()]
    v = analysis_map(lambdas)

    # Conjugate one-particle carrier used by the CAR supercharge.
    a_iso = conjugate_matrix(v)
    assert_close(mmul(dagger(a_iso), a_iso), eye(2))
    b_iso = gram_schmidt_complement(a_iso)
    assert_close(mmul(dagger(b_iso), b_iso), eye(2))
    assert_close(mmul(dagger(a_iso), b_iso), zeros(2, 2))

    group, _ = generate_2t()
    records = []
    for g in group:
        r, pi, phases = outcome_rep(g, lambdas)
        rbar = conjugate_matrix(r)
        records.append((g, rbar))

    # chi=(det R)^2, while B in the conjugate carrier has character rho*chi^2.
    chi = []
    char_rho = []
    char_b = []
    for g, rbar in records:
        r = conjugate_matrix(rbar)
        x = det4(r) ** 2
        chi.append(x)
        char_rho.append(trace(g))
        ub = mmul(mmul(dagger(b_iso), rbar), b_iso)
        char_b.append(trace(ub))
    for cb, rr, x in zip(char_b, char_rho, chi):
        assert abs(cb - rr * x * x) < 5e-8

    # TIR C3 character carrier: D=diag(1,chi,chi^2).
    # X shifts character sectors and transforms with character chi.
    xshift = [
        [0j, 0j, 1 + 0j],
        [1 + 0j, 0j, 0j],
        [0j, 1 + 0j, 0j],
    ]
    assert_close(mmul(dagger(xshift), xshift), eye(3))
    for x in chi:
        d = diag3(1 + 0j, x, x * x)
        lhs = mmul(mmul(d, xshift), dagger(d))
        assert_close(lhs, mscale(x, xshift))

    # The compensated B character is rho: chi * (rho chi^2)=rho.
    compensated_b_char = [x * cb for x, cb in zip(chi, char_b)]
    for a, b in zip(compensated_b_char, char_rho):
        assert abs(a - b) < 5e-8

    # Build orthogonal CAR doublets.
    creators = [creation(a) for a in range(4)]
    a_create = [
        linear_creation(column(a_iso, alpha), creators)
        for alpha in range(2)
    ]
    b_create = [
        linear_creation(column(b_iso, alpha), creators)
        for alpha in range(2)
    ]

    i16 = eye(16)
    z16 = zeros(16, 16)
    for alpha in range(2):
        for beta in range(2):
            aa = anticommutator(dagger(a_create[alpha]), a_create[beta])
            bb = anticommutator(dagger(b_create[alpha]), b_create[beta])
            ab = anticommutator(dagger(a_create[alpha]), b_create[beta])
            target = i16 if alpha == beta else z16
            assert_close(aa, target)
            assert_close(bb, target)
            assert_close(ab, z16)

    # Equal-weight rest frame: P_{alpha dot beta}=4p delta.
    p = 1.0
    scale = 2.0 * math.sqrt(2.0 * p)
    i3 = eye(3)
    i48 = eye(48)
    z48 = zeros(48, 48)

    q = [[None for _ in range(2)] for _ in range(2)]
    for alpha in range(2):
        q[0][alpha] = mscale(scale, kron(i3, a_create[alpha]))
        q[1][alpha] = mscale(scale, kron(xshift, b_create[alpha]))

    # Exact N=2-form rest-frame algebra.
    for I in range(2):
        for J in range(2):
            for alpha in range(2):
                for beta in range(2):
                    mixed = anticommutator(q[I][alpha], dagger(q[J][beta]))
                    expected_scalar = (
                        8.0 * p
                        if I == J and alpha == beta
                        else 0.0
                    )
                    assert_close(mixed, mscale(expected_scalar, i48), 1e-7)

                    same = anticommutator(q[I][alpha], q[J][beta])
                    assert_close(same, z48, 1e-7)

    # Check normalization against 2 delta_IJ P with P=4p I2.
    assert abs(8.0 * p - 2.0 * (4.0 * p)) < TOL

    print("TIR_C3_UNTWISTED_NAIMARK_N2_REST_V0_1: PASS")
    print("ONE_PARTICLE = rho + rho*chi^2  [conjugate orientation]")
    print("C3_COMPENSATOR = unitary character shift X")
    print("ALGEBRA = {Q^I_alpha,Qbar^J_dotbeta}=2 delta_IJ P_alpha_dotbeta")
    print("DOMAIN = equal-weight rest frame, 2T covariance")
    print("FULL_LORENTZ_N2 = OPEN")


if __name__ == "__main__":
    main()
