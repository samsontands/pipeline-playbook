"""Feature engineering for the MPG pipeline."""
import numpy as np
import pandas as pd
from pathlib import Path

FEATURES = ["displacement", "horsepower", "weight", "acceleration"]


def load_data() -> pd.DataFrame:
    raw_path = Path("data/raw/mpg.csv")
    return pd.read_csv(raw_path)


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")
    df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())
    df["power_to_weight"] = df["horsepower"] / df["weight"]
    df["sqrt_displacement"] = np.sqrt(df["displacement"])
    df["inv_weight"] = 1 / df["weight"]
    df["horsepower_sq"] = df["horsepower"] ** 2
    df["origin"] = df["origin"].astype(str)
    df = pd.get_dummies(df, columns=["origin"], prefix="origin")
    return df


def save_features(df: pd.DataFrame):
    processed_path = Path("data/processed/features.csv")
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_path, index=False)
    print(f"Saved engineered features to {processed_path}")


def main():
    df = engineer_features(load_data())
    save_features(df)

if __name__ == "__main__":
    main()
