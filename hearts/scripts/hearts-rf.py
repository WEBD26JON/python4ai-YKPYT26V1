# ============================================================
# @license (c) Alexander Soviet9773Red - https://github.com/Soviet9773Red/
# ============================================================
# Random Forest Classifier

from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "heart_prepared.csv")

# Split
X = df.drop(columns=["ahd"])
y = df["ahd"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Model

# model = RandomForestClassifier(
#     n_estimators=100,
#     random_state=42
# )

for depth in [2, 3, 4, 5, None]:
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Metrics
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    print(
    f"\n=== RESULTS (Random Forest: depth={depth}, trees={model.n_estimators}) ==="
        )
    
    print(
        f"Accuracy: {accuracy_score(y_test, y_pred):.3f} " 
        f", n_estimators={model.n_estimators}, "
        f"max_depth={model.max_depth}" 
        )   

    print("\nCONFUSION MATRIX:")
    print(cm)
    print(f"Healthy → correct: {tn}, wrong: {fp}")
    print(f"Disease → correct: {tp}, missed: {fn}")

    print("\nCLASSIFICATION REPORT:")
    print(classification_report(y_test, y_pred))