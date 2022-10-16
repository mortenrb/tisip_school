"""
Introduksjon til programmering med Python
Modul 6 - Funksjoner og metoder
Øving 6 - Oppgave 1
M. Bjørklund
"""

"""
Oppgavetekst:
Anta at du er på handletur, og for hver gang du legger til en vare i handlevogna di,
så skriver du prisen på en lapp. Når du kommer hjem så bestemmer du deg for å lage et Python-script som har en liste med alle matvareprisene.
Det er nok å hardkode (skrive inn tallene direkte i koden). 

Når listen har innhold, så kommer den egentlige utfordringen: Skriv nå kode som finner ut en del informasjon om listen din: 

- Finn summen av alle varene du handlet
- Finn høyeste pris
- Finn laveste pris
- Vis listen i original rekkefølge
- Vis listen i sortert rekkefølge, stigende
- Vis listen i synkende rekkefølge
- Vis antall varer du har handlet
"""

# Deklarering av variabel for prisene som skal brukes i oppgaven
prisListe = [10.90, 32.00, 69, 420, 7.50, 14.99]

# Finn informasjonen som oppgaven spør etter
prisListeSum = sum(prisListe)
prisListeHoyest = max(prisListe) 
prisListeLavest = min(prisListe)
prisListeSortedASC = prisListe.copy()
prisListeSortedASC.sort()
prisListeSortedDESC = prisListe.copy()
prisListeSortedDESC.sort(reverse=True)
prisListeAntall = len(prisListe)

# Skriv ut informasjonen i oppgaven
print("Totalsum: {}".format(prisListeSum))
print("Høyeste pris: {}".format(prisListeHoyest))
print("Laveste pris: {}".format(prisListeLavest))
print("Originalliste: {}".format(prisListe))
print("Sortert stigende: {}".format(prisListeSortedASC))
print("Sortert synkende: {}".format(prisListeSortedDESC))
print("Antall varer: {}".format(prisListeAntall))