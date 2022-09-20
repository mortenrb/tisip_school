"""
Introduksjon til programmering med Python
Modul 2 - Variabler og datatyper
Øving 2 - Oppgave 2
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et program som lagrer et tall i en variabel.
Skriv ut hva halvparten av tallet er, hva det dobbelte av tallet er, hva det tredobbelte av tallet er,
og hva tallet ganget med seg selv er.
"""

# Deklarering av variabel
tall = 42

# Utreninger ihht. oppgave. Halvparten, dobbel, tredobbel og ganget med seg selv
halvtall = tall / 2
dobbeltall = 2 * tall
tredobbeltall = 3 * tall
gangettall = tall * tall

# Vis resultat på skjerm
print("Halvpart: {}\r\n"
      "Dobling: {}\r\n"
      "Tredobling: {}\r\n"
      "Ganget med seg selv: {}".format(halvtall, dobbeltall, tredobbeltall, gangettall))
