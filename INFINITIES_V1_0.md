# Infinities v1.0 — finite research-programme freeze

Status: **V1.0 RESEARCH PROGRAMME FREEZE / SCOPED THEOREMS + FALSIFICATIONS + OPEN BOUNDARIES**

This document closes the first finite `Infinities` research programme. It does **not** claim that mathematical infinity has been classified completely, that a universal operator basis has been found, or that any major open problem has been solved.

The freeze criterion is narrower and auditable:

```text
every material claim carried by the programme is assigned to one of

PROVED / EXACT / STANDARD_THEOREM
FALSIFIED / FAIL
REPRESENTATION_OR_TYPE_BOUNDARY
OPEN / NOT_CLAIMED
```

No unresolved statement is silently promoted to a theorem.

## 1. Core exact finite kernel result

For finite input and output carriers and a supplied semiring-like algebra,

```text
(T_K f)(y) = fold_x( K(y,x) * f(x) )
```

factors exactly as

```text
BRANCH -> MAP -> FOLD.
```

This is the exact finite-kernel BMF theorem. It is not a universal-computation theorem.

## 2. Boundary of strict BMF

Strict fixed-kernel BMF remains semimodule-linear. Consequently it cannot, in its defined real polynomial witness class, represent dynamic degree-two terms such as

```text
x_1 x_2.
```

The Boolean-semiring two-input/one-output classification likewise contains only four of the sixteen Boolean functions under the strict kernel definition.

These are exact scope boundaries, not defects to hide by enlarging MAP or FOLD until universality becomes tautological.

## 3. Conditional polynomial extension: COUPLE

`COUPLE` is the typed dynamic-dynamic multiplication operation

```text
C(a,b)=a*b
```

with multiplication supplied independently by the ambient algebra.

For finite word-polynomials,

```text
P_y(f) = sum_m c_(y,m) product_(x in w_m) f(x),
```

BMCF gives an exact factorization

```text
BRANCH -> MAP -> COUPLE -> FOLD.
```

For commutative semirings this includes finite polynomials with fixed coefficients; finite multilinear kernel operators are a special case.

## 4. Exact conditional COUPLE obstruction

Inside the finite polynomial grammar, let `delta_C(E)` be nested binary-COUPLE depth. Then

```text
deg(E) <= 2 ^ delta_C(E).
```

Therefore strict BMF (`delta_C=0`) has dynamic degree at most one.

For a nonzero finite polynomial of degree `d>=1`, the exact minimum binary-COUPLE depth is

```text
omega_C(P) = ceil(log2 d).
```

Thus, in this class only,

```text
deg(P) > 1  =>  COUPLE is necessary,
```

and the required depth is known exactly.

This is the strongest supported meaning of a conditional fourth operator in v1.0.

## 5. Why omega_C is not universal

The degree obstruction remains exact under ordinary polynomial composition, but it stops at the polynomial boundary.

Two exact witnesses are retained:

```text
1/x  : rational reciprocal boundary
|x|  : piecewise/gated boundary
```

Neither target receives a larger numeric `omega_C`; `omega_C` is **undefined outside its polynomial domain**.

A supplied reciprocal primitive can represent `1/x` without dynamic-dynamic coupling. A supplied predicate plus GATE/ITE can represent piecewise functions such as `|x|`. Hence COUPLE depth is not a universal scalar measure of nonlinearity.

## 6. FIX / ITERATE boundary

One BMF/BMCF data pass is not generally a fixed-point computation. However, for every inflationary map

```text
F : {0,1}^n -> {0,1}^n,
```

iteration reaches a fixed point after at most `n` strict state changes.

Finite Boolean reachability is a corollary and admits bounded unrolling.

Therefore v1.0 does **not** promote FIX to an independently necessary mathematical primitive. It remains a useful control abstraction and a genuine boundary for unbounded/infinite/transfinite or otherwise non-covered dynamics.

## 7. QUOTIENT / COEQUALIZE boundary

Finite partitions are in bijection with finite equivalence relations. Therefore a finite quotient can be represented on the original fixed carrier by its equivalence matrix.

