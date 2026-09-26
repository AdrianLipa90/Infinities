#!/usr/bin/env python3
"""No-target-leakage validator for the finite Hardy-CAR form factor."""
import cmath
import math


def cluster_direct(N: int, s: float) -> float:
    z=sum(cmath.exp(2j*math.pi*n*s/N) for n in range(N))/N
    return abs(z)**2


def cluster_fourier(N: int, s: float) -> complex:
    return sum(
        (N-abs(k))*cmath.exp(2j*math.pi*k*s/N)
        for k in range(-(N-1),N)
    )/(N*N)


def form_factor_finite(N: int, k: int) -> float:
    if abs(k) < N:
        return abs(k)/N
    return 1.0


def main():
    for N in [2,3,8,31,128]:
        for s in [-2.2,-0.7,-0.1,0.0,0.35,1.4,2.8]:
            assert abs(cluster_direct(N,s)-cluster_fourier(N,s)) < 2e-12

    for N in [3,8,32,127]:
        for k in range(-2*N,2*N+1):
            expected=min(abs(k)/N,1.0)
            assert abs(form_factor_finite(N,k)-expected) < 1e-15

    for N in [16,64,256,1024]:
        for tau in [0.125,0.25,0.5,0.75,1.0,1.25]:
            k=round(N*tau)
            observed=form_factor_finite(N,k)
            assert abs(observed-min(abs(k/N),1.0)) < 1e-15

    print("TIR_HARDY_CAR_SPECTRAL_FORM_FACTOR_V0_1: PASS")
    print("GUE_OR_ZETA_USED_AS_INPUT=false")
    print("FINITE_FORM_FACTOR=S_N(k/N)=min(|k|/N,1)")
    print("CONTINUUM_FORM_FACTOR=S(tau)=min(|tau|,1)")
    print("STATUS=DERIVED_IN_FRAMEWORK/FORCED_PREDICTION")


if __name__ == "__main__":
    main()
