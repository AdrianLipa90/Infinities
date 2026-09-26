# Spectral Closure of the Shifted von Mangoldt Tower v0.1

Status: \`PROVED_FROM_STANDARD_LANDAU + EXACT_FINITE_DIVISOR_IDENTITY\`

This note closes a precise loop between the existing shifted-von-Mangoldt tower and the zeta-zero spectrum. The novelty claim is deliberately limited: the ingredients are classical, while the present statement packages them in the repository's \(p+1\) fibre coordinates.

## 1. Classical inputs

For every integer \(n\ge2\),

\[
\log n
=
\sum_{\substack{d\mid n\\d>1}}
\Lambda(d).
\]

For fixed \(x>1\), Landau's formula gives

\[
\sum_{0<\gamma\le T}x^\rho
=
-\frac{T}{2\pi}\Lambda(x)
+
O_x(\log T).
\]

Therefore define

\[
\mathcal L_x(T)
=
-\frac{2\pi}{T}
\sum_{0<\gamma\le T}x^\rho.
\]

Then

\[
\boxed{
\lim_{T\to\infty}\mathcal L_x(T)=\Lambda(x).
}
\]

## 2. Finite-divisor spectral reconstruction

Because every fixed integer \(n\) has only finitely many divisors, the limit may be summed over its divisor set:

\[
\boxed{
\log n
=
\lim_{T\to\infty}
\sum_{\substack{d\mid n\\d>1}}
\mathcal L_d(T)
}
\]

or equivalently

\[
\boxed{
\log n
=
-
\lim_{T\to\infty}
\frac{2\pi}{T}
\sum_{\substack{d\mid n\\d>1}}
\sum_{0<\gamma\le T}
d^\rho.
}
\]

Non-prime-power divisors contribute zero in the Landau limit because their von Mangoldt weight is zero.

This is an exact corollary of two standard results; no interchange of an infinite divisor sum is involved.

## 3. Closure of the existing On-Primes identity

For a prime \(p\), the repository already uses

\[
\log(p+1)
=
\sum_{r^j\mid p+1}\log r,
\]

where \(r\) ranges over primes and \(j\ge1\).

Since

\[
\Lambda(r^j)=\log r,
\]

Landau gives

\[
\boxed{
\log(p+1)
=
-
\lim_{T\to\infty}
\frac{2\pi}{T}
\sum_{r^j\mid p+1}
\sum_{0<\gamma\le T}
(r^j)^\rho.
}
\]

Thus every shifted prime-power shell \(r^j\mid p+1\) has a matching zeta-zero spectral channel at the same scale \(r^j\), with the same weight \(\log r\).

This is the exact spectral closure of the shifted-von-Mangoldt tower.

## 4. Critical-line phase representation

If one specializes to zeros on the critical line,

\[
\rho=\frac12+i\gamma,
\]

then

\[
(r^j)^\rho
=
r^{j/2}e^{ij\gamma\log r}.
\]

Hence

\[
\boxed{
\log(p+1)
=
-
\lim_{T\to\infty}
\frac{2\pi}{T}
\sum_{r^j\mid p+1}
r^{j/2}
\sum_{\gamma\le T}
e^{ij\gamma\log r}.
}
\]

This phase-only form uses critical-line placement. The preceding \(d^\rho\) reconstruction does not.

## 5. Dyadic component

For the unique address

\[
p+1=a_p2^{k_p},
\]

the dyadic term is

\[
k_p\log2
=
\sum_{j=1}^{k_p}\Lambda(2^j).
\]

Therefore

\[
\boxed{
k_p\log2
=
-
\lim_{T\to\infty}
\frac{2\pi}{T}
\sum_{j=1}^{k_p}
\sum_{\gamma\le T}
2^{j\rho}.
}
\]

On the critical line,

\[
\boxed{
k_p\log2
=
-
\lim_{T\to\infty}
\frac{2\pi}{T}
\sum_{j=1}^{k_p}
2^{j/2}
\sum_{\gamma\le T}
e^{ij\gamma\log2}.
}
\]

So the integer fibre coordinate \(k_p=v_2(p+1)\) counts how many dyadic Landau channels contribute to the exact logarithmic mass of \(p+1\).

## 6. Renormalized dyadic tower

Define

\[
Z_j(T)
=
-\frac{2\pi}{T}
\sum_{\gamma\le T}
(2^j)^\rho.
\]

Then for every fixed \(j\ge1\),

\[
\boxed{
Z_j(T)\longrightarrow\log2.
}
\]

On the critical line,

\[
Z_j(T)
=
-\frac{2\pi}{T}
2^{j/2}
\sum_{\gamma\le T}
e^{ij\gamma\log2}.
\]

Thus the amplitude decay \(2^{-j/2}\) in the raw phase average is exactly removed by the critical-line factor \(2^{j/2}\), leaving the same von Mangoldt atom \(\log2\) at every dyadic prime-power level.

## 7. Finite numerical witness

For the first 256 positive critical-line zero ordinates, with

\[
T=478.9421815346348,
\]

the real parts of the renormalized \(Z_j(T)\) are approximately:

| \(j\) | \(\Re Z_j(T)\) | \(\log2\) ratio |
|---:|---:|---:|
| 1 | 0.684780 | 0.98793 |
| 2 | 0.671900 | 0.96935 |
| 3 | 0.684733 | 0.98786 |
| 4 | 0.503365 | 0.72620 |
| 5 | 0.582229 | 0.83998 |

The first three levels already track the common asymptotic weight closely. Higher low-height harmonics have larger finite-\(T\) error, as expected.

This table is a numerical witness only.

## 8. Collatz reverse-fibre corollary

For an accelerated odd-Collatz reverse predecessor

\[
B_a(m)=\frac{2^a m-1}{3},
\qquad m\ \text{odd},
\]

we have

\[
3B_a(m)+1=2^a m
\]

and therefore

\[
v_2(3B_a(m)+1)=a.
\]

The dyadic contribution to

\[
\log(3B_a(m)+1)
\]

is exactly

\[
a\log2
=
\sum_{j=1}^{a}\Lambda(2^j).
\]

Moving within the same reverse fibre from \(a\) to \(a+2\) gives

\[
B_{a+2}(m)=4B_a(m)+1
\]

and adds exactly

\[
\boxed{
2\log2
=
\Lambda(2^{a+1})
+
\Lambda(2^{a+2}).
}
\]

Therefore its spectral form is

\[
\boxed{
2\log2
=
-
\lim_{T\to\infty}
\frac{2\pi}{T}
\sum_{\gamma\le T}
\left(
2^{(a+1)\rho}
+
2^{(a+2)\rho}
\right).
}
\]

On the critical line this becomes a sum of two consecutive dyadic phase harmonics.

This is an exact local arithmetic/spectral representation. It does not prove global Collatz convergence.

## 9. Hilbert-Hotel interpretation

The dyadic prime-power channels form a countable tower

\[
2,4,8,16,\ldots
\]

indexed by \(j\in\mathbb N\). The unilateral shift

\[
j\mapsto j+1
\]

moves one room along this tower.

Landau's spectral limit maps every fixed room to the same renormalized atom:

\[
2^j
\mapsto
\Lambda(2^j)
=
\log2.
\]

Hence the countable dyadic tower is simultaneously:

- a Hilbert-Hotel index set;
- the harmonic ladder of the \(\gamma\log2\) phase clock;
- the \(2\)-primary part of the shifted von Mangoldt decomposition;
- the valuation ladder used by the accelerated Collatz map.

These are exact shared representations, not an identification of the underlying open problems.

## 10. Claim types

| ID | Statement | Status |
|---|---|---|
| SVMC-001 | \(\log n=\sum_{d\mid n}\Lambda(d)\). | STANDARD |
| SVMC-002 | Landau's fixed-\(x\) zero formula. | STANDARD |
| SVMC-003 | Finite-divisor spectral reconstruction of \(\log n\). | PROVED_FROM_STANDARD |
| SVMC-004 | Spectral reconstruction of \(\log(p+1)\) over prime-power divisor channels. | PROVED_FROM_STANDARD |
| SVMC-005 | Dyadic reconstruction of \(k_p\log2\). | PROVED_FROM_STANDARD |
| SVMC-006 | \(Z_j(T)\to\log2\) for every fixed dyadic level \(j\). | STANDARD_COROLLARY |
| SVMC-007 | Reverse-Collatz step \(a\to a+2\) adds exactly two dyadic von Mangoldt channels. | EXACT |
| SVMC-008 | The phase-only formulas use critical-line placement. | CONDITIONAL_REPRESENTATION |

## Boundary

Nothing here proves RH, Collatz, Littlewood's sign-change theorem, or a formula for the first Skewes crossing.

The supported result is narrower and exact:

\[
\boxed{
\text{shifted prime-power divisor tower}
\longleftrightarrow
\text{Landau zero-spectrum channels}
}
\]

with the dyadic sector shared by On-Primes and the local reverse-Collatz fibre.
