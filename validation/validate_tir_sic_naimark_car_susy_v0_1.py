#!/usr/bin/env python3
"""Finite controls for the TIR tetrahedral SIC -> Naimark -> CAR bridge.

The script validates the explicit qubit tetrahedral frame, its minimal rank-one
Naimark analysis isometry, the 24-element binary tetrahedral action, the
equivariant outcome representation, fermionic CAR on the four-outcome carrier,
the center -> fermion-parity identity, and equal-weight supercharge covariance.

It does not establish physical fermions or physical supersymmetry.
"""
from __future__ import annotations

import cmath
import math
from itertools import product

TOL = 2.0e-9


def zeros(n: int, m: int):
    return [[0j for _ in range(m)] for _ in range(n)]


def eye(n: int):
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = 1.0 + 0j
    return out


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mscale(c, a):
    return [[c * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    assert len(a[0]) == k
    out = zeros(n, m)
    for i in range(n):
        for j in range(m):
            out[i][j] = sum(a[i][r] * b[r][j] for r in range(k))
    return out


def dagger(a):
    return [[a[i][j].conjugate() for i in range(len(a))] for j in range(len(a[0]))]


def mmax(a):
    return max(abs(x) for row in a for x in row)


def mdiff(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def assert_close(a, b, tol=TOL):
    err = mmax(mdiff(a, b))
    assert err < tol, err


def vdot(u, v):
    return sum(x.conjugate() * y for x, y in zip(u, v))


def mvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def outer(u, v):
    return [[u[i] * v[j].conjugate() for j in range(len(v))] for i in range(len(u))]


def matrix_key(a):
    vals = []
    for row in a:
        for z in row:
            vals.extend((round(z.real, 10), round(z.imag, 10)))
    return tuple(vals)


I2 = eye(2)
SX = [[0j, 1 + 0j], [1 + 0j, 0j]]
SY = [[0j, -1j], [1j, 0j]]
SZ = [[1 + 0j, 0j], [0j, -1 + 0j]]


def pauli_combo(n):
    out = [row[:] for row in I2]
    for coeff, sigma in zip(n, (SX, SY, SZ)):
        out = madd(out, mscale(coeff, sigma))
    return out


def tetra_vectors():
    r = 1.0 / math.sqrt(3.0)
    return [
        (r, r, r),
        (r, -r, -r),
        (-r, r, -r),
        (-r, -r, r),
    ]


def spinor_from_bloch(n):
    nx, ny, nz = n
    a = math.sqrt((1.0 + nz) / 2.0)
    b = (nx + 1j * ny) / math.sqrt(2.0 * (1.0 + nz))
    lam = [a + 0j, b]
    assert abs(vdot(lam, lam) - 1.0) < TOL
    return lam


def build_v(lambdas):
    # phi_a = lambda_a/sqrt(2), V_{a,*}=<phi_a|.
    return [
        [z.conjugate() / math.sqrt(2.0) for z in lam]
        for lam in lambdas
    ]


def generate_2t():
    gx = mscale(1j, SX)
    gy = mscale(1j, SY)
    gz = mscale(1j, SZ)
    u3 = madd(
        mscale(-0.5, I2),
        mscale(-0.5j, madd(madd(SX, SY), SZ)),
    )
    gens = [gx, gy, gz, u3]
    group = {matrix_key(I2): I2}
    changed = True
    while changed:
        changed = False
        current = list(group.values())
        for a in current:
            for g in gens:
                for b in (mmul(a, g), mmul(g, a)):
                    k = matrix_key(b)
                    if k not in group:
                        group[k] = b
                        changed = True
    assert len(group) == 24
    return list(group.values())


def match_spin_action(g, lambdas):
    permutation = []
    phases = []
    for lam in lambdas:
        glam = mvec(g, lam)
        overlaps = [vdot(target, glam) for target in lambdas]
        b = max(range(4), key=lambda j: abs(overlaps[j]))
        ov = overlaps[b]
        assert abs(abs(ov) - 1.0) < 1.0e-8
        permutation.append(b)
        phases.append(cmath.phase(ov))
    assert sorted(permutation) == [0, 1, 2, 3]
    return permutation, phases


def outcome_rep(g, lambdas):
    permutation, phases = match_spin_action(g, lambdas)
    r = zeros(4, 4)
    for a, (b, chi) in enumerate(zip(permutation, phases)):
        r[b][a] = cmath.exp(1j * chi)
    return r, permutation, phases


def conjugate_matrix(a):
    return [[z.conjugate() for z in row] for row in a]


def creation(mode: int):
    dim = 16
    c = zeros(dim, dim)
    bit = 1 << mode
    lower = bit - 1
    for mask in range(dim):
        if mask & bit:
            continue
        sign = -1.0 if ((mask & lower).bit_count() % 2) else 1.0
        c[mask | bit][mask] = sign
    return c


def fock_monomial(permutation, phases):
    """Second quantization of e_a -> phases[a] e_{pi(a)}."""
    dim = 16
    g = zeros(dim, dim)
    for mask in range(dim):
        occupied = [a for a in range(4) if mask & (1 << a)]
        mapped = [permutation[a] for a in occupied]
        phase = 1.0 + 0j
        for a in occupied:
            phase *= phases[a]

        # Sign needed to sort mapped wedge factors.
        inv = 0
        for i in range(len(mapped)):
            for j in range(i + 1, len(mapped)):
                if mapped[i] > mapped[j]:
                    inv += 1
        if inv % 2:
            phase *= -1.0

        out_mask = 0
        for b in mapped:
            out_mask |= 1 << b
        g[out_mask][mask] = phase
    return g


def anticommutator(a, b):
    return madd(mmul(a, b), mmul(b, a))


def main():
    ns = tetra_vectors()
    lambdas = [spinor_from_bloch(n) for n in ns]

    # SIC projectors/effects and null-ray normalization.
    sum_p = zeros(2, 2)
    for n, lam in zip(ns, lambdas):
        p = outer(lam, lam)
        e = mscale(0.5, p)
        k = pauli_combo(n)
        assert_close(k, mscale(4.0, e))
        # det(I+n.sigma)=0.
        det_k = k[0][0] * k[1][1] - k[0][1] * k[1][0]
        assert abs(det_k) < TOL
        sum_p = madd(sum_p, p)
    assert_close(sum_p, mscale(2.0, I2))

    # Naimark isometry and minimality.
    v = build_v(lambdas)
    assert_close(mmul(dagger(v), v), I2)
    for a, lam in enumerate(lambdas):
        phi = [z / math.sqrt(2.0) for z in lam]
        image = mvec(v, phi)
        # Pi_a V phi_a = ||phi_a||^2 e_a = (1/2)e_a.
        assert abs(image[a] - 0.5) < TOL

    # Binary tetrahedral group and equivariant Naimark representation.
    group = generate_2t()
    reps = {}
    group_by_key = {matrix_key(g): g for g in group}
    for g in group:
        r, pi, chi = outcome_rep(g, lambdas)
        reps[matrix_key(g)] = (r, pi, chi)
        assert_close(mmul(v, g), mmul(r, v))

    for g, h in product(group, repeat=2):
        r_g = reps[matrix_key(g)][0]
        r_h = reps[matrix_key(h)][0]
        gh = mmul(g, h)
        r_gh = reps[matrix_key(gh)][0]
        assert_close(mmul(r_g, r_h), r_gh, 1.0e-8)

    # Identify the central -I and verify its outcome action.
    minus_i2 = mscale(-1.0, I2)
    assert matrix_key(minus_i2) in group_by_key
    r_z, pi_z, chi_z = reps[matrix_key(minus_i2)]
    assert pi_z == [0, 1, 2, 3]
    assert_close(r_z, mscale(-1.0, eye(4)))

    # CAR algebra on Lambda^* C^4.
    creators = [creation(a) for a in range(4)]
    annihilators = [dagger(c) for c in creators]
    i16 = eye(16)
    z16 = zeros(16, 16)
    for a in range(4):
        for b in range(4):
            target = i16 if a == b else z16
            assert_close(anticommutator(annihilators[a], creators[b]), target)
            assert_close(anticommutator(creators[a], creators[b]), z16)
            assert_close(anticommutator(annihilators[a], annihilators[b]), z16)

    # Fermion parity.
    parity = zeros(16, 16)
    for mask in range(16):
        parity[mask][mask] = -1.0 if (mask.bit_count() % 2) else 1.0
    for c in creators:
        assert_close(madd(mmul(parity, c), mmul(c, parity)), z16)

    # Conjugate outcome representation and second quantization.
    fock_reps = {}
    for g in group:
        _, pi, chi = reps[matrix_key(g)]
        conj_phases = [cmath.exp(-1j * x) for x in chi]
        gamma = fock_monomial(pi, conj_phases)
        fock_reps[matrix_key(g)] = gamma
        # Check creator covariance.
        gamma_d = dagger(gamma)
        for a in range(4):
            lhs = mmul(mmul(gamma, creators[a]), gamma_d)
            rhs = mscale(conj_phases[a], creators[pi[a]])
            assert_close(lhs, rhs, 1.0e-8)

    # Center -> fermion parity.
    assert_close(fock_reps[matrix_key(minus_i2)], parity)

    # Equal-weight supercharge closure and 2T covariance.
    p = 1.0
    q = []
    for alpha in range(2):
        q_alpha = zeros(16, 16)
        for a in range(4):
            q_alpha = madd(
                q_alpha,
                mscale(math.sqrt(2.0 * p) * lambdas[a][alpha], creators[a]),
            )
        q.append(q_alpha)

    # Mixed anticommutator gives 2 sum p lambda lambda^dagger = 4p I_2,
    # times the Fock identity on the operator side.
    for alpha in range(2):
        for beta in range(2):
            lhs = anticommutator(q[alpha], dagger(q[beta]))
            scalar = 2.0 * sum(
                p * lambdas[a][alpha] * lambdas[a][beta].conjugate()
                for a in range(4)
            )
            rhs = mscale(scalar, i16)
            assert_close(lhs, rhs, 1.0e-8)

    for alpha in range(2):
        for beta in range(2):
            assert_close(anticommutator(q[alpha], q[beta]), z16, 1.0e-8)

    # Q is odd under fermion parity.
    for q_alpha in q:
        assert_close(madd(mmul(parity, q_alpha), mmul(q_alpha, parity)), z16)

    # Combined spin/Fock 2T invariance at equal weights.
    for g in group:
        gamma = fock_reps[matrix_key(g)]
        gamma_d = dagger(gamma)
        transformed_fock = [mmul(mmul(gamma, q_beta), gamma_d) for q_beta in q]
        for alpha in range(2):
            transformed = zeros(16, 16)
            for beta in range(2):
                transformed = madd(
                    transformed,
                    mscale(g[alpha][beta], transformed_fock[beta]),
                )
            assert_close(transformed, q[alpha], 2.0e-8)

    print("TIR_SIC_NAIMARK_CAR_SUPERSYMMETRY_V0_1: PASS")


if __name__ == "__main__":
    main()
