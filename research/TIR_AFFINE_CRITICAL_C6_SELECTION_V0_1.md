# TIR Affine-Critical C6 Supergrading Selection Theorem v0.1

Status: **EXACT_FAMILY_CLASSIFICATION / AFFINE_CRITICALITY_SELECTS_N3 / C6_SUPERGRADING_SELECTED / TOPOLOGICAL_INDEX_NOT_SELECTOR / PHYSICAL_TEMPORAL_BINDING_OPEN**

Date: 2026-09-22

Parents:
- research/TIR_CYCLIC_ARM_CRITICALITY_E6_V0_1.md
- research/TIR_C6_SUPERGRADING_CROSSWALK_V0_1.md
- research/TIR_C3_ARM_DECOMPOSITION_MCKAY_INDEX_V0_1.md
- TIR/integration/TIR_IDT_MOD6PI_C3_PAULI_CROSSWALK_V0_1.md

## 1. Uniform cyclic-arm supersymmetry family

For each integer \(n\ge1\), let

\[
B_n=[I_n\mid\mathbf1_n]:
\mathbb C^{n+1}\to\mathbb C^n
\]

be the cyclic \(n\)-arm graph-incidence operator.

The arm-rotation symmetry is

\[
C_n=\langle R_n\rangle,
\qquad
R_n^n=I.
\]

The finite SUSY factorization has the ordinary fermionic grading

\[
Z_2^F=\langle\mathcal P_F\rangle,
\qquad
\mathcal P_F^2=I.
\]

The arm action and fermion parity commute.

Hence the joint finite grading group is

\[
\boxed{
\mathcal G_n
=
C_n\times Z_2^F.
}
\]

## 2. Cyclicity of the joint grading

A direct product \(C_n\times C_2\) is cyclic exactly when

\[
\gcd(n,2)=1.
\]

Therefore

\[
\boxed{
C_n\times Z_2
\cong
C_{2n}
\iff
n\text{ is odd}.
}
\]

When \(n\) is odd, the element

\[
G_{2n}=R_n\mathcal P_F
\]

has order

\[
\operatorname{ord}(G_{2n})
=
\operatorname{lcm}(n,2)
=
2n
\]

and generates the whole product.

Moreover,

\[
\boxed{
G_{2n}^n=\mathcal P_F.
}
\]

Because \(n\) is odd, choose the inverse of \(2\) modulo \(n\),

\[
s=\frac{n+1}{2},
\qquad
2s\equiv1\pmod n.
\]

Then

\[
\boxed{
G_{2n}^{\,2s}=R_n.
}
\]

Thus one cyclic generator recovers both the arm rotation and fermion parity.

For even \(n\), \(C_n\times Z_2\) is not cyclic and the product element \(R_n\mathcal P_F\) has order \(n\), not \(2n\).

## 3. Supercharge degree in the odd-\(n\) cyclic refinement

Suppose the compensated supercharges preserve the arm/internal \(C_n\) character and are odd under fermion parity:

\[
R_nQR_n^{-1}=Q,
\qquad
\mathcal P_FQ\mathcal P_F^{-1}=-Q.
\]

Then for odd \(n\),

\[
\boxed{
G_{2n}QG_{2n}^{-1}
=
-Q.
}
\]

Let

\[
\zeta_{2n}=e^{2\pi i/(2n)}.
\]

Since

\[
-1=\zeta_{2n}^{\,n},
\]

the supercharge has exact cyclic degree

\[
\boxed{
\deg_{C_{2n}}Q=n.
}
\]

Thus

\[
\boxed{
Q:\mathcal H_q\to\mathcal H_{q+n}.
}
\]

The ordinary \(Z_2\) oddness is recovered by reducing the \(C_{2n}\) degree modulo \(2\).

## 4. Spectral criticality independently selects \(n=3\)

The exact cyclic-arm spectral theorem gives

\[
\rho(A_n)=\sqrt{n+1}
\]

for the full bipartite adjacency

\[
A_n=
\begin{pmatrix}
0&B_n^\dagger\\
B_n&0
\end{pmatrix}.
\]

The associated simply-laced Cartan-type matrix

\[
C_n^{\rm Cartan}=2I-A_n
\]

is affine-critical exactly when

\[
\rho(A_n)=2.
\]

Hence

\[
\sqrt{n+1}=2
\iff
n=3.
\]

Therefore

\[
\boxed{
C_n^{\rm Cartan}\text{ is affine-critical}
\iff
n=3.
}
\]

At that unique point,

\[
\Gamma_3\cong\widetilde E_6.
\]

## 5. Affine criticality selects the sixfold supergrading

Combining Sections 2 and 4,

\[
\boxed{
\text{affine criticality}
\Longrightarrow
n=3
\Longrightarrow
C_n\times Z_2^F
=
C_3\times Z_2^F
\cong
C_6.
}
\]