Changing quotient cardinality alone is consequently insufficient evidence that QUOTIENT must be an independent universal primitive.

Actual quotient-carrier construction, canonical naming of classes, arbitrary colimits, and infinite/category-theoretic extensions remain outside the finite theorem.

## 8. SELECT / symmetry boundary

For every bare finite set `X` with `|X|>=2`, no distinguished-element selector can be equivariant under all permutations of `X` without additional structure.

A supplied total order removes the obstruction by permitting

```text
s(X)=min(X).
```

The proved result is therefore a symmetry-breaking requirement, not universal minimality of a SELECT primitive and not a theorem about arbitrary uses of Choice.

## 9. Final typed architecture

The v1.0 architecture is deliberately not collapsed into a fake universal four-operator slogan:

```text
CORE FINITE KERNEL DATA:
    BRANCH -> MAP -> FOLD

CONDITIONAL FINITE POLYNOMIAL DATA:
    BRANCH -> MAP -> COUPLE[omega_C] -> FOLD

TYPED AUXILIARY BOUNDARIES:
    RECIP
    GATE / ITE
    ITERATE / FIX
    QUOTIENT / COEQUALIZE
    SELECT_WITH_STRUCTURE
```

A software runtime may expose the auxiliary cases through one tagged dispatcher. That software convenience is **not** a theorem that these cases are one mathematical primitive.

## 10. Negative results preserved

v1.0 intentionally retains negative results:

```text
universal [1/2] seam across all catalogued infinity sectors     NOT SUPPORTED
v0.1 five-generator vocabulary universally minimal             NOT ESTABLISHED
strict BMF universal computation model                          FALSE IN TESTED/DEFINED SENSE
one universal fourth operator                                   NOT ESTABLISHED
omega_C universal nonlinearity scalar                           FALSE OUTSIDE DOMAIN
COUPLE unique/minimal across all grammars                       NOT ESTABLISHED
FIX independent primitive in finite inflationary Boolean class  NOT ESTABLISHED
QUOTIENT independent primitive from cardinality change alone    NOT ESTABLISHED
SELECT universally necessary                                    NOT ESTABLISHED
```

These results are part of the programme, not discarded failed experiments.

## 11. Open boundaries retained explicitly

The following are outside the finite closure and remain open/not claimed:

- infinite or transfinite iteration and fixed points;
- arbitrary quotient/colimit constructions;
- Choice-sensitive witness selection beyond the finite symmetry theorem;
- infinite folds without explicit topology, measure, valuation, completion, or convergence rules;
- transcendental/analytic function classes beyond the finite polynomial/rational/piecewise witnesses;
- universal minimality of any operator grammar;
- mathematical novelty relative to arithmetic circuits, rational circuits, categorical constructions, or established complexity theory without a dedicated literature comparison.

## 12. Open-problem firewall

Nothing in v1.0 proves or materially closes:

```text
Riemann Hypothesis
Collatz conjecture
Twin Prime conjecture
```

The repository contains structural encodings and scoped local results involving these sectors, but no global proof promotion is allowed.

## 13. Reproducibility contract

The canonical CI workflow runs every validator from the original controls through the v0.10 typed-boundary audit, plus the v1.0 freeze validator.

A v1.0 release candidate may be merged to `main` only if:

```text
each required result matches its preregistered expected verdict,
including intentional FAIL results used as falsification evidence,
all validators pass,
CLAIMS.md retains the epistemic firewall,
VERSION is exactly 1.0.0,
no open-problem proof claim is introduced.
```

An intentional negative result such as the GREMLIN holdout failure or falsified universal-half hypothesis is a **successful control outcome** when it matches the preregistered expectation. The freeze must never rewrite such a result to `PASS` merely to make the release look green.

## 14. Freeze meaning

`v1.0 COMPLETE` means:

```text
the first finite Infinities research programme is closed as an auditable body
of scoped theorems, counterexamples, exact finite classifications, typed
boundaries, and explicit open questions.
```

It does **not** mean:

```text
all infinities are solved.
```

That distinction is part of the theorem hygiene of the release.
