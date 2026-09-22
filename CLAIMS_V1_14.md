# Claim ledger v1.14 — C6-refined supersymmetry grading and IDT crosswalk

This ledger is additive to \`CLAIMS_V1_13.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-199 | The conserved internal \(C_3\) generator \(\mathcal Z\) and fermion parity \(\mathcal P_F=(-1)^F\) commute and combine as \(\mathcal G_6=\mathcal Z\mathcal P_F\) with \(\mathcal G_6^6=I\) | EXACT | group arithmetic + finite validator |
| INF-200 | \(\mathcal G_6^3=\mathcal P_F\), \(\mathcal G_6^4=\mathcal Z\), and \(\mathcal G_6^2=\mathcal Z^2\); hence the \(C_6\) generator recovers both original gradings | EXACT | finite group identity |
| INF-201 | The 48-dimensional compensated carrier splits into six \(C_6\) eigensectors of equal dimension 8, equivalently \(8\) copies of the regular \(C_6\) representation | EXACT | exhaustive 48-state charge count |
| INF-202 | The charge dictionary is \(q=2r+3f\pmod6\), with inverse \(f=q\pmod2\), \(r=2q\pmod3\) | EXACT CRT ISOMORPHISM | exhaustive validator |
| INF-203 | The three 16-state massive \(N=2\) long-multiplet sectors refine as \(\mathcal M_0=\mathcal H_0\oplus\mathcal H_3\), \(\mathcal M_1=\mathcal H_2\oplus\mathcal H_5\), \(\mathcal M_2=\mathcal H_4\oplus\mathcal H_1\) | EXACT | INF-201/202 |
| INF-204 | Every compensated supercharge commutes with \(\mathcal Z\), anticommutes with \((-1)^F\), and therefore has \(C_6\) degree \(3\): \(Q:\mathcal H_q\to\mathcal H_{q+3}\) | EXACT | CAR/compensation theorem + exhaustive transition validator |
| INF-205 | The existing IDT six-state generator \(G_T=P_T\otimes J_\chi\) and the SUSY generator \(\mathcal G_6=\mathcal Z(-1)^F\) realize the same abstract \(C_3\times Z_2\cong C_6\) extension algebra, with cube equal to the \(Z_2\) factor and fourth power equal to the \(C_3\) factor | EXACT REPRESENTATION CROSSWALK | TIR-IDT crosswalk + present group identities |
| INF-206 | The Pauli lift \(U_3^3=-I\), \(U_3^6=I\) is compatible with the SIC/Naimark/Fock center map \(-I\mapsto(-1)^F\), yielding the same order-six central-extension pattern | EXACT REPRESENTATION-THEORETIC COMPATIBILITY | existing TIR Pauli crosswalk + v0.4 center theorem |
| INF-207 | The affine-\(\widetilde E_6\) graph-incidence complex refines into degree-three \(C_6\) channels \(0\to3\), \(2\to5\), and \(4\to1\) | EXACT | C3 Fourier decomposition + charge dictionary |
| INF-208 | The graph-incidence index \(+1\) is carried only by the neutral \(q=0\to3\) channel; the protected graph zero mode has \(C_6\) charge \(0\) | EXACT | graph block decomposition + validator |
| INF-209 | The \(C_6\)-refined grading is a new physical six-fold supersymmetry algebra | FALSE / NOT CLAIMED | it is a refinement of the ordinary \(Z_2\) grading |
| INF-210 | The IDT temporal \(C_3\) is physically identical to the internal SUSY \(C_3\), or Stage-23 chirality is physically identical to fermion parity | OPEN / NOT CLAIMED | physical sector-binding theorem required |
| INF-211 | The numerical IDT \(6\pi\) phase budget is identified with a physical spin-rotation period | FALSE / NOT CLAIMED | representation crosswalk only |
| INF-212 | The C6-refined SIC/Naimark/Fock/IDT crosswalk is literature-first | CANDIDATE ONLY / PRIORITY AUDIT REQUIRED | dedicated novelty search required |

## v1.14 core

The previously separate \(C_3\) and fermion-parity labels combine into one exact cyclic grading:

\[
\boxed{
\mathcal G_6=\mathcal Z(-1)^F,
\qquad
\mathcal G_6^3=(-1)^F,
\qquad
\mathcal G_6^4=\mathcal Z.
}
\]

The 48-state carrier becomes six eight-dimensional sectors, and every compensated supercharge has degree \(3\) modulo \(6\). This gives an exact representation-level crosswalk to the pre-existing IDT \(C_3\times Z_2\cong C_6\) six-state carrier while keeping temporal/internal and chirality/fermion-parity physical identifications explicitly open.
