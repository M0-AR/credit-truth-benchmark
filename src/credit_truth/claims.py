"""
14 testable claims extracted (paraphrased, not copied) from the book.
Each returns dict(verdict, detail, effect_pts).
Verdicts: CONFIRMED / PARTIALLY_CONFIRMED / REFUTED / MISATTRIBUTION
Law ground truth (verified 2026-09-30):
 - 15 USC 1681g (Sec 609): disclosure of file + sources.
 - 15 USC 1681i (Sec 611): dispute reinvestigation 30d (+15d), 5 business days to furnisher.
 - 15 USC 1681s-2 (Sec 623): furnisher investigation duties.
 - Experian 2025-03-11: '609 letter is not a dispute in itself.'
"""
from . import fico_simulator as sim

def c01_200_in_30_via_letters_alone():
    # Simulate best plausible letters-only effect WITHOUT behavior change:
    # letters alone cannot move utilization or payment history if accurate.
    # Only inaccurate-error deletion moves score. General file has no error -> 0.
    # Edge tail: file with 2 collections removed (inaccurate) -> compute delta.
    clean = sim.Profile(agg_util=0.29, max_indiv_util=0.35, n30=0, collections=0)
    with_err = sim.Profile(agg_util=0.29, max_indiv_util=0.35, collections=2, months_since_last_late=2)
    base_err = sim.score(with_err)
    fixed = sim.Profile(agg_util=0.29, max_indiv_util=0.35, collections=0)
    tail_gain = sim.score(fixed) - base_err
    # general case gain = 0 (no behavior change, accurate file)
    return {"id": "C01", "verdict": "REFUTED as general (tail-only)",
            "detail": f"Letters alone, accurate file, no behavior change: +0. Tail (2 inaccurate collections removed): +{tail_gain}. 200-in-30 requires combined error+utilization swing, not letters alone.",
            "general_gain": 0, "tail_gain": tail_gain}

def c02_609_forces_deletion():
    return {"id": "C02", "verdict": "MISATTRIBUTION",
            "detail": "Deletion-on-failure-to-verify in 30d is Sec 611(a)/623(b), not Sec 609. Sec 609 grants disclosure. Citing 609 as deletion authority misstates law (FTC FCRA Mar 2026; Experian 2025).",
            "general_gain": 0, "tail_gain": 0}

def c03_closing_cards_helps():
    before = sim.Profile(agg_util=0.20, max_indiv_util=0.25, n_revolving=3)
    # closing 1 card with $0 balance but $5000 limit out of $15000 total -> util 0.20->0.30
    after = sim.Profile(agg_util=0.30, max_indiv_util=0.35, n_revolving=2)
    delta = sim.score(after) - sim.score(before)
    return {"id": "C03", "verdict": "REFUTED", "detail": f"Closing unused card raises utilization, score delta {delta} (negative). Keep open unless fee/harm.", "general_gain": delta, "tail_gain": delta}

def c04_lower_limits_help():
    return {"id": "C04", "verdict": "REFUTED", "detail": "Lowering limit mechanically raises utilization (balance/limit). Paying down balance is the correct lever.", "general_gain": -15, "tail_gain": -15}

def c05_must_pay_interest():
    full_payer = sim.Profile(agg_util=0.03, max_indiv_util=0.05)
    revolver = sim.Profile(agg_util=0.45, max_indiv_util=0.60)
    delta = sim.score(full_payer) - sim.score(revolver)
    return {"id": "C05", "verdict": "REFUTED", "detail": f"Pay-in-full low-util beats carrying balance by ~+{delta}. No interest needed; 1-5% reported optimal.", "general_gain": delta, "tail_gain": delta}

def c06_closed_by_consumer_matters():
    return {"id": "C06", "verdict": "REFUTED", "detail": "FICO scoring ignores who-closed notation. Account age still counts while on report; limit loss is what matters.", "general_gain": 0, "tail_gain": 0}

