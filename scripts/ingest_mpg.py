"""Load the Seaborn `mpg` dataset and persist it locally."""
import pandas as pd
from pathlib import Path

def main():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
    dataset = pd.read_csv(url)
    dataset = dataset.drop(columns=["name"])
    raw_path = Path("data/raw/mpg.csv")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(raw_path, index=False)
    print(f"Saved raw dataset to {raw_path}")

if __name__ == "__main__":
    main()
