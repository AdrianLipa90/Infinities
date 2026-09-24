# TIR C3-Untwisted Naimark-Complement Doubled Rest-Frame Superalgebra v0.1

Status: **EXACT_2T_COVARIANT_DOUBLED_REST_FRAME_SUPERALGEBRA / C3_COMPENSATOR_EXACT / CROSS_CAR_EXACT / FULL_LORENTZ_N2_OPEN / NOVELTY_OPEN**

Date: 2026-09-22

Parents:
- research/TIR_SIC_NAIMARK_CAR_SUPERSYMMETRY_V0_1.md
- research/TIR_NAIMARK_FOCK_MCKAY_E6_V0_1.md
- TIR/integration/TIR_IDT_MOD6PI_C3_PAULI_CROSSWALK_V0_1.md

## 1. One-particle decomposition in the CAR orientation

The tetrahedral supercharge uses the conjugate Naimark outcome representation. In that orientation the one-particle carrier splits as

\[
\boxed{
\overline{\mathcal K}
=
\mathcal A\oplus\mathcal B,
\qquad
\mathcal A\cong\rho,
\qquad
\mathcal B\cong\rho\chi^2,
}
\]

where
\[
\chi:2T\to U(1)
\]
is a nontrivial character of
\[
2T/Q_8\cong C_3.
\]

The two summands are orthogonal.

Let
\[
J_A:\mathbb C^2\to\mathcal A,
\qquad
J_B:\mathbb C^2\to\mathcal B
\]
be unitary intertwiners, with the second typed as
\[
\overline R(g)J_B
=
J_B\bigl(\chi(g)^2\rho(g)\bigr).
\]

The choice of each irreducible intertwiner is unique up to phase.

## 2. The TIR C3 compensator

Pull the quotient character to the exact three-state TIR C3 character carrier

\[
\mathcal C_3
=
L_1\oplus L_\chi\oplus L_{\chi^2}.
\]

In its character basis define

\[
D(g)
=
\operatorname{diag}
\bigl(
1,\chi(g),\chi(g)^2
\bigr).
\]

Define the cyclic unitary

\[
\boxed{
X
=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}.
}
\]

Then

\[
\boxed{
D(g)XD(g)^\dagger
=
\chi(g)X.
}
\]

Therefore \(X\) is an operator-valued carrier of exactly the inverse twist needed by the Naimark-complement spinor:

\[
\chi\cdot(\rho\chi^2)=\rho.
\]

Reversing the orientation convention exchanges \(X\leftrightarrow X^\dagger\) and \(\chi\leftrightarrow\chi^2\).

## 3. Orthogonal CAR doublets

On
\[
\mathcal F_-(\overline{\mathcal K})
=
\Lambda^\bullet\overline{\mathcal K},
\]
define

\[
a_\alpha^\dagger
=
c^\dagger(J_Ae_\alpha),
\qquad
b_\alpha^\dagger
=
c^\dagger(J_Be_\alpha).
\]

Because the two one-particle summands are orthogonal,

\[
\boxed{
\{a_\alpha,a_\beta^\dagger\}
=
\delta_{\alpha\beta},
}
\]

\[
\boxed{
\{b_\alpha,b_\beta^\dagger\}
=
\delta_{\alpha\beta},
}
\]

and

\[
\boxed{
\{a_\alpha,b_\beta^\dagger\}
=
0.
}
\]

All creation-creation and annihilation-annihilation anticommutators vanish.

## 4. Doubled supercharges at the equal-weight rest frame

For the tetrahedral equal-weight sector
\[
p_a=p,
\]
the momentum bispinor is

\[
\boxed{
P_{\alpha\dot\beta}
=
4p\,\delta_{\alpha\dot\beta}.
}
\]

On the enlarged carrier

\[
\mathcal H_{\rm ext}
=
\mathcal C_3
\otimes
\mathcal F_-(\overline{\mathcal K}),
\]

define

\[
\boxed{
Q^1_\alpha
=
2\sqrt{2p}\,
I_3\otimes a_\alpha^\dagger,
}
\]

and

\[
\boxed{
Q^2_\alpha
=
2\sqrt{2p}\,
X\otimes b_\alpha^\dagger.
}
\]

