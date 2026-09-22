#!/usr/bin/env python3
"""Exact controls for the exceptional McKay balance / C6 selector theorem."""

from itertools import combinations
from math import gcd


def det2(a,b,c,d):
    return a*d-b*c


def det3(M):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )


def smith_invariants_3x3(M):
    # For a full-rank 3x3 integer matrix:
    # d1 = gcd(entries), d1*d2 = gcd(2x2 minors), d1*d2*d3 = |det|.
    entries = [abs(x) for row in M for x in row]
    d1 = 0
    for x in entries:
        d1 = gcd(d1, x)

    minors = []
    for rs in combinations(range(3), 2):
        for cs in combinations(range(3), 2):
            a,b = M[rs[0]][cs[0]], M[rs[0]][cs[1]]
            c,d = M[rs[1]][cs[0]], M[rs[1]][cs[1]]
            minors.append(abs(det2(a,b,c,d)))
    g2 = 0
    for x in minors:
        g2 = gcd(g2, x)

    det = abs(det3(M))
    d2 = g2 // d1
    d3 = det // (d1*d2)
    return (d1,d2,d3)


def bipartition(n, edges):
    adj=[[] for _ in range(n)]
    for i,j in edges:
        adj[i].append(j); adj[j].append(i)
    color=[None]*n
    color[0]=0
    stack=[0]
    while stack:
        i=stack.pop()
        for j in adj[i]:
            if color[j] is None:
                color[j]=1-color[i]
                stack.append(j)
            else:
                assert color[j] != color[i]
    assert all(c is not None for c in color)
    return color


def main():
    # Binary (2,3,n) presentations: r^2=s^3=t^n=rst.
    abelian = {}
    for n in (3,4,5):
        M=[
            [2,-3,0],
            [0,3,-n],
            [-1,-1,n-1],
        ]
        snf=smith_invariants_3x3(M)
        abelian[n]=snf
    assert abelian[3] == (1,1,3)
    assert abelian[4] == (1,1,2)
    assert abelian[5] == (1,1,1)

    data={
        "E6":{
            "n":3,
            "order":24,
            "dims":[3,2,2,2,1,1,1],
            "edges":[(0,1),(0,2),(0,3),(1,4),(2,5),(3,6)],
            "h":12,
            "ab_order":3,
        },
        "E7":{
            "n":4,
            "order":48,
            "dims":[4,3,2,1,3,2,1,2],
            "edges":[(0,1),(1,2),(2,3),(0,4),(4,5),(5,6),(0,7)],
            "h":18,
            "ab_order":2,
        },
        "E8":{
            "n":5,
            "order":120,
            "dims":[6,5,4,3,2,1,4,2,3],
            "edges":[(0,1),(1,2),(2,3),(3,4),(4,5),(0,6),(6,7),(0,8)],
            "h":30,
            "ab_order":1,
        },
    }

    results={}
    for name,row in data.items():
        d=row["dims"]
        color=bipartition(len(d),row["edges"])
        lin=[
            sum(d[i] for i,c in enumerate(color) if c==k)
            for k in (0,1)
        ]
        sq=[
            sum(d[i]*d[i] for i,c in enumerate(color) if c==k)
            for k in (0,1)
        ]
        assert sum(d) == row["h"]
        assert sum(x*x for x in d) == row["order"]
        assert sq == [row["order"]//2, row["order"]//2]

        joint_order = 2*row["ab_order"]
        results[name]=(lin,sq,joint_order,row["h"]//2)

    # Linear parity balance is exceptional to E6 among this family.
    assert sorted(results["E6"][0]) == [6,6]
    assert sorted(results["E7"][0]) == [8,10]
    assert sorted(results["E8"][0]) == [14,16]

    # Joint abelianization x fermion parity:
    # E6: C3 x C2 = C6, E7: C2 x C2 = V4, E8: C2.
    # Order equals h/2 only in E6.
    assert results["E6"][2] == 6 == results["E6"][3]
    assert results["E7"][2] == 4 and results["E7"][3] == 9
    assert results["E8"][2] == 2 and results["E8"][3] == 15

    matches=[
        name for name,(lin,sq,joint,half_h) in results.items()
        if lin[0] == lin[1] and joint == half_h
    ]
    assert matches == ["E6"]

    # Number of 1D irreps equals abelianization order for finite groups.
    assert [data[k]["ab_order"] for k in ("E6","E7","E8")] == [3,2,1]

    print("TIR_EXCEPTIONAL_MCKAY_BALANCE_C6_SELECTOR_V0_1: PASS")
    print("ABELIANIZATIONS = C3, C2, 1")
    print("LINEAR_PARITY_SUMS = E6 6|6; E7 8|10; E8 14|16")
    print("QUADRATIC_PARITY_BALANCE = UNIVERSAL")
    print("JOINT_GRADING_ORDERS = 6,4,2")
    print("HALF_COXETER = 6,9,15")
    print("UNIQUE_MATCH = E6")


if __name__ == "__main__":
    main()
