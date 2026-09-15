from __future__ import annotations

import cmath
import hashlib
import json
import math
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmf import (
    Semiring,
    canonical_selector_exists_on_bare_finite_set,
    direct_kernel_transform,
    kernel_transform,
)

SEED = 20260915
FLOAT = Semiring[complex](
    add=lambda a, b: a + b,
    mul=lambda a, b: a * b,
    zero=0j,
    one=1 + 0j,
)
BOOL = Semiring[bool](
    add=lambda a, b: a or b,
    mul=lambda a, b: a and b,
    zero=False,
    one=True,
)


def max_abs_error(a, b) -> float:
    return max((abs(complex(a[k]) - complex(b[k])) for k in a), default=0.0)


def dft_case(n: int) -> float:
    values = {x: complex((x + 1) / n, (-1) ** x / (n + 1)) for x in range(n)}
    outputs = tuple(range(n))
    kernel = {
        (k, x): cmath.exp(-2j * math.pi * k * x / n)
        for k in outputs for x in values
    }
    bmf = kernel_transform(values, outputs, kernel, FLOAT)
    direct = direct_kernel_transform(values, outputs, kernel, FLOAT)
    return max_abs_error(bmf, direct)


def markov_case(rng: random.Random, n: int = 5) -> float:
    rows = []
    for _ in range(n):
        raw = [rng.random() + 0.01 for _ in range(n)]
        total = sum(raw)
        rows.append([x / total for x in raw])
    state_raw = [rng.random() + 0.01 for _ in range(n)]
    state_sum = sum(state_raw)
    state = {i: complex(state_raw[i] / state_sum) for i in range(n)}
    outputs = tuple(range(n))
    kernel = {(y, x): complex(rows[x][y]) for y in outputs for x in state}
    bmf = kernel_transform(state, outputs, kernel, FLOAT)
    direct = {
        y: sum(state[x] * kernel[(y, x)] for x in state)
        for y in outputs
    }
    return max_abs_error(bmf, direct)


def boolean_adjacency_case() -> bool:
    state = {0: True, 1: False, 2: True, 3: False}
    outputs = tuple(range(4))
    edges = {(0, 1), (2, 1), (2, 3), (3, 0)}
    kernel = {(y, x): (x, y) in edges for y in outputs for x in state}
    return kernel_transform(state, outputs, kernel, BOOL) == direct_kernel_transform(
        state, outputs, kernel, BOOL
    )


def divisibility_zeta_case(n: int = 30) -> bool:
    values = {d: complex((d % 7) - 3) for d in range(1, n + 1)}
    outputs = tuple(range(1, n + 1))
    kernel = {(m, d): (1 + 0j if m % d == 0 else 0j) for m in outputs for d in values}
    bmf = kernel_transform(values, outputs, kernel, FLOAT)
    direct = {m: sum(values[d] for d in values if m % d == 0) for m in outputs}
    return max_abs_error(bmf, direct) == 0.0


def walsh_hadamard_case(bits: int = 3) -> float:
    n = 1 << bits
    values = {x: complex((3 * x + 1) % 11 - 5) for x in range(n)}
    outputs = tuple(range(n))

    def parity(z: int) -> int:
        return z.bit_count() & 1

    kernel = {(y, x): complex(-1 if parity(x & y) else 1) for y in outputs for x in values}
    bmf = kernel_transform(values, outputs, kernel, FLOAT)
    direct = direct_kernel_transform(values, outputs, kernel, FLOAT)
    return max_abs_error(bmf, direct)


