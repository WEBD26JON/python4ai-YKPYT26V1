Bias i datasetet analyserades genom att studera fördelningen av variabler.

Exempelvis observerades att vissa kategorier var ojämnt representerade, såsom "asymptomatic" i bröstsmärta, vilket kan påverka modellens inlärning. Även vissa värden i variabeln "Thal" förekom mycket sällan, vilket kan leda till sämre generalisering för dessa fall.

Vidare analyserades fördelningen mellan målklasserna (AHD), som visade sig vara relativt balanserad, vilket är positivt för modellens prestanda.

Ingen avancerad bias-analys genomfördes, men grundläggande statistisk analys användes för att identifiera potentiella snedfördelningar i datat.


hearts-bias-report.py



Analysen visar att datasetet är relativt balanserat mellan klasserna, vilket är positivt för modellens prestanda.

Samtidigt finns tydliga snedfördelningar i vissa variabler. Exempelvis är andelen män betydligt högre i gruppen med hjärtsjukdom, vilket kan leda till bias i modellen. Även ålder visar en tydlig skillnad mellan grupperna, där patienter med sjukdom är äldre i genomsnitt.

Vissa variabler, såsom typ av bröstsmärta och resultat från thal-testet, uppvisar starka samband med hjärtsjukdom. Dessa variabler fungerar snarare som viktiga prediktorer än bias.

Sammanfattningsvis innehåller datasetet både informativa variabler och potentiella bias, vilket bör beaktas vid tolkning av modellens resultat.


