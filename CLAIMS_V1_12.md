# Claim ledger v1.12 — C3 arm reconstruction and McKay-index localization

This ledger is additive to \`CLAIMS_V1_11.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-173 | Each conserved 16-state \(N=2\) long-multiplet sector has parity decomposition \(5\cdot\chi^r\oplus3\) in the even sector and \(4\cdot\rho\chi^r\) in the odd sector after restriction to the diagonal \(2T\) subgroup | EXACT | character decomposition + long-multiplet structure |
| INF-174 | The irrep-type support of one conserved sector is exactly one affine-\(E_6\) arm \(\chi^r-\rho\chi^r-3\) | EXACT | fusion/selection-rule audit |
| INF-175 | The union of the three \(C_3\)-related long-multiplet arm supports, after identifying the common triplet irrep type, is exactly the full affine-\(E_6\) McKay graph | EXACT | finite support validator |
| INF-176 | The affine-\(E_6\) bipartite incidence block is \(B=[I_3\mid\mathbf1_3]\) and is \(C_3\)-equivariant under cyclic arm permutation | EXACT | matrix identity |
| INF-177 | After the \(C_3\) Fourier transform, \(B\) decomposes into two invertible nontrivial-character scalar channels and one trivial-character block \((1,\sqrt3):\mathbb C^2\to\mathbb C\) | EXACT | Fourier/matrix factorization |
| INF-178 | The graph-incidence index \(+1\) is localized entirely in the trivial \(C_3\) Fourier channel | EXACT | block-index decomposition |
| INF-179 | The unique graph zero mode \(v_0=(1,1,1,-1)\) is \(C_3\)-invariant and orthogonal to the affine positive dimension vector \(d_+=(1,1,1,3)\) | EXACT | exact validator |
| INF-180 | The eigenvalues of \(B^\dagger B\) split as \(0\) on the protected trivial-\(C_3\) graph mode, \(1,1\) on the two nontrivial arm modes, and \(4\) on the affine dimension-vector mode | EXACT | exact matrix identities |
| INF-181 | Each 16-state long multiplet has Fock Witten index \(0\), and the full 48-state carrier has Fock Witten index \(0\) | STANDARD LONG-MULTIPLET FACT + EXACT COUNT | parity dimensions \(8=8\) per sector |
| INF-182 | The graph-incidence Witten index \(+1\) is not the physical/internal Fock Witten index; it arises after decategorifying irrep spaces and multiplicities to one-dimensional graph nodes | EXACT STATUS DISTINCTION | INF-176..181 |
| INF-183 | The identity \(\widetilde E_6=C_3\)-orbit closure of one \(N=2\) long-multiplet arm is claimed to be literature-first | CANDIDATE ONLY / NOT YET CLAIMED | priority audit required |
| INF-184 | The graph-index localization proves an \(E_6\) gauge theory or a nonzero physical Witten index | FALSE / NOT CLAIMED | representation-support firewall |

## v1.12 core

The finite supersymmetry carrier resolves the affine-\(E_6\) support into three conserved \(C_3\) sectors:

\[
\boxed{
\widetilde E_6
=
\bigcup_{r\in\mathbb Z_3}
\left(
\chi^r-\rho\chi^r-3
\right).
}
\]

The graph-level index \(+1\) is a separate decategorified invariant and is concentrated in the trivial \(C_3\) Fourier block. The actual long-multiplet Fock Witten index remains zero.
