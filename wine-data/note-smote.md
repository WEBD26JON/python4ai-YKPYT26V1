# SMOTE · Synthetic Minority Over-sampling Technique

## Vad är SMOTE?

SMOTE är en metod för att hantera obalanserade dataset —
det vill säga dataset där vissa klasser är kraftigt
underrepresenterade jämfört med andra.

Till skillnad från enkel kopiering av befintliga rader
genererar SMOTE **syntetiska nya datapunkter** för den
underrepresenterade klassen.

## Hur fungerar det?

SMOTE tar två liknande poster från den lilla klassen
och skapar en ny post någonstans mellan dem i
feature-rymden.

<pre>
Post A:  alcohol=9.5, volatile acidity=0.6, sulphates=0.5
Post B:  alcohol=10.2, volatile acidity=0.7, sulphates=0.6
Syntetisk post (mitt emellan):
alcohol=9.85, volatile acidity=0.65, sulphates=0.55
</pre>

Resultatet är ett mer balanserat träningsset utan att
förlora information från den stora klassen.

## Relevans för wine-projektet

I wine-datasetet finns en tydlig klassimbalans:
<pre>
quality 3:   30 prover   (< 1%)
quality 4:  206 prover   (4%)
quality 5: 1752 prover   (33%)
quality 6: 2321 prover   (44%)
</pre>

Klasser 3 och 4 är kraftigt underrepresenterade.
Modellen tränas i praktiken nästan uteslutande på
quality 5–6 och lär sig dåligt att identifiera
lågkvalitetsviner.

SMOTE skulle kunna balansera träningsdatan och
förbättra modellens förmåga att känna igen
`ordinary`-klassen — särskilt de lägsta kvalitetsnivåerna.

## Implementering (Python)

Kräver biblioteket `imbalanced-learn`:

```bash
pip install imbalanced-learn
```

```python
from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state=42)
X_resampled, y_resampled = sm.fit_resample(X_train, y_train)

model.fit(X_resampled, y_resampled)
```

SMOTE appliceras **endast på träningsdatan** — aldrig
på testdatan, eftersom testdatan ska representera
verkliga förhållanden.

## Alternativ till SMOTE

- **Undersampling** — ta bort poster från den stora klassen
- **class_weight='balanced'** — inbyggt i sklearn,
  justerar modellens förlustfunktion utan att ändra datan
- **Kombinerad approach** — SMOTE + undersampling (SMOTEENN)

## Sammanfattning

SMOTE är ett verktyg för framtida förbättring av projektet.
Det implementerades inte i detta projekt men identifierades
som en relevant metod givet datasetets klassimbalans.

