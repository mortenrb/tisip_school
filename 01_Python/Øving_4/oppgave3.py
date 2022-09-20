"""
Introduksjon til programmering med Python
Modul 4 - Løkker - Øving 4
Oppgave 3
M. Bjørklund
"""

"""
Oppgavetekst:
Lag kode som spør brukeren “Vil du vise tallene nedover eller oppover”?
Anta at brukeren svarer enten N eller O, der N står for Nedover mens O står for Oppover.
Basert på dette svaret fra brukeren skal programmet enten vise tallene 1, 2, 3, 4 og 5 – eller 5, 4, 3, 2, 1.
Dette skal skje ved hjelp av en løkke.
For å løse denne oppgaven trenger du å bruke funksjonen input() og kombinere if-setninger med while. 
"""

# Deklarering av variabler
fraVerdi = 0
tilVerdi = 0
retning = 0

# Funksjon for å få hvilken retning bruker ønsker å få tallene
def getRetning():
    inputRetning = input("Vil du vise tallene nedover eller oppover? ").lower()
    if inputRetning == 'n':
        return [5, 0, -1]
    elif inputRetning == 'o':
        return [1, 6, 1]
    else:
        print("Jeg forstod ikke hva du mente, prøv igjen")
        return getRetning()

# Sett verdiene til variablene, slik at vi kan printe tallene i riktig rekkefølge, verdi hents fra funksjonen getRetning()
fraVerdi, tilVerdi, retning = getRetning()

# Løkke for å skrive ut verdiene i valgt rekkefølge
for i in range(fraVerdi, tilVerdi, retning):
    print(i)