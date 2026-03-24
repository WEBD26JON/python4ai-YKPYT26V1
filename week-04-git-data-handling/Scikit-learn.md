# Guide: Hur man använder regressionsmodeller i Scikit-learn

## Grundstruktur (gemensam för alla modeller)

from sklearn.model_selection import train_test_split

## 1. Välj feature och target

X = df[["feature_column"]]  
y = df["target_column"]

## 2. Dela data

X_train, X_test, y_train, y_test = train_test_split(X, y)

## 3. Skapa modell

model = MODEL()

## 4. Träna modellen

model.fit(X_train, y_train)

## 5. Prediktion

predictions = model.predict(X_test)

---

## 📊 Vanliga regressionsmodeller

### 1. Linjär regression

from sklearn.linear_model import LinearRegression

model = LinearRegression()

---

### 2. Ridge regression

from sklearn.linear_model import Ridge

model = Ridge(alpha=1.0)

---

### 3. Lasso regression

from sklearn.linear_model import Lasso

model = Lasso(alpha=0.1)

---

### 4. Polynomregression

from sklearn.preprocessing import PolynomialFeatures  
from sklearn.linear_model import LinearRegression

poly = PolynomialFeatures(degree=2)  
X_poly = poly.fit_transform(X)

model = LinearRegression()  
model.fit(X_poly, y)

---

### 5. Icke-linjär modell (exempel via transformation)

import numpy as np

X_log = np.log(X)

model = LinearRegression()  
model.fit(X_log, y)

---

## Viktiga metoder

model.fit(X_train, y_train) # träning  
model.predict(X_test) # prediktion  
model.score(X_test, y_test) # enkel utvärdering (R²)

---

## Viktiga begrepp

| Begrepp | Betydelse           |
| ------- | ------------------- |
| feature | indata (X)          |
| target  | utdata (y)          |
| fit     | anpassa modellen    |
| predict | beräkna värden      |
| model   | matematisk funktion |

---

## Kort sammanfattning

Scikit-learn använder samma arbetsflöde för de flesta modeller:  
definiera data → skapa modell → träna → prediktera.
