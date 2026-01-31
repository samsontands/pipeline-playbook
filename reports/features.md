# Feature Engineering Notes

- **Horsepower imputation**: Null values are replaced with the median so the regression receives a consistent signal.
- **Derived predictors**:
  - `power_to_weight` (horsepower divided by weight) captures engine strength relative to mass.
  - `sqrt_displacement` softens the effect of large displacement values.
  - `inv_weight` prioritizes lighter cars, trading off low horsepower.
  - `horsepower_sq` helps catch nonlinear effects beyond the linear baseline.
- **Origin encoding**: One-hot columns allow the model to account for manufacturing zones (USA, Europe, Japan).

The processed dataset lives at `data/processed/features.csv` and serves as the cleaned input for future modeling iterations.