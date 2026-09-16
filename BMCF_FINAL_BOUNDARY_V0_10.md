# BMCF Final Boundary v0.10 — control, quotient, and symmetry closure audit

Status: **EXACT FINITE BOUNDARY THEOREMS / REPRESENTATION AUDIT / NO UNIVERSAL FOURTH-OPERATOR CLAIM**

v0.10 closes the remaining finite boundaries that were left deliberately unresolved in v0.5-v0.9: `FIX/ITERATE`, `QUOTIENT/COEQUALIZE`, and symmetry-breaking `SELECT`.

The purpose is destructive: determine which candidates are genuinely forced, which are only control/representation choices, and which require additional structure rather than a new universal operator.

## 1. Theorem BMCF-F1 — finite inflationary Boolean fixed points have a bounded horizon

Let

```text
F : {0,1}^n -> {0,1}^n
```

be inflationary in the coordinatewise order:

```text
x <= F(x)
```

for every state `x`. Starting from `x_0`, define

```text
x_(k+1)=F(x_k).
```

Then the sequence reaches a fixed point after at most `n` strict state changes.

### Proof

The orbit is monotone:

```text
x_0 <= x_1 <= x_2 <= ...
```

Whenever `x_(k+1) != x_k`, at least one coordinate changes from `0` to `1`. No coordinate can ever change back to `0`, so there are at most `n` strict changes. After that, the state cannot increase further and therefore `F(x)=x`. QED. □

This means that in this finite class an explicit `FIX` operator is not mathematically forced if bounded iteration/control is already available: it can be unrolled to a known finite horizon.

It does **not** show that one strict BMF/BMCF data pass computes the fixed point, nor does it cover unbounded, infinite, transfinite, non-inflationary, or oscillatory dynamics.

## 2. Corollary BMCF-F1a — finite reachability is bounded iteration

For a directed graph on `n` vertices, define one Boolean reachability expansion step by

```text
R_A(v) = v OR A v
```

with Boolean OR/AND arithmetic. This map is inflationary. Therefore repeated reachability expansion stabilizes after at most `n` strict additions of vertices.

For a fixed finite `n`, transitive reachability from a seed can therefore be implemented by bounded iteration. `FIX` remains a useful control abstraction, but this finite witness does not establish it as an independent mathematical primitive. □

## 3. Theorem BMCF-Q1 — finite quotients admit a fixed-carrier equivalence representation

Let `X` be a finite set. There is a bijection between:

```text
partitions of X
```

and

```text
equivalence relations on X.
```

A partition `{B_i}` determines

```text
x ~ y  iff  x and y lie in the same block B_i,
```

and an equivalence relation determines its set of equivalence classes. These constructions are mutually inverse. QED. □

Hence a finite quotient can be represented without dynamically creating a smaller carrier: store the equivalence relation as a Boolean matrix on the original carrier `X`.

This defeats the naive promotion

```text
changing quotient cardinality -> QUOTIENT must be an independent fourth primitive.
```

The promotion is representation-dependent.

If the runtime specifically requires the actual quotient carrier `X/~` with canonical class labels, then carrier formation and canonical naming are additional structural obligations. v0.10 does not erase that type distinction.

## 4. Exhaustive finite partition control

The computation enumerates all set partitions for sizes `0..5` and checks the standard Bell counts:

```text
B_0=1, B_1=1, B_2=2, B_3=5, B_4=15, B_5=52.
```

Each partition is converted to an equivalence matrix and reconstructed from that matrix. The round trip must be exact and collision-free.

This is a finite implementation control for BMCF-Q1, not the proof itself.

## 5. Theorem BMCF-S1 — no permutation-equivariant selector exists on a bare finite set

Let `X` be a finite set with `|X|>=2`. There is no function assigning a distinguished element

```text
s(X) in X
```

that is invariant/equivariant under every permutation of the bare set while using no extra structure.

### Proof

Assume such a selector chooses `a=s(X)`. Since `|X|>=2`, choose `b!=a` and let `sigma` be the permutation swapping `a` and `b`. Equivariance would require

```text
s(X)=sigma(s(X)).
```

But `sigma(a)=b!=a`. Contradiction. QED. □

This upgrades the earlier finite enumeration witness to a general finite theorem.

## 6. Corollary BMCF-S1a — order supplies the missing structure

If `X` is equipped with a total order, then

```text
s(X)=min(X)
```

is canonical relative to that supplied order. Thus the obstruction is not "selection is impossible"; it is:

```text
canonical selection from a bare symmetric set is impossible without symmetry-breaking structure.
```

Therefore `SELECT` is not automatically a primitive. It may instead expose a missing-order/missing-structure requirement. □

## 7. Final finite classification of the fourth-operator candidates

The strongest statements now supported are:

```text
COUPLE:
    exact conditional necessity and exact depth inside finite polynomial BMCF.

FIX / ITERATE:
    one-pass BMF is insufficient for general closure,
    but finite inflationary Boolean fixed points admit bounded unrolling.
    Independent primitive: NOT ESTABLISHED.

QUOTIENT / COEQUALIZE:
    actual carrier formation is type-distinct,
    but finite partitions admit a fixed-carrier equivalence representation.
    Independent primitive: REPRESENTATION-DEPENDENT / NOT ESTABLISHED.

SELECT:
    impossible canonically on a bare finite set of size >=2,
    but becomes canonical after symmetry-breaking structure such as an order.
    Primitive status: NOT ESTABLISHED; structural requirement is proved.

RECIP / GATE:
    exact out-of-polynomial boundary witnesses from v0.9,
    global minimality: NOT ESTABLISHED.
```

## 8. No single fourth operator is promoted

The finite evidence does not justify collapsing all of these typed boundaries into one mathematical operation.

The honest runtime architecture is therefore:

```text
CORE DATA:
    BRANCH -> MAP -> FOLD

CONDITIONAL POLYNOMIAL DATA EXTENSION:
    COUPLE[omega_C]

TYPED AUXILIARY BOUNDARIES:
    RECIP | GATE | ITERATE/FIX | QUOTIENT | SELECT_WITH_STRUCTURE
```

A software dispatcher over those cases may be one implementation slot, but it is not one proved mathematical primitive.

## 9. v0.10 firewall

Forbidden promotions:

```text
finite bounded FIX unrolling -> all fixed points reducible to finite iteration     FORBIDDEN
partition/equivalence encoding -> all quotients/colimits are BMCF data operators   FORBIDDEN
no bare selector -> Choice theorem or universal SELECT minimality                   FORBIDDEN
ordered min selector -> every selection problem solved by order                     FORBIDDEN
typed AUX family -> one universal fourth mathematical operator                      FORBIDDEN
v0.10 -> RH, Collatz, or unrelated open problems                                    FORBIDDEN
```

## 10. Closure status

For the finite research programme, every major candidate is now assigned one of:

```text
PROVED SCOPED RESULT
FALSIFIED OVERPROMOTION
REPRESENTATION/TYPE BOUNDARY
OPEN / NOT CLAIMED
```

This is sufficient to proceed to a v1.0 freeze without pretending the open boundaries have been solved.
