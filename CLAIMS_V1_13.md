# Claim ledger v1.13 — Cyclic-arm criticality and affine-E6 selection

This ledger is additive to \`CLAIMS_V1_12.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-185 | For the uniform \(n\)-arm two-step star, the bipartite block is \(B_n=[I_n\mid\mathbf1_n]:\mathbb C^{n+1}\to\mathbb C^n\) and is \(C_n\)-equivariant under cyclic arm rotation | EXACT | explicit matrix/action |
| INF-186 | \(B_n\) is surjective with one-dimensional kernel spanned by \((1,\ldots,1,-1)\), so the graph-SUSY/Fredholm index is \(+1\) for every \(n\ge1\) | EXACT | rank/kernel validator |
| INF-187 | After the \(C_n\) Fourier transform, the nontrivial character blocks are scalar \(1\) and the trivial block is \((1,\sqrt n):\mathbb C^2\to\mathbb C\) | EXACT | Fourier decomposition |
| INF-188 | The equivariant index is the trivial \(C_n\) representation \([\mathbf1]\); equivalently the equivariant heat supertrace equals \(1\) on every group element | STANDARD EQUIVARIANT-INDEX FACT + EXACT SPECIALIZATION | Fourier proof |
| INF-189 | \(\operatorname{spec}(B_n^\dagger B_n)=\{0,1^{(n-1)},n+1\}\) and the full bipartite adjacency has spectral radius \(\sqrt{n+1}\) | EXACT | \(B_nB_n^\dagger=I+J\) |
| INF-190 | For \(C_n^{\rm Cartan}=2I-A_n\): \(n<3\) gives positive definite, \(n=3\) positive semidefinite corank one, and \(n>3\) indefinite | EXACT SPECTRAL CLASSIFICATION | INF-189 |
| INF-191 | The uniform two-step cyclic-arm family is affine-critical iff \(n=3\) | EXACT | \(\sqrt{n+1}=2\iff n=3\) |
| INF-192 | The critical graph \(\Gamma_3\) is the affine \(E_6\) Dynkin graph | STANDARD GRAPH IDENTIFICATION + EXACT SPECIALIZATION | seven-node degree/edge audit |
| INF-193 | The positive Perron vector has source part \((1,\ldots,1,n)\) and target part \(\sqrt{n+1}(1,\ldots,1)\); at \(n=3\) this becomes the integral affine-\(E_6\) dimension vector \((1,1,1,3;2,2,2)\) | EXACT | eigenvector validator |
| INF-194 | The protected graph-SUSY zero mode \((1,\ldots,1,-1)\) is orthogonal to the positive Perron source vector \((1,\ldots,1,n)\) for every \(n\) | EXACT | direct identity |
| INF-195 | At the affine point, the even-sector Hamiltonian hierarchy is \(0\) on the protected trivial-\(C_3\) mode, \(1\) on the two nontrivial \(C_3\) arm modes, and \(4\) on the affine dimension mode | EXACT | Fourier/spectral decomposition |
| INF-196 | The unit graph-SUSY index selects \(n=3\) | FALSE | index is \(+1\) for all \(n\); affine spectral criticality is the selector |
| INF-197 | Within this declared uniform cyclic two-step-arm family, the same threefold arm count appearing in the conserved internal \(C_3\) is uniquely the affine-ADE critical arm count | EXACT FAMILY-LEVEL SELECTION | INF-191 + v1.11/v1.12 |
| INF-198 | The cyclic-arm criticality theorem is literature-first or physically identifies the three arms with particle generations | NOT CLAIMED / OPEN | priority audit and physical binding required |

## v1.13 core

The topological and spectral mechanisms are now separated:

\[
\operatorname{ind}(B_n)=1
\quad\text{for every }n,
\]

while

\[
\rho(A_n)=2
\iff
n=3.
\]

Thus the Hilbert-Hotel/Fredholm defect is universal across the arm family, whereas affine closure uniquely selects three arms. At the selected point the graph is exactly \(\widetilde E_6\), and its positive affine vector is the binary-tetrahedral McKay dimension vector.
