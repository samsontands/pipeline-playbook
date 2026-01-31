# Pipeline Playbook

A living data-science showcase. Each commit walks through one stage of a data pipeline so visitors can see the full lifecycle: ingestion ➜ EDA ➜ modeling ➜ presentation. We refresh the repo every ~5 hours with a new focused job, and the history documents progress in short, clear commits.

## Structure

- `data/raw/` — raw datasets that are archived once ingested.
- `data/processed/` — datasets ready for modeling or visualization.
- `src/` — reusable scripts (ingestion, wrangling, modeling).
- `reports/` — Markdown summaries, feature notes, model metrics, and presentation exports.
- `notebooks/` — (optional) exploratory notebooks.
- `docs/schedule.md` — the 5-hour cadence plan for the upcoming sprint.

## Current Pipeline Focus
1. **Data ingestion** — `data/raw/mpg.csv` is loaded from `seaborn` and stored for reproducibility.
2. **Exploration** — `reports/initial-eda.md` summarizes distributions and missingness.
3. **Modeling** — A baseline regression targets `mpg` using a simple feature set, reported in `reports/model-summary.md`.
4. **Presentation** — Placeholders for a future Streamlit explorer or dashboard.

## Next Job (Cycle 1)
- Timestamp: TODO (keep 5-hour blocks)
- Task: profile residuals + save figure to `reports/figures`.

More updates will follow in subsequent commits, each pushing the work forward a notch.
