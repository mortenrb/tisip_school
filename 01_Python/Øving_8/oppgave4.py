"""
Introduksjon til programmering med Python
Modul 8 - Filbehandling
Øving 8 - Oppgave 4
M. Bjørklund
"""

"""
Oppgavetekst:
Lag kode som lar brukeren søke etter et navn, og så viser telefonnummeret til vedkommende.
Hvis navnet ikke fins, så skal det gis beskjed om dette. 
"""

import os

# Bruker VSCode, og for å få CTRL+F5 til å kjøre filen uten feilmelding (file not found)
# så henter jeg først stien til øvingen, før jeg joiner stien med adressebok.txt
filsti = os.path.dirname(os.path.abspath(__file__))
filnavn = "adressebok.txt"
adressebok = '\\'.join([filsti,filnavn])

kontaktliste = []

# Sjekker om du har en adressebok man kan søke i, hvis ikke, terminerer vi skriptet.
if not os.path.exists(adressebok):
    print("Du har ikke en adressebok vi kan søke i, terminerer programmet.")
    quit()

# Åpner adressebok i lesemodus og lagrer all informasjonen i en liste for bruk senere   
with open(adressebok, 'r') as f:
    for oppslag in f:
        kontaktliste.append(oppslag.strip().split(","))

# Får input fra brukeren
kontaktsok = input("Skriv inn navn på kontakten du ønsker å søke etter: ")

# Standard retur, hvis man ikke finner kontakten i listen
resultat = f"Fant ikke {kontaktsok} i adresseboken."

# Løkke for å finne kontakt
for kontakt in kontaktliste:
    if kontaktsok.lower() in map(str.lower, kontakt):
        resultat = f"Telefonnummeret til {kontaktsok} er {kontakt[1]}"
        break

# Skriv resultat til
print(resultat)
