"""
Introduksjon til programmering med Python
Modul 6 - Funksjoner og metoder
Øving 6 - Oppgave 3
M. Bjørklund
"""

"""
Oppgavetekst:
I leksjon 6 på side 13 er det en tabell med oversikt over noen liste-metoder.
Lag et program som bruker en del av disse metodene, og kjør programmet i konsollet så det viser hva som skjer.
Her kan du være kreativ og får frihet til å lage det du selv vil.
Hensikten er at du skal jobbe med metodene og prøve og feile, og lære gjennom det.  
"""

# Deklarering lister vi kan bruke. Verdiene er fiktive.
studenter = ["Morten", "Håkon", "Lars", "Kjell", "Anne", "Ingrid"]
alder = [27, 15, 38, 45, 25, 19]

# Skriv ut gjeldende lister
print(studenter)
print(alder)

# Gjør endringer på listen
studenter.append("Lisa")
alder.append(25)

# Skriv ut nye lister
print(studenter)
print(alder)

# Opprett en ny liste basert på studenter
nyStudentListe = studenter.copy()

# Lag en pointer til eksisterende studentliste
pointerStudenter = studenter

# Gjør endringer på pointer
pointerStudenter.pop(0)
pointerStudenter.reverse()
pointerStudenter.insert(3, "Morten")

# Skriv ut alle 3 studentlistene (legg merke til at listen studenter endret seg, til tross for at vi ikke brukte funksjonene direkte på den listen)
print(studenter)
print(nyStudentListe)
print(pointerStudenter)