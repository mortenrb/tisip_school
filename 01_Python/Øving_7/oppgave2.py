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

# Funksjon for å finne det største tallet
def storst(x:float, z:float)->str:
    if x > z:
        return "{} er større enn {}".format(x, z)
    if z > x:
        return "{} er større enn {}".format(z, x)
    return("Begge verdiene er like store")

# Deklarering av input verdier for tall1 og tall 2
tall1 = float(input("Skriv inn første tallet: "))
tall2 = float(input("Skriv inn første tallet: "))

# Print resultatet
print(storst(tall1, tall2))
