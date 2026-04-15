# Steg 1 — Datarensning (data-clean.py)

## Vad skriptet gör
Läser rådata, analyserar struktur före och efter rensning,
tar bort onödiga kolumner, hanterar saknade värden och
dubbletter, sparar wine-clean.csv.

## Åtgärder

### Borttagna kolumner
- `Unnamed: 0` — gammalt index utan analytiskt värde
- `high_quality` — härledd från quality (quality >= 6 → 1),
  tas bort för att undvika data leakage

### Saknade värden
Inga saknade värden i datasetet. dropna() tar bort noll rader.

### Dubbletter
- Totalt funna: 1 177 (med keep="first")
- Totalt markerade (keep=False): 2 169
  (white: 1 709, red: 460)
- Skillnaden 992 = antal unika grupper av dubbletter
- Fördelningen red/white är proportionell före och efter
- Efter rensning: 6 497 → 5 320 rader

## NaN i describe(include="all")
Inte ett dataproblem. Pandas fyller NaN där en metrik
inte är tillämplig — exempelvis mean för string-kolumner
eller top/freq för numeriska kolumner.
Lösning: använd describe() och describe(include=["str"])
separat för tydligare utskrift.

## Observation: uteliggare
residual sugar: max=65.8, medelvärde=5.0, median=2.7
Tydlig uteliggare. Hanteras inte i detta steg men
noteras inför visualisering och analys.

## Resultat
wine-clean.csv: 5 318 rader, 13 kolumner
Red: 1 359 | White: 3 961