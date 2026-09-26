# Claim ledger v0.10 + post-v1.0 research extensions

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
| INF-016 | A bare finite set of size `2..5` has no distinguished element equivariant under its full permutation group | FINITE OBSTRUCTION / EXACT ENUMERATION; SUBSUMED BY INF-051 | `validate_bmf_v0_4.py` |
| INF-017 | `MAP-BRANCH-FOLD` is a universal minimal grammar for all mathematics of infinity | OPEN / NOT CLAIMED | v0.5-v0.10 expose typed boundaries beyond the strict finite-kernel class |
| INF-018 | Choice-like witness selection always requires a fourth primitive `SELECT` | OPEN / NOT CLAIMED | selector obstruction proves missing symmetry-breaking structure, not universal primitive minimality |
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
| INF-029 | `COUPLE` is the unique or universally minimal fourth primitive | OPEN / NOT CLAIMED | v0.7-v0.10 prove scoped polynomial results and distinct typed boundaries |
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
| INF-041 | For nonconstant univariate polynomials over an integral domain, `deg(P∘Q)=deg(P)deg(Q)`; polynomial composition therefore stays inside the v0.8 degree grammar | STANDARD/EXACT POLYNOMIAL THEOREM IN STATED DOMAIN | `validate_bmcf_boundary_v0_9.py` |
| INF-042 | Repeated squaring `S_{k+1}=S_k^2` has degree `2^k` and exact minimal binary-COUPLE depth `k` in the polynomial BMCF grammar | EXACT COROLLARY OF INF-039 + COMPOSITION/DEGREE CONSTRUCTION | `bmcf_boundary_v0_9.py` |
| INF-043 | The formal rational function `1/x` over `Q` is outside finite polynomial BMCF; `omega_C(1/x)` is undefined rather than a larger numeric depth | EXACT TYPE/ALGEBRAIC BOUNDARY | `validate_bmcf_boundary_v0_9.py` |
| INF-044 | The real function `|x|` is not polynomial although each of its two linear branches has degree one; branchwise degree therefore does not detect gated/piecewise structure | EXACT POLYNOMIAL IDENTITY OBSTRUCTION | `validate_bmcf_boundary_v0_9.py` |
| INF-045 | `omega_C` is a universal scalar measure of nonlinearity across polynomial, rational, and piecewise targets | FALSE / OUTSIDE DEFINED DOMAIN | `bmcf_boundary_v0_9.py` |
| INF-046 | `RECIP` or `GATE` is proved globally minimal or unique outside the polynomial grammar | OPEN / NOT CLAIMED | v0.9 proves only distinct typed boundary witnesses |
| INF-047 | Every inflationary map `F:{0,1}^n->{0,1}^n` reaches a fixed point from any start after at most `n` strict state changes | EXACT FINITE THEOREM | `validate_bmcf_final_boundary_v0_10.py` |
| INF-048 | Finite Boolean reachability from one seed can be resolved by bounded iteration; this does not establish `FIX` as an independent primitive | EXACT COROLLARY / INDEPENDENT PRIMITIVE NOT ESTABLISHED | `bmcf_final_boundary_v0_10.py` |
| INF-049 | Partitions of a finite set are in bijection with equivalence relations on that set, providing a fixed-carrier representation of finite quotients | STANDARD/EXACT FINITE THEOREM | `validate_bmcf_final_boundary_v0_10.py` |
| INF-050 | `QUOTIENT` is a representation-independent mandatory fourth primitive | NOT ESTABLISHED / REPRESENTATION-DEPENDENT TYPE BOUNDARY | `bmcf_final_boundary_v0_10.py` |
| INF-051 | No permutation-equivariant distinguished-element selector exists on a bare finite set of cardinality at least two | EXACT GENERAL FINITE THEOREM | `validate_bmcf_final_boundary_v0_10.py` |
| INF-052 | A supplied total order removes that selector obstruction via `min`; the missing ingredient is symmetry-breaking structure | EXACT CONSTRUCTION RELATIVE TO ORDER | `validate_bmcf_final_boundary_v0_10.py` |
| INF-053 | One universal fourth mathematical operator has been established across the polynomial, rational, gated, fixed-point, quotient, and selection boundaries | NOT ESTABLISHED / NOT CLAIMED | typed AUX architecture remains an implementation/type discipline |
| INF-054 | For `E(z)=exp(i*pi*z)`, `-1` is an exact fixed point; the fixed-point branch `EulerInfinity=-1` is named **Euler's Infinity** | DEFINITION + EXACT FIXED-POINT IDENTITY | `validate_eulers_infinity_v0_1.py` |
| INF-055 | `E'(-1)=-i*pi` and `|E'(-1)|=pi>1`, so the Euler fixed point is repelling under ordinary forward iteration | EXACT / STANDARD COMPLEX-DYNAMICS CRITERION | `validate_eulers_infinity_v0_1.py` |
| INF-056 | The algebraic square-root fibre of Euler's Infinity is `{+i,-i}` | EXACT | `validate_eulers_infinity_v0_1.py` |
| INF-057 | Fixed points of `X=exp(i*pi*X)` satisfy `X_k=(i/pi) W_k(-i*pi)` branchwise | EXACT BRANCHWISE IDENTITY | analytic derivation in `research/EULERS_INFINITY_V0_1.md` |
| INF-058 | On a declared logarithm branch, `E_k^{-1}(w)=2k-(i/pi)Log(w)`; finite inverse compositions form a countably branching preimage tree | EXACT ON DECLARED LOG BRANCH | `validate_eulers_infinity_v0_1.py` |
| INF-059 | Every infinite integer branch address converges to a well-defined geometric limit | OPEN / NOT CLAIMED | requires branch/domain/convergence theorem |
| INF-060 | The Euler preimage tree has a specific Hausdorff dimension or universal self-similar fractal law | OPEN / NOT CLAIMED | requires a precise dynamical/fractal invariant |

