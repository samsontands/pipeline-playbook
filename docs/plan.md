# Iteration Plan

This document tracks the planned steps for ongoing pipeline work. Each entry is human-curated, reflecting the next area of focus.

## Planned Moves
- **Data ingestion & storage** — lock down the mpg dataset (`scripts/ingest_mpg.py`) and keep `data/raw/mpg.csv` as the canonical snapshot.
- **Exploration** — document distributional insights, missingness audits, and observation notes in `reports/initial-eda.md`.
- **Modeling** — train a linear regression and Random Forest on the engineered predictors, capture metrics, and document the comparisons in `reports/modeling-summary.md`.
- **Diagnostics** — residual analysis + figure in `reports/residuals.md` and `reports/figures/residuals.png` to validate the baseline.
- **Interpretability** — run permutation importance scripts to rank engineered predictors and summarize them in `reports/interpretability.md` (plots saved in `reports/figures`).
- **Feature engineering** — enrich the dataset with ratios, polynomial terms, and one-hot origin flags; save the output to `data/processed/features.csv` and document the choices in `reports/features.md`.
- **Presentation** — build a narrative section (`reports/presentation.md`) that highlights ingestion, features, modeling, diagnostics, and includes the plot gallery.

As each step completes, the notes here can be expanded with results, references to new scripts, or links to artifacts.
