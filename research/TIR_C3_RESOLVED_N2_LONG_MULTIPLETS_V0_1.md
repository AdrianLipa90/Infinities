# TIR C3-Resolved Massive N=2 Long-Multiplet Decomposition v0.1

Status: **EXACT_SU2_X_C3_EXTENSION / THREE_16D_LONG_MULTIPLETS / UNITARY_MASSIVE_INDUCED_REPRESENTATION_EXISTS / E6_ENVELOPE_IS_DIAGONAL_2T_SHADOW**

Date: 2026-09-22

Parents:
- research/TIR_C3_UNTWISTED_NAIMARK_N2_REST_V0_1.md
- research/TIR_C3_E6_GRAPH_DYNAMICS_V0_1.md
- research/TIR_LORENTZ_TRANSPORTED_E6_SUPERTRANSLATION_V0_1.md
- CLAIMS_V1_10.md

## 1. The hidden compact extension

In the CAR orientation of the previous construction, the four-dimensional one-particle carrier splits as

\[
\overline{\mathcal K}
=
\mathcal A\oplus\mathcal B,
\]

with

\[
\mathcal A\cong \rho,
\qquad
\mathcal B\cong \rho\chi^2
\]

under the diagonal binary-tetrahedral action, where

\[
\chi:2T\to C_3
\]

is the nontrivial quotient character used in the current orientation convention.

The twist does not need to be extended as a character of connected \(SU(2)\). Instead, separate the compact little-group and internal factors.

Let

\[
S\cong\mathbb C^2
\]

carry the defining representation of \(SU(2)\), and let the internal \(C_3\) act with charges

\[
0\quad\text{on }\mathcal A,
\qquad
2\quad\text{on }\mathcal B.
\]

Then the one-particle carrier extends to a unitary representation of

\[
\boxed{
SU(2)_{\rm little}\times C_3^{\rm int}
}
\]

with

\[
\boxed{
\overline{\mathcal K}
\cong
(S\otimes L_0)
\oplus
(S\otimes L_2).
}
\]

Under the diagonal embedding

\[
\boxed{
\Delta_\chi(2T)
=
\{(g,\chi(g)):g\in2T\}
\subset
SU(2)\times C_3,
}
\]

the restriction is exactly

\[
\rho\oplus\rho\chi^2.
\]

Thus the nontrivial Naimark character twist is an internal \(C_3\) charge, not an obstruction to extending the spin factor to the full massive little group.

## 2. The extended 48-dimensional rest carrier

Let

\[
\mathcal C_3
=
L_0\oplus L_1\oplus L_2
\]

be the regular three-character carrier with

\[
Z_{\mathcal C}
=
\operatorname{diag}(1,\omega,\omega^2),
\qquad
\omega=e^{2\pi i/3},
\]

and cyclic shift \(X\) satisfying

\[
Z_{\mathcal C}XZ_{\mathcal C}^\dagger
=
\omega X.
\]

The finite rest carrier is

\[
\boxed{
\mathcal H_{\rm ext}
=
\mathcal C_3
\otimes
\Lambda^\bullet(\mathcal A\oplus\mathcal B),
}
\]

with

\[
\dim\mathcal H_{\rm ext}=3\cdot2^4=48.
\]

The compensated rest supercharges are

\[
Q^1_\alpha
=
2\sqrt{2p}\,
I_{\mathcal C_3}\otimes a_\alpha^\dagger,
\]

\[
Q^2_\alpha
=
2\sqrt{2p}\,
X\otimes b_\alpha^\dagger.
\]

## 3. A conserved internal \(C_3\) charge

Let the internal \(C_3\) act on the one-particle Fock carrier by

\[
Y
=
I_{\mathcal A}
\oplus
\omega^2 I_{\mathcal B}.
\]

Its fermionic second quantization is

\[
\Gamma_-(Y)
=
\omega^{2N_{\mathcal B}},
\]

where \(N_{\mathcal B}\) is the number operator for the two \(\mathcal B\)-modes.

Define

\[
\boxed{
\mathcal Z
=
Z_{\mathcal C}
\otimes
\Gamma_-(Y).
}
\]

Then

\[
\mathcal Z^3=I.
\]

For the first supercharge,

\[
\mathcal Z Q^1_\alpha\mathcal Z^\dagger
=
Q^1_\alpha.
\]

For the second,

\[
Z_{\mathcal C}XZ_{\mathcal C}^\dagger
=
\omega X
\]

and

\[
\Gamma_-(Y)b_\alpha^\dagger\Gamma_-(Y)^\dagger
=
\omega^2 b_\alpha^\dagger,
\]

