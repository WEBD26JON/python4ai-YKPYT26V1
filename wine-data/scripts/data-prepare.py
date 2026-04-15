from pathlib import Path
import pandas as pd

# 1. Load cleaned data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "wine-clean.csv")
# round values
df = df.round({
    "fixed acidity":        1,
    "volatile acidity":     2,
    "citric acid":          2,
    "residual sugar":       1,
    "chlorides":            3,
    "free sulfur dioxide":  0,
    "total sulfur dioxide": 0,
    "density":              4,
    "pH":                   2,
    "sulphates":            2,
    "alcohol":              1,
})
print("\n=== INITIAL SHAPE:", df.shape)

def check_result(df, name):
    print(f"\n=== {name} ===")
    print(f"Shape: {df.shape}")
    #print(f"\nDtypes:\n{df.dtypes}")
    print(f"Target distribution:\n{df['quality_class'].value_counts().sort_index()}")
    #print(f"\nHead:\n{df.head()}")

# Wine color encoding
df["color"] = df["color"].map({"red": 0, "white": 1})

# Option 1 — original quality classes
df_orig = df.copy()
# quality already is a number (3–9), just rename to unify
df_orig = df_orig.rename(columns={"quality": "quality_class"})
df_orig.to_csv(DATA_DIR / "wine-prepared-orig.csv", index=False)
# Check res:
check_result(df_orig, "RAW CLASSES")

# Option 2- bynary quality classes
df_2 = df.copy()
df_2["quality_class"] = pd.cut(df_2["quality"], bins=[2,5,9], labels=["ordinary","high"])
df_2 = df_2.drop(columns=["quality"])
df_2.to_csv(DATA_DIR / "wine-prepared-2.csv", index=False)
# Check res:
check_result(df_2, "PREPARED 2 CLASSES (binary)")

# Option 3- three quality classes
# bins:   [2, 5, 6, 9]
# low     = quality 3–5  →  1988 rader  (37%)
# medium  = quality 6    →  2323 rader  (44%)
# high    = quality 7–9  →  1009 rader  (19%)
df_3 = df.copy()
df_3["quality_class"] = pd.cut(df_3["quality"], bins=[2,5,6,9], labels=["low","medium","high"])
df_3 = df_3.drop(columns=["quality"])
df_3.to_csv(DATA_DIR / "wine-prepared-3a.csv", index=False)
# Check res:
check_result(df_3, "PREPARED 3a CLASSES")

# Option 4- 
# low    = 3–5  →  30+206+1752 = 1988  (37%)
# medium = 6–7  →  2323+856   = 3179  (60%)
# high   = 8–9  →  148+5      = 153   (3%)
df_3 = df.copy()
df_3["quality_class"] = pd.cut(df_3["quality"], bins=[2, 5, 7, 9], labels=["low", "medium", "high"])
df_3 = df_3.drop(columns=["quality"])
df_3.to_csv(DATA_DIR / "wine-prepared-3b.csv", index=False)
# Check res:
check_result(df_3, "PREPARED 3b CLASSES")
