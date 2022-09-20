"""
Introduksjon til programmering med Python
Modul 4 - Løkker
Øving 4 - Oppgave 1
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et lite program som skriver ut med print() annethvert tall mellom 1 og 10.
Altså skal 2, 4, 6, 8 og 10 skrives ut.
Hvis du trenger et hint, så se oppgave 2 for inspirasjon.
"""

# Deklarering av variabler
tall = 1
slutt = 10

# While-løkke hvor tall er under eller lik slutt (10)
while tall <= slutt:
    if (tall % 2) == 0:
        print(tall)
    tall += 1