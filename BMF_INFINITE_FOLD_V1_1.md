# BMF Infinite Fold v1.1 — absolute convergence and completion

Status: **STANDARD BANACH-SPACE THEOREMS + EXACT BMF EXTENSION ON A DEFINED DOMAIN / ADVERSARIAL BOUNDARIES / NO UNIVERSAL INFINITE-FOLD CLAIM**

v1.0 deliberately stopped at finite `FOLD`. v1.1 takes the first infinite step without changing the meaning of `FOLD` by fiat.

The question is:

```text
when does

(T_K f)(y) = sum_x K(y,x) f(x)

remain a legal BMF factorization when the input carrier is countably infinite?
```

The answer below is exact on an absolute-convergence domain. It is standard functional analysis expressed in the repository's typed BMF language; mathematical novelty is **not claimed**.

## 1. Scope

Let `X` be countable and let `E` be a real or complex Banach space. For a family

```text
a : X -> E
```

define

```text
||a||_1 = sum_(x in X) ||a(x)||.
```

The v1.1 infinite fold is defined only on the absolutely summable domain

```text
l1(X;E) = { a : sum_x ||a(x)|| < infinity }.
```

No implicit summation method, regularisation, analytic continuation, Cesaro summation, Abel summation, or rearrangement convention is inserted.

## 2. Theorem BMF-I1 — absolute-completion fold

Let `E` be Banach and `X` countable. Every absolutely summable family `a in l1(X;E)` has a well-defined sum

```text
F_abs(a) = sum_(x in X) a(x) in E,
```

and the value is independent of the enumeration of `X`.

Moreover,

```text
||F_abs(a)|| <= sum_x ||a(x)||,
```

so `F_abs : l1(X;E) -> E` is bounded linear with operator norm at most one.

### Proof

Choose an enumeration `X={x_1,x_2,...}` and write

```text
S_N = sum_(n=1)^N a(x_n).
```

For `M>N`,

```text
||S_M-S_N||
<= sum_(n=N+1)^M ||a(x_n)||.
```

Because the scalar series of norms converges, the right-hand side tends to zero uniformly in `M>N`; hence `(S_N)` is Cauchy. Completeness of `E` gives a limit `S in E`.

To prove independence of enumeration, fix `epsilon>0`. Absolute summability gives a finite set `F subset X` such that

```text
sum_(x notin F) ||a(x)|| < epsilon.
```

Any two sufficiently long partial sums from any two enumerations contain `F`; their difference is formed only from terms outside `F`, so its norm is bounded by at most twice the tail bound. Since `epsilon` is arbitrary, every enumeration has the same limit.

Finally, applying the triangle inequality to finite partial sums and passing to the limit gives

```text
||F_abs(a)|| <= ||a||_1.
```

Linearity follows from linearity of finite sums and passage to the limit. QED. □

## 3. Theorem BMF-I2 — countable absolute BMF factorization

Let `X` be countable, `Y` any index set, and `E` a Banach space. Suppose a kernel action is specified such that for every target `y` and input `f`, the family

```text
a_y(x) = K(y,x) f(x)
```

lies in `l1(X;E)`.

Define

```text
(Bf)(y,x)     = f(x),
(M_K Bf)(y,x) = K(y,x) f(x),
F_abs(a_y)    = sum_x a_y(x).
```

Then

```text
T_K = F_abs o M_K o B
```

with

```text
(T_K f)(y) = sum_x K(y,x) f(x).
```

### Proof

`BRANCH` exposes the indexed family, `MAP` applies the prescribed kernel action, and the hypothesis places the resulting row in the domain of Theorem BMF-I1. `F_abs` therefore exists and equals the stated series. This is equality by definition of the three typed stages on their legal domain. QED. □

This extends the finite-kernel theorem to a countable absolute-convergence domain. It does **not** extend BMF to arbitrary infinite families.

## 4. Theorem BMF-I3 — row-l1 kernel bound on l-infinity inputs

Let `X,Y` be countable, let `E` be a Banach space, and let `K:Y x X -> F` be a scalar kernel over `F=R` or `C`. Assume

```text
C = sup_(y in Y) sum_(x in X) |K(y,x)| < infinity.
```

For every bounded input `f in l-infinity(X;E)`, the row family

```text
K(y,x) f(x)
```

is absolutely summable for each `y`, and

```text
||T_K f||_infinity <= C ||f||_infinity.
```

Hence

```text
T_K : l-infinity(X;E) -> l-infinity(Y;E)
```

is a bounded linear operator with

```text
||T_K|| <= C.
```

### Proof

For every `y`,

```text
sum_x ||K(y,x)f(x)||
= sum_x |K(y,x)| ||f(x)||
<= ||f||_infinity sum_x |K(y,x)|
<= C ||f||_infinity.
```

Theorem BMF-I1 therefore defines the fold. Its norm bound gives

```text
||T_K f(y)|| <= C ||f||_infinity
```

uniformly in `y`. QED. □

