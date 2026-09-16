from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infinities.bmcf_final_boundary import (
    equivalence_matrix_to_partition,
    full_permutation_equivariant_selector_exists,
    inflationary_maps,
    iterate_to_fixed,
    ordered_min_selector,
    partition_to_equivalence_matrix,
    set_partitions,
)


def main():
    expected_map_counts = {1: 2, 2: 16, 3: 4096}
    for nbits, expected in expected_map_counts.items():
        maps = tuple(inflationary_maps(nbits))
        assert len(maps) == expected
        for mapping in maps:
            for start in range(1 << nbits):
                orbit, strict = iterate_to_fixed(mapping, start)
                assert orbit[-1] == orbit[-2]
                assert strict <= nbits

    expected_bell = {0: 1, 1: 1, 2: 2, 3: 5, 4: 15, 5: 52}
    for n, expected in expected_bell.items():
        partitions = tuple(set_partitions(n))
        assert len(partitions) == expected
        matrices = set()
        for partition in partitions:
            matrix = partition_to_equivalence_matrix(partition, n)
            matrices.add(matrix)
            assert equivalence_matrix_to_partition(matrix) == partition
        assert len(matrices) == expected

    for n in range(2, 8):
        assert not full_permutation_equivariant_selector_exists(n)
    assert ordered_min_selector((4, 2, 9)) == 2

    try:
        ordered_min_selector(())
    except ValueError:
        pass
    else:
        raise AssertionError("empty ordered selector must fail closed")

    output = subprocess.check_output(
        [sys.executable, str(ROOT / "computations" / "bmcf_final_boundary_v0_10.py")],
        text=True,
    )
    result = json.loads(output)
    assert result["overall_status"] == "PASS"
    assert result["claims"]["finite_inflationary_boolean_fix_has_bounded_horizon"] == "EXACT_THEOREM"
    assert result["claims"]["finite_reachability_fix_requires_independent_primitive"] == "NO_NOT_ESTABLISHED_BOUNDED_UNROLLING_EXISTS"
    assert result["claims"]["finite_partition_has_fixed_carrier_equivalence_representation"] == "EXACT_THEOREM"
    assert result["claims"]["bare_finite_set_equivariant_selector_exists_for_n_ge_2"] == "NO_EXACT_THEOREM"
    assert result["claims"]["single_universal_fourth_operator"] == "NOT_ESTABLISHED"

    print("PASS BMCF v0.10 final typed-boundary controls")


if __name__ == "__main__":
    main()
