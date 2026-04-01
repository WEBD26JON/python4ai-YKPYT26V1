# ver. 1.0.3
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load cleaned data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "heart_clean.csv")

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

# 3. Seaborn settings
# -------------------------
sns.set_theme(style="whitegrid")

# 4, 5. Numerical features vs target distribution
# -------------------------
# Compare how numeric variables differ between classes
# Using boxplots to see distribution and spread

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Target distribution (теперь в grid)
# Shows how many cases have heart disease vs no disease
sns.countplot(data=df, x="ahd", ax=axes[0, 0])
axes[0, 0].set_title("Heart Disease Distribution")

# 2. Age vs disease
sns.boxplot(data=df, x="ahd", y="age", ax=axes[0, 1])
axes[0, 1].set_title("Age vs Heart Disease")

# 3. Cholesterol vs disease
sns.boxplot(data=df, x="ahd", y="chol", ax=axes[1, 0])
axes[1, 0].set_title("Cholesterol vs Heart Disease")

# 4. Max heart rate vs disease
sns.boxplot(data=df, x="ahd", y="max_hr", ax=axes[1, 1])
axes[1, 1].set_title("Max Heart Rate vs Disease")

plt.tight_layout()
#plt.show()

# 6. Categorical features vs target
# -------------------------
# Shows how categories are distributed across classes

plt.figure(figsize=(8, 9))

sns.countplot(data=df, x="chest_pain", hue="ahd")
plt.title("Chest Pain vs Heart Disease")

# Rotate labels for better readability
plt.xticks(rotation=30)

plt.show()

"""
# Kommentar (struktur)
- **Block 4** → visar balans i target (baseline)
- **Block 5** → analyserar numeriska variabler
- **Block 6** → analyserar kategoriska variabler

# Viktigt att observera
När du kör detta, titta efter:
- skiljer sig boxplots tydligt mellan Yes/No?
- finns det variabler som separerar grupperna?
- vilka features verkar mest informativa?
"""
