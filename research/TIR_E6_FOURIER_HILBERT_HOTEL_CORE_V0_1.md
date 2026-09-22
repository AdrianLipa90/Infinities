# TIR Affine-E6 Fourier–Hilbert-Hotel Core Theorem v0.1

Status: **EXACT_C3_ISOTYPIC_REDUCTION / EXACT_HILBERT_HOTEL_CORE / AFFINE_AND_INDEX_MODES_LOCALIZED / K_THEORY_CLASS_EXPOSED / NOVELTY_NOT_YET_CLAIMED**

Date: 2026-09-22

Parents:
- research/TIR_C3_ARM_DECOMPOSITION_MCKAY_INDEX_V0_1.md
- research/TIR_CYCLIC_ARM_CRITICALITY_E6_V0_1.md
- research/TIR_EXCEPTIONAL_MCKAY_BALANCE_C6_SELECTOR_V0_1.md
- research/EULER_HILBERT_HOTEL_SUPERSYMMETRY_V0_5.md

## 1. McKay incidence and the character-group action

For the binary tetrahedral group \(2T\), the one-dimensional character group is

\[
\widehat{2T}_{1D}\cong C_3
=
\{1,\eta,\eta^2\}.
\]

Tensoring an irrep by a one-dimensional character preserves tensor-product multiplicities with the defining doublet:

\[
V\otimes(\eta\lambda)
\cong
\eta(V\otimes\lambda).
\]

Therefore tensoring by \(\eta\) acts by an automorphism of the McKay graph.

On the affine-\(E_6\) irreducible types it cycles

\[
1\to\eta\to\eta^2\to1,
\]

\[
V\to\eta V\to\eta^2V\to V,
\]

and fixes the unique three-dimensional irrep \(3\).

Thus the abstract character group \(C_3\) is exactly the three-arm rotation of the affine-\(E_6\) McKay graph.

This identifies the previously separate objects

\[
\boxed{
\text{abelianization/character }C_3
=
\text{McKay arm-rotation }C_3
}
\]

at the representation-ring level.

## 2. The affine-E6 incidence block

Order the center-even irreducible types as

\[
(1,\eta,\eta^2,3)
\]

and the center-odd types as

\[
(V,\eta V,\eta^2V).
\]

The bipartite incidence block is

\[
\boxed{
B=
\begin{pmatrix}
1&0&0&1\\
0&1&0&1\\
0&0&1&1
\end{pmatrix}
=
[I_3\mid\mathbf1_3].
}
\]

The \(C_3\) character action simultaneously cycles the first three domain coordinates and all three codomain coordinates, while fixing the central \(3\)-node coordinate.

Hence \(B\) is \(C_3\)-equivariant.

## 3. Exact Fourier/isotypic decomposition

Let

\[
F_3=
\frac1{\sqrt3}
\begin{pmatrix}
1&1&1\\
1&\omega&\omega^2\\
1&\omega^2&\omega
\end{pmatrix},
\qquad
\omega=e^{2\pi i/3}.
\]

Apply \(F_3\) to the three arm coordinates on both sides, leaving the central coordinate unchanged.

Then

\[
\boxed{
F_3^\dagger
B
(F_3\oplus1)
=
\begin{pmatrix}
1&0&0&\sqrt3\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
}
\]

After grouping characters,

\[
\boxed{
B
\simeq
B_0\oplus B_\eta\oplus B_{\eta^2},
}
\]

with

\[
\boxed{
B_0=
\begin{pmatrix}
1&\sqrt3
\end{pmatrix}
:
\mathbb C^2\to\mathbb C,
}
\]

and

\[
\boxed{
B_\eta=B_{\eta^2}=[1].
}
\]

Thus all nontrivial character sectors are invertible supersymmetric pairs. Every index defect and every affine-critical singular value sits in the trivial-character block.

## 4. Canonical Hilbert-Hotel reduction of the trivial block

Define the orthogonal/unitary matrix

\[
U_0
=
\frac12
\begin{pmatrix}
1&\sqrt3\\
\sqrt3&-1
\end{pmatrix}.
\]

Its first column is parallel to \(B_0^\dagger\) and its second column spans \(\ker B_0\).

Directly,

\[
\boxed{
B_0U_0
=
\begin{pmatrix}
2&0
\end{pmatrix}.
}
\]

Therefore

\[
\boxed{
B
\sim_{\rm unitary}
[2,0]\oplus[1]\oplus[1].
}
\]

A positive rescaling of the first nonzero singular value gives a Fredholm homotopy

\[
[2,0]
\sim_{\rm Fredholm}
[1,0].
\]

Hence

\[
\boxed{
B
\sim_{\rm Fredholm}
[1,0]\oplus[1]\oplus[1].
}
\]

The two scalar identity blocks are invertible and carry zero index. The entire index is the one-dimensional deletion defect

\[
\boxed{
[1,0]:\mathbb C^2\to\mathbb C.
}
\]

This is the finite-dimensional Hilbert-Hotel normal core of affine-\(E_6\) graph supersymmetry.

## 5. Protected and affine modes are the two orthogonal trivial-character directions

In the original even-node basis, the protected kernel vector is

\[
\boxed{
v_0=(1,1,1,-1)^T.
}
\]

The affine positive dimension vector on the even side is

\[
\boxed{
d_+=(1,1,1,3)^T.
}
\]

Both are \(C_3\)-invariant, and

\[
\boxed{
v_0\cdot d_+=0.
}
\]

After normalization, these are precisely the two columns selected by \(U_0\) inside the trivial \(C_3\) domain block:

