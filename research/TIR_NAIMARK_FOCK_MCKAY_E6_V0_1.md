# TIR Naimark–Fock–McKay E6 Representation Theorem v0.1

Status: EXACT_2T_NAIMARK_DECOMPOSITION / EXACT_FOCK_IRREP_CENSUS / EXACT_CENTER_PARITY_SPLIT / EXACT_AFFINE_E6_MCKAY_ENVELOPE / SINGLE_SUPERCHARGE_FULL_E6_REALIZATION_REJECTED / NOVELTY_OPEN

Date: 2026-09-22

Parent sources:
- research/TIR_SIC_NAIMARK_CAR_SUPERSYMMETRY_V0_1.md
- TIR Stage 14: TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE14_MCKAY_ADE_CLOSURE_V0_1.md
- TIR source pin: AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations@f7b754347502f5051d423867f8a8d60627b1f8d7

This note concerns finite representation theory. It does not claim a new physical symmetry, a physical E6 grand-unification model, or physical supersymmetry.

## 1. Setup

Let
\[
\rho:2T\longrightarrow SU(2)
\]
be the defining spinor representation. Let
\[
V:\mathbb C^2\hookrightarrow\mathcal K,\qquad \mathcal K\cong\mathbb C^4
\]
be the minimal tetrahedral-SIC Naimark isometry with
\[
V\rho(g)=R(g)V.
\]

Then
\[
\mathcal A=\operatorname{Im}V
\]
is an invariant two-dimensional subspace with
\[
R|_{\mathcal A}\cong\rho.
\]
Let
\[
\mathcal B=\ker V^\dagger=\mathcal A^\perp.
\]
Then
\[
\mathcal K=\mathcal A\oplus\mathcal B
\]
orthogonally and \(\mathcal B\) is invariant.

## 2. The C3 quotient character

The binary tetrahedral group satisfies
\[
2T\cong Q_8\rtimes C_3,\qquad 2T_{\rm ab}\cong C_3.
\]
Define
\[
\boxed{\chi(g)=\det(R(g))^2.}
\]
The exact finite audit verifies
\[
\chi^3=1,\qquad \chi|_{Q_8}=1,
\]
and \(\chi\) is nontrivial on the threefold quotient. Reversing the orientation convention exchanges \(\chi\) and \(\chi^2\).

## 3. Naimark complement theorem

The complex irreducible dimensions of \(2T\) are
\[
1,1,1,2,2,2,3.
\]
The three spinorial doublets are
\[
\rho,\qquad \rho\chi,\qquad \rho\chi^2.
\]

Since
\[
R(-I)=-I_4
\]
and \(\rho(-I)=-I_2\), the two-dimensional complement also has central sign minus. It therefore cannot split into one-dimensional characters and must be a spinorial doublet. The determinant character fixes its twist.

### Theorem 1
Up to \(\chi\leftrightarrow\chi^2\),
\[
\boxed{R\cong\rho\oplus\rho\chi.}
\]
Equivalently,
\[
\boxed{\operatorname{Im}V\cong\rho,\qquad \ker V^\dagger\cong\rho\chi.}
\]

The validator checks on all 24 elements that
\[
\operatorname{tr}_{\ker V^\dagger}R(g)
=
\chi(g)\operatorname{tr}\rho(g).
\]

Thus the Naimark complement is a \(C_3\)-twisted spinor, not an arbitrary auxiliary plane.

## 4. Exterior/Fock decomposition

Using
\[
\Lambda^2\rho\cong\mathbf1,\qquad
\rho\otimes\rho\cong\mathbf1\oplus\mathbf3,
\]
one gets
\[
\boxed{\Lambda^0\mathcal K=\mathbf1,}
\]
\[
\boxed{\Lambda^1\mathcal K=\rho\oplus\rho\chi,}
\]
\[
\boxed{\Lambda^2\mathcal K=\mathbf1\oplus\chi\oplus\chi^2\oplus\mathbf3,}
\]
\[
\boxed{\Lambda^3\mathcal K=\rho\chi\oplus\rho\chi^2,}
\]
\[
\boxed{\Lambda^4\mathcal K=\chi^2.}
\]

Hence
\[
\boxed{\mathcal F_{\rm even}
=2\mathbf1\oplus\chi\oplus2\chi^2\oplus\mathbf3,}
\]
and
\[
\boxed{\mathcal F_{\rm odd}
=\rho\oplus2\rho\chi\oplus\rho\chi^2.}
\]

For the conjugate one-particle representation used by the supercharge, exchange \(\chi\leftrightarrow\chi^2\).

Every complex irreducible representation of \(2T\) occurs in the 16-dimensional fermionic Fock carrier.

## 5. Center parity

