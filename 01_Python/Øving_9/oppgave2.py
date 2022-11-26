"""
Introduksjon til programmering med Python
Modul 9 - Smarte triks i Python
Øving 9 - Oppgave 2
M. Bjørklund
"""

"""
Oppgavetekst:
Du kan lese en god del informasjon ut av et personnummer. Som kjent har personnummeret 11 sifre,
der de første 6 er fødselsdatoen til personen.
Du skal nå lage et lite script som mottar et personnummer som brukeren skriver inn via input() fra konsollet.
Så skal inputen behandles på ulike måter og resultatet skal vises i konsollet med print(). 

MERK: Denne oppgaven må løses med såkalt "string slicing", se for eksempel notatet om oppdeling av lister kalt Læringsaktivitet:
Dele opp lister. Det er ganske lite kode som skal til for å løse denne oppgaven.
Deloppgavene du skal løse, er som følger:

a. Skriv ut fødselsdatoen på “rå” form, det vil si at du skal hente ut de 6 første sifrene fra personnummeret.
b. Skriv ut fødselsdatoen på formatert form, typisk 15.03.76
c. Skriv ut hvilket kjønn personen har. Siffer nummer 9 angir hvilket kjønn personen har.
   Dersom 9. siffer er et oddetall, er personen en mann, mens partall gir kvinne. Hint: Søk etter “modulo operator Python”. 
d. Skriv ut bare de siste 5 sifrene av personnummeret
e. Personnummeret skrevet ut baklengs
"""

# Deklarering av variabler vi skal bruke i scriptet
personnummer = ""

while not personnummer.isnumeric() or len(personnummer) != 11:
    personnummer = input("Skriv inn ditt personnummer (11 siffer): ")

# Deloppgave a. Skriv ut fødselsdatoen på “rå” form, det vil si at du skal hente ut de 6 første sifrene fra personnummeret.
print(personnummer[0:6])

# Deloppgave b. Skriv ut fødselsdatoen på formatert form, typisk 15.03.76
d = personnummer[0:2]
m = personnummer[2:4]
y = personnummer[4:6]
print(f"{d}.{m}.{y}")

# Deloppgave c. Skriv ut hvilket kjønn personen har. Siffer nummer 9 angir hvilket kjønn personen har.
# Dersom 9. siffer er et oddetall, er personen en mann, mens partall gir kvinne. Hint: Søk etter “modulo operator Python”. 
kjonn = "Mann" if (int(personnummer[8]) % 2) else "Kvinne"
print(kjonn)

# Deloppgave d. Skriv ut bare de siste 5 sifrene av personnummeret
print(personnummer[-5:])

# Deloppgave e. Personnummeret skrevet ut baklengs
print(personnummer[::-1])
