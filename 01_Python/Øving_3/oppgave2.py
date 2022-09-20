"""
Introduksjon til programmering med Python
Modul 3 - If-setninger
Øving 3 - Oppgave 2
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et program som ber om en alder, og skriver ut meldingen "Du er myndig" dersom personen er over 18 år,
"Du er dessuten pensjonist" dersom personen også er over 67 år, og "Du er ikke myndig enda" dersom personen er under 18 år. 

Ekstrautfordring til deg som vil: Prøv å sjekke inngangsdata.
Her forventes tall, altså må du sjekke at ikke for eksempel et navn skrives inn. 
"""

try:
    # Deklarering av variablene
    alder = int(input("Hvor gammel er du? "))
except ValueError:
    print("En feil oppstod, skrev du inn alder som heltall, eller i et annet format?")
    exit()

# Sjekk hvilken aldersgruppe personen er i
if alder >= 18:
    print("Du er myndig.")
if alder >= 67:
    print("Du er dessuten pensjonist")
if alder < 18:
    print("Du er ikke myndig enda")
