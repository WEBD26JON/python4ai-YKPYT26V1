# ============================================================
# @license (c) Alexander Soviet9773Red - https://github.com/Soviet9773Red/
# ============================================================
# 🧠 hearts-logreg.py

from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load prepared data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "heart_prepared.csv")

print("=== DATA SHAPE ===")
print(df.shape)

# 2. Split features / target
# -------------------------
X = df.drop(columns=["ahd"])
y = df["ahd"]

print("\n=== FEATURES ===")
print(X.columns)

# 3. Train / Test split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 4. Model
# -------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. Prediction
# -------------------------
y_pred = model.predict(X_test)

# 6. Evaluation
# -------------------------
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print("\n=== RESULTS (Logistic Regression) ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")

print("\nCONFUSION MATRIX:")
print(cm)
print(f"Healthy → correct: {tn}, wrong: {fp}")
print(f"Disease → correct: {tp}, missed: {fn}")

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))