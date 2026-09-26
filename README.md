# Infinities

A research programme on the mathematical structures of infinity.

**Release status:** `v1.0.0` finite research-programme freeze. See `INFINITIES_V1_0.md` and `CLAIMS.md` for the exact theorem, falsification, boundary, and open-claim ledger.

`Infinities` does **not** claim a proof of the Riemann Hypothesis, the Collatz conjecture, the Twin Prime conjecture, or any other open problem. Those problems are used here as distinct examples of how infinity appears through cardinality, iteration, spectral analysis, and arithmetic distribution.

## Scope

The project studies several mathematically different forms of infinity inside a common operator language:

- **Cardinal infinity** — Hilbert's Hotel and the fact that a countably infinite whole can be placed in bijection with a proper subset of itself.
- **Iterative infinity** — Collatz-type dynamics, unbounded iteration depth, recurrence, stopping times, and orbit structure.
- **Spectral / analytic infinity** — Dirichlet series, the Riemann zeta function, analytic continuation, and spectral weighting of the natural numbers.
- **Distributional infinity** — primes, twin primes, sparse infinite subsets, counting functions, and asymptotic structure.
- **Phase-recursive / branch infinity** — complex phase iteration, repelling fixed points, multi-branch inverses, and symbolic preimage trees, introduced by **Euler's Infinity**.

The objective is comparison and structural unification, not reduction of all of these questions to one theorem.

## Common carrier

A natural common carrier is

\[
\mathcal H=\ell^2(\mathbb N),
\]

with canonical basis \(|n\rangle\), \(n\ge 1\).

Define the number operator

\[
N|n\rangle=n|n\rangle,
\]

and the unilateral shift

\[
S|n\rangle=|n+1\rangle.
\]

Then

\[
S^\dagger S=I,
\qquad
SS^\dagger=I-|1\rangle\langle1|.
\]

This is the operator form of the Hilbert-Hotel phenomenon: the whole countable basis is isometrically embedded into a proper part of itself, with a rank-one defect.

The same number operator gives, for \(\Re(s)>1\),

\[
\zeta(s)=\operatorname{Tr}(N^{-s})
=\sum_{n=1}^{\infty}n^{-s}.
\]

Thus cardinal and analytic infinity can already be represented on the same Hilbert-space carrier without identifying them as the same mathematical object.

## Iterative sector

For a Collatz-type map \(T:\mathbb N\to\mathbb N\), define the induced basis operator

\[
C|n\rangle=|T(n)\rangle.
\]

The purpose of this operator is to encode orbit structure, branching, recurrence, and information loss or retention under iteration. Its presence in this framework is **not** a claim that the Collatz conjecture has been proved.

A reversible or isometric extension may retain branch history in an enlarged countable state space. Hilbert-Hotel structure is therefore relevant as a model of countable state allocation for iterative histories.

## Prime-distribution sector

Let \(P\) be the spectral projector of \(N\) onto prime-labelled basis states:

\[
P|n\rangle=
\begin{cases}
|n\rangle,& n\text{ prime},\\
0,&\text{otherwise}.
\end{cases}
\]

A twin-prime selector can then be written using the shift,

\[
Q_2=P\,S^{\dagger 2}P S^2P.
\]

On a prime basis vector,

\[
Q_2|p\rangle=
\begin{cases}
|p\rangle,& p\text{ and }p+2\text{ are prime},\\
0,&\text{otherwise}.
\end{cases}
\]

This rewrites the distributional question in operator language; it does not settle whether \(Q_2\) has infinite rank.

## Nonconformal inversion

A central geometric comparison map in this project is the anti-holomorphic inversion

\[
\boxed{\mathcal J(z)=\frac{1}{\overline z}}.
\]

For the Möbius coordinate

\[
z=\frac{s}{1-s},
\]

the reflection

\[
s\mapsto 1-\overline s
\]

becomes exactly

\[
z\mapsto\frac1{\overline z}.
\]

Moreover,

\[
\Re(s)=\frac12
\iff
|z|=1.
\]

The unit circle is therefore the fixed locus of this nonconformal inversion. In `Infinities`, this map is used as a geometric comparison tool between reciprocal sectors; it is **not** presented as a proof mechanism for the Riemann Hypothesis.

## Euler's Infinity — phase-recursive branch infinity

Define the Euler phase map

\[
\mathcal E(z)=e^{i\pi z}.
\]

The post-v1.0 research extension **Euler's Infinity** selects the exact fixed-point branch

\[
\boxed{\mathfrak E_\infty=-1},
\qquad
\mathcal E(-1)=-1.
\]

Its algebraic square-root fibre is

\[
\boxed{\sqrt{\mathfrak E_\infty}=\{+i,-i\}},
\]

and the fixed point is repelling under ordinary forward iteration because

\[
\mathcal E'(-1)=-i\pi,
\qquad
|\mathcal E'(-1)|=\pi>1.
\]

On a declared logarithm branch, the inverse family is

\[
\boxed{
\mathcal E_k^{-1}(w)=2k-\frac{i}{\pi}\Log w,
\qquad k\in\mathbb Z.
}
\]

Finite inverse compositions therefore form a countably branching preimage tree. Infinite-address convergence and any specific fractal-dimension claim remain **OPEN / NOT CLAIMED**.

