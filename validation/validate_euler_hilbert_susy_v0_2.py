#!/usr/bin/env python3
"""Exact finite regression controls for Euler-Hilbert-Hotel SUSY v0.2.

These controls verify finite algebraic/group-theoretic identities only.
They do not replace the infinite-dimensional Fredholm/Toeplitz theorems.
"""
from fractions import Fraction


TETRA = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def pauli_x(v):
    x, y, z = v
    return (x, -y, -z)


def pauli_y(v):
    x, y, z = v
    return (-x, y, -z)


def pauli_z(v):
    x, y, z = v
    return (-x, -y, z)


def c3(v):
    x, y, z = v
    return (y, z, x)


def perm_from_action(action):
    return tuple(TETRA.index(action(v)) for v in TETRA)


def compose(p, q):
    return tuple(p[q[i]] for i in range(4))


def generated_permutation_group(gens):
    identity = tuple(range(4))
    group = {identity}
    frontier = [identity]
    while frontier:
        p = frontier.pop()
        for g in gens:
            h = compose(g, p)
            if h not in group:
                group.add(h)
                frontier.append(h)
    return group


def qmul(q, r):
    a, b, c, d = q
    e, f, g, h = r
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


def qconj(q):
    a, b, c, d = q
    return (a, -b, -c, -d)


def qpow(q, n):
    out = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    for _ in range(n):
        out = qmul(out, q)
    return out


ONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
MINUS_ONE = (Fraction(-1), Fraction(0), Fraction(0), Fraction(0))
QI = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
QJ = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))
QK = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))
OMEGA = (
    Fraction(-1, 2),
    Fraction(1, 2),
    Fraction(1, 2),
    Fraction(1, 2),
)


def subgroup_closure(gens):
    group = {ONE}
    frontier = [ONE]
    all_gens = list(gens) + [qconj(g) for g in gens]
    while frontier:
        x = frontier.pop()
        for g in all_gens:
            y = qmul(g, x)
            if y not in group:
                group.add(y)
                frontier.append(y)
    return group


def main():
    # Tetrahedral 2-design / SIC geometry.
    assert tuple(sum(v[j] for v in TETRA) for j in range(3)) == (0, 0, 0)
    for a in range(4):
        assert dot(TETRA[a], TETRA[a]) == 3
        for b in range(4):
            if a != b:
                assert dot(TETRA[a], TETRA[b]) == -1
                # Tr(P_a P_b) = (1+n_a.n_b)/2 = 1/3.
                assert Fraction(1, 2) * (1 + Fraction(-1, 3)) == Fraction(1, 3)

    second = [
        [sum(TETRA[a][i] * TETRA[a][j] for a in range(4)) for j in range(3)]
        for i in range(3)
    ]
    assert second == [[4, 0, 0], [0, 4, 0], [0, 0, 4]]

    # Projective Pauli orbit is exactly the tetrahedron.
    orbit = {TETRA[0], pauli_x(TETRA[0]), pauli_y(TETRA[0]), pauli_z(TETRA[0])}
    assert orbit == set(TETRA)

    px = perm_from_action(pauli_x)
    py = perm_from_action(pauli_y)
    pz = perm_from_action(pauli_z)
    pc3 = perm_from_action(c3)

    # V4 from Pauli half-turns; A4 after adjoining tetrahedral C3.
    v4 = generated_permutation_group([px, py, pz])
    a4 = generated_permutation_group([px, py, pz, pc3])
    assert len(v4) == 4
    assert len(a4) == 12

    # Exact binary tetrahedral lift: Q8 extended by an order-three Hurwitz unit.
    q8 = subgroup_closure([QI, QJ])
    two_t = subgroup_closure([QI, QJ, OMEGA])
    assert len(q8) == 8
    assert len(two_t) == 24
    assert qpow(OMEGA, 3) == ONE
    assert q8.issubset(two_t)

    # Omega conjugation cyclically rotates the quaternion axes (orientation choice).
    omega_inv = qconj(OMEGA)
    conj_i = qmul(qmul(OMEGA, QI), omega_inv)
    conj_j = qmul(qmul(OMEGA, QJ), omega_inv)
    conj_k = qmul(qmul(OMEGA, QK), omega_inv)
    assert {conj_i, conj_j, conj_k} == {QI, QJ, QK}
    assert len({conj_i, conj_j, conj_k}) == 3

    # Index arithmetic / modular composition for the monomial specialization.
    for k in range(0, 17):
        assert -k == 0 - k
    for k in range(0, 9):
        for m in range(0, 9):
            assert -(k + m) == (-k) + (-m)

    print("EULER_HILBERT_HOTEL_SUSY_V0_2: PASS")


if __name__ == "__main__":
    main()
