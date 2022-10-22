"""
Introduksjon til programmering med Python
Modul 4 - Løkker
Øving 4 - Oppgave 6
M. Bjørklund
"""

"""
Oppgavetekst:
Lag kode som skriver ut gangetabellen (multiplikasjonstabellen) ved hjelp av to while-løkker nøstet i hverandre.
"""

rekkeTeller = 1

while rekkeTeller <= 10:
    nyRad = ""
    kolonneTeller = 1
    while kolonneTeller <= 10:
        produkt = rekkeTeller * kolonneTeller
        nyRad += "{}\t".format(produkt)
        kolonneTeller += 1
    print(nyRad)
    rekkeTeller += 1
