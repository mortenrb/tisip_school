"""
Introduksjon til programmering med Python
Modul 7 - Egendefinerte funksjoner
Øving 7 - Oppgave 2
M. Bjørklund
"""

"""
Oppgavetekst:
Lag en funksjon som finner det største av to tall.

Lag så kode hvor brukeren skriver inn to tall. Finn ut hvilket tall som er det største. 
"""

# Oppgave 2 og 4 er tilnærmet indentiske, så lager en felles fil for dem og importerer den til hver av oppgavene
# filen heter storst.py
import storst

# Deklarering av input verdier for tall1 og tall 2
tall1 = float(input("Skriv inn første tallet: "))
tall2 = float(input("Skriv inn første tallet: "))

# Print resultatet
print(storst.storst(tall1, tall2))
