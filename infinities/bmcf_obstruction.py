from __future__ import annotations

from typing import Callable, Sequence, TypeVar

S = TypeVar("S")


def couple_activation_required(total_degree: int) -> bool:
    """Return whether polynomial dynamic degree forces at least one COUPLE.

    Degree -1 is allowed for the zero polynomial. Constants and affine/linear
    targets do not require dynamic-dynamic multiplication in the polynomial
    grammar when a fixed unit/scalar source is available.
    """
    return total_degree > 1


def minimal_couple_depth_for_degree(total_degree: int) -> int:
    """Exact binary-COUPLE nesting depth required by total degree.

    In the finite polynomial grammar with degree-1 dynamic generators, fixed
    scalars, BRANCH, scalar MAP, finite additive FOLD, and binary multiplicative
    COUPLE, a nonzero target of degree d requires and admits depth ceil(log2 d).
    Zero/constant/linear targets have depth 0.
    """
    if total_degree <= 1:
        return 0
    return (total_degree - 1).bit_length()


def degree_upper_bound_from_couple_depth(couple_depth: int) -> int:
    """Maximum dynamic total degree reachable at a given COUPLE nesting depth."""
    if couple_depth < 0:
        raise ValueError("couple_depth must be nonnegative")
    return 1 << couple_depth


def balanced_couple(
    values: Sequence[S],
    mul: Callable[[S, S], S],
    one: S,
) -> tuple[S, int]:
    """Multiply an ordered word with balanced binary COUPLE depth.

    Pairing preserves left-to-right order. Associativity of `mul` is required
    for equivalence with ordinary ordered word multiplication.
    """
    level = list(values)
    if not level:
        return one, 0
    depth = 0
    while len(level) > 1:
        nxt: list[S] = []
        it = iter(level)
        for left in it:
            try:
                right = next(it)
            except StopIteration:
                nxt.append(left)
                break
            nxt.append(mul(left, right))
        level = nxt
        depth += 1
    return level[0], depth


def minimal_binary_product_depth_dp(total_degree: int) -> int:
    """Independent finite DP witness for minimal binary multiplication depth."""
    if total_degree <= 1:
        return 0
    depth = [0] * (total_degree + 1)
    for d in range(2, total_degree + 1):
        depth[d] = 1 + min(max(depth[a], depth[d - a]) for a in range(1, d))
    return depth[total_degree]
