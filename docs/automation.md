# Automation Notes

This section explains how the pipeline can be executed from ingestion to presentation.

1. `scripts/ingest_mpg.py` — snapshots the raw mpg dataset from Seaborn into `data/raw/mpg.csv` so the baseline can be reproduced.
2. `scripts/feature_engineering.py` — runs next to build `data/processed/features.csv` with derived predictors and one-hot origin flags.
3. `scripts/modeling.py` — trains the linear regression and Random Forest models on the cleaned features, saves their artifacts under `models/`, and exports prediction vs. actual plots.
4. `scripts/residuals.py` — recreates the residual scatter (for diagnostics) such that the latest model artifacts are consumed.
5. `scripts/interpretability.py` — loads the serialized models, computes permutation importance, and snapshots the resulting charts.

Running the scripts in this order ensures each stage feeds the next. Future automation could add a `Makefile`, Airflow DAG, or GitHub Actions workflow that ties these commands together, but for now the repo documents the manual order and the required dependencies (`requirements.txt`).
