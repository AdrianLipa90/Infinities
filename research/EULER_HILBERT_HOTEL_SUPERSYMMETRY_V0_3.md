# Euler-Hilbert-Hotel Supersymmetry v0.3

Status: **EXACT FREDHOLM-HOMOTOPY CLASSIFICATION / TOEPLITZ K-THEORY CROSSWALK / EXACT BLASCHKE ZERO-MODE REALIZATION / BINARY-TETRAHEDRAL REST-FRAME COVARIANCE / PHYSICAL INTERPRETATION OPEN**

Date: 2026-09-22

## 1. Scope

This revision keeps the programme strictly modular.

Brick A is bounded Fredholm N=2 supersymmetric quantum mechanics and its Toeplitz/Hardy specialization.

Brick B is the tetrahedral null-spinor N=1 supertranslation frame with binary-tetrahedral covariance after explicit CAR input.

No RH, ToE, or other external research programme is needed.

## 2. Universal bounded-Fredholm SUSY factorization

Let H be a separable infinite-dimensional complex Hilbert space and let A:H->H be bounded Fredholm. On H direct-sum H define

[
Gamma=diag(I,-I),
qquad
Q_A=
\begin{pmatrix}
0&0\\
A&0
\end{pmatrix},
qquad
Q_A^dagger=
\begin{pmatrix}
0&A^dagger\\
0&0
\end{pmatrix}.
]

Then

[
Q_A^2=(Q_A^dagger)^2=0,
qquad
{Gamma,Q_A}={Gamma,Q_A^dagger}=0,
]

and

[
H_A={Q_A,Q_A^dagger}
=
diag(A^dagger A,AA^dagger).
]

The real supercharges close to

[
{Q_i,Q_j}=2delta_ij H_A.
]

The zero-mode sectors are

[
ker H_+=ker A,
qquad
ker H_-=ker A^dagger,
]

hence

[
oxed{
Delta_W(A)
=
dim ker A-dim ker A^dagger
=
ind(A).
}
]

This is standard Fredholm/SUSY operator theory.

## 3. Hilbert-Hotel normal-form theorem

The Atiyah-Janich theorem implies

[
pi_0(Fred(H))cong Z
]

with the Fredholm index as the complete connected-component invariant.

Therefore the associated bounded-Fredholm N=2 SUSY systems are homotopy-classified by their Witten index.

Let S be the unilateral shift. Since

[
ind(S^k)=-k,
qquad
ind((S^dagger)^k)=+k,
]

every Fredholm supercharge A is connected through a norm-continuous path of Fredholm operators to the explicit normal form

[
A_q=
egin{cases}
(S^dagger)^q,&q>0,\\
I,&q=0,\\
S^{-q},&q<0,
end{cases}
qquad
q=Delta_W(A).
]

Thus

[
oxed{
[A]_{Fredholm homotopy}
longleftrightarrow
Delta_W(A)in Z
longleftrightarrow
A_q.
}
]

This is the precise universal Hilbert-Hotel statement: every bounded Fredholm N=2 SUSY sector has a shift/adjoint-shift representative carrying exactly the same protected zero-mode imbalance.

No claim of novelty is made for the Atiyah-Janich classification; the present point is its explicit Hilbert-Hotel/SUSY normal-form interpretation.

## 4. Euler-Toeplitz classification

Let f:S^1->C* be continuous and T_f its Toeplitz operator on H^2(D). The classical theorem gives

[
ind(T_f)=-wind(f).
]

Therefore

[
oxed{
Delta_W(T_f)=-wind(f).
}
]

Moreover

[
fsimeq g 	ext{through nonvanishing symbols}
iff
wind(f)=wind(g)
iff
Delta_W(T_f)=Delta_W(T_g).
]

Hence the Witten index is a complete invariant of scalar nonvanishing-symbol Toeplitz SUSY sectors under symbol homotopy.

If k=wind(f), then f is homotopic in C* to z^k and

[
T_fsimeq_{Fredholm} T_{z^k}.
]

Thus the Toeplitz classification has the explicit normal form

[
T_{z^k}
=
egin{cases}
S^k,&kge0,\\
(S^dagger)^{-k},&k<0.
end{cases}
]

## 5. Toeplitz extension and K-theory boundary map

The Toeplitz C*-algebra fits into

[
0	o K(H^2)	o T	o C(S^1)	o0.
]

For a nonvanishing symbol f let

[
u_f=f/|f|
]

be its boundary unitary. The six-term exact sequence carries the connecting map

[
partial:
K_1(C(S^1))
	o
K_0(K(H^2)).
]

Using the convention fixed by

[
partial[z]=ind(T_z)=-1,
]

one has

[
oxed{
partial[u_f]
=
ind(T_f)
=
Delta_W(T_f)
=
-wind(f).
}
]

Since

[
K_1(C(S^1))cong Z,
qquad
K_0(K)cong Z,
]

the Euler phase winding is the K_1 charge and the Witten/Fredholm defect is its K_0 boundary image.

This is the conceptual reason the same integer appears in the analytic, topological, operator, and SUSY descriptions.

## 6. Group law and inverse sectors

For nonvanishing symbols,

[
wind(fg)=wind(f)+wind(g),
]

hence

[
oxed{
Delta_W(fg)
=
Delta_W(f)+Delta_W(g).
}
]

Also

[
Delta_W(f^{-1})=-Delta_W(f).
]

