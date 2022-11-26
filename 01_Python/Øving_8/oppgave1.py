"""
Introduksjon til programmering med Python
Modul 8 - Filbehandling
Øving 8 - Oppgave 1
M. Bjørklund
"""

"""
Oppgavetekst:
I denne øvingen skal du lage flere Python-script som i sum utgjør en adressebok.
Start med å lage et script som lagrer informasjon om en person på en fil: Navn og telefonnummer.
Bruk komma til å skille informasjonen fra hverandre, og la hver person stå på en ny linje, slik: 

Ola,12345678
Kari,11223344
Lise,87654321

Hardkod informasjonen rett i scriptet. 
"""

import os

# Bruker VSCode, og for å få CTRL+F5 til å kjøre filen uten feilmelding (file not found)
# så henter jeg først stien til øvingen, før jeg joiner stien med adressebok.txt
filsti = os.path.dirname(os.path.abspath(__file__))
filnavn = "adressebok.txt"
adressebok = '\\'.join([filsti,filnavn])

# Data som skal skrives til adresseboken, joiner med linjeskift
kontakter = '\n'.join(["Ola,12345678","Kari,11223344","Lise,87654321"])

with open(adressebok, 'w') as f:
    f.writelines(kontakter)
