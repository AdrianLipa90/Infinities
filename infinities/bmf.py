from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from typing import Callable, Generic, Iterable, Mapping, Sequence, TypeVar

X = TypeVar("X")
Y = TypeVar("Y")
S = TypeVar("S")


@dataclass(frozen=True)
class Semiring(Generic[S]):
    """Minimal semiring-like operations needed by the BMF kernel factorization.

    No algebraic laws are inferred at runtime. Callers are responsible for using
    operations with the laws required by their mathematical setting.
    """

    add: Callable[[S, S], S]
    mul: Callable[[S, S], S]
    zero: S
    one: S


def branch_over_indices(values: Mapping[X, S], outputs: Sequence[Y]) -> dict[tuple[Y, X], S]:
    """B: copy one indexed input family into output-indexed channels.

    (B f)(y, x) = f(x)
    """
    return {(y, x): value for y in outputs for x, value in values.items()}


def map_kernel(
    branched: Mapping[tuple[Y, X], S],
    kernel: Mapping[tuple[Y, X], S],
    mul: Callable[[S, S], S],
) -> dict[tuple[Y, X], S]:
    """M_K: apply a local kernel weight to each already-created channel."""
    missing = set(branched) - set(kernel)
    if missing:
        raise KeyError(f"kernel missing {len(missing)} channel(s)")
    return {key: mul(kernel[key], value) for key, value in branched.items()}


def fold_by_output(
    mapped: Mapping[tuple[Y, X], S],
    outputs: Sequence[Y],
    inputs: Sequence[X],
    add: Callable[[S, S], S],
    zero: S,
) -> dict[Y, S]:
    """F: aggregate channels over the input index for each output index."""
    out: dict[Y, S] = {}
    for y in outputs:
        acc = zero
        for x in inputs:
            acc = add(acc, mapped[(y, x)])
        out[y] = acc
    return out


def kernel_transform(
    values: Mapping[X, S],
    outputs: Sequence[Y],
    kernel: Mapping[tuple[Y, X], S],
    semiring: Semiring[S],
) -> dict[Y, S]:
    """Exact BMF factorization of a finite kernel operator.

    T_K = F_add ◦ M_K ◦ B

    For infinite index sets, this function is a finite witness only. The
    existence and meaning of an infinite fold must be supplied by the caller's
    topology/completion/convergence structure.
    """
    inputs = tuple(values)
    ys = tuple(outputs)
    branched = branch_over_indices(values, ys)
    mapped = map_kernel(branched, kernel, semiring.mul)
    return fold_by_output(mapped, ys, inputs, semiring.add, semiring.zero)


def direct_kernel_transform(
    values: Mapping[X, S],
    outputs: Sequence[Y],
    kernel: Mapping[tuple[Y, X], S],
    semiring: Semiring[S],
) -> dict[Y, S]:
    """Reference direct implementation of the same finite kernel operator."""
    out: dict[Y, S] = {}
    for y in outputs:
        acc = semiring.zero
        for x, value in values.items():
            acc = semiring.add(acc, semiring.mul(kernel[(y, x)], value))
        out[y] = acc
    return out


def full_permutations(items: Sequence[X]) -> tuple[tuple[X, ...], ...]:
    return tuple(permutations(items))


def equivariant_distinguished_elements(items: Sequence[X]) -> tuple[X, ...]:
    """Return elements fixed by every permutation of a finite symmetric set.

    A canonical selector on a bare finite set would need to return such an
    element. For |items| >= 2 this set is empty.
    """
    xs = tuple(items)
    if not xs:
        return ()
    fixed: list[X] = []
    for candidate in xs:
        if all(perm[xs.index(candidate)] == candidate for perm in full_permutations(xs)):
            fixed.append(candidate)
    return tuple(fixed)


def canonical_selector_exists_on_bare_finite_set(items: Sequence[X]) -> bool:
    """Finite equivariance obstruction for a distinguished-element selector."""
    return bool(equivariant_distinguished_elements(items))


def ordered_select_min(items: Iterable[X], *, key: Callable[[X], object] | None = None) -> X:
    """Selection becomes canonical only after extra order structure is supplied."""
    xs = tuple(items)
    if not xs:
        raise ValueError("cannot select from an empty family")
    return min(xs, key=key)
