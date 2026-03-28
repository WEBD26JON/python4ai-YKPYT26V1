
-   Pythons grundarkitektur
    
-   att allt är objekt
    
-   funktioner och variabler som objekt
    
-   specialmetoder
    
-   klasser
    
-   varför `__init__`, `__str__`, `__len__`, `__iter__` och `__next__` finns
    

Du kan använda texten både för egna anteckningar och som underlag i diskussion med läraren.

* * *

**Från Pythons arkitektur till klasser och specialmetoder**

**1\. Grundidén i Python**

En av de viktigaste idéerna i Python är:

**nästan allt är objekt.**

Det betyder att värden, funktioner, listor, strängar och även klasser behandlas som objekt i språkets modell.

Exempel:

x = 10  
text = "hej"  
nums = \[1, 2, 3\]

Alla dessa är objekt.

Vi kan kontrollera typen:

print(type(x))  
print(type(text))  
print(type(nums))

Resultat:

<class 'int'>  
<class 'str'>  
<class 'list'>

Alltså: ett heltal i Python är inte bara "ett tal". Det är ett objekt av typen `int`.  
En sträng är ett objekt av typen `str`.  
En lista är ett objekt av typen `list`.

Detta är en viktig utgångspunkt, eftersom klasser inte är något främmande tillägg ovanpå Python. De växer naturligt fram ur samma modell.

* * *

**2\. Objekt har data och beteende**

Ett objekt kan ha:

-   **attribut** - data som hör till objektet
    
-   **metoder** - funktioner som hör till objektet
    

Exempel med en sträng:

text = "hello"  
print(text.upper())

Här är `"hello"` ett objekt, och `upper()` är en metod som tillhör det objektet.

Man kan säga att Python ofta arbetar enligt modellen:

objekt.någonting

där `någonting` kan vara ett attribut eller en metod.

* * *

**3\. Även funktioner är objekt**

I Python är även funktioner objekt.

Exempel:

def add(a, b):  
    return a + b  
  
print(type(add))

Resultat:

<class 'function'>

Det betyder att en funktion kan behandlas som ett vanligt objekt.  
Man kan till exempel lagra den i en variabel:

f = add  
print(f(2, 3))

Alltså är en funktion i Python inte bara "kod som körs". Den är också ett objekt som kan skickas runt, sparas och användas senare.

Detta är viktigt, eftersom det visar att Python har en ganska enhetlig arkitektur: samma objektidé gäller på många nivåer.

* * *

**4\. Python-syntax är ofta bara en förenklad yta**

När man börjar programmera ser det ofta ut som att Python har många separata "magiska" konstruktioner:

print(x)  
len(nums)  
  
for n in nums:  
    print(n)

Men bakom denna syntax använder Python ofta objektens egna metoder.

Det innebär att språkets syntax ofta bara är ett bekvämt sätt att anropa särskilda metoder på objekt.

Det är här specialmetoderna kommer in.

* * *

**5\. Specialmetoder**

Specialmetoder är metoder med dubbla understreck före och efter namnet, till exempel:

\_\_init\_\_  
\_\_str\_\_  
\_\_len\_\_  
\_\_iter\_\_  
\_\_next\_\_

De kallas ofta:

-   **special methods**
    
-   **dunder methods** ("double underscore")
    

De anropas ofta inte direkt av programmeraren, utan **automatiskt av Python** när man använder viss syntax.

Det är därför de är så viktiga: de kopplar ihop objekt med språkets inbyggda konstruktioner.

* * *

**6\. `__init__` - används när ett objekt skapas**

När man skriver:

class Dog:  
    def \_\_init\_\_(self, name):  
        self.name = name  
  
dog = Dog("Buddy")

då händer i princip detta:

1.  Python skapar ett nytt objekt
    
2.  Python anropar `__init__` för att ge objektet sitt startläge
    

Man kan tänka ungefär så här:

Dog.\_\_init\_\_(dog, "Buddy")

`__init__` används alltså för att **initiera objektet**, det vill säga ge det startvärden.

**Rollen av `self`**

`self` är en referens till det aktuella objektet.

I exemplet ovan betyder:

self.name = name

att namnet sparas i just det objekt som håller på att skapas.

Om vi skapar två objekt:

dog1 = Dog("Buddy")  
dog2 = Dog("Max")

så får varje objekt sitt eget värde på `name`.

* * *

**7\. `__str__` - används när objektet ska visas som text**

Om man skriver ut ett objekt:

print(dog)

så försöker Python få fram en textrepresentation av objektet.

Om klassen innehåller `__str__`, används den:

class Dog:  
    def \_\_init\_\_(self, name):  
        self.name = name  
  
    def \_\_str\_\_(self):  
        return f"Dog named {self.name}"  
  
dog = Dog("Buddy")  
print(dog)

Resultat:

Dog named Buddy

Om `__str__` inte finns, visas ofta något tekniskt och mindre användbart, till exempel objektets adress i minnet.

Alltså:

-   `__str__` används av `print(objekt)`
    
-   också av `str(objekt)`
    
-   och ofta i f-strängar
    

Det är objektets **mänskligt läsbara textform**.

* * *

**8\. `__len__` - används av `len(...)`**

Om man skriver:

len(obj)

så försöker Python anropa:

obj.\_\_len\_\_()

Exempel:

class Team:  
    def \_\_init\_\_(self, members):  
        self.members = members  
  
    def \_\_len\_\_(self):  
        return len(self.members)  
  
