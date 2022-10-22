"""
Introduksjon til programmering med Python
Modul 5 - Lister
Øving 5 - Oppgave 4
M. Bjørklund
"""

"""
Oppgavetekst:
Lag en liste av steder i Norge hvor du lar brukeren skrive inn via input-funksjonen.
Dersom du ikke får det til, så hardkod listen. 
"""

# Deklarering av variabler, er kommentert ut da den ikke er i bruk.
# steder = ["Bergen", "Førde", "Oslo", "Trondheim"]

# Deklarering av variabel "steder" vha. en input som konverterer input til liste
steder = list(input("Skriv inn stedsnavn i Norge, separert med mellomrom\n").split())

# Bare en test-print for å se at det var en liste som ble laget fra inputten
# print(steder)
