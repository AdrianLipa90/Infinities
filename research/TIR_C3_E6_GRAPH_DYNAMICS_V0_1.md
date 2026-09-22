# TIR C3-Compensated Fock–McKay E6 Operator-Support Theorem v0.1

Status: **EXACT_AFFINE_E6_OPERATOR_SUPPORT / BOTH_SUPERCHARGE_CHANNELS_PASS / FULL_LORENTZ_IMPLEMENTATION_OPEN / NOVELTY_OPEN**

Date: 2026-09-22

Parents:
- research/TIR_SIC_NAIMARK_CAR_SUPERSYMMETRY_V0_1.md
- research/TIR_NAIMARK_FOCK_MCKAY_E6_V0_1.md
- research/TIR_C3_UNTWISTED_NAIMARK_N2_REST_V0_1.md
- TIR Stage 14 McKay closure: 2T <-> affine E6

## 1. Question

The previous note established that the doubled rest-frame construction acts on both spinorial Naimark summands, but left open whether the resulting odd operators realize the full affine-E6 McKay adjacency dynamically.

The precise finite question is:

For the combined carrier

\[
\widetilde{\mathcal F}
=
\mathcal C_3\otimes
\Lambda^\bullet\overline{\mathcal K},
\]

does the nonzero inter-isotypic operator support of the two supercharge channels project exactly to the affine-E6 McKay graph?

The answer is yes.

## 2. Representation data

Use the seven irreducible 2T types

\[
1,\chi,\chi^2,\rho,\rho\chi,\rho\chi^2,3,
\]

with defining spinor \(\rho\). Tensoring by \(\rho\) gives the affine-E6 edges

\[
1\!-\!\rho,\qquad
\chi\!-\!\rho\chi,\qquad
\chi^2\!-\!\rho\chi^2,
\]

and

\[
3\!-\!\rho,\qquad
3\!-\!\rho\chi,\qquad
3\!-\!\rho\chi^2.
\]

Let this six-edge set be \(E_{\widetilde E_6}\).

The conjugate Naimark one-particle carrier is

\[
\overline{\mathcal K}
=
\mathcal A\oplus\mathcal B,
\]

with

\[
\mathcal A\cong\rho,
\qquad
\mathcal B\cong\rho\chi^2
\]

in the orientation convention of the parent note.

Creation from \(\mathcal A\) therefore transforms as \(\rho\). Creation from \(\mathcal B\) transforms as \(\rho\chi^2\).

## 3. Internal C3 labeling

The TIR character carrier is

\[
\mathcal C_3
=
L_1\oplus L_\chi\oplus L_{\chi^2}.
\]

A state in internal sector \(L_{\chi^r}\) and Fock irrep \(\lambda\) has effective 2T type

\[
\boxed{
[\lambda,r]_{\rm eff}
=
\chi^r\lambda.
}
\]

For \(Q^1\), the internal operator is \(I_3\), so \(r\) is unchanged.

For \(Q^2\), the compensator \(X\) obeys

\[
D(g)XD(g)^\dagger=\chi(g)X
\]

in the convention of the parent note. Equivalently, if the complement one-particle twist is written as \(\rho\chi^2\), the internal shift contributes exactly the inverse character required to make the full operator transform as \(\rho\).

Thus both full supercharge channels have effective 2T operator type

\[
\boxed{\rho.}
\]

## 4. Selection-rule no-extra-edge theorem

Because \(Q^I\) transforms as \(\rho\), Schur/Frobenius selection gives

\[
P_\mu Q^I P_\lambda\neq0
\quad\Longrightarrow\quad
\mu\subset\rho\otimes\lambda.
\]

Therefore a nonzero block can occur only on a McKay edge.

Hence the operator-support graph satisfies

\[
\boxed{
E(Q^I)\subseteq E_{\widetilde E_6}.
}
\]

This excludes spurious non-McKay transitions after the C3 compensation is included.

## 5. Exhaustion theorem

The finite validator constructs all 24 elements of \(2T\), the complete exterior-Fock representation, the seven central character projectors, and the two orthogonal creation doublets.

