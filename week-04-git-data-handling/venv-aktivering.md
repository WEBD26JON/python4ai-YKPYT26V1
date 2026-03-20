## 🛠 Problem med aktivering av venv i PowerShell (Windows)

När man försöker aktivera en virtuell miljö (`venv`) i PowerShell kan följande fel uppstå:

running scripts is disabled on this system

Detta beror på att PowerShell som standard blockerar körning av `.ps1`-skript av säkerhetsskäl.

---

### ✔️ Tillfällig lösning (rekommenderad)

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

---

## 📌 Notering

Problemet är inte relaterat till Python eller `venv` i sig, utan till PowerShells säkerhetsmodell. Det är en vanlig källa till förvirring, särskilt i utbildningsmiljöer där detta inte alltid förklaras tydligt.
