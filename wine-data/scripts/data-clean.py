# 🧹 Data Cleaning (Pandas)
from pathlib import Path
import pandas as pd

# 1. Load data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "wine-data-raw.csv")

print("=== RAW HEAD ===")
print(df.head())

print("\n=== RAW INFO ===")
print(df.info())

print("\n=== RAW DESCRIBE ===")
#print(df.describe(include="all"))
print(df.describe())                          # numbers only
print(df.describe(include=["str"]))           # strings only

# 2. Drop unnecessary columns
# -------------------------
# Remove index column Unnamed
# high_quality is derived from quality (quality >= 6 → 1)
# Removing to avoid data leakage and redundancy
df = df.drop(columns=["Unnamed: 0", "high_quality"])
print(f"\nUnnecessary columns [Unnamed, high_quality] droped")

# 3. Check missing values
# -------------------------
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 4. Handle missing values
# -------------------------

# Option A: drop rows with missing values
df_clean = df.dropna()

# 5. Check duplicates
# -------------------------
print("\n=== DUPLICATES: ", df_clean.duplicated().sum())

# Dublicates details
dupes = df_clean[df_clean.duplicated(keep=False)]
print("\n=== DUPLICATE ROWS SAMPLE ===")
print(dupes.sort_values(by=list(df_clean.columns)).head(10))

# Dublicates by color?
print("\n=== DUPLICATES BY COLOR ===")
print(dupes["color"].value_counts())

print("\nCleaninng duplicates ...")
df_clean = df_clean.drop_duplicates()

# Remove extreme outlier: residual sugar > 30
# Likely measurement error or dessert wine outside dataset scope
# This is added after visualisation
before = len(df_clean)
df_clean = df_clean[df_clean["residual sugar"] <= 30]
print(f"Removed {before - len(df_clean)} rows with residual sugar > 30")

# 6. Check data types
# -------------------------
print("\n=== CLEANED DTYPES ===")
print(df_clean.dtypes)

# 7. Inspect categorical columns
# -------------------------
categorical_cols = df_clean.select_dtypes(include=["object", "string"]).columns

for col in categorical_cols:
    print(f"\n=== CLEANED VALUE COUNTS: {col} ===")
    print(df_clean[col].value_counts())

print("=== CLEANED HEAD ===")
print(df_clean.head())

print("\n=== CLEANED INFO ===")
print(df_clean.info())

print("\n=== CLEANED DESCRIBE ===")
#print(df_clean.describe(include="all"))
print(df_clean.describe())                          # numbers only
print(df_clean.describe(include=["str"]))           # strings only

# 8. Save cleaned dataset
# -------------------------
OUTPUT_PATH = BASE_DIR / "data" / "wine-clean.csv"
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