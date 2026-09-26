#!/usr/bin/env python3
"""Finite phase-bank witness for zeta-zero log phases.

Requires mpmath. This is an experiment script, not a repository theorem checker.
It numerically illustrates the standard Landau/von-Mangoldt phase response and
runs small Montgomery-Dyson / Collatz controls.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math

try:
    import mpmath as mp
except ImportError as exc:
    raise SystemExit("mpmath is required for this experiment") from exc

TWOPI = 2.0 * math.pi


def prime_power_base(n: int):
    if n < 2:
        return False, None, None
    x = n
    factors = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0:
                x //= d
                e += 1
            factors.append((d, e))
        d = 3 if d == 2 else d + 2
    if x > 1:
        factors.append((x, 1))
    if len(factors) == 1:
        p, e = factors[0]
        return True, p, e
    return False, None, None


def von_mangoldt_int(n: int) -> float:
    ok, p, _ = prime_power_base(n)
    return math.log(p) if ok else 0.0


def phase_mean(gammas, q: int) -> complex:
    w = math.log(q)
    return sum(cmath.exp(1j * g * w) for g in gammas) / len(gammas)


def landau_phase_main(T: float, N: int, q: int) -> float:
    lam = von_mangoldt_int(q)
    return 0.0 if lam == 0.0 else -(T / TWOPI) * lam / math.sqrt(q) / N


def smooth_N(t: float) -> float:
    return t / TWOPI * math.log(t / TWOPI) - t / TWOPI + 7.0 / 8.0


def pair_correlation_rmse(gammas, max_s=3.0, bins_n=20):
    u = [smooth_N(t) for t in gammas]
    diffs = []
    for i, ui in enumerate(u):
        for uj in u[i + 1:]:
            d = uj - ui
            if d > max_s:
                break
            diffs.append(d)
    width = max_s / bins_n
    counts = [0] * bins_n
    for d in diffs:
        j = min(int(d / width), bins_n - 1)
        if 0 <= j < bins_n:
            counts[j] += 1
    rhat = [c / (len(gammas) * width) for c in counts]
    centers = [(j + 0.5) * width for j in range(bins_n)]
    def sinc_pi(x):
        return 1.0 if x == 0 else math.sin(math.pi * x) / (math.pi * x)
    gue = [1.0 - sinc_pi(s) ** 2 for s in centers]
    rmse_gue = math.sqrt(sum((a-b)**2 for a,b in zip(rhat,gue))/bins_n)
    rmse_poisson = math.sqrt(sum((a-1.0)**2 for a in rhat)/bins_n)
    return {
        "pair_count": len(diffs),
        "rmse_vs_gue_pair_curve": rmse_gue,
        "rmse_vs_poisson_pair_curve": rmse_poisson,
    }


def circular_distance(a, b):
    return abs((a - b + math.pi) % TWOPI - math.pi)


def binomial_upper_tail(k, n, p):
    return sum(math.comb(n,j) * p**j * (1-p)**(n-j) for j in range(k,n+1))


def collatz_period3_control(gammas, eps=0.05):
    lines = (TWOPI/3.0, 2.0*TWOPI/3.0)
    doubled = [(2.0*g*math.log(2.0)) % TWOPI for g in gammas]
    ds = [min(circular_distance(w,r) for r in lines) for w in doubled]
    hits = sum(d <= eps for d in ds)
    p0 = 2.0 * eps / math.pi
    return {
        "epsilon_rad": eps,
        "hits": hits,
        "expected_uniform_hits": len(gammas)*p0,
        "one_sided_binomial_reference_p": binomial_upper_tail(hits,len(gammas),p0),
        "minimum_distance_rad": min(ds),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=256)
    ap.add_argument("--dps", type=int, default=30)
    ap.add_argument("--max-base", type=int, default=20)
    ns = ap.parse_args()

    mp.mp.dps = ns.dps
    gammas = [float(mp.im(mp.zetazero(i))) for i in range(1, ns.n + 1)]
    T = gammas[-1]

    scan = []
    for q in range(2, ns.max_base + 1):
        z = phase_mean(gammas, q)
        pp, p, e = prime_power_base(q)
        scan.append({
            "q": q,
            "prime_power": pp,
            "base_prime": p,
            "exponent": e,
            "observed_real": z.real,
            "observed_imag": z.imag,
            "observed_abs": abs(z),
            "landau_main_real": landau_phase_main(T, len(gammas), q),
        })

    pp_abs = [x["observed_abs"] for x in scan if x["prime_power"]]
    non_pp_abs = [x["observed_abs"] for x in scan if not x["prime_power"]]

    dyadic = []
    for m in range(1,6):
        q = 2**m
        z = phase_mean(gammas,q)
        main = landau_phase_main(T,len(gammas),q)
        dyadic.append({
            "m": m,
            "q": q,
            "observed_abs": abs(z),
            "observed_real": z.real,
            "observed_imag": z.imag,
            "landau_main_real": main,
            "abs_ratio_to_main": abs(z)/abs(main),
        })

    print(json.dumps({
        "schema": "SPECTRAL_VON_MANGOLDT_PHASE_BANK_V0_1",
        "status": "PASS_NUMERICAL_WITNESS",
        "mpmath_version": mp.__version__,
        "n": len(gammas),
        "T_last": T,
        "dyadic_harmonics": dyadic,
        "base_scan": scan,
        "base_scan_summary": {
            "prime_power_count": len(pp_abs),
            "non_prime_power_count": len(non_pp_abs),
            "min_prime_power_abs": min(pp_abs),
            "max_non_prime_power_abs": max(non_pp_abs),
            "finite_sample_perfect_separation_by_magnitude": min(pp_abs) > max(non_pp_abs),
        },
        "montgomery_dyson_sanity_check": pair_correlation_rmse(gammas),
        "collatz_period3_control": collatz_period3_control(gammas),
        "claims": {
            "landau_formula": "STANDARD",
            "phase_only_form": "CRITICAL_LINE_SPECIALIZATION",
            "finite_scan": "NUMERICAL_WITNESS",
            "rh_proof": False,
            "collatz_proof": False,
            "new_zero_law": False,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
