from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmf import Semiring
from infinities.bmcf import PolynomialTerm, polynomial_transform


def exact_integer_polynomial_control():
    semiring = Semiring(add=lambda a, b: a + b, mul=lambda a, b: a * b, zero=0, one=1)
    values = {"x": 2, "y": 3}
    terms = {
        "p": (
            PolynomialTerm(5, ()),
            PolynomialTerm(7, ("x",)),
            PolynomialTerm(11, ("x", "y")),
            PolynomialTerm(13, ("x", "x", "y")),
        )
    }
    got = polynomial_transform(values, ("p",), terms, semiring)
    expected = 5 + 7 * 2 + 11 * 2 * 3 + 13 * 2 * 2 * 3
    assert got == {"p": expected}


def main():
    exact_integer_polynomial_control()
    runner = ROOT / "computations" / "bmcf_polynomial_v0_7.py"
    proc = subprocess.run([sys.executable, str(runner)], check=True, capture_output=True, text=True)
    result = json.loads(proc.stdout)
    assert result["overall_status"] == "PASS"
    assert result["claims"]["finite_word_polynomial_bmcf_factorization"] == "EXACT_DEFINED_CLASS"
    assert result["claims"]["commutative_finite_polynomial_factorization"] == "EXACT_DEFINED_CLASS"
    assert result["claims"]["finite_multilinear_kernel_factorization"] == "EXACT_DEFINED_CLASS"
    assert result["claims"]["bmcf_universal_computation_model"] == "NOT_CLAIMED"
    assert result["claims"]["couple_unique_minimal_fourth_operator"] == "NOT_CLAIMED"
    assert result["claims"]["novelty_relative_to_arithmetic_circuits"] == "NOT_ESTABLISHED"
    assert result["tests"]["strict_bmf_degree_separation"]["max_degree_seen_for_fixed_scalar_linear_forms"] <= 1
    assert result["tests"]["strict_bmf_degree_separation"]["couple_quadratic_degree"] == 2
    assert result["tests"]["ordered_noncommutative_word"]["A_times_B"] != result["tests"]["ordered_noncommutative_word"]["B_times_A"]
    print("PASS BMCF v0.7 polynomial theorem controls")


if __name__ == "__main__":
    main()
