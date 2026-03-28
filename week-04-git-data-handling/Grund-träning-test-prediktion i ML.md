# Grundläggande förståelse av träning, test och prediktion i Machine Learning

Den här delen förklarar samma workflow som i kursen, men utan att behandla funktionerna som “svarta lådor”. Fokus ligger på vad som faktiskt händer i varje steg.

---

# 📌 1. Dataset – utgångspunkt

Vi börjar med en enkel tabell:

| hours_studied | test_score |
| ------------- | ---------- |
| 1             | 52         |
| 2             | 55         |
| 3             | 60         |
| 4             | 65         |
| 5             | 71         |
| 6             | 76         |
| 7             | 82         |
| 8             | 88         |

- **Feature (X)** = input (hours_studied)

- **Target (y)** = output (test_score)

---

# 📌 2. Vad betyder träning och test?

## 🔹 Träning (training)

Modellen använder en del av datan för att hitta ett mönster.

## 🔹 Test (testing)

Modellen testas på data den **inte har sett tidigare**.

👉 Syfte:

- kontrollera om modellen fungerar på nya data

- inte bara på de data den redan sett

---

# 📌 3. Hur fungerar train/test split?

Kod:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
```

---

## 🔧 Vad händer bakom kulisserna

### 1. Data blandas (shuffle)

Original:

```
[1,2,3,4,5,6,7,8]
```

Efter blandning:

```
[5,2,8,1,7,3,6,4]
```

---

### 2. Data delas upp

- 75% → träning

- 25% → test

```
Train: första 6 rader
Test:  sista 2 rader
```

👉 Viktigt:

- train och test är olika rader

- modellen ser aldrig test-datan under träning

---

# 📌 4. Vad är en “modell” här?

Kod:

```python
model = LinearRegression()
```

👉 Detta skapar en matematisk modell:

```
y = a * x + b
```

Men:

- a och b är ännu okända

---

# 📌 5. Vad gör `.fit()`?

```python
model.fit(X_train, y_train)
```

👉 Det som sker:

- modellen tittar på datapunkterna

- beräknar den bästa linjen

Exempel:

```
a = 5.1
b = 47.2
```

👉 Resultat:

```
y = 5.1x + 47.2
```

---

## ❗ Viktigt

Detta är “träning”:

- inte intelligens

- inte minne

- bara matematik

---

# 📌 6. Vad gör `.predict()`?

```python
predictions = model.predict(X_test)
```

👉 Modellen använder formeln:

```
y = a * x + b
```

Exempel:

```
x = 7
y = 5.1 * 7 + 47.2 ≈ 82.9
```

---

# 📌 7. Vad är egentligen en prediktion?

Det är inte “gissning” i mänsklig mening.

👉 Det är:

> att använda en beräknad regel på nya värden

---

# 📌 8. Varför behövs testdata?

Om vi testar på samma data:

```python
model.predict(X_train)
```

👉 modellen blir nästan perfekt

MEN:

- den har redan sett datan

- resultatet är inte trovärdigt

---

## ✔️ Med testdata

```python
model.predict(X_test)
```

👉 modellen måste:

- använda sin regel

- på nya data

---

# 📌 9. Sammanfattning av hela flödet

## 🔁 Workflow (utan magi)

1. Läs in data

2. Välj X och y

3. Blanda data

4. Dela i train/test

5. Skapa modell (formel)

6. Fit → beräkna parametrar

7. Predict → använd formeln

8. Jämför med verkliga värden

---

# 📌 10. Nyckelinsikt

Det viktigaste att förstå:

> Machine Learning på denna nivå =  
> data + matematik + struktur

---

## ❌ Inte:

- intelligens

- “tänkande”

- komplex AI

---

## ✔️ Utan:

- mönster

- beräkning

- generalisering

---

# 📌 11. Varför detta är viktigt

Om detta inte är tydligt:

- blir biblioteket en “black box”

- parametrar känns slumpmässiga

- modellen känns mystisk

---

Om detta är tydligt:

👉 hela ML blir förutsägbart och logiskt

---

# 📌 Slut

Den här förståelsen är grunden för allt som kommer senare:

- klassificering

- k-NN

- beslutsträd

- neurala nätverk

Alla följer samma princip:

> lära från data → använda på ny data
