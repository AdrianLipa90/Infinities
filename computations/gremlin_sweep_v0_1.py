from __future__ import annotations

from dataclasses import dataclass, asdict
from itertools import combinations
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

BASELINE = ("SHIFT", "SCALE", "BRANCH", "FACTOR", "INVERT")
EXTENSIONS = ("AVERAGE", "TRANSFORM", "POWERSET", "STOCHASTIC")
UNIVERSE = BASELINE + EXTENSIONS

@dataclass(frozen=True)
class Case:
    id: str
    name: str
    phase: str
    representations: tuple[tuple[str, ...], ...]
    completion: str
    invariants: tuple[str, ...]
    half_status: str
    fixed_point: str | None = None
    note: str = ""

def C(id, name, phase, reps, completion, invariants, half_status="NA", fixed_point=None, note=""):
    return Case(
        id=id, name=name, phase=phase,
        representations=tuple(tuple(r) for r in reps),
        completion=completion,
        invariants=tuple(invariants),
        half_status=half_status,
        fixed_point=fixed_point,
        note=note,
    )

CASES = (
    C("I01","N equipotent with 2N","training",[("SCALE",)],"CARDINAL",
      ("CARDINALITY","SELF_EMBEDDING")),
    C("I02","unilateral Hilbert shift","training",[("SHIFT",)],"HILBERT_NORM",
      ("FREDHOLM_INDEX","FINITE_DEFECT")),
    C("I03","geometric series","training",[("SCALE",)],"ARCHIMEDEAN",
      ("FINITE_LIMIT","CONTRACTION")),
    C("I04","harmonic divergence","training",[("SCALE",)],"ARCHIMEDEAN",
      ("DIVERGENCE_RATE",)),
    C("I05","alternating harmonic series","training",[("SCALE","BRANCH")],"ARCHIMEDEAN",
      ("CONDITIONAL_CONVERGENCE","SIGN_BALANCE")),
    C("I06","Riemann rearrangement","training",[("SHIFT",)],"ORDER_SENSITIVE",
      ("ORDER_DEFECT",)),
    C("I07","0.999... = 1","training",[("SCALE",)],"ARCHIMEDEAN",
      ("COMPLETION_IDENTITY",)),
    C("I08","ordinal asymmetry 1+omega != omega+1","training",[("SHIFT",)],"ORDER_TOPOLOGY",
      ("NONCOMMUTATIVITY",)),
    C("I09","epsilon_0 fixed point","training",[("SCALE",)],"ORDER_TOPOLOGY",
      ("FIXED_POINT",),"COUNTEREXAMPLE","epsilon_0",
      "Fixed point is not a normalized half seam."),
    C("I10","middle-third Cantor set","training",[("SCALE","BRANCH")],"HAUSDORFF",
      ("SELF_SIMILARITY","DIMENSION","SHANNON"),"CONFIRMED","1/2",
      "Equal binary branch weights give p0=p1=1/2."),
    C("I11","Gabriel horn","training",[("SCALE",)],"IMPROPER_INTEGRAL",
      ("VOLUME_AREA_SPLIT","THRESHOLD")),
    C("I12","Euler product for zeta","training",[("FACTOR","SCALE")],"ABSOLUTE_CONVERGENCE",
      ("PRIME_FACTORIZATION","DIRICHLET_EULER_EQUIVALENCE")),
    C("I13","telescoping infinite product","training",[("FACTOR","SCALE")],"ARCHIMEDEAN",
      ("PRODUCT_TO_ZERO","RECIPROCAL_ESCAPE")),
    C("I14","continued fraction sqrt(2)","training",[("SHIFT","INVERT")],"ARCHIMEDEAN",
      ("ATTRACTING_FIXED_POINT",),"COUNTEREXAMPLE","sqrt(2)",
      "The natural attracting fixed point is sqrt(2), not 1/2."),
    C("I15","Cantor fractal dimension","training",[("SCALE","BRANCH")],"HAUSDORFF",
      ("DIMENSION","SHANNON"),"CONFIRMED","1/2"),
    C("I16","reciprocal inversion z -> 1/z","training",[("INVERT",)],"RIEMANN_SPHERE",
      ("INVOLUTION","ZERO_INFINITY_DUALITY")),
    C("I17","anti-holomorphic inversion z -> 1/conj(z)","training",[("INVERT",)],"RIEMANN_SPHERE",
      ("INVOLUTION","UNIT_CIRCLE_FIXED_SET"),"CONFIRMED","1/2",
      "After radial compactification q=R/(1+R), inversion R->1/R gives q->1-q."),
    C("I18","2-adic geometric series","training",[("SCALE",)],"P_ADIC_2",
      ("METRIC_DEPENDENT_LIMIT",),"COUNTEREXAMPLE","-1",
      "1+2+4+... converges to -1 in Q_2."),
    C("I19","infinite-dimensional l2 with finite norm","training",[("SHIFT",)],"HILBERT_NORM",
      ("FINITE_NORM","INFINITE_DIMENSION")),

    C("H01","Basel series","holdout",[("SCALE",)],"ARCHIMEDEAN",
      ("FINITE_LIMIT",)),
    C("H02","Koch curve","holdout",[("SCALE","BRANCH")],"HAUSDORFF",
      ("INFINITE_LENGTH","FINITE_AREA","DIMENSION")),
    C("H03","Sierpinski triangle","holdout",[("SCALE","BRANCH")],"HAUSDORFF",
      ("SELF_SIMILARITY","DIMENSION")),
    C("H04","Cesaro summation of Grandi series","holdout",[("AVERAGE",)],"CESARO",
      ("REGULARIZED_LIMIT",),"CONFIRMED","1/2",
      "Cesaro means converge to 1/2, but by averaging rather than inversion."),
    C("H05","Fourier series / l2 spectral expansion","holdout",[("TRANSFORM",)],"HILBERT_NORM",
      ("SPECTRAL_DECOMPOSITION","PARSEVAL")),
    C("H06","Cantor theorem power set growth","holdout",[("POWERSET",)],"CARDINAL",
      ("STRICT_CARDINAL_GROWTH",)),
    C("H07","simple random walk recurrence/transience","holdout",[("STOCHASTIC","BRANCH")],"PROBABILITY",
      ("RECURRENCE","ESCAPE_PROBABILITY")),
    C("H08","Newton iteration for sqrt(2)","holdout",[("SCALE","INVERT")],"ARCHIMEDEAN",
      ("ATTRACTING_FIXED_POINT",),"COUNTEREXAMPLE","sqrt(2)"),
    C("H09","golden-ratio continued fraction","holdout",[("SHIFT","INVERT")],"ARCHIMEDEAN",
      ("ATTRACTING_FIXED_POINT",),"COUNTEREXAMPLE","phi"),
    C("H10","factorial growth n!","holdout",[("FACTOR","SCALE")],"ARCHIMEDEAN",
      ("SUPEREXPONENTIAL_GROWTH",)),
    C("H11","prime-counting function pi(x)","holdout",[("FACTOR",)],"ARCHIMEDEAN",
      ("ASYMPTOTIC_DENSITY",)),
    C("H12","Euler-Mascheroni renormalized harmonic sequence","holdout",[("SCALE",)],"ARCHIMEDEAN",
      ("FINITE_REMAINDER","RENORMALIZED_DIFFERENCE")),
    C("H13","Jacobi theta modular inversion","holdout",[("TRANSFORM","INVERT")],"MODULAR",
      ("DUALITY","MODULAR_INVERSION")),
)

