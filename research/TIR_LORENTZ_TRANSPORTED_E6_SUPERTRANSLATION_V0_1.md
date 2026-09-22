# TIR Lorentz-Transported Affine-E6 Supertranslation Theorem v0.1

Status: **ALGEBRAIC_SL2C_ORBIT_CLOSED / TIMELIKE_TETRAHEDRAL_LITTLE_GROUP_EXACT / E6_SUPPORT_ORBIT_INVARIANT / FINITE_UNITARY_LORENTZ_IMPLEMENTATION_NO_GO**

Date: 2026-09-22

Parents:
- research/TIR_C3_UNTWISTED_NAIMARK_N2_REST_V0_1.md
- research/TIR_C3_E6_GRAPH_DYNAMICS_V0_1.md
- CLAIMS_V1_9.md
- TIR Stage-14 McKay closure \(2T\leftrightarrow\widetilde E_6\)

## 1. Full tetrahedral symmetry forces the rest decomposition

Let

\[
k_a=(1,\mathbf n_a),
\qquad
a=1,\dots,4,
\]

be the four future-null tetrahedral generators and let

\[
P=\sum_{a=1}^4 p_a k_a,
\qquad p_a\ge0.
\]

The rotational tetrahedral group \(A_4\) acts transitively on the four rays.

If the weighted decomposition is invariant under the full \(A_4\) action, then transitivity forces

\[
p_1=p_2=p_3=p_4=:p.
\]

Since

\[
\sum_a\mathbf n_a=0,
\]

one obtains

\[
\boxed{
P_0=(4p,0,0,0).
}
\]

In spinor/Hermitian form,

\[
\boxed{
P_{0,\alpha\dot\beta}=m\,\delta_{\alpha\dot\beta},
\qquad
m=4p.
}
\]

Thus the equal-weight rest frame is not an arbitrary extra choice once full tetrahedral invariance of the weighted null decomposition is imposed.

For \(p>0\),

\[
P_0^2=m^2=16p^2>0.
\]

## 2. Tetrahedral fixed-vector theorem

The real spatial representation of \(A_4\) on \(\mathbb R^3\) has no nonzero invariant vector. Therefore the fixed subspace of the standard \(A_4\) action on Minkowski space is

\[
\boxed{
\operatorname{Fix}_{\mathbb R^{1,3}}(A_4)
=
\mathbb R\,e_0.
}
\]

Consequently every nonzero future momentum fixed by the full tetrahedral rotational symmetry is timelike.

In particular, no nonzero null momentum is stabilized by the full tetrahedral \(A_4\) in the standard Lorentz-vector representation.

This is a representation-theoretic statement; it is not a claim that physical particles with the present internal structure must be massive.

## 3. Algebraic \(SL(2,\mathbb C)\) orbit of the rest momentum

Represent a future timelike momentum by a positive Hermitian \(2\times2\) matrix

\[
P=P_\mu\sigma^\mu>0.
\]

Its Lorentz norm is

\[
\det P=m^2>0.
\]

For the rest representative

\[
P_0=mI_2,
\]

and any \(L\in SL(2,\mathbb C)\), define

\[
\boxed{
P[L]=LP_0L^\dagger
=
mLL^\dagger.
}
\]

Then

\[
\det P[L]=m^2.
\]

Conversely, for every positive Hermitian \(P\) with \(\det P=m^2\), let \(P^{1/2}\) be its positive square root and define

\[
\boxed{
L=m^{-1/2}P^{1/2}.
}
\]

Then

\[
\det L=1
\]

and

\[
P=LP_0L^\dagger.
\]

Hence

\[
\boxed{
\{mLL^\dagger:L\in SL(2,\mathbb C)\}
=
\{P>0:\det P=m^2\}.
}
\]

Varying \(m>0\) covers the open future timelike cone. The future null cone is the degenerate boundary \(\det P=0\).

## 4. Lorentz transport of the doubled supertranslation algebra

At rest the previous theorem gives two supercharge doublets

\[
Q^I_\alpha,
\qquad I=1,2,
\]

satisfying

\[
\{Q^I_\alpha,\overline Q^J_{\dot\beta}\}
=
2\delta^{IJ}
(P_0)_{\alpha\dot\beta},
\]

and

\[
\{Q^I_\alpha,Q^J_\beta\}=0.
\]

For \(L\in SL(2,\mathbb C)\), define

\[
\boxed{
Q^I_\alpha[L]
=
L_\alpha{}^\beta Q^I_\beta.
}
\]

Then by bilinearity,

\[
\begin{aligned}
\{Q^I_\alpha[L],\overline Q^J_{\dot\beta}[L]\}
&=
L_\alpha{}^\gamma
\overline L_{\dot\beta}{}^{\dot\delta}
\{Q^I_\gamma,\overline Q^J_{\dot\delta}\}\\
&=
2\delta^{IJ}
(LP_0L^\dagger)_{\alpha\dot\beta}.
\end{aligned}
\]

Therefore

\[
\boxed{
\{Q^I_\alpha[L],\overline Q^J_{\dot\beta}[L]\}
=
2\delta^{IJ}P[L]_{\alpha\dot\beta}.
}
\]

Likewise,

\[
\boxed{
\{Q^I_\alpha[L],Q^J_\beta[L]\}=0.
}
\]

Thus the exact rest-frame construction closes algebraically on the entire future timelike \(SL(2,\mathbb C)\) orbit.

No finite-dimensional unitary Lorentz action on the state carrier is required for this algebraic covariance statement.

## 5. Lorentz transport of the tetrahedral null decomposition

Let the rest-frame null spinors obey

