# TIR C3-Untwisted N=2 Lorentz-Orbit Theorem v0.1

Status: **EXACT_SL2C_COVARIANT_SUPERTRANSLATION_ORBIT / FULL_FUTURE_TIMELIKE_MASS_SHELL_COVER / FINITE_UNITARY_LORENTZ_IMPLEMENTATION_NO_GO / PHYSICAL_SUPER-POINCARE_REPRESENTATION_OPEN**

Date: 2026-09-22

Parents:
- research/TIR_C3_UNTWISTED_NAIMARK_N2_REST_V0_1.md
- research/TIR_C3_E6_GRAPH_DYNAMICS_V0_1.md

## 1. Rest-frame input

The finite carrier

\[
\mathcal H_{\rm ext}
=
\mathcal C_3\otimes
\Lambda^\bullet\overline{\mathcal K}
\]

already carries two exact supercharge doublets satisfying at equal tetrahedral weight

\[
\boxed{
\{Q^I_\alpha,\overline Q^J_{\dot\beta}\}
=
2\delta^{IJ}m\,\delta_{\alpha\dot\beta},
\qquad
I,J=1,2,
}
\]

with

\[
m=4p>0,
\]

and

\[
\{Q^I_\alpha,Q^J_\beta\}=0.
\]

Equivalently the rest momentum bispinor is

\[
P_0=mI_2.
\]

## 2. Algebraic SL(2,C) orbit

For any

\[
L\in SL(2,\mathbb C)
\]

define transformed supercharges by the standard undotted/dotted spinor action

\[
\boxed{
Q^I_\alpha[L]
=
L_\alpha{}^\beta Q^I_\beta,
}
\]

\[
\boxed{
\overline Q^I_{\dot\alpha}[L]
=
\overline L_{\dot\alpha}{}^{\dot\beta}
\overline Q^I_{\dot\beta}.
}
\]

Then bilinearity of the anticommutator gives

\[
\begin{aligned}
\{Q^I_\alpha[L],\overline Q^J_{\dot\beta}[L]\}
&=
L_\alpha{}^\gamma
\overline L_{\dot\beta}{}^{\dot\delta}
\{Q^I_\gamma,\overline Q^J_{\dot\delta}\}\\
&=
2\delta^{IJ}
m(LL^\dagger)_{\alpha\dot\beta}.
\end{aligned}
\]

Define

\[
\boxed{
P[L]=mLL^\dagger.
}
\]

Therefore

\[
\boxed{
\{Q^I_\alpha[L],\overline Q^J_{\dot\beta}[L]\}
=
2\delta^{IJ}P_{\alpha\dot\beta}[L].
}
\]

Same-chirality anticommutators remain zero.

### Theorem 1 — Lorentz-covariant supertranslation orbit

The exact doubled rest-frame algebra extends canonically to an \(SL(2,\mathbb C)\)-covariant family of \(\mathcal N=2\)-form supertranslation algebras by spinor-index transport.

No extension of the nontrivial \(C_3\) character to \(SL(2,\mathbb C)\) is required: after the TIR \(C_3\) compensation has produced two effective defining-spinor doublets, the internal \(C_3\) carrier is held fixed under the Lorentz action.

## 3. Full future timelike mass shell

Every matrix

\[
P[L]=mLL^\dagger
\]

is positive Hermitian and satisfies

\[
\det P[L]
=
m^2|\det L|^2
=
m^2.
\]

Under

\[
P=p_\mu\sigma^\mu,
\]

this is

\[
(p^0)^2-|\mathbf p|^2=m^2,
\qquad
p^0>0.
\]

Conversely, for every positive-definite Hermitian \(2\times2\) matrix \(P\) with \(\det P=m^2\),

\[
L=\frac{P^{1/2}}{\sqrt m}
\]

has determinant one and obeys

\[
P=mLL^\dagger.
\]

Hence:

\[
\boxed{
\{mLL^\dagger:L\in SL(2,\mathbb C)\}
=
\mathcal H_m^+,
}
\]

the complete future timelike mass shell of mass \(m\).

