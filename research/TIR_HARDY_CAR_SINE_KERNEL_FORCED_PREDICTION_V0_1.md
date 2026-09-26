# TIR Hardy–CAR Sine-Kernel Forced Prediction v0.1

Status: **EXACT_IN_DECLARED_HARDY_CAR_SECTOR / FORCED_PREDICTION / EXTERNAL_ZETA_BINDING_OPEN**

Date: 2026-09-26

Parents:
- Euler-Hilbert-Hotel Supersymmetry v0.2 and later Toeplitz/Fredholm refinements.
- Equivariant minimal Naimark dilation and CAR carrier.
- Canonical Hilbert-Hotel unilateral shift on Hardy space.

## 1. Scope

This theorem asks a narrow question:

> Once the declared Hardy/Toeplitz Hilbert-Hotel shift and the declared CAR/Fock carrier are fixed, what two-point spacing law is forced by the canonical finite orbit projector after unit-density microscopic unfolding?

The derivation below does **not** assume:
- GUE;
- random matrices;
- Montgomery's pair-correlation formula;
- a zeta-zero list;
- prime data.

The GUE/Montgomery identification is made only after the internal derivation is complete.

## 2. Hardy/Hilbert-Hotel carrier

Let

\[
\mathcal H=H^2(S^1)
\]

with orthonormal monomial basis

\[
e_n(\theta)=\frac{e^{in\theta}}{\sqrt{2\pi}},
\qquad n=0,1,2,\ldots
\]

and unilateral shift

\[
Se_n=e_{n+1}.
\]

For \(N\ge1\), define the canonical finite orbit subspace

\[
\mathcal H_N
=
\operatorname{span}\{e_0,Se_0,\ldots,S^{N-1}e_0\}
=
\operatorname{span}\{e_0,\ldots,e_{N-1}\}.
\]

Let \(P_N\) be its orthogonal projector.

No random-matrix ensemble is used here. \(P_N\) is the finite projector onto the first \(N\) states of the declared Hilbert-Hotel shift orbit.

## 3. Exact finite projection kernel

The integral kernel of \(P_N\) is

\[
K_N(\theta,\phi)
=
\sum_{n=0}^{N-1}
e_n(\theta)\overline{e_n(\phi)}
=
\frac1{2\pi}
\sum_{n=0}^{N-1}
e^{in(\theta-\phi)}.
\]

Writing \(\delta=\theta-\phi\), the finite geometric series gives

\[
\boxed{
K_N(\theta,\phi)
=
\frac{e^{i(N-1)\delta/2}}{2\pi}
\frac{\sin(N\delta/2)}{\sin(\delta/2)}.
}
\]

On the diagonal,

\[
\boxed{
\rho_N:=K_N(\theta,\theta)=\frac{N}{2\pi}.
}
\]

Thus the one-point density is constant.

## 4. CAR/Fock lift

Use the declared fermionic second-quantization functor and form the filled \(N\)-mode Slater state

\[
\Omega_N
=
e_0\wedge e_1\wedge\cdots\wedge e_{N-1}
\in
\Lambda^N\mathcal H.
\]

Its one-particle density operator is exactly \(P_N\).

For a Slater/quasi-free CAR state, Wick factorization gives the two-point density

\[
\rho_{2,N}(\theta,\phi)
=
\det
\begin{pmatrix}
K_N(\theta,\theta)&K_N(\theta,\phi)\\
K_N(\phi,\theta)&K_N(\phi,\phi)
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\rho_{2,N}(\theta,\phi)
=
\rho_N^2-|K_N(\theta,\phi)|^2.
}
\]

At coincidence,

\[
\rho_{2,N}(\theta,\theta)=0,
\]

so quadratic short-range exclusion is already forced by the CAR determinant rather than fitted to an external spacing law.

## 5. Unit-density microscopic unfolding

Define the unfolded separation

\[
s
=
\rho_N(\theta-\phi)
=
\frac{N}{2\pi}\delta.
\]

Hence

\[
\delta=\frac{2\pi s}{N}.
\]

Normalize the pair density by \(\rho_N^2\):

\[
g_{2,N}(s)
=
\frac{\rho_{2,N}}{\rho_N^2}
=
1-
\left|
\frac{K_N(\theta,\phi)}{\rho_N}
\right|^2.
\]

Using the exact finite kernel,

\[
\frac{|K_N|}{\rho_N}
=
\left|
\frac{\sin(\pi s)}
{N\sin(\pi s/N)}
\right|.
\]

Therefore the declared framework forces the exact finite-\(N\) law

\[
\boxed{
g_{2,N}(s)
=
1-
\left[
\frac{\sin(\pi s)}
{N\sin(\pi s/N)}
\right]^2.
}
\]

This is obtained before any GUE or zeta comparison.

## 6. Hilbert-Hotel / continuum limit

For fixed \(s\),

\[
N\sin(\pi s/N)\to\pi s.
\]

Therefore

\[
\boxed{
g_2(s)
=
\lim_{N\to\infty}g_{2,N}(s)
=
1-
\left(
\frac{\sin\pi s}{\pi s}
\right)^2.
}
\]

Equivalently, the normalized one-particle kernel converges, up to an irrelevant gauge phase, to

\[
\boxed{
K_{\infty}(s)
=
\frac{\sin\pi s}{\pi s}.
}
\]