\[
k_{a,\alpha\dot\alpha}
=
\lambda_{a,\alpha}\bar\lambda_{a,\dot\alpha}.
\]

Define

\[
\lambda_a[L]=L\lambda_a.
\]

Then

\[
k_a[L]
=
Lk_aL^\dagger
=
\lambda_a[L]\lambda_a[L]^\dagger
\]

remains rank-one future null, and for equal weights

\[
\boxed{
\sum_a p\,k_a[L]
=
LP_0L^\dagger
=
P[L].
}
\]

Therefore the four-ray decomposition itself is Lorentz covariant.

However, the qubit-SIC/Parseval normalization is not invariant under a generic boost:

\[
\sum_a
\frac{\lambda_a[L]\lambda_a[L]^\dagger}{2}
=
LL^\dagger,
\]

which equals \(I\) only for \(L\in SU(2)\).

Hence the correct distinction is

\[
\boxed{
\text{tetrahedral SIC/Naimark normalization}
=
\text{rest-frame/internal metric structure},
}
\]

while

\[
\boxed{
\text{rank-one null-spinor decomposition}
=
\text{Lorentz-covariant structure}.
}
\]

## 6. Transported tetrahedral little group

At rest,

\[
2T\subset SU(2)
\]

stabilizes \(P_0=mI\).

For

\[
P[L]=LP_0L^\dagger,
\]

define

\[
\boxed{
2T_{P[L]}
=
L(2T)L^{-1}.
}
\]

For every \(u\in2T\),

\[
g=LuL^{-1}
\]

satisfies

\[
gP[L]g^\dagger
=
P[L].
\]

Therefore

\[
\boxed{
2T_{P[L]}
\subset
\operatorname{Stab}_{SL(2,\mathbb C)}(P[L]).
}
\]

The abstract group is unchanged, so its representation ring and McKay graph remain

\[
\boxed{
2T_{P[L]}
\longleftrightarrow
\widetilde E_6.
}
\]

Thus every point of the transported timelike orbit carries a conjugate binary-tetrahedral discrete little-group frame.

## 7. Affine-\(E_6\) operator support is invariant on the orbit

For fixed source and target isotypic projectors \(P_\lambda,P_\mu\), form the two-component block vector

\[
\mathcal B^{I}_{\mu\lambda}
=
\begin{pmatrix}
P_\mu Q^I_1P_\lambda\\
P_\mu Q^I_2P_\lambda
\end{pmatrix}.
\]

Under Lorentz transport,

\[
\boxed{
\mathcal B^{I}_{\mu\lambda}[L]
=
L\,\mathcal B^{I}_{\mu\lambda}.
}
\]

Because \(L\) is invertible,

\[
\mathcal B^{I}_{\mu\lambda}[L]=0
\iff
\mathcal B^{I}_{\mu\lambda}=0.
\]

Therefore the union support of the spinor doublet is unchanged.

Since the rest-frame theorem proves

\[
E(Q^1)=E(Q^2)=E_{\widetilde E_6},
\]

we obtain

\[
\boxed{
E(Q^1[L])
=
E(Q^2[L])
=
E_{\widetilde E_6}
\qquad
\forall L\in SL(2,\mathbb C).
}
\]

This is an algebraic support theorem. It does not identify \(E_6\) as a physical gauge group.

## 8. Finite-dimensional unitary Lorentz no-go

The connected real Lie group \(SL(2,\mathbb C)\) is noncompact and simple up to its finite center.

A nontrivial continuous finite-dimensional unitary representation would induce a nonzero Lie-algebra homomorphism

\[
\mathfrak{sl}(2,\mathbb C)_{\mathbb R}
\to
\mathfrak u(n).
\]

Its kernel is an ideal. Simplicity would make a nonzero map injective, embedding the noncompact simple real Lie algebra into a compact Lie algebra. This is impossible.

Therefore

\[
\boxed{
\text{every continuous finite-dimensional unitary representation of connected }SL(2,\mathbb C)
\text{ is trivial}.
}
\]

Hence the present finite \(C_3\otimes\)Fock carrier cannot itself be the full nontrivial unitary Lorentz Hilbert representation.

The correct status split is:

\[
\boxed{
\text{algebraic }SL(2,\mathbb C)\text{ covariance}
=
\text{CLOSED},
}
\]

\[
\boxed{
\text{nontrivial finite-dimensional unitary Lorentz implementation}
=
\text{IMPOSSIBLE},
}
\]

\[
\boxed{
\text{infinite-dimensional unitary Poincaré/SUSY state representation}
=
\text{OPEN}.
}
\]

## 9. Updated theorem chain

The current exact chain is

\[
\boxed{
\begin{array}{c}
\text{tetrahedral SIC/Naimark internal fiber}\\
\downarrow\\
\text{C3-compensated doubled rest-frame supercharges}\\
\downarrow\\
E(Q^1)=E(Q^2)=\widetilde E_6\\
\downarrow\quad SL(2,\mathbb C)\\
\text{full future timelike algebraic orbit}\\
\downarrow\\
2T_P\text{ discrete little-group frame}\\
\downarrow\\
E(Q^1[P])=E(Q^2[P])=\widetilde E_6.
\end{array}
}
\]

## 10. Firewall

This theorem proves algebraic Lorentz covariance of the supertranslation relations and orbit-invariance of the affine-\(E_6\) operator support.

It does not prove:

- a physical unitary super-Poincaré representation;
- locality or a quantum field theory;
- physical spin-statistics;
- an \(E_6\) gauge theory;
- supersymmetry in Nature.

The next mathematically clean gate is an induced-representation construction in which the finite tetrahedral/Naimark/Fock/\(C_3\) structure appears as an internal or little-group fiber over the massive momentum orbit.
