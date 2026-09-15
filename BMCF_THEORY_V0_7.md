# BMCF Theory v0.7 — finite polynomial and multilinear factorization

Status: **EXACT REPRESENTATION THEOREMS IN A DEFINED FINITE CLASS / ADVERSARIAL DEGREE SEPARATION / NOVELTY NOT CLAIMED**

This stage tests the strongest surviving v0.6 data-plane candidate, `COUPLE`, without promoting it to a universal or unique fourth operator.

The typed data path is

```text
BRANCH -> MAP -> COUPLE -> FOLD
```

with `COUPLE` omitted when no dynamic-dynamic interaction is required.

## 1. Primitive semantics

For a supplied semiring-like structure `(S, +, *, 0, 1)`:

- `BRANCH` duplicates or indexes already-present dynamic values;
- `MAP` applies a fixed coefficient, independent of the runtime target value;
- `COUPLE` multiplies two or more runtime channels in declared order;
- `FOLD` adds finitely many coupled term values.

The anti-tautology rule remains in force: coefficients and primitive laws are fixed independently of the target polynomial.

## 2. Theorem BMCF-P1 — finite word-polynomial factorization

Let `X` and `Y` be finite sets. For each output `y in Y`, let

```text
P_y(f) = sum_m c_(y,m) * prod_(x in w_m) f(x)
```

where each `w_m` is a finite ordered word in `X`, repeated symbols are allowed, and each coefficient `c_(y,m)` is fixed in `S`.

Then every such finite word-polynomial map factors exactly through BMCF.

### Proof

For each monomial word `w_m=(x_1,...,x_r)`:

1. `BRANCH` exposes the runtime channels `f(x_1),...,f(x_r)`;
2. `MAP` multiplies the first channel on the left by the fixed coefficient `c_(y,m)`; for the empty word it maps the unit channel to the coefficient;
3. `COUPLE` multiplies the resulting runtime channels in the declared order, yielding exactly `c_(y,m) * f(x_1) * ... * f(x_r)`;
4. `FOLD` sums the finitely many monomial values belonging to `y`.

The result is exactly `P_y(f)` for every `y`. No target-specific primitive is introduced. QED. □

For a commutative semiring, ordered words modulo permutation are ordinary monomials. Therefore every finite polynomial with fixed coefficients is BMCF-representable. □

## 3. Corollary BMCF-P2 — finite multilinear kernel factorization

For finite input families `X_1,...,X_r`, finite output set `Y`, fixed kernel `K`, and runtime families `f_j`, define

```text
T_K(f_1,...,f_r)(y)
  = sum_(x_1,...,x_r)
      K(y;x_1,...,x_r) * f_1(x_1) * ... * f_r(x_r).
```

This is the special case of BMCF-P1 whose monomials contain one factor from each input family. Hence every finite multilinear kernel operator of this form factors exactly through BMCF. QED. □

## 4. Theorem BMCF-P3 — strict degree separation from fixed-kernel BMF

Work in a free polynomial ring or semiring with dynamic generators `x_1,...,x_n`, while all kernel coefficients are fixed scalars independent of those generators.

Every strict BMF kernel operator has the form

```text
L(x) = sum_i a_i x_i
```

and composition of such fixed-kernel maps remains linear. Therefore its dynamic total degree is at most one.

BMCF represents

```text
C(x_1,x_2) = x_1 x_2,
```

which has dynamic total degree two. Hence BMCF is a strict extension of fixed-kernel BMF on this free-polynomial witness class. QED. □

This proves a strict extension, not uniqueness or minimality of `COUPLE`. Another independently defined nonlinear primitive could also cross the degree boundary.

## 5. Exact computational controls

`computations/bmcf_polynomial_v0_7.py` checks:

- exact sparse symbolic polynomial equality for hand-built degree-3 and degree-4 examples;
- 80 deterministic random finite polynomial specifications up to generated monomial degree 6;
- exact degree separation between fixed-scalar linear forms and a coupled quadratic term;
- 50 exact finite trilinear-kernel comparisons;
- a noncommutative 2x2 matrix word witness verifying that BMCF preserves declared multiplication order.

These computations validate the implementation. They are not substitutes for the proofs above.

## 6. What v0.7 does not prove

The following remain open or outside the current class:

```text
COUPLE is the unique fourth primitive                 NOT CLAIMED
COUPLE is globally minimal                            NOT CLAIMED
BMCF is a universal computation model                 NOT CLAIMED
FIXPOINT is reducible to COUPLE                       NOT CLAIMED
QUOTIENT/COEQUALIZER is reducible to COUPLE           NOT CLAIMED
SELECT is reducible without symmetry-breaking data    NOT CLAIMED
transfinite/infinite folds follow from finite BMCF     NOT CLAIMED
novelty relative to arithmetic-circuit formalisms     NOT ESTABLISHED
```

The finite polynomial representation itself is structurally close to standard arithmetic-circuit/polynomial evaluation ideas. v0.7 claims an exact result in this repository's typed BMCF grammar, not priority over that broader literature.

## 7. Current architecture

The strongest supported data-plane statement is now

```text
linear/kernel class:       BRANCH -> MAP -> FOLD
polynomial/multilinear:    BRANCH -> MAP -> COUPLE -> FOLD
```

while the unresolved non-data-plane boundaries remain

```text
CONTROL:    FIX / ITERATE
STRUCTURE:  QUOTIENT / COEQUALIZE
SYMMETRY:   SELECT_WITH_STRUCTURE
```

## 8. v0.7 firewall

Forbidden promotions:

- finite polynomial factorization -> universal computation;
- degree separation -> uniqueness/minimality of `COUPLE`;
- finite multilinear factorization -> arbitrary infinite tensor or integral theorem;
- implementation PASS -> independent mathematical novelty;
- BMCF-P1/P2/P3 -> RH, Collatz, or any unrelated open problem.
