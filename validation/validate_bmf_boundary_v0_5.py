from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPUTATION = ROOT / "computations" / "bmf_boundary_v0_5.py"
SNAPSHOT = ROOT / "results" / "bmf_boundary_v0_5_result.json"


def main() -> None:
    raw = subprocess.check_output([sys.executable, str(COMPUTATION)], text=True)
    result = json.loads(raw)
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))

    assert result == snapshot, "committed v0.5 snapshot differs from deterministic computation"
    assert result["overall_status"] == "PASS"

    tests = result["tests"]
    assert tests["boolean_semiring_single_layer"]["representable_count"] == 4
    assert tests["boolean_semiring_single_layer"]["total_boolean_functions"] == 16
    assert tests["boolean_semiring_two_layer_closure"]["hidden_width_to_representable_count"] == {
        "1": 4,
        "2": 4,
        "3": 4,
    }
    assert tests["real_square_nonadditivity"]["T_2_plus_3"] == 25
    assert tests["real_square_nonadditivity"]["T_2_plus_T_3"] == 13
    assert tests["reachability_requires_iteration"]["after_one_pass"] == [1, 1, 0]
    assert tests["reachability_requires_iteration"]["after_two_passes"] == [1, 1, 1]
    assert tests["coequalizer_partition_distribution_A2_to_B3"] == {
        "1+1+1": 9,
        "2+1": 48,
        "3": 24,
    }
    assert tests["pushout_cardinality_distribution_A2_B2_C2"] == {"2": 12, "3": 4}
    assert tests["unrestricted_unary_map_fixed_fold_counts"] == {
        "AND": 10,
        "OR": 10,
        "XOR": 8,
    }

    claims = result["claims"]
    assert claims["finite_kernel_factorization_survives"] == "YES"
    assert claims["bmf_kernel_is_universal_computation_model"] == "NO"
    assert claims["universal_three_primitive_grammar"] == "NOT_ESTABLISHED"
    assert claims["quotient_is_proved_independent_fourth_primitive"] == "NO"
    assert claims["rh_proof"] == "NO"
    assert claims["collatz_proof"] == "NO"

    print("PASS BMF v0.5 boundary controls")


if __name__ == "__main__":
    main()
