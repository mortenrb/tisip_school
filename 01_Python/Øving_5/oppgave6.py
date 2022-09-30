"""
Introduksjon til programmering med Python
Modul 5 - Lister
Øving 5 - Oppgave 6
M. Bjørklund
"""

"""
Oppgavetekst:
Lag først en liste med priser på 7 ulike matvarer, gjerne ved hjelp av input() men du kan også hardkode om du ønsker det.
Når listen har innhold, så kommer den egentlige utfordringen: Finn høyeste og laveste pris i listen.
Hint: Bruk en løkke (enten for eller while) og bruk hjelpevariabler for å hele tiden oppdatere hva som er størat og minst. 
"""

# Deklarering av variabler
# priser = [10, 20, 30, 40, 50, 60, 70]
priser = []
dyrest = None
billigst = None

# Løkke for å få brukeren til å skrive inn prisen på 7 varer
# Alternativt kunne man brukt priser = list(map(int, input("Skriv inn priser\n").split())), men det vil ikke begrense seg til 7 varer.
for i in range(7):
    pris = float(input("Skriv inn prisen på en matvare: "))
    priser.append(pris)
    
# Løkke for å finne den dyreste og billigste prisen
for i in range(len(priser)):
    if (dyrest is None) or (dyrest < priser[i]):
        dyrest = priser[i]
    if (billigst is None) or (billigst > priser[i]):
        billigst = priser[i]

# Skriv ut den billigste og dyreste varen i konsoll
print("Billigst: {:.2f}kr\r\nDyrest: {:.2f}kr\r\n".format(billigst, dyrest))

# Kontroll for å se at løkken ga riktig verdi
print("Kontroll: Billigst: {:.2f}kr\r\nKontroll: Dyrest: {:.2f}kr\r\n".format(min(priser), max(priser)))