team = Team(\["Anna", "Bob", "Eva"\])  
print(len(team))

Resultat:

3

Detta betyder att objektet beter sig som något som har en storlek eller längd.

`__len__` används alltså när objektet ska fungera som en slags container.

* * *

**9\. `__iter__` - används när objektet ska kunna itereras**

Om man skriver:

for x in obj:  
    ...

måste Python först kunna få en iterator från objektet.

Det görs via:

obj.\_\_iter\_\_()

Exempel:

class Numbers:  
    def \_\_init\_\_(self):  
        self.data = \[1, 2, 3\]  
  
    def \_\_iter\_\_(self):  
        return iter(self.data)  
  
nums = Numbers()  
  
for n in nums:  
    print(n)

Här gör `__iter__` att objektet kan användas i en `for`\-loop.

Det betyder att objektet är **itererbart**.

* * *

**10\. `__next__` - används för att hämta nästa värde i en iteration**

När iterationen väl har börjat behöver Python kunna hämta nästa element, ett i taget.

Det görs med:

\_\_next\_\_()

Ett enkelt exempel:

class Counter:  
    def \_\_init\_\_(self):  
        self.current = 0  
  
    def \_\_iter\_\_(self):  
        return self  
  
    def \_\_next\_\_(self):  
        if self.current < 3:  
            self.current += 1  
            return self.current  
        raise StopIteration

Om vi skriver:

c = Counter()  
  
for x in c:  
    print(x)

så händer ungefär detta:

1.  Python anropar `c.__iter__()`
    
2.  Python anropar sedan `__next__()` om och om igen
    
3.  när `StopIteration` kastas avslutas loopen
    

`__next__` används alltså i iteratorer för att leverera nästa värde.

* * *

**11\. Sambandet mellan syntax och specialmetoder**

Här blir den stora bilden tydlig.

Det som ser ut som vanlig Python-syntax är ofta kopplat till specialmetoder:

obj = MyClass()        -> \_\_init\_\_  
print(obj)             -> \_\_str\_\_  
len(obj)               -> \_\_len\_\_  
  
for x in obj:          -> \_\_iter\_\_ och \_\_next\_\_

Alltså:

**Python-syntax -> specialmetod -> objektets beteende**

Detta är en mycket viktig idé.  
Den visar att klasser i Python inte bara är "en skolövning i OOP", utan ett sätt att ansluta sina egna objekt till hur språket fungerar.

* * *

**12\. Hur detta leder fram till klasser**

Eftersom nästan allt i Python är objekt behöver det också finnas ett sätt att definiera **nya typer av objekt**.

Det är just det en klass gör.

En klass beskriver:

-   vilka attribut ett objekt ska ha
    
-   vilka metoder objektet ska ha
    
-   vilka specialmetoder objektet ska stödja
    

Exempel:

class Dog:  
    def \_\_init\_\_(self, name):  
        self.name = name  
  
    def \_\_str\_\_(self):  
        return f"Dog({self.name})"

Här definierar klassen en ny typ av objekt.

När vi sedan skapar ett objekt:

dog = Dog("Buddy")

så får vi ett konkret exemplar, en **instans**, av klassen.

* * *

**13\. Varför detta kan kännas svårt i början**

Problemet i många kursförklaringar är att man börjar direkt med:

-   klass
    
-   objekt
    
-   arv
    
-   metoder
    

utan att först visa att detta egentligen kommer ur Pythons allmänna modell.

Om man inte först förstår att:

-   värden är objekt
    
-   funktioner är objekt
    
-   språkets syntax ofta bygger på metodanrop
    
-   specialmetoder styr mycket av detta beteende
    

då känns klasser lätt som något konstigt, konstlat och byråkratiskt.

Men när man ser helheten blir klasser mer logiska.

De är bara ett sätt att säga:

**jag vill definiera en egen typ av objekt som beter sig enligt Pythons regler.**

* * *

**14\. En enkel kedja att minnas**

Man kan sammanfatta hela idén så här:

Python bygger på objekt  
objekt kan ha attribut och metoder  
språkets syntax använder ofta specialmetoder  
klasser definierar nya typer av objekt  
\_\_init\_\_ sätter startvärden  
\_\_str\_\_ ger textrepresentation  
\_\_len\_\_ gör att len() fungerar  
\_\_iter\_\_ gör objektet itererbart  
\_\_next\_\_ levererar nästa värde i iteration

* * *

**15\. Kort slutformulering för diskussion med lärare**

Om du vill uttrycka det mer kort och akademiskt på svenska kan du säga så här:

> I Python är klasser lättare att förstå om man först ser språkets objektmodell. Nästan allt i Python representeras som objekt, inklusive funktioner och inbyggda datatyper. Många språkkonstruktioner, som `print()`, `len()` och `for`, är i praktiken kopplade till objektens specialmetoder, till exempel `__str__`, `__len__`, `__iter__` och `__next__`. Ur det perspektivet blir en klass ett sätt att definiera en ny typ av objekt som kan integreras i språkets befintliga mekanismer.

* * *

**16\. Praktisk tolkning av de fem metoderna**

Till sist, mycket kort:

-   `__init__` - körs när objektet skapas
    
-   `__str__` - används när objektet visas som text
    
-   `__len__` - används av `len(obj)`
    
-   `__iter__` - gör att objektet kan användas i `for`
    
-   `__next__` - hämtar nästa värde under iteration
