from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULT = HERE.parent / "results" / "gremlin_sweep_v0_1_result.json"

def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    print(f"PASS {name}")

def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    claimed_hash = data.pop("result_sha256_without_self_hash")
    payload = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    check("result_hash", hashlib.sha256(payload).hexdigest() == claimed_hash)
    check("catalog_size", data["catalog_size"] == 32)
    check("training_baseline", data["baseline_training"]["covered"] == 19 and data["baseline_training"]["uncovered"] == [])
    check("holdout_fail_loud", data["baseline_holdout"]["covered"] == 8 and data["baseline_holdout"]["total"] == 13)
    check("uncovered_holdouts", set(data["baseline_holdout"]["uncovered"]) == {"H04","H05","H06","H07","H13"})
    check("baseline_all_coverage", data["baseline_all"]["covered"] == 27 and data["baseline_all"]["total"] == 32)
    check("missing_operators", data["baseline_all"]["missing_operator_counts"] == {
        "AVERAGE": 1, "POWERSET": 1, "STOCHASTIC": 1, "TRANSFORM": 2
    })
    check("finite_schema_minimum", data["minimal_vocabulary_size_under_catalog_schema"] == 9)
    check("half_universal_falsified", data["half_seam_test"]["universal_half_hypothesis"] == "FAIL")
    check("half_counterexamples", set(data["half_seam_test"]["counterexample_case_ids"]) == {"I09","I14","I18","H08","H09"})
    check("no_open_problem_promotion", data["claims"]["rh_proof"] == "NO" and data["claims"]["collatz_proof"] == "NO")
    check("no_minimality_theorem_promotion", data["claims"]["minimality_is_mathematical_theorem"] == "NO")
    print("PASS ALL")

if __name__ == "__main__":
    main()
