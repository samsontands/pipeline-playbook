# Pipeline Playbook

The Pipeline Playbook documents a full data-science workflow so visitors can follow the lifecycle: ingestion → exploration → modeling → presentation. Each folder pairs code with narrative context so the repo feels like a readable case study.

## Structure

- `data/raw/` — archived snapshots of the original datasets.
- `data/processed/` — clean, analysis-ready tables for modeling or visualization, including one-hot encoded and derived predictors.
- `src/` — reusable scripts (ingestion, wrangling, modeling).
- `reports/` — Markdown summaries, feature notes, model metrics, and presentation artifacts.
- `notebooks/` — optional exploratory notebooks and drafts.
- `docs/` — plans and runner notes for upcoming iterations.

## Current Pipeline Focus
1. **Data ingestion** — `data/raw/mpg.csv` is sourced from the Seaborn collection and snapshot locally.
2. **Exploration** — `reports/initial-eda.md` narrates the distributional profile and missingness checks.
3. **Modeling** — A baseline regression targets `mpg`, with results surfaced in `reports/model-summary.md`.
4. **Diagnostics** — Residual analysis lives in `reports/residuals.md` and the accompanying figure (`reports/figures/residuals.png`).
5. **Presentation** — Reserved space for dashboards or summary write-ups that will highlight the insights.

## Upcoming work
- Residual checks and figure export (reports/figures/)
- Expanded feature engineering for a stronger baseline
- Drafting a presentation-friendly README section that ties the story to business impact

More concise updates will be captured in the `docs/plan.md` notes as the story evolves.
