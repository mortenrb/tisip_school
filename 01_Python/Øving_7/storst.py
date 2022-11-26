"""
Introduksjon til programmering med Python
Modul 7 - Egendefinerte funksjoner
Øving 7 - Oppgave 2, 4
M. Bjørklund
"""

"""
Oppgavetekst:
Felles funksjon for oppgave 2 og oppgave 4
"""

# Funksjon for å finne det største kvadratet
def storst(x:float, z:float)->str:
    if x > z:
        return "{} er større enn {}".format(x, z)
    if z > x:
        return "{} er større enn {}".format(z, x)
    return("Begge verdiene er like store")