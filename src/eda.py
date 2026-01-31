import pandas as pd
from pathlib import Path

def summarize(df: pd.DataFrame) -> str:
    desc = df.describe().transpose().round(2).reset_index()
    stats = []
    for _, row in desc.iterrows():
        stats.append(
            f"- **{row['index']}** – mean {row['mean']}, std {row['std']}, min {row['min']}, max {row['max']}"
        )
    missing = df.isna().sum().rename('missing')
    missing_lines = [f"- {col}: {missing[col]} missing" for col in missing.index if missing[col] > 0]
    return "\n".join(["## Summary statistics", *stats, "", "## Missing values", *missing_lines])

def main():
    raw_path = Path("data/raw/mpg.csv")
    df = pd.read_csv(raw_path)
    report = summarize(df)
    report_path = Path("reports/initial-eda.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report + "\n")
    print(f"Wrote EDA report to {report_path}")

if __name__ == "__main__":
    main()
