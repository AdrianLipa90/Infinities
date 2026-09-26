# Claim ledger v1.19 — Hardy–CAR sine-kernel forced prediction

This ledger is additive to \`CLAIMS_V1_18.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-263 | The first \(N\) consecutive states of the Hardy unilateral-shift orbit define the projector kernel \(K_N(\theta,\phi)=(2\pi)^{-1}\sum_{n=0}^{N-1}e^{in(\theta-\phi)}\). | EXACT | finite projector identity |
| INF-264 | The geometric sum gives \(K_N=e^{i(N-1)\delta/2}\sin(N\delta/2)/(2\pi\sin(\delta/2))\). | EXACT | algebra + validator |
| INF-265 | The filled CAR/Slater state on \(\operatorname{Ran}P_N\) has two-point density \(\rho_{2,N}=\rho_N^2-|K_N|^2\), with \(\rho_N=N/(2\pi)\). | STANDARD CAR / EXACT IN DECLARED SECTOR | Wick/Slater determinant |
| INF-266 | Under unit-density unfolding \(s=N(\theta-\phi)/(2\pi)\), \(g_{2,N}(s)=1-[\sin(\pi s)/(N\sin(\pi s/N))]^2\). | EXACT | INF-263–265 |
| INF-267 | The microscopic limit is \(g_2(s)=1-[\sin(\pi s)/(\pi s)]^2\). | EXACT LIMIT | elementary sine limit + validator |
| INF-268 | In phase coordinates \(\Delta\Phi=2\pi s\), \(g_2(\Delta\Phi)=1-[\sin(\Delta\Phi/2)/(\Delta\Phi/2)]^2\). | EXACT REPARAMETRIZATION | INF-267 |
| INF-269 | The small-gap law is quadratic: \(g_2(s)=(\pi^2/3)s^2+O(s^4)\), equivalently \(g_2(\Delta\Phi)=(\Delta\Phi)^2/12+O(\Delta\Phi^4)\). | EXACT LOCAL EXPANSION | Taylor expansion + validator |
| INF-270 | The sine-kernel/GUE/Montgomery pair-correlation functional form is a forced prediction of the declared Hardy-shift + finite-projector + filled-CAR sector rather than an input to that derivation. | DERIVED_IN_FRAMEWORK / FORCED_PREDICTION | no-target-leakage theorem + validator |
| INF-271 | Riemann zeros are already proved to instantiate this exact Hardy–CAR consecutive-mode projector process. | OPEN / NOT ESTABLISHED HERE | requires independent zeta-to-projector binding theorem |
| INF-272 | Chemical, telescope, or phase-microscope spectra are automatically governed by this sine-kernel process. | FALSE AS A GENERAL CLAIM / DOMAIN BINDING REQUIRED | independent domain tests required |

## Exact forced-prediction chain

\[
\boxed{
H^2\text{ unilateral shift}
\to
P_N
\to
\Lambda^N\operatorname{Ran}P_N
\to
\det K_N
\to
g_{2,N}
\to
1-\operatorname{sinc}^2
}
\]

No random-matrix or zeta-zero sample appears upstream of the derived law.

| INF-273 | For a rank-\(N\) projector \(P_N\), the filled fermion sector \(\Lambda^N\operatorname{Ran}P_N\) is one-dimensional; its normalized Slater state is unique up to global phase and independent of orthonormal basis up to \(\det U\). | EXACT | Top exterior-power dimension and determinant covariance. |
| INF-274 | Once \(P_N\), CAR statistics and filled \(N\)-particle occupancy are fixed, the two-point determinant contains no further tunable state/basis parameter. | EXACT IN DECLARED SECTOR | INF-273 + CAR/Wick determinant. |
