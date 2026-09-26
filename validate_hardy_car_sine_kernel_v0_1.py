#!/usr/bin/env python3
"""No-target-leakage validator for the Hardy-CAR sine-kernel theorem."""
import cmath
import math


def hardy_projection_kernel_direct(N, theta, phi):
    return sum(cmath.exp(1j*n*(theta-phi)) for n in range(N))/(2*math.pi)


def hardy_projection_kernel_closed(N, theta, phi):
    d = theta-phi
    if abs(math.sin(d/2)) < 1e-14:
        return N/(2*math.pi)
    return (
        cmath.exp(1j*(N-1)*d/2)
        * math.sin(N*d/2)
        / (2*math.pi*math.sin(d/2))
    )


def g2_finite_from_car(N, s):
    d = 2*math.pi*s/N
    rho = N/(2*math.pi)
    k = hardy_projection_kernel_direct(N, d, 0.0)
    return 1.0-abs(k/rho)**2


def g2_finite_closed(N, s):
    if abs(s) < 1e-14:
        return 0.0
    return 1.0-(math.sin(math.pi*s)/(N*math.sin(math.pi*s/N)))**2


def derived_limit(s):
    if abs(s) < 1e-14:
        return 0.0
    return 1.0-(math.sin(math.pi*s)/(math.pi*s))**2


def main():
    for N in [2,3,8,17,64]:
        for d in [0.13,-0.41,1.2,2.7]:
            a=hardy_projection_kernel_direct(N,d,0.0)
            b=hardy_projection_kernel_closed(N,d,0.0)
            assert abs(a-b) < 2e-12

    grid=[-2.5,-1.7,-0.9,-0.25,0.0,0.25,0.9,1.7,2.5]
    for N in [4,8,32,128]:
        for s in grid:
            assert abs(g2_finite_from_car(N,s)-g2_finite_closed(N,s)) < 3e-12

    for N in [2,5,31]:
        assert abs(g2_finite_from_car(N,0.0)) < 1e-14

    errors=[]
    dense=[-3.0+6.0*j/600 for j in range(601)]
    for N in [16,64,256,1024]:
        err=max(abs(g2_finite_from_car(N,s)-derived_limit(s)) for s in dense)
        errors.append(err)
    assert all(errors[i+1] < errors[i] for i in range(len(errors)-1))
    assert errors[-1] < 4e-7

    for s in [1e-3,5e-4,2.5e-4]:
        ratio=derived_limit(s)/(s*s)
        assert abs(ratio-math.pi**2/3) < 2e-5

    print("TIR_HARDY_CAR_SINE_KERNEL_FORCED_PREDICTION_V0_1: PASS")
    print("INPUTS=HARDY_SHIFT_ORBIT+FINITE_PROJECTOR+CAR_SLATER+UNIT_DENSITY_UNFOLDING")
    print("GUE_OR_ZETA_USED_AS_INPUT=false")
    print("FINITE_N=g2_N(s)=1-[sin(pi s)/(N sin(pi s/N))]^2")
    print("LIMIT=g2(s)=1-[sin(pi s)/(pi s)]^2")
    print("PHASE_FORM=g2(DeltaPhi)=1-[sin(DeltaPhi/2)/(DeltaPhi/2)]^2")
    print("MAX_ERROR_N1024=", errors[-1])
    print("STATUS=DERIVED_IN_DECLARED_HARDY_CAR_SECTOR/FORCED_PREDICTION")


if __name__ == "__main__":
    main()
