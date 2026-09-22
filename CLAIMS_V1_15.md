# Claim ledger v1.15 — Affine-critical C6 supergrading selection

This ledger is additive to \`CLAIMS_V1_14.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-213 | For the uniform cyclic-arm family with commuting arm symmetry \(C_n\) and fermion parity \(Z_2^F\), the joint finite grading group is \(C_n\times Z_2^F\) | EXACT | direct product action |
| INF-214 | \(C_n\times C_2\cong C_{2n}\) iff \(n\) is odd; for odd \(n\), \(G_{2n}=R_n(-1)^F\) has order \(2n\) | STANDARD FINITE GROUP FACT + EXACT SPECIALIZATION | arithmetic validator |
| INF-215 | For odd \(n\), a supercharge preserving the \(C_n\) arm charge and flipping fermion parity has cyclic degree \(n\) in \(C_{2n}\): \(Q:\mathcal H_q\to\mathcal H_{q+n}\) | EXACT | grading calculation |
| INF-216 | The graph-incidence operator \(B_n=[I_n\mid\mathbf1_n]\) has Fredholm/index defect \(+1\) for every \(n\ge1\), so the topological defect does not select the arm count | EXACT | cyclic-arm theorem |
| INF-217 | The adjacency spectral radius is \(\rho(A_n)=\sqrt{n+1}\), hence the simply-laced Cartan-type matrix \(2I-A_n\) is affine-critical iff \(n=3\) | EXACT | cyclic-arm spectral theorem |
| INF-218 | At the unique affine-critical point \(n=3\), the graph is \(\widetilde E_6\) and the joint grading is \(C_3\times Z_2^F\cong C_6\) | EXACT | INF-214 + INF-217 |
| INF-219 | At the selected affine point, compensated supercharges have degree \(3\) modulo \(6\) | EXACT | INF-215 with \(n=3\) |
| INF-220 | Within the declared uniform cyclic two-step-arm family, affine \(E_6\) criticality selects the same threefold arm count whose combination with supersymmetric parity yields the sixfold cyclic grading | EXACT FAMILY-LEVEL SELECTION | INF-217..219 |
| INF-221 | The universal unit Fredholm/Witten graph index itself selects \(n=3\) or \(C_6\) | FALSE | index is \(+1\) for all \(n\) |
| INF-222 | The selected mathematical \(C_6\) proves the physical IDT \(6\pi\) phase budget or identifies time with the SUSY grading | FALSE / NOT CLAIMED | representation crosswalk only |
| INF-223 | The selected \(C_6\) proves that Stage-23 chirality is physical fermion parity | OPEN / NOT CLAIMED | sector-binding theorem required |
| INF-224 | The affine-critical \(E_6\to C_6\) selection packaging is literature-first | CANDIDATE ONLY / PRIORITY AUDIT REQUIRED | dedicated novelty search required |

## v1.15 core

The topological and spectral selectors are now sharply separated:

\[
\operatorname{ind}(B_n)=1
\quad
\forall n,
\]

while

\[
\rho(A_n)=2
\iff
n=3.
\]

Thus affine spectral criticality, not the protected Fredholm defect, selects the three-arm member. Because three is odd,

\[
C_3\times Z_2^F\cong C_6,
\]

and the supercharges acquire degree \(3\) modulo \(6\). Within this family,

\[
\boxed{
\widetilde E_6\text{ criticality}
\Longrightarrow
C_6\text{-refined supersymmetry grading}.
}
\]
