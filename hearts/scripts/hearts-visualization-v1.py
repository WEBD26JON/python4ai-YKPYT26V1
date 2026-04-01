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
sns.countplot(data=df, x="heart_disease")
plt.title("Heart Disease Distribution")
plt.show()


# 5. Age vs disease
# -------------------------
sns.boxplot(data=df, x="heart_disease", y="age")
plt.title("Age vs Heart Disease")
plt.show()


# 6. Chest pain vs disease
# -------------------------
sns.countplot(data=df, x="chest_pain_type", hue="heart_disease")
plt.title("Chest Pain vs Heart Disease")
plt.xticks(rotation=30)
plt.show()


# 7. Cholesterol vs disease
# -------------------------
sns.boxplot(data=df, x="heart_disease", y="cholesterol")
plt.title("Cholesterol vs Heart Disease")
plt.show()


# 8. Max heart rate
# -------------------------
sns.boxplot(data=df, x="heart_disease", y="max_heart_rate")
plt.title("Max Heart Rate vs Disease")
plt.show()