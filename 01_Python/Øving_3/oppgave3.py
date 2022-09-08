"""
Introduksjon til programmering med Python
Modul 3 - If-setninger - Øving 3
Oppgave 3
M. Bjørklund
"""

"""
Oppgavetekst:
Lag et program som lar brukeren skrive inn tippetegnet for en fotballkamp i konsollet (input).
Skriv ut teksten "Hjemme" når ”H” skrives inn, "Uavgjort" ved ”U” og "Borte" ved ”B”. 

Husk å sjekke inngangsdata. Her forventes bokstavene ”H”, ”U” eller ”B”,
altså må du gi beskjed til brukeren om hva som forventes dersom noe annet skrives inn. 
"""

# Deklarering av variablene
tippetegn = input("Hvem vinner (H-hjemme, B-borte, U-uavgjort)? ").lower()

# En dictionary med lovlige verdier
tippedict = {
    "h": "Hjemme",
    "u": "Uavgjort",
    "b": "Borte"
}

if tippetegn in tippedict:
    print(tippedict[tippetegn])
else:
    print("Jeg forstår ikke hva du mener?\r\n"
          "Skriv inn bokstaven H hvis du tror det blir hjemmeseier.\r\n"
          "B hvis du tror det blir borteseier\r\n"
          "eller U hvis du tror det blir uavgjort")