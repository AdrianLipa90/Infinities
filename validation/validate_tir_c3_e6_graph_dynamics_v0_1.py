#!/usr/bin/env python3
"""Audit the C3-compensated supercharge operator-support graph.

The validator checks that, after effective C3 character labeling, the nonzero
inter-isotypic blocks of each of the two rest-frame supercharge channels have
exactly the affine-E6 McKay edge support.

This is a finite representation-theory/operator-support audit. It does not
prove an E6 gauge theory or a full Lorentz-covariant physical model.
"""
from __future__ import annotations

import itertools
import math

from validate_tir_naimark_mckay_e6_v0_1 import (
    analysis_map,
    cinner,
    dagger,
    det4,
    eye,
    generate_2t,
    matrix_key,
    mmul,
    mscale,
    msub,
    outcome_rep,
    spinor_from_bloch,
    tetra_vectors,
    trace,
    vdot,
    zeros,
)
from validate_tir_sic_naimark_car_susy_v0_1 import creation
from validate_tir_c3_untwisted_naimark_n2_rest_v0_1 import (
    conjugate_matrix,
    gram_schmidt_complement,
)


TOL = 5.0e-8


LABELS = ("1", "chi", "chi2", "rho", "rhochi", "rhochi2", "3")
DIMS = {"1": 1, "chi": 1, "chi2": 1, "rho": 2, "rhochi": 2, "rhochi2": 2, "3": 3}


def det_small(a):
    n = len(a)
    if n == 0:
        return 1 + 0j
    total = 0j
    for p in itertools.permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        sign = -1 if inv % 2 else 1
        term = 1 + 0j
        for i in range(n):
            term *= a[i][p[i]]
        total += sign * term
    return total


SUBSETS = [s for k in range(5) for s in itertools.combinations(range(4), k)]
SUB_INDEX = {s: i for i, s in enumerate(SUBSETS)}


def exterior_rep4(u):
    out = zeros(16, 16)
    for s in SUBSETS:
        k = len(s)
        js = SUB_INDEX[s]
        for t in SUBSETS:
            if len(t) != k:
                continue
            it = SUB_INDEX[t]
            if k == 0:
                out[it][js] = 1 + 0j
            else:
                minor = [[u[i][j] for j in s] for i in t]
                out[it][js] = det_small(minor)
    return out


def frob_sq(a):
    return sum(abs(z) ** 2 for row in a for z in row)


def projector_from_character(records, char, dim):
    out = zeros(16, 16)
    for (_, gamma, _), z in zip(records, char):
        out = [
            [out[i][j] + dim * z.conjugate() * gamma[i][j] / 24.0 for j in range(16)]
            for i in range(16)
        ]
    return out


def linear_creation(coeffs, creators):
    out = zeros(16, 16)
    for a, z in enumerate(coeffs):
        out = [
            [out[i][j] + z * creators[a][i][j] for j in range(16)]
            for i in range(16)
        ]
    return out


def column(a, j):
    return [a[i][j] for i in range(len(a))]


def twist(label: str, r: int) -> str:
    r %= 3
    if label == "1":
        return ("1", "chi", "chi2")[r]
    if label == "chi":
        return ("chi", "chi2", "1")[r]
    if label == "chi2":
        return ("chi2", "1", "chi")[r]
    if label == "rho":
        return ("rho", "rhochi", "rhochi2")[r]
    if label == "rhochi":
        return ("rhochi", "rhochi2", "rho")[r]
    if label == "rhochi2":
        return ("rhochi2", "rho", "rhochi")[r]
    if label == "3":
        return "3"
    raise KeyError(label)


def undirected(edges):
    return {tuple(sorted((a, b))) for a, b in edges if a != b}


def main():
    lambdas = [spinor_from_bloch(n) for n in tetra_vectors()]
    v = analysis_map(lambdas)

    # CAR orientation: primary A ~= rho, complement B ~= rho chi^2.
    a_iso = conjugate_matrix(v)
    b_iso = gram_schmidt_complement(a_iso)

    creators = [creation(a) for a in range(4)]
    a_create = [linear_creation(column(a_iso, alpha), creators) for alpha in range(2)]
    b_create = [linear_creation(column(b_iso, alpha), creators) for alpha in range(2)]

    group, _ = generate_2t()

    rec = []
    chi = []
    char_rho = []
    for g in group:
        r, _, _ = outcome_rep(g, lambdas)
        rbar = conjugate_matrix(r)
        gamma = exterior_rep4(rbar)
        rec.append((g, gamma, rbar))
        x = det4(r) ** 2
        chi.append(x)
        char_rho.append(trace(g))

    chi2 = [x * x for x in chi]
    char_3 = [abs(z) ** 2 - 1.0 for z in char_rho]
    chars = {
        "1": [1 + 0j] * 24,
        "chi": chi,
        "chi2": chi2,
        "rho": char_rho,
        "rhochi": [a * b for a, b in zip(char_rho, chi)],
        "rhochi2": [a * b for a, b in zip(char_rho, chi2)],
        "3": char_3,
    }

    # Verify character orthonormality before using central projectors.
    for a in LABELS:
        for b in LABELS:
            target = 1 if a == b else 0
            val = cinner(chars[a], chars[b])
            assert abs(val - target) < 3e-7, (a, b, val)

    projectors = {
        name: projector_from_character(rec, chars[name], DIMS[name])
        for name in LABELS
    }

    # Raw Fock transition support of the two one-particle spinor summands.
    raw_a = set()
    raw_b = set()
    for src in LABELS:
        for dst in LABELS:
            pa = 0.0
            pb = 0.0
            for op in a_create:
                block = mmul(mmul(projectors[dst], op), projectors[src])
                pa += frob_sq(block)
            for op in b_create:
                block = mmul(mmul(projectors[dst], op), projectors[src])
                pb += frob_sq(block)
            if pa > 1e-8:
                raw_a.add((src, dst))
            if pb > 1e-8:
                raw_b.add((src, dst))

    # Standard affine-E6 McKay support for tensoring by rho.
    target = undirected({
        ("1", "rho"),
        ("chi", "rhochi"),
        ("chi2", "rhochi2"),
        ("3", "rho"),
        ("3", "rhochi"),
        ("3", "rhochi2"),
    })

    # Q1 has internal I_3: character sector r is unchanged.
    effective_q1 = set()
    for src, dst in raw_a:
        for r in range(3):
            effective_q1.add((twist(src, r), twist(dst, r)))

    # Q2 uses X with D X D^* = chi X. It shifts r -> r+1 and
    # compensates the raw complement type rho chi^2 to effective rho.
    effective_q2 = set()
    for src, dst in raw_b:
        for r in range(3):
            effective_q2.add((twist(src, r), twist(dst, r + 1)))

    q1_graph = undirected(effective_q1)
    q2_graph = undirected(effective_q2)

    assert q1_graph == target, (q1_graph, target)
    assert q2_graph == target, (q2_graph, target)

    # Selection-rule firewall: no compensated non-McKay edge survives.
    assert not (q1_graph - target)
    assert not (q2_graph - target)

    print("TIR_C3_E6_GRAPH_DYNAMICS_V0_1: PASS")
    print("Q1_EFFECTIVE_SUPPORT = AFFINE_E6")
    print("Q2_EFFECTIVE_SUPPORT = AFFINE_E6")
    print("E6_EDGE_COUNT =", len(target))
    print("E6_GAUGE_THEORY = NOT_CLAIMED")
    print("FULL_LORENTZ_UNITARY_IMPLEMENTATION = OPEN")


if __name__ == "__main__":
    main()