- the direction parallel to \(B_0^\dagger\) is the affine/Perron mode;
- the orthogonal direction is the protected Hilbert-Hotel kernel mode.

Explicitly,

\[
B^\dagger B\,v_0=0,
\]

\[
B^\dagger B\,d_+=4d_+.
\]

Thus the trivial character sector contains both extremal modes

\[
\boxed{
0_{\rm protected}
\qquad\text{and}\qquad
4_{\rm affine},
}
\]

while the \(\eta,\eta^2\) sectors each carry the paired eigenvalue

\[
\boxed{1}.
\]

## 6. Exact SUSY direct-sum decomposition

The graph supercharge built from \(B\),

\[
Q_B=
\begin{pmatrix}
0&0\\
B&0
\end{pmatrix},
\]

decomposes under the \(C_3\) character transform into

\[
\boxed{
Q_B
\simeq
Q_{\rm HH}
\oplus
Q_\eta
\oplus
Q_{\eta^2},
}
\]

where

\[
Q_{\rm HH}
\leftrightarrow
[2,0]
\]

has Witten/Fredholm index \(+1\), and

\[
Q_\eta,\ Q_{\eta^2}
\leftrightarrow
[1]
\]

are invertible paired sectors of index zero.

Therefore

\[
\boxed{
\Delta_W(Q_B)
=
\Delta_W(Q_{\rm HH})
+
0+0
=
1.
}
\]

This is stronger than merely computing the total index: it localizes the entire Hilbert-Hotel defect to a single symmetry sector.

## 7. Affine criticality is also localized to the same core

The singular values of the three character blocks are

\[
\boxed{
\sigma(B_0)=\{2,0\},
\qquad
\sigma(B_\eta)=\{1\},
\qquad
\sigma(B_{\eta^2})=\{1\}.
}
\]

Hence the full adjacency spectral radius

\[
\rho(A_{\widetilde E_6})=2
\]

comes entirely from the nonzero singular value of the same trivial-character block \(B_0\) that carries the index defect.

Thus two a priori different structures are co-localized:

\[
\boxed{
\text{Fredholm defect}
\quad\text{and}\quad
\text{affine spectral criticality}
}
\]

both reside in the \(C_3\)-invariant quotient block.

The nontrivial character sectors are spectrally subcritical and topologically trivial.

## 8. K-theory interpretation

After stabilization, the invertible scalar blocks represent the zero class in the Fredholm \(K\)-theory classification.

Therefore

\[
\boxed{
[B]_{\rm stable}
=
[B_0]_{\rm stable}
=
[S^\dagger]_{\rm Fredholm}.
}
\]

The full affine-\(E_6\) McKay graph carries no additional Fredholm charge beyond its one-dimensional \(C_3\)-invariant Hilbert-Hotel core.

The remaining graph structure records symmetry and finite spectral data rather than additional index charge.

## 9. Quotient interpretation

The \(C_3\)-orbit quotient of the three equal arms leaves the normalized invariant incidence block

\[
\boxed{
B_0=[1,\sqrt3].
}
\]

The coefficient \(\sqrt3\) is not inserted manually. It is the normalization factor from collapsing three symmetry-related center-to-arm edges into the invariant Fourier mode.

Thus the affine-\(E_6\) graph can be reconstructed as:

1. one weighted trivial-character supersymmetric core;
2. two unit nontrivial-character spectators;
3. inverse Fourier assembly into three equivalent arms.

This gives a minimal symmetry-reduced description of the graph.

## 10. Compact theorem statement

### Theorem — Affine-E6 Fourier–Hilbert-Hotel core

For the binary-tetrahedral McKay incidence operator

\[
B=[I_3\mid\mathbf1_3],
\]

the one-dimensional character group \(C_3\) acts as the three-arm graph automorphism. Under exact \(C_3\) Fourier decomposition,

\[
\boxed{
B
\simeq
[1,\sqrt3]\oplus[1]\oplus[1].
}
\]

After a unitary basis change in the invariant two-dimensional domain,

\[
\boxed{
[1,\sqrt3]
\sim_{\rm unitary}
[2,0].
}
\]

Consequently:

- the complete Fredholm/Witten index \(+1\) is carried by the single invariant deletion block;
- the protected zero mode and affine positive mode are the two orthogonal invariant directions;
- the affine spectral radius \(2\) is carried by the same invariant block;
- the two nontrivial \(C_3\) sectors are invertible, index-zero, singular-value-one pairs.

Hence

\[
\boxed{
\text{affine-}E_6
=
\text{one Hilbert-Hotel critical core}
\oplus
\text{two symmetry spectators}
}
\]

after exact character decomposition.

## 11. Firewall

### EXACT

- one-dimensional characters act by McKay graph automorphisms;
- in \(2T\), that action is the \(C_3\) arm rotation;
- Fourier decomposition \(B\simeq[1,\sqrt3]\oplus1\oplus1\);
- unitary reduction \([1,\sqrt3]\to[2,0]\);
- index localization;
- affine spectral-radius localization;
- protected/Perron orthogonal decomposition;
- stable class equals the unit Hilbert-Hotel class.

### NOT CLAIMED

- literature priority for this packaging;
- physical \(E_6\) gauge symmetry;
- that the graph index equals the physical Fock Witten index;
- supersymmetry in Nature.

The next novelty gate is now sharply defined: determine whether the simultaneous localization of affine criticality and Fredholm defect to the trivial character quotient has an existing general theorem for McKay graphs, and classify which finite subgroups of \(SU(2)\) admit an analogous one-block critical/index core.