Thus Toeplitz SUSY sectors form a Z-valued stable charge under composition at the K_1/index level.

For general Fredholm supercharges,

[
Delta_W(Aoplus B)
=
Delta_W(A)+Delta_W(B).
]

A sector stacked with its inverse has total index zero and lies in the neutral connected component.

## 7. Finite Blaschke products: exact zero-mode Hamiltonian

Let B be a finite Blaschke product of degree k. Multiplication by B on H^2 is an isometry:

[
M_B^dagger M_B=I.
]

Its range is BH^2, so

[
M_BM_B^dagger=P_{BH^2}=I-P_{K_B},
]

where

[
K_B=H^2ominus BH^2
]

is the model space.

Therefore the SUSY Hamiltonian is exactly

[
oxed{
H_B
=
\begin{pmatrix}
I&0\\
0&I-P_{K_B}
\end{pmatrix}.
}
]

Hence

[
oxed{
ker H_-=K_B,
qquad
dim K_B=k,
}
]

and

[
oxed{
#Z_D(B)
=
wind(B)
=
-ind(T_B)
=
-Delta_W
=
dim K_B.
}
]

This is stronger than an index count: the protected zero-mode Hilbert space is identified explicitly.

## 8. Zero locations become zero-mode wavefunctions

For a simple zero a in D, the Hardy reproducing kernel

[
k_a(z)=rac{1}{1-ar a z}
]

satisfies

[
M_B^dagger k_a
=
overline{B(a)}k_a
=
0.
]

Thus every simple analytic zero produces an explicit protected zero mode. Repeated zeros produce the standard derivative-kernel chain.

For the normalized kernels

[
kappa_a(z)
=
rac{sqrt{1-|a|^2}}{1-ar a z},
]

the overlap is

[
oxed{
|<kappa_a,kappa_b>|^2
=
rac{(1-|a|^2)(1-|b|^2)}
{|1-ar a b|^2}
=
1-ho(a,b)^2,
}
]

where

[
ho(a,b)
=
left|
rac{a-b}{1-ar a b}
ight|
]

is the pseudohyperbolic distance.

Therefore the internal geometry of protected SUSY zero modes remembers the hyperbolic geometry of the analytic zero locations, while the Witten index remembers only their total multiplicity.

Moving zeros inside the disk deforms the zero-mode wavefunctions but cannot change their protected net count until the nonvanishing boundary condition is lost.

## 9. Izumi 2026 demarcation

The Fredholm formula

[
ind(T_f)=-wind(f)
]

is classical.

Izumi (2026) generalizes the winding-number formula to a Witten index for a broader class of almost-normal Toeplitz operators, including settings where the operator need not be Fredholm and a principal-value formula replaces the ordinary winding integral.

The present v0.3 result therefore does not claim the winding/Witten formula as new. It deliberately stays in the bounded-Fredholm sector, where the index is integer-valued and topologically classified, and uses that sector to construct the Hilbert-Hotel normal form and explicit Blaschke zero-mode realization.

## 10. Tetrahedral sector: exact spinorial rest frame

Let

[
k_a=(1,n_a)
]

be the four tetrahedral null rays and let the N=1 supertranslation construction use weights p_a>=0.

For equal weights p_a=p,

[
P^mu
=
psum_a k_a^mu
=
(4p,0,0,0),
]

so

[
oxed{
P^2=16p^2.
}
]

The projective tetrahedral group A_4 fixes this timelike axis and permutes the four null generators. Its spin lift 2T is a finite subgroup of

[
SU(2)=Spin(3)
subset
SL(2,C)=Spin^+(1,3).
]

With the compensating CAR representation described in v0.2, the equal-weight supercharge tensor is invariant under the combined 2T action.

Thus the tetrahedral SUSY brick has an exact discrete spinorial rest-frame symmetry, independently of the Toeplitz/Fredholm brick.

## 11. Firewall

### STANDARD / EXACT

- bounded Fredholm -> N=2 SUSY factorization;
- Delta_W=ind(A);
- pi_0(Fred(H)) ~= Z via the index;
- Hilbert-Hotel shift/adjoint-shift normal representatives;
- Toeplitz index = minus winding;
- complete scalar symbol-homotopy classification by winding;
- Toeplitz extension boundary map carries K_1 phase charge to K_0 index charge;
- finite Blaschke model-space zero-mode realization;
- reproducing-kernel zero modes and their pseudohyperbolic overlap;
- tetrahedral equal-weight rest-frame identity and binary-tetrahedral covariance after CAR input.

### NOT CLAIMED

- novelty of Atiyah-Janich, Toeplitz index theory, model-space theory, or binary tetrahedral group theory;
- derivation of the CAR algebra from tetrahedral geometry;
- physical realization of supersymmetry in Nature.

## 12. Compact theorem chain

The operator brick can now be written as

[
oxed{
egin{array}{c}
	ext{Euler boundary phase }u_f\\
downarrow\\
[u_f]in K_1(C(S^1))\\
downarrow partial\\
K_0(K)cong Z\\
downarrow\\
ind(T_f)=Delta_W\\
downarrow\\
	ext{Hilbert-Hotel normal form}
end{array}
}
]

and for finite Blaschke products,

[
oxed{
	ext{analytic zero multiplicity}
=
	ext{winding}
=
-	ext{Witten index}
=
dim(	ext{protected zero-mode space}).
}
]

This is the v0.3 core.
