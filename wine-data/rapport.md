# Wine Quality Classifier
### Python för AI-utveckling · YKPYT26V1

Läs även [README.md](README.md) och [project-structure](project-structure.txt)

---

## Problem och dataset

Målet är att klassificera kvaliteten på vin utifrån dess kemiska
sammansättning. Inspirationen kommer från ett praktiskt scenario:
en kund läser etiketten och vill verifiera att vinets kemiska profil
stämmer överens med den deklarerade kvalitetsklassen.
Om modellens förutsägelse avviker från etiketten kan det tyda på
förfalskning eller felaktig märkning.

**Dataset:** Wine Quality Dataset — red and white wines, Vinho Verde, Portugal.<br>
Source: [github.com/bencmbit/datasets](https://github.com/bencmbit/datasets/blob/master/red-wine.csv)<br>
6 497 prover, 11 kemiska parametrar, ingen saknad data.

**Uppgiftstyp:** Binär klassificering —
`ordinary` (quality 3–5) vs `high` (quality 6–9).

---

## Dataförberedelse

Rådata innehöll en redundant indexkolumn (`Unnamed: 0`) och en
härledd kolumn (`high_quality` = quality ≥ 6) som togs bort för
att undvika data leakage.

1 177 dubbletter identifierades och togs bort (6 497 → 5 320 rader).
En extrem outlier i `residual sugar` (max=65.8 vid medelvärde=5.0)
togs bort som sannolikt mätfel (tröskel: > 30).

Kategorisk variabel `color` (red/white) kodades till 0/1.
Målvariabeln skapades med `pd.cut()`:
```
ordinary = quality 3–5  →  1 988 prover (37%)
high     = quality 6–9  →  3 330 prover (63%)
```
Skalning med `StandardScaler` användes för k-NN.
Decision Tree och Random Forest är skalningsoberoende.

**Visualisering:** Boxplots (Matplotlib) för `alcohol`,
`volatile acidity` och `sulphates` mot quality visade tydliga
samband — särskilt alkoholhalt som stiger konsekvent med kvalitet.

---

## Modeller och resultat

Tre modeller testades med hyperparametertuning (se även [compare.txt](compare.txt):

| Modell         | Best accuracy | Parametrar  |
|----------------|---------------|-------------|
| Random Forest  | **0.757**     | depth=None  |
| Decision Tree  | 0.740         | depth=5     |
| k-NN           | 0.730         | k=7, k=11   |

Treklass-varianten (low/medium/high) testades parallellt men gav
konsekvent ~0.12–0.15 lägre accuracy. Gränsen mellan quality=5
och quality=6 är kemiskt otydlig och ingen modell klarar att
separera dem tillförlitligt.

**Random Forest (depth=None)** valdes som slutlig modell.
Till skillnad från hearts-projektet där k-NN presterade bäst (0.87),
ger Random Forest bättre resultat här. Förklaringen är datasetets
komplexitet: 11 kemiska parametrar med icke-linjära samband passar
bättre för ett ensembleträd.

---

## Utvärdering

Bästa modell (Random Forest, binary, depth=None):
<pre>
CONFUSION MATRIX:
[[713 120]
 [203 294]]
precision  recall  f1-score  support
high       0.78    0.86      0.82      833
ordinary   0.71    0.59      0.65      497
accuracy                     0.76      1330
</pre>

<pre>
high  ordinary
high        [ 713    120 ]   → recall = 713/833 = 0.856 ≈ 0.86  ✅
ordinary    [ 203    294 ]   → recall = 294/497 = 0.591 ≈ 0.59  ✅
</pre>

Modellen hittar kvalitetsviner bra (recall 0.86) men missar
en del ordinära viner (recall 0.59). Detta beror på klassimbalansen
— 63% av datasetet är märkt som "high".

---

## Bias och begränsningar

- **Klassimbalans:** quality 3–4 utgör < 5% av data (236 prover).
  Modellen är tränad främst på quality 5–6 och är mindre tillförlitlig
  för extremklasserna.
- **Geografisk bias:** datasetet kommer uteslutande från Vinho Verde-
  regionen i Portugal. Resultaten generaliseras inte nödvändigtvis
  till viner från andra regioner.
- **Färgfördelning:** vita viner är ~3× fler än röda (3 961 vs 1 359
  efter rensning), vilket kan ge asymmetrisk prestanda per vintyp.
- **Subjektiv målvariabel:** quality-betyget är en sensorisk bedömning
  av experter och inte ett objektivt kemiskt mått.

---

## Praktisk tillämpning

En webbaserad diagnostisk applikation utvecklades med **Gradio**.
Användaren matar in kemiska parametrar via sliders och inputfält
och får ett klassificeringssvar med sannolikhet i fyra nivåer:
<pre>
🏆 High quality    p ≥ 0.65
🥈 Good quality    p ≥ 0.50
🥉 Borderline      p ≥ 0.35
🍶 Ordinary        p < 0.35
</pre>

Applikationen körs lokalt: `python scripts/wine-diagnose.py`
och öppnas automatiskt i webbläsaren på `http://127.0.0.1:7860`.

---

## Reflektion och förbättringsförslag

Projektet visar att datakvalitet och målvariabelns utformning
är avgörande för modellens prestanda. Accuracy 0.757 är ett
rimligt resultat givet datasetets begränsningar.

Möjliga förbättringar:
- Större och mer balanserat dataset
- [SMOTE](note-smote.md) eller undersampling för att hantera klassimbalans
- Feature importance-analys för att reducera irrelevanta parametrar
- Validering på viner från andra regioner

---

## Pipeline
<pre>
wine-data-raw.csv
→ data-preview.py    # rådata, struktur, statistik
→ data-clean.py      # rensning, dubbletter, outliers
→ data-vis.py        # visualisering (Matplotlib)
→ data-prepare.py    # encoding, target, sparar CSV-varianter
→ dtree.py           # Decision Tree, depth 2–None
→ knn.py             # k-NN, k 1–15, StandardScaler
→ rf.py              # Random Forest, depth 2–None
→ wine-test.py       # Gradio-applikation
</pre>
