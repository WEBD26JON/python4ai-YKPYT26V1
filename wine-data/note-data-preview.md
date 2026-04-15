# Steg 0 — Rådata (data-preview.py)

## Vad skriptet gör
Läser in rådatafilen med Pandas och skriver ut:
- `df.head()` — de första raderna
- `df.info()` — kolumntyper och antal icke-null värden
- `df.describe()` — statistisk sammanfattning

## Observationer

### Struktur
- 6 497 rader, 15 kolumner
- 11 float64, 3 int64, 1 str (color)
- Inga saknade värden

### Unnamed: 0
Kolumnen är ett gammalt index från två separata dataset
som slagits ihop (rött vin: 0–1598, vitt vin: 0–4897).
Indexet är alltså inte unikt globalt.
Tas bort i nästa steg — inget analytiskt värde.

### quality
- Intervall: 3–9
- Medelvärde: 5.82
- Majoriteten av vinerna ligger på 5–6
- Extremklasserna (3 och 9) är kraftigt underrepresenterade

### high_quality
- Binär kolumn (0/1), medelvärde ≈ 0.63
- Ca 63% av alla prover är märkta som "hög kvalitet"
- Trolig tröskel: quality ≥ 6
- Kolumnen är härled från quality — tas bort i prepare.py
  för att undvika data leakage

### alcohol / sulfur dioxide
- alcohol: 8.0–14.9 — relativt stor spridning
- total sulfur dioxide: stor variation mellan prover
- Skalning (StandardScaler) blir viktig för k-NN

## Nästa steg
wine-data-clean.py:
- Ta bort Unnamed: 0
- Bekräfta inga saknade värden (explicit)
- Kontrollera dubbletter
- Spara wine-data-clean.csv