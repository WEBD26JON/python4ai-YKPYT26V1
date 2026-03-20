

## Venv. Skapa och aktivera en virtuell miljö (venv)

1. Skapa en virtuell miljö
```
python -m venv .venv
```
---

 2. Aktivera miljön

#### Git Bash / Linux / macOS:
```
source .venv/Scripts/activate
```
#### Windows PowerShell:
```
.\.venv\Scripts\Activate.ps1
```
#### Windows CMD:
```
.venv\Scripts\activate.bat
```

Navigering i sökvägar (kort)

- `.` = aktuell mapp
  
- `..` = en nivå upp
  
- `/` används i Git Bash / Linux / macOS
  
- `\` används i Windows (PowerShell / CMD)
  

**Exempel:**

Aktivera venv i samma mapp:
```
.\.venv\Scripts\Activate.ps1 # PowerShell  
source .venv/Scripts/activate # Git Bash
```
Aktivera venv från undermapp (t.ex. `sandbox`):
```
..\.venv\Scripts\Activate.ps1 # PowerShell  
source ../.venv/Scripts/activate # Git Bash
```
### 3. Kontrollera att miljön är aktiv

Prompten ska visa:
```
(.venv)
```
Kontrollera Python:
```
python -c "import sys; print(sys.executable)"
```
---

### 4. Installera paket
```
pip install flask
```
---

### 5. Spara beroenden
```
pip freeze > requirements.txt
```
---

### 6. Avsluta miljön
```
deactivate
```
---

## Viktigt

- `cd .venv` aktiverar inte miljön
  
- Du måste köra aktiveringsskriptet
  
- Varje projekt bör ha sin egen `.venv`
  

---

Kort sammanfattning:

> Skapa → Aktivera → Installera → Arbeta → Deaktivera
