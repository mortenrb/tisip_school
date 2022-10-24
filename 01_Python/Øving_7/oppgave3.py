"""
Introduksjon til programmering med Python
Modul 7 - Egendefinerte funksjoner
Øving 7 - Oppgave 3
M. Bjørklund
"""

"""
Oppgavetekst:
Lag en funksjon som finner ut hva som er arealet til et kvadrat.
Funksjonen skal ta inn ett argument, nemlig antall cm som siden har.
Det er nok at kun en side er kjent for at arealet skal kunne regnes ut, fordi i et kvadrat er som kjent alle sider like store.
Formelen for arealet av et kvadrat blir derfor: Areal = side ganger side.
"""

# Funksjon for å regne ut arealet til et kvadrat
def areal(x:float)->float:
    return x * x

# Deklarering av input verdi for siden
side = float(input("Skriv inn lengden på sidene til kvadratet: "))

# Print resultatet, avrundet til 2 desimaler grunnet "floating point arithmetic issue" ved bruk av desimaler
print("Arealet til kvadratet er {:.2f} cm2".format(areal(side)))
