# Iteration Plan

This document tracks the planned steps for ongoing pipeline work. Each entry is human-curated, reflecting the next area of focus.

## Planned Moves
- **Data ingestion & storage** — lock down the mpg dataset (`scripts/ingest_mpg.py`) and keep `data/raw/mpg.csv` as the canonical snapshot.
- **Exploration** — document distributional insights, missingness audits, and observation notes in `reports/initial-eda.md`.
- **Modeling** — train a simple regression, track metrics, and write the findings to `reports/model-summary.md`.
- **Diagnostics** — add residual analysis + figure in `reports/residuals.md` and `reports/figures/residuals.png` to prove the baseline behaves.
- **Presentation** — build a narrative section with figures and summary text so the modeling story can live in a blog-style report or dashboard.

As each step completes, the notes here can be expanded with results, references to new scripts, or links to artifacts.
