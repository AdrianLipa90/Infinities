# TIR Cartan–SUSY Spectral Duality v0.1

Status: **EXACT_BIPARTITE_OPERATOR_IDENTITY / AFFINE_CRITICALITY_AS_SUSY_HAMILTONIAN_THRESHOLD / ZERO_MODE_AND_AFFINE_MODE_SEPARATED / NOVELTY_NOT_YET_CLAIMED**

Date: 2026-09-22

Parents:
- research/TIR_E6_FOURIER_HILBERT_HOTEL_CORE_V0_1.md
- research/TIR_CYCLIC_ARM_CRITICALITY_E6_V0_1.md
- research/EULER_HILBERT_HOTEL_SUPERSYMMETRY_V0_5.md

## 1. General bipartite SUSY operator

Let

\[
B:\mathcal H_+\to\mathcal H_-
\]

be any finite-dimensional complex matrix.

Define the odd self-adjoint bipartite operator

\[
\boxed{
D_B=
\begin{pmatrix}
0&B^\dagger\\
B&0
\end{pmatrix}.
}
\]

With grading

\[
\Gamma=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix},
\]

one has

\[
\{\Gamma,D_B\}=0.
\]

The corresponding \(N=2\) complex supercharge is

\[
Q_B=
\begin{pmatrix}
0&0\\
B&0
\end{pmatrix},
\]

and the SUSY Hamiltonian is

\[
\boxed{
H_B
=
\{Q_B,Q_B^\dagger\}
=
D_B^2
=
\begin{pmatrix}
B^\dagger B&0\\
0&BB^\dagger
\end{pmatrix}.
}
\]

## 2. Cartan operator from the same Dirac/McKay adjacency

Define the simply-laced Cartan-type operator

\[
\boxed{
C_B=2I-D_B.
}
\]

Then

\[
D_B=2I-C_B.
\]

Therefore the SUSY Hamiltonian and Cartan operator satisfy the exact polynomial identity

\[
\boxed{
H_B
=
(2I-C_B)^2.
}
\]

Equivalently,

\[
\boxed{
4I-H_B
=
C_B(4I-C_B).
}
\]

Thus the graph-SUSY Hamiltonian and the Cartan operator are not independent structures: both are polynomial functions of the same odd bipartite operator \(D_B\).

## 3. Spectral dictionary

If

\[
D_B\psi=\lambda\psi,
\]

then

\[
H_B\psi=\lambda^2\psi
\]

and

\[
C_B\psi=(2-\lambda)\psi.
\]

Hence

\[
\boxed{
\lambda_D
\longleftrightarrow
\lambda_H=\lambda_D^2
\longleftrightarrow
\lambda_C=2-\lambda_D.
}
\]

Because \(D_B\) is bipartite/odd, its nonzero spectrum is symmetric:

\[
\lambda\leftrightarrow-\lambda.
\]

The paired Cartan eigenvalues are correspondingly

\[
2-\lambda
\quad\leftrightarrow\quad
2+\lambda.
\]

## 4. Supersymmetric zero modes sit at Cartan eigenvalue two

A supersymmetric zero mode obeys

\[
H_B\psi=0.
\]

Since \(H_B=D_B^2\),

\[
H_B\psi=0
\iff
D_B\psi=0.
\]

Therefore

\[
\boxed{
H_B\psi=0
\iff
C_B\psi=2\psi.
}
\]

Thus protected SUSY zero modes are **not** affine Cartan zero modes. They occupy the Cartan eigenvalue \(2\).

The Witten index remains

\[
\boxed{
\Delta_W
=
\dim\ker B-\dim\ker B^\dagger.
}
\]

## 5. Affine Cartan zero modes sit at SUSY energy four

An affine null vector obeys

\[
C_Bd=0.
\]

Therefore

\[
D_Bd=2d
\]

and hence

\[
\boxed{
H_Bd=4d.
}
\]

Thus an affine positive dimension vector is a top-threshold state of the SUSY Hamiltonian, not a supersymmetric ground state.

The two special energies are exactly separated:

\[
\boxed{
E_{\rm SUSY\ zero}=0,
\qquad
E_{\rm affine}=4.
}
\]

## 6. Finite/affine/indefinite classification by the SUSY Hamiltonian

Let

\[
\rho(D_B)=\|D_B\|
\]

for the self-adjoint bipartite operator.

The Cartan-type operator is positive semidefinite exactly when

\[
\rho(D_B)\le2.
\]

Since

\[
\lambda_{\max}(H_B)=\rho(D_B)^2,
\]

one obtains

\[
\boxed{
C_B>0
\Longleftrightarrow
\lambda_{\max}(H_B)<4,
}
\]

\[
\boxed{
C_B\ge0\text{ singular}
\Longleftrightarrow
\lambda_{\max}(H_B)=4,
}
\]

\[
\boxed{
C_B\text{ indefinite}
\Longleftrightarrow
\lambda_{\max}(H_B)>4.
}
\]

