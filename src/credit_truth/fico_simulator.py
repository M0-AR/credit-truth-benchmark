"""
Educational FICO-like simulator — TRANSPARENT, DIRECTIONAL, NOT FICO.
Calibrated to PUBLIC tables only (myFICO weights 35/30/15/10/10,
Experian 2025 utilization-by-band, practitioner late-payment ranges).
Proprietary FICO formula is unpublished; this mimics direction + magnitude
for benchmarking book claims, not for predicting any real score.
"""
from dataclasses import dataclass

@dataclass
class Profile:
    # payment
    n30: int = 0
    n60: int = 0
    n90: int = 0
    collections: int = 0
    chargeoffs: int = 0
    bankruptcy: bool = False
    months_since_last_late: int = 999  # large = long ago / never
    # utilization (0..1)
    agg_util: float = 0.05
    max_indiv_util: float = 0.10
    # length
    age_oldest_yrs: float = 8.0
    avg_age_yrs: float = 5.0
    total_accounts: int = 6
    # new credit
    inquiries_12m: int = 0
    new_accounts_12m: int = 0
    # mix
    n_revolving: int = 2
    n_installment: int = 1
    has_mortgage: bool = False

def _decay_factor(months_since: int) -> float:
    # verified pattern: lates hurt less after 12mo, much less after 24mo
    if months_since >= 24:
        return 0.45
    if months_since >= 12:
        return 0.70
    return 1.0

def utilization_penalty(agg: float, max_indiv: float) -> int:
    if agg <= 0.001:
        base = -12  # no activity slightly suboptimal (verified: 0% slightly negative)
    elif agg <= 0.09:
        base = 0
    elif agg <= 0.29:
        base = -15
    elif agg <= 0.49:
        base = -40
    elif agg <= 0.74:
        base = -70
    else:
        base = -110
    extra = 0
    if max_indiv >= 0.90:
        extra = -20
    elif max_indiv >= 0.50:
        extra = -10
    return base + extra

def payment_penalty(p: Profile) -> int:
    d = _decay_factor(p.months_since_last_late)
    # asymmetry: clean files lose more — approximated by scaling first-late
    # if no prior derog, full hit; else attenuated (scorecard segmentation proxy)
    clean = (p.n30 + p.n60 + p.n90 + p.collections + p.chargeoffs == 1 and not p.bankruptcy)
    scale = 1.0 if clean else 0.75
    pen = 0
    if p.n30:
        pen += int(-80 * scale * d * min(p.n30, 2))  # cap stacking
    if p.n60:
        pen += int(-105 * scale * d * min(p.n60, 2))
    if p.n90:
        pen += int(-125 * scale * d * min(p.n90, 2))
    if p.collections:
        pen += int(-70 * d * min(p.collections, 3))
    if p.chargeoffs:
        pen += int(-135 * d * min(p.chargeoffs, 2))
    if p.bankruptcy:
        pen += -190  # 7-10y, -150 to -240 range; midpoint
    return pen

def length_penalty(p: Profile) -> int:
    pen = 0
    if p.avg_age_yrs < 1:
        pen -= 40
    elif p.avg_age_yrs < 2:
        pen -= 25
    elif p.avg_age_yrs < 5:
        pen -= 10
    if p.age_oldest_yrs < 2:
        pen -= 10
    if p.total_accounts < 3:
        pen -= 20  # thin file
    return pen

def new_credit_penalty(p: Profile) -> int:
    return min(p.inquiries_12m, 5) * -5 + min(p.new_accounts_12m, 3) * -8

def mix_adjustment(p: Profile) -> int:
    types = (1 if p.n_revolving > 0 else 0) + (1 if p.n_installment > 0 else 0) + (1 if p.has_mortgage else 0)
    if types <= 1:
        return -15
    if types >= 3:
        return 10
    return 0

def score(p: Profile) -> int:
    s = 850
    s += payment_penalty(p)
    s += utilization_penalty(p.agg_util, p.max_indiv_util)
    s += length_penalty(p)
    s += new_credit_penalty(p)
    s += mix_adjustment(p)
    return max(300, min(850, s))

def explain(p: Profile) -> dict:
    return {
        "payment": payment_penalty(p),
        "utilization": utilization_penalty(p.agg_util, p.max_indiv_util),
        "length_thin": length_penalty(p),
        "new_credit": new_credit_penalty(p),
        "mix": mix_adjustment(p),
        "total": score(p),
    }