so

\[
\boxed{
\mathcal Z Q^2_\alpha\mathcal Z^\dagger
=
\omega^3 Q^2_\alpha
=
Q^2_\alpha.
}
\]

Therefore

\[
\boxed{
[\mathcal Z,Q^I_\alpha]=0
\qquad
(I=1,2).
}
\]

The compensating \(C_3\) is thus a genuine conserved internal symmetry of the doubled rest superalgebra in this construction.

## 4. Three invariant 16-dimensional supermultiplet sectors

Let

\[
\Pi_r
=
\frac13
\sum_{k=0}^2
\omega^{-rk}\mathcal Z^k,
\qquad
r=0,1,2.
\]

Then

\[
\Pi_r\Pi_s=\delta_{rs}\Pi_r,
\qquad
\sum_r\Pi_r=I.
\]

Every Fock basis state has a unique internal \(\mathcal C_3\) label giving each prescribed total \(\mathcal Z\)-charge. Hence

\[
\boxed{
\operatorname{rank}\Pi_r=16
}
\]

for every \(r\).

Define

\[
\mathcal M_r=\Pi_r\mathcal H_{\rm ext}.
\]

Because \(\mathcal Z\) commutes with all supercharges,

\[
\boxed{
Q^I_\alpha\mathcal M_r
\subseteq
\mathcal M_r.
}
\]

Thus

\[
\boxed{
\mathcal H_{\rm ext}
=
\mathcal M_0
\oplus
\mathcal M_1
\oplus
\mathcal M_2
}
\]

is a decomposition into three independent 16-dimensional supersymmetry modules.

## 5. Each sector is the standard massive \(N=2\) Clifford module

Inside each \(\mathcal M_r\), the four normalized raising operators

\[
a_1^\dagger,\quad
a_2^\dagger,\quad
Xb_1^\dagger,\quad
Xb_2^\dagger
\]

obey the ordinary four-mode CAR.

Therefore each sector is canonically a four-fermion exterior module:

\[
\boxed{
\mathcal M_r
\cong
\Lambda^\bullet(S\oplus S),
}
\]

up to the overall conserved \(C_3\) charge \(\omega^r\).

Under \(SU(2)_{\rm little}\),

\[
S\oplus S
\]

is two copies of the defining spinor. Hence

\[
\boxed{
\mathcal M_r
\cong
5\cdot\mathbf1
\oplus
4\cdot\mathbf2
\oplus
\mathbf3
}
\]

as an \(SU(2)\) representation.

The dimensions are

\[
5+4\cdot2+3=16.
\]

This is exactly the standard massive four-dimensional \(N=2\) long Clifford multiplet built on a spin-zero Clifford vacuum, with no shortening/central-charge condition imposed.

## 6. The three sectors under the diagonal binary-tetrahedral subgroup

Restrict the compact symmetry

\[
SU(2)\times C_3
\]

to the diagonal subgroup

\[
\Delta_\chi(2T).
\]

On the \(\mathcal Z\)-charge-\(r\) sector,

\[
\boxed{
\mathcal M_r\big|_{\Delta_\chi(2T)}
\cong
\chi^r
\otimes
\left(
5\cdot1
\oplus
4\cdot\rho
\oplus
3
\right).
}
\]

Therefore

\[
\mathcal M_0:
\quad
5\cdot1
\oplus
4\cdot\rho
\oplus
3,
\]

\[
\mathcal M_1:
\quad
5\cdot\chi
\oplus
4\cdot\rho\chi
\oplus
3,
\]

\[
\mathcal M_2:
\quad
5\cdot\chi^2
\oplus
4\cdot\rho\chi^2
\oplus
3.
\]

Summing,

\[
\boxed{
\mathcal H_{\rm ext}\big|_{\Delta_\chi(2T)}
\cong
5(1\oplus\chi\oplus\chi^2)
\oplus
4(\rho\oplus\rho\chi\oplus\rho\chi^2)
\oplus
3\cdot3.
}
\]

Every one of the seven binary-tetrahedral irreducible types occurs.

Thus the affine-\(E_6\) representation envelope has a sharper interpretation:

\[
\boxed{
\text{full }E_6\text{ support}
=
\text{three }C_3\text{-graded copies of one standard massive }N=2\text{ long multiplet}
}
\]

after restriction to the diagonal finite subgroup and collapse to irrep types.

A single \(16\)-state long multiplet carries one \(E_6\) arm type

\[
\chi^r
-
\rho\chi^r
-
3,
\]

while the three \(C_3\)-related sectors exhaust the three arms.