Therefore the usual finite/affine/indefinite graph threshold is exactly the spectral threshold \(E=4\) of the associated SUSY Hamiltonian.

## 7. Application to the uniform cyclic-arm family

For

\[
B_n=[I_n\mid\mathbf1_n],
\]

the earlier theorem gives

\[
\operatorname{spec}(B_n^\dagger B_n)
=
\{0,1^{(n-1)},n+1\}.
\]

Therefore

\[
\boxed{
\lambda_{\max}(H_n)=n+1.
}
\]

The Cartan/SUSY threshold gives immediately

\[
\lambda_{\max}(H_n)=4
\iff
n+1=4
\iff
\boxed{n=3}.
\]

Thus the affine-\(E_6\) selector may be restated purely inside the supersymmetric Hamiltonian:

\[
\boxed{
\Gamma_n\text{ is affine-critical}
\iff
E_{\max}(H_n)=4
\iff
n=3.
}
\]

The universal Witten index remains

\[
\Delta_W=1
\]

for every \(n\), so the ground-state topological defect and the top-energy affine threshold remain logically distinct.

## 8. Application to affine \(E_6\)

For \(n=3\),

\[
\operatorname{spec}(B^\dagger B)
=
\{0,1,1,4\},
\]

\[
\operatorname{spec}(BB^\dagger)
=
\{1,1,4\}.
\]

Hence

\[
\boxed{
\operatorname{spec}(H_B)
=
\{0,1,1,1,1,4,4\}.
}
\]

The adjacency/Dirac spectrum is

\[
\boxed{
\operatorname{spec}(D_B)
=
\{-2,-1,-1,0,1,1,2\}.
}
\]

The Cartan spectrum is

\[
\boxed{
\operatorname{spec}(C_B)
=
\{0,1,1,2,3,3,4\}.
}
\]

The distinguished \(C_3\)-invariant vectors are:

\[
v_{\rm HH}
\in\ker H_B
\quad\Longleftrightarrow\quad
C_Bv_{\rm HH}=2v_{\rm HH},
\]

and

\[
d_{\rm aff}>0,
\qquad
C_Bd_{\rm aff}=0
\quad\Longleftrightarrow\quad
H_Bd_{\rm aff}=4d_{\rm aff}.
\]

They are orthogonal because they belong to distinct eigenspaces of the self-adjoint operator \(H_B\).

## 9. Fourier localization sharpens the identity

Under the exact \(C_3\) character decomposition,

\[
B
\simeq
[1,\sqrt3]\oplus1\oplus1.
\]

The invariant block contributes

\[
H_0:
\quad
\{0,4\},
\]

while the two nontrivial character sectors contribute

\[
H_\eta=H_{\eta^2}=\{1\}
\]

on each parity partner.

Therefore the same symmetry-reduced block contains both:

- the protected \(E=0\) Hilbert-Hotel state;
- the affine \(E=4\) Perron state.

This gives the exact co-localization statement

\[
\boxed{
\text{topological zero-energy endpoint}
\quad\text{and}\quad
\text{affine critical-energy endpoint}
}
\]

inside one \(C_3\)-invariant SUSY core.

## 10. Compact theorem statement

### Theorem — Cartan–SUSY spectral duality

For every finite bipartite incidence operator \(B\), let

\[
D_B=
\begin{pmatrix}0&B^\dagger\\B&0\end{pmatrix},
\qquad
H_B=D_B^2,
\qquad
C_B=2I-D_B.
\]

Then

\[
\boxed{
H_B=(2I-C_B)^2.
}
\]

Consequently:

1. SUSY zero modes are exactly the \(C_B\)-eigenvectors of eigenvalue \(2\);
2. affine Cartan zero modes are exactly the \(H_B\)-eigenvectors of energy \(4\) with \(D_B\)-eigenvalue \(+2\);
3. finite/affine/indefinite Cartan behavior is equivalent to
   \[
   E_{\max}(H_B)<4,\quad=4,\quad>4;
   \]
4. for \(B_n=[I_n\mid\mathbf1_n]\), the affine threshold is \(n=3\);
5. for affine \(E_6\), the \(E=0\) Hilbert-Hotel mode and \(E=4\) affine mode are orthogonal endpoints of the same trivial-\(C_3\) symmetry block.

## 11. Firewall

### EXACT

- \(H_B=D_B^2=(2I-C_B)^2\);
- spectral dictionary;
- zero-mode/affine-mode separation;
- \(E=4\) affine threshold;
- cyclic-arm application;
- affine-\(E_6\) spectra;
- \(C_3\) co-localization.

### STANDARD INGREDIENTS

- bipartite adjacency/Dirac factorization;
- graph Cartan matrices;
- finite-dimensional \(N=2\) factorization;
- ADE spectral-radius criterion.

### NOT CLAIMED

- literature priority for the combined Cartan/SUSY formulation;
- a physical energy value \(4\);
- physical \(E_6\) gauge symmetry;
- supersymmetry in Nature.

The value \(4\) is dimensionless and follows from the conventional simply-laced Cartan normalization \(C=2I-A\).
