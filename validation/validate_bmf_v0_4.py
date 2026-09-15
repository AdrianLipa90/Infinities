from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_bmf():
    path = ROOT / "infinities" / "bmf.py"
    spec = importlib.util.spec_from_file_location("infinities_bmf_v04", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_exact_small_kernel(bmf):
    semiring = bmf.Semiring(add=lambda a, b: a + b, mul=lambda a, b: a * b, zero=0, one=1)
    values = {"a": 2, "b": 3}
    outputs = ("u", "v")
    kernel = {
        ("u", "a"): 5, ("u", "b"): 7,
        ("v", "a"): 11, ("v", "b"): 13,
    }
    got = bmf.kernel_transform(values, outputs, kernel, semiring)
    assert got == {"u": 31, "v": 61}
    assert got == bmf.direct_kernel_transform(values, outputs, kernel, semiring)


def test_selector_obstruction(bmf):
    for n in range(2, 6):
        xs = tuple(range(n))
        assert bmf.equivariant_distinguished_elements(xs) == ()
        assert bmf.canonical_selector_exists_on_bare_finite_set(xs) is False
    assert bmf.ordered_select_min([5, 2, 9]) == 2


def run_ood_computation():
    target = ROOT / "computations" / "bmf_ood_v0_4.py"
    subprocess.run([sys.executable, str(target)], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    payload = json.loads((ROOT / "results" / "bmf_ood_v0_4_result.json").read_text(encoding="utf-8"))
    assert payload["schema"] == "INFINITIES_BMF_OOD_RESULT_V0_4"
    assert payload["overall_status"] == "PASS"
    assert payload["claims"]["all_infinity_mathematics_is_bmf"] == "NOT_CLAIMED"
    assert payload["claims"]["rh_proof"] == "NO"
    assert payload["claims"]["collatz_proof"] == "NO"
    return payload


def main():
    bmf = load_bmf()
    test_exact_small_kernel(bmf)
    print("PASS exact finite kernel factorization")
    test_selector_obstruction(bmf)
    print("PASS finite selector symmetry obstruction")
    payload = run_ood_computation()
    for name, result in payload["tests"].items():
        print(f"{result['status']} {name}")
    print("PASS ALL")


if __name__ == "__main__":
    main()
