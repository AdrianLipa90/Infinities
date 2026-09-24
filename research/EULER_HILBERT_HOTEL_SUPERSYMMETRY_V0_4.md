# Euler-Hilbert-Hotel Supersymmetry v0.4 — SIC/Naimark/Fock/McKay refinement

Status: EXACT REPRESENTATION-THEORETIC PACKAGE / NOVELTY NOT YET CLAIMED

Date: 2026-09-22

## 1. Scope

This revision attacks one narrow mathematical gate: whether the tetrahedral qubit SIC, its minimal Naimark dilation, and the binary-tetrahedral symmetry determine a non-arbitrary odd supersymmetry operator and a distinguished McKay/ADE structure.

No physical spin-statistics theorem, RH claim, or ToE claim is made.

## 2. Tetrahedral SIC and the minimal Naimark split

Let u_a in C^2, a=1,...,4, be normalized tetrahedral SIC spinors and put

\[
P_a=|u_a\rangle\langle u_a|,
\qquad
E_a=\frac12P_a.
\]

Then

\[
\sum_a E_a=I_2,
\qquad
|\langle u_a,u_b\rangle|^2=\frac13
\quad(a\ne b).
\]

Set phi_a=u_a/sqrt(2) and define the analysis isometry

\[
V:C^2\to K:=C^4,
\qquad
(V\psi)_a=\langle\phi_a,\psi\rangle.
\]

Then

\[
V^\dagger V=I_2.
\]

Let P=VV^\dagger. The minimal Naimark carrier splits as

\[
K=W_+\oplus W_-,
\qquad
W_+=\operatorname{Ran}P,
\qquad
W_-=\operatorname{Ran}(I-P),
\]

with dim W_+=dim W_-=2. The canonical Naimark grading is

\[
\boxed{\Gamma_N=2P-I_4,\qquad \Gamma_N^2=I_4.}
\]

## 3. Complement SIC and orientation reversal

For the normalized Gram matrix G=2P, the normalized Naimark-complement Gram matrix is

\[
\boxed{G^\perp=2I_4-G.}
\]

Hence, in a matched complement gauge,

\[
\langle u_a^\perp,u_b^\perp\rangle
=
-\langle u_a,u_b\rangle
\qquad(a\ne b).
\]

Therefore the complement is again a tetrahedral qubit SIC.

For the Bargmann triple invariant

\[
\Delta_{abc}
=
\langle u_a,u_b\rangle
\langle u_b,u_c\rangle
\langle u_c,u_a\rangle,
\]

one has

\[
\boxed{\Delta_{abc}^\perp=-\Delta_{abc}.}
\]

Thus the minimal Naimark complement reverses the oriented tetrahedral Bargmann phase.

## 4. Binary-tetrahedral module decomposition

Let 2T subset SU(2) be the binary tetrahedral group acting on the SIC rays. The induced monomial representation R on K satisfies

\[
\boxed{Vg=R(g)V.}
\]

Consequently both W_+ and W_- are 2T-invariant.

The abelianization is

\[
2T/Q_8\cong C_3.
\]

Let eta be either nontrivial character of this quotient. With orientation convention fixed,

\[
\boxed{
W_-\cong \eta\otimes W_+,
\qquad
\eta^3=1,\ \eta\ne1.
}
\]

Changing the tetrahedral orientation exchanges eta and eta^{-1}.

## 5. Untwisted no-go and twisted uniqueness

Since W_+ and W_- are inequivalent irreducible 2T-modules,

\[
\boxed{\operatorname{Hom}_{2T}(W_+,W_-)=0.}
\]

Thus no nonzero fully 2T-invariant odd map exists between the two Naimark sectors.

But

\[
W_-\cong\eta\otimes W_+,
\]

so Schur's lemma gives

\[
\boxed{
\dim_{\mathbb C}
\operatorname{Hom}_{2T}(\eta\otimes W_+,W_-)=1.
}
\]

Hence there is a twisted intertwiner A_eta:W_+->W_- satisfying

\[
\boxed{
R_-(g)A_\eta
=
\eta(g)A_\eta R_+(g),
}
\]

unique up to nonzero scalar. After unitary normalization it is unique up to phase.

This is the corrected answer to the former "canonical odd map" question: the canonical object is a one-dimensional twisted intertwiner space, not an untwisted invariant map.

## 6. Twisted finite N=2 algebra and discrete R-symmetry

Define on K=W_+\oplus W_-

\[
Q_\eta=
\begin{pmatrix}
0&0\\
A_\eta&0
\end{pmatrix},
\qquad
Q_\eta^\dagger=
\begin{pmatrix}
0&A_\eta^\dagger\\
0&0
\end{pmatrix}.
\]

Then

