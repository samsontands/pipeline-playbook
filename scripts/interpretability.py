"""Permutation importance diagnostics for final models."""
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.inspection import permutation_importance

FEATURES = [
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "power_to_weight",
    "sqrt_displacement",
    "inv_weight",
    "horsepower_sq",
]


def load_features():
    path = Path("data/processed/features.csv")
    return pd.read_csv(path)


def load_models():
    models = {}
    model_dir = Path("models")
    for file in model_dir.glob("*.pkl"):
        models[file.stem] = joblib.load(file)
    return models


def compute_importance(model, X, y):
    result = permutation_importance(model, X, y, n_repeats=20, random_state=42)
    df = pd.DataFrame({"feature": X.columns, "importance": result.importances_mean})
    return df.sort_values("importance", ascending=False)


def save_plot(df, model_name):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="importance", y="feature", data=df, ax=ax, palette="viridis")
    ax.set_title(f"Permutation Importance ({model_name})")
    ax.set_xlabel("Mean importance")
    ax.set_ylabel("Feature")
    path = Path("reports/figures")
    path.mkdir(parents=True, exist_ok=True)
    out = path / f"{model_name}_importance.png"
    fig.tight_layout()
    fig.savefig(out)
    plt.close(fig)
    return out


def write_report(scores):
    lines = ["# Interpretation Notes", ""]
    for model_name, df in scores.items():
        lines.append(f"## {model_name}")
        for _, row in df.iterrows():
            lines.append(f"- {row['feature']}: {row['importance']:.4f}")
        lines.append("")
    report_path = Path("reports/interpretability.md")
    report_path.write_text("\n".join(lines) + "\n")
    return report_path


def main():
    df = load_features()
    origin_cols = sorted([col for col in df.columns if col.startswith("origin_")])
    features = FEATURES + origin_cols
    df = df.dropna(subset=features + ["mpg"])
    X = df[features]
    y = df["mpg"]
    models = load_models()
    results = {}
    for name, model in models.items():
        df_imp = compute_importance(model, X, y)
        save_plot(df_imp, name)
        results[name] = df_imp
    report = write_report(results)
    print(f"Interpretability report saved to {report}")

if __name__ == "__main__":
    main()