def covered(case: Case, vocabulary: frozenset[str]) -> bool:
    return any(frozenset(rep) <= vocabulary for rep in case.representations)

def coverage(vocabulary, phase=None):
    v = frozenset(vocabulary)
    subset = [c for c in CASES if phase is None or c.phase == phase]
    ok = [c for c in subset if covered(c, v)]
    miss = [c for c in subset if not covered(c, v)]
    return ok, miss

def minimal_vocabularies():
    universe = tuple(UNIVERSE)
    answers = []
    for k in range(len(universe) + 1):
        for combo in combinations(universe, k):
            v = frozenset(combo)
            if all(covered(c, v) for c in CASES):
                answers.append(tuple(combo))
        if answers:
            break
    return answers

def loo_losses(vocabulary):
    base_ok, _ = coverage(vocabulary)
    n0 = len(base_ok)
    out = {}
    for op in vocabulary:
        v = [x for x in vocabulary if x != op]
        ok, miss = coverage(v)
        out[op] = {
            "covered_after_removal": len(ok),
            "loss": n0 - len(ok),
            "newly_uncovered": [c.id for c in miss if covered(c, frozenset(vocabulary))],
        }
    return out

def fingerprint(case: Case):
    rep = min(case.representations, key=lambda x: (len(x), x))
    return {
        "generators": list(rep),
        "completion": case.completion,
        "invariants": list(case.invariants),
    }