Allowing \(m>0\) to vary covers the entire open future timelike cone. The future null cone is its boundary/degeneration.

Thus the equal-weight tetrahedral rest frame is not a terminal restriction of the algebra: it is a base point whose Lorentz orbit covers every future timelike momentum at fixed mass.

## 4. Boosted tetrahedral interpretation

At rest the four tetrahedral null spinors \(\lambda_a\) satisfy

\[
P_0
=
p\sum_a\lambda_a\lambda_a^\dagger
=
mI_2.
\]

Under \(L\),

\[
\lambda_a\mapsto L\lambda_a,
\]

and therefore

\[
P_0
\mapsto
p\sum_a
(L\lambda_a)(L\lambda_a)^\dagger
=
LP_0L^\dagger
=
P[L].
\]

So the entire tetrahedral null decomposition can be boosted covariantly.

A general boost does not preserve the Euclidean Bloch-sphere SIC metric or Parseval normalization. What it preserves is the null-spinor decomposition and Lorentz causal structure. The SIC/Naimark construction should therefore be interpreted as the canonical rest-frame/internal normalization, with the Lorentz orbit acting on the spinor momentum decomposition afterward.

## 5. Finite-dimensional unitary implementation no-go

The preceding \(SL(2,\mathbb C)\) action is an algebraic action on the supercharge spinor indices.

It cannot be implemented nontrivially by a continuous finite-dimensional unitary representation on the present 48-dimensional carrier.

Indeed, suppose

\[
U:SL(2,\mathbb C)\to U(N)
\]

were a continuous nontrivial finite-dimensional unitary representation. Its derivative would be a Lie-algebra homomorphism from the real simple noncompact Lie algebra

\[
\mathfrak{sl}(2,\mathbb C)_{\mathbb R}
\]

to the compact Lie algebra

\[
\mathfrak u(N).
\]

The kernel is an ideal, so a nonzero homomorphism would be injective. But a noncompact simple Lie algebra cannot embed as a Lie subalgebra of a compact Lie algebra with its positive-definite invariant form. Therefore the derivative is zero, and connectedness forces \(U\) to be trivial.

Hence:

\[
\boxed{
\text{nontrivial connected Lorentz covariance}
\not\subset
\text{finite-dimensional unitary state implementation}.
}
\]

This is not a defect of the tetrahedral construction; it is the standard noncompact-group obstruction.

## 6. Correct architecture for a physical state representation

The finite carrier should therefore be typed as a rest-frame/internal fiber.

A genuine unitary Poincare or super-Poincare representation requires an infinite-dimensional momentum/orbit sector, schematically

\[
\boxed{
\mathscr H_m
=
L^2(\mathcal H_m^+,d\mu_m)
\otimes
\mathcal H_{\rm internal},
}
\]

with

\[
\mathcal H_{\rm internal}
\supset
\mathcal C_3\otimes
\Lambda^\bullet\overline{\mathcal K}.
\]

Momentum then acts by multiplication on the mass shell and Lorentz transformations by the usual induced-representation mechanism. Constructing that unitary induced representation while preserving the exact Naimark/C3/Fock structure is the next separate gate.

## 7. Status correction

The earlier statement

\[
\text{FULL LORENTZ N=2 = OPEN}
\]

is now split more precisely:

\[
\boxed{
\text{SL(2,C)-covariant supertranslation algebraic orbit}
=
\text{CLOSED EXACT}.
}
\]

\[
\boxed{
\text{nontrivial finite-dimensional unitary Lorentz implementation}
=
\text{IMPOSSIBLE}.
}
\]

\[
\boxed{
\text{infinite-dimensional unitary super-Poincare state representation}
=
\text{OPEN}.
}
\]

## 8. Firewall

This theorem does not prove physical supersymmetry in Nature.

It also does not construct the Lorentz generators as self-adjoint operators on a physical Hilbert space, nor establish locality, quantum fields, or a spin-statistics theorem.

It closes only the algebraic Lorentz-orbit problem and identifies the correct representation-theoretic reason that the physical state implementation must leave the finite-dimensional carrier.
