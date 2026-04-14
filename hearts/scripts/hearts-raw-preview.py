# Raw data viewer (Pandas)
from pathlib import Path
import pandas as pd

# 1. Load data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "heart_raw.csv")

print("\n=== RAW DATA (HEAD) ===")
print(df.head())

print("\n=== RAW INFO ===")
print(df.info())

print("\n=== RAW DESCRIBE ===")
print(df.describe())