\[
Q_\eta^2=(Q_\eta^\dagger)^2=0,
\qquad
\{\Gamma_N,Q_\eta\}=0.
\]

If A_eta is unitary,

\[
\boxed{
H_N=\{Q_\eta,Q_\eta^\dagger\}=I_4,
\qquad
\Delta_W=0.
}
\]

The supercharge transforms by

\[
\boxed{
R(g)Q_\eta R(g)^{-1}=\eta(g)Q_\eta.
}
\]

Thus the quotient character C_3 acts as a discrete R-symmetry of the complex supercharge. Its kernel is Q_8.

## 7. Fock lift and central parity

Use K^* as the one-particle space and form

\[
\mathcal F_-(K^*)=\Lambda^\bullet K^*.
\]

The CAR are canonical on this exterior Fock space.

The central element -I in 2T acts as -I on K^*, therefore second quantization gives

\[
\boxed{
\Gamma_-(R^\vee(-I))=(-1)^F.
}
\]

Thus the spinorial central sign becomes fermion parity exactly in this finite representation-theoretic construction.

## 8. Full 2T support in the 16-dimensional Fock space

Choose orientation so that

\[
K\cong 2\oplus\eta 2,
\qquad
K^*\cong 2\oplus\eta^{-1}2.
\]

Using

\[
\Lambda^\bullet 2=1\oplus2\oplus1
\]

and

\[
2\otimes2=1\oplus3,
\]

one obtains

\[
\boxed{
\mathcal F_-(K^*)
\cong
2\cdot1
\oplus
2\cdot\eta
\oplus
\eta^{-1}
\oplus
2
\oplus
\eta2
\oplus
2\cdot(\eta^{-1}2)
\oplus
3.
}
\]

Every irreducible 2T representation type appears at least once.

The parity sectors have supports

\[
\mathcal F_{\rm even}:
\{1,\eta,\eta^{-1},3\},
\]

\[
\mathcal F_{\rm odd}:
\{2,\eta2,\eta^{-1}2\}.
\]

These are exactly the two central-parity classes of the affine E6 McKay graph. Tensoring by the defining doublet flips the central sign, so McKay adjacency is bipartite across the same split.

Therefore, at the level of irreducible support,

\[
\boxed{
\text{fermion parity}
=
\text{central 2T parity}
=
\widetilde E_6\text{ bipartite parity}.
}
\]

## 9. Four-mode exceptional McKay selection theorem

TIR Stage 14 records the positive affine dimension vectors

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
12,\qquad18,\qquad30,
\]

which are the Coxeter numbers h(E6), h(E7), h(E8).

Any representation containing every irreducible representation type at least once must have dimension at least the sum of the irreducible dimensions. A fermionic Fock space on four complex modes has dimension

\[
2^4=16.
\]

Therefore

\[
12\le16,
\qquad
18>16,
\qquad
30>16.
\]

Hence:

\[
\boxed{
\text{Among }2T,2O,2I,
\text{ only }2T\leftrightarrow\widetilde E_6
\text{ can have representation-complete support in a four-mode Fock space.}
}
\]

The tetrahedral SIC/Naimark construction explicitly realizes that possibility.

This is an exact selection theorem inside the exceptional binary-polyhedral sequence. It does not claim that 2T is uniquely selected among all finite groups.

## 10. What this does and does not characterize

The condition "representation-complete four-mode Fock support" alone does not characterize a particular SIC frame; it is representation-theoretic.

A sharper tetrahedral characterization requires the joint hypotheses

\[
\boxed{
\text{four-outcome minimal qubit IC}
+
\text{transitive }A_4\text{ projective covariance}
+
\text{rank-one Parseval normalization}.
}
\]

Under these hypotheses the four Bloch rays form the unique regular tetrahedral orbit up to global unitary/rotation, permutation, and outcome phases.

Thus the strongest present classification is modular:

1. the covariance/IC hypotheses select the tetrahedral SIC;
2. minimal Naimark dilation gives the 2+2 module split;
3. the split forces the nontrivial C_3 twist;
4. the twist gives the unique odd intertwiner line;
5. exterior Fock quantization gives CAR, central parity, and full 2T support;
6. four-mode representation completeness selects E6 among the exceptional E6/E7/E8 McKay sequence.

## 11. Firewall

STANDARD ingredients include Naimark dilation, ETF complement theory, Schur's lemma, exterior Fock/CAR, binary-tetrahedral representation theory, and McKay correspondence.

The exact chain and the four-mode exceptional selection theorem are recorded as a candidate synthesis. No novelty claim is made until a dedicated literature audit has excluded an equivalent prior theorem.

No claim is made that this construction proves physical fermions, physical supersymmetry, or spin-statistics in Nature.
