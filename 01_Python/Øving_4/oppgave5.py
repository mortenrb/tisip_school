"""
Introduksjon til programmering med Python
Modul 4 - Løkker
Øving 4 - Oppgave 5
M. Bjørklund
"""

"""
Oppgavetekst:
Lag kode som spør brukeren om brukernavn og passord.
Dersom kombinasjonen av brukernavn/passord er feil, skal det gis et nytt forsøk.
Maksimalt tre forsøk. Hvis de brukes opp så får brukeren beskjed om at “Du har brukt alle forsøkene”.
Hvis brukeren derimot klarer å logge inn, så skal beskjeden “Du har logget inn” vises i konsollet.  
"""

brukernavn = "Morten"
passord = "P@55ord"

forsok = 0

while (forsok < 3):
    inputBrukernavn = input("Skriv inn brukernavn: ")
    inputPassord = input("Skriv inn passord: ")
    if(inputBrukernavn == brukernavn and inputPassord == passord):
        break
    else:
        forsok += 1

if forsok < 3:
    print("Du har logget inn")
else:
    print("Du har brukt alle forsøkene")