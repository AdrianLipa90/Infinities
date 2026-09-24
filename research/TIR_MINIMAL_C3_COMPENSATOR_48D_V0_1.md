# TIR Minimal C3 Compensator and 48D Carrier Theorem v0.1

Status: **EXACT_WEYL_DIMENSION_DIVISIBILITY / EXACT_FOUR_MODE_2T_COMPLETENESS / 48D_FACTORISED_MINIMALITY / NOVELTY_NOT_YET_CLAIMED**

Date: 2026-09-22

Parents:
- research/TIR_C3_RESOLVED_N2_LONG_MULTIPLETS_V0_1.md
- research/TIR_C3_ARM_DECOMPOSITION_MCKAY_INDEX_V0_1.md
- research/EULER_HILBERT_HOTEL_SUPERSYMMETRY_V0_5.md

## 1. The compensator problem

The Naimark complement carries a nontrivial \(C_3\) character twist. To compensate it unitarily, the construction uses operators \(Z\) and \(X\) obeying

\[
Z^3=I,
\qquad
ZXZ^\dagger=\omega X,
\qquad
\omega=e^{2\pi i/3}.
\]

The present question is whether the three-dimensional \(C_3\) carrier is merely convenient or forced by the algebra.

## 2. Weyl dimension-divisibility theorem

Let \(Z,X\in GL(n,\mathbb C)\) satisfy

\[
ZXZ^{-1}
=
\omega X,
\]

where \(\omega\) is a primitive \(q\)-th root of unity.

Taking determinants gives

\[
\det(ZXZ^{-1})
=
\det X,
\]

while

\[
\det(\omega X)
=
\omega^n\det X.
\]

Because \(X\) is invertible,

\[
\omega^n=1.
\]

Since \(\omega\) has exact order \(q\),

\[
\boxed{q\mid n.}
\]

Therefore any finite-dimensional invertible carrier of a primitive \(q\)-Weyl commutation relation has dimension divisible by \(q\).

For \(q=3\),

\[
\boxed{3\mid n.}
\]

Hence the smallest nonzero unitary \(C_3\) compensator has dimension

\[
\boxed{n_{\min}=3.}
\]

The standard clock/shift pair

\[
Z=
\operatorname{diag}(1,\omega,\omega^2),
\qquad
X=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}
\]

saturates the lower bound.

## 3. Equivalent eigenspace proof

Decompose the \(Z\)-carrier into character eigenspaces

\[
\mathcal C
=
\mathcal C_0\oplus\mathcal C_1\oplus\mathcal C_2.
\]

The Weyl relation implies

\[
X\mathcal C_r
=
\mathcal C_{r+1}.
\]

If \(X\) is unitary, all three eigenspaces have equal dimension:

\[
\dim\mathcal C_0
=
\dim\mathcal C_1
=
\dim\mathcal C_2.
\]

Thus

\[
\dim\mathcal C
=
3d.
\]

The minimal case \(d=1\) is precisely the regular three-character carrier used by TIR.

So the TIR \(C_3\) compensator is not an arbitrary three-state enlargement: it is the dimension-minimal unitary carrier capable of cancelling a primitive order-three character twist.

## 4. Independent minimum from the binary-tetrahedral Fock sector

The irreducible complex representation dimensions of \(2T\) are

\[
1,1,1,2,2,2,3.
\]

Any representation containing every irrep type at least once has dimension at least

\[
1+1+1+2+2+2+3
=
12.
\]

An \(m\)-mode complex fermionic Fock space has dimension

\[
2^m.
\]

Therefore representation-complete \(2T\) Fock support requires

\[
2^m\ge12,
\]

hence

\[
\boxed{m\ge4.}
\]

The tetrahedral SIC/Naimark one-particle carrier has exactly four complex outcome modes, and the exterior Fock representation contains all seven \(2T\) irreducible types. Therefore

\[
\boxed{
m_{\min}^{2T\text{-complete Fock}}=4,
\qquad
\dim\mathcal F_{\min}=16.
}
\]

## 5. 48-dimensional factorised minimality theorem

Consider the declared architecture class

\[
\mathcal H_{\rm ext}
=
\mathcal C
\otimes
\Lambda^\bullet K,
\]

subject to both conditions:

1. \(\mathcal C\) carries an invertible/unitary primitive \(C_3\) compensator
   \[
   ZXZ^{-1}=\omega X;
   \]
2. \(\Lambda^\bullet K\) contains every irreducible \(2T\)-type at least once.

Then

\[
\dim\mathcal C\ge3
\]

and

\[
\dim\Lambda^\bullet K\ge16.
\]

Therefore

\[
\boxed{
\dim\mathcal H_{\rm ext}
\ge
3\cdot16
=
48.
}
\]

The current TIR/SIC/Naimark/CAR construction has

\[
\dim\mathcal C_3=3,
\qquad
\dim\Lambda^\bullet\mathbb C^4=16,
\]

and hence

\[
\boxed{
\dim\mathcal H_{\rm ext}=48.
}
\]

Thus the existing finite rest carrier saturates both independent lower bounds simultaneously.

### Theorem — 3 x 16 optimality

Within the factorised class above,

\[
\boxed{
48
\text{ is the exact minimal finite dimension}
}
\]

for simultaneous primitive-\(C_3\) unitary twist compensation and representation-complete binary-tetrahedral fermionic Fock support.

## 6. Relation to the three long multiplets

The dimension-minimal compensator has exactly three one-dimensional character sectors.

The dimension-minimal complete Fock carrier has dimension \(16\).

The conserved total \(C_3\) charge therefore resolves the saturated \(48\)-dimensional carrier into

\[
\boxed{
48
=
16+16+16,
}
\]

and each \(16\)-dimensional invariant sector is the standard massive \(N=2\) long Clifford module already established in the parent theorem.

Thus

\[
\boxed{
3\times16=48
}
\]

is not merely dimension bookkeeping in this architecture:

- \(3\) is forced by the primitive \(C_3\) Weyl-compensator relation;
- \(16=2^4\) is forced by four fermionic modes, which are minimal for full \(2T\) irrep support.

## 7. Exceptional comparison

The same Fock-dimension lower-bound logic gives

\[
m\ge4
\quad\text{for }2T/\widetilde E_6,
\]

\[
m\ge5
\quad\text{for }2O/\widetilde E_7,
\]

\[
m\ge5
\quad\text{for }2I/\widetilde E_8.
\]

Only the tetrahedral exceptional case can saturate representation completeness with four fermionic modes.

The present \(48\)-dimensional optimality theorem additionally uses the order-three character twist specific to the \(2T\) architecture.

## 8. Firewall

The theorem is conditional on the declared factorised architecture and on invertible/unitary compensation of a primitive \(C_3\) character.

It does not claim:

- that every conceivable supersymmetry realization requires dimension \(48\);
- that \(48\) is a fundamental physical state count;
- that the three invariant sectors are observed generations;
- a physical \(E_6\) gauge theory;
- literature novelty.

The exact statement is an optimality theorem for the present mathematical architecture:

\[
\boxed{
\text{minimal primitive }C_3\text{ compensator}
\times
\text{minimal }2T\text{-complete fermionic Fock carrier}
=
3\times16
=
48.
}
\]