The center acts with sign plus on
\[
\mathbf1,\chi,\chi^2,\mathbf3
\]
and sign minus on
\[
\rho,\rho\chi,\rho\chi^2.
\]
Therefore
\[
\boxed{\mathcal F_{\rm even}=\text{center-even sector},\qquad
\mathcal F_{\rm odd}=\text{center-odd sector}.}
\]
This is the irrep-level form of
\[
\Gamma(-I)=(-1)^F.
\]

## 6. McKay adjacency

Tensoring by the defining spinor gives
\[
\rho\otimes\mathbf1=\rho,
\]
\[
\rho\otimes\chi=\rho\chi,\qquad
\rho\otimes\chi^2=\rho\chi^2,
\]
\[
\rho\otimes\rho=\mathbf1\oplus\mathbf3,
\]
\[
\rho\otimes\rho\chi=\chi\oplus\mathbf3,
\]
\[
\rho\otimes\rho\chi^2=\chi^2\oplus\mathbf3,
\]
\[
\rho\otimes\mathbf3=\rho\oplus\rho\chi\oplus\rho\chi^2.
\]

In the ordered basis
\[
(\mathbf1,\chi,\chi^2,\rho,\rho\chi,\rho\chi^2,\mathbf3)
\]
the adjacency matrix is
\[
\boxed{
A=
\begin{pmatrix}
0&0&0&1&0&0&0\\
0&0&0&0&1&0&0\\
0&0&0&0&0&1&0\\
1&0&0&0&0&0&1\\
0&1&0&0&0&0&1\\
0&0&1&0&0&0&1\\
0&0&0&1&1&1&0
\end{pmatrix}.
}
\]
With
\[
d=(1,1,1,2,2,2,3)^T,
\]
\[
\boxed{(2I-A)d=0.}
\]

This is the affine \(E_6\) McKay graph.

### Theorem 2 — Naimark–Fock McKay envelope

The tetrahedral SIC minimal Naimark carrier has a fermionic Fock completion containing every irreducible \(2T\)-type, and tensoring those types by the defining spinor is governed by
\[
\boxed{\widetilde E_6.}
\]

This agrees with the independently existing TIR Stage-14 theorem
\[
2T\leftrightarrow\widetilde E_6.
\]

## 7. HOUND no-go: the current Q is not the full E6 dynamics

For the present supercharge,
\[
Q_\alpha\propto\sum_a\lambda_{a,\alpha}f_a^\dagger,
\]
while
\[
V_{a\alpha}
=
\frac{\overline{\xi_{a,\alpha}}}{\sqrt2},
\qquad
\lambda_a=\sqrt2\,\xi_a.
\]
Therefore its coefficient matrix obeys
\[
\boxed{L=2\overline V,\qquad \operatorname{rank}L=2.}
\]

So the current \(Q\) directly uses only one defining-spinor summand of the four-dimensional one-particle carrier. The Naimark complement is not directly used.

The statement
\[
\text{current single Q realizes the full affine E6 adjacency}
\]
is therefore rejected.

The correct result is
\[
\boxed{
\text{Fock representation envelope}=\widetilde E_6,
\qquad
\text{current single Q}=\text{rank-two spinor subsector}.
}
\]

## 8. Next typed candidate

Because
\[
\ker V^\dagger\cong\rho\chi,
\]
the complement can be untwisted at the discrete representation level:
\[
\boxed{\ker V^\dagger\otimes L_{\chi^{-1}}\cong\rho.}
\]

TIR already has an exact \(C_3/F_3\) representation carrier. The next question is therefore precise:

Does the TIR \(C_3\) character line provide a canonical compensator for the Naimark-complement twist, yielding a second odd operator with vanishing cross-CAR terms?

This is OPEN.

Even if such an operator closes under \(2T\), it must not be called ordinary four-dimensional \(\mathcal N=2\) supersymmetry without an extension theorem to the relevant connected Lorentz-spin group. The nontrivial one-dimensional \(C_3\) characters of \(2T\) do not extend to nontrivial characters of connected \(SU(2)\).

## 9. Literature firewall

Standard ingredients:
- the seven irreducibles of \(2T\);
- \(2T/Q_8\cong C_3\);
- the three \(C_3\)-twisted spinor doublets;
- McKay \(2T\leftrightarrow\widetilde E_6\);
- exterior/Fock decomposition;
- covariant Naimark dilation.

Related literature also contains other SIC-to-\(E_6\) routes and other decompositions of \(2T\) representations into twisted spinor irreps.

Therefore the specific chain
\[
\text{tetrahedral SIC}
\to
R\cong\rho\oplus\rho\chi
\to
\Lambda^\bullet R
\to
\text{center parity}
\to
\widetilde E_6
\]
is retained as a synthesis/novelty candidate only, pending a dedicated priority audit.

## 10. Validation

Validator:
validation/validate_tir_naimark_mckay_e6_v0_1.py

It checks all 24 group elements, all irreducible character inner products, all exterior-power multiplicities, center/parity, the complete McKay matrix, the affine null-vector equation, and the rank-two single-supercharge firewall.

Current CI verdict: PASS.
