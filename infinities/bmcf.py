from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Generic, Mapping, Sequence, TypeVar

from .bmf import Semiring

X = TypeVar("X")
Y = TypeVar("Y")
S = TypeVar("S")


@dataclass(frozen=True)
class PolynomialTerm(Generic[X, S]):
    """One finite monomial term with a fixed left coefficient.

    `factors` may repeat input keys, so `(x, x, y)` represents x^2 y in a
    commutative setting and the ordered word x*x*y in a noncommutative setting.
    """

    coefficient: S
    factors: tuple[X, ...]


def branch_term(values: Mapping[X, S], term: PolynomialTerm[X, S]) -> tuple[S, ...]:
    """B: expose the dynamic channels requested by one monomial."""
    return tuple(values[key] for key in term.factors)


def map_term_coefficient(
    branched: Sequence[S],
    coefficient: S,
    semiring: Semiring[S],
) -> tuple[S, ...]:
    """M: apply a fixed coefficient without hiding a target computation.

    Coefficients multiply on the left. For a constant monomial, the coefficient
    itself becomes the single mapped channel.
    """
    channels = tuple(branched)
    if not channels:
        return (coefficient,)
    return (semiring.mul(coefficient, channels[0]), *channels[1:])


def couple_channels(channels: Sequence[S], semiring: Semiring[S]) -> S:
    """C: multiply runtime channels in their declared order."""
    acc = semiring.one
    for value in channels:
        acc = semiring.mul(acc, value)
    return acc


def fold_terms(term_values: Sequence[S], semiring: Semiring[S]) -> S:
    """F: add finitely many already-coupled monomial values."""
    acc = semiring.zero
    for value in term_values:
        acc = semiring.add(acc, value)
    return acc


def polynomial_transform(
    values: Mapping[X, S],
    outputs: Sequence[Y],
    terms: Mapping[Y, Sequence[PolynomialTerm[X, S]]],
    semiring: Semiring[S],
) -> dict[Y, S]:
    """Exact finite B-M-C-F evaluation of a finite polynomial specification.

    For commutative semirings this represents ordinary finite polynomials with
    supplied coefficients. For noncommutative semirings it represents ordered
    word polynomials with coefficients on the left.
    """
    out: dict[Y, S] = {}
    for y in outputs:
        coupled: list[S] = []
        for term in terms.get(y, ()):
            branched = branch_term(values, term)
            mapped = map_term_coefficient(branched, term.coefficient, semiring)
            coupled.append(couple_channels(mapped, semiring))
        out[y] = fold_terms(coupled, semiring)
    return out


def direct_polynomial_transform(
    values: Mapping[X, S],
    outputs: Sequence[Y],
    terms: Mapping[Y, Sequence[PolynomialTerm[X, S]]],
    semiring: Semiring[S],
) -> dict[Y, S]:
    """Reference evaluation of the same finite polynomial specification."""
    out: dict[Y, S] = {}
    for y in outputs:
        acc = semiring.zero
        for term in terms.get(y, ()):
            monomial = term.coefficient
            for key in term.factors:
                monomial = semiring.mul(monomial, values[key])
            acc = semiring.add(acc, monomial)
        out[y] = acc
    return out


def multilinear_transform(
    families: Sequence[Mapping[X, S]],
    outputs: Sequence[Y],
    kernel: Mapping[tuple[Y, tuple[X, ...]], S],
    semiring: Semiring[S],
) -> dict[Y, S]:
    """Finite multilinear kernel transform using B-M-C-F.

    T_K(f_1,...,f_r)(y)
      = sum_{x_1,...,x_r} K(y;x_1,...,x_r) * prod_j f_j(x_j).
    """
    if not families:
        raise ValueError("multilinear_transform requires at least one input family")
    index_families = [tuple(family) for family in families]
    out: dict[Y, S] = {}
    for y in outputs:
        term_values: list[S] = []
        for indices in product(*index_families):
            coefficient = kernel[(y, tuple(indices))]
            channels = tuple(family[key] for family, key in zip(families, indices))
            mapped = map_term_coefficient(channels, coefficient, semiring)
            term_values.append(couple_channels(mapped, semiring))
        out[y] = fold_terms(term_values, semiring)
    return out


def direct_multilinear_transform(
    families: Sequence[Mapping[X, S]],
    outputs: Sequence[Y],
    kernel: Mapping[tuple[Y, tuple[X, ...]], S],
    semiring: Semiring[S],
) -> dict[Y, S]:
    """Reference implementation of the same finite multilinear operator."""
    if not families:
        raise ValueError("direct_multilinear_transform requires at least one input family")
    index_families = [tuple(family) for family in families]
    out: dict[Y, S] = {}
    for y in outputs:
        acc = semiring.zero
        for indices in product(*index_families):
            value = kernel[(y, tuple(indices))]
            for family, key in zip(families, indices):
                value = semiring.mul(value, family[key])
            acc = semiring.add(acc, value)
        out[y] = acc
    return out