This is a representation-support statement, not an \(E_6\) gauge theory.

## 7. Exact \(SU(2)\times C_3\) transformation law of the supercharges

The compact little group acts identically on the two one-particle spinor summands:

\[
a_\alpha^\dagger
\mapsto
u_\alpha{}^\beta a_\beta^\dagger,
\]

\[
b_\alpha^\dagger
\mapsto
u_\alpha{}^\beta b_\beta^\dagger,
\qquad
u\in SU(2).
\]

The internal \(C_3\) assigns charge \(0\) to \(a^\dagger\), charge \(2\) to \(b^\dagger\), and charge \(1\) to \(X\).

Hence both full supercharge doublets transform as

\[
\boxed{
Q^I_\alpha
\sim
(\mathbf2,\mathbf1)
\quad\text{under }SU(2)_{\rm little}\times C_3^{\rm int}.
}
\]

The internal \(C_3\) commutes with the supercharges after compensation.

This resolves the earlier apparent obstruction caused by the fact that nontrivial \(C_3\) characters do not extend as characters of connected \(SU(2)\): the character belongs to a separate internal factor.

## 8. Massive unitary induced super-Poincaré representation

Let

\[
\mathcal O_m^+
=
\{P>0:\det P=m^2\}
\]

be the future massive momentum orbit with invariant measure \(d\mu_m\).

For each \(r\), define

\[
\boxed{
\mathscr H_{m,r}
=
L^2(\mathcal O_m^+,d\mu_m)
\otimes
\mathcal M_r.
}
\]

Choose measurable standard boosts \(B(P)\in SL(2,\mathbb C)\) satisfying

\[
P=B(P)(mI)B(P)^\dagger.
\]

For a Lorentz transformation \(\Lambda\), the Wigner rotation is

\[
W(\Lambda,P)
=
B(P)^{-1}
\Lambda
B(\Lambda^{-1}P)
\in SU(2).
\]

Let \(D_r\) be the \(SU(2)\) representation on \(\mathcal M_r\). Then the standard induced action

\[
\boxed{
(U_r(a,\Lambda)\Psi)(P)
=
e^{ia\cdot P}
D_r(W(\Lambda,P))
\Psi(\Lambda^{-1}P)
}
\]

is unitary.

Let \(q^I_\alpha\) denote the rest-frame supercharges on \(\mathcal M_r\). Define on the natural dense momentum-space domain

\[
\boxed{
(Q^I_\alpha\Psi)(P)
=
B(P)_\alpha{}^\beta
q^I_\beta
\Psi(P).
}
\]

Then fiberwise,

\[
\boxed{
\{Q^I_\alpha,\overline Q^J_{\dot\beta}\}
=
2\delta^{IJ}P_{\alpha\dot\beta},
}
\]

with vanishing same-chirality anticommutators.

Thus the standard Wigner-induced construction supplies a nontrivial infinite-dimensional unitary massive super-Poincaré representation carrying each \(\mathcal M_r\) as its rest fiber.

The direct sum

\[
\boxed{
\mathscr H_m
=
\bigoplus_{r=0}^2
\mathscr H_{m,r}
}
\]

carries the conserved internal \(C_3\) and the full three-sector finite envelope.

## 9. Relation to the affine-\(E_6\) support theorem

The unitary induced construction does not make \(E_6\) a continuous gauge symmetry.

Instead, at each timelike momentum the compact little group is a conjugate \(SU(2)_P\), with independent internal \(C_3\). Restricting

\[
SU(2)_P\times C_3
\]

to the conjugated diagonal binary-tetrahedral subgroup reproduces the same seven irrep types and the same McKay support.

Therefore the exact hierarchy is

\[
\boxed{
\text{massive super-Poincaré representation}
\supset
SU(2)_{\rm little}\times C_3^{\rm int}
\supset
\Delta_\chi(2T)
\longleftrightarrow
\widetilde E_6.
}
\]

The \(E_6\) graph is a finite diagonal-subgroup representation envelope/selection graph inside the massive induced representation.

## 10. Firewall

This construction closes the **existence** of a mathematically standard unitary massive induced representation carrying the compensated finite supersymmetry module.

It does not establish:

- that Nature realizes this representation;
- locality or an interacting supersymmetric QFT;
- an \(E_6\) gauge interaction;
- identification of the three \(C_3\) sectors with observed particle generations;
- uniqueness of the induced representation;
- a phenomenological mass spectrum.

The remaining questions are representation selection, dynamics/interactions, and novelty — not the existence of a unitary massive super-Poincaré carrier.
