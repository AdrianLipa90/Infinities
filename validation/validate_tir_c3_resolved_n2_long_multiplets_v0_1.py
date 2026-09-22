#!/usr/bin/env python3
"""Validate the C3-resolved 48D carrier as three massive N=2 long multiplets.

The audit checks:
- the twisted Naimark one-particle representation extends to SU(2) x C3;
- the diagonal 2T embedding reproduces the current conjugate outcome action;
- the compensated supercharges commute with one conserved total C3 generator;
- the 48D carrier splits into three orthogonal rank-16 sectors;
- each sector has the 2T character chi^r * (5*1 + 4*rho + 3).

It does not prove physical realization or interacting QFT.
"""
from __future__ import annotations

import cmath
import math

from validate_tir_naimark_mckay_e6_v0_1 import (
    I2,
    SX,
    SY,
    SZ,
    analysis_map,
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
    spinor_from_bloch,
    tetra_vectors,
    trace,
    zeros,
)
from validate_tir_c3_untwisted_naimark_n2_rest_v0_1 import (
    column,
    conjugate_matrix,
    gram_schmidt_complement,
    kron,
    linear_creation,
)
from validate_tir_c3_e6_graph_dynamics_v0_1 import (
    creation_subset,
    exterior_rep4,
)

TOL = 8.0e-8


def maxabs(a):
    return max(abs(z) for row in a for z in row)


def assert_close(a, b, tol=TOL):
    err = maxabs(msub(a, b))
    assert err < tol, err


def inner_frob(a, b):
    return sum(
        a[i][j].conjugate() * b[i][j]
        for i in range(len(a))
        for j in range(len(a[0]))
    )


def normalize_intertwiner(s):
    ss = mmul(dagger(s), s)
    c = (ss[0][0] + ss[1][1]).real / 2.0
    assert c > 1e-12
    out = mscale(1.0 / math.sqrt(c), s)
    assert_close(mmul(dagger(out), out), I2, 2e-7)
    return out


def find_intertwiner(actual_reps, target_reps):
    seeds = [I2, SX, SY, SZ]
    for seed in seeds:
        s = zeros(2, 2)
        for u, t in zip(actual_reps, target_reps):
            # Reynolds average: s intertwines target -> actual.
            term = mmul(mmul(u, seed), dagger(t))
            s = madd(s, term)
        if inner_frob(s, s).real > 1e-10:
            s = normalize_intertwiner(s)
            for u, t in zip(actual_reps, target_reps):
                assert_close(mmul(u, s), mmul(s, t), 3e-7)
            return s
    raise AssertionError("no nonzero intertwiner found")


def diag3(a, b, c):
    out = zeros(3, 3)
    out[0][0] = a
    out[1][1] = b
    out[2][2] = c
    return out


