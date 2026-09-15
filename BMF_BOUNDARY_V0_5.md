# BMF Boundary v0.5

Status: **ADVERSARIAL BOUNDARY ANALYSIS / EXACT FINITE CLASSIFICATIONS AND COUNTEREXAMPLES**

This stage is deliberately destructive. It asks where the v0.4 finite-kernel theorem stops, without broadening the definitions to manufacture universality.

## 1. The class that remains exact

For a finite input set `X`, finite output set `Y`, and supplied semiring-like operations, v0.4 implements

```text
(T_K f)(y) = fold_x( K(y,x) mul f(x) )
```

as `F o M_K o B`. That factorization remains exact for the defined class. v0.5 does not weaken it.

## 2. Boolean-semiring classification

For two Boolean inputs and one Boolean output with `add = OR` and `mul = AND`, every one-pass kernel BMF operator has the form

```text
T(x1,x2) = (k1 AND x1) OR (k2 AND x2),  k1,k2 in {0,1}.
```

There are therefore exactly four represented Boolean functions: constant zero, `x1`, `x2`, and `x1 OR x2`. The other 12 of the 16 binary Boolean functions are outside this class.

**Theorem BMF-B1.** The two-input/one-output Boolean-semiring kernel class contains exactly four Boolean functions.

**Proof.** The kernel is determined by the two coefficients `(k1,k2) in {0,1}^2`, so there are at most four operators. The four coefficient pairs produce four distinct truth tables. `QED`.

## 3. Stacking does not escape semiring linearity

Kernel BMF maps are semimodule-linear maps. Composition of semimodule-linear maps is semimodule-linear. Exhaustive finite enumeration for hidden widths 1, 2, and 3 independently confirms that two-layer Boolean-semiring networks still realize exactly the same four two-input/one-output truth tables.

**Corollary BMF-B2.** Merely stacking finite Boolean-semiring kernel BMF layers does not make the class functionally complete. `QED`.

This is a statement about the strict v0.4 kernel class, not about arbitrary nonlinear MAP or FOLD definitions.

## 4. A nonlinear real counterexample

Over the ordinary real additive/multiplicative structure, a one-input/one-output kernel transform is linear in its input. The map `x -> x^2` is not additive:

```text
T(2+3) = 25
T(2) + T(3) = 13.
```

Hence `x -> x^2` is not a member of the strict real kernel-BMF class. `QED`.

## 5. ITERATE/FIXPOINT is not identical to one pass

Consider the directed path `0 -> 1 -> 2`, use Boolean reachability with kernel `I OR A`, and start from `(1,0,0)`. One pass gives `(1,1,0)`; a second gives `(1,1,1)`. Therefore one BMF pass is not, in general, transitive closure or fixed-point computation.

This supports a type distinction between a BMF **data plane** and an `ITERATE/FIXPOINT` **control plane**. It does **not** prove that iteration is a universally minimal fourth primitive.

## 6. Quotient/coequalizer carrier boundary

For all 81 pairs of maps `A_2 => B_3`, exhaustive coequalizer enumeration gives partition profiles:

```text
1+1+1 :  9
2+1   : 48
3     : 24
```

Thus the quotient carrier may have cardinality 3, 2, or 1 depending on the maps. Similarly, for all 16 spans `B_2 <- A_2 -> C_2`, finite pushout cardinality is 2 in 12 cases and 3 in 4 cases.

The strict kernel transform assumes an output carrier `Y` is already supplied. Carrier formation by quotient is therefore not literally the same typed operation as evaluation of a kernel on a fixed `Y`. This is a **boundary observation**, not a proof that `QUOTIENT` is an independent primitive. Encodings into an ambient fixed carrier remain possible.

## 7. Anti-tautology guard

Allowing arbitrary unary maps while keeping the fold fixed gives only partial coverage of the 16 binary Boolean functions:

```text
OR fold  : 10/16
AND fold : 10/16
XOR fold :  8/16
```

If the binary FOLD itself is allowed to be an arbitrary target function, all 16 are trivially representable. That is not evidence for a universal BMF grammar; it simply hides the target computation inside a primitive.

**Rule:** a primitive family must be constrained independently of the target theorem before universality or minimality can be tested.

## 8. v0.5 epistemic firewall

The following promotions are forbidden:

- finite-kernel exactness -> universal computation;
- finite Boolean enumeration -> a theorem about all semirings or all carriers;
- the quotient type mismatch -> proof of an independent fourth primitive;
- one reachability counterexample -> universal necessity of `FIXPOINT`;
- unrestricted MAP/FOLD encodings -> evidence of non-tautological universality;
- any v0.5 result -> proof of RH, Collatz, or another open problem.

The current architecture should therefore be read as:

```text
DATA:       BRANCH -> MAP -> FOLD     [exact finite-kernel class]
CONTROL:    ITERATE / FIXPOINT        [boundary candidate]
STRUCTURE:  QUOTIENT / COEQUALIZE     [boundary candidate]
SELECT:     symmetry-breaking boundary, still open as a primitive question
```

Universal minimality remains **OPEN / NOT CLAIMED**.
