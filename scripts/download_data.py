

"""Download the UCI Chronic Kidney Disease dataset and save it unchanged.

Usage (from the repo root):
    uv run python scripts/download_data.py
    
"""
from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo

UCI_ID = 336  # Chronic Kidney Disease
OUT_PATH = Path("data/raw/ckd_raw.csv")


def main():
    ckd = fetch_ucirepo(id=UCI_ID)
    ckd_raw = pd.concat([ckd.data.features, ckd.data.targets], axis=1)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ckd_raw.to_csv(OUT_PATH, index=False)
    print(f"Saved {ckd_raw.shape[0]} rows x {ckd_raw.shape[1]} columns to {OUT_PATH}")


if __name__ == "__main__":
    main()
