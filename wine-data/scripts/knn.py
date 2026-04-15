# wine-knn.py

from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load prepared data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "wine-prepared-3a.csv")

print("=== DATA SHAPE ===")
print(df.shape)

# 2. Split features / target
# -------------------------
# Separate input features (X) from target (y) 
# IMPORTANT: remove target column from X to prevent data leakage 
# (model must not see the correct answer during training)
X = df.drop(columns=["quality_class"])
y = df["quality_class"]

# 3. Train / Test split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 4. Scaling (CRITICAL for KNN)
# -------------------------
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. KNN model
# -------------------------
# model = KNeighborsClassifier(n_neighbors=3)
for k in [1, 3, 5, 7, 9, 11, 13, 15]:
#for k in [11]:
    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train, y_train)

    # 6. Prediction
    # -------------------------
    y_pred = model.predict(X_test)

    # 7. Evaluation
    # -------------------------
    cm = confusion_matrix(y_test, y_pred)
    #tn, fp, fn, tp = cm.ravel() # FOR BINARY CLASS ONLY !

    print(f"\n ====== RESULTS k-NN (k={k}) ====== ")
    print(f" Accuracy: {accuracy_score(y_test, y_pred):.3f}")

    print("\nCONFUSION MATRIX:")#Confusion matrix
    print(cm)

    print("\nClassification report")
    print(classification_report(y_test, y_pred))
