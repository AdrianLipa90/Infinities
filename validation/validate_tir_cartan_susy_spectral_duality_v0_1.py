#!/usr/bin/env python3
"""Exact controls for the Cartan-SUSY spectral duality theorem."""

import math

TOL=1e-10


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A,B):
    return [
        [sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]


def eye(n):
    return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]


def msub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c,A):
    return [[c*x for x in row] for row in A]


def maxabs(A):
    return max(abs(x) for row in A for x in row)


def adjacency_from_B(B):
    Bt=transpose(B)
    np=len(Bt)
    nm=len(B)
    top=[
        [0.0]*np + Bt[i]
        for i in range(np)
    ]
    bottom=[
        B[i] + [0.0]*nm
        for i in range(nm)
    ]
    return top+bottom


def blockdiag(A,B):
    out=[]
    for i,row in enumerate(A):
        out.append(row+[0.0]*len(B))
    for row in B:
        out.append([0.0]*len(A)+row)
    return out


def Bn(n):
    return [[1.0 if j==i or j==n else 0.0 for j in range(n+1)] for i in range(n)]


def main():
    for n in range(1,13):
        B=Bn(n)
        Bt=transpose(B)
        H=blockdiag(matmul(Bt,B),matmul(B,Bt))
        D=adjacency_from_B(B)
        N=len(D)
        C=msub(mscale(2.0,eye(N)),D)

        # Exact polynomial identity H=(2I-C)^2 = D^2.
        D2=matmul(D,D)
        twoIminusC=msub(mscale(2.0,eye(N)),C)
        RHS=matmul(twoIminusC,twoIminusC)
        assert maxabs(msub(H,D2)) < TOL
        assert maxabs(msub(H,RHS)) < TOL

        # 4I-H = C(4I-C).
        lhs=msub(mscale(4.0,eye(N)),H)
        rhs=matmul(C,msub(mscale(4.0,eye(N)),C))
        assert maxabs(msub(lhs,rhs)) < TOL

        # Protected zero mode in source/even sector.
        vsrc=[1.0]*n+[-1.0]
        v=vsrc+[0.0]*n
        assert max(abs(x) for x in matvec(H,v)) < TOL
        Cv=matvec(C,v)
        assert max(abs(Cv[i]-2.0*v[i]) for i in range(N)) < TOL

        # Positive Perron mode and top Hamiltonian energy n+1.
        lam=math.sqrt(n+1.0)
        dplus=[1.0]*n+[float(n)]
        dminus=[lam]*n
        d=dplus+dminus
        Dd=matvec(D,d)
        assert max(abs(Dd[i]-lam*d[i]) for i in range(N)) < 2e-9
        Hd=matvec(H,d)
        assert max(abs(Hd[i]-(n+1.0)*d[i]) for i in range(N)) < 2e-8

        if n==3:
            Cd=matvec(C,d)
            assert max(abs(x) for x in Cd) < 2e-9
            assert abs((n+1)-4.0) < TOL
        elif n<3:
            assert n+1 < 4
        else:
            assert n+1 > 4

    # Affine E6 exact distinguished source vectors.
    B=Bn(3)
    Bt=transpose(B)
    BTB=matmul(Bt,B)
    v0=[1,1,1,-1]
    da=[1,1,1,3]
    assert matvec(BTB,v0) == [0.0,0.0,0.0,0.0]
    assert matvec(BTB,da) == [4.0*x for x in da]
    assert sum(a*b for a,b in zip(v0,da)) == 0

    print("TIR_CARTAN_SUSY_SPECTRAL_DUALITY_V0_1: PASS")
    print("H = D^2 = (2I-C)^2")
    print("SUSY_ZERO <-> CARTAN_EIGENVALUE_2")
    print("AFFINE_ZERO <-> SUSY_ENERGY_4")
    print("CYCLIC_ARM_AFFINE_THRESHOLD = EMAX_4_AT_N3")


if __name__ == "__main__":
    main()
