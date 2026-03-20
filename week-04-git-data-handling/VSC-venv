## ⚠️ Viktigt: VSCode och venv fungerar oberoende av terminalen

I VSCode finns två separata mekanismer:

1. **Terminal (PowerShell / CMD)**
  
2. **Python Interpreter (VSCode-inställning)**
  

De är **inte synkroniserade automatiskt**.


### 🔍 Standardbeteende

Som standard använder VSCode systemets Python:

C:\Users\<user>\AppData\Local\Programs\Python\Python3xx\python.exe

Om inget ändras körs all kod med denna interpreter.


### ✔️ Rekommenderad inställning per projekt

För varje projekt bör man manuellt välja interpreter:

Ctrl + Shift + P  
Python: Select Interpreter

Och välja:

<project>\.venv\Scripts\python.exe


### 📌 Viktigt att förstå

- `deactivate` påverkar **endast terminalen**
  
- VSCode fortsätter använda vald interpreter oberoende av detta
  
- Prompten `(.venv)` är **inte en pålitlig indikator i VSCode**
  



### ⚠️ Vanlig missuppfattning

Att arbeta med flera projekt kräver **inte flera IDE:er**.

VSCode hanterar detta korrekt eftersom:

- varje projekt har egen `.venv`
  
- varje workspace sparar sin interpreter
  
- VSCode växlar automatiskt mellan dem
  


### ✔️ Hur flera projekt fungerar i praktiken

Struktur:

project1/  
 .venv/

project2/  
 .venv/

VSCode kommer:

- använda `.venv` i project1 när den mappen är öppen
  
- använda `.venv` i project2 när du öppnar den mappen
  


### 📌 Slutsats

- venv är per projekt
  
- interpreter är per workspace
  
- terminal är separat
