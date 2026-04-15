from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load cleaned data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "wine-clean.csv")

#sns.boxplot(data=df, x="quality", y="alcohol")

quality_labels = sorted(df["quality"].unique())

# Boxplot alcohol vs quality
# -------------------------
groups = [df[df["quality"] == q]["alcohol"].values for q in quality_labels]

plt.figure(figsize=(10, 6))
plt.boxplot(groups, tick_labels=quality_labels)
plt.title("Alcohol vs Quality")
plt.xlabel("Quality")
plt.ylabel("Alcohol (%)")
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Boxplot volatile acidity vs quality
# -------------------------
groups = [df[df["quality"] == q]["volatile acidity"].values for q in quality_labels]

plt.figure(figsize=(10, 6))
plt.boxplot(groups, tick_labels=quality_labels)
plt.title("Volatile Acidity vs Quality")
plt.xlabel("Quality")
plt.ylabel("Volatile Acidity")
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Boxplot sulphates vs quality
# -------------------------
groups = [df[df["quality"] == q]["sulphates"].values for q in quality_labels]

plt.figure(figsize=(10, 6))
plt.boxplot(groups, tick_labels=quality_labels)
plt.title("Sulphates vs Quality")
plt.xlabel("Quality")
plt.ylabel("Sulphates")
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Histogram residual sugar
# -------------------------
plt.figure(figsize=(10, 6))
plt.hist(df["residual sugar"], bins=60, edgecolor="black", color="steelblue")
plt.title("Residual Sugar — Distribution")
plt.xlabel("Residual Sugar")
plt.ylabel("Count")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()