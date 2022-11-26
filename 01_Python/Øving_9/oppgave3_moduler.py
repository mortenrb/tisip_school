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

# Returnerer bolsk verdi for om tallet er partall eller ei
def is_even(nummer: int)->bool:
    return (nummer % 2 == 0)

# Returnerer bolsk verdi for om tallet er oddetall eller ei
def is_odd(nummer: int)->bool:
    return not (nummer % 2 == 0)

# Returnerer en bruker-input, forutsatt at den er en tallverdi
def num_input(tekst: str = "Skriv inn tallverdi: ")->str:
    numberinput = ""
    while not numberinput.isnumeric():
        numberinput = input(tekst)
    return numberinput

# Returnerer gjennomsnittsverdien av en liste.
def average(liste: list)->float:
    try:
        return sum(liste) / len(liste)
    except TypeError:
        print("Liste må være en liste av integer- og/eller float-verdier.")
        return 0
    except ZeroDivisionError:
        print("Listen er tom, kan ikke dele på 0")
        return 0
