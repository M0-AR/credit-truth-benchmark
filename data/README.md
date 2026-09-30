# Data — public + synthetic only

- `raw/` stays empty in git (see .gitignore). Download manually:
  - CFPB Consumer Complaints: https://www.consumerfinance.gov/data-research/consumer-complaints/
  - Fed Survey of Consumer Finances: https://www.federalreserve.gov/econres/scfindex.htm
  - Kaggle (auth required): `chaitanyajamble/realistic-credit-scoring-and-loan-default-prediction`, `hamziai/3million-enterprise-bank-records-ultimate-fraud`
- `processed/` holds only aggregates (see `src/credit_truth/data_loaders.py PUBLIC_AGGREGATES`).
- NEVER place AnnualCreditReport PDFs or bureau files here.
- Run `python -m credit_truth.data_loaders` helper? Use: `python -c "from credit_truth.data_loaders import fetch_public; print(fetch_public())"`
