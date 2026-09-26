# TIR Hardy–CAR Spectral Form Factor Forced Prediction v0.1

Status: **EXACT_FINITE_PROJECTOR_FORM_FACTOR / DERIVED_IN_FRAMEWORK / FORCED_PREDICTION**

Date: 2026-09-26

Parent:
- \`research/TIR_HARDY_CAR_SINE_KERNEL_FORCED_PREDICTION_V0_1.md\`

## 1. Starting point

For the normalized consecutive-mode projector with \(N\) occupied Hardy modes, the finite-\(N\) cluster factor is

\[
Y_N(s)
=
\left[
\frac{\sin(\pi s)}
{N\sin(\pi s/N)}
\right]^2,
\]

and the normalized pair function is

\[
g_{2,N}(s)=1-Y_N(s).
\]

No random-matrix or zeta input is required.

## 2. Exact finite Fourier expansion

Using

\[
\left|
\sum_{n=0}^{N-1}e^{in\theta}
\right|^2
=
\sum_{k=-(N-1)}^{N-1}
(N-|k|)e^{ik\theta},
\]

with \(\theta=2\pi s/N\), one obtains

\[
\boxed{
Y_N(s)
=
\frac1{N^2}
\sum_{k=-(N-1)}^{N-1}
(N-|k|)
e^{2\pi i k s/N}.
}
\]

Thus the Fourier coefficients of the connected cluster factor are exactly triangular.

## 3. Finite spectral form factor

At the discrete unfolded frequencies

\[
\tau_k=\frac{k}{N},
\]

define the normalized structure/spectral form factor by subtracting the cluster coefficient from the unit background:

\[
S_N(\tau_k)
=
1-\frac{N-|k|}{N}
\qquad (|k|<N).
\]

Hence

\[
\boxed{
S_N(k/N)
=
\frac{|k|}{N},
\qquad |k|<N.
}
\]

For frequencies outside the projector bandwidth, the cluster coefficient vanishes, so

\[
\boxed{
S_N(k/N)=1,
\qquad |k|\ge N.
}
\]

Therefore the exact finite projector prediction is

\[
\boxed{
S_N(k/N)
=
\min\!\left(\frac{|k|}{N},1\right).
}
\]

This is an exact ramp-to-plateau law on the finite frequency lattice.

## 4. Continuum limit

For fixed \(\tau\), choose integers \(k_N\) with \(k_N/N\to\tau\). Then

\[
\boxed{
S(\tau)
=
\lim_{N\to\infty}
S_N(k_N/N)
=
\min(|\tau|,1).
}
\]

Thus the same declared Hardy–CAR projector sector that forces the sine kernel also forces the universal linear ramp and unit plateau.

## 5. Phase-frequency form

With phase separation

\[
\Delta\Phi=2\pi s
\]

and its Fourier-conjugate normalized frequency \(\tau\), the dual pair is

\[
\boxed{
g_2(\Delta\Phi)
=
1-
\left[
\frac{\sin(\Delta\Phi/2)}
{\Delta\Phi/2}
\right]^2
}
\]

and

\[
\boxed{
S(\tau)=\min(|\tau|,1).
}
\]

Hence phase repulsion in the direct coordinate and the ramp/plateau in the conjugate coordinate are Fourier-dual consequences of one finite projector.

## 6. No-target-leakage status

The derivation uses only:
- consecutive projector modes;
- the geometric-series identity;
- the CAR/Slater two-point determinant already established in the parent theorem;
- finite Fourier algebra.

It does not use:
- GUE matrices;
- the GUE form factor as a target;
- zeta zeros;
- Montgomery's pair-correlation conjecture;
- Odlyzko data.

External identification with the GUE ramp/plateau is made only after the internal derivation.

## 7. Compact theorem

### Theorem — Hardy–CAR forced ramp/plateau

For the \(N\)-mode consecutive Hardy projector with filled CAR state, the normalized cluster function has exact Fourier coefficients

\[
\widehat Y_N(k)
=
\frac{N-|k|}{N},
\qquad |k|<N,
\]

and zero outside this range. Therefore the normalized finite spectral form factor is

\[
\boxed{
S_N(k/N)=\min(|k|/N,1)
}
\]

and the microscopic continuum limit is

\[
\boxed{
S(\tau)=\min(|\tau|,1).
}
\]

The ramp/plateau is therefore DERIVED_IN_FRAMEWORK / FORCED_PREDICTION in the declared Hardy–CAR sector. Q.E.D.