Moreover the supercharge degree becomes

\[
\boxed{
\deg_{C_6}Q=3.
}
\]

Thus, within the declared uniform cyclic two-step-arm family,

\[
\boxed{
\widetilde E_6\text{ affine closure}
\Longleftrightarrow
n=3
\Longrightarrow
\text{cyclic six-grade supersymmetry refinement}.
}
\]

This is a selection theorem for the finite grading structure.

It does not identify the resulting \(C_6\) with a physical spacetime periodicity.

## 6. Topological versus spectral selectors

The graph-Fredholm index satisfies

\[
\boxed{
\operatorname{ind}(B_n)=1
\qquad
\forall n\ge1.
}
\]

Therefore the protected Hilbert-Hotel defect does not select the arm number.

By contrast,

\[
\boxed{
\rho(A_n)=2
\iff
n=3.
}
\]

Hence the two mechanisms have sharply different roles:

\[
\boxed{
\text{Fredholm/Witten index}
=
\text{universal topological defect},
}
\]

\[
\boxed{
\text{affine spectral criticality}
=
\text{three-arm selector}.
}
\]

At the selected point, fermion parity refines the selected \(C_3\) into \(C_6\).

## 7. Relation to the IDT six-state carrier

The pre-existing TIR-IDT crosswalk has the exact finite carrier

\[
C_3^{\rm IDT}\times Z_2^\chi
\cong
C_6
\]

with generator

\[
G_T=P_T\otimes J_\chi.
\]

The present theorem arrives at the same group order through an independent route:

\[
\boxed{
\text{affine graph criticality}
\to
C_3
\to
C_3\times Z_2^F
\cong
C_6.
}
\]

Thus the number six is no longer merely the product of an already chosen three-cycle and a binary grading inside this supersymmetry branch: the arm number three is itself uniquely selected by the affine spectral threshold in the declared graph family.

The exact representation crosswalk is

\[
\boxed{
C_6^{\rm IDT\ label}
\cong
C_6^{\rm SUSY\ grading}
}
\]

as finite cyclic representations.

The physical identifications

\[
C_3^{\rm temporal}
\stackrel{?}{=}
C_3^{\rm internal}
\]

and

\[
Z_2^\chi
\stackrel{?}{=}
Z_2^F
\]

remain open.

## 8. Critical spectra

For general \(n\),

\[
\operatorname{spec}(B_n^\dagger B_n)
=
\{0,1^{(n-1)},n+1\}.
\]

At \(n=3\),

\[
\boxed{
\operatorname{spec}(B_3^\dagger B_3)
=
\{0,1,1,4\}.
}
\]

Under the selected \(C_6\) grading:

- the protected neutral mode lies at \(q=0\) with eigenvalue \(0\);
- the two nontrivial arm characters occupy the nontrivial \(C_3\) channels and have eigenvalue \(1\);
- the affine positive dimension mode is \(C_3\)-trivial/even and has eigenvalue \(4\).

Thus the critical Hamiltonian hierarchy is simultaneously compatible with the \(C_6\) refinement.

## 9. Compact theorem statement

### Theorem — Affine-critical sixfold supergrading selection

For the uniform cyclic two-step-arm family

\[
B_n=[I_n\mid\mathbf1_n],
\]

equipped with commuting arm symmetry \(C_n\) and fermion parity \(Z_2^F\):

1. \(\operatorname{ind}(B_n)=1\) for every \(n\);
2. \(2I-A_n\) is affine-critical iff \(n=3\);
3. at the unique affine point, \(\Gamma_3\cong\widetilde E_6\);
4. because \(3\) is odd,

\[
C_3\times Z_2^F\cong C_6;
\]

5. any supercharge preserving the arm \(C_3\) and flipping fermion parity has \(C_6\) degree \(3\).

Therefore

\[
\boxed{
\text{affine }E_6\text{ criticality}
\Longrightarrow
\text{three arms}
\Longrightarrow
C_6\text{-refined supersymmetry grading}.
}
\]

## 10. Firewall

### EXACT

- cyclicity criterion \(C_n\times C_2\cong C_{2n}\iff n\) odd;
- supercharge degree \(n\) in the odd-\(n\) cyclic refinement;
- universal graph index \(+1\);
- affine criticality iff \(n=3\);
- \(\Gamma_3\cong\widetilde E_6\);
- selected grading \(C_3\times Z_2^F\cong C_6\);
- degree-three supercharge at the selected point.

### NOT CLAIMED

- that the mathematical \(C_6\) is a physical time period;
- that it proves the IDT \(6\pi\) phase budget from first principles;
- that IDT chirality equals physical fermion parity;
- that affine \(E_6\) is a physical gauge symmetry;
- literature novelty before a dedicated audit.

The strongest exact conclusion is family-internal: the spectral affine threshold selects the same threefold arm count whose combination with supersymmetric parity produces the sixfold cyclic refinement.
