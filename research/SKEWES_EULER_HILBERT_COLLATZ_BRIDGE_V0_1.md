# Skewes–Euler–Hilbert–Collatz Bridge v0.1

Status: \`POST-V1.0 ADDITIVE MODULE / EXACT OPERATOR BRIDGE + STANDARD NUMBER-THEORY INPUT + OPEN SPECTRAL TESTS\`

This module links four infinity sectors already present in **Infinities** without collapsing them into one theorem:

- cardinal infinity: Hilbert-Hotel self-embedding;
- distributional infinity: infinitely many primes and the Littlewood–Skewes sign-reversal phenomenon;
- analytic/spectral infinity: zeta-zero phases in logarithmic scale;
- iterative infinity: accelerated odd Collatz and its inverse fibres.

The bridge is an exact dyadic affine/log-phase structure. No open problem is promoted to solved status.

## 1. Affine dilation as a shared normal form

For

\[
F_{q,c}(x)=qx+(q-1)c
\]

and \(h_c(x)=x+c\),

\[
h_c\circ F_{q,c}\circ h_c^{-1}(y)=qy.
\]

Thus every such affine map is conjugate to a pure dilation. Its fixed point is \(-c\).

Two sectors of interest are

\[
T(x)=2x+1=F_{2,1}
\]

and

\[
R(x)=4x+1=F_{4,1/3}.
\]

Their exact logarithmic coordinates are

\[
\tau_P(x)=\log(x+1),
\qquad
\tau_C(x)=\log\left(x+\frac13\right),
\]

with

\[
\Delta\tau_P=\log2,
\qquad
\Delta\tau_C=\log4=2\log2.
\]

Hence both live on one dyadic log-clock.

## 2. Euler prime infinity -> Hilbert-Hotel isometry

Let \(p_n\) denote the \(n\)-th prime and let

\[
\mathcal H=\ell^2(\mathbb N).
\]

Prime infinitude implies that the prime set is countably infinite. Define

\[
V_{\mathbb P}|n\rangle=|p_n\rangle.
\]

For the prime projector \(P\),

\[
V_{\mathbb P}^\dagger V_{\mathbb P}=I,
\qquad
V_{\mathbb P}V_{\mathbb P}^\dagger=P.
\]

This is a precise cardinal-infinity bridge: the entire countable basis is isometrically embedded into the proper prime-labelled subspace.

It is analogous to, but not identical with, the unilateral Hilbert-Hotel shift. The defect \(I-P\) is not rank one.

## 3. Skewes sign reversal as an analytic infinity observable

Define

\[
\Delta(x)=\pi(x)-\operatorname{li}(x).
\]

Littlewood's theorem states that \(\Delta(x)\) changes sign infinitely often. Skewes' historical bounds concern where the first positive region must occur; they do not alter the theorem that both signs recur arbitrarily far out.

The prime-counting error is linked through the standard explicit-formula machinery to the nontrivial zeros

\[
\rho=\beta+i\gamma
\]

of \(\zeta(s)\). Each spectral factor has the exact form

\[
x^\rho
=
e^{\beta\log x}e^{i\gamma\log x}.
\]

Therefore in log-coordinate \(t=\log x\), each zero ordinate \(\gamma\) is an angular frequency.

This is the analytic/spectral infinity sector.

## 4. Euler sign phase

For \(\Delta(x)\neq0\), define

\[
\theta_\Delta(x)=
\begin{cases}
0,&\Delta(x)>0,\\
\pi,&\Delta(x)<0.
\end{cases}
\]

Then

\[
\operatorname{sgn}\Delta(x)=e^{i\theta_\Delta(x)}.
\]

A sign reversal is represented by a \(\pi\)-phase flip.

This is a representation theorem only. Euler's identity \(e^{i\pi}=-1\) does not by itself prove Littlewood's theorem or locate a Skewes crossing.

## 5. Dyadic sampling of zeta-zero phases

For a prime \(p\), use the On-Primes address

\[
p+1=a_p2^{k_p},
\qquad
\delta_p=\log\left(1+\frac1p\right).
\]

Then

\[
\log p
=
\log a_p+k_p\log2-\delta_p
\]

and therefore

\[
e^{i\gamma\log p}
=
e^{i\gamma\log a_p}
e^{ik_p\gamma\log2}
e^{-i\gamma\delta_p}.
\]

Define

\[
\boxed{\omega_\gamma=\gamma\log2\pmod{2\pi}}.
\]

The zero phase advances by one \(\omega_\gamma\) per dyadic fibre step.

## 6. Hilbert-Hotel shift -> Weyl phase algebra

On \(\ell^2(\mathbb N_0)\), let

\[
S|k\rangle=|k+1\rangle,
\qquad
D_\omega|k\rangle=e^{ik\omega}|k\rangle.
\]

Then

\[
\boxed{
D_\omega S=e^{i\omega}S D_\omega.
}
\]

Thus the countable shift and the phase mode form an exact Weyl pair.

For \(\omega=\gamma\log2\), the Hilbert-Hotel index shift becomes the operator carrier of the dyadic zeta phase progression.

This is an exact operator identity; it does not imply a new theorem about zeta zeros.

## 7. Collatz reverse fibres are themselves Hilbert-Hotel fibres

For odd \(n\), define

\[
U(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}.
\]

Fix odd \(m\).

If \(3\mid m\), no odd one-step predecessor exists.

If \(3\nmid m\), the complete odd reverse fibre is

\[
U^{-1}(m)\cap(2\mathbb Z+1)
=
\left\{
\frac{2^a m-1}{3}:
a\ge1,\;
2^a m\equiv1\pmod3
\right\}.
\]

The admissible \(a\)'s have one fixed parity:

\[
m\equiv1\pmod3 \Rightarrow a=2,4,6,\ldots,
\]

\[
m\equiv2\pmod3 \Rightarrow a=1,3,5,\ldots.
\]

Therefore every odd \(m\) not divisible by \(3\) has countably infinitely many odd one-step predecessors.

If

\[
B_a(m)=\frac{2^a m-1}{3},
\]

then

\[
\boxed{
B_{a+2}(m)=4B_a(m)+1.
}
\]

Hence each reverse fibre is a Hilbert-Hotel sequence indexed by \(j\in\mathbb N_0\), with index shift implemented arithmetically by \(R(x)=4x+1\).

In the shifted coordinate

\[
x+\frac13,
\]

this becomes pure multiplication by \(4\).

## 8. Shared phase clock

The exact phase increment of a mode \(e^{i\gamma\tau}\) is

\[
\omega_\gamma=\gamma\log2
\]

for one On-Primes dyadic step and

\[
2\omega_\gamma
\]

for one same-target Collatz reverse-fibre step.

Thus:

\[
\text{Hilbert index shift}
\leftrightarrow
\log2\text{ translation}
\leftrightarrow
\omega_\gamma\text{ phase rotation},
\]

while the Collatz reverse fibre selects the doubled step.

This is the common structure added by this module.

## 9. Typed claim ledger

| ID | Statement | Status |
|---|---|---|
| INF-X001 | \(F_{q,c}\) is conjugate to multiplication by \(q\). | EXACT |
| INF-X002 | Prime infinitude yields an isometry \(\ell^2(\mathbb N)\to P\mathcal H\). | STANDARD_THEOREM + EXACT CONSTRUCTION |
| INF-X003 | \(\pi(x)-\operatorname{li}(x)\) changes sign infinitely often. | STANDARD_THEOREM |
| INF-X004 | A zero factor \(x^{\beta+i\gamma}\) carries phase \(e^{i\gamma\log x}\). | EXACT |
| INF-X005 | Dyadic prime addressing gives phase step \(\omega_\gamma=\gamma\log2\). | EXACT |
| INF-X006 | \(D_\omega S=e^{i\omega}SD_\omega\). | EXACT |
| INF-X007 | Odd accelerated-Collatz reverse fibres are empty for \(3\mid m\), otherwise countably infinite with step \(4x+1\). | EXACT |
| INF-X008 | The Collatz reverse log-step is \(2\log2\). | EXACT |
| INF-X009 | Skewes sign can be encoded by phase \(0/\pi\). | DEFINITION |
| INF-O001 | The distribution of \(\omega_\gamma\) may carry a useful dyadic spectral statistic. | OPEN |
| INF-O002 | Prime-mask and Collatz-reverse observables may share or fail to share phase coherence under \(\omega_\gamma\mapsto2\omega_\gamma\). | OPEN |

## 10. Research programme

The immediate finite programme is:

1. ingest verified zero ordinates \(\gamma_j\);
2. compute \(\omega_j=\gamma_j\log2\bmod2\pi\);
3. test phase uniformity and pair-correlation diagnostics;
4. sample the same modes on On-Primes dyadic fibres;
5. sample doubled phases on exact Collatz reverse fibres;
6. preregister null models before interpreting any apparent coherence;
7. keep Skewes/Littlewood analysis on a continuation-safe explicit-formula path.

A positive finite correlation is not a theorem. A null result is informative and must be retained.

## 11. Boundary

This module establishes a shared operator/coordinate structure only. It does not establish:

- the Riemann Hypothesis;
- the Collatz conjecture;
- the Twin Prime conjecture;
- a formula for the first Skewes crossing;
- a dynamical equivalence between Collatz and prime distribution;
- a new zero-spacing law.

The new exact statement is narrower:

\[
\boxed{
\text{countable shift}
+
\text{dyadic affine dilation}
+
\text{log-phase rotation}
}
\]

form one common mathematical carrier across these sectors.
