"""
Introduksjon til programmering med Python
Modul 6 - Funksjoner og metoder
Øving 6 - Oppgave 2
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et program som lar brukeren skrive inn navn og bosted med input() i to variabler.
Når det er gjort, skal scriptet ditt vise informasjon om det som ble skrevet inn: 

- Antall tegn i bosted
- Bostedet med store bokstaver
- Navnet med stor første bokstav
- Bosted og navn baklengs
- En del av navnet (du velger selv hva) 
- Eventuelt andre finurligheter du måtte finne på selv. 
"""

# Deklarering av input variabler
navn = input("Hva heter du? ")
bosted = input("Hvor bor du? ")

# De ønskede funksjonene for bosted
lengdeBosted = len(bosted)
storBosted = bosted.upper()
baklengsBosted = bosted[::-1]

# De ønskede funksjonene for navn
storNavn = navn.capitalize()
baklengsNavn = navn[::-1]
delAvNavn = navn[int(len(navn)/2)]


print("Tegn i bosted: {}".format(lengdeBosted))
print("Bosted STOR: {}".format(storBosted))
print("Navn med stor første bokstav: {}".format(storNavn))
print("Bosted baklengs {}".format(baklengsBosted))
print("Navn baklengs {}".format(baklengsNavn))
print("En del av navnet: {}".format(delAvNavn))