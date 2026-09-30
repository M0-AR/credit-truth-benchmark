import sys
sys.path.insert(0, "src")
from credit_truth import fico_simulator as sim
from credit_truth import claims as C

def test_weights_direction():
    clean = sim.score(sim.Profile())
    assert 750 <= clean <= 850, clean

def test_utilization_monotonic():
    low = sim.score(sim.Profile(agg_util=0.05, max_indiv_util=0.08))
    high = sim.score(sim.Profile(agg_util=0.80, max_indiv_util=0.95))
    assert low - high >= 60, (low, high)

def test_late_payment_asymmetry_ranges():
    clean = sim.score(sim.Profile())
    late = sim.score(sim.Profile(n30=1, months_since_last_late=1))
    drop = clean - late
    assert 50 <= drop <= 120, drop

def test_c01_refuted_as_general():
    r = C.c01_200_in_30_via_letters_alone()
    assert r["general_gain"] == 0
    assert "REFUTED" in r["verdict"]

def test_c03_closing_hurts_or_neutral():
    r = C.c03_closing_cards_helps()
    assert r["general_gain"] <= 0

def test_c08_confirmed():
    r = C.c08_utilization_thresholds()
    assert r["verdict"] == "CONFIRMED" and r["general_gain"] > 30
