"""
Introduksjon til programmering med Python
Modul 5 - Lister
Øving 5 - Oppgave 5
M. Bjørklund
"""

"""
Oppgavetekst:
Les inn temperaturer i en liste. Gå gjennom hvert av stedene i listen fra oppgave 3 med kode,
og la brukeren skrive inn hva som er temperaturen på hvert av disse stedene.
Hvis du hadde 4 steder i oppgave 3-listen, så skal det altså spørres om 4 temperatuerer via input-funksjonen. 
"""

# Deklarering av liste over byer som ble brukt i oppgave 4 (anntar oppgavetekst er feil og mener oppgave 4, ikke 3)
steder = ["Bergen", "Førde", "Oslo", "Trondheim"]
temperaturer = []

# Løkke for å få hente temperaturen og lagre den i en liste
for i in range(len(steder)):
    temperaturInput = float(input("Skriv inn en temperatur for {}: ".format(steder[i])))
    temperaturer.append(temperaturInput)

# Skriv ut alle verdiene i listen til konsoll (ikke en del av oppgaven, mer som test-kode)
for y in range(len(steder)):
    print("Du skrev at temperaturen i {} er {:.2f}°C".format(steder[y], temperaturer[y]))
