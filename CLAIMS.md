# Claim ledger v0.8

| ID | Claim | Status | Computational test |
|---|---|---|---|
| INF-001 | `q(1/x)=1-q(x)`, `eta(1/x)=-eta(x)`, `B(1/x)=-B(x)` for `x>0` | EXACT | `validate_infinities_v0_1.py` |
| INF-002 | `x=1` maps to the self-dual seam `q=1/2` | EXACT | validator |
| INF-003 | Uniform Cantor information dimension equals `ln(2)/ln(3)` | STANDARD_THEOREM / EXACT FORMULA | validator |
| INF-004 | `prod_{n=2}^N(1-1/n)=1/N` | EXACT | validator |
| INF-005 | Finite continued-fraction convergents approach `sqrt(2)` | STANDARD_THEOREM / NUMERICAL_WITNESS | validator |
| INF-006 | `1+2+4+...` tends to `-1` in `Q_2` | STANDARD_THEOREM / EXACT ERROR NORM | validator |
| INF-007 | Compactified accelerated odd-Collatz branch is Möbius on each valuation branch | EXACT LOCAL STRUCTURE | validator witnesses |
| INF-008 | Global Collatz convergence follows from INF-007 | OPEN / FORBIDDEN PROMOTION | none |
| INF-009 | Gabriel family has finite volume iff `p>1/2`, finite area iff `p>1` | STANDARD_THEOREM | analytic criterion |
| INF-010 | `rank(I-U^k U*^k)=k`, `ind(U^k)=-k` | STANDARD_THEOREM | validator |
| INF-011 | Finite Euler/Dirichlet approximants approach `zeta(2)` | NUMERICAL_WITNESS | validator |
| INF-012 | The v0.1 five-generator vocabulary is minimal beyond its finite catalogue encoding | NOT ESTABLISHED / SUPERSEDED BY NORMALIZATION | `gremlin_sweep_v0_1.py` + v0.4 normalization |
| INF-013 | `[1/2]` is the unique universal seam across all infinity sectors | FALSIFIED IN CATALOGUED NATURAL-SEAM TEST / UNIVERSAL CLAIM NOT SUPPORTED | `gremlin_sweep_v0_1.py` |
| INF-014 | Every finite kernel operator `(T_K f)(y)=⊕_x K(y,x)⊗f(x)` factors exactly as `F ∘ M_K ∘ B` | EXACT (DEFINED CLASS) | `validate_bmf_v0_4.py` |
| INF-015 | DFT, finite Markov transition, Boolean adjacency, divisibility-zeta, Walsh-Hadamard, Dirichlet convolution and finite tensor contraction admit the implemented BMF factorization | NUMERICAL/FINITE WITNESS | `bmf_ood_v0_4.py` |
| INF-016 | A bare finite set of size `2..5` has no distinguished element equivariant under its full permutation group | FINITE OBSTRUCTION / EXACT ENUMERATION | `validate_bmf_v0_4.py` |
| INF-017 | `MAP-BRANCH-FOLD` is a universal minimal grammar for all mathematics of infinity | OPEN / NOT CLAIMED | v0.5-v0.8 expose boundaries beyond the strict finite-kernel class |
| INF-018 | Choice-like witness selection always requires a fourth primitive `SELECT` | OPEN / NOT CLAIMED | current result only isolates a symmetry obstruction without extra structure |
| INF-019 | The two-input/one-output Boolean-semiring kernel-BMF class contains exactly four of the sixteen Boolean functions | EXACT FINITE CLASSIFICATION | `validate_bmf_boundary_v0_5.py` |
| INF-020 | Stacking finite Boolean-semiring kernel-BMF layers does not escape semimodule linearity or yield functional completeness | EXACT ALGEBRAIC CLOSURE; FINITE ENUMERATION WITNESS | `bmf_boundary_v0_5.py` |
| INF-021 | Over ordinary real addition/multiplication, `x -> x^2` is outside the strict one-input/one-output kernel-BMF class | EXACT COUNTEREXAMPLE | `bmf_boundary_v0_5.py` |
| INF-022 | One Boolean adjacency/reachability BMF pass is not in general identical to transitive closure or fixed-point iteration | EXACT COUNTEREXAMPLE | `bmf_boundary_v0_5.py` |
| INF-023 | Finite quotient/coequalizer carrier formation is not literally the same typed operation as evaluating a kernel on a pre-supplied fixed output carrier | TYPE BOUNDARY / FINITE EXHAUSTIVE WITNESS; INDEPENDENT PRIMITIVE NOT PROVED | `bmf_boundary_v0_5.py` |
| INF-024 | If an unrestricted FOLD may encode the target function itself, apparent BMF universality becomes tautological | EXACT MODELING WARNING | `bmf_boundary_v0_5.py` |
| INF-025 | A fixed dynamic-dynamic multiplication operator `COUPLE` strictly extends the strict real kernel-BMF class: branching `x` twice and coupling gives `x^2` | EXACT CONSTRUCTION | `fourth_operator_search_v0_6.py` |
| INF-026 | Over Boolean variables/constants, closure under fixed OR and dynamic AND contains exactly the six two-variable monotone Boolean functions | EXACT FINITE CLASSIFICATION | `validate_fourth_operator_v0_6.py` |
| INF-027 | With the separately fixed local unary library `{ZERO, ONE, ID, NOT}`, dynamic AND plus OR-fold realizes all 16 two-variable Boolean functions; general finite Boolean representation follows by DNF | EXACT FINITE ENUMERATION + STANDARD DNF CONSTRUCTION | `fourth_operator_search_v0_6.py` |
| INF-028 | Fixed `ITE` with constants/variables is Boolean-functionally complete by Shannon expansion | STANDARD BOOLEAN CONSTRUCTION / FINITE ENUMERATION WITNESS | `fourth_operator_search_v0_6.py` |
| INF-029 | `COUPLE` is the unique or universally minimal fourth primitive | OPEN / NOT CLAIMED | v0.7-v0.8 prove scoped polynomial results, not uniqueness across grammars |
| INF-030 | One optional software `AUX` slot with typed variants is one mathematical fourth operator | FALSE AS STATED / TYPE DISTINCTION PRESERVED | `FOURTH_OPERATOR_SEARCH_V0_6.md` |
| INF-031 | Every finite left-coefficient word-polynomial over a supplied semiring-like algebra factors exactly through typed `BRANCH -> MAP -> COUPLE -> FOLD` | EXACT (DEFINED CLASS) | `validate_bmcf_v0_7.py` |
| INF-032 | Over a commutative semiring, every finite polynomial with fixed coefficients is BMCF-representable | EXACT COROLLARY OF INF-031 | `bmcf_polynomial_v0_7.py` |
| INF-033 | Every finite multilinear kernel operator of the specified tensor form factors exactly through BMCF | EXACT (DEFINED CLASS) | `validate_bmcf_v0_7.py` |
| INF-034 | On a free-polynomial witness class with fixed scalar kernels, strict BMF has dynamic degree at most one while BMCF represents degree-two terms such as `x_1 x_2` | EXACT DEGREE-SEPARATION THEOREM | `validate_bmcf_v0_7.py` |
| INF-035 | The v0.7 polynomial factorization is mathematically novel relative to arithmetic-circuit/polynomial formalisms | NOT ESTABLISHED / NOT CLAIMED | requires literature comparison |
| INF-036 | In the finite polynomial grammar, any expression of nested binary-COUPLE depth `c` has dynamic total degree at most `2^c` | EXACT STRUCTURAL-INDUCTION THEOREM | `validate_bmcf_obstruction_v0_8.py` |
| INF-037 | In that grammar, strict BMF has COUPLE depth zero and therefore dynamic total degree at most one | EXACT COROLLARY OF INF-036 | `validate_bmcf_obstruction_v0_8.py` |
| INF-038 | With a supplied unit/scalar source, a finite polynomial target requires at least one `COUPLE` iff its dynamic total degree exceeds one | EXACT CONDITIONAL OBSTRUCTION (DEFINED CLASS) | `bmcf_obstruction_v0_8.py` |
| INF-039 | A nonzero finite polynomial of degree `d>=1` has exact minimal binary-COUPLE nesting depth `ceil(log2 d)` in the BMCF polynomial grammar | EXACT LOWER+UPPER BOUND (DEFINED CLASS) | `validate_bmcf_obstruction_v0_8.py` |
| INF-040 | The v0.8 degree/depth theorem is novel relative to arithmetic-circuit multiplicative-depth literature | NOT ESTABLISHED / NOT CLAIMED | requires literature comparison |

## v0.8 firewall

The exact v0.8 statements are scoped to the finite polynomial BMCF grammar with degree-one dynamic generators, fixed scalar coefficients, a supplied unit/scalar source, finite additive FOLD, and binary multiplicative COUPLE. The degree obstruction makes `COUPLE` conditionally necessary for polynomial degree greater than one inside this grammar; it does not prove that `COUPLE` is the unique nonlinear primitive or globally minimal across alternative grammars. `FIXPOINT`, `QUOTIENT/COEQUALIZE`, and symmetry-breaking `SELECT` remain type-distinct unresolved boundaries. Infinite folds require explicit topology, valuation, measure, completion, or convergence structure. The degree/depth relationship is close to standard arithmetic-circuit reasoning, so novelty is not claimed without literature comparison. No result here proves the Riemann Hypothesis, the Collatz conjecture, or universal completeness of BMCF.
