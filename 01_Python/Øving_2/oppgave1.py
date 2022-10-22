"""
Introduksjon til programmering med Python
Modul 2 - Variabler og datatyper
Øving 2 - Oppgave 1
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et program som gjør følgende ting (det siste kulepunktet kan være småvrient):
    - Lagrer navnet ditt i en variabel.
    - Lagrer alderen din i en variabel
    - Viser navnet og alderen på skjerm, altså i konsollvinduet.
    - Viser følgende tekst på skjermen: ”Jeg heter Ola Nordmann og er 83 år”,
      hvis navnet i variabelen er Ola Nordmann og alderen er 83 år. Du skal bruke ditt eget navn og din alder.
"""

# Deklarering av variablene
navn = "Morten Bjørklund"
alder = 29

# Alternativt, få variablene fra input
# navn = input("Ditt navn: ")
# alder = int(input("Skriv inn din alder (i heltall): "))

# Vis navn og alder på skjerm
print("Navn: {}\r\nAlder: {}år".format(navn, alder))

# En mer komplett introduksjonstekst
print("Jeg heter {} og er {} år".format(navn, alder))
