
from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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

# Model (Tree)
# model = DecisionTreeClassifier(max_depth=5, random_state=42)
# for depth in [2, 3, 4, 5, 6, 7, 8, None]:
for depth in [3]:    
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)

    model.fit(X_train, y_train)
    # Predict
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Metrics
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    print("\n=== RESULTS (Decision Tree) ===")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f} , depth={depth}")

    print("\nCONFUSION MATRIX:")
    print(cm)
    print(f"Healthy → correct: {tn}, wrong: {fp}")
    print(f"Disease → correct: {tp}, missed: {fn}")

    print("\nCLASSIFICATION REPORT:")
    print(classification_report(y_test, y_pred))
