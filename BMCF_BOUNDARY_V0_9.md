# BMCF Boundary v0.9 — where the degree obstruction stops

Status: **EXACT BOUNDARY THEOREMS / TNT OUTSIDE THE POLYNOMIAL CLASS / NO UNIVERSAL FOURTH-OPERATOR CLAIM**

v0.8 proved an exact conditional activation rule for `COUPLE` inside the finite polynomial BMCF grammar. v0.9 deliberately attacks the temptation to export that rule beyond its legal domain.

The question is not whether `omega_C` is useful. It is. The question is where it stops being the right invariant.

## 1. Scope

Recall the polynomial grammar

```text
BRANCH  : duplicate/index an existing dynamic channel
MAP     : multiply by a fixed scalar coefficient
COUPLE  : binary multiplication of two runtime expressions
FOLD    : finite addition
```

and, for a finite polynomial target `P`,

```text
omega_C(P) = 0                    if deg(P) <= 1
             ceil(log2 deg(P))    if deg(P) >= 2.
```

Within that class, `omega_C(P)` is the exact minimal nested binary-COUPLE depth.

v0.9 tests three directions:

```text
POLYNOMIAL COMPOSITION
RATIONAL / DYNAMIC RECIPROCAL
PIECEWISE / GATED SELECTION
```

## 2. Theorem BMCF-D1 — polynomial composition remains inside the degree grammar

Let `P,Q` be nonconstant univariate polynomials over an integral domain. Then

```text
deg(P o Q) = deg(P) * deg(Q).
```

### Proof

Write

```text
P(x) = a_m x^m + lower terms,
Q(x) = b_n x^n + lower terms,
```

with `a_m,b_n != 0`. The leading term of `P(Q(x))` is

```text
a_m (b_n x^n)^m = a_m b_n^m x^(mn).
```

Because the coefficient ring is an integral domain, `a_m b_n^m != 0`, and no lower term of `P` can produce degree `mn`. Hence `deg(P o Q)=mn`. QED. □

Therefore ordinary polynomial composition does **not** break the v0.8 obstruction. After composition, the target is still a polynomial, and `omega_C` applies to the resulting polynomial.

### Corollary BMCF-D1a — repeated squaring is depth-optimal

Define

```text
S_0(x)=x,
S_(k+1)(x)=S_k(x)^2.
```

Then

```text
deg(S_k)=2^k,
omega_C(S_k)=k.
```

A depth-`k` balanced/repeated-squaring construction attains the lower bound, so the coupling depth is exact. □

## 3. Theorem BMCF-D2 — dynamic reciprocal is outside the polynomial grammar

Over `Q`, the formal rational function

```text
R(x)=1/x
```

is not representable by any finite polynomial BMCF expression.

### Proof

Every expression in the polynomial BMCF grammar denotes a polynomial in `Q[x]`. If some polynomial `P(x)` represented `1/x` as a formal rational function, then

```text
x P(x) = 1
```

in `Q[x]`. But the left-hand side is divisible by `x`, while the constant polynomial `1` is not. Equivalently, any nonzero `xP(x)` has degree at least one. Contradiction. QED. □

This is an important anti-slop boundary:

```text
omega_C(1/x) is not 0.
omega_C(1/x) is not 1.
omega_C(1/x) is UNDEFINED because 1/x is outside the polynomial domain.
```

If an independently specified unary reciprocal primitive

```text
RECIP(z)=z^(-1)
```

is added, then `1/x` requires no dynamic-dynamic `COUPLE` at all. Thus `COUPLE` depth cannot be promoted into a universal measure of nonlinearity.

## 4. Finite root-count certificate for the reciprocal boundary

The formal theorem above has an exact finite adversarial certificate at every proposed polynomial degree bound `d`.

Suppose a polynomial `P` with `deg(P)<=d` agrees with `1/x` at `d+2` distinct nonzero points. Then

```text
H(x)=xP(x)-1
```

has degree at most `d+1` but at least `d+2` distinct roots. Therefore `H` is the zero polynomial, contradicting the theorem above.

Hence no degree-`d` polynomial can match `1/x` on `d+2` arbitrary distinct nonzero points. □

