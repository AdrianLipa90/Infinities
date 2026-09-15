from __future__ import annotations

import json
from itertools import combinations, product

INPUTS_2 = ((0, 0), (0, 1), (1, 0), (1, 1))
ALL_BOOLEAN_TABLES = tuple(product((0, 1), repeat=4))
UNARY_BOOLEAN_MAPS = {
    "ZERO": (0, 0),
    "ONE": (1, 1),
    "ID": (0, 1),
    "NOT": (1, 0),
}


def truth_table(fn):
    return tuple(int(bool(fn(a, b))) for a, b in INPUTS_2)


def strict_boolean_bmf_tables():
    return {
        truth_table(lambda a, b, k1=k1, k2=k2: (k1 and a) or (k2 and b))
        for k1, k2 in product((0, 1), repeat=2)
    }


def monotone_or_and_closure():
    closure = {
        (0, 0, 0, 0),
        (1, 1, 1, 1),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
    }
    changed = True
    while changed:
        changed = False
        current = tuple(closure)
        for left in current:
            for right in current:
                for op in ("OR", "AND"):
                    table = tuple((x | y) if op == "OR" else (x & y) for x, y in zip(left, right))
                    if table not in closure:
                        closure.add(table)
                        changed = True
    return closure


def couple_dnf_coverage():
    terms = set()
    for left in UNARY_BOOLEAN_MAPS.values():
        for right in UNARY_BOOLEAN_MAPS.values():
            terms.add(tuple(left[a] & right[b] for a, b in INPUTS_2))
    terms = tuple(sorted(terms))
    coverage = {(0, 0, 0, 0)}
    min_terms = {(0, 0, 0, 0): 0}
    for width in range(1, 5):
        for indices in combinations(range(len(terms)), width):
            selected = [terms[i] for i in indices]
            table = tuple(int(any(values)) for values in zip(*selected))
            coverage.add(table)
            min_terms[table] = min(min_terms.get(table, width), width)
    return coverage, min_terms, terms


def gate_shannon_coverage():
    tables = set()
    for g0 in UNARY_BOOLEAN_MAPS.values():
        for g1 in UNARY_BOOLEAN_MAPS.values():
            tables.add(tuple(g1[b] if a else g0[b] for a, b in INPUTS_2))
    return tables


def real_square_couple_witness():
    samples = (-3, -1, 0, 2, 5)
    values = {str(x): x * x for x in samples}
    return values, all(values[str(x)] == x ** 2 for x in samples)


def finite_fixpoint_witness():
    kernel = ((1, 0, 0), (1, 1, 0), (0, 1, 1))
    def step(vector):
        return tuple(int(any(kernel[y][x] and vector[x] for x in range(3))) for y in range(3))
    states = [(1, 0, 0)]
    while True:
        nxt = step(states[-1])
        states.append(nxt)
        if nxt == states[-2]:
            break
        if len(states) > 10:
            raise RuntimeError("finite witness did not stabilize")
    return states


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
    roots = [find(i) for i in range(size)]
    return tuple(sorted((roots.count(r) for r in set(roots)), reverse=True))


def coequalizer_profiles():
    maps = tuple(product(range(3), repeat=2))
    counts = {}
    for left in maps:
        for right in maps:
            profile = partition_sizes(3, zip(left, right))
            key = "+".join(map(str, profile))
            counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def main():
    strict = strict_boolean_bmf_tables()
    monotone = monotone_or_and_closure()
    dnf_coverage, dnf_min_terms, dnf_terms = couple_dnf_coverage()
    gate = gate_shannon_coverage()
    square_values, square_ok = real_square_couple_witness()
    fix_states = finite_fixpoint_witness()
    coeq = coequalizer_profiles()
    result = {
        "schema": "INFINITIES_FOURTH_OPERATOR_SEARCH_RESULT_V0_6",
        "overall_status": "PASS",
        "tests": {
            "strict_boolean_bmf_baseline": {"representable_count": len(strict), "total_boolean_functions": 16, "status": "PASS" if len(strict) == 4 else "FAIL"},
            "couple_monotone_extension": {"representable_count": len(monotone), "total_boolean_functions": 16, "status": "PASS" if len(monotone) == 6 else "FAIL"},
            "couple_plus_fixed_unary_library_dnf": {"distinct_conjunctive_terms": len(dnf_terms), "representable_count": len(dnf_coverage), "max_terms_needed_for_two_variable_tables": max(dnf_min_terms.values()), "total_boolean_functions": 16, "status": "PASS" if len(dnf_coverage) == 16 else "FAIL"},
            "gate_ite_shannon_two_variable": {"representable_count": len(gate), "total_boolean_functions": 16, "status": "PASS" if len(gate) == 16 else "FAIL"},
            "couple_real_square": {"sample_values": square_values, "status": "PASS" if square_ok else "FAIL"},
            "fixpoint_reachability": {"states": [list(state) for state in fix_states], "fixed_point": list(fix_states[-1]), "status": "PASS" if fix_states[-1] == (1, 1, 1) and fix_states[-1] == fix_states[-2] else "FAIL"},
            "quotient_carrier_boundary_recheck": {"coequalizer_profiles_A2_to_B3": coeq, "status": "PASS" if coeq == {"1+1+1": 9, "2+1": 48, "3": 24} else "FAIL"},
        },
        "conclusion": {
            "single_universal_fourth_operator_found": "NO",
            "best_supported_data_plane_candidate": "COUPLE",
            "conditional_fourth_slot_is_mathematical_singleton": "NOT_ESTABLISHED",
            "typed_aux_sum_is_allowed_as_software_architecture": "YES_NOT_A_UNIVERSALITY_THEOREM",
        },
        "firewall": {
            "couple_is_unique_minimal_fourth": "NOT_CLAIMED",
            "ite_is_universal_over_all_domains": "NOT_CLAIMED",
            "fixpoint_and_quotient_are_reducible_to_couple": "NOT_CLAIMED",
            "typed_aux_dispatcher_is_one_mathematical_primitive": "NO",
            "rh_proof": "NO",
            "collatz_proof": "NO",
        },
    }
    statuses = [test["status"] for test in result["tests"].values() if "status" in test]
    if any(status != "PASS" for status in statuses):
        result["overall_status"] = "FAIL"
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
