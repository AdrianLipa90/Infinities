# GREMLIN-INFINITIES-SWEEP v0.1 — falsification report

Status: `RUN_COMPLETE_LOCAL_REFERENCE`
Target branch: `feat/computational-infinities-v0.1`
Main branch mutation: `NO`

## Scope

This run tests a finite, typed catalog. It does **not** prove that the operator vocabulary is mathematically minimal or universal.

Baseline dynamic vocabulary:

`SHIFT, SCALE, BRANCH, FACTOR, INVERT`

Holdout extension candidates:

`AVERAGE, TRANSFORM, POWERSET, STOCHASTIC`

## Results

- Training catalog: **PASS 19/19** under the baseline vocabulary.
- Holdout catalog: **FAIL 8/13** under the baseline vocabulary.
- Uncovered holdouts: `H04, H05, H06, H07, H13`.
- Missing typed operations exposed by those holdouts:
  - `AVERAGE`: 1 case
  - `TRANSFORM`: 2 cases
  - `POWERSET`: 1 case
  - `STOCHASTIC`: 1 case
- Full finite catalog: **27/32 = 84.375%** covered by baseline.
- Smallest vocabulary under the preregistered finite schema: **9 typed operations**.
- Universal `[1/2]` seam hypothesis: **FAIL**.

Natural fixed-point / limit counterexamples to a universal half seam in the catalog:

- `epsilon_0`
- `sqrt(2)` from continued-fraction iteration
- `-1` for the 2-adic geometric series
- `sqrt(2)` from Newton iteration
- `phi` from the golden-ratio continued fraction

Confirmed half appearances remain real but mechanism-specific:

- equal binary Cantor weights
- Cantor information/fractal relation
- inversion after radial compactification
- Cesaro sum of Grandi's series

Therefore `[1/2]` is not promoted to a universal fixed point of infinity. A weaker hypothesis remains viable: half is a distinguished seam in **binary-balanced and complement/involution-normalized sectors**.

## GREMLIN-style verdicts

`baseline_fits_training_catalog = PASS`

`baseline_generalizes_to_all_holdouts = FAIL`

`universal_half_seam = FAIL`

`finite_catalog_extended_grammar = PASS`

`minimality_is_mathematical_theorem = NO`

`rh_proof = NO`

`collatz_proof = NO`

## Interpretation boundary

The 9-operation minimum is a result of the explicit finite representation schema used by this computation. It is not a proof that nine primitive generators are irreducible in mathematics. Alternative encodings may reduce or alter the vocabulary.

The immediate research target is therefore not to defend the original five operators. It is to test whether the four exposed extensions can themselves be derived from compositions, quotients, or completion operators already present at a deeper level.

Result payload SHA-256 (compact result, before self-hash insertion):

`59fd28cb688d382b17be8b59d00c4c132d0627eeff3621de556df771909908ea`
