## Modellval — motivering och jämförelse med hearts-projektet

### Varför inte Logistic Regression som primär modell?

I hearts-projektet gav Logistic Regression accuracy ~0.85–0.87.
Det fungerade bra där eftersom medicinska data (blodtryck, kolesterol,
EKG-värden) tenderar att vara linjärt separerbara — en rak gräns
räcker för att skilja sjuk från frisk.

Vindata är annorlunda. Sambandet mellan kemisk sammansättning och
kvalitetsklass är sannolikt icke-linjärt — exempelvis påverkar
alkohol och syra kvaliteten i kombination, inte var för sig.
Logistic Regression söker bara linjära gränser och passar därför
sämre för detta dataset.

Linear Regression används inte alls — den förutsäger ett kontinuerligt
tal, inte en klass, och är inte ett klassificeringsverktyg.

### Valda modeller för wine-projektet

**Decision Tree**
Samma modell som i hearts, men här används den för multiclass (3 klasser)
istället för binär klassificering. Enkel, tolkbar, visar direkt vilka
features som är viktigast (feature importance). Bra startpunkt.

**Random Forest**
Ensemble av Decision Trees. Mer robust mot överanpassning än ett
enskilt träd. Förväntas prestera bättre på vindata med mer brus
och icke-linjära samband än i hearts-projektet.

**k-NN**
Avståndbaserad modell. Kräver StandardScaler (som i hearts).
Intressant att jämföra — fungerar bra när liknande viner
verkligen har liknande kemisk profil.

### Jämförelsetabell

| Modell               | Hearts (binär) | Wine (3 klasser) |
|----------------------|----------------|------------------|
| Logistic Regression  | ~0.85–0.87     | ej primär        |
| Decision Tree        | ~0.80          | primär start     |
| Random Forest        | ingen tydlig   | förväntas bäst   |
|                      | förbättring    |                  |
| k-NN (k=11)          | bäst (~0.87)   | kräver scaling   |

I hearts-projektet var k-NN den bästa modellen.
I wine-projektet är hypotesen att Random Forest presterar bättre
på grund av datasetets komplexitet och fler klasser.