The full definition, Lambert-\(W\) fixed-point representation, branch firewall, and finite regression witness are in `research/EULERS_INFINITY_V0_1.md` and `validate_eulers_infinity_v0_1.py`.

## Research principle

The project asks whether apparently different infinities can be compared through a shared collection of structures such as

\[
\{N,S,C,P,\mathcal J\},
\]

while preserving the distinctions between their mathematical roles.

The intended objects of study include:

- shift defect and countable self-embedding;
- orbit depth, recurrence, and branching;
- weighted traces and spectral regularisation;
- sparse-projector rank and arithmetic distribution;
- reciprocal and anti-holomorphic symmetries;
- fixed sets, boundaries, and invariant sectors.

## Epistemic policy

Every result in this repository should be typed explicitly as one of:

`DEFINITION`, `EXACT`, `STANDARD_THEOREM`, `NUMERICAL_WITNESS`, `CONDITIONAL`, `CONJECTURAL`, `OPEN`, or `FAIL`.

Repository presence is not evidence of truth. Open problems remain open unless a complete proof is independently checkable and survives dedicated verification.

## v1.0 finite operator programme

The first finite operator programme is frozen at `v1.0.0`. Its strongest scoped results are:

- exact `BRANCH -> MAP -> FOLD` factorization for the defined finite-kernel class;
- exact finite word-polynomial and multilinear `BRANCH -> MAP -> COUPLE -> FOLD` factorization;
- exact polynomial obstruction `omega_C(P)=ceil(log2 deg(P))` for minimal binary-COUPLE depth in the defined polynomial grammar;
- exact boundaries showing that reciprocal, piecewise/gated, fixed-point, quotient, and selection structure cannot be collapsed into that degree invariant without changing the type of the problem;
- preserved negative controls and falsified overpromotions rather than rewritten success labels.

The freeze deliberately does **not** establish a universal minimal operator grammar or a single universal fourth mathematical operator.

## Post-freeze additive research: Euler-Hilbert-Hotel supersymmetry

The programme is now at v0.3 and is split into independent theorem modules.

The operator module is summarized in `research/EULER_HILBERT_HOTEL_SUPERSYMMETRY_V0_3.md`. Its central classification is

[
pi_0(mathrm{Fred}(H))
cong
mathbb Z,
qquad
[A]mapsto
Delta_W(A)=operatorname{ind}(A),
]

with explicit Hilbert-Hotel normal representatives built from the unilateral shift and its adjoint.

For scalar Toeplitz symbols,

[
Delta_W(T_f)
=
-operatorname{wind}(f),
]

and the Toeplitz extension identifies this integer as the K-theory boundary image of the Euler boundary-phase class. Finite Blaschke products give an explicit protected zero-mode space `K_B=H^2 minus B H^2`, not merely an index count; normalized zero modes inherit the pseudohyperbolic geometry of their analytic zero locations.

The tetrahedral module remains independent. Its equal-weight N=1 supertranslation frame has an exact timelike rest axis fixed by the tetrahedral rotational symmetry, with the binary tetrahedral group acting through the spin lift after explicit CAR input.

The LaTeX paper is `papers/euler_hilbert_hotel_supersymmetry.tex`. Scoped claims are in `CLAIMS_V1_2.md` through `CLAIMS_V1_4.md`.

## Status

**v1.0.0 — finite research-programme freeze.** The first programme is closed as an auditable collection of scoped theorems, counterexamples, finite classifications, typed boundaries, and explicit open questions. `v1.0 COMPLETE` refers to that repository scope only; it does not mean that all mathematical infinities or the open problems named above are solved.

## Post-freeze additive research: Skewes–Euler–Hilbert–Collatz bridge

The module [research/SKEWES_EULER_HILBERT_COLLATZ_BRIDGE_V0_1.md](research/SKEWES_EULER_HILBERT_COLLATZ_BRIDGE_V0_1.md) adds an exact operator bridge between prime infinitude, Hilbert-Hotel self-embedding, Littlewood–Skewes sign reversal, zeta log-phases, and accelerated odd-Collatz reverse fibres. The local algebraic checks are in `validation/validate_skewes_euler_hilbert_collatz_bridge_v0_1.py`.

Its strongest exact statement is a shared dyadic affine/log-phase carrier with phase increments (gammalog2) and (2gammalog2). No open-problem proof is claimed.


## Post-freeze additive research: spectral von Mangoldt phase bank

The common infinity/operator programme now includes:

- [research/SPECTRAL_VON_MANGOLDT_PHASE_BANK_V0_1.md](research/SPECTRAL_VON_MANGOLDT_PHASE_BANK_V0_1.md)
- [research/SPECTRAL_SHIFTED_VON_MANGOLDT_CLOSURE_V0_1.md](research/SPECTRAL_SHIFTED_VON_MANGOLDT_CLOSURE_V0_1.md)
- [computations/phase_bank_von_mangoldt_v0_1.py](computations/phase_bank_von_mangoldt_v0_1.py)

This extension makes the shared dyadic clock precise through Landau's zero-spectral reconstruction of von Mangoldt prime-power weights. It remains additive to the frozen v1.0 programme and does not promote any open problem to solved status.
