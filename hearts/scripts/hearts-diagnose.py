# ============================================================
# @license (c) Alexander Soviet9773Red - https://github.com/Soviet9773Red/
# ============================================================
# Diagnose
from pathlib import Path
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Load dataset and train model
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "heart_prepared.csv")

X = df.drop(columns=["ahd"])
y = df["ahd"]

"""
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
"""

# Input patient
# -------------------------
def get_patient():
    print("\n    k-NN model , k = 11")
    print("\n=== ENTER PATIENT DATA ===")

    print(
        f"Short info:\n "
        f"Chest pain        → type of chest discomfort (or absence of it)\n" 
        f"Exercise angina   → pain triggered by physical activity\n "
        f"Oldpeak           → how much the heart struggles under stress\n " 
        f"Ca                → number of blocked or narrowed arteries\n "
        f"ST depression     → ECG signal abnormality under stress\n "
        f"Thal              → quality of blood flow through heart muscle\n "
        )

    age = int(input("Age (29–77): "))
    sex = int(input("Sex (1=male, 0=female): "))
    
    print("Chest pain type:")
    print("0=typical, 1=atypical, 2=non-anginal, 3=asymptomatic")
    chest_pain = int(input("Chest pain (0–3): "))

    chol = float(input("Cholesterol (100–400): "))
    max_hr = int(input("Max heart rate (70–200): "))
    
    ex_angina = int(input("Exercise angina (1=yes, 0=no): "))
    oldpeak = float(input("ST depression (0.0–6.0): "))
    ca = int(input("Number of vessels (0–3): "))

    print("Thal:")
    print("0=normal, 1=fixed, 2=reversible")
    thal = int(input("Thal (0–2): "))

    return {
        "age": age,
        "sex": sex,
        "chest_pain": chest_pain,
        "chol": chol,
        "max_hr": max_hr,
        "ex_angina": ex_angina,
        "oldpeak": oldpeak,
        "ca": ca,
        "thal": thal
    }

# Prepare input
# -------------------------
def prepare_input(data, columns):
    df_input = pd.DataFrame([data])
    df_input = df_input.reindex(columns=columns, fill_value=0)
    return df_input

# Transform input
# -------------------------
def transform_input(data, columns):
    df = pd.DataFrame([data])

    # one-hot вручную
    df["chest_pain_asymptomatic"] = int(data["chest_pain"] == 3)
    df["chest_pain_nonanginal"] = int(data["chest_pain"] == 2)
    df["chest_pain_nontypical"] = int(data["chest_pain"] == 1)

    df["thal_normal"] = int(data["thal"] == 0)
    df["thal_reversable"] = int(data["thal"] == 2)

    df = df.drop(columns=["chest_pain", "thal"])

    # привести к тем же колонкам
    df = df.reindex(columns=columns, fill_value=0)

    return df

# Diagnose
# -------------------------
def diagnose():
    df = pd.read_csv(DATA_DIR / "heart_prepared.csv")

    X = df.drop(columns=["ahd"])
    y = df["ahd"]

    # split + scaling
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    model = KNeighborsClassifier(n_neighbors=11)
    model.fit(X_train, y_train)

    # input
    patient = get_patient()

    X_input = transform_input(patient, X.columns)
    X_input = scaler.transform(X_input)

    pred = model.predict(X_input)[0]
    proba = model.predict_proba(X_input)[0][1]

    print("\n=== RESULT ===")

    print("Diagnosis:", "Disease" if pred == 1 else "No disease")
    print(f"Risk probability: {proba:.2f}")

# Run
# -------------------------
if __name__ == "__main__":
    diagnose()

