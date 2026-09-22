# TIR Cyclic-Arm Criticality and the Affine-E6 Supersymmetry Selector v0.1

Status: **EXACT_CYCLIC_ARM_SPECTRAL_CLASSIFICATION / C3_EQUIVARIANT_INDEX_EXACT / AFFINE_E6_CRITICAL_POINT_EXACT / NOVELTY_NOT_YET_CLAIMED**

Date: 2026-09-22

Parents:
- research/TIR_C3_RESOLVED_N2_LONG_MULTIPLETS_V0_1.md
- CLAIMS_V1_12.md
- research/EULER_HILBERT_HOTEL_SUPERSYMMETRY_V0_5.md
- TIR Stage-14 McKay closure \(2T\leftrightarrow\widetilde E_6\)

## 1. The uniform cyclic-arm family

For an integer \(n\ge1\), define the bipartite graph \(\Gamma_n\) with

- \(n\) outer even vertices \(s_0,\ldots,s_{n-1}\);
- one central even vertex \(c\);
- \(n\) odd middle vertices \(d_0,\ldots,d_{n-1}\);

and edges

\[
s_j-d_j,
\qquad
c-d_j,
\qquad
j\in\mathbb Z_n.
\]

The cyclic group \(C_n\) acts by simultaneous arm rotation

\[
s_j\mapsto s_{j+1},
\qquad
d_j\mapsto d_{j+1},
\qquad
c\mapsto c.
\]

In the ordered even/odd bases, the bipartite incidence block is

\[
\boxed{
B_n=
\begin{pmatrix}
I_n&\mathbf1_n
\end{pmatrix}
:
\mathbb C^{n+1}\to\mathbb C^n.
}
\]

For \(n=3\), this is exactly the affine-\(E_6\) block already present in the supersymmetry branch.

## 2. Universal SUSY index

The identity block makes \(B_n\) surjective, so

\[
\operatorname{rank}B_n=n,
\qquad
\dim\ker B_n=1,
\qquad
\dim\ker B_n^\dagger=0.
\]

Therefore

\[
\boxed{
\operatorname{ind}(B_n)=1
\qquad
\forall n\ge1.
}
\]

The protected zero mode is

\[
\boxed{
v_0^{(n)}
=
(1,\ldots,1,-1)^T.
}
\]

With

\[
Q_n=
\begin{pmatrix}
0&0\\
B_n&0
\end{pmatrix},
\]

the standard finite Fredholm factorization gives

\[
\boxed{
\Delta_W(Q_n)=1.
}
\]

Thus the unit graph-SUSY defect is universal across the whole cyclic-arm family. It does not by itself select \(n=3\).

## 3. Exact \(C_n\) Fourier decomposition

Let

\[
\omega_n=e^{2\pi i/n}.
\]

Fourier transform the arm coordinates. The \(n-1\) nontrivial character channels each reduce to

\[
\boxed{
B_{n,k}=1,
\qquad
k=1,\ldots,n-1.
}
\]

The trivial character receives both the arm-symmetric source coordinate and the central vertex and is

\[
\boxed{
B_{n,0}
=
\begin{pmatrix}
1&\sqrt n
\end{pmatrix}
:
\mathbb C^2\to\mathbb C.
}
\]

Hence

\[
\boxed{
B_n
\simeq
[1,\sqrt n]
\oplus
\bigoplus_{k=1}^{n-1}[1].
}
\]

All nontrivial character channels are invertible. The entire index is localized in the trivial \(C_n\) channel:

\[
\boxed{
\operatorname{Ind}_{C_n}(B_n)
=
[\mathbf1]
\in R(C_n).
}
\]

Equivalently, for every \(g\in C_n\) and every \(t\ge0\),

\[
\boxed{
\operatorname{Tr}\!\left(g\,e^{-tB_n^\dagger B_n}\right)
-
\operatorname{Tr}\!\left(g\,e^{-tB_nB_n^\dagger}\right)
=
1.
}
\]

This is the finite equivariant McKean--Singer identity for the present complex.

## 4. Exact singular and adjacency spectra

One has

\[
B_nB_n^\dagger
=
I_n+J_n,
\]

where \(J_n=\mathbf1_n\mathbf1_n^T\). Therefore

\[
\operatorname{spec}(B_nB_n^\dagger)
=
\{\,n+1,\;1^{(n-1)}\,\}.
\]

Consequently

\[
\boxed{
\operatorname{spec}(B_n^\dagger B_n)
=
\{\,0,\;1^{(n-1)},\;n+1\,\}.
}
\]

Define the full bipartite adjacency matrix

\[
A_n=
\begin{pmatrix}
0&B_n^\dagger\\
B_n&0
\end{pmatrix}.
\]

Its spectrum is

\[
\boxed{
\operatorname{spec}(A_n)
=
\left\{
\pm\sqrt{n+1},
\ \pm1^{(n-1)},
\ 0
\right\}.
}
\]

In particular,

\[
\boxed{
\rho(A_n)=\sqrt{n+1}.
}
\]

## 5. The criticality theorem

Define the simply-laced Cartan-type matrix

\[
C_n=2I-A_n.
\]

Because \(A_n\) is symmetric, the smallest eigenvalue of \(C_n\) is

\[
\lambda_{\min}(C_n)
=
2-\sqrt{n+1}.
\]

Therefore:

