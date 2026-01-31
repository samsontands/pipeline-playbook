import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

FEATURES = ["displacement", "horsepower", "weight", "acceleration"]
TARGET = "mpg"


def train_model(df: pd.DataFrame):
    df = df.dropna(subset=FEATURES + [TARGET])
    X = df[FEATURES]
    y = df[TARGET]
    model = LinearRegression()
    model.fit(X, y)
    preds = model.predict(X)
    mse = mean_squared_error(y, preds)
    metrics = {
        "rmse": mse ** 0.5,
        "r2": r2_score(y, preds),
    }
    coefficients = dict(zip(FEATURES, model.coef_.round(3)))
    return metrics, coefficients


def write_report(metrics, coefficients):
    path = Path("reports/model-summary.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Baseline MPG Regression", ""]
    lines.append(f"- **RMSE**: {metrics['rmse']:.2f}")
    lines.append(f"- **R²**: {metrics['r2']:.3f}")
    lines.append("")
    lines.append("## Coefficients")
    for feat, coef in coefficients.items():
        lines.append(f"- {feat}: {coef}")
    path.write_text("\n".join(lines) + "\n")
    print(f"Wrote model summary to {path}")


def main():
    raw_path = Path("data/raw/mpg.csv")
    df = pd.read_csv(raw_path)
    metrics, coefficients = train_model(df)
    write_report(metrics, coefficients)

if __name__ == "__main__":
    main()
