# Infinities

A research programme on the mathematical structures of infinity.

`Infinities` does **not** claim a proof of the Riemann Hypothesis, the Collatz conjecture, the Twin Prime conjecture, or any other open problem. Those problems are used here as distinct examples of how infinity appears through cardinality, iteration, spectral analysis, and arithmetic distribution.

## Scope

The project studies several mathematically different forms of infinity inside a common operator language:

- **Cardinal infinity** — Hilbert's Hotel and the fact that a countably infinite whole can be placed in bijection with a proper subset of itself.
- **Iterative infinity** — Collatz-type dynamics, unbounded iteration depth, recurrence, stopping times, and orbit structure.
- **Spectral / analytic infinity** — Dirichlet series, the Riemann zeta function, analytic continuation, and spectral weighting of the natural numbers.
- **Distributional infinity** — primes, twin primes, sparse infinite subsets, counting functions, and asymptotic structure.

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

## Status

Initial operator framework established. Formal derivations, validators, and typed claim ledgers will be added incrementally.
