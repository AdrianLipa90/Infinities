#!/usr/bin/env python3
"""Finite fixtures for the SL(2,C)-covariant doubled supertranslation orbit.

This validates the algebraic orbit on the existing finite rest-frame operators.
It does not construct a unitary Lorentz representation on the finite carrier.
"""
from __future__ import annotations

import cmath
import math

from validate_tir_naimark_mckay_e6_v0_1 import (
    analysis_map,
    dagger,
    det2,
    eye,
    generate_2t,
    madd,
    mmul,
    mscale,
    msub,
    spinor_from_bloch,
    tetra_vectors,
    zeros,
)
from validate_tir_sic_naimark_car_susy_v0_1 import anticommutator, creation
from validate_tir_c3_untwisted_naimark_n2_rest_v0_1 import (
    conjugate_matrix,
    gram_schmidt_complement,
    column,
    linear_creation,
    kron,
)


def maxabs(a):
    return max(abs(z) for row in a for z in row)


def assert_close(a, b, tol=2e-7):
    err = maxabs(msub(a, b))
    assert err < tol, err


def mat2(a, b, c, d):
    return [[a, b], [c, d]]


def qmix(L, qpair):
    out = []
    for alpha in range(2):
        m = zeros(len(qpair[0]), len(qpair[0][0]))
        for beta in range(2):
            m = madd(m, mscale(L[alpha][beta], qpair[beta]))
        out.append(m)
    return out


def main():
    lambdas = [spinor_from_bloch(n) for n in tetra_vectors()]
    v = analysis_map(lambdas)

    a_iso = conjugate_matrix(v)
    b_iso = gram_schmidt_complement(a_iso)

    creators = [creation(a) for a in range(4)]
    a_create = [linear_creation(column(a_iso, alpha), creators) for alpha in range(2)]
    b_create = [linear_creation(column(b_iso, alpha), creators) for alpha in range(2)]

    xshift = [
        [0j, 0j, 1 + 0j],
        [1 + 0j, 0j, 0j],
        [0j, 1 + 0j, 0j],
    ]
    i3 = eye(3)

    p = 1.0
    mrest = 4.0 * p
    scale = 2.0 * math.sqrt(2.0 * p)

    q = [[None for _ in range(2)] for _ in range(2)]
    for alpha in range(2):
        q[0][alpha] = mscale(scale, kron(i3, a_create[alpha]))
        q[1][alpha] = mscale(scale, kron(xshift, b_create[alpha]))

    i48 = eye(48)
    z48 = zeros(48, 48)

    fixtures = [
        eye(2),
        mat2(math.exp(0.35), 0j, 0j, math.exp(-0.35)),
        mat2(cmath.exp(-0.31j), 0j, 0j, cmath.exp(0.31j)),
        mat2(1 + 0j, 0.4 + 0.2j, 0j, 1 + 0j),
    ]

    for L in fixtures:
        assert abs(det2(L) - 1) < 1e-10
        P = mscale(mrest, mmul(L, dagger(L)))
        assert abs(det2(P) - mrest * mrest) < 2e-7

        qL = [qmix(L, q[I]) for I in range(2)]

        for I in range(2):
            for J in range(2):
                for alpha in range(2):
                    for beta in range(2):
                        mixed = anticommutator(qL[I][alpha], dagger(qL[J][beta]))
                        expected = (
                            mscale(2.0 * P[alpha][beta], i48)
                            if I == J
                            else z48
                        )
                        assert_close(mixed, expected)

                        same = anticommutator(qL[I][alpha], qL[J][beta])
                        assert_close(same, z48)

    # A genuine boost is nonunitary on the spinor index, so the rest Parseval
    # frame operator I transforms to L L^dagger rather than remaining I.
    Lb = fixtures[1]
    frame_boosted = mmul(Lb, dagger(Lb))
    assert maxabs(msub(frame_boosted, eye(2))) > 1e-3

    print("TIR_C3_N2_LORENTZ_ORBIT_V0_1: PASS")
    print("ALGEBRAIC_SL2C_ORBIT = CLOSED")
    print("FIXED_MASS_SHELL_DET_P = m^2")
    print("FINITE_DIMENSIONAL_UNITARY_LORENTZ_IMPLEMENTATION = NO_GO_THEOREM")
    print("INFINITE_DIMENSIONAL_SUPER_POINCARE_REPRESENTATION = OPEN")


if __name__ == "__main__":
    main()
