# Euler's Infinity v0.1

Status: **POST-v1.0 RESEARCH EXTENSION / EXACT LOCAL IDENTITIES + OPEN FRACTAL-LIMIT QUESTIONS**

This note introduces **Euler's Infinity** as a phase-recursive complex-dynamical object inside the `Infinities` programme.

It does not claim a new theorem about the Riemann Hypothesis, Collatz, twin primes, or a universal theory of infinity. The exact statements below are elementary complex-analysis identities; the infinite-address and fractal-limit questions are kept explicitly open.

## 1. Euler phase map

Define

\[
\boxed{\mathcal E(z)=e^{i\pi z}.}
\]

The point (-1) is an exact fixed point:

\[
\boxed{\mathcal E(-1)=e^{-i\pi}=-1.}
\]

We call the fixed-point branch

\[
\boxed{\mathfrak E_\infty=-1}
\]

**Euler's Infinity**.

The right-nested notation

\[
e^{i\pi e^{i\pi e^{i\pi\cdots}}}
\]

is used here only as a symbolic fixed-point notation for the branch satisfying

\[
\boxed{X=e^{i\pi X},\qquad X=-1.}
\]

It must not be read as a claim that arbitrary finite truncations or arbitrary seeds converge to (-1).

A literal seeded iteration is defined separately by

\[
z_{n+1}=\mathcal E(z_n).
\]

If (z_0=-1), then (z_n=-1) for every (n). Other seeds need not converge to this fixed point.

## 2. Square-root double cover

Since

\[
\mathfrak E_\infty=-1,
\]

its algebraic square roots are

\[
\boxed{
\sqrt{\mathfrak E_\infty}\in\{+i,-i\}.
}
\]

Equivalently,

\[
(+i)^2=(-i)^2=-1.
\]

If a single-valued principal square-root convention is imposed, the principal value is (+i). The unordered algebraic square-root fibre is the two-point set ({+i,-i}).

Thus Euler's Infinity naturally carries a two-sheeted square-root lift:

\[
\boxed{
-1\longleftarrow\{+i,-i\}.
}
\]

This is the exact content of the (pm i) statement. No stronger topological or physical interpretation is assumed.

## 3. Fixed points and Lambert W

Every fixed point (X) of (mathcal E) satisfies

\[
X=e^{i\pi X}.
\]

Multiplying by (e^{-i\pi X}) and introducing

\[
Y=-i\pi X
\]

gives

\[
Y e^Y=-i\pi.
\]

Hence the fixed points are represented branchwise by the Lambert (W) function:

\[
\boxed{
X_k=\frac{i}{\pi}W_k(-i\pi),
\qquad k\in\mathbb Z,
}
\]

where (W_k) denotes a branch of Lambert (W).

The Euler's-Infinity point (X=-1) corresponds to any branch value satisfying

\[
W_k(-i\pi)=i\pi,
\]

because

\[
(i\pi)e^{i\pi}=-i\pi.
\]

This is a branch statement, not a claim that one distinguished global Lambert-(W) branch has been selected canonically.

## 4. Dynamical status of the Euler fixed point

The derivative is

\[
\mathcal E'(z)=i\pi e^{i\pi z}.
\]

Therefore

\[
\boxed{
\mathcal E'(-1)=-i\pi,
\qquad
|\mathcal E'(-1)|=\pi>1.
}
\]

Thus (-1) is a **repelling fixed point** of the ordinary forward iteration of (mathcal E).

This is why Euler's Infinity is defined as a fixed-point branch rather than as a universal attracting infinite tower.

## 5. Inverse branches and the Euler branch tree

Solving

\[
e^{i\pi z}=w
\]

gives

\[
i\pi z=\Log w+2\pi i k,
\qquad k\in\mathbb Z,
\]

and therefore

\[
\boxed{
\mathcal E_k^{-1}(w)
=
2k-\frac{i}{\pi}\Log w.
}
\]

For every admissible logarithm domain this gives countably many inverse branches indexed by (k\in\mathbb Z).

Finite inverse compositions therefore generate a countably branching preimage tree:

\[
w
\leftarrow
\mathcal E_{k_1}^{-1}(w)
\leftarrow
\mathcal E_{k_2}^{-1}\mathcal E_{k_1}^{-1}(w)
\leftarrow\cdots.
\]

A finite branch address is a word

