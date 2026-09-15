from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from infinities.core import (
    cantor_dimension, cantor_dimension_from_shannon, compactify_positive,
    continued_fraction_sqrt2, euler_product_partial, hilbert_shift_defect_rank,
    hilbert_shift_fredholm_index, telescoping_product, two_adic_geometric_partial,
    p_adic_norm_fraction, zeta_dirichlet_partial
)


def main():
    samples = {}
    samples["half_seam"] = {
        "x": 1.0,
        "compactified": compactify_positive(1.0).__dict__,
        "status": "EXACT_BY_DEFINITION",
    }
    samples["cantor"] = {
        "dimension_classical": cantor_dimension(),
        "dimension_from_shannon": cantor_dimension_from_shannon(),
        "difference": cantor_dimension()-cantor_dimension_from_shannon(),
        "status": "EXACT_FORMULA_NUMERICAL_EVALUATION",
    }
    samples["telescoping"] = {
        str(N): {"product": str(telescoping_product(N)), "inverse": N}
        for N in (2, 10, 100, 1000)
    }
    cf = continued_fraction_sqrt2(20)
    samples["continued_fraction"] = {
        "convergent": str(cf),
        "float": float(cf),
        "sqrt2": math.sqrt(2),
        "error": abs(float(cf)-math.sqrt(2)),
    }
    samples["two_adic"] = {}
    for N in (0, 1, 4, 10, 20):
        S = two_adic_geometric_partial(N)
        samples["two_adic"][str(N)] = {
            "S_N": S,
            "real_size": abs(S),
            "two_adic_distance_to_minus_one": str(p_adic_norm_fraction(S+1, 2)),
        }
    samples["hilbert_shift"] = {
        str(k): {"defect_rank": hilbert_shift_defect_rank(k), "fredholm_index": hilbert_shift_fredholm_index(k)}
        for k in (1, 2, 8)
    }
    target = math.pi**2/6
    samples["zeta2"] = {
        "target_pi2_over_6": target,
        "dirichlet_N_20000": zeta_dirichlet_partial(2.0, 20000),
        "euler_prime_limit_20000": euler_product_partial(2.0, 20000),
        "status": "NUMERICAL_WITNESS",
    }
    print(json.dumps(samples, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
