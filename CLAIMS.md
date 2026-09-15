# Claim ledger v0.4

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
| INF-017 | `MAP-BRANCH-FOLD` is a universal minimal grammar for all mathematics of infinity | OPEN / NOT CLAIMED | requires a theorem or counterexample beyond the implemented class |
| INF-018 | Choice-like witness selection always requires a fourth primitive `SELECT` | OPEN / NOT CLAIMED | current result only isolates a symmetry obstruction without extra structure |

## v0.4 firewall

The exact statement in INF-014 is scoped to the explicitly defined finite kernel class. Infinite folds require an explicit topology, valuation, measure, completion, or convergence rule. Finite OOD coverage must not be promoted to a proof of universal BMF completeness, the Riemann Hypothesis, or the Collatz conjecture.
