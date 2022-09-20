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

multiplikator1 = 1
multiplikator2 = 1

while multiplikator1 <= 10:
    while multiplikator2 <= 10:
        print("{} * {} = {}".format(multiplikator1, multiplikator2, multiplikator1 * multiplikator2))
        multiplikator2 += 1
    multiplikator1 += 1
    multiplikator2 = 1