\[
(k_1,\ldots,k_n)\in\mathbb Z^n.
\]

An infinite symbolic address is a sequence

\[
\mathbf k=(k_1,k_2,\ldots)\in\mathbb Z^{\mathbb N}.
\]

The symbolic address space is exact. Whether a particular infinite address defines a convergent geometric limit requires additional branch, domain, and convergence conditions and is therefore **OPEN**.

## 6. Why the word "fractal" needs a firewall

The exponential map is a standard object of complex dynamics, and repelling periodic/fixed points participate in Julia-set dynamics. However, this repository does not promote the phrase "fractal infinity" into a theorem merely from the existence of the branch tree.

The following statements are separated:

- countably many inverse branches: **EXACT**;
- arbitrarily deep preimage trees: **EXACT**;
- infinite symbolic branch addresses: **DEFINITION / EXACT SYMBOLIC SPACE**;
- convergence of every infinite address: **OPEN / FALSE WITHOUT EXTRA CONDITIONS IN GENERAL**;
- a particular Hausdorff dimension or self-similar fractal law for the Euler branch tree: **OPEN / NOT CLAIMED**.

Accordingly, "Euler's Infinity" names the fixed-point/branch construction, while "fractal infinity" remains a research interpretation until a precise invariant is stated and proved.

## 7. Relation to the Infinities programme

Euler's Infinity adds a new sector to the programme:

\[
\boxed{
\text{phase-recursive / branch infinity}
}
\]

with the basic data

\[
\boxed{
\left(
\mathcal E(z)=e^{i\pi z},
\;
\mathfrak E_\infty=-1,
\;
\sqrt{\mathfrak E_\infty}=\{\pm i\},
\;
\{\mathcal E_k^{-1}\}_{k\in\mathbb Z}
\right).
}
\]

It differs from the existing sectors:

- Hilbert-Hotel infinity concerns countable self-embedding;
- Collatz-type infinity concerns unbounded discrete iteration;
- spectral infinity concerns analytic/spectral summation;
- distributional infinity concerns sparse infinite subsets;
- Euler's Infinity concerns a complex phase map, a repelling fixed point, and its multi-branch inverse tree.

The common research question is whether these distinct forms admit useful operator-level relations without collapsing their mathematical types.

## 8. Minimal exact theorem package

The following package is exact:

\[
\boxed{
\begin{aligned}
\mathcal E(z)&=e^{i\pi z},\\
\mathcal E(-1)&=-1,\\
\mathcal E'(-1)&=-i\pi,\\
|\mathcal E'(-1)|&=\pi>1,\\
\sqrt{-1}&=\{+i,-i\},\\
\mathcal E_k^{-1}(w)
&=2k-\frac{i}{\pi}\Log w.
\end{aligned}
}
\]

The fixed-point family is

\[
\boxed{
X_k=\frac{i}{\pi}W_k(-i\pi).
}
\]

Anything beyond this package must be typed separately.

## 9. Epistemic ledger

| Claim | Status |
|---|---|
| (mathcal E(z)=e^{i\pi z}) | DEFINITION |
| (mathcal E(-1)=-1) | EXACT |
| Euler's Infinity is the fixed-point branch (mathfrak E_\infty=-1) | DEFINITION + EXACT FIXED-POINT IDENTITY |
| (sqrt{\mathfrak E_\infty}=\{+i,-i\}) | EXACT |
| fixed points satisfy (X_k=(i/\pi)W_k(-i\pi)) | EXACT BRANCHWISE IDENTITY |
| (-1) is repelling because (|\mathcal E'(-1)|=\pi>1) | EXACT / STANDARD COMPLEX-DYNAMICS CRITERION |
| inverse branches are (2k-(i/\pi)\Log w) | EXACT ON A DECLARED LOG BRANCH |
| finite inverse compositions form a countably branching preimage tree | EXACT |
| every infinite integer address converges to a geometric point | OPEN / NOT CLAIMED |
| the preimage tree has a specified fractal dimension | OPEN / NOT CLAIMED |
| Euler's Infinity proves any classical open problem | FALSE AS A REPOSITORY CLAIM / NOT CLAIMED |

## 10. Computational witness

`validate_eulers_infinity_v0_1.py` checks the exact finite identities with standard-library complex arithmetic.

The validator is a regression witness for the formulas. It is not a substitute for analytic proofs and does not test the open infinite-address/fractal claims.
