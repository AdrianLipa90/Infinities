# Euler-Hilbert-Hotel Supersymmetry v0.5 — Twist/Completeness and McKay-Incidence SUSY

Status: **EXACT FINITE REPRESENTATION THEOREMS / MODE-MINIMAL E6 SUPPORT / NOVELTY NOT YET CLAIMED**

Date: 2026-09-22

## 1. Setup

Let (G=2T) be the binary tetrahedral group. Let (eta) generate its one-dimensional character group

[
widehat{G}_{1D}cong G_{mathrm{ab}}cong C_3,
qquad
eta^3=1.
]

Let (V) denote the defining spinorial doublet. The three spinorial irreducibles are

[
V,qquad eta V,qquad eta^{-1}V.
]

The remaining irreducibles are

[
1,qquad eta,qquad eta^{-1},qquad 3.
]

The standard McKay fusion rules are

[
Votimes 1=V,
qquad
Votimeseta=eta V,
qquad
Votimeseta^{-1}=eta^{-1}V,
]

[
Votimes V=1oplus3,
]

[
Votimeseta V=etaoplus3,
qquad
Votimeseta^{-1}V=eta^{-1}oplus3,
]

[
Votimes3=Vopluseta Vopluseta^{-1}V.
]

## 2. Twist–completeness equivalence

For (jinmathbb Z/3mathbb Z), define a four-dimensional one-particle carrier

[
K_j=Voplus eta^jV.
]

Its fermionic Fock space is

[
mathcal F_j=Lambda^ullet K_j^*.
]

Because (V^*cong V),

[
K_j^*cong Vopluseta^{-j}V.
]

For a doublet (eta^rV),

[
Lambda^ullet(eta^rV)
=
1opluseta^rVopluseta^{-r},
]

since (det(eta^rV)=eta^{2r}=eta^{-r}).

### Theorem 2.1 — Twist–completeness equivalence

For the family (K_j=Vopluseta^jV),

[
oxed{
j
eq0
iff
operatorname{Supp}Lambda^ullet K_j^*
=
operatorname{Irr}(2T).
}
]

Equivalently, the exterior Fock representation contains all seven irreducible (2T)-types if and only if the second doublet is a nontrivial (C_3) twist of the defining doublet.

For (j=0),

[
Lambda^ullet K_0^*
cong
5cdot1oplus4cdot Voplus3,
]

so only the types

[
{1,V,3}
]

occur.

For (j=1),

[
Lambda^ullet K_1^*
cong
2cdot1
oplus
2cdoteta
oplus
eta^{-1}
oplus
V
oplus
eta V
oplus
2cdot(eta^{-1}V)
oplus
3.
]

For (j=2), the formula is obtained by (etaleftrightarroweta^{-1}). In both nontrivial cases all seven irreducible types occur.

## 3. Intertwiner dichotomy

The same twist controls the odd-operator sector.

If (j=0), then

[
dim_{mathbb C}operatorname{Hom}_{2T}(V,V)=1.
]

Hence an untwisted equivariant odd line exists.

If (j
eq0), Schur's lemma gives

[
oxed{
operatorname{Hom}_{2T}(V,eta^jV)=0,
}
]

but

[
oxed{
dim_{mathbb C}
operatorname{Hom}_{2T}
(eta^jV,eta^jV)
=1.
}
]

Equivalently, the odd map exists uniquely only as a (C_3)-charged/twisted intertwiner.

Thus

[
oxed{
	ext{nontrivial complement twist}
iff
	ext{no untwisted odd map}
iff
	ext{unique twisted odd line}
iff
	ext{full Fock irrep support}.
}
]

For the tetrahedral SIC minimal Naimark complement, v0.4 identifies exactly the (j=pm1) case. Hence the mirror Naimark sector supplies the representation-completing twist and simultaneously forces the complex supercharge to carry nontrivial discrete (C_3) R-charge.

## 4. Minimal fermionic mode theorem for (2T)

Any representation containing every irreducible (2T)-type at least once has dimension at least

[
1+1+1+2+2+2+3=12.
]

An (m)-mode complex fermionic Fock space has dimension (2^m). Therefore representation-complete support requires

[
2^mge12,
]

so

[
mge4.
]

The tetrahedral SIC/Naimark construction has exactly four outcome modes and v0.4/v0.5 explicitly realizes all seven irreducible types. Therefore

[
oxed{
m_{min}^{mathrm{Fock support}}(2T)=4.
}
]

This is an exact mode-minimality theorem.

## 5. Exceptional McKay mode thresholds

TIR Stage 14 records the affine exceptional dimension vectors

[
widetilde E_6: (3,2,2,2,1,1,1),
]

[
widetilde E_7: (4,3,2,1,3,2,1,2),
]

[
widetilde E_8: (6,5,4,3,2,1,4,2,3).
]

Their coordinate sums are

[
12,qquad18,qquad30.
]

Thus any Fock representation containing every irreducible type of the corresponding binary polyhedral group must satisfy

[
2^mge12,quad 2^mge18,quad 2^mge30,
]

respectively. Hence

[
oxed{
mge4 	ext{for }2T,
qquad
mge5 	ext{for }2O,
qquad
mge5 	ext{for }2I.
}
]

Consequently a four-mode Fock carrier can be representation-complete for the exceptional (E_6) case but cannot be representation-complete for the exceptional (E_7) or (E_8) cases.

The tetrahedral SIC/Naimark carrier realizes the allowed (E_6) case and saturates the lower bound.

## 6. McKay incidence as a finite N=2 supercharge

Split the seven irreducible (2T)-types by the central element (-I):

