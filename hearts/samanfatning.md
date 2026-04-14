**Sammanfattning**

Detta projekt undersöker hur maskininlärningsmodeller kan användas för att diagnostisera hjärtsjukdom baserat på ett medicinskt dataset. Arbetet genomfördes stegvis, från rådata till färdig diagnostisk applikation.

Initialt analyserades datasetet i sitt ursprungliga skick, där flera problem identifierades, såsom otydliga kolumnnamn, kategoriska variabler och saknade värden. Därefter genomfördes datarensning och strukturering för att möjliggöra vidare analys.

Efter datarensning utfördes visualisering med hjälp av Seaborn för att förstå samband mellan variabler, exempelvis hur vissa typer av bröstsmärta korrelerar med förekomst av hjärtsjukdom. Dessa insikter användes som grund för modellval och vidare experiment.

Flera modeller testades, inklusive logistisk regression, k-NN, beslutsträd och Random Forest. Särskild uppmärksamhet ägnades åt modellernas prestanda, där både noggrannhet (accuracy) och felklassificeringar analyserades. Parametrar som antal grannar (k) och träddjup justerades för att optimera resultaten.

Resultaten visade att enklare modeller som logistisk regression och k-NN presterade lika bra eller bättre än mer komplexa modeller. Random Forest gav ingen signifikant förbättring, vilket tyder på att datasetets informationsinnehåll sätter en övre gräns för modellens prestanda.

Projektet avslutades med utvecklingen av en enkel diagnostisk modul (CLI), där användaren kan mata in patientdata och få en prediktion samt en sannolikhetsbedömning.

Slutligen reflekterar projektet över modellens begränsningar, såsom liten datamängd, potentiell bias och att resultaten inte direkt kan användas i klinisk praxis utan vidare validering.
