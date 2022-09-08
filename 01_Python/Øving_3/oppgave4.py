"""
Introduksjon til programmering med Python
Modul 3 - If-setninger - Øving 3
Oppgave 4
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et program som beregner kostnad på bussreiser etter følgende regler: 

- 50% for barn under 12 år.
- 20% for pensjonister, dvs. folk over 67 år.
- Ingen rabatt for de øvrige aldersgruppene. 

I tillegg skal prisen beregnes utfra en enhetspris per kilometer på 3,52 kroner. Prøv først å la det være en passasjer.
Dersom du klarer det kan du la det være mulig å oppgi antall barn, antall pensjonister og antall øvrige aldersgrupper. 
"""

# Deklarering av funskjon for billetter.
def billetter():
    alder = int(input("Hvor gammel er de reisende? "))
    if alder > 12 and alder < 67:
        billettype = "a"
    elif alder <= 12:
        billettype = "b"
    else:
        billettype = "p"
    antall = int(input("Hvor mange {} reiser? ".format(billettdict[billettype])))
    distanse = int(input("Hvor langt skal dere reise? (i hele km) "))
    oppdaterBilletter(billettype, antall, distanse)
    flereBilletter = input("Er det flere som skal bestille? [J]a eller [N]ei ").lower()
    if flereBilletter == "j":
        billetter()
    else:
        return()


# Deklarering av funksjon for å oppdatere listene for billettene
def oppdaterBilletter(billettype, antall, distanse):
    antalldict[billettype] += antall
    distansedict[billettype] += distanse * antall
    billettpris = float("{:.2f}".format(antall * distanse * prisdict[billettype] * enhetspris))
    totalprisdict[billettype] += billettpris


# Deklarering av faste variabler
enhetspris = 3.52

# Deklarering av andre variabler
totalpasasjerer = 0
totaldistanse = 0
totalpris = 0

# Deklarering av faste dictionaries som skal brukes for beregning av priser.
billettdict = {
    "b": "Barn",
    "p": "Pensjonister",
    "a": "Andre"
}
prisdict = {
    "b": 0.5,
    "p": 0.8,
    "a": 1
}

# Deklarering av variable dictionaries
antalldict = {
    "b": 0,
    "p": 0,
    "a": 0
}
distansedict = {
    "b": 0,
    "p": 0,
    "a": 0
}
totalprisdict = {
    "b": 0.0,
    "p": 0.0,
    "a": 0.0
}

# Kall funksjonen for å få antall billetter
billetter()

# Print ut alle verdier i konsoll
for billettype in billettdict:
    totalpasasjerer += antalldict[billettype]
    totaldistanse += distansedict[billettype]
    totalpris += totalprisdict[billettype]
    print("{} {} reiser totalt {}km og betalter {:.2f}kr.".format(antalldict[billettype],
                                                              billettdict[billettype], distansedict[billettype],
                                                              totalprisdict[billettype]))

print("Totalt reiser {} passasjerer {}km for {}kr".format(totalpasasjerer, totaldistanse, totalpris))
