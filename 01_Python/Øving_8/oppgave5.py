"""
Introduksjon til programmering med Python
Modul 8 - Filbehandling
Øving 8 - Oppgave 5
M. Bjørklund
"""

"""
Oppgavetekst:
Fra de tidligere oppgavene har adresseboka innhold. La brukeren skrive et navn og telefonnummer ved hjelp av funksjonen input(),
og lagre informasjonen på fil uten å slette det som allerede ligger der.

Det er fint om du klarer å feilsjekke det som skrives inn. 
"""

import os

# Bruker VSCode, og for å få CTRL+F5 til å kjøre filen uten feilmelding (file not found)
# så henter jeg først stien til øvingen, før jeg joiner stien med adressebok.txt
filsti = os.path.dirname(os.path.abspath(__file__))
filnavn = "adressebok.txt"
adressebok = '\\'.join([filsti,filnavn])

# Deklarering av variabler vi skal bruke
ny_kontakt = ""
navn = input("Skriv inn navnet på kontakten: ").strip()
telefon = input("Skriv inn nummeret til kontakten: ")

while not navn:
    print("Navn må ha en verdi.")
    navn = input("Skriv inn navnet på kontakten: ")
    
# Hvis telefonnummeret ikke er numerisk, så må det skrives på nytt.
while not telefon.isnumeric():
    print("Telefonnummeret må være en tallverdi.")
    telefon = input("Skriv inn nummeret til kontakten: ")

# Standard formattering, for eksempel hvis filen ikke allerede eksisterer
ny_kontakt = f"{navn},{telefon}\n"

# Sjekker om siste linjen i adresseboken er linjeskift, slik at vi ikke ødelegger adresselisten
if os.path.exists(adressebok):
    with open(adressebok, 'r') as f:
        siste_linje = f.readlines()[-1]
        har_nylinje = siste_linje.endswith(('\n', '\r', '\r\n'))
        if not har_nylinje:
            ny_kontakt = f"\n{navn},{telefon}\n"

# Åpner filen og appender navn og telefonnummer til adresseboken
with open(adressebok, 'a') as f:
    f.write(ny_kontakt)
