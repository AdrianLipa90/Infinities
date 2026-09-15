# Conditional Fourth-Operator Search v0.6

Status: **PREREGISTERED CANDIDATE SEARCH / EXACT FINITE ENUMERATIONS / NO UNIVERSAL FOURTH OPERATOR CLAIM**

This stage asks whether the v0.5 boundaries can be repaired by one optional fourth primitive without weakening the anti-tautology guard. The answer at v0.6 is: **not yet**. We have a strong data-plane candidate, but the control-plane and carrier-formation boundaries remain type-distinct.

## 1. Search rule

A candidate is admissible only if its semantics are fixed independently of the target computation. A candidate does not count if it can hide the desired result inside an arbitrary MAP, FOLD, predicate, quotient, or oracle.

The search tests four obstruction types exposed by v0.5:

```text
LINEARITY / CROSS-CHANNEL INTERACTION
CONTROL / FEEDBACK
CARRIER FORMATION
SYMMETRY BREAKING
```

## 2. COUPLE: dynamic-dynamic interaction

Define a typed dynamic coupling

```text
C_otimes(a,b) = a otimes b
```

where `otimes` is supplied by the ambient algebra and both arguments are runtime values. This differs from the v0.4 kernel MAP, where a runtime value is multiplied only by a fixed kernel coefficient.

Over the reals, duplicating `x` and applying dynamic multiplication gives

```text
C_mul(x,x) = x^2.
```

Thus COUPLE crosses the strict linearity boundary exhibited in v0.5 without hiding `x^2` inside an arbitrary unary MAP.

Over the Boolean semiring, dynamic multiplication is AND. Starting from variables and constants and closing under OR and AND gives exactly the six monotone Boolean functions of two variables. Therefore COUPLE alone is **not** Boolean-functionally complete.

If the local MAP library is separately and explicitly fixed to

```text
{ZERO, ONE, ID, NOT}
```

then conjunction by COUPLE and disjunction by FOLD give disjunctive normal form. Exhaustive two-variable enumeration realizes all 16 truth tables; the computation needs at most two conjunctive terms for this finite case. The general Boolean statement is the standard DNF construction, but it depends on local complement being part of the supplied structure.

**v0.6 status:** COUPLE is a strict and non-tautological extension of the BMF data plane. It is **not proved unique, minimal, or universal**.

## 3. GATE / ITE

The fixed conditional operator

```text
ITE(p, a, b) = a if p else b
```

is target-independent. For Boolean functions, Shannon expansion gives

```text
f(x1,...,xn) = ITE(x1, f(1,x2,...,xn), f(0,x2,...,xn)).
```

For two variables, exhaustive enumeration of

```text
ITE(a, g1(b), g0(b))
```

with the four unary Boolean maps realizes all 16 truth tables.

This establishes Boolean functional completeness of fixed ITE with constants/variables. It does **not** establish that ITE supplies arbitrary real nonlinearity, quotient carrier formation, or fixed points without additional structure.

## 4. FIXPOINT remains a control-plane operation

The path witness

```text
0 -> 1 -> 2
```

stabilizes under repeated Boolean reachability as

```text
100 -> 110 -> 111 -> 111.
```

An explicit finite FIX/ITERATE procedure therefore resolves this boundary. Nothing in v0.6 proves that FIX is reducible to COUPLE or ITE while preserving the strict typing and anti-tautology rules.

## 5. QUOTIENT remains a carrier-formation operation

The v0.5 coequalizer enumeration is reproduced exactly:

```text
1+1+1 :  9
2+1   : 48
3     : 24
```

The output carrier changes with the generated equivalence relation. COUPLE and ITE operate on already supplied carriers; neither computation in v0.6 proves that quotient formation is the same typed operation.

## 6. SELECT remains symmetry-sensitive

The earlier permutation obstruction still applies to a bare finite set. A selector becomes canonical only after supplying extra symmetry-breaking structure such as an order. v0.6 does not promote SELECT to a universal fourth primitive.

## 7. Interim architecture

A software runtime may expose one optional fourth **slot**, but this must not be confused with one mathematical operator. The honest interim type is a tagged sum:

```text
AUX = COUPLE | GATE | FIX | QUOTIENT | SELECT_WITH_STRUCTURE
```

with activation controlled by an explicit obstruction witness. In symbolic notation,

```text
AUX[omega]
```

is conditional on the obstruction class `omega`; the variants are not declared equivalent.

The strongest current data-plane candidate is therefore

```text
BRANCH -> MAP -> COUPLE? -> FOLD
```

where `COUPLE?` is absent for strict kernel-linear operators and present only when a cross-channel interaction is required.

## 8. v0.6 firewall

Forbidden promotions:

- COUPLE strict-extension witness -> unique minimal fourth primitive;
- two-variable enumeration -> universal theorem over arbitrary domains;
- ITE Boolean completeness -> universal mathematical completeness;
- finite FIX witness -> transfinite fixed-point theorem;
- finite quotient enumeration -> reduction of all colimits/quotients;
- tagged software AUX slot -> proof that there is one fourth mathematical operator;
- any v0.6 result -> proof of RH, Collatz, or another open problem.

## 9. Current verdict

```text
single universal fourth operator: NOT FOUND
COUPLE as data-plane fourth candidate: SURVIVES v0.6
GATE as Boolean/control candidate: SURVIVES scoped test
FIX as control-plane candidate: STILL DISTINCT
QUOTIENT as structure-plane candidate: STILL DISTINCT
SELECT as symmetry-breaking candidate: STILL CONDITIONAL ON EXTRA STRUCTURE
```

The next falsification target is whether COUPLE can be characterized by a theorem for polynomial/multilinear operator classes and whether FIX or QUOTIENT can be derived from a common constrained construction without making that construction tautological.