The v0.9 computation checks this with exact rational arithmetic for degree bounds `0..24`.

## 5. Theorem BMCF-D3 — branchwise degree does not detect piecewise structure

Consider

```text
A(x)=|x| = x   for x>=0
             = -x  for x<0.
```

Each branch has polynomial degree one, but `A` is not a polynomial over `R`.

### Proof

Assume polynomial `P` satisfies `P(x)=|x|` for all real `x`. On every positive real,

```text
P(x)-x=0.
```

A nonzero polynomial has only finitely many roots, so `P(x)-x` must be the zero polynomial. Hence `P(x)=x` for all real `x`. But at `x=-1`, this gives `P(-1)=-1`, whereas `|-1|=1`. Contradiction. QED. □

Therefore a branchwise degree report

```text
max branch degree = 1
```

does **not** imply strict BMF or polynomial BMCF representability. A supplied predicate plus a typed selection primitive such as `GATE/ITE` crosses a different boundary from `COUPLE`.

Again, this does not prove that `GATE` is a universally minimal primitive. It proves that polynomial degree alone does not encode piecewise selection structure.

## 6. Finite root-count certificate for the piecewise boundary

For any proposed degree bound `d>=1`, if a polynomial `P` of degree at most `d` agrees with `|x|` on `d+1` distinct positive points, then `P-x` has more roots than its degree and therefore `P=x` identically. One negative point then falsifies the representation.

The computation uses an even stronger overdetermined exact system and verifies inconsistency for degree bounds `0..24` using rational row reduction.

## 7. What survives and what breaks

The v0.8 obstruction survives exactly under polynomial composition:

```text
polynomial target -> omega_C is defined and exact
```

but fails as a universal classifier outside that class:

```text
1/x      -> outside polynomial grammar; reciprocal-type boundary
|x|      -> outside polynomial grammar; gate/predicate boundary
```

Thus the correct statement is typed:

```text
POLYNOMIAL DATA PLANE:
    omega_C controls minimal COUPLE depth exactly.

RATIONAL EXTENSION:
    may require RECIP / DIV-type structure not measured by omega_C.

PIECEWISE EXTENSION:
    may require GATE / ITE plus supplied predicate structure, not measured by omega_C.
```

## 8. No fake universal obstruction scalar

A tempting but invalid promotion would be to define one scalar `omega` and declare that every non-polynomial or nonlinear target merely has a larger `omega_C`.

v0.9 rejects that move. `1/x` and `|x|` are not higher-degree polynomial cases; they are different typed obstructions.

The honest architecture remains a typed obstruction family rather than one magic number:

```text
COUPLE obstruction   : polynomial multiplicative degree/depth
RECIP boundary       : dynamic inversion / rational structure
GATE boundary        : conditional/piecewise selection
FIX boundary         : feedback / iteration
QUOTIENT boundary    : carrier formation
SELECT boundary      : symmetry breaking
```

No claim is made that this list is complete or minimal.

## 9. TNT criteria

v0.9 is considered successful only if all of the following hold:

- polynomial composition preserves the v0.8 degree obstruction;
- repeated squaring attains the predicted exact COUPLE depth;
- reciprocal targets produce exact polynomial inconsistency certificates;
- piecewise absolute value produces exact polynomial inconsistency certificates;
- the implementation refuses to assign a numeric `omega_C` to targets outside the polynomial class;
- no result is promoted to a universal fourth-operator theorem.

## 10. Firewall

Forbidden promotions:

```text
omega_C exact on polynomials -> omega_C universal on all functions          FORBIDDEN
1/x outside polynomial BMCF -> RECIP is globally minimal                    FORBIDDEN
|x| outside polynomial BMCF -> GATE is globally minimal                     FORBIDDEN
finite degree certificates -> theorem about arbitrary analytic classes       FORBIDDEN
polynomial composition theorem -> arbitrary functional composition theorem   FORBIDDEN
v0.9 -> RH, Collatz, or unrelated open problems                              FORBIDDEN
```

Novelty relative to arithmetic-circuit complexity, rational circuits, and decision/gated circuit formalisms remains **NOT ESTABLISHED**.
