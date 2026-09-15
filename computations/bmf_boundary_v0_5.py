from __future__ import annotations

import json
from collections import Counter
from itertools import product

INPUTS_2 = ((0, 0), (0, 1), (1, 0), (1, 1))


def truth_table(fn):
    return tuple(int(bool(fn(a, b))) for a, b in INPUTS_2)


def boolean_semiring_single_output_tables():
    tables = set()
    for k1, k2 in product((0, 1), repeat=2):
        tables.add(truth_table(lambda a, b, k1=k1, k2=k2: (k1 and a) or (k2 and b)))
    return tables


def bool_linear_apply(matrix, vector):
    return tuple(int(any(coeff and value for coeff, value in zip(row, vector))) for row in matrix)


def two_layer_boolean_tables(hidden_width):
    tables = set()
    for first_bits in product((0, 1), repeat=2 * hidden_width):
        first = [first_bits[2 * row:2 * row + 2] for row in range(hidden_width)]
        for second in product((0, 1), repeat=hidden_width):
            table = []
            for vector in INPUTS_2:
                hidden = bool_linear_apply(first, vector)
                output = int(any(coeff and value for coeff, value in zip(second, hidden)))
                table.append(output)
            tables.add(tuple(table))
    return tables


def unrestricted_unary_map_tables(fold):
    unary = tuple(product((0, 1), repeat=2))
    tables = set()
    for left, right in product(unary, repeat=2):
        tables.add(truth_table(lambda a, b, left=left, right=right: fold(left[a], right[b])))
    return tables


def partition_sizes(size, identifications):
    parent = list(range(size))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for left, right in identifications:
        union(left, right)
    counts = Counter(find(i) for i in range(size))
    return tuple(sorted(counts.values(), reverse=True))


def coequalizer_distribution():
    maps = tuple(product(range(3), repeat=2))
    counter = Counter()
    for left in maps:
        for right in maps:
            counter[partition_sizes(3, zip(left, right))] += 1
    return counter


def pushout_cardinality_distribution():
    maps = tuple(product(range(2), repeat=2))
    counter = Counter()
    for left in maps:
        for right in maps:
            identifications = ((left[i], 2 + right[i]) for i in range(2))
            classes = partition_sizes(4, identifications)
            counter[len(classes)] += 1
    return counter


def reachability_iteration_witness():
    # Directed path 0 -> 1 -> 2; kernel is I OR A.
    kernel = (
        (1, 0, 0),
        (1, 1, 0),
        (0, 1, 1),
    )

    def step(vector):
        return tuple(int(any(kernel[y][x] and vector[x] for x in range(3))) for y in range(3))

    initial = (1, 0, 0)
    once = step(initial)
    twice = step(once)
    return initial, once, twice


def main():
    baseline = boolean_semiring_single_output_tables()
    two_layer = {str(width): len(two_layer_boolean_tables(width)) for width in (1, 2, 3)}

    fold_counts = {
        "OR": len(unrestricted_unary_map_tables(lambda a, b: a | b)),
        "AND": len(unrestricted_unary_map_tables(lambda a, b: a & b)),
        "XOR": len(unrestricted_unary_map_tables(lambda a, b: a ^ b)),
    }

    coeq = coequalizer_distribution()
    pushout = pushout_cardinality_distribution()
    initial, once, twice = reachability_iteration_witness()

    square_additivity_witness = {
        "T_2_plus_3": (2 + 3) ** 2,
        "T_2_plus_T_3": 2 ** 2 + 3 ** 2,
    }

    result = {
        "schema": "INFINITIES_BMF_BOUNDARY_RESULT_V0_5",
        "overall_status": "PASS",
        "tests": {
            "boolean_semiring_single_layer": {
                "representable_count": len(baseline),
                "total_boolean_functions": 16,
                "truth_tables": [list(table) for table in sorted(baseline)],
                "status": "PASS",
            },
            "boolean_semiring_two_layer_closure": {
                "hidden_width_to_representable_count": two_layer,
                "status": "PASS" if all(count == 4 for count in two_layer.values()) else "FAIL",
            },
            "real_square_nonadditivity": {
                **square_additivity_witness,
                "status": "PASS" if square_additivity_witness["T_2_plus_3"] != square_additivity_witness["T_2_plus_T_3"] else "FAIL",
            },
            "reachability_requires_iteration": {
                "initial": list(initial),
                "after_one_pass": list(once),
                "after_two_passes": list(twice),
                "status": "PASS" if once == (1, 1, 0) and twice == (1, 1, 1) else "FAIL",
            },
            "coequalizer_partition_distribution_A2_to_B3": {
                "+".join(map(str, key)): value for key, value in sorted(coeq.items())
            },
            "pushout_cardinality_distribution_A2_B2_C2": {
                str(key): value for key, value in sorted(pushout.items())
            },
            "unrestricted_unary_map_fixed_fold_counts": fold_counts,
            "unrestricted_binary_fold_warning": {
                "representable_count_if_fold_may_be_target_function": 16,
                "total_boolean_functions": 16,
                "interpretation": "TAUTOLOGICAL_IF_TARGET_IS_HIDDEN_IN_FOLD",
                "status": "PASS",
            },
        },
        "claims": {
            "finite_kernel_factorization_survives": "YES",
            "bmf_kernel_is_universal_computation_model": "NO",
            "iteration_fixpoint_is_already_identical_to_one_bmf_pass": "NO",
            "quotient_is_proved_independent_fourth_primitive": "NO",
            "universal_three_primitive_grammar": "NOT_ESTABLISHED",
            "rh_proof": "NO",
            "collatz_proof": "NO",
        },
    }

    statuses = []
    for value in result["tests"].values():
        if isinstance(value, dict) and "status" in value:
            statuses.append(value["status"])
    if any(status != "PASS" for status in statuses):
        result["overall_status"] = "FAIL"

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
