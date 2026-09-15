# BMCF Conditional COUPLE v0.8 — degree obstruction and exact multiplicative depth

Status: **EXACT THEOREMS IN THE FINITE POLYNOMIAL GRAMMAR / CONDITIONAL ACTIVATION OF COUPLE / NOVELTY NOT CLAIMED**

This stage asks a narrower question than universal fourth-operator minimality:

> Within the finite polynomial BMCF grammar, when is dynamic-dynamic `COUPLE` mathematically forced, and how much nested coupling is minimally required?

The answer is exact for this defined class.

## 1. Grammar and scope

Work with finite polynomials in dynamic generators `x_1,...,x_n` over a coefficient ring/semiring where fixed scalar coefficients and a unit/scalar source are supplied. The data grammar is:

```text
BRANCH  : duplicate/index an existing dynamic channel
MAP     : multiply by a fixed scalar coefficient
COUPLE  : binary multiplication of two runtime expressions
FOLD    : finite addition
```

`BRANCH`, fixed-scalar `MAP`, and additive `FOLD` do not create dynamic degree greater than the maximum degree already present. `COUPLE` is the only primitive in this grammar that combines two dynamic degrees multiplicatively.

This is not a claim about arbitrary computation, FIXPOINT, QUOTIENT, SELECT, transcendental functions, infinite folds, or unrestricted MAP/FOLD definitions.

## 2. Definition — COUPLE depth

For an expression `E`, define the nested binary-COUPLE depth `delta_C(E)` recursively:

```text
delta_C(variable or scalar) = 0
delta_C(B(E))               = delta_C(E)
delta_C(M_a(E))             = delta_C(E)
delta_C(F(E_1,...,E_k))      = max_i delta_C(E_i)
delta_C(C(E_1,E_2))          = 1 + max(delta_C(E_1), delta_C(E_2))
```

For a nonzero polynomial `P`, let `deg(P)` denote dynamic total degree. Constants have degree 0; the zero polynomial is handled separately with obstruction index 0.

## 3. Theorem BMCF-C1 — degree bound by COUPLE depth

For every expression in the grammar,

```text
deg(E) <= 2 ^ delta_C(E).
```

### Proof

Proceed by structural induction.

- A dynamic generator has degree 1 and depth 0, so `1 <= 2^0`.
- A scalar has degree 0 and depth 0.
- `BRANCH` preserves the expression.
- fixed-scalar `MAP` does not increase dynamic degree.
- finite additive `FOLD` has degree at most the maximum degree of its inputs, while its COUPLE depth is their maximum.
- for `C(E_1,E_2)`, polynomial degree is at most `deg(E_1)+deg(E_2)`. If `m=max(delta_C(E_1),delta_C(E_2))`, the induction hypothesis gives

```text
deg(E_1)+deg(E_2) <= 2^m + 2^m = 2^(m+1),
```

and `delta_C(C(E_1,E_2))=m+1`.

Therefore the bound holds for all expressions. QED. □

## 4. Corollary BMCF-C2 — strict BMF degree obstruction

Strict BMF expressions have no `COUPLE`, hence `delta_C=0`. Therefore

```text
deg(E) <= 1.
```

So any polynomial target `P` with

```text
deg(P) > 1
```

cannot be represented by strict BMF in this polynomial grammar. At least one dynamic-dynamic `COUPLE` is required. QED. □

This gives a formal conditional activation flag:

```text
chi_C(P) = 1  if deg(P) > 1
           0  otherwise.
```

For the polynomial class, `chi_C(P)=1` is an exact obstruction to a zero-COUPLE realization. Constants require a supplied unit/scalar source, but they do not require dynamic-dynamic coupling.

## 5. Theorem BMCF-C3 — exact minimal COUPLE depth

Let `P` be a finite nonzero polynomial of total degree `d >= 1`. Then the minimum possible binary-COUPLE depth of any BMCF representation of `P` is

```text
ceil(log2 d).
```

### Lower bound

By BMCF-C1, any representation of depth `c` satisfies

```text
d <= 2^c,
```

so

```text
c >= ceil(log2 d).
```

### Upper bound

Each degree-`r` monomial can be formed by a balanced binary multiplication tree over its `r` dynamic factors, with depth `ceil(log2 r)`. All monomials can be constructed in parallel, fixed coefficients applied by `MAP`, and then combined by additive `FOLD`, which does not increase COUPLE depth. Since every monomial degree is at most `d`, the whole polynomial has a representation of depth at most `ceil(log2 d)`.

The lower and upper bounds coincide. QED. □

For constants and the zero polynomial, the required COUPLE depth is defined as 0.

## 6. Conditional obstruction index

Define

```text
omega_C(P) = 0                    if deg(P) <= 1
             ceil(log2 deg(P))    if deg(P) >= 2.
```

Within the finite polynomial grammar, `omega_C(P)` is exactly the minimal nested binary-COUPLE depth needed by the target.

Hence `COUPLE` is not activated by convention or taste. It is activated by a measurable obstruction:

```text
omega_C(P) > 0  =>  strict BMF is insufficient.
```

## 7. Computational controls

`computations/bmcf_obstruction_v0_8.py` independently checks:

- the activation boundary at degree 2;
- the closed formula against a dynamic-programming search for degrees 0..128;
- the degree ceiling `2^depth`;
- balanced monomial constructions for degrees 0..64;
- 200 deterministic random degree-obstruction trials;
- preservation of ordered noncommutative multiplication under balanced parenthesization, assuming associativity.

These are implementation and finite-search controls. They do not replace the proofs above.

## 8. TNT / anti-slop boundary

What v0.8 proves:

```text
strict BMF degree <= 1 in the defined polynomial grammar          PROVED
COUPLE is necessary for polynomial degree > 1                    PROVED
minimal binary-COUPLE depth = ceil(log2 degree)                   PROVED
```

What it does not prove:

```text
COUPLE is the unique possible nonlinear primitive                NOT CLAIMED
COUPLE is globally minimal across all grammars                    NOT CLAIMED
BMCF is a universal computation model                             NOT CLAIMED
FIXPOINT is reducible to COUPLE                                   NOT CLAIMED
QUOTIENT/COEQUALIZER is reducible to COUPLE                       NOT CLAIMED
SELECT is reducible without extra symmetry-breaking structure     NOT CLAIMED
novelty over arithmetic-circuit multiplicative-depth results      NOT ESTABLISHED
```

The degree/depth relationship is close to standard arithmetic-circuit reasoning. v0.8 establishes the statement for the repository's typed grammar; it does not assert priority over existing circuit-complexity literature.

## 9. Current architecture

```text
DEGREE <= 1:
    BRANCH -> MAP -> FOLD

DEGREE > 1:
    BRANCH -> MAP -> COUPLE[omega_C] -> FOLD
```

The unresolved non-data-plane boundaries remain separate:

```text
CONTROL:    FIX / ITERATE
STRUCTURE:  QUOTIENT / COEQUALIZE
SYMMETRY:   SELECT_WITH_STRUCTURE
```
