# TIR Exceptional McKay Balance and Cyclic-Supergrading Selector v0.1

Status: **EXACT_EXCEPTIONAL_BINARY_POLYHEDRAL_CLASSIFICATION / E6_LINEAR_PARITY_BALANCE_UNIQUE / E6_CYCLIC_SUPERGRADING_MATCH_UNIQUE / NOVELTY_NOT_YET_CLAIMED**

Date: 2026-09-22

Parents:
- research/TIR_AFFINE_CRITICAL_C6_SELECTION_V0_1.md
- research/TIR_C6_SUPERGRADING_CROSSWALK_V0_1.md
- research/TIR_CYCLIC_ARM_CRITICALITY_E6_V0_1.md
- TIR Stage-14 McKay closure \(2T\leftrightarrow\widetilde E_6\), \(2O\leftrightarrow\widetilde E_7\), \(2I\leftrightarrow\widetilde E_8\)

## 1. Exceptional binary-polyhedral family

Let

\[
G_n=\langle r,s,t\mid r^2=s^3=t^n=rst\rangle,
\qquad
n\in\{3,4,5\}.
\]

These are respectively the exceptional binary polyhedral groups

\[
G_3=2T,\qquad
G_4=2O,\qquad
G_5=2I.
\]

Their McKay graphs for the defining spinor representation are

\[
2T\leftrightarrow\widetilde E_6,
\qquad
2O\leftrightarrow\widetilde E_7,
\qquad
2I\leftrightarrow\widetilde E_8.
\]

## 2. Exact abelianization classification from the presentations

Abelianizing the presentation gives additive relations

\[
2r=3s,
\qquad
3s=nt,
\qquad
nt=r+s+t.
\]

In the basis \((r,s,t)\), the relation matrix is

\[
M_n=
\begin{pmatrix}
2&-3&0\\
0&3&-n\\
-1&-1&n-1
\end{pmatrix}.
\]

Its Smith normal form for \(n=3,4,5\) is

\[
\operatorname{SNF}(M_3)=\operatorname{diag}(1,1,3),
\]

\[
\operatorname{SNF}(M_4)=\operatorname{diag}(1,1,2),
\]

\[
\operatorname{SNF}(M_5)=\operatorname{diag}(1,1,1).
\]

Therefore

\[
\boxed{
(2T)_{\rm ab}\cong C_3,
\qquad
(2O)_{\rm ab}\cong C_2,
\qquad
(2I)_{\rm ab}=1.
}
\]

Equivalently,

\[
\boxed{
|G_n^{\rm ab}|=6-n.
}
\]

Hence the number of one-dimensional irreducible characters in the exceptional McKay systems is respectively

\[
3,\qquad2,\qquad1.
\]

## 3. Central spin parity and McKay bipartition

Let

\[
z=-I
\]

be the central order-two element of each binary group.

Every irreducible representation has central sign

\[
\varepsilon_\lambda\in\{+1,-1\}.
\]

Since the defining spinor \(V\) has central sign \(-1\), tensoring by \(V\) flips central parity. Therefore every exceptional McKay graph is bipartite:

\[
\mathcal R_+
\longleftrightarrow
\mathcal R_-.
\]

For the Stage-14 affine dimension vectors, use the exact graph bipartitions determined by the McKay edges.

The linear sums of dimensions on the two parity classes are:

\[
\widetilde E_6:
\qquad
\boxed{6\mid6},
\]

\[
\widetilde E_7:
\qquad
\boxed{8\mid10},
\]

\[
\widetilde E_8:
\qquad
\boxed{14\mid16},
\]

up to exchanging the two colors.

Thus:

\[
\boxed{
\text{linear central-parity balance}
\iff
G=2T
\iff
\widetilde E_6
}
\]

within the exceptional family.

This balance is strictly stronger than the universal quadratic balance below.

## 4. Universal quadratic parity balance

Let \(d_\lambda=\dim\lambda\).

The regular representation has character zero on every nonidentity element, in particular on the center \(z=-I\). Therefore

\[
0
=
\chi_{\rm reg}(z)
=
\sum_\lambda
d_\lambda\,\chi_\lambda(z)
=
\sum_\lambda
\varepsilon_\lambda d_\lambda^2.
\]

Hence for every binary polyhedral group in the exceptional family,

\[
\boxed{
\sum_{\lambda\in\mathcal R_+}d_\lambda^2
=
\sum_{\lambda\in\mathcal R_-}d_\lambda^2
=
\frac{|G|}{2}.
}
\]

Numerically:

\[
2T:\quad12\mid12,
\]

\[
2O:\quad24\mid24,
\]

\[
2I:\quad60\mid60.
\]

So quadratic parity balance is universal, whereas linear parity balance uniquely selects \(2T/\widetilde E_6\).

## 5. Coxeter-number comparison

The sums of all affine McKay dimensions are

\[
12,\qquad18,\qquad30,
\]

which are the Coxeter numbers

\[
h(E_6)=12,\qquad
h(E_7)=18,\qquad
h(E_8)=30.
\]

