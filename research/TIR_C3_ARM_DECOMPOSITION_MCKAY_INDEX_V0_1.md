# TIR C3-Arm Decomposition and McKay-Index Localization v0.1

Status: **EXACT_C3_SECTOR_DECOMPOSITION / EXACT_AFFINE_E6_ARM_RECONSTRUCTION / GRAPH_INDEX_LOCALIZED_TO_TRIVIAL_C3_SECTOR / FOCK_INDEX_FIREWALL**

Date: 2026-09-22

Parents:
- research/TIR_C3_RESOLVED_N2_LONG_MULTIPLETS_V0_1.md
- research/TIR_C3_E6_GRAPH_DYNAMICS_V0_1.md
- research/EULER_HILBERT_HOTEL_SUPERSYMMETRY_V0_5.md

## 1. Three long multiplets are the three affine-E6 arms

The conserved total internal charge decomposes the 48-dimensional rest carrier as

\[
\mathcal H_{\rm ext}
=
\mathcal M_0\oplus\mathcal M_1\oplus\mathcal M_2,
\qquad
\dim\mathcal M_r=16.
\]

Each sector is a standard massive \(N=2\) long Clifford module

\[
\mathcal M_r
\cong
\Lambda^\bullet(\mathbf2\oplus\mathbf2).
\]

Its fermion-parity decomposition under the massive little group is

\[
\boxed{
\mathcal M_{r,\rm even}
\cong
5\cdot\mathbf1\oplus\mathbf3,
}
\]

\[
\boxed{
\mathcal M_{r,\rm odd}
\cong
4\cdot\mathbf2.
}
\]

Restricting to the diagonal binary-tetrahedral subgroup and including the conserved \(C_3\) charge gives

\[
\boxed{
\mathcal M_{r,\rm even}
\cong
5\cdot\chi^r\oplus3,
}
\]

\[
\boxed{
\mathcal M_{r,\rm odd}
\cong
4\cdot\rho\chi^r.
}
\]

Hence the irrep-type support of one \(C_3\) sector is exactly

\[
\boxed{
\chi^r
\;-\;
\rho\chi^r
\;-\;
3.
}
\]

The supercharges are odd and have effective type \(\rho\), so within a fixed conserved sector the only possible nonzero type transitions are

\[
\chi^r\leftrightarrow\rho\chi^r,
\qquad
3\leftrightarrow\rho\chi^r.
\]

These are exactly one arm of the affine-\(E_6\) McKay graph.

Taking the union over \(r=0,1,2\) yields

\[
\boxed{
\widetilde E_6
=
\bigcup_{r\in\mathbb Z_3}
\left(
\chi^r-\rho\chi^r-3
\right),
}
\]

where the three copies of the triplet irrep type are identified as the common central node after forgetting the conserved-sector multiplicity.

Thus the affine-\(E_6\) support is the \(C_3\)-orbit closure of one supersymmetric arm.

## 2. The graph-incidence operator

Order the center-even irrep types as

\[
(1,\chi,\chi^2,3)
\]

and the center-odd types as

\[
(\rho,\rho\chi,\rho\chi^2).
\]

The bipartite McKay-incidence operator is

\[
\boxed{
B=
\begin{pmatrix}
1&0&0&1\\
0&1&0&1\\
0&0&1&1
\end{pmatrix}
=
\begin{pmatrix}I_3&\mathbf1_3\end{pmatrix}.
}
\]

The \(C_3\) action cyclically permutes the first three domain coordinates and the three codomain coordinates, while fixing the central triplet coordinate.

Therefore \(B\) is \(C_3\)-equivariant.

## 3. Exact \(C_3\)-Fourier block decomposition

Let \(F_3\) be the unitary discrete Fourier transform on the three arms, with first Fourier mode the trivial character.

Apply \(F_3\) to the three endpoint coordinates and to the three odd coordinates, leaving the central \(3\)-node coordinate unchanged.

Then

\[
\boxed{
F_3\,B\,(F_3^\dagger\oplus1)
=
\begin{pmatrix}
1&0&0&\sqrt3\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
}
\]

Thus the McKay-incidence SUSY splits into three independent \(C_3\) character channels:

- two nontrivial character channels, each the invertible scalar map \(1:\mathbb C\to\mathbb C\);
- one trivial-character channel, the rectangular map

\[
\boxed{
B_0=
\begin{pmatrix}
1&\sqrt3
\end{pmatrix}
:
\mathbb C^2\to\mathbb C.
}
\]

