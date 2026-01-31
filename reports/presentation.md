# Pipeline Presentation

## Ingestion
- `scripts/ingest_mpg.py` snapshots the Seaborn `mpg` dataset to `data/raw/mpg.csv`. The CSV is stored in the repo so reviewers see exactly which raw records were used.

## Feature Engineering
- `scripts/feature_engineering.py` derives power-to-weight, sqrt-displacement, inverse weight, and horsepower² features, and one-hot encodes the `origin` column. The clean table lives at `data/processed/features.csv` and is documented in `reports/features.md`.

## Modeling
- Two models (Linear Regression + Random Forest) are trained on the engineered features (`scripts/modeling.py`). Both predictions are compared in `reports/modeling-summary.md` along with their RMSE/R². The `models/` folder holds the serialized artifacts for future reuse.
- Prediction vs. actual snapshots are available:
  - `reports/figures/linear_regression-predictions.png`
  - `reports/figures/random_forest-predictions.png`

## Diagnostics
- Residual inspection is captured in `reports/residuals.md`, supported by the scatter plot `reports/figures/residuals.png`.

## Results at a glance
![Residuals](reports/figures/residuals.png)
![Linear Regression](reports/figures/linear_regression-predictions.png)
![Random Forest](reports/figures/random_forest-predictions.png)

## What’s next
1. Test interpretability: SHAP or permutation importance so the models can be trusted by stakeholders.
2. Deploy a lightweight Streamlit app (or Streamlit-powered story) to surface the predictions and explainability notes.
3. Add automation notes (e.g., scheduling, CI) once the modeling pipeline stabilizes.