Thus the sine kernel is not inserted as a reference function. It is the microscopic limit of the canonical finite projector on consecutive Hardy/Hilbert-Hotel shift modes.

## 7. Phase-coordinate form

Let

\[
\Delta\Phi=2\pi s.
\]

Then

\[
\boxed{
g_2(\Delta\Phi)
=
1-
\left[
\frac{\sin(\Delta\Phi/2)}
{\Delta\Phi/2}
\right]^2.
}
\]

Near coincidence,

\[
g_2(s)
=
\frac{\pi^2}{3}s^2+O(s^4),
\]

or equivalently

\[
\boxed{
g_2(\Delta\Phi)
=
\frac{(\Delta\Phi)^2}{12}
+
O((\Delta\Phi)^4).
}
\]

The quadratic repulsion exponent is therefore forced by the CAR projector geometry of this sector.

## 8. External identification made only after derivation

The derived limiting law

\[
1-\left(\frac{\sin\pi s}{\pi s}\right)^2
\]

is the standard bulk two-point law of the unit-density sine\(_2\) / GUE process and is the function appearing in the Montgomery pair-correlation conjecture for unfolded zeta zeros.

This external name does not participate in Sections 2–7.

The logical direction is

\[
\boxed{
\text{Hardy shift}
\to
P_N
\to
\text{CAR Slater determinant}
\to
g_{2,N}
\to
\text{sine-kernel law}
}
\]

followed only afterward by

\[
\boxed{
\text{sine-kernel law}
=
\text{GUE/Montgomery target}.
}
\]

## 9. What is and is not forced

### Forced in the declared Hardy–CAR sector

- the finite Dirichlet/Szegő projection kernel;
- constant one-point density \(N/(2\pi)\);
- the determinantal two-point law from the filled CAR state;
- exact coincidence exclusion;
- the finite-\(N\) formula for \(g_{2,N}\);
- the sine-kernel microscopic limit;
- the quadratic small-gap coefficient;
- the phase-coordinate law.

### Still requiring a binding theorem

This theorem alone does **not** establish that:
- Riemann zeros are eigenphases of this particular Hardy/CAR projector;
- chemical spectra instantiate this projector;
- telescope spectra instantiate this projector;
- phase-microscope images instantiate this projector.

Those are domain-binding questions.

For zeta zeros, the remaining bridge is now sharply typed:

\[
\boxed{
\text{zeta-zero spectral process}
\stackrel{?}{\longrightarrow}
\text{canonical Hardy–CAR consecutive-mode projector sector}.
}
\]

If that binding is independently derived, Montgomery–Dyson pair correlation is no longer an additional statistical ansatz inside the framework; it is inherited from the theorem above.

## 10. No-target-leakage receipt

The executable validator:
- constructs \(K_N\) directly from the Hardy shift orbit;
- derives the two-point law through the CAR determinant;
- derives the finite closed form from the geometric series;
- takes the microscopic limit;
- only then reports the external sine-kernel form.

No zero list, GUE matrix, random-matrix sample, prime list, or Montgomery target is an input to the construction.

## 11. Compact theorem

### Theorem — Hardy–CAR sine-kernel forced prediction

Let \(S\) be the unilateral shift on \(H^2(S^1)\), let \(P_N\) project onto the first \(N\) consecutive orbit states of \(S\), and let \(\Omega_N\) be the filled fermionic Slater state on \(\operatorname{Ran}P_N\). Under unit-density microscopic unfolding,

\[
\boxed{
g_{2,N}(s)
=
1-
\left[
\frac{\sin(\pi s)}
{N\sin(\pi s/N)}
\right]^2
}
\]

and

\[
\boxed{
g_2(s)
=
1-
\left(
\frac{\sin\pi s}{\pi s}
\right)^2.
}
\]

Equivalently, for \(\Delta\Phi=2\pi s\),

\[
\boxed{
g_2(\Delta\Phi)
=
1-
\left[
\frac{\sin(\Delta\Phi/2)}
{\Delta\Phi/2}
\right]^2.
}
\]

The conclusion is exact in the declared Hardy–CAR sector. External identification with GUE/Montgomery is a comparison, not an input. Q.E.D.


## 12. Filled-sector uniqueness lemma

The word "filled" does not introduce a continuously tunable state after the projector sector and fermion number have been fixed.

Let \(V_N=\operatorname{Ran}P_N\) with \(\dim V_N=N\). Then

\[
\dim \Lambda^N V_N = 1.
\]

Hence every normalized \(N\)-fermion vector occupying exactly \(V_N\) differs from

\[
\Omega_N=e_0\wedge\cdots\wedge e_{N-1}
\]

only by a global phase. If \(f_j=\sum_k U_{kj}e_k\) is any other orthonormal basis of \(V_N\), then

\[
f_0\wedge\cdots\wedge f_{N-1}
=
\det(U)\,
e_0\wedge\cdots\wedge e_{N-1},
\qquad |\det U|=1.
\]

Therefore all gauge-invariant correlation functions of the filled sector are basis independent and are fixed by \(P_N\).

This removes basis choice or Slater-vector phase as a fitting freedom. The remaining type-level assumption is the declaration that the physical/spectral process occupies the **filled \(N\)-fermion sector** associated with \(P_N\). For the abstract Hardy--CAR theorem that declaration is part of the sector definition. For zeta zeros it remains the separate SOH-MD001B occupancy binding.
