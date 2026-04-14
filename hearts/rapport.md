## Heart Disease Prediction Project

### Sammanfattning

Detta projekt undersöker hur maskininlärningsmodeller kan användas för att diagnostisera hjärtsjukdom baserat på ett medicinskt dataset. Arbetet genomfördes stegvis, från rådata till färdig diagnostisk applikation.

Initialt analyserades datasetet i sitt ursprungliga skick, där flera problem identifierades, såsom otydliga kolumnnamn, kategoriska variabler och saknade värden. Därefter genomfördes datarensning och strukturering för att möjliggöra vidare analys.

Flera modeller testades, inklusive logistisk regression, k-NN, beslutsträd och Random Forest. Resultaten visade att enklare modeller ofta presterade lika bra eller bättre än mer komplexa modeller.

Projektet avslutades med en enkel diagnostisk modul där användaren kan mata in patientdata och få en prediktion.

---

### Problem och dataset

Målet med projektet var att skapa en modell som kan klassificera om en patient har hjärtsjukdom eller inte baserat på medicinska parametrar.

Datasetet innehåller information om patienter, inklusive ålder, kön, blodtryck, kolesterol och resultat från olika tester. Målvariabeln (AHD) anger om hjärtsjukdom förekommer.

---

### Data preparation

Arbetet började med analys av rådata. Datasetet innehöll en indexkolumn som saknade analytiskt värde och därför togs bort.

Kategoriska variabler omvandlades till numeriskt format med hjälp av one-hot encoding. Saknade värden hanterades genom att rader med ofullständig information togs bort.

Efter rensning sparades datat som `heart_clean.csv`.

Två versioner av datat användes:

- **No scaling** – data i originalskala

- **Scaled** – data normaliserat med StandardScaler

Skalning användes eftersom vissa modeller är känsliga för skillnader i variablernas storlek.

---

### Logistic Regression

Logistisk regression valdes som första modell eftersom den är enkel och fungerar väl för binär klassificering.

Två varianter testades:

- Utan skalning – accuracy ≈ 0.87 (men konvergensproblem)

- Med skalning – accuracy ≈ 0.85 (stabil modell)

Trots något lägre accuracy ansågs den skalade modellen mer tillförlitlig.

---

### k-Nearest Neighbors (k-NN)

k-NN testades som alternativ modell baserad på avstånd mellan datapunkter.

Initialt användes standardvärden, vilket gav sämre resultat. Genom att testa flera värden på k (1–13) identifierades att:

- k = 11 gav bästa resultat

- lägre värden var instabila

- högre värden gav ingen förbättring

Den slutliga modellen använder därför **k = 11**.

---

### Decision Tree

Ett enskilt beslutsträd testades för att analysera modellens beteende.

Flera djup testades och det bästa resultatet uppnåddes vid:

- **depth = 3**

Trots detta var prestandan sämre än tidigare modeller.

---

### Random Forest

Random Forest testades som en förbättring av Decision Tree.

Djupet sattes till 3 baserat på tidigare resultat. Modellen gav dock ingen tydlig förbättring jämfört med enklare modeller.

Detta visar att ökad komplexitet inte alltid leder till bättre resultat.

---

### Utvärdering

Vid utvärdering analyserades inte bara accuracy utan även typen av fel.

Särskild vikt lades på **false negatives** (missade sjuka patienter), eftersom detta anses mer kritiskt än att felaktigt klassificera friska som sjuka.

---

### Bias och dataanalys

En enkel bias-analys genomfördes med hjälp av pandas.

Analysen visade att:

- datasetet är relativt balanserat

- män har högre andel hjärtsjukdom

- vissa variabler är ojämnt fördelade

Resultaten sparades i en rapportfil via ett loggsystem.

Metoden skulle kunna användas för hela projektet, men implementerades endast för denna del på grund av tidsbegränsningar.

---

### Praktisk tillämpning – diagnostik

En enkel CLI-baserad diagnostisk modul utvecklades.

Användaren kan mata in patientdata och få:

- klassificering (sjuk / frisk)

- sannolikhet för sjukdom

Tester visade att modellen ger rimliga och förväntade resultat.

---

### Reflektion

Projektet visar att enkla modeller ofta är tillräckliga för denna typ av data.

Begränsningar:

- datasetet är relativt litet

- bias kan påverka resultat

- modellen är inte validerad för verklig medicinsk användning

För framtida arbete kan följande förbättras:

- mer avancerad bias-analys

- större dataset

- bättre hyperparameteroptimering

- utökad diagnostisk funktionalitet

---

### Sammanfattande slutsats

Projektet demonstrerar hela processen från rådata till fungerande applikation.

Det visar tydligt att:

- datakvalitet är avgörande

- modellval påverkar resultatet

- enkelhet ofta är tillräcklig

- praktisk implementering är möjlig även med grundläggande verktyg
