"""
Introduksjon til programmering med Python
Modul 5 - Lister
Øving 5 - Oppgave 3
M. Bjørklund
"""

"""
Oppgavetekst:
Fyll en liste med noen tall. Lag kode som finner summen av alle tallene i listen, og deretter gjennomsnittsverdien.
Hint: Bruk en løkke. 
"""

# Deklarering av variablerne
liste = [20, 52, 2, 97, 6, 88]
sumListe = 0
avgListe = 0

# Løkke for å summere alle elementene i listen sammen alternativt kunne vi brukt sum(liste), men oppgaven er om løkker
for element in liste:
    sumListe += element

# Skriv ut summen til konsoll
print("Summen av alle tallene i listen er {}".format(sumListe))

# Regn ut gjennomsnittet til tallene listen
avgListe = sumListe / len(liste)

# Skriv ut gjennomsnittet til konsoll
print("Gjennomsnittsverdien av tallene i listen er {:.2f}".format(avgListe))
