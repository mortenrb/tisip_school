"""
Introduksjon til programmering med Python
Modul 2 - Variabler og datatyper
Øving 2 - Oppgave 3
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et program som lagrer fornavn ogetternavn i to variabler. Deretter skal det vises en beskjed på formen:
    “My name is ETTERNAVN, FORNAVN ETTERNAVN”.
Med andre ord: Hvis du lagrer James i variabelen fornavn og Bond i etternavn, så skal det vises
    My name is Bond, James Bond.
Hvis du skriver ditt navn, så blir det tilsvarende.
"""

# Deklarering av variablene
fornavn = "Morten"
etternavn = "Bjørklund"

# Alternativt, få variablene fra input
# fornavn = input("Ditt fornavn: ")
# etternavn = input("Ditt etternavn: ")

# Skriv ut på formatet "My name is ETTERNAVN, FORNAVN ETTERNAVN"
print("My name is {1}, {0} {1}".format(fornavn, etternavn))