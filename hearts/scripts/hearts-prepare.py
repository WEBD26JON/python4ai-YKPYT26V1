# clean data → numeric data 
# 🧠 hearts-prepare.py

from pathlib import Path
import pandas as pd

# 1. Load cleaned data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "heart_clean.csv")

print("=== INITIAL SHAPE ===")
print(df.shape)

# 2. Rename columns (metadata)
# -------------------------

COLUMN_INFO = {
    "Age": "age",               # age in years
    "Sex": "sex",               # 1 = male, 0 = female
    "ChestPain": "chest_pain",  # type of chest pain (typical / atypical / non-anginal / asymptomatic)
    "RestBP": "rbl_pres",       # resting blood pressure (mm Hg at rest)
    "Chol": "chol",             # cholesterol level in blood
    "Fbs": "fbl_sugar",         # fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
    "RestECG": "rest_ecg",      # resting electrocardiographic results (heart electrical activity)
    "MaxHR": "max_hr",          # maximum heart rate achieved during test
    "ExAng": "ex_angina",       # exercise induced angina (chest pain during activity)
    "Oldpeak": "oldpeak",       # ST depression (how much ECG signal drops during stress)
    "Slope": "st_slope",        # slope of ST segment (shape of ECG curve during peak exercise)
    "Ca": "ca",                 # number of major vessels (0–3) detected by fluoroscopy
    "Thal": "thal",             # thalassemia type (normal / fixed defect / reversible defect)
    "AHD": "ahd"                # angiographic heart disease (Yes/No → later 1/0) - target
}

df = df.rename(columns=COLUMN_INFO)

# 3. Target encoding
# -------------------------
# Convert Yes/No → 1/0

df["ahd"] = df["ahd"].map({
    "Yes": 1,
    "No": 0
})

# 4. Feature encoding
# -------------------------
# Convert categorical features → numeric (one-hot encoding)

df = pd.get_dummies(df, drop_first=True)

# 5. Check result
# -------------------------
print("\n=== AFTER ENCODING ===")
print(df.head())

print("\n=== DTYPES ===")
print(df.dtypes)

print("\n=== SHAPE ===")
print(df.shape)

# 6. Save prepared data
# -------------------------
OUTPUT_PATH = DATA_DIR / "heart_prepared.csv"
df.to_csv(OUTPUT_PATH, index=False)
print("\nSaved prepared dataset to:", OUTPUT_PATH)
