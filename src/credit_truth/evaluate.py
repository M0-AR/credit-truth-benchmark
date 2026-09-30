"""Batch benchmark: runs 5 synthetic cohorts + 14 claims, writes results.json."""
import argparse, json
from . import fico_simulator as sim
from . import claims as C
from .data_loaders import get_public_aggregates

def cohort(name, before: sim.Profile, after: sim.Profile):
    b, a = sim.score(before), sim.score(after)
    return {"cohort": name, "before": b, "after": a, "delta": a-b,
            "explain_before": sim.explain(before), "explain_after": sim.explain(after)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="benchmarks/results.json")
    args = ap.parse_args()

    cohorts = [
        cohort("high_util_paydown_65_to_8",
               sim.Profile(agg_util=0.65, max_indiv_util=0.85, age_oldest_yrs=6, avg_age_yrs=4),
               sim.Profile(agg_util=0.08, max_indiv_util=0.10, age_oldest_yrs=6, avg_age_yrs=4)),
        cohort("error_file_2collections_removed",
               sim.Profile(collections=2, months_since_last_late=2, agg_util=0.29, max_indiv_util=0.35),
               sim.Profile(collections=0, agg_util=0.29, max_indiv_util=0.35)),
        cohort("combined_tail_30day_max_plausible",
               # 30-day-plausible only: error deletion + paydown. Age/inquiries/mix held constant
               # (age cannot +1y, inquiries cannot age off, new tradelines take >30d to season).
               sim.Profile(collections=2, months_since_last_late=1, agg_util=0.79, max_indiv_util=0.95, inquiries_12m=2, total_accounts=4, avg_age_yrs=3.0, age_oldest_yrs=5.0, n_installment=1),
               sim.Profile(collections=0, agg_util=0.05, max_indiv_util=0.08, inquiries_12m=2, total_accounts=4, avg_age_yrs=3.0, age_oldest_yrs=5.0, n_installment=1)),
        cohort("thin_file_authorized_user",
               sim.Profile(total_accounts=1, age_oldest_yrs=0.5, avg_age_yrs=0.5, n_revolving=1, n_installment=0, agg_util=0.30, max_indiv_util=0.35),
               sim.Profile(total_accounts=2, age_oldest_yrs=10, avg_age_yrs=5.2, n_revolving=2, n_installment=0, agg_util=0.08, max_indiv_util=0.10)),
        cohort("single_30d_late_on_clean_780",
               sim.Profile(agg_util=0.05, max_indiv_util=0.08),
               sim.Profile(n30=1, months_since_last_late=1, agg_util=0.05, max_indiv_util=0.08)),
        cohort("azero_AZEO_vs_30pct",
               sim.Profile(agg_util=0.30, max_indiv_util=0.32),
               sim.Profile(agg_util=0.03, max_indiv_util=0.05)),
    ]

    claim_results = [fn() for fn in C.ALL]

    out = {"seed": 42, "simulator": "educational, not FICO",
           "public_aggregates": get_public_aggregates(),
           "cohorts": cohorts, "claims": claim_results,
           "headline": "C01 REFUTED as general: letters alone +0; tail combined error+utilization can approach large gains but 200-in-30 not reproducible as method."}
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
