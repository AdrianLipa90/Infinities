from __future__ import annotations

import json
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmcf_final_boundary import (
    directed_graph_masks,
    equivalence_matrix_to_partition,
    full_permutation_equivariant_selector_exists,
    inflationary_maps,
    iterate_to_fixed,
    ordered_min_selector,
    partition_to_equivalence_matrix,
    reachability_bfs_reference,
    reachability_fixed_point,
    set_partitions,
)


def exhaustive_inflationary_map_trials():
    expected_counts = {1: 2, 2: 16, 3: 4096}
    rows = {}
    overall = True
    for nbits in (1, 2, 3):
        count = 0
        max_strict = 0
        for mapping in inflationary_maps(nbits):
            count += 1
            for start in range(1 << nbits):
                orbit, strict = iterate_to_fixed(mapping, start)
                max_strict = max(max_strict, strict)
                if strict > nbits or orbit[-1] != orbit[-2]:
                    overall = False
        rows[str(nbits)] = {
            "map_count": count,
            "expected_map_count": expected_counts[nbits],
            "max_strict_changes": max_strict,
            "bound": nbits,
            "status": "PASS" if count == expected_counts[nbits] and max_strict <= nbits else "FAIL",
        }
        overall = overall and rows[str(nbits)]["status"] == "PASS"
    return overall, rows


def exhaustive_reachability_trials(max_n: int = 4):
    rows = {}
    overall = True
    for n in range(1, max_n + 1):
        possible_edges = directed_graph_masks(n)
        graph_count = 0
        max_strict = 0
        for edge_bits in range(1 << len(possible_edges)):
            edges = {
                edge
                for index, edge in enumerate(possible_edges)
                if edge_bits & (1 << index)
            }
            graph_count += 1
            for seed in range(n):
                orbit, strict = reachability_fixed_point(n, edges, 1 << seed)
                reference = reachability_bfs_reference(n, edges, seed)
                max_strict = max(max_strict, strict)
                if orbit[-1] != reference or strict > n - 1:
                    overall = False
        rows[str(n)] = {
            "graph_count": graph_count,
            "expected_graph_count": 2 ** (n * (n - 1)),
            "max_strict_changes": max_strict,
            "bound": max(0, n - 1),
            "status": "PASS" if graph_count == 2 ** (n * (n - 1)) and max_strict <= max(0, n - 1) else "FAIL",
        }
        overall = overall and rows[str(n)]["status"] == "PASS"
    return overall, rows


def partition_roundtrip_trials(max_n: int = 5):
    bell = {0: 1, 1: 1, 2: 2, 3: 5, 4: 15, 5: 52}
    rows = {}
    overall = True
    for n in range(max_n + 1):
        partitions = tuple(set_partitions(n))
        matrices = set()
        roundtrip_ok = True
        for partition in partitions:
            matrix = partition_to_equivalence_matrix(partition, n)
            matrices.add(matrix)
            recovered = equivalence_matrix_to_partition(matrix)
            if recovered != partition:
                roundtrip_ok = False
        status = len(partitions) == bell[n] and len(matrices) == bell[n] and roundtrip_ok
        rows[str(n)] = {
            "partition_count": len(partitions),
            "equivalence_matrix_count": len(matrices),
            "expected_bell_count": bell[n],
            "roundtrip_exact": roundtrip_ok,
            "status": "PASS" if status else "FAIL",
        }
        overall = overall and status
    return overall, rows


def selector_trials():
    bare = {}
    overall = True
    for n in range(2, 8):
        exists = full_permutation_equivariant_selector_exists(n)
        bare[str(n)] = exists
        overall = overall and not exists
    ordered_examples = {
        "3,1,2": ordered_min_selector((3, 1, 2)),
        "9,-4,7": ordered_min_selector((9, -4, 7)),
    }
    overall = overall and ordered_examples == {"3,1,2": 1, "9,-4,7": -4}
    return overall, bare, ordered_examples


def main():
    inflationary_ok, inflationary_rows = exhaustive_inflationary_map_trials()
    reachability_ok, reachability_rows = exhaustive_reachability_trials()
    partition_ok, partition_rows = partition_roundtrip_trials()
    selector_ok, bare_selector, ordered_examples = selector_trials()

    tests = {
        "exhaustive_inflationary_boolean_fixed_points": {
            "status": "PASS" if inflationary_ok else "FAIL",
            "dimensions": inflationary_rows,
        },
        "exhaustive_finite_reachability_unrolling": {
            "status": "PASS" if reachability_ok else "FAIL",
            "dimensions": reachability_rows,
        },
        "finite_partition_equivalence_roundtrip": {
            "status": "PASS" if partition_ok else "FAIL",
            "dimensions": partition_rows,
        },
        "bare_selector_symmetry_and_ordered_repair": {
            "status": "PASS" if selector_ok else "FAIL",
            "bare_equivariant_selector_exists": bare_selector,
            "ordered_min_examples": ordered_examples,
        },
    }
    overall = "PASS" if all(test["status"] == "PASS" for test in tests.values()) else "FAIL"
    result = {
        "schema": "INFINITIES_BMCF_FINAL_BOUNDARY_RESULT_V0_10",
        "overall_status": overall,
        "tests": tests,
        "claims": {
            "finite_inflationary_boolean_fix_has_bounded_horizon": "EXACT_THEOREM",
            "finite_reachability_fix_requires_independent_primitive": "NO_NOT_ESTABLISHED_BOUNDED_UNROLLING_EXISTS",
            "finite_partition_has_fixed_carrier_equivalence_representation": "EXACT_THEOREM",
            "quotient_is_representation_independent_fourth_primitive": "NO_NOT_ESTABLISHED",
            "bare_finite_set_equivariant_selector_exists_for_n_ge_2": "NO_EXACT_THEOREM",
            "order_supplies_selector_structure": "YES",
            "single_universal_fourth_operator": "NOT_ESTABLISHED",
            "typed_aux_architecture": "SUPPORTED_AS_SOFTWARE_AND_TYPE_DISCIPLINE_NOT_UNIVERSALITY_THEOREM",
            "rh_proof": "NO",
            "collatz_proof": "NO",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if overall != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
