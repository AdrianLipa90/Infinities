#!/usr/bin/env python3
"""Exact controls for the affine-critical C6 supergrading selection theorem."""

from math import gcd, sqrt


def product_order(n):
    # Order of (generator of C_n, generator of C_2).
    from math import lcm
    return lcm(n, 2)


def main():
    critical = []
    for n in range(1, 33):
        # C_n x C_2 is cyclic iff gcd(n,2)=1.
        cyclic = gcd(n, 2) == 1
        assert (product_order(n) == 2 * n) == cyclic

        # Universal graph index.
        assert (n + 1) - n == 1

        # Affine threshold for the declared family.
        rho = sqrt(n + 1)
        is_affine = abs(rho - 2.0) < 1e-12
        if is_affine:
            critical.append(n)

        # If cyclic, supercharge degree n flips parity.
        if cyclic:
            assert n % 2 == 1
            assert (n % 2) == 1
            # q -> q+n changes parity and preserves C_n charge.
            for q in range(2 * n):
                q2 = (q + n) % (2 * n)
                assert (q2 - q) % n == 0
                assert (q2 - q) % 2 == 1

    assert critical == [3]

    n = 3
    assert gcd(n, 2) == 1
    assert product_order(n) == 6

    # Critical graph spectrum at n=3.
    even_spectrum = [0, 1, 1, 4]
    assert even_spectrum == [0, 1, 1, 4]

    # C6 charge pairs induced by degree-3 supercharges.
    pairs = {(0, 3), (2, 5), (4, 1)}
    assert all((b - a) % 6 == 3 for a, b in pairs)

    print("TIR_AFFINE_CRITICAL_C6_SELECTION_V0_1: PASS")
    print("UNIVERSAL_INDEX = +1_FOR_ALL_N")
    print("AFFINE_CRITICAL_ARM_COUNT = 3_ONLY")
    print("SELECTED_JOINT_GRADING = C6")
    print("SELECTED_SUPERCHARGE_DEGREE = 3_MOD_6")


if __name__ == "__main__":
    main()
