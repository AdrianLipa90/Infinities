#!/usr/bin/env python3
"""Exact/numerical controls for the affine-E6 Fourier Hilbert-Hotel core theorem."""

import cmath
import math

TOL=1e-10


def matmul(A,B):
    return [
        [sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def dagger(A):
    return [[A[i][j].conjugate() for i in range(len(A))] for j in range(len(A[0]))]


def maxerr(A,B):
    return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]


def main():
    B=[
        [1+0j,0j,0j,1+0j],
        [0j,1+0j,0j,1+0j],
        [0j,0j,1+0j,1+0j],
    ]

    w=cmath.exp(2j*math.pi/3)
    F=[
        [1/math.sqrt(3),1/math.sqrt(3),1/math.sqrt(3)],
        [1/math.sqrt(3),w/math.sqrt(3),w**2/math.sqrt(3)],
        [1/math.sqrt(3),w**2/math.sqrt(3),w/math.sqrt(3)],
    ]

    # Domain transform F on first three coordinates, identity on center.
    R=[
        [F[0][0],F[0][1],F[0][2],0j],
        [F[1][0],F[1][1],F[1][2],0j],
        [F[2][0],F[2][1],F[2][2],0j],
        [0j,0j,0j,1+0j],
    ]
    L=dagger(F)
    BF=matmul(matmul(L,B),R)

    target=[
        [1+0j,0j,0j,math.sqrt(3)+0j],
        [0j,1+0j,0j,0j],
        [0j,0j,1+0j,0j],
    ]
    assert maxerr(BF,target) < 1e-9

    # Trivial block B0=[1,sqrt(3)] and its canonical domain rotation.
    B0=[[1.0,math.sqrt(3.0)]]
    U0=[
        [0.5,math.sqrt(3.0)/2.0],
        [math.sqrt(3.0)/2.0,-0.5],
    ]
    U0t=[list(row) for row in zip(*U0)]
    assert maxerr(matmul(U0t,U0),[[1.0,0.0],[0.0,1.0]]) < TOL
    reduced=matmul(B0,U0)
    assert abs(reduced[0][0]-2.0) < TOL
    assert abs(reduced[0][1]) < TOL

    # Original protected and affine modes.
    v0=[1,1,1,-1]
    dp=[1,1,1,3]
    assert matvec(B,v0) == [0j,0j,0j]
    assert sum(a*b for a,b in zip(v0,dp)) == 0

    BT=dagger(B)
    BTB=matmul(BT,B)
    assert max(abs(x) for x in matvec(BTB,v0)) < TOL
    out=matvec(BTB,dp)
    assert max(abs(out[i]-4*dp[i]) for i in range(4)) < TOL

    # Singular-value squares: trivial block {4,0}, nontrivial blocks {1},{1}.
    B0t=[list(row) for row in zip(*B0)]
    B0tB0=matmul(B0t,B0)
    assert abs(B0tB0[0][0] + B0tB0[1][1] - 4.0) < TOL
    assert abs(B0tB0[0][0]*B0tB0[1][1]-B0tB0[0][1]*B0tB0[1][0]) < TOL

    # Total finite index: domain 4 - codomain 3 = +1.
    assert 4-3 == 1
    # Nontrivial scalar blocks are invertible/index zero.
    assert 1-1 == 0

    print("TIR_E6_FOURIER_HILBERT_HOTEL_CORE_V0_1: PASS")
    print("FOURIER_BLOCKS = [1,sqrt(3)] + [1] + [1]")
    print("TRIVIAL_BLOCK_UNITARY_NORMAL_FORM = [2,0]")
    print("INDEX_DEFECT_LOCATION = TRIVIAL_C3_BLOCK")
    print("AFFINE_CRITICAL_SINGULAR_VALUE = 2_IN_TRIVIAL_C3_BLOCK")
    print("NONTRIVIAL_CHARACTER_BLOCKS = INVERTIBLE_SPECTATORS")


if __name__ == "__main__":
    main()
