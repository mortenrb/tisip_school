"""
Introduksjon til programmering med Python
Modul 7 - Egendefinerte funksjoner
Øving 7 - Oppgave 5
M. Bjørklund
"""

"""
Oppgavetekst:
Lag en funksjon som fyller en liste med tilfeldige tall.
Dette er nyttig i mange sammenhenger når du trenger “data” å jobbe på. Kall deretter funksjonen.

Bruk gjerne random.randint(), se hvordan på for eksempel denne siden: https://www.w3schools.com/python/ref_random_randint.asp 

Dersom du klarer det, så lag slik at funksjonen oppretter så mange tall som du ønsker.
Dersom du ikke oppgir antall når du kaller funksjonen, så skal den lage en liste med 10 tall. 
"""

import random

# Definer funksjonen for å generere en liste med tilfeldige tall
def genererListe(lengde: int=10) -> list:
    liste = []
    for i in range(lengde):
        liste.append(random.randint(0,1000))
    return liste

# Print listen med parameter for hvor lang den skal være
print(genererListe(25))
print(genererListe(6))
print(genererListe(1))

# Prinst listen uten parameter for lengden
print(genererListe())
