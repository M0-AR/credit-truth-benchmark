# SOURCES — every factual claim → URL + retrieval date

## Law (retrieved 2026-09-30)
- FTC FCRA March 2026 PDF (§609 p.47, §611 p.59): https://www.ftc.gov/system/files/ftc_gov/pdf/fcra-march-2026.pdf — via websearch
- Fed §609 Disclosures page: https://www.federalreserve.gov/frrs/regulations/section-609-disclosures-to-consumers.htm — via websearch
- CFPB Reg V App O 2026 ($16 cap): https://www.federalregister.gov/documents/2025/12/15/2025-22772/fair-credit-reporting-act-disclosures — via websearch
- FTC furnisher duties (623b/611a, 30d +15d, 5 business days): https://www.ftc.gov/system/files/ftc_gov/pdf/698A_Consumer%20Reports_2025_508.pdf — via websearch
- FTC §611 procedure PDF: https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/fair-credit-reporting-act-611.pdf — via duckduckgo_search
- Experian 609 blog (Akin, 2025-03-11, “609 request isn't actually a dispute”): https://www.experian.com/blogs/ask-experian/what-is-a-609-dispute-letter/ — fetched 2026-09-30 via free-search_fetch

## Scoring (retrieved 2026-09-30)
- myFICO weights 35/30/15/10/10: https://www.myfico.com/credit-education/whats-in-your-credit-score — fetched via free-search_fetch
- Experian avg 713 + util table (29% natl; 79/61/39/15/7 by band): https://www.experian.com/blogs/ask-experian/what-is-the-average-credit-score-in-the-u-s/ — via agent-reach_search
- FICO Insights Spring 26 avg 714, 48.1% ≥750: https://investors.fico.com/news-releases/news-release-details/ficor-score-credit-insights-report-average-fico-score-dips-714 — via agent-reach_search
- Velocity triangulations (10–20/mo, 100/6mo conditional, 30–60/cycle util): SaveCompare/Firstcard/HL Hunt/ScoreMachine/Chivam — via agent-reach_search (secondary, ranges only)

## Academic (via paper-search + openresearch 2026-09-30)
- Hoadley arXiv:2003.00280 QP FICO problem
- Brown et al. RFS financial education & youth debt (OpenAlex W3125824752)
- Agarwal et al. Age of Reason U-shape (OpenAlex W3126071966)
- Homonoff et al. NBER w26048 / SSRN 3129075 FICO-knowledge RCT (400k borrowers)
- Berger & Frame small-business scoring; Róna-Tas off-label use

## Public datasets
- Kaggle search_everything 2026-09-30: chaitanyajamble/realistic-credit-scoring-and-loan-default-prediction (CC0); hamziai/3million-enterprise-bank-records-ultimate-fraud (CC BY-SA 4.0)
- Wiki search: Credit score in the United States; Credit bureau; Credit history
- AnnualCreditReport.com; CFPB complaints; Fed SCF; FRED (manual checklist in data_loaders.fetch_public)

## Search-method compliance
One search at a time (no parallel websearch); searxng unreachable (network error logged); openresearch web_search timed out once (logged); gsd_websearch empty (logged). All failures recorded, no hidden retries in parallel.

## README / preview / demo craft (retrieved 2026-09-30, sequential, different keywords)
- websearch: Standard-README spec (Title/Banner/Badges/TOC order) + awesome-readme (+35% star lift w/ hero, GIF above fold) + 2026 audit (800–1500 words, 4 badges, 3-step quickstart, star history)
- free-search_search: MDN video/GIF/accessibility + open-source etiquette docs
- duckduckgo_search: GitHub video workarounds — MP4 via Issue drag-drop URL, YouTube thumbnail link, GIF inline, AVIF/WebP silent loops (rapidevelopers, StackOverflow Q4279611, GeeksforGeeks, george-hawkins/video-in-github-markdown, glideo.app)
- agent-reach_search: shields.io MIT/Apache-2.0 dual-license + badge hosting (1.6B/mo) + live test-count badge pattern
- wiki_search: README (GNU history), Open weights, FOSS lists
- kaggle_search_everything: documentation notebooks visualization examples
- paper-search: reproducible research / open-science software testing (Milewicz, Dorner, QIIME2, Quantum ESPRESSO)
- openresearch_search_openalex: contributor signals (Qiu et al. 2019), RAPID geoscience sharing, Ten Simple Rules Git/GitHub (Pérez-Riverol et al. 2016)
- gsd_websearch: empty (logged) · superpowers_semantic_search: writing-skills docs · gitmcp badges/shields: badge URL conventions + self-hosting + service tests
- Playwright MCP verified 2026-09-30: `browser_navigate http://localhost:8000/preview.html` → title OK, full snapshot OK (1 favicon 404, non-blocking); `take_screenshot fullPage` → `docs/screenshot-preview.png` 950K
- Demo assets generated from verified code (not hand-drawn): `benchmarks/util_cliffs.png` [838,850,835,810,770,730,720], `late_decay.png` [80,80,56,56,36,36], `claims_waterfall.png`, `docs/demo.gif` 99K + `docs/demo.mp4` 15K (ffmpeg yuv420p); `preview.html` 14K HTTP 200; pytest 6 passed; evaluate headline holds
