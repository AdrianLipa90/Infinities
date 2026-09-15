from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmcf_obstruction import (
    balanced_couple,
    couple_activation_required,
    degree_upper_bound_from_couple_depth,
    minimal_binary_product_depth_dp,
    minimal_couple_depth_for_degree,
)


def main():
    assert not couple_activation_required(-1)
    assert not couple_activation_required(0)
    assert not couple_activation_required(1)
    assert couple_activation_required(2)

    for degree in range(0, 257):
        assert minimal_couple_depth_for_degree(degree) == minimal_binary_product_depth_dp(degree)

    for depth in range(0, 12):
        assert degree_upper_bound_from_couple_depth(depth) == 2**depth

    for degree in range(0, 65):
        value, depth = balanced_couple([3] * degree, lambda a, b: a * b, 1)
        assert value == 3**degree
        assert depth == minimal_couple_depth_for_degree(degree)

    try:
        degree_upper_bound_from_couple_depth(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative COUPLE depth must fail closed")

    output = subprocess.check_output(
        [sys.executable, str(ROOT / "computations" / "bmcf_obstruction_v0_8.py")],
        text=True,
    )
    result = json.loads(output)
    assert result["overall_status"] == "PASS"
    assert result["claims"]["couple_required_for_degree_gt_one"] == "EXACT_THEOREM_DEFINED_CLASS"
    assert result["claims"]["couple_unique_nonlinear_primitive"] == "NOT_CLAIMED"
    assert result["claims"]["bmcf_universal_computation_model"] == "NOT_CLAIMED"
    assert result["claims"]["novelty_relative_to_arithmetic_circuit_depth_results"] == "NOT_ESTABLISHED"

    print("PASS BMCF v0.8 conditional COUPLE obstruction controls")


if __name__ == "__main__":
    main()
