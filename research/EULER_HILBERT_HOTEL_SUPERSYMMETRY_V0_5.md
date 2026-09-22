# Euler-Hilbert-Hotel Supersymmetry v0.5 — Twist/Completeness and McKay-Incidence SUSY

Status: **EXACT FINITE REPRESENTATION THEOREMS / MODE-MINIMAL E6 SUPPORT / NOVELTY NOT YET CLAIMED**

Date: 2026-09-22

## 1. Setup

Let \(G=2T\) be the binary tetrahedral group. Let \(\eta\) generate its one-dimensional character group

\[
\widehat G_{\rm 1D}\cong G_{\rm ab}\cong C_3,
\qquad
\eta^3=1.
\]

Let \(V\) denote the defining spinorial doublet. The three spinorial irreducibles are

\[
V,\qquad \eta V,\qquad \eta^{-1}V.
\]

The remaining irreducibles are

\[
1,\qquad \eta,\qquad \eta^{-1},\qquad 3.
\]

The standard McKay fusion rules are

\[
V\otimes 1=V,\qquad
V\otimes\eta=\eta V,\qquad
V\otimes\eta^{-1}=\eta^{-1}V,
\]

\[
V\otimes V=1\oplus3,
\]

\[
V\otimes\eta V=\eta\oplus3,\qquad
V\otimes\eta^{-1}V=\eta^{-1}\oplus3,
\]

\[
V\otimes3=V\oplus\eta V\oplus\eta^{-1}V.
\]

## 2. Twist–completeness equivalence

For \(j\in\mathbb Z/3\mathbb Z\), define a four-dimensional one-particle carrier

\[
K_j=V\oplus \eta^jV.
\]

Its fermionic Fock space is

\[
\mathcal F_j=\Lambda^\bullet K_j^*.
\]

Because \(V^*\cong V\),

\[
K_j^*\cong V\oplus\eta^{-j}V.
\]

For a doublet \(\eta^rV\),

\[
\Lambda^\bullet(\eta^rV)
=
1\oplus\eta^rV\oplus\eta^{-r},
\]

since \(\det(\eta^rV)=\eta^{2r}=\eta^{-r}\).

### Theorem 2.1 — Twist–completeness equivalence

For the family \(K_j=V\oplus\eta^jV\),

\[
\boxed{
j\neq0
\iff
\operatorname{Supp}\Lambda^\bullet K_j^*
=
\operatorname{Irr}(2T).
}
\]

Equivalently, the exterior Fock representation contains all seven irreducible \(2T\)-types if and only if the second doublet is a nontrivial \(C_3\) twist of the defining doublet.

For \(j=0\),

\[
\Lambda^\bullet K_0^*
\cong
5\cdot1\oplus4\cdot V\oplus3,
\]

so only the types

\[
\{1,V,3\}
\]

occur.

For \(j=1\),

\[
\Lambda^\bullet K_1^*
\cong
2\cdot1
\oplus
2\cdot\eta
\oplus
\eta^{-1}
\oplus
V
\oplus
\eta V
\oplus
2\cdot(\eta^{-1}V)
\oplus
3.
\]

For \(j=2\), exchange \(\eta\leftrightarrow\eta^{-1}\). In both nontrivial cases all seven irreducible types occur.

## 3. Intertwiner dichotomy

The same twist controls the odd-operator sector.

If \(j=0\), then

\[
\dim_{\mathbb C}\operatorname{Hom}_{2T}(V,V)=1.
\]

Hence an untwisted equivariant odd line exists.

If \(j\neq0\), Schur's lemma gives

\[
\boxed{
\operatorname{Hom}_{2T}(V,\eta^jV)=0,
}
\]

but

\[
\boxed{
\dim_{\mathbb C}
\operatorname{Hom}_{2T}
(\eta^jV,\eta^jV)
=1.
}
\]

Equivalently, the odd map exists uniquely only as a \(C_3\)-charged/twisted intertwiner.

Thus

\[
\boxed{
\text{nontrivial complement twist}
\iff
\text{no untwisted odd map}
\iff
\text{unique twisted odd line}
\iff
\text{full Fock irrep support}.
}
\]

