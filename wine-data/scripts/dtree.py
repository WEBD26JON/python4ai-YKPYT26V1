
from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "wine-prepared-3a.csv")

# Split
X = df.drop(columns=["quality_class"])
y = df["quality_class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Model (Tree)
for depth in [2, 3, 4, 5, 6, 7, 8, None]:
#for depth in [3]:    
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    cm = confusion_matrix(y_test, y_pred)

    print(f"\n=== RESULTS (Decision Tree, depth={depth}) ===")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")

    print("\nCONFUSION MATRIX:")
    print(cm)

    print("\nCLASSIFICATION REPORT:")
    print(classification_report(y_test, y_pred))
