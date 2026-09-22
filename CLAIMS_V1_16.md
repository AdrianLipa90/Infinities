# Claim ledger v1.16 — Exceptional McKay balance and cyclic-supergrading selector

This ledger is additive to \`CLAIMS_V1_15.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-225 | The exceptional binary-polyhedral presentations \(G_n=\langle r,s,t\mid r^2=s^3=t^n=rst\rangle\), \(n=3,4,5\), abelianize to \(C_3,C_2,1\) respectively | STANDARD GROUP FACT + EXACT SMITH-NORMAL-FORM DERIVATION | integer relation-matrix validator |
| INF-226 | The number of one-dimensional irreducible characters of \(2T,2O,2I\) is \(3,2,1\), equal to the order of the abelianization | STANDARD FINITE REPRESENTATION FACT | INF-225 |
| INF-227 | Central \(-I\) parity bipartitions each exceptional McKay graph because tensoring by the defining spinor flips the central sign | STANDARD MCKAY/REPRESENTATION FACT | graph bipartition |
| INF-228 | The affine McKay dimension-vector linear sums across the two central-parity classes are \(6|6\) for \(\widetilde E_6\), \(8|10\) for \(\widetilde E_7\), and \(14|16\) for \(\widetilde E_8\) | EXACT | Stage-14 vectors + bipartition validator |
| INF-229 | Linear central-parity balance occurs only for \(2T/\widetilde E_6\) among the exceptional binary-polyhedral family | EXACT FAMILY-LEVEL CLASSIFICATION | INF-228 |
| INF-230 | Quadratic central-parity balance is universal: \(\sum_{\mathcal R_+}d_\lambda^2=\sum_{\mathcal R_-}d_\lambda^2=|G|/2\) | STANDARD REGULAR-CHARACTER IDENTITY + EXACT SPECIALIZATION | character argument + validator |
| INF-231 | The affine dimension-vector sums \(12,18,30\) equal the Coxeter numbers \(h(E_6),h(E_7),h(E_8)\) | STANDARD ADE FACT + EXACT STAGE-14 DATA | dimension-vector sums |
| INF-232 | The joint abelianization/fermion-parity groups are \(C_6\) for \(2T\), \(V_4\) for \(2O\), and \(C_2\) for \(2I\) | EXACT | INF-225 + finite abelian group arithmetic |
| INF-233 | Among \(2T,2O,2I\), only the tetrahedral case has a cyclic joint abelianization/parity grading of order greater than two | EXACT | INF-232 |
| INF-234 | The equality \(|G_{\rm ab}\times Z_2^F|=h/2\) holds only for \(2T/\widetilde E_6\): \(6=12/2\), while \(4\neq18/2\) and \(2\neq30/2\) | EXACT EXCEPTIONAL-FAMILY SELECTION | validator |
| INF-235 | In the \(E_6\) case, the common linear parity sum, the joint \(C_6\) grading order, and \(h(E_6)/2\) are all equal to \(6\) | EXACT | INF-228/232/234 |
| INF-236 | The uniform cyclic-arm affine-critical selector and the exceptional binary-polyhedral balance/cyclicity selector are independent routes that both select the tetrahedral/\(\widetilde E_6\) case | EXACT WITHIN DECLARED FAMILIES | v1.15 + INF-229..235 |
| INF-237 | The combined exceptional selector is literature-first | CANDIDATE ONLY / PRIORITY AUDIT REQUIRED | dedicated novelty search required |
| INF-238 | The selector proves physical \(E_6\), physical time \(C_6\), or supersymmetry in Nature | FALSE / NOT CLAIMED | physical binding/evidence required |

## v1.16 core

Two distinct finite classification problems now converge on the same object.

The graph-family selector gives

\[
\rho(A_n)=2
\iff
n=3
\iff
\Gamma_n\cong\widetilde E_6.
\]

The exceptional binary-polyhedral selector gives

\[
\boxed{
\text{linear central-parity balance}
+
\text{cyclic }(G_{\rm ab}\times Z_2^F)
+
|G_{\rm ab}\times Z_2^F|=h/2
}
\]

only for

\[
\boxed{
2T\leftrightarrow\widetilde E_6.
}
\]

At that point,

\[
\boxed{
6
=
\sum_{\mathcal R_+}d_\lambda
=
\sum_{\mathcal R_-}d_\lambda
=
|C_6|
=
\frac{h(E_6)}2.
}
\]

Priority and physical interpretation remain explicitly open.