For the tetrahedral SIC minimal Naimark complement, v0.4 identifies exactly the \(j=\pm1\) case. Hence the mirror Naimark sector supplies the representation-completing twist and simultaneously forces the complex supercharge to carry nontrivial discrete \(C_3\) charge before the compensating TIR \(C_3\) carrier of the later construction is added.

## 4. Minimal fermionic mode theorem for \(2T\)

Any representation containing every irreducible \(2T\)-type at least once has dimension at least

\[
1+1+1+2+2+2+3=12.
\]

An \(m\)-mode complex fermionic Fock space has dimension \(2^m\). Therefore representation-complete support requires

\[
2^m\ge12,
\]

so

\[
m\ge4.
\]

The tetrahedral SIC/Naimark construction has exactly four outcome modes and explicitly realizes all seven irreducible types. Therefore

\[
\boxed{
m_{\min}^{\rm Fock\ support}(2T)=4.
}
\]

## 5. Exceptional McKay mode thresholds

TIR Stage 14 records the affine exceptional dimension vectors

\[
\widetilde E_6:\ (3,2,2,2,1,1,1),
\]

\[
\widetilde E_7:\ (4,3,2,1,3,2,1,2),
\]

\[
\widetilde E_8:\ (6,5,4,3,2,1,4,2,3).
\]

Their coordinate sums are

\[
12,\qquad18,\qquad30.
\]

Thus any Fock representation containing every irreducible type of the corresponding binary polyhedral group must satisfy

\[
2^m\ge12,\qquad 2^m\ge18,\qquad 2^m\ge30,
\]

respectively. Hence

\[
\boxed{
m\ge4\ \text{for }2T,\qquad
m\ge5\ \text{for }2O,\qquad
m\ge5\ \text{for }2I.
}
\]

Consequently a four-mode Fock carrier can be representation-complete for the exceptional \(E_6\) case but cannot be representation-complete for the exceptional \(E_7\) or \(E_8\) cases.

The tetrahedral SIC/Naimark carrier realizes the allowed \(E_6\) case and saturates the lower bound.

## 6. McKay incidence as a finite \(N=2\) supercharge

Split the seven irreducible \(2T\)-types by the central element \(-I\):

\[
\mathcal R_+
=
\{1,\eta,\eta^{-1},3\},
\]

\[
\mathcal R_-
=
\{V,\eta V,\eta^{-1}V\}.
\]

Tensoring by the defining spinor \(V\) flips central parity. In the ordered bases

\[
(1,\eta,\eta^{-1},3)
\]

and

\[
(V,\eta V,\eta^{-1}V),
\]

the McKay incidence operator \(B:\mathbb C^4\to\mathbb C^3\) is

\[
\boxed{
B=
\begin{pmatrix}
1&0&0&1\\
0&1&0&1\\
0&0&1&1
\end{pmatrix}.
}
\]

It has

\[
\operatorname{rank}B=3,
\qquad
\dim\ker B=1,
\qquad
\dim\ker B^\dagger=0.
\]

Therefore

\[
\boxed{
\operatorname{ind}(B)=1.
}
\]

Define

\[
Q_B=
\begin{pmatrix}
0&0\\
B&0
\end{pmatrix},
\qquad
Q_B^\dagger=
\begin{pmatrix}
0&B^\dagger\\
0&0
\end{pmatrix}.
\]

Then

\[
Q_B^2=(Q_B^\dagger)^2=0
\]

and

\[
H_B=
\{Q_B,Q_B^\dagger\}
=
\operatorname{diag}(B^\dagger B,BB^\dagger).
\]

Hence this incidence system is an exact finite \(N=2\) supersymmetric quantum-mechanical model with

\[
\boxed{\Delta_W=1.}
\]

Its spectra are

\[
\boxed{
\operatorname{spec}(B^\dagger B)=\{0,1,1,4\},
\qquad
\operatorname{spec}(BB^\dagger)=\{1,1,4\}.
}
\]

The unique protected zero mode is

\[
\boxed{
v_0=(1,1,1,-1)^T,
}
\]

up to scale and basis-sign convention.

## 7. Affine \(E_6\) dimension vector inside the same incidence operator

Let

\[
d_+=(1,1,1,3)^T,
\qquad
d_-=(2,2,2)^T.
\]

