from __future__ import annotations

from fractions import Fraction
from math import ceil, log2
from typing import Sequence


def trim_polynomial(coefficients: Sequence[Fraction | int]) -> tuple[Fraction, ...]:
    coeffs = [Fraction(value) for value in coefficients]
    if not coeffs:
        coeffs = [Fraction(0)]
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return tuple(coeffs)


def polynomial_degree(coefficients: Sequence[Fraction | int]) -> int:
    coeffs = trim_polynomial(coefficients)
    if len(coeffs) == 1 and coeffs[0] == 0:
        return -1
    return len(coeffs) - 1


def polynomial_add(
    left: Sequence[Fraction | int],
    right: Sequence[Fraction | int],
) -> tuple[Fraction, ...]:
    width = max(len(left), len(right))
    return trim_polynomial(
        [
            (Fraction(left[i]) if i < len(left) else Fraction(0))
            + (Fraction(right[i]) if i < len(right) else Fraction(0))
            for i in range(width)
        ]
    )


def polynomial_mul(
    left: Sequence[Fraction | int],
    right: Sequence[Fraction | int],
) -> tuple[Fraction, ...]:
    a = trim_polynomial(left)
    b = trim_polynomial(right)
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim_polynomial(out)


def polynomial_compose(
    outer: Sequence[Fraction | int],
    inner: Sequence[Fraction | int],
) -> tuple[Fraction, ...]:
    """Exact univariate composition outer(inner(x)) over Q."""
    result = (Fraction(0),)
    power = (Fraction(1),)
    for coefficient in trim_polynomial(outer):
        scaled = tuple(coefficient * value for value in power)
        result = polynomial_add(result, scaled)
        power = polynomial_mul(power, inner)
    return trim_polynomial(result)


def omega_c_for_polynomial_degree(degree: int) -> int:
    """Exact v0.8 minimal binary-COUPLE depth for polynomial degree."""
    if degree < -1:
        raise ValueError("invalid polynomial degree")
    if degree <= 1:
        return 0
    return ceil(log2(degree))


def omega_c_for_target(target_class: str, degree: int | None = None) -> int | None:
    """Typed guard: omega_C is numeric only on the polynomial target class.

    Returning None is deliberate. Rational/piecewise targets are not silently
    coerced into a fake polynomial degree.
    """
    if target_class != "POLYNOMIAL":
        return None
    if degree is None:
        raise ValueError("polynomial target requires a degree")
    return omega_c_for_polynomial_degree(degree)


def vandermonde(points: Sequence[Fraction | int], max_degree: int) -> list[list[Fraction]]:
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    return [
        [Fraction(point) ** power for power in range(max_degree + 1)]
        for point in points
    ]


def linear_system_consistent(
    matrix: Sequence[Sequence[Fraction | int]],
    rhs: Sequence[Fraction | int],
) -> bool:
    """Exact Gaussian-elimination consistency test over Q."""
    if len(matrix) != len(rhs):
        raise ValueError("matrix/rhs row mismatch")
    if not matrix:
        return True
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")

    augmented = [
        [Fraction(value) for value in row] + [Fraction(value_rhs)]
        for row, value_rhs in zip(matrix, rhs)
    ]
    rows = len(augmented)
    pivot_row = 0

    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, rows) if augmented[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        augmented[pivot_row], augmented[pivot] = augmented[pivot], augmented[pivot_row]
        scale = augmented[pivot_row][column]
        augmented[pivot_row] = [value / scale for value in augmented[pivot_row]]

        for row in range(rows):
            if row == pivot_row or augmented[row][column] == 0:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                current - factor * pivot_value
                for current, pivot_value in zip(augmented[row], augmented[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break

    for row in augmented:
        if all(value == 0 for value in row[:width]) and row[width] != 0:
            return False
    return True


def polynomial_fit_consistent(
    points: Sequence[Fraction | int],
    values: Sequence[Fraction | int],
    max_degree: int,
) -> bool:
    return linear_system_consistent(vandermonde(points, max_degree), values)


def reciprocal_polynomial_certificate(max_degree: int) -> bool:
    """True iff exact finite data certify no degree<=d polynomial fits 1/x."""
    points = [Fraction(index) for index in range(1, max_degree + 3)]
    values = [Fraction(1, point) for point in points]
    return not polynomial_fit_consistent(points, values, max_degree)


def absolute_value_polynomial_certificate(max_degree: int) -> bool:
    """True iff exact finite data certify no degree<=d polynomial fits |x|."""
    positive_points = [Fraction(index) for index in range(1, max_degree + 3)]
    points = [*positive_points, Fraction(-1)]
    values = [abs(point) for point in points]
    return not polynomial_fit_consistent(points, values, max_degree)
