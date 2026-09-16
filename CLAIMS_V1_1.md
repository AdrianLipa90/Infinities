# Claim ledger v1.1 — infinite-fold extension

This file is additive to the frozen v1.0 claim ledger. `CLAIMS.md` remains the v1.0 freeze ledger; v1.1 claims begin here.

| ID | Claim | Status | Computational test |
|---|---|---|---|
| INF-054 | Every absolutely summable family in a Banach space has an enumeration-independent sum, defining a bounded linear `F_abs:l1(X;E)->E` with norm at most one | STANDARD THEOREM / PROVED | `validate_bmf_infinite_fold_v1_1.py` provides finite certificates only |
| INF-055 | On the domain where each mapped kernel row lies in `l1(X;E)`, the countable kernel operator factors exactly as `F_abs o M_K o B` | EXACT CONDITIONAL REPRESENTATION | `validate_bmf_infinite_fold_v1_1.py` |
| INF-056 | If `C=sup_y sum_x |K(y,x)|<infinity`, then the scalar-kernel operator maps `l-infinity(X;E)` boundedly to `l-infinity(Y;E)` with operator norm at most `C` | STANDARD THEOREM / PROVED | exact finite row-bound witness |
| INF-057 | Completeness cannot simply be removed: in `c_00` with the `l1` norm, `sum 2^{-n}e_n` is absolutely Cauchy but its limit lies outside `c_00` | EXACT COUNTEREXAMPLE | exact geometric tail certificate |
| INF-058 | `l2` control of terms alone does not imply existence of the ordinary additive fold: `a_n=1/n` is square-summable but its scalar series diverges | STANDARD / EXACT COUNTEREXAMPLE | dyadic harmonic lower bounds + `sum 1/n^2<=2` certificate |
| INF-059 | Conditional convergence cannot define a general enumeration-independent scalar fold; the alternating harmonic series is rearrangement-sensitive | STANDARD THEOREM / COUNTEREXAMPLE FRAME | finite alternating-prefix witness; infinite fact is theorem-level, not computational |
| INF-060 | `F_abs` is a universal infinite fold covering conditional, measure-theoretic, p-adic, transfinite, or arbitrary completed processes | FALSE AS PROMOTION / NOT CLAIMED | v1.1 firewall |
| INF-061 | The v1.1 absolute-fold extension is mathematically novel relative to Banach-space series/operator theory | NOT ESTABLISHED / NOT CLAIMED | requires literature comparison |

## v1.1 firewall

The v1.1 result is an exact extension of the repository's BMF factorization to a countable **absolute-convergence** domain in a complete normed carrier. The proofs are standard Banach-space arguments expressed in the repository's typed operator language. Finite computations are implementation/certificate controls and do not replace the infinite proofs. Absolute convergence is a clean sufficient domain; it is not claimed to be necessary for every unconditional series in arbitrary Banach spaces. No claim is made about arbitrary integrals, non-absolute unconditional summation, p-adic completion, transfinite iteration, the Riemann Hypothesis, the Collatz conjecture, or the Twin Prime conjecture.
