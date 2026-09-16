from __future__ import annotations

import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmcf_boundary import (
    absolute_value_polynomial_certificate,
    omega_c_for_polynomial_degree,
    omega_c_for_target,
    polynomial_compose,
    polynomial_degree,
    reciprocal_polynomial_certificate,
)


def main():
    # Exact degree multiplication under nonconstant composition over Q.
    outer = (1, -2, 3)       # degree 2
    inner = (4, 0, 0, 5)     # degree 3
    composed = polynomial_compose(outer, inner)
    assert polynomial_degree(composed) == 6

    # Repeated-squaring degree targets hit the v0.8 lower bound exactly.
    for depth in range(0, 13):
        assert omega_c_for_polynomial_degree(2**depth) == depth

    # Exact finite inconsistency certificates for the two out-of-class targets.
    for degree in range(0, 25):
        assert reciprocal_polynomial_certificate(degree)
        assert absolute_value_polynomial_certificate(degree)

    # Fail closed: omega_C is not silently extended beyond polynomial targets.
    assert omega_c_for_target("POLYNOMIAL", 1) == 0
    assert omega_c_for_target("POLYNOMIAL", 2) == 1
    assert omega_c_for_target("POLYNOMIAL", 17) == 5
    assert omega_c_for_target("RATIONAL_RECIPROCAL") is None
    assert omega_c_for_target("PIECEWISE") is None

    try:
        omega_c_for_target("POLYNOMIAL")
    except ValueError:
        pass
    else:
        raise AssertionError("polynomial target without degree must fail closed")

    # Formal reciprocal witness: x*P=1 cannot hold for polynomial P.
    # The finite certificate below is a degree-5 exact rational instance.
    points = [Fraction(i) for i in range(1, 8)]
    assert len(points) == 7
    assert reciprocal_polynomial_certificate(5)

    output = subprocess.check_output(
        [sys.executable, str(ROOT / "computations" / "bmcf_boundary_v0_9.py")],
        text=True,
    )
    result = json.loads(output)
    assert result["overall_status"] == "PASS"
    assert result["claims"]["omega_C_is_universal_nonlinearity_measure"] == "NO"
    assert result["claims"]["reciprocal_is_globally_minimal_new_primitive"] == "NOT_CLAIMED"
    assert result["claims"]["gate_is_globally_minimal_new_primitive"] == "NOT_CLAIMED"
    assert result["claims"]["single_universal_fourth_operator"] == "NOT_ESTABLISHED"
    assert result["claims"]["novelty_relative_to_circuit_complexity"] == "NOT_ESTABLISHED"

    print("PASS BMCF v0.9 degree-boundary TNT controls")


if __name__ == "__main__":
    main()