For the parity halves one therefore has:

\[
\widetilde E_6:
\qquad
6+6=12,
\]

\[
\widetilde E_7:
\qquad
8+10=18,
\]

\[
\widetilde E_8:
\qquad
14+16=30.
\]

Only in the \(E_6\) case is the Coxeter mark sum split equally:

\[
\boxed{
\sum_{\mathcal R_+}d_\lambda
=
\sum_{\mathcal R_-}d_\lambda
=
\frac{h(E_6)}{2}
=
6.
}
\]

## 6. Abelianization plus fermion parity

Combine the one-dimensional character group with fermion parity:

\[
\mathcal G_{\rm ab+F}
=
G_{\rm ab}\times Z_2^F.
\]

For the three exceptional groups:

\[
2T:
\qquad
C_3\times C_2
\cong
\boxed{C_6},
\]

\[
2O:
\qquad
C_2\times C_2
\cong
\boxed{V_4},
\]

\[
2I:
\qquad
1\times C_2
\cong
\boxed{C_2}.
\]

Thus the tetrahedral case is uniquely characterized by a cyclic joint abelianization/parity grading of order greater than two.

## 7. Exceptional Coxeter-supergrading matching theorem

The orders of the joint grading groups are

\[
6,\qquad4,\qquad2.
\]

The half-Coxeter numbers are

\[
6,\qquad9,\qquad15.
\]

Therefore

\[
\boxed{
|\mathcal G_{\rm ab+F}|
=
\frac{h}{2}
}
\]

holds exactly for

\[
\boxed{
2T\leftrightarrow\widetilde E_6
}
\]

and fails for \(2O/\widetilde E_7\) and \(2I/\widetilde E_8\).

Equivalently, within the exceptional binary-polyhedral sequence, the following conditions hold simultaneously only in the tetrahedral case:

1. the affine McKay dimension vector is linearly balanced across central parity;
2. the abelianization combined with fermion parity is cyclic;
3. the order of that cyclic grading equals the dimension sum on either parity half;
4. that common value is \(h/2\).

Hence

\[
\boxed{
2T/\widetilde E_6:
\qquad
|C_6|
=
6
=
\sum_{\mathcal R_+}d_\lambda
=
\sum_{\mathcal R_-}d_\lambda
=
\frac{h(E_6)}2.
}
\]

This is an exact exceptional-family selection theorem.

## 8. Relation to the present supersymmetry carrier

The current tetrahedral construction already provides

\[
\mathcal G_6
=
\mathcal Z(-1)^F
\]

with

\[
\mathcal G_6^3=(-1)^F,
\qquad
\mathcal G_6^4=\mathcal Z.
\]

The present theorem shows that this \(C_6\) is not merely available because a \(C_3\) happened to be chosen.

Within the exceptional McKay family:

- \(2T\) is the only member whose abelian character group is \(C_3\);
- only \(2T\) combines with fermion parity to produce a cyclic \(C_6\);
- only its affine \(E_6\) dimension vector is linearly parity-balanced;
- the balance value is exactly the order of the \(C_6\) grading.

Thus the tetrahedral branch has a four-way compatibility:

\[
\boxed{
\text{abelianization}
\leftrightarrow
\text{fermion parity}
\leftrightarrow
\text{affine McKay marks}
\leftrightarrow
\text{Coxeter number}.
}
\]

## 9. Separation from the earlier arm-family selector

There are now two independent selection mechanisms.

### Uniform cyclic-arm family

\[
\rho(A_n)=2
\iff
n=3
\]

selects the three-arm graph and hence \(\widetilde E_6\).

### Exceptional binary-polyhedral family

\[
\boxed{
\text{linear parity balance}
+
\text{cyclic }(G_{\rm ab}\times Z_2^F)
+
|G_{\rm ab}\times Z_2^F|=h/2
}
\]

selects \(2T/\widetilde E_6\).

The two selectors begin from different data and converge on the same exceptional case.

This convergence is mathematically stronger than either selector alone, but it is not by itself a proof of physical uniqueness.

## 10. Firewall

### EXACT / STANDARD GIVEN THE DECLARED PRESENTATIONS AND MCKAY DATA

- exceptional binary-polyhedral presentations;
- abelianizations \(C_3,C_2,1\);
- central-parity bipartition;
- universal equality of quadratic parity sums;
- Stage-14 affine dimension vectors;
- linear parity sums \(6|6\), \(8|10\), \(14|16\);
- Coxeter numbers \(12,18,30\);
- joint grading groups \(C_6,V_4,C_2\);
- uniqueness of the \(E_6\) equality
  \[
  |\mathcal G_{\rm ab+F}|=h/2.
  \]

### NOT CLAIMED

- literature priority for this combined selector;
- that \(E_6\) is a physical gauge symmetry;
- that the mathematical \(C_6\) is physical time;
- that the exceptional-family selector proves supersymmetry in Nature.

The next gate is a dedicated literature audit of the combined balance/cyclicity/Coxeter matching theorem and, independently, a categorical formulation that explains why the two separate \(E_6\) selectors coincide.
