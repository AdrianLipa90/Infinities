# Claim ledger v1.10 — Tetrahedral rest uniqueness, transported little group, and E6-support orbit invariance

This ledger is additive to \`CLAIMS_V1_9.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-147 | Full \(A_4\) invariance of the four tetrahedral null-ray weights forces \(p_1=p_2=p_3=p_4\) by transitivity | EXACT | permutation-orbit proof + finite group validator |
| INF-148 | The equal-weight tetrahedral momentum is uniquely \(P_0=(4p,0,0,0)\), hence timelike for \(p>0\) | EXACT | tetrahedral first-moment identity |
| INF-149 | The fixed subspace of the standard \(A_4\) Lorentz-vector action is the time axis; no nonzero null vector is fixed by the full tetrahedral rotation group | EXACT REPRESENTATION FACT | irreducibility/no-invariant-spatial-vector argument |
| INF-150 | For each timelike \(P[L]=LP_0L^\dagger\), the conjugate subgroup \(2T_{P[L]}=L(2T)L^{-1}\) lies in the \(SL(2,\mathbb C)\) stabilizer of \(P[L]\) | EXACT | direct conjugation identity + 24-element fixtures |
| INF-151 | Lorentz transport of the four rank-one null spinors preserves the null decomposition and reproduces \(P[L]\) exactly | EXACT | direct spinor-factorization audit |
| INF-152 | The tetrahedral SIC/Parseval frame operator transforms as \(I\mapsto LL^\dagger\), so generic boosts preserve the null-spinor structure but not the rest-frame SIC normalization | EXACT | frame-operator identity + fixtures |
| INF-153 | The union of nonzero inter-isotypic blocks of a spinor doublet is invariant under any invertible \(L\in SL(2,\mathbb C)\) acting on the spinor index | EXACT LINEAR-ALGEBRA THEOREM | invertibility argument |
| INF-154 | Because the rest-frame supercharge support is affine \(\widetilde E_6\), the Lorentz-transported spinor doublets have the same affine-\(E_6\) support on the full timelike algebraic orbit | EXACT COROLLARY | INF-153 + v1.8 |
| INF-155 | The abstract McKay correspondence of the transported discrete little group remains \(2T_{P[L]}\leftrightarrow\widetilde E_6\) because conjugation does not change the group or its representation ring | EXACT | group-conjugacy argument |
| INF-156 | Algebraic \(SL(2,\mathbb C)\) covariance of the supertranslation relations does not require a finite-dimensional unitary Lorentz action on the state carrier | EXACT STATUS DISTINCTION | v1.9 + present note |
| INF-157 | The finite \(C_3\otimes\)Fock carrier by itself supplies a nontrivial continuous finite-dimensional unitary representation of connected \(SL(2,\mathbb C)\) | FALSE | standard noncompact-simple-group no-go |
| INF-158 | A physical infinite-dimensional induced super-Poincaré representation carrying the finite tetrahedral/Naimark/Fock/\(C_3\) structure as a fiber is already constructed | OPEN / NOT CLAIMED | next representation-theory gate |

## v1.10 core

The rest-frame assumption has been narrowed to a symmetry theorem:

\[
A_4\text{-invariant tetrahedral weights}
\Longrightarrow
p_1=p_2=p_3=p_4
\Longrightarrow
P_0=(4p,0,0,0).
\]

The exact finite supercharge system then transports algebraically over the entire timelike Lorentz orbit, with a conjugate binary-tetrahedral little-group frame and unchanged affine-\(E_6\) operator-support graph.

The remaining open problem is a unitary infinite-dimensional state-space realization, not the algebraic Lorentz covariance of the supertranslation relations.
