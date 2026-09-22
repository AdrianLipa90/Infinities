# Claim ledger v1.18 — Cartan–SUSY spectral duality

This ledger is additive to \`CLAIMS_V1_17.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-251 | For any finite bipartite incidence operator \(B\), the odd self-adjoint operator \(D_B=\begin{psmallmatrix}0&B^\dagger\\B&0\end{psmallmatrix}\) gives the SUSY Hamiltonian \(H_B=D_B^2\) | STANDARD / EXACT | direct block multiplication |
| INF-252 | With \(C_B=2I-D_B\), one has the exact polynomial identity \(H_B=(2I-C_B)^2\), equivalently \(4I-H_B=C_B(4I-C_B)\) | EXACT | algebraic identity + validator |
| INF-253 | The spectral dictionary is \(\lambda_H=\lambda_D^2\), \(\lambda_C=2-\lambda_D\) | EXACT | functional calculus |
| INF-254 | SUSY zero modes are exactly \(C_B\)-eigenvectors of eigenvalue \(2\) | EXACT | INF-252/253 |
| INF-255 | Affine Cartan null vectors are \(D_B\)-eigenvectors of eigenvalue \(+2\) and hence \(H_B\)-eigenvectors of energy \(4\) | EXACT | INF-252/253 |
| INF-256 | For simply-laced bipartite graph normalization \(C_B=2I-D_B\), finite/affine/indefinite behavior is equivalent to \(\lambda_{\max}(H_B)<4,=4,>4\) | EXACT SPECTRAL CLASSIFICATION | self-adjoint spectral theorem |
| INF-257 | For \(B_n=[I_n\mid\mathbf1_n]\), \(\lambda_{\max}(H_n)=n+1\), so affine criticality occurs iff \(n=3\) | EXACT | cyclic-arm spectrum |
| INF-258 | In affine \(E_6\), \(\operatorname{spec}(D)=\{-2,-1,-1,0,1,1,2\}\), \(\operatorname{spec}(H)=\{0,1,1,1,1,4,4\}\), and \(\operatorname{spec}(C)=\{0,1,1,2,3,3,4\}\) | EXACT | block/Fourier spectrum |
| INF-259 | The protected Hilbert-Hotel mode and affine positive mode are distinct orthogonal spectral endpoints of the same \(C_3\)-invariant SUSY block, at energies \(0\) and \(4\) | EXACT | v1.17 + spectral identity |
| INF-260 | The value \(4\) is a physical energy prediction | FALSE | it is dimensionless and fixed by the Cartan normalization \(2I-A\) |
| INF-261 | The Cartan–SUSY spectral-duality packaging is literature-first | CANDIDATE ONLY / PRIORITY AUDIT REQUIRED | dedicated literature search required |
| INF-262 | The theorem proves physical \(E_6\) gauge symmetry or supersymmetry in Nature | FALSE / NOT CLAIMED | physical evidence required |

## v1.18 core

The graph Cartan operator and the supersymmetric Hamiltonian are two polynomial views of the same bipartite Dirac/McKay operator:

\[
\boxed{
D_B=
\begin{pmatrix}0&B^\dagger\\B&0\end{pmatrix},
\qquad
H_B=D_B^2,
\qquad
C_B=2I-D_B,
}
\]

so

\[
\boxed{
H_B=(2I-C_B)^2.
}
\]

This separates two modes that must not be conflated:

\[
H_B\psi=0
\iff
C_B\psi=2\psi,
\]

whereas

\[
C_Bd=0
\iff
H_Bd=4d.
\]

For the cyclic-arm family the affine threshold is therefore exactly the SUSY-Hamiltonian threshold \(E_{\max}=4\), which occurs only at \(n=3\).
