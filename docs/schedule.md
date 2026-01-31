# 5-Hour Cadence Schedule

Each 5-hour sprint delivers one clear piece of the pipeline. The format is:

1. **Plan** – short note describing the task and dataset.
2. **Execute** – run scripts, generate data, create visual outputs.
3. **Summarize** – update reports/README with conclusions.
4. **Push** – commit + push, then ping Samson on Telegram with the brief.

## Week 1 Outline

| Sprint | Focus | Deliverable |
| --- | --- | --- |
| Sprint 0 | Data ingestion & raw dump | `data/raw/mpg.csv`, `reports/initial-eda.md` |
| Sprint 1 | Feature engineering & target definition | `src/feature_engineering.py`, `data/processed/features.csv` |
| Sprint 2 | Baseline modeling + metrics | `reports/model-summary.md`, `src/model.py` |
| Sprint 3 | Presentation layer (Streamlit or report) | `reports/preview.md`, optional `notebooks/presentation.ipynb` |
| Sprint 4 | Automation notes & scheduling | `docs/automation.md`, `reports/plan.md` |

Adjust as we go—later sprints will layer more advanced modeling, explainability, and deployment hooks.
