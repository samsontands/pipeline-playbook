"""Train and evaluate models using the engineered features."""
import joblib
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

TARGET = "mpg"
BASE_FEATURES = [
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "power_to_weight",
    "sqrt_displacement",
    "inv_weight",
    "horsepower_sq",
]


def load_data() -> pd.DataFrame:
    path = Path("data/processed/features.csv")
    return pd.read_csv(path)


def eval_model(model, X_train, y_train, X_test, y_test):
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, preds)
    return preds, {"rmse": rmse, "r2": r2}


def save_plot(y_test, preds, model_name: str) -> Path:
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(y_test, preds, alpha=0.6, color="#4b4deb")
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "--", color="#1e88e5")
    ax.set_title(f"{model_name} Predictions vs Actual")
    ax.set_xlabel("Actual MPG")
    ax.set_ylabel("Predicted MPG")
    ax.grid(alpha=0.3)
    path = Path("reports/figures")
    path.mkdir(parents=True, exist_ok=True)
    out = path / f"{model_name.replace(' ', '_').lower()}-predictions.png"
    fig.savefig(out)
    plt.close(fig)
    return out


def main():
    df = load_data()
    origin_cols = sorted([col for col in df.columns if col.startswith("origin_")])
    features = BASE_FEATURES + origin_cols
    df = df.dropna(subset=features + [TARGET])
    X = df[features]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.25)

    models = [
        ("Linear Regression", LinearRegression()),
        ("Random Forest", RandomForestRegressor(random_state=42, n_estimators=100)),
    ]
    lines = ["# Modeling Summary", ""]
    for name, model in models:
        model.fit(X_train, y_train)
        preds, metrics = eval_model(model, X_train, y_train, X_test, y_test)
        fig_path = save_plot(y_test, preds, name)
        lines.append(f"## {name}")
        lines.append(f"- RMSE: {metrics['rmse']:.2f}")
        lines.append(f"- R²: {metrics['r2']:.3f}")
        lines.append(f"- Prediction plot: {fig_path}")
        lines.append("")
        joblib.dump(model, Path("models") / f"{name.replace(' ', '_').lower()}.pkl")

    report_path = Path("reports/modeling-summary.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n")
    print(f"Modeling summary saved to {report_path}")

if __name__ == "__main__":
    Path("models").mkdir(exist_ok=True)
    main()
