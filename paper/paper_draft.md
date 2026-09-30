# Credit-Truth: Verifying “200 Points in 30 Days” and the §609 Loophole Against Public Law and Scoring Guidance
### PhD-ready draft v0.1 — Educational reproduction, 2026-09-30

> Not legal/financial advice. No human subjects. No personal bureau data. Synthetic + public aggregates only.

## Abstract
Popular credit-repair books promise +200 FICO points in <30 days via “§609 letters” without agencies. We operationalize 14 claims from a representative 2021 compendium into falsifiable tests, ground law in the FTC FCRA text (Mar 2026) and bureau guidance (Experian 2025-03-11), ground scoring in myFICO weights and Experian/FICO 2025–26 aggregates, and test via a transparent educational simulator plus public datasets. Result: the headline promise is **refuted as a general method**; §609 is misattributed (disclosure, not dispute — that is §611/§623); 8 sub-claims confirm with nuance (utilization, payment history, retention periods); 5 refute; 2 partially confirm conditionally (goodwill/pay-for-delete, authorized-user with FICO-8 attenuation). We surface 7 hidden patterns (statement-date gap, per-card vs aggregate, late asymmetry, scorecard non-linearity, 609→611 pipeline, knowledge-gap moderator, utilization cliffs) as PhD extensions. All code, seeds, and sources are released for one-command reproduction.

**Keywords:** consumer credit, FICO, FCRA §§609/611/623, credit-report accuracy, reproducibility, financial education.

## 1. Introduction
1.1 The promise: 200-in-30, “secrets agencies won’t tell,” 12 templates + goodwill/cease-desist.
1.2 Why it matters: avg FICO 713–714 (2025–26), 83% prioritize score (FICO/Harris Spring ’26), yet 67% hold income-myth; CFPB complaints 4.6M (2025, per practitioner compilation — verify via CFPB API); $3.5B/yr repair-scam cost (FTC, via secondary — needs primary citation).
1.3 Research questions: RQ1 (law), RQ2 (scoring velocity), RQ3 (which sub-claims survive), RQ4 (hidden moderators).
1.4 Contributions: (a) claim→test mapping, (b) transparent simulator, (c) public-aggregate benchmark, (d) hidden-pattern catalog, (e) reproducible Docker artifact.

## 2. Legal ground truth (verified 2026-09-30)
- **§609 (15 USC §1681g):** consumer disclosure — all info in file, sources, recipients, rights summary. Source: Federal Reserve Reg V text; CFPB Reg V App O 2026 cap $16; FTC FCRA Mar 2026 PDF pp.47ff.
- **§611 (15 USC §1681i):** dispute reinvestigation — 30 days (+15 if consumer supplies additional info), CRA notifies furnisher within 5 business days, reports findings within 5 days post-investigation. Source: FTC §611 PDF; Experian “609 request isn’t actually a dispute letter.”
- **§623 (15 USC §1681s-2(b)) + Furnisher Rule 660.4:** investigate, review all relevant info, report, correct/delete if unverifiable; frivolous/irrelevant + credit-repair-form exceptions.
- **Implication:** “cite §609 + demand deletion in 30 days” misstates authority. Valid disputes invoke §611/§623 with specificity + documentation; bureaus may label vague/template floods frivolous.
- **Related:** FDCPA cease-communication, FCBA billing-error (100-mile/$50 hidden-gem nuance needs primary verification — flagged as unverified in book), state privacy overlays.

## 3. Scoring ground truth
- **Weights (myFICO, fetched 2026-09-30):** 35/30/15/10/10; profile-dependent (12 scorecards: bankruptcy/delinquency/thin/age buckets — per book’s list, consistent with FICO community docs; treat as approximate).
- **Bands (public):** 300–579 poor, 580–669 fair, 670–739 good, 740–799 very good, 800–850 exceptional (Experian/FICO convergent).
- **Utilization table (Experian Sep 2025):** national 29%; poor 79%, fair 61%, good 39%, very good 15%, exceptional 7%. Optimal 1–9%, acceptable <30% (multiple 2026 triangulations).
- **Velocity (triangulated 2026):** 10–20/mo ×6mo deliberate, then 5–10/mo; 100/6mo feasible from 580–680 with errors+utilization fixes; 30–60 in one cycle from 50%+→<10% common; 200/30 tail-only.
- **Retention:** 7y most negatives, 10y Ch.7, 2y inquiry visibility (~12mo scoring weight).

## 4. Method
4.1 Claim extraction: paraphrase 14 claims (C01–C14), avoid reproducing copyrighted templates verbatim.
4.2 Simulator (§ ): transparent penalties calibrated to ranges above; seed 42; NOT FICO.
4.3 Cohorts (n=synthetic profiles, not humans): high-util paydown, error deletion, combined tail, thin→AU, clean→30d-late, AZEO vs 30%.
4.4 Public data: FICO Insights, Experian aggregates, CFPB complaints (manual CSV), Fed SCF, Kaggle synthetic (CC0/CC-BY-SA) for distributional plausibility — never personal files.
4.5 Live check: AnnualCreditReport.com weekly; user-entered utilization into notebook; FRED/CFPB rate spreads for economic significance ($50k lifetime example on $400k/30y 720→760 — practitioner calc, to be recomputed from FRED in future work).
4.6 Ethics: no false-dispute instructions, no fraud-alert abuse, no paid-tradeline facilitation; NFCC/FCCA referral.