[
mathcal R_+
=
{1,eta,eta^{-1},3},
]

[
mathcal R_-
=
{V,eta V,eta^{-1}V}.
]

Tensoring by the defining spinor (V) flips central parity. In the ordered bases

[
(1,eta,eta^{-1},3)
]

and

[
(V,eta V,eta^{-1}V),
]

the McKay incidence operator (B:mathbb C^4	omathbb C^3) is

[
oxed{
B=
egin{pmatrix}
1&0&0&1\
0&1&0&1\
0&0&1&1
end{pmatrix}.
}
]

It has

[
operatorname{rank}B=3,
qquad
dimker B=1,
qquad
dimker B^dagger=0.
]

Therefore

[
oxed{
operatorname{ind}(B)=1.
}
]

Define

[
Q_B=
egin{pmatrix}
0&0\
B&0
end{pmatrix},
qquad
Q_B^dagger=
egin{pmatrix}
0&B^dagger\
0&0
end{pmatrix}.
]

Then

[
Q_B^2=(Q_B^dagger)^2=0
]

and

[
H_B=
{Q_B,Q_B^dagger}
=
operatorname{diag}(B^dagger B,BB^dagger).
]

Hence this McKay-incidence system is an exact finite (mathcal N=2) supersymmetric quantum-mechanical model with

[
oxed{
Delta_W=1.
}
]

Its spectra are

[
oxed{
operatorname{spec}(B^dagger B)={0,1,1,4},
qquad
operatorname{spec}(BB^dagger)={1,1,4}.
}
]

The unique protected zero mode is

[
oxed{
v_0=(1,1,1,-1)^T,
}
]

up to scale and basis-sign convention.

This vector is the linear relation saying that the central McKay branch column equals the sum of the three arm columns.

## 7. Affine (E_6) dimension vector inside the same incidence operator

Let

[
d_+=(1,1,1,3)^T,
qquad
d_-=(2,2,2)^T.
]

Then

[
oxed{
Bd_+=2d_-,
qquad
B^dagger d_-=2d_+.
}
]

Therefore the full bipartite adjacency operator

[
D_{mathrm{McK}}
=
egin{pmatrix}
0&B^dagger\
B&0
end{pmatrix}
]

satisfies

[
oxed{
D_{mathrm{McK}}
inom{d_+}{d_-}
=
2
inom{d_+}{d_-}.
}
]

Equivalently,

[
oxed{
C_{widetilde E_6}
=
2I-D_{mathrm{McK}}
}
]

annihilates the positive affine dimension vector.

Thus the same rectangular operator (B) simultaneously carries:

1. the central-parity McKay adjacency;
2. an (mathcal N=2) SUSY factorization with Witten index (+1);
3. the affine (E_6) Perron/dimension-vector relation.

## 8. Relation to the Fock construction

The one-particle creation operators transforming in (Vsubset K^*) change fermion parity and obey the same representation-selection rules encoded by (B).

Therefore (B) is the irrep-type/decategorified support matrix of the defining-spinor CAR creation channel.

The v0.4 identity

[
(-I)_{mathrm{spin}}mapsto(-1)^F
]

and the v0.5 McKay incidence factorization are compatible:

[
oxed{
	ext{CAR oddness}
longleftrightarrow
	ext{central-parity flip}
longleftrightarrow
widetilde E_6	ext{ adjacency}.
}
]

## 9. Stable Hilbert-Hotel class

The finite McKay incidence operator has index (+1). After the standard infinite-dimensional stabilization used in Fredholm K-theory, its connected Fredholm class is the same index class as the adjoint unilateral shift:

[
oxed{
[B]_{mathrm{stable}}
=
[S^dagger]_{mathrm{Fredholm}},
qquad
Delta_W=+1.
}
]

Thus the affine-(E_6) McKay incidence brick lands in the unit Hilbert-Hotel supersymmetry sector.

This is a stable-index statement, not an identification of the finite matrix (B) with (S^dagger).

## 10. Status firewall

### EXACT / STANDARD GIVEN THE DECLARED REPRESENTATION RING

- the seven irreducible (2T)-types and McKay fusion rules;
- the exterior-algebra decompositions above;
- the twist–completeness equivalence for (K_j=Vopluseta^jV);
- the intertwiner dichotomy by Schur's lemma;
- the exact minimum of four fermionic modes for representation-complete (2T) support;
- the exceptional four-mode exclusion for (2O/E_7) and (2I/E_8);
- the explicit affine-(E_6) bipartite incidence matrix;
- its rank, index, SUSY spectrum and protected zero mode;
- the affine dimension-vector equations (Bd_+=2d_-) and (B^dagger d_-=2d_+);
- stable Fredholm equivalence of index-(+1) systems after standard stabilization.

### NOT YET CLAIMED

- that the twist–completeness equivalence or mode-minimal McKay-SUSY packaging is absent from the literature;
- that this finite representation-theoretic SUSY is physical supersymmetry;
- a physical spin-statistics theorem;
- uniqueness of the tetrahedral SIC from Fock completeness alone.

## 11. Current novelty target

The strongest candidate statement requiring a dedicated literature audit is now:

[
oxed{
	ext{For the tetrahedral SIC, the same nontrivial }C_3	ext{ twist}
}
]

[
oxed{
	ext{(i) reverses the Naimark orientation,}
quad
	ext{(ii) forces a charged rather than invariant odd supercharge,}
}
]

[
oxed{
	ext{and (iii) is exactly the condition that completes the four-mode exterior Fock support to all seven affine-}E_6	ext{ McKay nodes.}
}
]

This is the current theorem package to audit for genuine novelty.
