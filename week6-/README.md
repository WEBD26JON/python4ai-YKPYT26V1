## Learning Path

### 01. k-NN Classification

   Recall Questions<br>
What is the difference between classification and regression?<br>
What do features and target mean in this week's examples?<br>
What does n_neighbors=3 mean in clear words?<br>
Why can stratify=y be useful in classification?<br>
Why can feature scale matter for k-NN?<br>

#### 1. Skillnad mellan classification och regression

- **Classification**: förutsäger en kategori (t.ex. pass / fail)
- **Regression**: förutsäger ett numeriskt värde (t.ex. poäng eller pris)
  

#### 2. Vad betyder features och target?

- **Features (X)**: indata som används för att göra en prediktion
- **Target (y)**: det värde eller den kategori som ska förutsägas
  
#### 3. Vad betyder n_neighbors=3?

- Modellen tittar på de **3 närmaste datapunkterna**
- Resultatet bestäms genom majoritetsbeslut

#### 4. Varför är stratify=y användbart?

- Ser till att **fördelningen av klasser** är liknande i train och test
- Ger en mer rättvis och stabil utvärdering<br>
Det hjälpte att förstå att `train_test_split()` inte enbart delar datasetet, utan vanligtvis först blandar raderna för att göra testet mer rättvist.<br>
Syntax. `from sklearn.model_selection import train_test_split`
  
#### 5. Varför spelar feature scale roll i k-NN?

- k-NN använder **avstånd** för att jämföra data
- Stora värden kan dominera små
- Därför behöver data ofta **skalning (normalisering)**

k-NN fungerar genom att jämföra nya data med liknande exempel och fatta beslut baserat på närhet, inte på förståelse eller logik.

---

### 02. Decision Trees

### 03. Metrics and Cross-Validation

### 04. Integration: Compare Classification Models

### Week 6 Completion Checklist
