# Steg 5 — Diagnostik (wine-test.py)

## Applikation: Gradio

Till skillnad från hearts-projektet där diagnostiken
kördes som ett CLI-verktyg i terminalen, använder
wine-projektet Gradio för ett webbaserat gränssnitt.

Gradio startas från terminalen:
```
python scripts/wine-diagnose.py
```
men öppnas automatiskt i webbläsaren på: http://127.0.0.1:7860 

Ingen installation av webbserver krävs — Gradio
hanterar detta internt. Applikationen körs lokalt
och kräver ingen internetuppkoppling.

## Gränssnittet

Inmatningsfälten är uppdelade i två kolumner:

**Nyckelparametrar (sliders):**
- Wine type: red / white (radio button)
- Alcohol, Volatile acidity, Sulphates (sliders
  med visuellt intervall)

**Kemisk sammansättning (number inputs):**
- Fixed acidity, Citric acid, Residual sugar,
  Chlorides, Free/Total SO₂, Density, pH
  (med angivna giltiga intervall i label)

Resultatet visas som Markdown med emoji-klassificering
i fyra nivåer baserat på sannolikhet för "high":
```
p_high ≥ 0.65  →  🏆 High quality
p_high ≥ 0.50  →  🥈 Good quality
p_high ≥ 0.35  →  🥉 Borderline case
p_high < 0.35  →  🍶 Ordinary wine
```
## Modellval — motivering

Samtliga modeller testades på binär klassificering
(ordinary / high) och tre klasser (low / medium / high).

Sammanfattning av bästa resultat per modell:

| Modell         | Data    | Best acc | Parametrar   |
|----------------|---------|----------|--------------|
| Random Forest  | binary  | 0.757    | depth=None   |
| Decision Tree  | binary  | 0.740    | depth=5      |
| k-NN           | binary  | 0.730    | k=7, k=11   |
| Random Forest  | 3 klass | 0.641    | depth=8      |
| Decision Tree  | 3 klass | 0.616    | depth=6      |
| k-NN           | 3 klass | 0.587    | k=15         |

**Random Forest med depth=None** valdes som modell
för diagnostiken eftersom den ger högst accuracy
på binär klassificering (0.757).

Till skillnad från hearts-projektet där k-NN var
bäst (0.87), presterar Random Forest bättre här.
Förklaringen är datasetets komplexitet: 11 kemiska
parametrar med icke-linjära samband passar bättre
för ett ensembleträd än för avståndbaserad k-NN.

Treklass-varianten (low / medium / high) testades
med alla tre modeller men gav konsekvent sämre
resultat (~0.12–0.15 lägre accuracy). Gränsen
mellan quality=5 och quality=6 är kemiskt otydlig
och ingen modell klarar att separera dem tillförlitligt.

## Begränsningar — disclaimer

Följande text visas i Gradio-gränssnittet:

> ⚠️ **Disclaimer**
> This model is trained on a limited dataset
> (5 320 samples after cleaning). Low-quality wines
> (quality 3–4) are significantly underrepresented
> (< 5% of data), which reduces the model's ability
> to reliably detect them. Results should be treated
> as indicative, not conclusive.
> Accuracy on test data: **0.757**

## Nästa steg
- wine-bias-report.py — fördelningsanalys
- README.md — projektdokumentation
- main.py — CLI-launcher för alla skript