## Euler's Infinity extension firewall

Euler's Infinity is a post-v1.0 research extension. The exact fixed-point, derivative, square-root, Lambert-W, and inverse-branch identities do not imply convergence of arbitrary exponential towers. The notation for an infinite right-nested exponential is used only with an explicit fixed-point/branch interpretation. No specific fractal dimension, universal convergence law, or classical open-problem proof is promoted.

## v0.10 firewall

The finite programme now separates exact data-plane theorems from control, representation, and symmetry boundaries. `COUPLE` is conditionally necessary with exact depth only inside the defined finite polynomial grammar. Finite inflationary Boolean fixed points admit bounded unrolling, so their existence does not prove `FIX` primitive independence. Finite quotient structure can be encoded as an equivalence relation on a fixed carrier, so changing quotient cardinality alone does not prove `QUOTIENT` primitive independence. Bare finite sets of size at least two admit no permutation-equivariant canonical selector, but a supplied order resolves that obstruction; this proves a symmetry-breaking requirement, not universal `SELECT` minimality. `RECIP` and `GATE` remain distinct out-of-polynomial boundary witnesses. Infinite/transfinite processes, arbitrary colimits, Choice-sensitive constructions, and analytic completion remain outside these finite closure theorems. Novelty over established circuit/category/selection literature is not claimed without comparison. No result here proves the Riemann Hypothesis, the Collatz conjecture, or universal completeness of BMF/BMCF.


## Spectral von Mangoldt phase-bank extension

| ID | Statement | Status | Notes |
|---|---|---|---|
| INF-S001 | Landau's fixed-\(x\) zero formula reconstructs the von Mangoldt weight \(\Lambda(x)\). | STANDARD_THEOREM | Classical input. |
| INF-X010 | Combining Landau with the finite divisor identity reconstructs \(\log n\) from the zero-spectrum channels of its divisors. | EXACT_FROM_STANDARD | Finite divisor set. |
| INF-X011 | The dyadic tower \(2^j\) has renormalized spectral limit \(\log2\) at every fixed level \(j\). | STANDARD_COROLLARY | \(\Lambda(2^j)=\log2\). |
| INF-X012 | In a reverse Collatz fibre, \(a\to a+2\) adds exactly the two dyadic channels \(2^{a+1}\) and \(2^{a+2}\), totaling \(2\log2\). | EXACT | Local reverse-fibre statement only. |
| INF-N001 | First-256-zero phase-bank calculations reproduce the leading dyadic Landau response and give a GUE-closer-than-Poisson pair-correlation sanity check. | NUMERICAL_WITNESS | Diagnostic, not a proof of Montgomery-Dyson or RH. |
| INF-O003 | Any claimed cross-sector phase coherence beyond the Landau/von-Mangoldt contribution requires an independent null and preregistered statistic. | OPEN | Prevents re-labelling the built-in explicit-formula signal as a new effect. |
