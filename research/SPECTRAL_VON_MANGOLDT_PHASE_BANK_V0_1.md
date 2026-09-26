# Spectral von Mangoldt Phase Bank v0.1

Status: \`STANDARD_COROLLARY + NUMERICAL_WITNESS + OPEN_RESEARCH_PROGRAMME\`

This module sharpens the Skewes–Euler–Hilbert–Collatz bridge by replacing a qualitative phase analogy with a classical spectral identity.

It does **not** claim a new proof of the Riemann Hypothesis, the Collatz conjecture, or a new zero-spacing law.

## 1. Landau's formula

For fixed \(x>1\), Landau's formula gives

\[
\sum_{0<\gamma\le T} x^\rho
=
-\frac{T}{2\pi}\Lambda(x)
+
O_x(\log T),
\]

where the sum is over nontrivial zeros \(\rho=\beta+i\gamma\) of \(\zeta(s)\), and \(\Lambda(x)\) is the von Mangoldt function when \(x\) is an integer, extended as zero away from prime powers.

Thus the zero spectrum distinguishes prime powers at the level of the main term:

\[
\Lambda(q)
=
\begin{cases}
\log p,&q=p^a,\\
0,&q\text{ is not a prime power}.
\end{cases}
\]

This is classical mathematics, not a new theorem of this repository.

## 2. Phase-only form on the critical line

Under the critical-line specialization \(\rho=\tfrac12+i\gamma\),

\[
q^\rho
=
\sqrt q\,q^{i\gamma},
\]

so for a fixed integer \(q\ge2\),

\[
\sum_{0<\gamma\le T} q^{i\gamma}
=
-\frac{T}{2\pi}\frac{\Lambda(q)}{\sqrt q}
+
O_q(\log T).
\]

Define the normalized phase response

\[
R_q(T)
=
\frac1{N(T)}
\sum_{0<\gamma\le T}
e^{i\gamma\log q}.
\]

Using the Riemann–von Mangoldt asymptotic for \(N(T)\),

\[
R_q(T)
\sim
-\frac{\Lambda(q)}
{\sqrt q\,\log T}.
\]

Equivalently, in this critical-line phase form,

\[
\boxed{
\Lambda(q)
=
-\sqrt q
\lim_{T\to\infty}
\log T\,R_q(T)
}
\]

whenever the stated asymptotic hypotheses are used.

The important distinction is:

- Landau's original \(q^\rho\) formula is unconditional;
- the reduction to a pure phase average \(q^{i\gamma}\) uses critical-line placement.

## 3. Prime-power phase bank

For every integer base \(q\ge2\), define

\[
\omega_{\gamma,q}
=
\gamma\log q
\pmod{2\pi}.
\]

Then

\[
R_q(T)
=
\frac1{N(T)}
\sum_{\gamma\le T}
e^{i\omega_{\gamma,q}}.
\]

The main phase line is nonzero exactly when \(q\) is a prime power.

This gives a phase-bank representation of the von Mangoldt support:

\[
\boxed{
q\mapsto
\{\omega_{\gamma,q}\}_\gamma
\quad\Longrightarrow\quad
\Lambda(q)
}
\]

in the asymptotic Landau sense.

Again, this is a spectral re-expression of a classical theorem, not a new primality algorithm.

## 4. Dyadic clock

For the On-Primes affine map

\[
T(x)=2x+1
\]

we already have

\[
T(x)+1=2(x+1),
\qquad
\Delta\log(x+1)=\log2.
\]

Therefore the natural phase is

\[
\omega_\gamma
=
\gamma\log2
\pmod{2\pi}.
\]

Its \(m\)-th harmonic is

\[
e^{im\omega_\gamma}
=
(2^m)^{i\gamma}.
\]

Since every \(2^m\) is a prime power,

\[
\Lambda(2^m)=\log2,
\]

and the Landau phase main term is

\[
\boxed{
\frac1{N(T)}
\sum_{\gamma\le T}
e^{im\gamma\log2}
\sim
-
\frac{\log2}
{2^{m/2}\log T}.
}
\]

Thus the dyadic phase clock is not merely an arbitrary logarithmic coordinate: every harmonic lands on a prime-power line of the von Mangoldt spectrum.

## 5. Collatz reverse fibre lands on the second dyadic harmonic

For the accelerated odd-Collatz reverse fibre established in the companion bridge note,

\[
B_{a+2}(m)=4B_a(m)+1,
\]

and

\[
B_{a+2}(m)+\frac13
=
4\left(B_a(m)+\frac13\right).
\]

Hence its logarithmic step is

\[
\Delta\tau_C=\log4=2\log2.
\]

The associated zero phase is therefore

\[
e^{i\gamma\log4}
=
e^{2i\gamma\log2},
\]

which is exactly the \(m=2\) harmonic of the dyadic phase bank.

So the precise shared structure is

\[
\boxed{
2x+1
\leftrightarrow
\log2
\leftrightarrow
m=1
}
\]

and

\[
\boxed{
4x+1
\leftrightarrow
\log4
\leftrightarrow
m=2.
}
\]

This does **not** imply that zeta zeros govern Collatz dynamics. It says that the affine dilation scale occurring in the reverse Collatz fibre is the second harmonic of the same dyadic logarithmic clock.

## 6. Hilbert shift / Weyl relation

On fibre-index space,

\[
S|k\rangle=|k+1\rangle,
\qquad
D_\omega|k\rangle=e^{ik\omega}|k\rangle,
\]

so

\[
D_\omega S=e^{i\omega}SD_\omega.
\]

For

\[
\omega=\gamma\log2,
\]

the Hilbert-Hotel shift, the On-Primes dyadic index, and the Landau phase response are carried by the same phase operator.

## 7. Montgomery–Dyson remains a separate statistic

The Montgomery pair-correlation programme studies unfolded differences between zero ordinates and predicts the GUE pair-correlation curve

\[
1-
\left(
\frac{\sin\pi u}{\pi u}
\right)^2.
\]

This is **not** the same statistic as the phase projection

\[
\gamma\mapsto\gamma\log2\pmod{2\pi}.
\]

Both can be measured on the same zero set, but they must remain logically separate:

- Montgomery–Dyson: local spacing correlations after unfolding;
- present phase bank: Fourier response at fixed logarithmic frequencies \(\log q\).

## 8. Numerical witness: first 256 critical-line zeros

A finite experiment was run on the first 256 positive critical-line zero ordinates, through

\[
T=478.9421815346348.
\]

The zero values were generated with \`mpmath 1.3.0\` at 30 decimal-digit working precision. The first entries were cross-checked against published zero tables.

For the dyadic harmonics:

| \(m\) | \(q=2^m\) | observed \(|R_q|\) | Landau main-term magnitude | ratio |
|---:|---:|---:|---:|---:|
| 1 | 2 | 0.14427897 | 0.14593979 | 0.98862 |
| 2 | 4 | 0.10004494 | 0.10319502 | 0.96947 |
| 3 | 8 | 0.07208890 | 0.07296990 | 0.98793 |
| 4 | 16 | 0.03941446 | 0.05159751 | 0.76388 |
| 5 | 32 | 0.04139349 | 0.03648495 | 1.13454 |

For \(q=2,\ldots,20\), the finite sample had:

\[
\min_{\text{prime power }q}|R_q|
=
0.03941446,
\]

while

\[
\max_{\text{non-prime-power }q}|R_q|
=
0.01674392.
\]

Thus this finite window perfectly separates the 12 prime-power bases from the 7 non-prime-power composite bases by response magnitude. This is a **NUMERICAL_WITNESS** of the classical Landau mechanism, not a general classification theorem.

## 9. Montgomery–Dyson sanity check

Using the smooth Riemann–von Mangoldt unfolding and a coarse pair-correlation histogram on the same 256 zeros:

\[
\mathrm{RMSE}_{GUE}\approx0.12560,
\]

\[
\mathrm{RMSE}_{Poisson}\approx0.37919.
\]

The small low-zero sample is substantially closer to the GUE pair-correlation curve than to a Poisson baseline. This is only a diagnostic sanity check; Odlyzko's classical large computations are the relevant high-quality numerical evidence.

## 10. Controls

### Collatz period-3 reverse-branch control

The reverse-fibre branchability observable has an exact period-3 structure, with Fourier lines at

\[
\frac{2\pi}{3},
\qquad
\frac{4\pi}{3}.
\]

Testing the doubled dyadic zero phases against a preregistered local window \(\varepsilon=0.05\) rad gave:

- observed hits: 8;
- uniform reference expectation: 8.149;
- one-sided binomial reference \(p\approx0.570\).

No excess resonance is detected in this finite control.

### Dyadic prime-shell exploratory alignment

A separate transform used the finite residuals of the shell counts

\[
v_2(p+1)=k
\]

for primes \(p\le10^6\), relative to the simple finite reference \(N_{\rm odd}/2^k\).

The observed mean spectral power over the 256 dyadic zero phases was 1.13465. Against global rotations of the same zero-phase set, only about 0.00684 of reference rotations were at least as large.

This is **not an inferential p-value** and is explicitly classified as

\[
\texttt{EXPLORATORY\_NONINDEPENDENT}.
\]

The zero phases already possess the Landau dyadic bias, so a global-shift reference is not an independent null. This signal must be re-tested with a preregistered statistic and an appropriate analytic/null model before any interpretation.

## 11. Strongest supported conclusion

The strongest supported statement is:

\[
\boxed{
\text{prime-power support of }\Lambda
\quad\longleftrightarrow\quad
\text{main Fourier lines of zeta-zero log phases}
}
\]

with the dyadic On-Primes clock selecting \(q=2^m\) and the exact reverse-Collatz fibre selecting \(q=4\).

This is a genuine mathematical bridge, but its Landau core is classical.

## 12. Open programme

The next nontrivial questions are:

1. derive a continuation-safe version of the phase-bank observable directly inside the existing shifted-von-Mangoldt tower;
2. replace post-hoc shell alignment with preregistered statistics;
3. separate Riemann-zeta zero channels from Dirichlet-\(L\) channels associated with the residue shells \(p\equiv-1\pmod{r^j}\);
4. test whether the prime-mask spectra contain anything beyond the standard explicit-formula/Landau response;
5. keep the Skewes sign-reversal problem at the aggregate explicit-formula level rather than attributing a crossing to one phase line.

## 13. Claim firewall

Established here or imported from standard mathematics:

- affine dyadic and reverse-Collatz log steps: exact;
- Weyl shift relation: exact;
- Landau formula: standard theorem;
- phase-only von Mangoldt response: standard critical-line specialization;
- 256-zero response table: numerical witness;
- Montgomery–Dyson comparison: numerical diagnostic.

Not established:

- RH;
- Collatz convergence;
- a new proof of prime infinitude;
- a new proof of Littlewood sign changes;
- a first-Skewes-crossing formula;
- a new zero-spacing theorem;
- an independent prime-shell resonance.

## References

- E. Landau, *Über die Nullstellen der Zetafunktion*, Math. Ann. **71** (1911), 548–564.
- H. L. Montgomery, *The pair-correlation function for zeros of the zeta function*, Proc. Symp. Pure Math. **24** (1973), 181–193.
- A. M. Odlyzko, *On the Distribution of Spacings Between Zeros of the Zeta Function*, Math. Comp. **48** (1987), 273–308.
- F. Çiçek and S. M. Gonek, *The uniform distribution modulo one of certain subsequences of ordinates of zeros of the zeta function*, Math. Proc. Camb. Phil. Soc. **176** (2024), 593–608, doi:10.1017/S0305004124000045.
