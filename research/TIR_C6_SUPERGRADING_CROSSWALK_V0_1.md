# TIR C6-Refined Supersymmetry Grading Crosswalk v0.1

Status: **EXACT_C6_REFINEMENT / SIX_8D_SECTORS / SUPERCHARGE_DEGREE_3 / IDT_C6_REPRESENTATION_CROSSWALK_CLOSED / PHYSICAL_TEMPORAL_BINDING_OPEN**

Date: 2026-09-22

Parents:
- research/TIR_C3_RESOLVED_N2_LONG_MULTIPLETS_V0_1.md
- research/TIR_C3_ARM_DECOMPOSITION_MCKAY_INDEX_V0_1.md
- TIR/integration/TIR_IDT_MOD6PI_C3_PAULI_CROSSWALK_V0_1.md
- research/EULER_HILBERT_HOTEL_SUPERSYMMETRY_V0_4.md

## 1. Two commuting finite gradings

The compensated finite supersymmetry carrier has a conserved internal operator

\[
\mathcal Z^3=I,
\qquad
[\mathcal Z,Q^I_\alpha]=0,
\]

and the fermionic Fock space has parity

\[
\mathcal P_F=(-1)^F,
\qquad
\mathcal P_F^2=I,
\qquad
\{\mathcal P_F,Q^I_\alpha\}=0.
\]

The operators commute:

\[
[\mathcal Z,\mathcal P_F]=0.
\]

Define

\[
\boxed{
\mathcal G_6
=
\mathcal Z\,\mathcal P_F.
}
\]

Since the orders \(3\) and \(2\) are coprime,

\[
\boxed{
\mathcal G_6^6=I.
}
\]

More strongly,

\[
\boxed{
\mathcal G_6^3=\mathcal P_F,
\qquad
\mathcal G_6^4=\mathcal Z,
\qquad
\mathcal G_6^2=\mathcal Z^2.
}
\]

Thus \(\mathcal G_6\) contains both the internal \(C_3\) charge and fermion parity. This is the concrete Chinese-remainder realization

\[
\boxed{
C_6\cong C_3\times Z_2.
}
\]

## 2. Six exact eigensectors

Let

\[
\zeta_6=e^{2\pi i/6}.
\]

Define the spectral projectors

\[
\Pi_q^{(6)}
=
\frac16
\sum_{k=0}^5
\zeta_6^{-qk}\mathcal G_6^k,
\qquad
q\in\mathbb Z_6.
\]

Write

\[
\mathcal H_q
=
\Pi_q^{(6)}\mathcal H_{\rm ext}.
\]

The 48-dimensional carrier decomposes as

\[
\boxed{
\mathcal H_{\rm ext}
=
\bigoplus_{q=0}^{5}\mathcal H_q.
}
\]

The previous \(C_3\)-resolved theorem gives three 16-dimensional sectors, each with eight even and eight odd Fock states. Therefore every joint \((C_3,Z_2)\) character occurs with multiplicity eight, and hence

\[
\boxed{
\dim\mathcal H_q=8
\qquad
(q=0,\ldots,5).
}
\]

Equivalently, as a \(C_6\)-module,

\[
\boxed{
\mathcal H_{\rm ext}
\cong
8\,\mathbb C[C_6],
}
\]

eight copies of the regular representation.

## 3. Exact charge dictionary

Let

\[
\mathcal Z\psi=\omega^r\psi,
\qquad
\mathcal P_F\psi=(-1)^f\psi,
\]

with

\[
r\in\mathbb Z_3,
\qquad
f\in\mathbb Z_2.
\]

Then

\[
\mathcal G_6\psi
=
\zeta_6^q\psi
\]

with

\[
\boxed{
q
\equiv
2r+3f
\pmod6.
}
\]

Conversely,

\[
\boxed{
f\equiv q\pmod2,
\qquad
r\equiv2q\pmod3.
}
\]

Thus the \(C_6\) charge is exactly equivalent to the pair consisting of conserved internal \(C_3\) charge and fermion parity.

The three 16-state long-multiplet sectors refine as

\[
\boxed{
\mathcal M_0
=
\mathcal H_0\oplus\mathcal H_3,
}
\]

\[
\boxed{
\mathcal M_1
=
\mathcal H_2\oplus\mathcal H_5,
}
\]

\[
\boxed{
\mathcal M_2
=
\mathcal H_4\oplus\mathcal H_1.
}
\]

Each pair contains an eight-dimensional even half and an eight-dimensional odd half.

## 4. Supercharges have degree three

Because the compensated supercharges commute with \(\mathcal Z\) and are odd under fermion parity,

\[
\mathcal ZQ^I_\alpha\mathcal Z^{-1}
=
Q^I_\alpha,
\]

\[
\mathcal P_FQ^I_\alpha\mathcal P_F^{-1}
=
-Q^I_\alpha.
\]

Therefore

\[
\boxed{
\mathcal G_6Q^I_\alpha\mathcal G_6^{-1}
=
-Q^I_\alpha
=
\zeta_6^3 Q^I_\alpha.
}
\]

Hence every supercharge has \(C_6\) degree \(3\):

\[
\boxed{
Q^I_\alpha:
\mathcal H_q
\longrightarrow
\mathcal H_{q+3}.
}
\]

The ordinary \(Z_2\) supergrading is therefore the quotient/refinement shadow of the \(C_6\) grading:

\[
\boxed{
\deg_{Z_2}Q
=
3\bmod2
=
1.
}
\]

This is a \(C_6\)-refinement of an ordinary supersymmetric grading, not a claim of a new physical six-fold supersymmetry algebra.

## 5. Exact crosswalk to the existing IDT \(C_6\) carrier

