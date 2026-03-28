### Python: från språkets arkitektur till klasser

**1. Grundprincipen i Python**
En viktig idé i Python är: allt är objekt.<br>
Det betyder att nästan varje sak i språket representeras internt som ett objekt i minnet.

***Exempel:**
```
heltal
strängar
listor
funktioner
klasser
```
Alla dessa är objekt.
Till exempel:<br>
```x = 10```

Här är 10 ett objekt av typen int.
Vi kan kontrollera detta:
```
print(type(x))
Resultat:
<class 'int'>
```
Detta visar att värdet inte bara är ett tal utan ett objekt av klassen int.<br>
________________________________________
**2. Objekt och attribut**
   
Eftersom allt är objekt kan de ha:
attribut (data)
metoder (funktioner kopplade till objektet)
Exempel:<br>
```
text = "hello"
Objektet "hello" har metoder:
upper()
lower()
replace()
```
Exempel:<br>
```text.upper()```
Här anropas en metod som tillhör objektet.<br>
________________________________________

**3. Vad är egentligen en funktion i Python**
En funktion i Python är också ett objekt.
Exempel:
```
def add(a, b):
    return a + b
```
Vi kan skriva:
```
print(type(add))
```
Resultat:
```
<class 'function'>
```
Det betyder att funktionen själv är ett objekt.
Vi kan till exempel lägga en funktion i en variabel eller i en lista:
```
f = add
print(f(2,3))
```
________________________________________

**4. Iteration och objekt**
   
När vi använder konstruktioner som
```
for
filter
map
```
arbetar Python egentligen med objekt som implementerar vissa metoder.
Till exempel fungerar en for-loop eftersom objektet implementerar en iterator.
Internt använder Python metoder som:
```
__iter__()
__next__()
```
Exempel:
```
numbers = [1,2,3]

for n in numbers:
    print(n)
```
Bakom kulisserna gör Python ungefär detta:<br>
```
iterator = numbers.__iter__()
value = iterator.__next__()
```
Det betyder att iteration fungerar eftersom objektet innehåller vissa metoder.
________________________________________

**5. Specialmetoder i Python**

Python använder många speciella metoder som börjar och slutar med dubbla understreck.
Exempel:<br>
```
__init__
__str__
__len__
__iter__
__next__
```
Dessa kallas ofta special methods eller dunder methods.
De används av Python automatiskt.
Exempel:<br>
```
len(my_list)
Python gör egentligen:
my_list.__len__()
```
________________________________________

**6. Hur klasser passar in i denna arkitektur**

Eftersom allt i Python är objekt måste även objekt själva skapas från någon struktur.
Den strukturen är en klass.
En klass beskriver:
vilken data objektet har
vilka metoder objektet har
Man kan se en klass som en definition av en ny typ.
Exempel:
```
class Dog:
    pass
```
Nu har vi skapat en ny typ.
________________________________________

**7. Att skapa ett objekt**

När vi skriver:<br>
```
dog = Dog()
```

sker flera saker:<br>
1 Python skapar ett nytt objekt i minnet

2 Python anropar en speciell metod
```
__init__()
```
________________________________________

**8. Rollen av init**

Metoden __init__ används för att initialisera objektet.
Exempel:
```
class Dog:

    def __init__(self, name):
        self.name = name
```

När vi skriver:<br>
```
dog = Dog("Buddy")
```
gör Python ungefär detta:<br>

1 skapa objekt
2 anropa Dog.__init__(dog, "Buddy")
________________________________________

**9. Vad är self**
    
self är bara en referens till det aktuella objektet.
Det gör att metoden vet vilket objekt den arbetar med.
Exempel:<br>
```
dog1 = Dog("Buddy")
dog2 = Dog("Max")
```
Varje objekt får sina egna attribut:
```
dog1.name
dog2.name
```
________________________________________

**10. Sammanfattning**

Arkitekturen kan beskrivas i följande nivåer:

Python runtime<br>
    ↓<br>
allt är objekt<br>
    ↓<br>
objekt har attribut och metoder<br>
    ↓<br>
speciella metoder styr språkets beteende<br>
    ↓<br>
klasser definierar nya typer av objekt<br>
    ↓<br>
__init__ initialiserar objekt<br>
________________________________________

**11. Varför detta är viktigt**
    
Den objektorienterade modellen gör det möjligt att:<br>
organisera kod<br>
modellera verkliga system<br>
återanvända kod<br>
Men i Python är detta inte ett separat system - det är en naturlig konsekvens av språkets arkitektur där allt representeras som objekt.