For \(Q^1\), after the three internal \(C_3\) sectors are folded to effective irrep labels, the nonzero block support is exactly

\[
\boxed{
E(Q^1)=E_{\widetilde E_6}.
}
\]

For the complement channel \(Q^2\), before compensation the raw Fock transitions are the character-twisted McKay graph. The internal \(C_3\) shift removes that twist. After folding to effective labels,

\[
\boxed{
E(Q^2)=E_{\widetilde E_6}.
}
\]

Therefore both supercharge channels independently have the complete affine-E6 support graph.

### Theorem — doubled Fock–McKay operator support

On

\[
\widetilde{\mathcal F}
=
\mathcal C_3\otimes
\Lambda^\bullet\overline{\mathcal K},
\]

the two exact rest-frame supercharge doublets satisfy

\[
\boxed{
E(Q^1)
=
E(Q^2)
=
E_{\widetilde E_6}
}
\]

after collapsing multiplicities and internal character copies to effective \(2T\) irrep types.

Thus the previously open graph-dynamics support gate is closed.

## 6. What "dynamic E6" means here

The theorem is deliberately typed.

It means:

- the Hilbert carrier contains all seven 2T irrep types;
- the odd supercharges have defining-spinor transformation type after compensation;
- the set of nonzero inter-isotypic supercharge blocks is exactly the six-edge affine-E6 McKay graph.

It does not mean:

- an E6 gauge theory;
- the finite simple Lie algebra \(E_6\) acts as a physical gauge symmetry;
- every matrix element along a McKay edge has equal magnitude;
- a physical particle spectrum is identified with E6 nodes.

The result is an operator-support theorem for the affine McKay graph.

## 7. Why the earlier rank-two firewall is refined, not contradicted

The single tetrahedral supercharge coefficient matrix has one-particle rank two. That remains true.

The missing point was that McKay adjacency itself is defined by tensoring with the defining two-dimensional spinor \(\rho\). A rank-two spinor operator is therefore exactly the correct representation type to generate McKay edges.

The previous rank-two observation correctly rejected the stronger statement that one supercharge spans the full four-dimensional Naimark one-particle carrier. It does not forbid the same rank-two operator from realizing the full \(\rho\)-McKay adjacency across a representation-complete Fock space.

The new validator checks the actual inter-isotypic blocks rather than inferring graph dynamics from one-particle rank alone.

## 8. New exact chain

The current finite theorem chain is

\[
\boxed{
\begin{array}{c}
\text{tetrahedral SIC}\\
\downarrow\\
\text{minimal Naimark }(\rho\oplus\rho\chi^2)\\
\downarrow\\
\text{exterior Fock: all seven }2T\text{ irreps}\\
\downarrow\\
\text{TIR }C_3\text{ compensation}\\
\downarrow\\
Q^1,Q^2\text{ both of effective type }\rho\\
\downarrow\\
\text{nonzero operator blocks}\\
=\widetilde E_6\text{ adjacency}.
\end{array}
}
\]

## 9. Remaining frontier

The next gate is no longer affine-E6 support.

It is the relation between the finite exact rest-frame construction and connected Lorentz covariance.

Two distinct levels must be separated:

1. **algebraic Lorentz orbit:** transform the spinor indices by \(L\in SL(2,\mathbb C)\) and momentum by \(P\mapsto LPL^\dagger\);
2. **unitary implementation on states:** construct an appropriate infinite-dimensional Poincare/SUSY representation carrying the finite Naimark/Fock/C3 structure as an internal fiber.

A nontrivial finite-dimensional unitary representation of the noncompact connected Lorentz-spin group cannot supply the second level. The finite 48-dimensional carrier should therefore be treated as a rest-frame/internal fiber, not as the full physical one-particle Hilbert representation.

## 10. Novelty firewall

McKay correspondence, finite-group character projectors, exterior Fock representations, and supersymmetry selection rules are standard ingredients.

The exact equality between the compensated supercharge support graph and affine E6 in this tetrahedral SIC/Naimark/TIR-C3 construction is retained as a novelty candidate only until a dedicated priority audit is completed.
