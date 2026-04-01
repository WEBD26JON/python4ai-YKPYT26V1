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
    "Age": "age",
    "Sex": "sex",
    "ChestPain": "chest_pain_type",
    "RestBP": "resting_blood_pressure",
    "Chol": "cholesterol",
    "Fbs": "fasting_blood_sugar",
    "RestECG": "rest_ecg",
    "MaxHR": "max_heart_rate",
    "ExAng": "exercise_angina",
    "Oldpeak": "st_depression",
    "Slope": "st_slope",
    "Ca": "num_vessels",
    "Thal": "thalassemia",
    "AHD": "heart_disease"
}

df = df.rename(columns=COLUMN_INFO)

# 3. Seaborn settings
# -------------------------
sns.set_theme(style="whitegrid")

# 4. Target distribution
# -------------------------
# Shows how many cases have heart disease vs no disease
plt.figure(figsize=(6, 5))

sns.countplot(data=df, x="heart_disease")
plt.title("Heart Disease Distribution")

#plt.show()

# 5. Numerical features vs target
# -------------------------
# Compare how numeric variables differ between classes
# Using boxplots to see distribution and spread

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Age vs disease
sns.boxplot(data=df, x="heart_disease", y="age", ax=axes[0, 0])
axes[0, 0].set_title("Age vs Heart Disease")

# Cholesterol vs disease
sns.boxplot(data=df, x="heart_disease", y="cholesterol", ax=axes[0, 1])
axes[0, 1].set_title("Cholesterol vs Heart Disease")

# Max heart rate vs disease
sns.boxplot(data=df, x="heart_disease", y="max_heart_rate", ax=axes[1, 0])
axes[1, 0].set_title("Max Heart Rate vs Disease")

# Empty subplot (no fourth variable yet)
axes[1, 1].axis("off")

# Adjust spacing so plots don't overlap
plt.tight_layout()
#plt.show()

# 6. Categorical features vs target
# -------------------------
# Shows how categories are distributed across classes

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="chest_pain_type", hue="heart_disease")
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
