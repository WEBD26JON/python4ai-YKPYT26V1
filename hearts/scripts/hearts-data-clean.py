# 🧹 Data Cleaning (Pandas)
from pathlib import Path
import pandas as pd

# 1. Load data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "heart_raw.csv")

print("=== HEAD ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe(include="all"))

# 2. Drop unnecessary columns
# -------------------------
# Example: remove index column if exists
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# 3. Check missing values
# -------------------------
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 4. Handle missing values
# -------------------------

# Option A: drop rows with missing values
df_clean = df.dropna()

# Option B (alternative): fill missing values
# df["Ca"] = df["Ca"].fillna(df["Ca"].median())
# df["Thal"] = df["Thal"].fillna(df["Thal"].mode()[0])

# 5. Check duplicates
# -------------------------
print("\n=== DUPLICATES ===")
print(df_clean.duplicated().sum())

df_clean = df_clean.drop_duplicates()

# 6. Check data types
# -------------------------
print("\n=== DTYPES ===")
print(df_clean.dtypes)

# 7. Inspect categorical columns
# -------------------------
categorical_cols = df_clean.select_dtypes(include=["object", "string"]).columns

for col in categorical_cols:
    print(f"\n=== VALUE COUNTS: {col} ===")
    print(df_clean[col].value_counts())

# 8. Save cleaned dataset
# -------------------------
OUTPUT_PATH = BASE_DIR / "data" / "heart_clean.csv"
df_clean.to_csv(OUTPUT_PATH, index=False)

print("\nSaved cleaned dataset to:", OUTPUT_PATH)

# Kommentar
"""
Detta skript gör:

* läser in data
* analyserar struktur
* tar bort onödiga kolumner
* hanterar saknade värden
* kontrollerar dubbletter
* visar kategoriska värden
* sparar en ren version av datasetet

# Viktigt

Detta är **första steget** innan:

* visualisering (Seaborn)
* encoding (get_dummies)
* scaling
* ML-modeller

"""