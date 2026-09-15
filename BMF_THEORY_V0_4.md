# BMF Operator Factorization — v0.4

Status: **RESEARCH PROGRAMME / EXACT FINITE KERNEL FACTORIZATION / OOD NUMERICAL WITNESSES**

This file records the operator reduction reached after the v0.1 GREMLIN sweep. It does **not** claim a universal classification theorem for all mathematics of infinity.

## Typed primitive grammar

The normalized candidate grammar uses three typed operations:

- `MAP` (`M`): local transformation of an already existing channel.
- `BRANCH` (`B`): create an indexed family of channels.
- `FOLD` (`F`): aggregate an indexed family under a specified operation and completion/convergence rule.

For a finite kernel operator over a semiring-like carrier,

\[
(T_K f)(y)=\bigoplus_{x\in X}K(y,x)\otimes f(x),
\]

there is an exact factorization

\[
T_K = F_{\oplus}\circ M_K\circ B,
\]

with

\[
(Bf)(y,x)=f(x),
\qquad
(M_K Bf)(y,x)=K(y,x)\otimes f(x),
\]

and

\[
(F_{\oplus}M_KBf)(y)
=
\bigoplus_x K(y,x)\otimes f(x).
\]

The executable implementation is `infinities/bmf.py`.

For infinite index sets this formula is only meaningful after the caller specifies the required topology, valuation, completion, measure, or convergence mode. The code deliberately does not silently promote a finite fold into an infinite one.

## OOD witnesses

`computations/bmf_ood_v0_4.py` checks finite witnesses outside the original 32-case catalogue:

- discrete Fourier transform,
- finite Markov transition,
- Boolean graph adjacency,
- divisibility-poset zeta transform,
- Walsh–Hadamard transform,
- Dirichlet convolution,
- tensor contraction / matrix multiplication.

These are tests of the BMF factorization pattern, not evidence that every construction in infinity mathematics is BMF-reducible.

## Symmetry obstruction to canonical selection

The three operators are intentionally canonical/structural. A separate issue arises when a construction must choose one distinguished witness from a completely symmetric family.

Let `S(A) in A` be a selector required to be equivariant under every permutation of a bare finite set `A`. For a two-element set \(A=\{a,b\}\), the swap \(\sigma(a)=b,\sigma(b)=a\) gives

\[
S(A)=S(\sigma A)=\sigma S(A),
\]

but the swap has no fixed point. Hence no such canonical selector exists.

`equivariant_distinguished_elements()` checks the finite full-permutation obstruction for sizes 2–5. Supplying extra structure, e.g. an order, permits a selector such as `min`; therefore this obstruction identifies missing symmetry-breaking structure rather than proving a universal fourth infinity generator.

## Epistemic firewall

Allowed labels:

- `EXACT`: finite kernel factorization by construction.
- `NUMERICAL_WITNESS`: finite numerical checks of DFT/Markov/Walsh/tensor cases.
- `FINITE_OBSTRUCTION`: finite permutation-equivariance selector obstruction.
- `OPEN`: universality/minimality beyond the explicit typed class.

Forbidden promotions:

- finite OOD coverage -> universal classification of infinity,
- BMF factorization -> proof of the Riemann Hypothesis,
- BMF factorization -> proof of the Collatz conjecture,
- finite selector obstruction -> theorem that every use of Choice requires a new primitive operator.
