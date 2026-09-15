# Infinities — Computational Foundations v0.1

Status: `RESEARCH_PROGRAMME / COMPUTATIONAL_BOOTSTRAP`

This document turns the initial `Infinities` operator sketch into a falsifiable computational programme. It does not claim a proof of the Riemann Hypothesis, Collatz, Twin Primes, or another open problem.

## State model

A working infinity object is represented as

\[
\mathfrak I=(X,\mathcal G,\tau,\mathcal O),
\]

where `X` is a carrier, `G` is a generator family, `tau` is the topology / valuation / completion rule, and `O` is a family of observables or defects. A concrete infinity type is studied through

\[
\operatorname{InfType}(x)=\operatorname{Asymp}_{\tau}\left(\mathcal O(G_n\cdots G_1x)\right).
\]

The current generator vocabulary is deliberately small: transport/order, scale/weight, branching/factorisation, inversion/duality, and completion. Fixed points, entropy, Fredholm index, dimension, escape rate, and finite defects are observables rather than assumed generators.

## Exact computational targets

The first suite checks the following exact identities or criteria:

1. Positive compactification
   \[q=x/(1+x),\quad \eta=(x-1)/(x+1),\quad B=\log x.\]
   Under `x -> 1/x`,
   \[q\to1-q,\quad\eta\to-\eta,\quad B\to-B.\]
   The self-dual seam is `x=1 <=> q=1/2`.

2. Cantor / Shannon bridge for the uniform Cantor measure
   \[H(1/2,1/2)=\ln2,\qquad D=\frac{H}{\ln3}=\frac{\ln2}{\ln3}.\]

3. Telescoping product
   \[\prod_{n=2}^{N}(1-1/n)=1/N.\]
   Inversion therefore exchanges the product collapse with ordinary growth `N -> infinity`.

4. Continued fraction fixed point
   \[x=1+1/(1+x)\Rightarrow x=\sqrt2.\]

5. `2`-adic geometric series
   \[S_N=1+2+\cdots+2^N=2^{N+1}-1,\]
   while
   \[|S_N+1|_2=2^{-(N+1)}\to0.\]

6. Compactified accelerated odd-Collatz branch
   \[U(n)=(3n+1)/2^{a(n)},\quad a(n)=v_2(3n+1),\]
   with
   \[B_C(n)=(n-1)/(n+1)\]
   and exact branch map
   \[T_a(B)=\frac{(2-c)+(1+c)B}{(2+c)+(1-c)B},\quad c=2^{a-1}.\]
   The validator checks `T_a(B_C(n)) = B_C(U(n))` on explicit integer witnesses. This is not a proof of global Collatz convergence.

7. Gabriel family `y=x^{-p}`
   volume converges iff `p>1/2`; surface area converges iff `p>1`. The classical horn `p=1` therefore has finite volume and infinite area.

8. Unilateral shift
   for `U^k`, the defect rank is `k` and the Fredholm index is `-k`. The infinite self-embedding retains a finite algebraic defect.

9. Euler product / Dirichlet series
   numerical witnesses compare finite approximants at `s=2` against `zeta(2)=pi^2/6`. The equality of the infinite objects for `Re(s)>1` is standard mathematics; the finite calculation is only a numerical control.

## Claim firewall

Every future computation must carry one of: `DEFINITION`, `EXACT`, `STANDARD_THEOREM`, `NUMERICAL_WITNESS`, `CONDITIONAL`, `CONJECTURAL`, `OPEN`, or `FAIL`.

A numerical witness cannot be promoted to a theorem. Structural similarity cannot be promoted to identity. A finite Collatz test cannot be promoted to global convergence. A zeta calculation cannot be promoted to RH. The appearance of `ln(2)` does not by itself authorize insertion of the project constant `kappa = ln(2)/(24*pi)` into another branch.