def fingerprint_classes():
    groups = defaultdict(list)
    for c in CASES:
        fp = fingerprint(c)
        key = json.dumps(fp, sort_keys=True, separators=(",", ":"))
        groups[key].append(c.id)
    out = []
    for key, ids in groups.items():
        if len(ids) > 1:
            out.append({"fingerprint": json.loads(key), "case_ids": ids, "size": len(ids)})
    return sorted(out, key=lambda x: (-x["size"], x["case_ids"]))

def main():
    baseline_ok_train, baseline_miss_train = coverage(BASELINE, "training")
    baseline_ok_hold, baseline_miss_hold = coverage(BASELINE, "holdout")
    baseline_ok_all, baseline_miss_all = coverage(BASELINE)
    mins = minimal_vocabularies()

    half_confirmed = [c for c in CASES if c.half_status == "CONFIRMED"]
    half_counter = [c for c in CASES if c.half_status == "COUNTEREXAMPLE"]

    missing_counter = Counter()
    for c in baseline_miss_all:
        required = set(min(c.representations, key=lambda x: (len(x), x)))
        for op in required - set(BASELINE):
            missing_counter[op] += 1

    result = {
        "schema": "GREMLIN_INFINITIES_SWEEP_RESULT_V0_1",
        "catalog_size": len(CASES),
        "training_size": sum(c.phase == "training" for c in CASES),
        "holdout_size": sum(c.phase == "holdout" for c in CASES),
        "baseline_vocabulary": list(BASELINE),
        "extension_candidates": list(EXTENSIONS),
        "baseline_training": {
            "covered": len(baseline_ok_train),
            "total": len(baseline_ok_train) + len(baseline_miss_train),
            "coverage": len(baseline_ok_train)/(len(baseline_ok_train)+len(baseline_miss_train)),
            "uncovered": [c.id for c in baseline_miss_train],
        },
        "baseline_holdout": {
            "covered": len(baseline_ok_hold),
            "total": len(baseline_ok_hold) + len(baseline_miss_hold),
            "coverage": len(baseline_ok_hold)/(len(baseline_ok_hold)+len(baseline_miss_hold)),
            "uncovered": [c.id for c in baseline_miss_hold],
        },
        "baseline_all": {
            "covered": len(baseline_ok_all),
            "total": len(CASES),
            "coverage": len(baseline_ok_all)/len(CASES),
            "uncovered": [c.id for c in baseline_miss_all],
            "missing_operator_counts": dict(sorted(missing_counter.items())),
        },
        "minimal_vocabulary_size_under_catalog_schema": len(mins[0]) if mins else None,
        "minimal_vocabularies_under_catalog_schema": [list(x) for x in mins],
        "leave_one_operator_out_full_universe": loo_losses(UNIVERSE),
        "half_seam_test": {
            "universal_half_hypothesis": "FAIL" if half_counter else "NOT_FALSIFIED",
            "confirmed_case_ids": [c.id for c in half_confirmed],
            "counterexample_case_ids": [c.id for c in half_counter],
            "scope_note": "This tests the catalogued natural fixed points/seams only; it is not a theorem about all possible representations.",
        },
        "equivalence_classes_exact_fingerprint": fingerprint_classes(),
        "claims": {
            "baseline_fits_training_catalog": "PASS" if not baseline_miss_train else "FAIL",
            "baseline_generalizes_to_all_holdouts": "PASS" if not baseline_miss_hold else "FAIL",
            "universal_half_seam": "FAIL" if half_counter else "NOT_FALSIFIED",
            "finite_catalog_extended_grammar": "PASS" if mins else "FAIL",
            "minimality_is_mathematical_theorem": "NO",
            "rh_proof": "NO",
            "collatz_proof": "NO",
        },
        "cases": [asdict(c) | {"fingerprint": fingerprint(c)} for c in CASES],
    }

    payload = json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    result["result_sha256_without_self_hash"] = hashlib.sha256(payload).hexdigest()

    out = Path(__file__).with_name("gremlin_sweep_v0_1_result.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"catalog={len(CASES)}")
    print(f"training baseline: {len(baseline_ok_train)}/{len(baseline_ok_train)+len(baseline_miss_train)}")
    print(f"holdout baseline: {len(baseline_ok_hold)}/{len(baseline_ok_hold)+len(baseline_miss_hold)}")
    print("holdout uncovered:", ",".join(c.id for c in baseline_miss_hold))
    print("missing ops:", dict(sorted(missing_counter.items())))
    print("minimal size:", len(mins[0]))
    print("minimal vocabularies:", mins)
    print("universal half:", result["half_seam_test"]["universal_half_hypothesis"])
    print("half counterexamples:", ",".join(c.id for c in half_counter))
    print("sha256:", result["result_sha256_without_self_hash"])

if __name__ == "__main__":
    main()
