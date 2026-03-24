## Contents, vecka 4

- [Venv](https://github.com/Soviet9773Red/python4ai-YKPYT26V1/blob/main/week-04-git-data-handling/venv.md)
- [Venv-aktivering](https://github.com/Soviet9773Red/python4ai-YKPYT26V1/blob/main/week-04-git-data-handling/venv-aktivering.md)
- [VSC-venv](https://github.com/Soviet9773Red/python4ai-YKPYT26V1/blob/main/week-04-git-data-handling/VSC-venv.md)
- [Venv python.org](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Skikit-learn.md](https://github.com/Soviet9773Red/python4ai-YKPYT26V1/blob/main/week-04-git-data-handling/Scikit-learn.md)

## Översikt: Approximationsmetoder (anpassning av modeller)

**Definition:**  
Approximationsmetoder används för att hitta en funktion som bäst beskriver sambandet mellan indata och utdata baserat på observationer.

---

## 1. Linjär regression (Linear Regression)

**Idé:**  
Anpassar en rät linje:

y = ax + b

**Metod:**  
Minimerar summan av kvadrerade fel (minsta kvadratmetoden).

**Användning:**

- Enkla samband
- Första analyssteg
- Baslinjemodell

---

## 2. Polynomregression (Polynomial Regression)

**Idé:**  
Utökar linjär regression med högre ordningens termer:

y = a0 + a1x + a2x² + ...

**Fördel:**  
Kan modellera krökta samband

**Nackdel:**  
Risk för överanpassning (overfitting)

---

## 3. Ridge-regression

**Idé:**  
Linjär regression med regularisering (L2):

minimera fel + straff för stora koefficienter

**Syfte:**

- Stabilare modell
- Minskar känslighet för brus

---

## 4. Lasso-regression

**Idé:**  
Regularisering (L1) som kan sätta vissa koefficienter till noll

**Effekt:**

- Automatisk variabelselektion
- Förenklar modellen

---

## 5. Icke-linjär regression

**Idé:**  
Modellen är inte linjär i parametrar

Exempel:

y = a * e^(bx)

**Användning:**

- Fysiska processer
- Dämpade signaler
- Tillväxtmodeller

---

## 6. Minsta kvadratmetoden (Least Squares)

**Kärnprincip:**

minimera Σ (y_observerad − y_modell)^2

**Kommentar:**  
Detta är grunden för många regressionsmetoder.

---

## 7. Interpolation vs approximation

- **Interpolation:** exakt genom alla datapunkter
- **Approximation:** bästa möjliga anpassning (tillåter fel)

I ML används nästan alltid **approximation**.

---

## 8. Koppling till maskininlärning

I praktiken:

data → anpassning av modell → prediktion

Terminologi:

| Klassisk term | ML-term |
| --- | --- |
| approximation | learning |
| parametrar | weights |
| modell | model |
| beräkning | prediction |

---

## Sammanfattning

- Linjär regression är den enklaste approximationsmetoden
- De flesta ML-algoritmer bygger på samma idé: minimera fel
- Skillnaden ligger i modellens komplexitet och flexibilitet

Maskininlärning i grundform är generaliserad approximation,  
där modellen anpassas automatiskt utifrån data istället för att definieras manuellt.