def dirichlet_convolution_case(n: int = 40) -> bool:
    f = {d: complex((d % 5) - 2) for d in range(1, n + 1)}
    g = {d: complex((2 * d + 1) % 7 - 3) for d in range(1, n + 1)}
    outputs = tuple(range(1, n + 1))
    kernel = {
        (m, d): (g[m // d] if m % d == 0 else 0j)
        for m in outputs for d in f
    }
    bmf = kernel_transform(f, outputs, kernel, FLOAT)
    direct = {
        m: sum(f[d] * g[m // d] for d in f if m % d == 0)
        for m in outputs
    }
    return max_abs_error(bmf, direct) == 0.0


def tensor_contraction_case(rng: random.Random, m: int = 4, k: int = 5, n: int = 3) -> float:
    a = [[rng.uniform(-2, 2) for _ in range(k)] for _ in range(m)]
    b = [[rng.uniform(-2, 2) for _ in range(n)] for _ in range(k)]
    values = {r: complex(1.0) for r in range(k)}
    outputs = tuple((i, j) for i in range(m) for j in range(n))
    kernel = {
        ((i, j), r): complex(a[i][r] * b[r][j])
        for i, j in outputs for r in values
    }
    bmf = kernel_transform(values, outputs, kernel, FLOAT)
    direct = {
        (i, j): sum(a[i][r] * b[r][j] for r in range(k))
        for i, j in outputs
    }
    return max_abs_error(bmf, direct)


def selector_obstruction() -> dict[str, object]:
    counts = {
        str(n): int(canonical_selector_exists_on_bare_finite_set(tuple(range(n))))
        for n in range(2, 6)
    }
    return {
        "sizes": [2, 3, 4, 5],
        "equivariant_selector_exists": counts,
        "status": "PASS" if all(v == 0 for v in counts.values()) else "FAIL",
        "claim_scope": "FINITE_BARE_SET_FULL_PERMUTATION_EQUIVARIANCE_ONLY",
    }


def main() -> None:
    rng = random.Random(SEED)
    dft_errors = {str(n): dft_case(n) for n in (2, 3, 5, 8)}
    markov_error = markov_case(rng)
    walsh_error = walsh_hadamard_case()
    tensor_error = tensor_contraction_case(rng)

    result = {
        "schema": "INFINITIES_BMF_OOD_RESULT_V0_4",
        "seed": SEED,
        "kernel_factorization": "T_K = F_add o M_K o B",
        "infinite_scope_note": (
            "All executable checks are finite witnesses. Infinite folds additionally require "
            "explicit topology/completion/convergence assumptions."
        ),
        "tests": {
            "dft": {
                "status": "PASS" if max(dft_errors.values()) < 1e-12 else "FAIL",
                "max_abs_error_by_n": dft_errors,
            },
            "markov": {
                "status": "PASS" if markov_error < 1e-12 else "FAIL",
                "max_abs_error": markov_error,
            },
            "boolean_adjacency": {"status": "PASS" if boolean_adjacency_case() else "FAIL"},
            "divisibility_zeta": {"status": "PASS" if divisibility_zeta_case() else "FAIL"},
            "walsh_hadamard": {
                "status": "PASS" if walsh_error < 1e-12 else "FAIL",
                "max_abs_error": walsh_error,
            },
            "dirichlet_convolution": {
                "status": "PASS" if dirichlet_convolution_case() else "FAIL"
            },
            "tensor_contraction": {
                "status": "PASS" if tensor_error < 1e-12 else "FAIL",
                "max_abs_error": tensor_error,
            },
            "selector_symmetry_obstruction": selector_obstruction(),
        },
        "claims": {
            "finite_kernel_operators_factor_through_bmf_by_construction": "EXACT",
            "all_infinity_mathematics_is_bmf": "NOT_CLAIMED",
            "canonical_bmf_is_universally_complete": "NOT_CLAIMED",
            "choice_like_witness_selection_is_reducible_to_bmf_without_extra_structure": "NOT_CLAIMED",
            "rh_proof": "NO",
            "collatz_proof": "NO",
        },
    }
    result["overall_status"] = (
        "PASS"
        if all(test["status"] == "PASS" for test in result["tests"].values())
        else "FAIL"
    )
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    result["result_sha256_without_self_hash"] = hashlib.sha256(canonical).hexdigest()

    out = ROOT / "results" / "bmf_ood_v0_4_result.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    main()
