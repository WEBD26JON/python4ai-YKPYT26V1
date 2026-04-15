# Steg 2 — Dataförberedelse (data-prepare.py)

#### Datastruktur (data)
```
Data types:
data/
├── wine-data-raw.csv       # raw data
├── wine-clean.csv          # after data-clean.py
├── wine-prepared-3.csv     # three quality classes: low / medium / high
└── wine-prepared-2.csv     # binary quality classes: ordinary / high
```

## Vad skriptet gör
Läser wine-clean.csv, skapar target-kolumn (quality_class),
kodar kategoriska variabler, tar bort quality-råkolumnen
och sparar två separata filer för olika klassificeringsuppgifter.

## Åtgärder

### Borttagna kolumner
- `quality` — ersätts av `quality_class` (target)
- `color` — kodas om via one-hot encoding eller label encoding

### Target — två varianter

**Variant 1 — tre klasser (wine-prepared-3.csv)**
```
bins:   [2, 5, 6, 9]
low     = quality 3–5  →  1988 rader  (37%)
medium  = quality 6    →  2323 rader  (44%)
high    = quality 7–9  →  1009 rader  (19%)
```
Obalans finns men är hanterbar.
Gränsen mellan low/medium (5→6) är kemiskt tunn — 
modellen kan ha svårt att skilja dessa klasser åt.

**Variant 2 — binär (wine-prepared-2.csv)**
```
bins:   [2, 5, 9]
ordinary  = quality 3–5  →  1988 rader  (37%)
high      = quality 6–9  →  3332 rader  (63%)
```
Enklare uppgift, bättre balans.
Används som fallback om tre klasser ger dåligt resultat.

### Encoding av color
`color` (red/white) är en kategorisk variabel.
Kodas till numeriskt värde inför modellträning:
```python
df["color"] = df["color"].map({"red": 0, "white": 1})
```

## Strategi
Startar med wine-prepared-3.csv och Decision Tree.
Confusion matrix visar var modellen förväxlar klasser.
Om low-klassen är svår att förutsäga — byt till binär variant
utan att skriva om modellskripten (ändra bara filnamnet).

## Observation: residual sugar
Extrem outlier (max=65.8) borttagen i data-clean.py.
Tröskel: residual sugar > 30 → tas bort.
Motiv: sannolikt mätfel eller dessertvin utanför datasetets scope.

Resultat: /outputs/clases-wine.log

## Nästa steg
wine-tree.py — Decision Tree på wine-prepared-3.csv:
- Testa olika max_depth
- Analysera confusion matrix för tre klasser
- Identifiera vilka klasser som förväxlas
