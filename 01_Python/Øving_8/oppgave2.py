"""
Introduksjon til programmering med Python
Modul 8 - Filbehandling
Øving 8 - Oppgave 2
M. Bjørklund
"""

"""
Oppgavetekst:
Lag kode som viser all informasjonen i adresseboka. Det er altså følgende som skal vises i konsollet: 

Ola,12345678
Kari,1223344
Lise,87654321

Hint: Åpne filen i r-modus.
"""

import os

# Bruker VSCode, og for å få CTRL+F5 til å kjøre filen uten feilmelding (file not found)
# så henter jeg først stien til øvingen, før jeg joiner stien med adressebok.txt
filsti = os.path.dirname(os.path.abspath(__file__))
filnavn = "adressebok.txt"
adressebok = '\\'.join([filsti,filnavn])

# Sjekker om du har en adressebok man kan søke i, hvis ikke, terminerer vi skriptet.
if not os.path.exists(adressebok):
    print("Du har ikke en adressebok vi kan søke i, terminerer programmet.")
    quit()
    
# Åpner adressebok i lesemodus og skriver hvert oppslag i konsollet.
with open(adressebok, 'r') as f:
    for oppslag in f:
        print(oppslag, end="")