The TIR-IDT Mod-\(6\pi\) crosswalk already defines

\[
G_T
=
P_T\otimes J_\chi
\]

with

\[
P_T^3=I,
\qquad
J_\chi^2=I,
\qquad
[P_T,J_\chi]=0,
\]

and proves

\[
\boxed{
G_T^6=I,
\qquad
G_T^3=J_\chi.
}
\]

It also follows directly that

\[
\boxed{
G_T^4=P_T.
}
\]

The supersymmetry carrier satisfies the identical finite-extension algebra

\[
\boxed{
\mathcal G_6^6=I,
\qquad
\mathcal G_6^3=\mathcal P_F,
\qquad
\mathcal G_6^4=\mathcal Z.
}
\]

Hence there is an exact abstract representation crosswalk

\[
\boxed{
P_T
\longleftrightarrow
\mathcal Z,
\qquad
J_\chi
\longleftrightarrow
\mathcal P_F,
\qquad
G_T
\longleftrightarrow
\mathcal G_6.
}
\]

Both sides realize the same extension

\[
\boxed{
1\to Z_2\to C_6\to C_3\to1.
}
\]

This closes only the finite representation crosswalk. It does not identify the IDT temporal carrier with the internal \(C_3\) charge, nor the Stage-23 chirality label with physical fermion parity.

## 6. Spinorial \(C_6\) lift and fermion parity

The same TIR-IDT crosswalk has the Pauli lift

\[
U_3
=
\exp\left[
-\frac{i\pi}{3}
\frac{\sigma_x+\sigma_y+\sigma_z}{\sqrt3}
\right]
\in SU(2),
\]

with

\[
\boxed{
U_3^3=-I,
\qquad
U_3^6=I.
}
\]

The SIC/Naimark/Fock theorem independently proves

\[
\boxed{
-I_{\rm spin}
\longmapsto
(-1)^F.
}
\]

Therefore, after choosing the orientation of the \(C_6\) generator, the two central-extension patterns fit the commutative relation

\[
\boxed{
U_3^3=-I
\quad\longmapsto\quad
\mathcal G_6^3=(-1)^F.
}
\]

This is an exact representation-theoretic compatibility between the spinorial double cover and the refined Fock grading.

It is not a spin-statistics theorem and does not identify the IDT numerical \(6\pi\) budget with a physical spin-rotation period.

## 7. Affine-\(E_6\) graph complex as a degree-three \(C_6\) complex

The graph-incidence theorem has three \(C_3\) Fourier channels. Under the \(C_6\) refinement they become

\[
q=0\longrightarrow3,
\]

\[
q=2\longrightarrow5,
\]

\[
q=4\longrightarrow1.
\]

Each map has degree \(3\).

The two nontrivial \(C_3\) channels are invertible scalar maps and have zero index.

The trivial channel is

\[
B_0=(1,\sqrt3):\mathbb C^2\to\mathbb C
\]

and has index \(+1\).

Thus the graph complex has the exact \(C_6\)-resolved spectrum

\[
\boxed{
q=0:\ \{0,4\},
\qquad
q=3:\ \{4\},
}
\]

\[
\boxed{
q=2,5,4,1:\ \{1\}.
}
\]

The unique protected graph zero mode lies in the neutral \(C_6\) sector

\[
\boxed{
q=0.
}
\]

Therefore the graph-incidence index can be sharpened to

\[
\boxed{
\operatorname{Ind}_{C_6}(B)
=
[\mathbf1],
}
\]

the trivial \(C_6\) character, while the actual 16-state long-multiplet Fock index remains zero.

## 8. Structural meaning

The chain is now

\[
\boxed{
C_3^{\rm int}\times Z_2^F
\cong
C_6
}
\]

with

\[
\boxed{
\text{three }16D\text{ long multiplets}
=
\text{three pairs of opposite-by-3 }C_6\text{ sectors}.
}
\]

The supercharges preserve the \(C_3\) label but exchange the two parity halves:

\[
\boxed{
q\leftrightarrow q+3.
}
\]

The IDT six-state carrier and the supersymmetry six-grade carrier therefore share the same exact finite extension structure.

## 9. Firewall

### EXACT

- \(\mathcal G_6=\mathcal Z(-1)^F\) has order six;
- \(\mathcal G_6^3=(-1)^F\) and \(\mathcal G_6^4=\mathcal Z\);
- the 48D carrier splits into six rank-8 eigensectors;
- the \(C_6\) charge is equivalent to the joint \(C_3\times Z_2\) charge;
- every compensated supercharge has \(C_6\) degree three;
- the three long multiplets are the three \(q\leftrightarrow q+3\) pairs;
- the IDT \(C_3\times Z_2\) six-cycle has the same abstract \(C_6\) extension algebra;
- the graph-incidence protected mode lies in the neutral \(C_6\) channel.

### NOT CLAIMED

- that IDT temporal phase is physically identical to the internal \(C_3\) symmetry;
- that Stage-23 chirality is physically identical to fermion parity;
- that the numerical \(6\pi\) IDT phase budget is a spin-rotation period;
- a physical spin-statistics theorem;
- a new kind of six-fold physical supersymmetry;
- literature novelty before a dedicated priority audit.

## 10. Current frontier

The exact finite carrier now has one generator that simultaneously recovers the two previously separate gradings:

\[
\boxed{
\mathcal G_6
\quad\Longrightarrow\quad
\mathcal Z=\mathcal G_6^4,
\qquad
(-1)^F=\mathcal G_6^3.
}
\]

The next mathematical question is whether this \(C_6\)-refined grading has a useful universal characterization among finite supersymmetric Clifford modules with a commuting order-three internal symmetry, and whether the tetrahedral SIC/Naimark construction is minimal or unique under that characterization.
