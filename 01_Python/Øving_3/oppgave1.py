"""
Introduksjon til programmering med Python
Modul 3 - If-setninger - Øving 3
Oppgave 1
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et program som ber om en alder, og skriver ut meldingen "Du er pensjonist" dersom personen er over 67 år. 
"""

# Deklarering av variablene
alder = int(input("Skriv inn din alder (i heltall): "))

# Sjekk om alderen er over 67
if alder >= 67:
    print("Du er pensjonist.")
