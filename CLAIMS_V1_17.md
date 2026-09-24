# Claim ledger v1.17 — Affine-E6 Fourier Hilbert-Hotel core

This ledger is additive to \`CLAIMS_V1_16.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-239 | Tensoring binary-tetrahedral irreps by the one-dimensional character \(\eta\) acts as the three-arm automorphism of the affine-\(\widetilde E_6\) McKay graph | STANDARD REPRESENTATION-RING FACT + EXACT SPECIALIZATION | fusion rules |
| INF-240 | In the ordered parity bases, the affine-\(E_6\) incidence block is \(B=[I_3\mid\mathbf1_3]\) and is \(C_3\)-equivariant | EXACT | direct matrix/action |
| INF-241 | Exact \(C_3\) Fourier reduction gives \(B\simeq[1,\sqrt3]\oplus[1]\oplus[1]\) | EXACT | DFT validator |
| INF-242 | The invariant block \([1,\sqrt3]\) is unitarily equivalent to \([2,0]\), hence Fredholm-homotopic to the canonical deletion map \([1,0]\) | EXACT | explicit unitary normal form |
| INF-243 | The full graph Witten/Fredholm index \(+1\) is entirely localized in the trivial \(C_3\) character block; the two nontrivial character blocks are invertible and index-zero | EXACT | block decomposition |
| INF-244 | The protected kernel mode \(v_0=(1,1,1,-1)\) and affine positive mode \(d_+=(1,1,1,3)\) are orthogonal \(C_3\)-invariant directions with \(B^\dagger B\) eigenvalues \(0\) and \(4\) | EXACT | matrix validator |
| INF-245 | The affine spectral radius \(2\) is carried by the same trivial-character block through its nonzero singular value \(2\); the two nontrivial character blocks have singular value \(1\) | EXACT | block singular spectrum |
| INF-246 | After standard Fredholm stabilization, the full affine-\(E_6\) incidence system and its trivial-character core represent the same unit Hilbert-Hotel class \([S^\dagger]\) | STANDARD FREDHOLM CLASSIFICATION COROLLARY | INF-242/243 |
| INF-247 | The \(C_3\)-orbit quotient produces the coefficient \(\sqrt3\) canonically from normalized collapse of three equal arms | EXACT | invariant-subspace normalization |
| INF-248 | In the declared graph-SUSY model, affine criticality and Fredholm defect are co-localized in the same \(C_3\)-invariant symmetry quotient | EXACT | INF-243/245 |
| INF-249 | The decomposition implies that physical/internal Fock Witten index equals the graph-incidence index | FALSE | graph/Fock index firewall retained |
| INF-250 | The co-localization theorem is literature-first | CANDIDATE ONLY / PRIORITY AUDIT REQUIRED | dedicated novelty search required |

## v1.17 core

The affine-\(E_6\) graph admits an exact character decomposition

\[
\boxed{
B_{\widetilde E_6}
\simeq
[1,\sqrt3]
\oplus
[1]
\oplus
[1].
}
\]

The invariant block obeys

\[
[1,\sqrt3]
\sim_{\rm unitary}
[2,0]
\sim_{\rm Fredholm}
[1,0].
\]

Therefore the protected index defect and the affine-critical singular value both sit in the same trivial-\(C_3\) quotient block, while the two nontrivial character sectors are invertible spectators.
