"""Generate residual diagnostics and save a figure."""
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

FEATURES = ["displacement", "horsepower", "weight", "acceleration"]
TARGET = "mpg"


def load_data():
    raw_path = Path("data/raw/mpg.csv")
    return pd.read_csv(raw_path)


def train_model(df):
    df_clean = df.dropna(subset=FEATURES + [TARGET])
    X = df_clean[FEATURES]
    y = df_clean[TARGET]
    model = LinearRegression()
    model.fit(X, y)
    preds = model.predict(X)
    residuals = y - preds
    return df_clean, preds, residuals


def plot_residuals(df, residuals):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df[TARGET], residuals, alpha=0.75, color="#1e88e5", edgecolor="white", linewidth=0.5)
    ax.axhline(0, linestyle="--", color="#4b4deb")
    ax.set_title("Residuals vs. MPG")
    ax.set_xlabel("Actual MPG")
    ax.set_ylabel("Residual")
    fig.tight_layout()
    out_path = Path("reports/figures")
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "residuals.png"
    fig.savefig(file_path)
    plt.close(fig)
    return file_path


def write_report(residuals):
    stats = residuals.describe().round(2)
    lines = ["# Residual Diagnostics", "", f"- **Mean residual**: {stats['mean']}", f"- **Std residual**: {stats['std']}", f"- **Min residual**: {stats['min']}", f"- **Max residual**: {stats['max']}", "", "Residuals are roughly centered around 0, indicating no obvious bias, and the scatter plot saved above helps visualise heteroscedasticity."]
    report_path = Path("reports/residuals.md")
    report_path.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    df, preds, residuals = train_model(load_data())
    fig_path = plot_residuals(df, residuals)
    write_report(residuals)
    print(f"Residual report written to reports/residuals.md and plot saved to {fig_path}")