\[
\boxed{
n<3
\Longrightarrow
C_n>0,
}
\]

\[
\boxed{
n=3
\Longrightarrow
C_n\ge0
\ \text{with corank }1,
}
\]

\[
\boxed{
n>3
\Longrightarrow
C_n\ \text{is indefinite}.
}
\]

Hence

\[
\boxed{
C_n
\text{ is affine-critical}
\iff
n=3.
}
\]

At that unique critical value, \(\Gamma_3\) is the seven-node three-arm graph with arm length two, i.e.

\[
\boxed{
\Gamma_3\cong\widetilde E_6.
}
\]

Thus, within the uniform cyclic two-step-arm family, affine \(E_6\) is selected uniquely by spectral criticality.

## 6. Positive affine vector

For general \(n\), the Perron eigenvalue of \(A_n\) is \(\sqrt{n+1}\). A positive Perron vector may be chosen as

\[
d_n=
\binom{d_{+,n}}{d_{-,n}},
\]

with

\[
d_{+,n}
=
(1,\ldots,1,n)^T,
\]

\[
d_{-,n}
=
\sqrt{n+1}\,(1,\ldots,1)^T.
\]

Then

\[
A_nd_n
=
\sqrt{n+1}\,d_n.
\]

This vector is integral with the affine normalization at the critical point \(n=3\):

\[
\boxed{
d_{+,3}=(1,1,1,3)^T,
\qquad
d_{-,3}=(2,2,2)^T.
}
\]

Therefore

\[
\boxed{
A_3d_3=2d_3,
\qquad
C_3d_3=0.
}
\]

This is exactly the binary-tetrahedral affine-\(E_6\) dimension vector.

## 7. Orthogonality of the protected and affine modes

The protected graph-SUSY zero mode lives in the even sector:

\[
v_0^{(n)}
=
(1,\ldots,1,-1)^T.
\]

Its inner product with the positive Perron source vector is

\[
\langle v_0^{(n)},d_{+,n}\rangle
=
n-n
=
0.
\]

Hence

\[
\boxed{
v_0^{(n)}
\perp
d_{+,n}
\qquad
\forall n.
}
\]

At \(n=3\), the two geometrically distinguished trivial-\(C_3\) modes are therefore orthogonal:

- \(v_0^{(3)}\): protected graph-SUSY kernel mode;
- \(d_{+,3}\): affine-\(E_6\) positive dimension mode.

Their Hamiltonian eigenvalues are respectively

\[
0
\qquad\text{and}\qquad
4.
\]

The two nontrivial \(C_3\) arm modes sit between them at eigenvalue \(1\).

Thus the full even-sector spectrum at the affine point is the exact hierarchy

\[
\boxed{
0_{\rm protected}
\ <\
1_{\chi,\chi^2}
\ <\
4_{\rm affine}.
}
\]

## 8. Relation to the three massive \(N=2\) sectors

The current finite supersymmetry carrier has three conserved \(C_3\)-graded long-multiplet sectors

\[
\mathcal M_0,\mathcal M_1,\mathcal M_2,
\]

whose diagonal-\(2T\) supports are the three arms

\[
\chi^r-\rho\chi^r-3.
\]

The union of those arms gives \(\widetilde E_6\).

The present theorem shows that the number of equal arms is not merely compatible with affine \(E_6\). In the uniform two-step cyclic-arm family,

\[
\boxed{
\text{affine spectral criticality}
\Longrightarrow
n=3.
}
\]

Therefore the same threefold arm count that appears as the conserved internal \(C_3\) is precisely the unique arm number at which this graph family reaches the affine ADE threshold.

This is a mathematical selection statement for the declared family. It does not identify the three arms with physical generations.

## 9. What is universal and what is selected

The family separates two mechanisms cleanly:

\[
\boxed{
\operatorname{ind}(B_n)=1
\quad\text{for every }n,
}
\]

but

\[
\boxed{
\rho(A_n)=2
\iff
n=3.
}
\]

Thus the protected Hilbert-Hotel/Fredholm defect is topological and insensitive to the arm count, whereas affine-\(E_6\) closure is a spectral criticality condition that uniquely fixes three arms.

This prevents a false inference that the unit Witten index by itself selects \(E_6\).

## 10. Status firewall

### EXACT

- \(C_n\)-equivariant Fourier decomposition of \(B_n\);
- ordinary and equivariant index \(+1\) / trivial character;
- exact singular and adjacency spectra;
- positive/affine/indefinite trichotomy of \(2I-A_n\);
- uniqueness \(n=3\) of the affine-critical member;
- identification \(\Gamma_3\cong\widetilde E_6\);
- protected-mode / Perron-mode orthogonality;
- recovery of the affine-\(E_6\) dimension vector.

### STANDARD INGREDIENTS

- Fourier decomposition of cyclic representations;
- finite-dimensional supersymmetric/Fredholm factorization;
- spectral characterization of simply-laced finite/affine graph Cartan matrices;
- affine-\(E_6\) Dynkin graph.

### NOT CLAIMED

- that this classification is absent from graph/Dynkin literature;
- that \(C_3\) is physically a generation symmetry;
- that affine \(E_6\) is a physical gauge group;
- that the theorem establishes supersymmetry in Nature.

The novelty candidate is the exact placement of this criticality theorem inside the SIC/Naimark/CAR/\(C_3\)/massive-\(N=2\) chain.
