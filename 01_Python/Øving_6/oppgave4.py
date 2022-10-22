"""
Introduksjon til programmering med Python
Modul 6 - Funksjoner og metoder
Øving 6 - Oppgave 4
M. Bjørklund
"""

"""
Oppgavetekst:
Du kan lese en god del informasjon ut av et personnummer. Som kjent har personnummeret 11 sifre,
der de første 6 er fødselsdatoen til personen.
Du skal nå lage et lite script som mottar et personnummer som brukeren skriver inn via input() fra konsollet.
Så skal inputen behandles på ulike måter og resultatet skal vises i konsollet med print(): 

- Fødselsdatoen på “rå” form, det vil si at du skal hente ut de 6 første sifrene fra personnummeret.
- Fødselsdatoen på formatert form, typisk 15.03.76
- Hvilket kjønn personen har. Siffer nummer 9 angir hvilket kjønn personen har.
  Dersom 9. siffer er et oddetall, er personen en mann, mens partall gir kvinne. Hint: Søk etter “modulo operator Python”. 
- Bare de siste 5 sifrene av personnummeret
- Personnummeret skrevet ut baklengs
"""

# Deklarering av variabel for personnummer
import re

personnummer = ""

while not personnummer.isnumeric() or len(personnummer) != 11:
    personnummer = input("Skriv inn ditt personnummer (11 siffer): ")

# Fødselsdato på "rå" form    
rawFodselsdato = personnummer[:6]

# Formatter fødselsdato som dd.mm.yy fra rawFodselsdato
regex = r"(\d{2})(\d{2})(\d{2})"
pattern = "\\1.\\2.\\3"
formatertFodselsdato = re.sub(regex, pattern, rawFodselsdato)

# Finn kjønn, basert på 9. siffer (index 8)
kjonn = "Mann" if (int(personnummer[8]) % 2) else "Kvinne"

# Siste 5 siffer av personnummeret
sisteFem = personnummer[-5:]

# Personnummeret baklengs
baklengs = personnummer[::-1]


print("Fødselsdato på \"rå\" form: {}".format(rawFodselsdato))
print("Fødselsdato formatert: {}".format(formatertFodselsdato))
print("Kjønn: {}".format(kjonn))
print("Siste 5 siffer: {}".format(sisteFem))
print("Personnummer baklengs: {}".format(baklengs))
