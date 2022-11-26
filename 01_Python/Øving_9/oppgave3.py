"""
Introduksjon til programmering med Python
Modul 9 - Smarte triks i Python
Øving 9 - Oppgave 3
M. Bjørklund
"""

"""
Oppgavetekst:
Lag en modul med noen egendefinerte funksjoner, altså funksjoner du skriver selv med def-stikkordet.
Se gjennom tidligere øvinger du har levert inn eller annen kode du har skrevet,
og spør deg selv om noe av denne koden kan egne seg som funksjoner i en slik modul-fil. 

Her kan du være kreativ, du bestemmer selv hvor mange funksjoner du vil lage og hvor avanserte de skal være. 

Lag også et script hvor du kaller opp en eller flere av funksjonene (husk at du må importere modulen du har laget). 
"""
import oppgave3_moduler as funksjoner

# Deklarering av variabler vi skal bruke i scriptet
partallsliste = []
oddetallsliste = []
talliste = []

# Få bruker til å skrive inn 10 tallverdier og sorterer det som partall eller oddetall,
# så vell som en samling av alle tallene.
for i in range(10):
    tallinput = funksjoner.num_input(f"Skriv inn en tallverdi ({i+1}/10):")
    tallinput = int(tallinput)
    talliste.append(tallinput)
    if funksjoner.is_even(tallinput):
        partallsliste.append(tallinput)
    if funksjoner.is_odd(tallinput):
        oddetallsliste.append(tallinput)

# Finn gjennomsnittet av hver av talllistene
avg_partallsliste = funksjoner.average(partallsliste)
avg_oddetallsliste = funksjoner.average(oddetallsliste)
avg_talliste = funksjoner.average(talliste)

# Skriv resultatet i konsoll
print(f"Gjennomsnitt partall {avg_partallsliste}")
print(f"Gjennomsnitt oddetall {avg_oddetallsliste}")
print(f"Gjennomsnitt alle tall {avg_talliste}")