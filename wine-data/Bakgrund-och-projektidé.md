**Wine Quality Project**

Projektanteckningar — Dataanalys och Tankegång

Alexander Soviet9773Red · ITHS · Python-for-ai

# **1. Bakgrund och projektidé**

Idén till projektet kom från ett praktiskt scenario: en kund läser etiketten på en vinflaska och ser den kemiska sammansättningen. Utifrån dessa parametrar ska det vara möjligt att klassificera vinets kvalitetsnivå.

Om modellens förutsägelse inte stämmer överens med vinets deklarerade klass — exempelvis att ett vin märkt som 'premium' klassificeras som medelmåttigt — kan detta indikera en förfalskning eller ett felaktigt märkt vin.

Projektet är alltså inte bara en akademisk övning, utan har en tydlig potentiell tillämpning inom livsmedelskontroll och konsumentskydd.

# **2. Dataset — Struktur och första observation**

## **2.1 Källa**

[datasets/red-wine.csv at master · bencmbit/datasets · GitHub](https://github.com/bencmbit/datasets/blob/master/red-wine.csv "https://github.com/bencmbit/datasets/blob/master/red-wine.csv")

Datasetet innehåller kemisk analys av röda och vita viner från Portugals Vinho Verde-region. Totalt 6 497 prover.

- 1 599 röda viner

- 4 898 vita viner

## **2.2 Kolumner (features)**

Alla features är numeriska och representerar kemiska mätvärden:

- fixed acidity — fast syrahalt
- volatile acidity — flyktig syra (hög halt = negativ smak)
- citric acid — citronsyra
- residual sugar — kvarvarande socker efter jäsning
- chlorides — kloridinnehåll
- free sulfur dioxide — fritt svaveldioxid (konserveringsmedel)
- total sulfur dioxide — totalt svaveldioxid
- density — densitet
- pH — surhetsgrad
- sulphates — sulfater
- alcohol — alkoholhalt i procent

## **2.3 Möjliga målvariabler (Target-kandidater)**

- quality (3–9) — sensorisk bedömning av experter, heltalsvärd
- high_quality (0/1) — binär, förmodligen quality ≥ 6
- color (red/white) — vinets typ

Viktigt att notera: high_quality är en variabel som redan är härledd från quality. Om quality används som target måste high_quality tas bort från features för att undvika data leakage.

# **3. Val av Target och klassificeringstyp**

## **3.1 Problemet med quality som råvariabel**

Fördelningen av quality-värden är kraftigt obalanserad:

- Klass 3: 30 prover
- Klass 9: 5 prover
- Klass 5–6: majoriteten (~77%)

En modell som tränas direkt på quality (3–9) kommer att ignorera extremklasserna och bara lära sig att förutsäga 5 eller 6. Det ger hög accuracy men dålig praktisk nytta.

## **3.2 Beslut: omgruppering till 3 klasser**

Lösningen är att slå ihop quality-värdena till tre meningsfulla klasser:

- low — quality 3–4
- medium — quality 5–6
- high — quality 7–9

Detta ger en rimligare klassbalans och matchar verkligheten bättre: vin klassificeras i praktiken sällan med exakt poäng, utan placeras i kategorier som 'enkel', 'godkänd' och 'premium'.

## **3.3 Klassificeringstyp**

Med tre klasser är detta en multiclass classification-uppgift — till skillnad från hearts-projektet som använde binär klassificering.

Alla planerade modeller (Decision Tree, Random Forest, k-NN) stödjer multiclass utan ändringar. Logistic Regression fungerar också via one-vs-rest, men är inte prioriterad i detta projekt.

# **4. Features och förberedelse**

## **4.1 color som feature**

Kolumnen color (red/white) behålls som feature. Det är logiskt: kunden vet vilket vin det handlar om, och kemisk sammansättning skiljer sig systematiskt mellan röda och vita viner.

color kodas om med one-hot encoding eller label encoding inför modellträning.

## **4.2 Vad tas bort**

- Unnamed: 0 — indexkolumn, inget analytiskt värde
- high_quality — härledd från quality, skapar data leakage

## **4.3 Skalning**

Kemiska features har olika skalor (t.ex. alcohol 8–15, total sulfur dioxide 0–300). Skalning med StandardScaler är nödvändig för k-NN och förbättrar konvergens för Logistic Regression. Decision Tree och Random Forest är skalningsoberoende.

# **5. Modellval**

Projektet fokuserar på tre modeller som alla stödjer multiclass classification:

## **Decision Tree**

Enkel, tolkbar modell. Bra för att förstå vilka features som är viktigast. Tenderar att överanpassa vid stort djup — max_depth justeras experimentellt.

## **Random Forest**

Ensemble av Decision Trees. Mer robust mot överanpassning. Förväntas prestera bättre på detta dataset med mer brus än hearts-datasetet.

## **k-Nearest Neighbors (k-NN)**

Avståndbaserad modell. Kräver skalning. Känslig för irrelevanta features. Intressant att jämföra med Random Forest på ett kemiskt dataset.

# **6. Pipeline**

- wine-raw-preview.py — rådata, shape, info, describe
- wine-data-clean.py — ta bort onödiga kolumner, kontrollera saknade värden
- wine-prepare.py — skapa quality_class (low/medium/high), one-hot encoding, ta bort high_quality
- wine-vis.py — visualisering med Matplotlib (ej Seaborn)
- wine-tree.py — Decision Tree, testa olika djup
- wine-rf.py — Random Forest
- wine-knn.py — k-NN med skalning
- wine-bias-report.py — fördelningsanalys
- wine-diagnose.py — CLI: mata in kemiska värden, få kvalitetsklass

# **7. Lärandemål för detta projekt**

- Matplotlib istället för Seaborn — mer kontroll, mer explicit kod
- Multiclass classification — metrics, confusion matrix för 3 klasser
- Djupare dataanalys — fördelningar, korrelationer, feature importance
- Mer medveten pipeline — varje steg motiveras, inte bara kopieras

Utkast · April 2026
