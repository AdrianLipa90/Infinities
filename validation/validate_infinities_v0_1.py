from __future__ import annotations

from fractions import Fraction
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from infinities.core import (
    accelerated_odd_collatz,
    cantor_dimension,
    cantor_dimension_from_shannon,
    collatz_B,
    collatz_mobius_B,
    compactify_positive,
    continued_fraction_sqrt2,
    euler_product_partial,
    gabriel_area_converges,
    gabriel_volume_converges,
    hilbert_shift_defect_rank,
    hilbert_shift_fredholm_index,
    p_adic_norm_fraction,
    telescoping_product,
    two_adic_geometric_partial,
    zeta_dirichlet_partial,
)


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    print(f"PASS {name}")


def main():
    for x in (0.125, 0.5, 1.0, 2.0, 8.0):
        a = compactify_positive(x)
        b = compactify_positive(1.0/x)
        check(f"inversion_q_{x}", math.isclose(b.q, 1.0-a.q, abs_tol=1e-15))
        check(f"inversion_eta_{x}", math.isclose(b.eta, -a.eta, abs_tol=1e-15))
        check(f"inversion_B_{x}", math.isclose(b.B, -a.B, abs_tol=1e-15))

    check("half_seam", compactify_positive(1.0).q == 0.5)
    check("cantor_shannon_identity", math.isclose(cantor_dimension(), cantor_dimension_from_shannon(), rel_tol=0, abs_tol=1e-15))

    for N in (2, 3, 10, 100):
        check(f"telescoping_{N}", telescoping_product(N) == Fraction(1, N))

    cf = continued_fraction_sqrt2(20)
    check("continued_fraction_sqrt2", abs(float(cf)-math.sqrt(2.0)) < 1e-12)

    for N in (0, 1, 4, 10):
        S = two_adic_geometric_partial(N)
        error = Fraction(S + 1, 1)
        expected = Fraction(1, 2 ** (N+1))
        check(f"two_adic_error_{N}", p_adic_norm_fraction(error, 2) == expected)

    for n in (1, 3, 5, 7, 9, 15, 27, 31):
        u, a = accelerated_odd_collatz(n)
        check(f"collatz_mobius_{n}", collatz_mobius_B(collatz_B(n), a) == collatz_B(u))

    check("gabriel_p1_volume", gabriel_volume_converges(1.0))
    check("gabriel_p1_area_diverges", not gabriel_area_converges(1.0))
    check("gabriel_threshold_below_half", not gabriel_volume_converges(0.5))
    check("gabriel_area_above_one", gabriel_area_converges(1.01))

    check("hilbert_defect_rank_1", hilbert_shift_defect_rank(1) == 1)
    check("hilbert_defect_rank_7", hilbert_shift_defect_rank(7) == 7)
    check("hilbert_index_7", hilbert_shift_fredholm_index(7) == -7)

    target = math.pi**2/6.0
    ds = zeta_dirichlet_partial(2.0, 20000)
    ep = euler_product_partial(2.0, 20000)
    check("zeta_dirichlet_numerical", abs(ds-target) < 6e-5)
    check("euler_product_numerical", abs(ep-target) < 2e-5)

    print("PASS ALL")


if __name__ == "__main__":
    main()