### Theorem — exact doubled rest-frame superalgebra

The two supercharge doublets satisfy

\[
\boxed{
\{Q^I_\alpha,\overline Q^J_{\dot\beta}\}
=
2\delta^{IJ}
P_{\alpha\dot\beta},
\qquad
I,J=1,2,
}
\]

and

\[
\boxed{
\{Q^I_\alpha,Q^J_\beta\}=0,
\qquad
\{\overline Q^I_{\dot\alpha},\overline Q^J_{\dot\beta}\}=0.
}
\]

Proof:

For \(I=J=1\), the result follows from the CAR of the A-doublet.

For \(I=J=2\), the internal factor cancels because
\[
XX^\dagger=X^\dagger X=I_3.
\]

For \(I\neq J\), the mixed terms vanish because
\[
\mathcal A\perp\mathcal B
\]
implies the cross-CAR relations.

The normalization gives

\[
(2\sqrt{2p})^2
=
8p
=
2(4p),
\]
which is exactly
\[
2P_{\alpha\dot\beta}
\]
in the rest frame.

## 5. 2T covariance

Under the combined action of

\[
D(g)
\]
on the TIR C3 carrier and fermionic second quantization of
\[
\overline R(g)
\]
on Fock space,

\[
Q^1
\]
transforms as \(\rho\).

For the second doublet, the factors transform as

\[
X\mapsto\chi X,
\]

and

\[
b^\dagger
\mapsto
(\rho\chi^2)b^\dagger.
\]

Therefore

\[
\boxed{
Q^2
\mapsto
\chi(\rho\chi^2)Q^2
=
\rho Q^2.
}
\]

Thus both doublets carry the same defining spinor representation after the exact C3 compensation.

The center satisfies
\[
\chi(-I)=1,
\]
so both doublets retain the same spinorial minus sign and remain odd under fermion parity.

## 6. What this proves

It proves an exact algebra with the form of an \(\mathcal N=2\) supertranslation algebra at the equal-weight rest frame, together with exact covariance under the binary tetrahedral subgroup.

This closes the earlier complement problem at the discrete rest-frame level:

\[
\boxed{
\text{Naimark primary spinor}
+
\text{C3-untwisted Naimark complement}
\to
\text{two orthogonal supercharge doublets}.
}
\]

## 7. What this does not prove

The following remain open:

1. extension from the discrete spin subgroup \(2T\) to full connected \(SL(2,\mathbb C)\) Lorentz-spin covariance;
2. extension away from equal tetrahedral weights / the rest frame;
3. a physical interpretation of the TIR C3 carrier as an R-symmetry or other physical internal symmetry;
4. a physical realization of supersymmetry in Nature.

Accordingly the result is named

\[
\boxed{
\textbf{2T-covariant doubled rest-frame superalgebra}
}
\]

rather than a full four-dimensional physical \(\mathcal N=2\) theory.

## 8. Relation to the E6 envelope

The first supercharge uses the primary Naimark spinor summand.

The second uses the previously spectator complement after exact C3 compensation.

Therefore the doubled construction is the first current operator package that acts nontrivially on both spinorial summands of the four-dimensional Naimark one-particle carrier.

This is stronger than the single-Q construction, but it still does not by itself prove that all affine-E6 McKay edges are dynamically generated.

That stronger graph-dynamics statement remains a separate gate.

## 9. Validation

Validator:

validation/validate_tir_c3_untwisted_naimark_n2_rest_v0_1.py

The validator checks:
- the conjugate one-particle decomposition;
- orthogonality of the two spinor summands;
- the C3 Weyl-pair identity \(DXD^\dagger=\chi X\);
- compensated complement character \(=\rho\);
- both CAR doublets and all cross-CAR terms;
- the full doubled anticommutator algebra on the 48-dimensional finite carrier.

Current CI verdict:

PASS.

## 10. Novelty firewall

Every ingredient has standard ancestors: finite-group character twisting, C3 Weyl pairs, CAR/Fock functors, Naimark complements, and supersymmetry algebras.

The specific use of the TIR C3 character carrier to untwist the tetrahedral SIC Naimark complement and close the second orthogonal supercharge doublet is retained as a novelty candidate only.

A dedicated literature-priority audit is required before any novelty claim.