## 5. Results
| ID | Verdict | Effect (sim pts) | Basis |
|----|---------|------------------|-------|
| C01 200-in-30 letters-alone | REFUTED general | 0 general; tail ~+80–120 combined | §5.1 cohorts |
| C02 §609 forces deletion | MISATTRIBUTION | 0 | §2 |
| C03 closing helps | REFUTED | –15 | limit-loss |
| C04 lower limits help | REFUTED | –15 | util arithmetic |
| C05 must pay interest | REFUTED | +55 full-payer advantage | 1–9% optimal |
| C06 closed-by-consumer | REFUTED | 0 | scoring ignores notation |
| C07 self-check hurts | REFUTED | 0 | soft inquiry |
| C08 util thresholds+timing | CONFIRMED | +70–110 | cliffs + statement-close |
| C09 payment 35% | CONFIRMED | –80 clean 30d | asymmetry |
| C10 inquiries | CONFIRMED nuanced | –5 each | 25mo vis / 12mo weight |
| C11 goodwill/pay-delete | PARTIAL conditional | +40–70 if granted | written agreement; FICO8 vs 9/10T |
| C12 AU piggyback | CONFIRMED attenuated | +30–50 thin | FICO8 dampening |
| C13 retention | CONFIRMED | — | FCRA 605 |
| C14 monitoring prevents | REFUTED as prevention | — | detection only |
Run `python -m credit_truth.evaluate` to reproduce numbers (directional, not guarantees).

## 6. Hidden patterns (PhD contributions)
P1 Statement-vs-due gap + AZEO (+20–50 vs 30%).
P2 Per-card penalty (one 90%+ = –20 even if aggregate low).
P3 Late asymmetry + decay (×1.0 <12mo, ×0.7 12–24mo, ×0.45 ≥24mo; clean files hit harder).
P4 Scorecard non-linearity (thin-file –20, 12-card segmentation proxy).
P5 609→611 pipeline (disclosure enables dispute; zero direct effect).
P6 Knowledge-gap moderator (Homonoff et al. NBER w26048: FICO-knowledge RCT ↓ past-due; Brown et al. financial-education ↑ score; Agarwal et al. U-shape mistakes).
P7 Utilization cliffs (0% –12, 1–9% 0, 10–29% –15, 30–49% –40, 50–74% –70, 75%+ –110).

## 7. Threats & limits
Simulator ≠ FICO; VantageScore differs (reported but not modeled); CFPB 4.6M + $3.5B scam figures need primary-source re-verification; mortgage FICO 10T transition ongoing; no longitudinal panel; synthetic cohorts lack selection effects; economic-significance calc is illustrative.

## 8. Related work
Hoadley (2020, arXiv:2003.00280) QP solution to FICO problem + PILE constraints; Berger & Frame small-business scoring; Brown et al. (RFS) youth debt + education; Agarwal et al. age-of-reason U-shape; Homonoff–O’Brien–Sussman (NBER w26048/SSRN 3129075) FICO-knowledge field experiment (400k borrowers); Róna-Tas off-label use; Cortés ODR.

## 9. Conclusion + publish path
Books mix valid fundamentals (pay on time, utilization, §611 disputes, goodwill/AU conditionally) with a headline promise and legal misattribution that fail verification. Next: (a) CFPB complaint-panel longitudinal study of dispute outcomes, (b) RCT on statement-date nudge, (c) AU attenuation across FICO versions, (d) cross-model (FICO vs Vantage) comparison. All require IRB + no personal data without consent.

## References (retrieved 2026-09-30 unless noted)
- FTC FCRA Mar 2026 PDF; Fed §609 page; CFPB Reg V App O 2026 ($16); FTC §611 PDF + furnisher guidance (623(b)/660.4).
- myFICO “What’s in my FICO Scores” (35/30/15/10/10).
- Experian Ask Experian “What is a 609 dispute letter?” (Jim Akin, 2025-03-11).
- Experian “Average credit score 713” (Mar 30 2026, Sep 2025 data); FICO Insights Spring ’26 (avg 714, 48.1% ≥750).
- Practitioner triangulations (SaveCompare, Firstcard, HL Hunt, ScoreMachine, Chivam) — treated as secondary, ranges only.
- OpenAlex/Crossref: Hoadley 2020; Brown et al. 2016; Agarwal et al. 2009; Homonoff et al. 2018/2019; Berger & Frame; Róna-Tas 2017.
- Kaggle: Realistic Credit Scoring (CC0), 3M Enterprise Bank Records (CC BY-SA 4.0) — synthetic.
- AnnualCreditReport.com; NFCC/FCCA counselor lists.
