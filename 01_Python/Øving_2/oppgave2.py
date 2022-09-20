"""
Introduksjon til programmering med Python
Modul 2 - Variabler og datatyper
Øving 2 - Oppgave 2
M. Bjørklund
"""

"""
Oppgavetekst:
Lag en liten kalkulator som fungerer slik:
    - Det skal være tre tall som ligger i variablene tall1, tall2 og tall3.
    - Summen av tallene skal skrives ut på skjerm, altså i konsollvinduet.
    - Gjennomsnittet av tallene skal også skrives ut.
"""

# Deklarering av variablene
tall1 = 20
tall2 = 12
tall3 = 34

# Alternativt, få variablene fra input
# tall1 = int(input("Skriv inn første tallet (i heltall): "))
# tall2 = int(input("Skriv inn andre tallet (i heltall): "))
# tall3 = int(input("Skriv inn tredje tallet (i heltall): "))

# Regn ut summen av tallene etterfulgt av gjennomsnittet av tallene
sumtall = tall1 + tall2 + tall3
gjennomsnitt = sumtall / 3

# Vis verdiene på skjerm
print(sumtall)
print(gjennomsnitt)