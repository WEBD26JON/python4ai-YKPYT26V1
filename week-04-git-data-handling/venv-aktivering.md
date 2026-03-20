## 🛠 Problem med aktivering av venv i PowerShell (Windows)

När man försöker aktivera en virtuell miljö (`venv`) i PowerShell kan följande fel uppstå:

running scripts is disabled on this system

Detta beror på att PowerShell som standard blockerar körning av `.ps1`-skript av säkerhetsskäl.


## ✔️ Manuell hantering

Kör följande kommando i PowerShell:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Detta:

- gäller endast för aktuell terminalsession
  
- ändrar inte systemets globala säkerhetsinställningar
  
- är säkert att använda i utvecklingssammanhang
  

Efter det kan den virtuella miljön aktiveras:

.\.venv\Scripts\Activate.ps1

Om du redan befinner dig i `.venv`-mappen:

.\Scripts\Activate.ps1

---

## ✔️ Kontroll

Efter aktivering ska prompten ändras till:

(.venv) PS ...

Detta visar att den virtuella miljön är aktiv.

---

## 🔁 Alternativ (utan PowerShell-policy)

Om man vill undvika detta helt kan man använda:

### CMD (kommandotolk)

.\.venv\Scripts\activate.bat

### Direkt anrop av Python

.\.venv\Scripts\python.exe script.py


## 📌 Notering

Problemet är inte relaterat till Python eller `venv` i sig, utan till PowerShells säkerhetsmodell. Det är en vanlig källa till förvirring, särskilt i utbildningsmiljöer där detta inte alltid förklaras tydligt.


## ⚙️ Automatisk hantering av venv i VSCode

Istället för att manuellt aktivera `venv` varje gång kan Visual Studio Code hantera detta automatiskt.

### ✔️ Välj Python-interpreter (engångsinställning)

Öppna kommandopaletten:

Ctrl + Shift + P

Skriv och välj:

Python: Select Interpreter

Välj din virtuella miljö:

..\.venv\Scripts\python.exe


### ✔️ Resultat

Efter detta:

- VSCode använder automatiskt rätt Python (från `.venv`)
  
- Terminalen aktiveras ofta automatiskt
  
- Körning via "Run" eller "Play"-knappen använder korrekt miljö
  

### 📌 Viktigt att förstå

VSCode "aktiverar" inte venv på samma sätt som PowerShell-kommandot.  
Istället pekar den direkt på rätt Python-interpreter.

Detta innebär att:

- du slipper manuella kommandon
  
- miljön fungerar korrekt även utan synlig `(.venv)` i prompten
  

## 🔁 Alternativ utan aktivering (direkt anrop)

Man kan helt hoppa över aktivering och köra direkt:

.\.venv\Scripts\python.exe pandas_test.py

Detta är:

- tekniskt mer förutsägbart
  
- oberoende av terminal och shell
  
- vanligt i automatiserade scripts och CI/CD
  

---

## 📌 Slutsats

Manuell aktivering av `venv` behövs inte alltid.  
I praktiken finns tre arbetssätt:

1. Manuell aktivering (klassisk metod)
  
2. VSCode interpreter (rekommenderad i utveckling)
  
3. Direkt anrop av python.exe (stabilast tekniskt)
