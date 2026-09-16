from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert version == "1.0.0"

    manifest_path = ROOT / "results" / "v1_0_freeze_manifest.json"
    manifest = load_json(manifest_path)
    assert manifest["schema"] == "INFINITIES_V1_0_FREEZE_MANIFEST"
    assert manifest["version"] == version

    for relative in manifest["required_documents"]:
        path = ROOT / relative
        assert path.is_file(), f"missing required document: {relative}"

    for relative, expected in manifest["required_result_expectations"].items():
        path = ROOT / relative
        assert path.is_file(), f"missing required result: {relative}"
        result = load_json(path)
        if relative.endswith("gremlin_sweep_v0_1_result.json"):
            claims = result["claims"]
            for key, value in expected.items():
                assert claims[key] == value, (relative, key, claims[key], value)
        else:
            for key, value in expected.items():
                assert result[key] == value, (relative, key, result[key], value)

    invariants = manifest["freeze_invariants"]
    assert invariants["all_required_result_expectations_must_match"] is True
    assert invariants["intentional_negative_results_are_preserved"] is True
    assert invariants["riemann_hypothesis_proof_claim"] is False
    assert invariants["collatz_proof_claim"] is False
    assert invariants["twin_prime_proof_claim"] is False
    assert invariants["universal_fourth_operator_claim"] is False
    assert invariants["universal_bmf_bmcf_completeness_claim"] is False
    assert invariants["novelty_claim_without_literature_audit"] is False
    assert invariants["open_boundaries_are_allowed_if_explicitly_typed"] is True

    claims = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    release = (ROOT / "INFINITIES_V1_0.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    required_claim_tokens = (
        "INF-053",
        "NOT ESTABLISHED / NOT CLAIMED",
        "FORBIDDEN PROMOTION",
        "No result here proves the Riemann Hypothesis",
    )
    for token in required_claim_tokens:
        assert token in claims, f"missing claims firewall token: {token}"

    required_release_tokens = (
        "v1.0 COMPLETE",
        "It does **not** mean",
        "Riemann Hypothesis",
        "Collatz conjecture",
        "Twin Prime conjecture",
        "intentional FAIL results",
    )
    for token in required_release_tokens:
        assert token in release, f"missing release firewall token: {token}"

    assert "v1.0" in readme.lower(), "README must expose v1.0 freeze status"
    assert "does **not** claim" in readme, "README must retain open-problem disclaimer"

    # Preserve the two intentional falsification outcomes rather than laundering
    # them into release-green PASS labels.
    gremlin = load_json(ROOT / "results" / "gremlin_sweep_v0_1_result.json")
    assert gremlin["claims"]["baseline_generalizes_to_all_holdouts"] == "FAIL"
    assert gremlin["claims"]["universal_half_seam"] == "FAIL"

    final_boundary = load_json(ROOT / "results" / "bmcf_final_boundary_v0_10_result.json")
    assert final_boundary["claims"]["single_universal_fourth_operator"] == "NOT_ESTABLISHED"

    print("PASS Infinities v1.0 freeze controls")


if __name__ == "__main__":
    main()