def mpow(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = mmul(out, a)
    return out


def projector_c3(zop, r, omega):
    out = zeros(len(zop), len(zop))
    zk = eye(len(zop))
    for k in range(3):
        out = madd(out, mscale((omega ** (-r * k)) / 3.0, zk))
        zk = mmul(zk, zop)
    return out


def matrix_rank_from_projector(p):
    # For an orthogonal projector, rank = trace.
    tr = trace(p)
    assert abs(tr.imag) < 2e-7
    n = round(tr.real)
    assert abs(tr.real - n) < 2e-6
    return n


def main():
    lambdas = [spinor_from_bloch(n) for n in tetra_vectors()]
    v = analysis_map(lambdas)

    # CAR orientation: conjugate outcome carrier.
    a_iso0 = conjugate_matrix(v)
    b_iso0 = gram_schmidt_complement(a_iso0)

    group, _ = generate_2t()

    actual_a = []
    actual_b = []
    rbar_records = []
    chi = []

    for g in group:
        r, _, _ = outcome_rep(g, lambdas)
        rbar = conjugate_matrix(r)
        rbar_records.append(rbar)

        ua = mmul(mmul(dagger(a_iso0), rbar), a_iso0)
        ub = mmul(mmul(dagger(b_iso0), rbar), b_iso0)
        actual_a.append(ua)
        actual_b.append(ub)

        x = det4(r) ** 2
        chi.append(x)

    # Choose unitary intertwiners so A is rho and B is rho*chi^2 exactly.
    target_a = group
    target_b = [mscale(x * x, g) for g, x in zip(group, chi)]

    s_a = find_intertwiner(actual_a, target_a)
    s_b = find_intertwiner(actual_b, target_b)

    a_iso = mmul(a_iso0, s_a)
    b_iso = mmul(b_iso0, s_b)

    assert_close(mmul(dagger(a_iso), a_iso), I2)
    assert_close(mmul(dagger(b_iso), b_iso), I2)
    assert_close(mmul(dagger(a_iso), b_iso), zeros(2, 2))

    p_a = mmul(a_iso, dagger(a_iso))
    p_b = mmul(b_iso, dagger(b_iso))
    assert_close(madd(p_a, p_b), eye(4), 2e-7)

    # Verify diagonal 2T subset of SU(2) x C3 reproduces rbar.
    for g, x, rbar in zip(group, chi, rbar_records):
        u4 = madd(
            mmul(mmul(a_iso, g), dagger(a_iso)),
            mscale(x * x, mmul(mmul(b_iso, g), dagger(b_iso))),
        )
        assert_close(u4, rbar, 4e-7)

    omega = cmath.exp(2j * math.pi / 3.0)

    # Independent compact SU(2) x C3 one-particle extension.
    c3_one_particle = madd(p_a, mscale(omega * omega, p_b))
    assert_close(mpow(c3_one_particle, 3), eye(4), 3e-7)

    # External regular C3 carrier.
    zc = diag3(1 + 0j, omega, omega * omega)
    xshift = [
        [0j, 0j, 1 + 0j],
        [1 + 0j, 0j, 0j],
        [0j, 1 + 0j, 0j],
    ]
    assert_close(mmul(mmul(zc, xshift), dagger(zc)), mscale(omega, xshift), 2e-7)

    gamma_c3 = exterior_rep4(c3_one_particle)
    ztotal = kron(zc, gamma_c3)
    assert_close(mpow(ztotal, 3), eye(48), 5e-7)

    # Build the two compensated supercharge creation doublets.
    creators = [
        creation_subset([1 + 0j if i == a else 0j for i in range(4)])
        for a in range(4)
    ]
    a_create = [
        linear_creation(column(a_iso, alpha), creators)
        for alpha in range(2)
    ]
    b_create = [
        linear_creation(column(b_iso, alpha), creators)
        for alpha in range(2)
    ]

    q1 = [kron(eye(3), op) for op in a_create]
    q2 = [kron(xshift, op) for op in b_create]

    # Conserved total C3 charge.
    zdag = dagger(ztotal)
    for q in q1 + q2:
        assert_close(mmul(mmul(ztotal, q), zdag), q, 6e-7)

    # Three orthogonal rank-16 sectors.
    projectors = [projector_c3(ztotal, r, omega) for r in range(3)]
    for r, pr in enumerate(projectors):
        assert_close(mmul(pr, pr), pr, 8e-7)
        assert matrix_rank_from_projector(pr) == 16
        for q in q1 + q2:
            assert_close(mmul(pr, q), mmul(q, pr), 8e-7)
        for s, ps in enumerate(projectors):
            if r != s:
                assert_close(mmul(pr, ps), zeros(48, 48), 8e-7)
    assert_close(
        madd(madd(projectors[0], projectors[1]), projectors[2]),
        eye(48),
        8e-7,
    )

    # Combined diagonal 2T action on the 48D carrier.
    combined = []
    for g, x, rbar in zip(group, chi, rbar_records):
        d = diag3(1 + 0j, x, x * x)
        gamma = exterior_rep4(rbar)
        combined.append(kron(d, gamma))

    # Sector characters equal chi^r times the standard 16-state long-multiplet character.
    for r, pr in enumerate(projectors):
        for g, x, big in zip(group, chi, combined):
            t = trace(g)
            long_char = (2.0 + t) ** 2
            got = trace(mmul(pr, big))
            expected = (x ** r) * long_char
            assert abs(got - expected) < 2e-6, (r, got, expected)

    # Total character decomposition dimensions: 3 sectors x 16.
    assert sum(matrix_rank_from_projector(p) for p in projectors) == 48

    print("TIR_C3_RESOLVED_N2_LONG_MULTIPLETS_V0_1: PASS")
    print("ONE_PARTICLE_EXTENSION = SU2_x_C3")
    print("TOTAL_C3_SECTORS = 3 x 16")
    print("EACH_SECTOR_SU2_CONTENT = 5*1 + 4*2 + 3")
    print("DIAGONAL_2T_SECTOR_CHARACTER = chi^r * standard_long_N2")
    print("UNITARY_MASSIVE_WIGNER_INDUCTION = STANDARD_EXISTENCE_THEOREM")


if __name__ == "__main__":
    main()
