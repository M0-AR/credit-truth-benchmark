"""Public-aggregate loaders only. No personal bureau pulls. Retrieval dates recorded."""
PUBLIC_AGGREGATES = {
    "avg_fico_2025_experian": {"value": 713, "source": "https://www.experian.com/blogs/ask-experian/what-is-the-average-credit-score-in-the-u-s/", "retrieved": "2026-09-30", "note": "Sep 2025 data, published Mar 30 2026, first decline since 2013"},
    "avg_fico_spring26_fico": {"value": 714, "source": "https://investors.fico.com/news-releases/news-release-details/ficor-score-credit-insights-report-average-fico-score-dips-714", "retrieved": "2026-09-30"},
    "avg_util_2025": {"value": 0.29, "source": "Experian 2025 table", "retrieved": "2026-09-30"},
    "util_by_band": {
        "poor_300_579": 0.79, "fair_580_669": 0.61, "good_670_739": 0.39,
        "verygood_740_799": 0.15, "exceptional_800_850": 0.07,
        "source": "Experian Sep 2025",
    },
    "fico_weights": {"payment": 0.35, "amounts_owed": 0.30, "length": 0.15, "new_credit": 0.10, "mix": 0.10,
                     "source": "https://www.myfico.com/credit-education/whats-in-your-credit-score", "retrieved": "2026-09-30"},
    "kaggle_synthetic": [
        "chaitanyajamble/realistic-credit-scoring-and-loan-default-prediction (CC0, FICO-like)",
        "hamziai/3million-enterprise-bank-records-ultimate-fraud (CC BY-SA 4.0, synthetic)",
    ],
    "law": {
        "sec609_disclosure": "15 USC 1681g — https://www.federalreserve.gov/frrs/regulations/section-609-disclosures-to-consumers.htm",
        "sec611_dispute": "15 USC 1681i — 30d (+15d), 5 business days to furnisher",
        "ftc_fcra_mar2026": "https://www.ftc.gov/system/files/ftc_gov/pdf/fcra-march-2026.pdf",
        "experian_609_blog": "https://www.experian.com/blogs/ask-experian/what-is-a-609-dispute-letter/ (2025-03-11)",
    },
}

def get_public_aggregates():
    return PUBLIC_AGGREGATES

def fetch_public(out_dir="data/raw"):
    """Keyless best-effort fetch. Writes manual-fetch checklist if offline."""
    import os
    os.makedirs(out_dir, exist_ok=True)
    checklist = os.path.join(out_dir, "MANUAL_FETCH_CHECKLIST.md")
    with open(checklist, "w") as f:
        f.write("# Manual public-data checklist (no personal data)\n\n"
                "1. AnnualCreditReport.com — free weekly reports (verify your own file manually, do not upload here).\n"
                "2. CFPB Complaint Database — https://www.consumerfinance.gov/data-research/consumer-complaints/ — download CSV to data/raw/.\n"
                "3. Federal Reserve SCF — https://www.federalreserve.gov/econres/scfindex.htm\n"
                "4. FICO Insights Spring 26 — avg 714 link above.\n"
                "5. Kaggle synthetic sets above (require kaggle API auth for download).\n")
    return checklist
