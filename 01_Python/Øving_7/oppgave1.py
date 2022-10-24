"""
Introduksjon til programmering med Python
Modul 7 - Egendefinerte funksjoner
Øving 7 - Oppgave 1
M. Bjørklund
"""

"""
Oppgavetekst:
Lag en funksjon som returnerer teksten "Du er tenåring" hvis alder er mellom 13 og 19 år,
og ellers returnerer teksten "Du er ikke tenåring". Her må du bruke if-setning i funksjonen.

Når funksjonen er laget skal du skrive kode som viser (med print-setninger) informasjon om hvorvidt personene nedenfor er tenåring eller ikke.
Her er fakta om personene: 

1. Ola er 12 år
2. Kari er 15 år
3. Lise er 20 år 
Hint: print og så navn på funksjonen du må kalle med oppgitt argument, for hver av personene. 
"""

# Funksjon for å sjekke om alder er definert som tenårene eller ei
def erTenaring(alder:int)->str:
    # IF-setning for å sjekke om alder er i aldersområdet 13-19 år og returnerer en string hvis det er tilfellet
    if alder >= 13 and alder <= 19:
        return "Du er tenåring"
    # Returnerer string for om du ikke er tenåring
    return "Du er ikke tenåring"

# Printer ut test-parametrene formatert med funksjonen.
print("Ola er 12 år. {}".format(erTenaring(12)))
print("Kari er 15 år. {}".format(erTenaring(15)))
print("Lise er 20 år . {}".format(erTenaring(20)))
