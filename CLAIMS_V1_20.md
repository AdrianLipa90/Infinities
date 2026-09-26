# Claim ledger v1.20 — Hardy–CAR spectral form factor

This ledger is additive to \`CLAIMS_V1_19.md\`.

| ID | Claim | Status | Validation |
|---|---|---|---|
| INF-273 | The finite cluster factor \(Y_N(s)=[\sin(\pi s)/(N\sin(\pi s/N))]^2\) has exact triangular Fourier coefficients \((N-|k|)/N^2\) before density normalization. | EXACT | finite double-sum/geometric-series identity |
| INF-274 | After the standard unit-density normalization, the finite structure/spectral form factor satisfies \(S_N(k/N)=|k|/N\) for \(|k|<N\) and \(1\) for \(|k|\ge N\). | EXACT | INF-273 |
| INF-275 | The microscopic continuum form factor is \(S(\tau)=\min(|\tau|,1)\). | EXACT LIMIT | INF-274 |
| INF-276 | The linear ramp and unit plateau are forced by the same Hardy–CAR projector sector that forces the sinc-square pair law; GUE/zeta data are not derivation inputs. | DERIVED_IN_FRAMEWORK / FORCED_PREDICTION | no-target-leakage theorem + validator |
| INF-277 | Actual zeta zeros are proved here to realize the full forced ramp/plateau process. | OPEN / NOT ESTABLISHED | requires zeta occupancy/projector binding |

## Dual forced law

\[
\boxed{
g_2(s)
=
1-\left(\frac{\sin\pi s}{\pi s}\right)^2
\quad\Longleftrightarrow\quad
S(\tau)=\min(|\tau|,1)
}
\]

within the declared consecutive-projector + filled-CAR sector.
