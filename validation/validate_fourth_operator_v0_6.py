from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "computations" / "fourth_operator_search_v0_6.py"


def main():
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    result = json.loads(completed.stdout)

    assert result["schema"] == "INFINITIES_FOURTH_OPERATOR_SEARCH_RESULT_V0_6"
    assert result["overall_status"] == "PASS"

    tests = result["tests"]
    assert tests["strict_boolean_bmf_baseline"]["representable_count"] == 4
    assert tests["couple_monotone_extension"]["representable_count"] == 6
    assert tests["couple_plus_fixed_unary_library_dnf"]["representable_count"] == 16
    assert tests["gate_ite_shannon_two_variable"]["representable_count"] == 16
    assert tests["couple_real_square"]["status"] == "PASS"
    assert tests["fixpoint_reachability"]["fixed_point"] == [1, 1, 1]
    assert tests["quotient_carrier_boundary_recheck"]["coequalizer_profiles_A2_to_B3"] == {
        "1+1+1": 9,
        "2+1": 48,
        "3": 24,
    }

    conclusion = result["conclusion"]
    assert conclusion["single_universal_fourth_operator_found"] == "NO"
    assert conclusion["best_supported_data_plane_candidate"] == "COUPLE"
    assert conclusion["conditional_fourth_slot_is_mathematical_singleton"] == "NOT_ESTABLISHED"

    firewall = result["firewall"]
    assert firewall["couple_is_unique_minimal_fourth"] == "NOT_CLAIMED"
    assert firewall["typed_aux_dispatcher_is_one_mathematical_primitive"] == "NO"
    assert firewall["rh_proof"] == "NO"
    assert firewall["collatz_proof"] == "NO"

    print("PASS fourth-operator v0.6 candidate search and firewall")


if __name__ == "__main__":
    main()