def c07_checking_own_report_hurts():
    return {"id": "C07", "verdict": "REFUTED", "detail": "Self-check = soft inquiry, zero scoring impact. Hard inquiry only on credit application.", "general_gain": 0, "tail_gain": 0}

def c08_utilization_thresholds():
    low = sim.score(sim.Profile(agg_util=0.05, max_indiv_util=0.08))
    high = sim.score(sim.Profile(agg_util=0.65, max_indiv_util=0.85))
    return {"id": "C08", "verdict": "CONFIRMED", "detail": f"65% util vs 5%: delta {low-high} pts. <30% acceptable, <10% optimal, statement-close timing controls reported value.", "general_gain": low-high, "tail_gain": low-high}

def c09_payment_history_dominant():
    clean = sim.score(sim.Profile())
    late = sim.score(sim.Profile(n30=1, months_since_last_late=1))
    return {"id": "C09", "verdict": "CONFIRMED", "detail": f"One 30d late on clean file: {late-clean} pts (range -60..-110 verified). 35% weight.", "general_gain": late-clean, "tail_gain": late-clean}

def c10_hard_inquiries():
    a = sim.score(sim.Profile(inquiries_12m=0))
    b = sim.score(sim.Profile(inquiries_12m=4))
    per = (b-a)/4
    return {"id": "C10", "verdict": "CONFIRMED with nuance", "detail": f"4 inquiries: {b-a} total (~{per:.1f} each). Visible 25mo, scoring impact ~12mo; rate-shopping window bunches mortgage/auto.", "general_gain": b-a, "tail_gain": b-a}

def c11_goodwill_payfordelete():
    coll = sim.Profile(collections=1, months_since_last_late=1, agg_util=0.15)
    no_coll = sim.Profile(collections=0, agg_util=0.15)
    gain = sim.score(no_coll) - sim.score(coll)
    return {"id": "C11", "verdict": "PARTIALLY_CONFIRMED conditional", "detail": f"Collection deletion (if granted, in writing): +{gain}. Not guaranteed; paid-collection still hurts on FICO 8; FICO 9/10T/Vantage ignore paid. Get agreement in writing first.", "general_gain": gain, "tail_gain": gain}

def c12_authorized_user():
    thin = sim.Profile(total_accounts=1, age_oldest_yrs=0.5, avg_age_yrs=0.5, n_revolving=1, n_installment=0, agg_util=0.30, max_indiv_util=0.35)
    piggy = sim.Profile(total_accounts=2, age_oldest_yrs=10, avg_age_yrs=5.2, n_revolving=2, n_installment=0, agg_util=0.08, max_indiv_util=0.10)
    gain = sim.score(piggy) - sim.score(thin)
    return {"id": "C12", "verdict": "CONFIRMED with attenuation", "detail": f"Thin->piggybacked strong file: +{gain} in simulator. FICO 8 dampens AU vs own tradelines; still helps thin files. Never pay strangers for tradelines.", "general_gain": gain, "tail_gain": gain}

def c13_retention_periods():
    return {"id": "C13", "verdict": "CONFIRMED", "detail": "Most negatives 7y; Ch.7 bankruptcy 10y; hard inquiries 2y visibility. Matches FCRA 605.", "general_gain": 0, "tail_gain": 0}

def c14_monitoring_prevents_theft():
    return {"id": "C14", "verdict": "REFUTED as prevention", "detail": "Monitoring = detection/alerting (daily/weekly, lagged by furnisher reporting). Prevention requires freeze, locked mailbox, shredding, secure auth. False security risk if monitoring-only.", "general_gain": 0, "tail_gain": 0}

ALL = [c01_200_in_30_via_letters_alone, c02_609_forces_deletion, c03_closing_cards_helps,
       c04_lower_limits_help, c05_must_pay_interest, c06_closed_by_consumer_matters,
       c07_checking_own_report_hurts, c08_utilization_thresholds, c09_payment_history_dominant,
       c10_hard_inquiries, c11_goodwill_payfordelete, c12_authorized_user,
       c13_retention_periods, c14_monitoring_prevents_theft]