Consequently

\[
\operatorname{ind}(B_{\chi})=0,
\qquad
\operatorname{ind}(B_{\chi^2})=0,
\]

while

\[
\boxed{
\operatorname{ind}(B_0)=1.
}
\]

Hence

\[
\boxed{
\operatorname{ind}(B)=1
}
\]

is entirely localized in the \(C_3\)-invariant sector.

## 4. Protected graph zero mode and affine dimension vector

In the original node basis, the unique kernel vector is

\[
\boxed{
v_0=(1,1,1,-1)^T.
}
\]

It is \(C_3\)-invariant.

The positive affine dimension vector on the even side is

\[
\boxed{
d_+=(1,1,1,3)^T,
}
\]

and on the odd side

\[
\boxed{
d_-=(2,2,2)^T.
}
\]

They satisfy

\[
Bd_+=2d_-,
\qquad
B^\dagger d_-=2d_+.
\]

The two \(C_3\)-invariant domain vectors

\[
v_0=(1,1,1,-1),
\qquad
d_+=(1,1,1,3)
\]

are orthogonal:

\[
\boxed{
v_0\cdot d_+=0.
}
\]

They diagonalize the trivial-character part of \(B^\dagger B\):

\[
B^\dagger B\,v_0=0,
\]

\[
\boxed{
B^\dagger B\,d_+=4d_+.
}
\]

The two nontrivial \(C_3\) endpoint modes have eigenvalue \(1\).

Therefore

\[
\boxed{
\operatorname{spec}(B^\dagger B)=\{0,1,1,4\}
}
\]

has a direct representation-theoretic interpretation:

\[
0:
\text{ protected trivial-}C_3\text{ graph mode},
\]

\[
1,1:
\text{ the two nontrivial }C_3\text{ arm modes},
\]

\[
4:
\text{ the positive affine dimension-vector mode}.
\]

## 5. The graph Witten index is not the Fock Witten index

Each physical/internal 16-dimensional long multiplet has

\[
\dim\mathcal M_{r,\rm even}
=
\dim\mathcal M_{r,\rm odd}
=
8,
\]

so its ordinary long-multiplet Witten index vanishes:

\[
\boxed{
\Delta_W(\mathcal M_r)=0.
}
\]

The full 48-dimensional carrier likewise has

\[
24\text{ even states}
\quad\text{and}\quad
24\text{ odd states},
\]

hence zero Fock Witten index.

By contrast, the graph-incidence complex replaces every irrep type by one basis node:

\[
\mathbb C^{\{1,\chi,\chi^2,3\}}
\overset{B}{\longrightarrow}
\mathbb C^{\{\rho,\rho\chi,\rho\chi^2\}},
\]

whose dimensions are \(4\) and \(3\). Its index is therefore \(+1\) because \(B\) has full row rank.

Thus

\[
\boxed{
\Delta_W^{\rm graph}=+1
\neq
\Delta_W^{\rm Fock}=0.
}
\]

The \(+1\) index is created by the decategorifying collapse from representation spaces/multiplicities to one-dimensional irrep-type nodes. It must not be interpreted as a physical long-multiplet Witten index.

This sharpens the v0.5 firewall.

## 6. C3-orbit reconstruction theorem

Combining the previous sections gives the exact finite statement

\[
\boxed{
\text{one massive }N=2\text{ long multiplet}
\;\xrightarrow{\text{restrict to }\Delta_\chi(2T)}
\text{one }E_6\text{ arm},
}
\]

and

\[
\boxed{
C_3\text{-orbit of the three conserved long-multiplet sectors}
\;\xrightarrow{\text{identify common irrep type }3}
\widetilde E_6.
}
\]

The affine graph is therefore not inserted independently into the finite supersymmetry carrier. It is reconstructed as the type-support orbit of the three \(C_3\)-resolved long multiplets.

## 7. Firewall

This theorem is about finite representation support, parity, and graph incidence.

It does not claim:

- an \(E_6\) gauge theory;
- that the graph-incidence index is a physical supersymmetric index;
- that the three \(C_3\) sectors are observed particle generations;
- interacting dynamics;
- literature novelty.

The strongest exact new organizational statement is:

\[
\boxed{
\widetilde E_6
=
C_3\text{-orbit closure of one }N=2\text{ long-multiplet arm},
}
\]

while the graph index \(+1\) is localized entirely in the trivial \(C_3\) Fourier channel and is explicitly separated from the zero Fock Witten index.