## 5. Boundary theorem/counterexample BMF-I4 — completeness cannot simply be removed

Let

```text
E = c_00
```

be the finitely supported real sequences with the `l1` norm. This normed space is not complete.

Let `e_n` be the standard basis and define

```text
a_n = 2^(-n) e_n,  n>=1.
```

Then

```text
sum_n ||a_n||_1 = 1,
```

so the series is absolutely summable in norm. Its partial sums are Cauchy, with exact tail norm

```text
||sum_(n>N) a_n||_1 = 2^(-N).
```

But their limit in the completion is

```text
(1/2,1/4,1/8,...),
```

which has infinite support and therefore is not an element of `c_00`.

Thus absolute norm summability alone does not guarantee that the fold lands back in the original carrier unless the carrier is complete or an explicit completion is supplied. □

## 6. Boundary BMF-I5 — l2 control is not enough for an additive infinite fold

The scalar sequence

```text
a_n = 1/n
```

satisfies

```text
sum_n |a_n|^2 = sum_n 1/n^2 < infinity,
```

but

```text
sum_n a_n = sum_n 1/n = infinity.
```

Therefore square-summability of the term family does not imply existence of the ordinary additive fold. In particular, replacing the `l1` domain of `F_abs` by `l2` without further structure is invalid. □

The implementation uses the standard integral bounds

```text
sum_(n>=1) 1/n^2 <= 2
```

and the dyadic harmonic lower bound

```text
H_(2^m) >= 1 + m/2
```

as exact finite certificates of the two directions.

## 7. Boundary BMF-I6 — conditional scalar convergence is not an unordered fold

The alternating harmonic series

```text
1 - 1/2 + 1/3 - 1/4 + ...
```

converges but not absolutely. By the classical Riemann rearrangement theorem, permutations of its terms can change the limit or destroy convergence.

Therefore ordinary conditional convergence cannot be used as a general enumeration-independent `FOLD` rule for scalar series.

Important scope point: in real and complex scalar series, unconditional convergence is equivalent to absolute convergence. In arbitrary infinite-dimensional Banach spaces, unconditional convergence need not imply absolute convergence. v1.1 therefore claims absolute convergence as a clean sufficient domain for `F_abs`; it does **not** claim that it is the only possible infinite-fold domain in every Banach space.

## 8. Computational controls

`computations/bmf_infinite_fold_v1_1.py` and `validation/validate_bmf_infinite_fold_v1_1.py` check:

- exact geometric-series partial sums and exact tails;
- an exact finite instance of the row-`l1` / input-`l-infinity` norm bound;
- exact `c_00` geometric tail norms;
- dyadic lower bounds for harmonic divergence;
- the standard `sum 1/n^2 <= 2` integral-test certificate;
- finite prefixes of the alternating harmonic witness;
- the epistemic firewall in the deterministic result snapshot.

These controls test implementation and certificates. They are **not** substitutes for the infinite proofs above.

## 9. What v1.1 establishes

```text
countable absolutely summable Banach-valued family
    -> enumeration-independent completed fold                 STANDARD / PROVED

absolute row domain
    -> exact countable BMF factorization                      EXACT CONDITIONAL REPRESENTATION

uniform row-l1 kernel bound + bounded input
    -> bounded l-infinity-to-l-infinity operator              STANDARD / PROVED

incomplete carrier c_00
    -> absolute Cauchy series may leave the carrier           EXACT COUNTEREXAMPLE

l2 term control alone
    -> does not guarantee additive fold                        EXACT COUNTEREXAMPLE

conditional scalar convergence
    -> cannot define a general unordered fold                  STANDARD COUNTEREXAMPLE FRAME
```

## 10. Firewall

Forbidden promotions:

```text
absolute Banach fold -> every infinite fold is BMF                         FORBIDDEN
row-l1 theorem -> arbitrary integral/operator-kernel theorem                FORBIDDEN
absolute convergence -> necessary for every Banach-space unconditional sum FORBIDDEN
finite certificates -> proof of the infinite theorems                      FORBIDDEN
completion witness -> unique universal completion operator                  FORBIDDEN
v1.1 -> RH, Collatz, Twin Prime, or unrelated open problems                FORBIDDEN
```

Novelty relative to standard Banach-space series and operator theory is **NOT ESTABLISHED / NOT CLAIMED**.

## 11. Architecture after v1.1

The typed data path now has a first rigorous infinite extension:

```text
FINITE KERNEL:
    BRANCH -> MAP -> FOLD_fin

COUNTABLE ABSOLUTE KERNEL:
    BRANCH -> MAP -> FOLD_abs[E complete]
```

The next unresolved boundaries are intentionally not collapsed into `FOLD_abs`:

```text
CONDITIONAL / UNCONDITIONAL NON-ABSOLUTE SUMS
MEASURE / INTEGRAL FOLDS
P-ADIC AND OTHER VALUATION COMPLETIONS
TRANSFINITE / UNBOUNDED ITERATION
```
