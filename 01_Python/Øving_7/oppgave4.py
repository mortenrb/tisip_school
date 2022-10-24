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

# Funksjon for å finne det største kvadratet
def storst(x:float, z:float)->str:
    if x > z:
        return "{} er større enn {}".format(x, z)
    if z > x:
        return "{} er større enn {}".format(z, x)
    return("Begge verdiene er like store")

# Deklarering av input verdi for kvadratene
kvadrat1 = float(input("Skriv inn størrelsen på det første kvadratet: "))
kvadrat2 = float(input("Skriv inn størrelsen på det andre kvadratet: "))

# Print ut resultatet
print(storst(kvadrat1, kvadrat2))
