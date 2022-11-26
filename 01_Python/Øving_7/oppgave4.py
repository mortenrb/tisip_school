"""
Introduksjon til programmering med Python
Modul 7 - Egendefinerte funksjoner
Øving 7 - Oppgave 4
M. Bjørklund
"""

"""
Oppgavetekst:
La brukeren lese inn størrelsen på to kvadrater.
Programmet ditt skal, på en kompakt måte, finne ut hva som er det største kvadratet. 
"""

# Oppgave 2 og 4 er tilnærmet indentiske, så lager en felles fil for dem og importerer den til hver av oppgavene
# filen heter storst.py
import storst

# Deklarering av input verdi for kvadratene
kvadrat1 = float(input("Skriv inn størrelsen på det første kvadratet: "))
kvadrat2 = float(input("Skriv inn størrelsen på det andre kvadratet: "))

# Print ut resultatet
print(storst.storst(kvadrat1, kvadrat2))
