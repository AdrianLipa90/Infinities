# Claim ledger v1.5 — TIR/SIC/Naimark/CAR supersymmetry bridge

This ledger is additive to `CLAIMS_V1_4.md`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-095 | The tetrahedral qubit SIC effects satisfy (E_a=(I+n_a\cdot\sigma)/4), and the corresponding future-null Hermitian rays obey (K_a=I+n_a\cdot\sigma=4E_a) | STANDARD SIC + EXACT NORMALIZATION | analytic proof + finite validator |
| INF-096 | The rank-one tetrahedral SIC defines an isometric analysis map (V:\mathbb C^2\to\mathbb C^4) with (E_a=V^\dagger\Pi_aV) | STANDARD NAIMARK CONSTRUCTION / EXACT | analytic proof + finite validator |
| INF-097 | The four-outcome Naimark dilation is minimal; its unitary-equivalence class is fixed by the labeled SIC, with spinor phase changes acting by diagonal outcome unitaries | STANDARD MINIMAL-DILATION UNIQUENESS + EXACT SPECIALIZATION | analytic proof |
| INF-098 | The binary tetrahedral spin action induces a monomial (R:2T\to U(4)) on the minimal outcome carrier satisfying (V\rho(g)=R(g)V) | EXACT EQUIVARIANT DILATION | finite 24-element group validator |
| INF-099 | Fermionic second quantization of the conjugate outcome representation yields four canonical CAR modes up to Naimark unitary equivalence | STANDARD FOCK/CAR FUNCTOR + EXACT SPECIALIZATION | finite CAR validator |
| INF-100 | The central element (-I_2\in2T) maps to (-I_4) on the outcome carrier and to fermion parity ((-1)^F) on (Lambda^\bullet\mathbb C^4) | EXACT | finite group/Fock validator |
| INF-101 | (Q_\alpha=\sqrt2\sum_a\sqrt{p_a}\lambda_{a,\alpha}f_a^\dagger) is odd under fermion parity and closes as ({Q_\alpha,\bar Q_{\dot\beta}\}=2\sum_ap_a\lambda_{a,\alpha}\bar\lambda_{a,\dot\beta}) | EXACT AFTER STANDARD FERMIONIC SECOND QUANTIZATION | finite CAR validator |
| INF-102 | At equal tetrahedral weights the combined spin/Fock (2T) action leaves the supercharge invariant | EXACT | 24-element covariance validator |
| INF-103 | The TIR primitive N/S carrier is automatically identical to the auxiliary Fredholm-SUSY grading | NOT PROVED / REQUIRES TYPED IDENTIFICATION | proof firewall |
| INF-104 | A TIR Poincare disk uniquely forces Hardy-space quantization (H^2(\mathbb D)) | FALSE AS STATED / QUANTIZATION CHOICE REQUIRED | proof firewall |
| INF-105 | The center-to-parity theorem is the physical spin-statistics theorem | NOT CLAIMED | physical/QFT theorem boundary |
| INF-106 | Tetrahedral geometry alone physically derives Standard-Model fermions | OPEN / NOT CLAIMED | physical sector-binding required |

## Core v1.5 statement

The exact new structural package is

[
\boxed{
\text{tetrahedral SIC}
\to
\text{minimal equivariant Naimark carrier}
\to
\text{fermionic Fock/CAR}
}
]

with

[
\boxed{
-I_{\rm spinor}\mapsto(-1)^F.
}
]

The standard ingredients are Naimark dilation, fermionic second quantization, and binary-tetrahedral spin symmetry. The present contribution is their explicit equivariant synthesis on the TIR tetrahedral SIC carrier and the resulting supercharge construction. No physical supersymmetry or component-theorem novelty is claimed.