Then

\[
\boxed{
Bd_+=2d_-,
\qquad
B^\dagger d_-=2d_+.
}
\]

Therefore the full bipartite adjacency operator

\[
D_{\rm McK}
=
\begin{pmatrix}
0&B^\dagger\\
B&0
\end{pmatrix}
\]

satisfies

\[
\boxed{
D_{\rm McK}
\binom{d_+}{d_-}
=
2
\binom{d_+}{d_-}.
}
\]

Equivalently,

\[
\boxed{
C_{\widetilde E_6}
=
2I-D_{\rm McK}
}
\]

annihilates the positive affine dimension vector.

Thus the same rectangular matrix \(B\) carries the McKay adjacency, a finite SUSY factorization with Witten index \(+1\), and the affine-\(E_6\) dimension-vector relation.

## 8. Relation to the actual Fock supercharges

The one-particle creation operators transforming in \(V\subset K^*\) change fermion parity and obey the representation-selection rules encoded by the same McKay graph.

Accordingly \(B\) is an irrep-type, decategorified incidence matrix for the defining-spinor creation channel.

This does **not** identify the graph-level SUSY Hamiltonian \(H_B\) with the Fock-space supertranslation Hamiltonian. In particular:

- the McKay-incidence model has \(\Delta_W(B)=+1\);
- the nonzero-momentum CAR supertranslation channels have fully paired constant anticommutator Hamiltonians and do not acquire that graph index merely by collapsing to irrep support.

The collapse from operator blocks to the seven-node support graph is not index-preserving.

The exact common statement is instead

\[
\boxed{
\text{CAR oddness}
\longleftrightarrow
\text{central-parity flip}
\longleftrightarrow
\widetilde E_6\text{ selection-rule adjacency}.
}
\]

## 9. Stable Hilbert-Hotel class of the graph-incidence model

The finite McKay incidence operator has index \(+1\). After the standard infinite-dimensional stabilization used in Fredholm \(K\)-theory, its connected Fredholm class is the same index class as the adjoint unilateral shift:

\[
\boxed{
[B]_{\rm stable}
=
[S^\dagger]_{\rm Fredholm},
\qquad
\Delta_W=+1.
}
\]

This statement concerns the separate graph-incidence SUSY model. It is not an identification of the physical/internal Fock supercharge with \(S^\dagger\).

## 10. Status firewall

### EXACT / STANDARD GIVEN THE DECLARED REPRESENTATION RING

- the seven irreducible \(2T\)-types and McKay fusion rules;
- the exterior-algebra decompositions above;
- the twist–completeness equivalence for \(K_j=V\oplus\eta^jV\);
- the intertwiner dichotomy by Schur's lemma;
- the exact minimum of four fermionic modes for representation-complete \(2T\) support;
- the exceptional four-mode exclusion for \(2O/E_7\) and \(2I/E_8\);
- the explicit affine-\(E_6\) bipartite incidence matrix;
- its rank, index, SUSY spectrum and protected zero mode;
- the affine dimension-vector equations \(Bd_+=2d_-\) and \(B^\dagger d_-=2d_+\);
- stable Fredholm equivalence of index-\(+1\) graph-incidence systems after standard stabilization.

### NOT YET CLAIMED

- that the twist–completeness equivalence or mode-minimal McKay-SUSY packaging is absent from the literature;
- that graph-incidence SUSY and the Fock supertranslation Hamiltonian are the same object;
- that this finite representation-theoretic SUSY is physical supersymmetry;
- a physical spin-statistics theorem;
- uniqueness of the tetrahedral SIC from Fock completeness alone.

## 11. Current novelty target

The strongest candidate statement requiring a dedicated literature audit is the joint package:

\[
\boxed{
\text{tetrahedral SIC}
\to
\text{nontrivial Naimark }C_3\text{ twist}
\to
\text{representation-complete four-mode Fock carrier}
}
\]

together with the exact compensated supercharge support theorem already established in the TIR \(C_3\) branch:

\[
\boxed{
E(Q^1)=E(Q^2)=E_{\widetilde E_6}.
}
\]

The component theorems are standard or exact specializations; priority for this synthesis remains open.
