# Euler-Hilbert-Hotel Supersymmetry v0.1

Status: **EXACT OPERATOR CONSTRUCTION / STANDARD SUSY ALGEBRA / TETRAHEDRAL SUPERTRANSLATION LIFT EXACT WITH CAR INPUT / PHYSICAL INTERPRETATION OPEN**

Date: 2026-09-22

## 1. Cross-repository input

\`Infinities\` already contains the common Hilbert carrier

\[
\mathcal H=\ell^2(\mathbb N)
\]

and the unilateral shift

\[
S|n\rangle=|n+1\rangle,
\qquad
S^\dagger S=I,
\qquad
SS^\dagger=I-|1\rangle\langle1|.
\]

The \`secret-of-a-half\` result \`SOH-G013\` independently proves an exact Pauli / SU(2) lift of the Euler/projective operator algebra. In particular the non-central lifts square to \`-I\`, and the projective order-two action becomes order four in the spinor lift.

The present note combines these structures without importing any zeta-zero claim.

## 2. Exact N=2 construction

On

\[
\mathscr H=\mathcal H\oplus\mathcal H
\]

define the grading

\[
\Gamma=\begin{pmatrix}I&0\\0&-I\end{pmatrix}
\]

and complex supercharges

\[
\mathcal Q=\begin{pmatrix}0&0\\S&0\end{pmatrix},
\qquad
\mathcal Q^\dagger=\begin{pmatrix}0&S^\dagger\\0&0\end{pmatrix}.
\]

Then

\[
\mathcal Q^2=(\mathcal Q^\dagger)^2=0,
\qquad
\{\Gamma,\mathcal Q\}=\{\Gamma,\mathcal Q^\dagger\}=0,
\]

and

\[
H=\{\mathcal Q,\mathcal Q^\dagger\}
=\begin{pmatrix}I&0\\0&I-P_1\end{pmatrix},
\quad
P_1=|1\rangle\langle1|.
\]

For

\[
Q_1=\mathcal Q+\mathcal Q^\dagger,
\qquad
Q_2=i(\mathcal Q^\dagger-\mathcal Q),
\]

we obtain the standard supersymmetric quantum-mechanical algebra

\[
\boxed{\{Q_i,Q_j\}=2\delta_{ij}H},
\qquad
[H,Q_i]=0,
\qquad
\{\Gamma,Q_i\}=0.
\]

This is theorem-level in the declared Hilbert-space model.

## 3. Witten index = Hilbert-Hotel/Fredholm defect

The positive sector has no zero mode. The negative sector has the protected zero mode \`|1>\`.

With the grading convention above,

\[
\boxed{\Delta_W=-1=\operatorname{ind}(S)}.
\]

For the k-step shift,

\[
S^{\dagger k}S^k=I,
\qquad
S^kS^{\dagger k}=I-P_k,
\]

where \`P_k\` projects onto the first \`k\` basis states. Therefore

\[
\boxed{\Delta_W(H_k)=-k=\operatorname{ind}(S^k)}
\]

and exactly \`k\` zero modes are protected in one grading sector.

## 4. Zero-centred complex analytic carriers

A bare pointed plane \`(C,0)\` does not determine a unique supercharge.

However, on Hardy space \`H^2(D)\`, multiplication by \`z\` is exactly the unilateral shift:

\[
M_z(1,z,z^2,\ldots)=(z,z^2,z^3,\ldots).
\]

The distinguished zero \`z=0\` determines the codimension-one subspace \`zH^2(D)\`. Thus the supersymmetric defect becomes a genuine analytic zero-mode defect once the Hilbert carrier is specified.

This is the correct scoped version of the statement that a zero-centred complex analytic plane supports the supersymmetric construction.

## 5. Tetrahedral null-generated causal cone

Let

\[
\mathbf n_1=(1,1,1)/\sqrt3,
\quad
\mathbf n_2=(1,-1,-1)/\sqrt3,
\]

\[
\mathbf n_3=(-1,1,-1)/\sqrt3,
\quad
\mathbf n_4=(-1,-1,1)/\sqrt3.
\]

Then

\[
\sum_a\mathbf n_a=0,
\qquad
\mathbf n_a\cdot\mathbf n_b=-1/3\;(a\ne b),
\qquad
\frac14\sum_a\mathbf n_a\mathbf n_a^T=I_3/3.
\]

Define future-null generators

\[
k_a=(1,\mathbf n_a).
\]

For nonnegative coefficients \`p_a\`,

\[
P=\sum_a p_a k_a
\]

obeys the exact identity

\[
\boxed{
P^2=\frac83\sum_{a<b}p_ap_b\ge0.
}
\]

Hence the positive span of the four null rays is a simplicial causal cone contained in the future Lorentz cone. Its fixed-time section is the regular tetrahedron inside the unit ball; only the four vertices are null.

## 6. Spinor lift

For Pauli matrices \`sigma^mu=(I,sigma_x,sigma_y,sigma_z)\`,

\[
K_a=I+\mathbf n_a\cdot\boldsymbol\sigma
\]

is positive semidefinite, rank one, and has zero determinant. Therefore

\[
\boxed{K_a=\lambda_a\lambda_a^\dagger}
\]

for a two-spinor \`lambda_a\`.

The phase gauge is

\[
\lambda_a\sim e^{i\chi_a}\lambda_a.
\]

The sign \`lambda_a -> -lambda_a\` is the Euler half-turn element of that phase gauge; it is not the entire gauge freedom.

## 7. Exact tetrahedral N=1 supertranslation lift

Attach four fermionic modes satisfying

\[
\{f_a,f_b^\dagger\}=\delta_{ab},
\qquad
\{f_a,f_b\}=\{f_a^\dagger,f_b^\dagger\}=0.
\]

For \`p_a >= 0\`, define

\[
P_{\alpha\dot\beta}
=\sum_a p_a\lambda_{a\alpha}\bar\lambda_{a\dot\beta},
\]

\[
Q_\alpha
=\sqrt2\sum_a\sqrt{p_a}\lambda_{a\alpha}f_a^\dagger,
\qquad
\bar Q_{\dot\beta}
=\sqrt2\sum_a\sqrt{p_a}\bar\lambda_{a\dot\beta}f_a.
\]

The CAR immediately give

\[
\boxed{
\{Q_\alpha,\bar Q_{\dot\beta}\}
=2P_{\alpha\dot\beta}
}
\]

and

\[
\{Q_\alpha,Q_\beta\}=0,
\qquad
\{\bar Q_{\dot\alpha},\bar Q_{\dot\beta}\}=0.
\]

Thus the tetrahedral momentum cone admits an exact algebraic realization of the 3+1 dimensional N=1 supertranslation algebra once one CAR mode is supplied per null ray.

## 8. Proof firewall

### PROVED / EXACT IN DECLARED MODEL

- unilateral-shift N=2 SUSY algebra;
- protected zero mode of the rank-one shift defect;
- \`Delta_W = ind(S^k) = -k\` with the declared grading convention;
- tetrahedral isotropy identities;
- nullity of the four generators;
- exact causal-cone norm \`P^2=(8/3) sum_{a<b} p_a p_b\`;
- rank-one spinor factorization of each tetrahedral null generator;
- N=1 supertranslation algebra after CAR modes are supplied.

### STANDARD / NOT A NOVELTY CLAIM

- general supersymmetric quantum-mechanical factorization by a Fredholm operator;
- Witten/Fredholm index relation in this standard operator setting;
- null-vector two-spinor factorization;
- CAR realization of the supertranslation anticommutator.

### OPEN / NOT PROMOTED

- physical supersymmetry of Nature;
- a theory of everything;
- derivation of fermionic CAR modes from tetrahedral geometry alone;
- a canonical scale law for an infinite nested tetrahedral cone;
- a unique supercharge from a bare pointed complex plane;
- any implication for RH, Collatz, Twin Prime, or other open problems.

## 9. Article

The full LaTeX article is stored at:

\`papers/euler_hilbert_hotel_supersymmetry.tex\`

A locally compiled and visually checked PDF was produced from the same source.
