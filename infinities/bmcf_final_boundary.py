from __future__ import annotations

from itertools import product, permutations
from typing import Iterable, Sequence


def supersets(state: int, nbits: int) -> tuple[int, ...]:
    full = (1 << nbits) - 1
    missing = full ^ state
    bits = [1 << index for index in range(nbits) if missing & (1 << index)]
    out = []
    for mask in range(1 << len(bits)):
        value = state
        for index, bit in enumerate(bits):
            if mask & (1 << index):
                value |= bit
        out.append(value)
    return tuple(out)


def inflationary_maps(nbits: int):
    """Enumerate all maps F on {0,1}^n satisfying x <= F(x)."""
    states = tuple(range(1 << nbits))
    choices = [supersets(state, nbits) for state in states]
    for outputs in product(*choices):
        yield outputs


def iterate_to_fixed(mapping: Sequence[int], start: int, max_steps: int = 10_000):
    state = start
    orbit = [state]
    strict_changes = 0
    for _ in range(max_steps):
        nxt = mapping[state]
        orbit.append(nxt)
        if nxt == state:
            return tuple(orbit), strict_changes
        strict_changes += 1
        state = nxt
    raise RuntimeError("iteration did not stabilize within max_steps")


def directed_graph_masks(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((source, target) for source in range(n) for target in range(n) if source != target)


def reachability_step(n: int, edges: set[tuple[int, int]], state: int) -> int:
    out = state
    for source, target in edges:
        if state & (1 << source):
            out |= 1 << target
    return out


def reachability_fixed_point(n: int, edges: set[tuple[int, int]], start: int):
    state = start
    orbit = [state]
    strict_changes = 0
    while True:
        nxt = reachability_step(n, edges, state)
        orbit.append(nxt)
        if nxt == state:
            return tuple(orbit), strict_changes
        strict_changes += 1
        state = nxt


def reachability_bfs_reference(n: int, edges: set[tuple[int, int]], seed: int) -> int:
    seen = {seed}
    changed = True
    while changed:
        changed = False
        for source, target in edges:
            if source in seen and target not in seen:
                seen.add(target)
                changed = True
    mask = 0
    for vertex in seen:
        mask |= 1 << vertex
    return mask


def set_partitions(n: int):
    """Canonical set partitions of range(n) as tuples of sorted blocks."""
    if n == 0:
        yield ()
        return

    blocks: list[list[int]] = []

    def rec(value: int):
        if value == n:
            yield tuple(tuple(block) for block in blocks)
            return
        for index in range(len(blocks)):
            blocks[index].append(value)
            yield from rec(value + 1)
            blocks[index].pop()
        blocks.append([value])
        yield from rec(value + 1)
        blocks.pop()

    blocks.append([0])
    yield from rec(1)


def partition_to_equivalence_matrix(partition: Sequence[Sequence[int]], n: int) -> tuple[tuple[int, ...], ...]:
    block_of: dict[int, int] = {}
    for block_index, block in enumerate(partition):
        for value in block:
            if value in block_of:
                raise ValueError("partition contains duplicate element")
            block_of[value] = block_index
    if set(block_of) != set(range(n)):
        raise ValueError("partition does not cover carrier")
    return tuple(
        tuple(int(block_of[i] == block_of[j]) for j in range(n))
        for i in range(n)
    )


def equivalence_matrix_to_partition(matrix: Sequence[Sequence[int]]):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    unassigned = set(range(n))
    blocks = []
    while unassigned:
        root = min(unassigned)
        block = tuple(index for index in range(n) if matrix[root][index])
        if not block:
            raise ValueError("matrix is not reflexive")
        blocks.append(block)
        unassigned.difference_update(block)
    return tuple(blocks)


def full_permutation_equivariant_selector_exists(n: int) -> bool:
    """Finite exhaustive witness for bare-set selector obstruction."""
    if n <= 0:
        return False
    carrier = tuple(range(n))
    all_perms = tuple(permutations(carrier))
    for candidate in carrier:
        if all(perm[candidate] == candidate for perm in all_perms):
            return True
    return False


def ordered_min_selector(carrier: Iterable[int]) -> int:
    values = tuple(carrier)
    if not values:
        raise ValueError("cannot select from empty carrier")
    return min(values)
