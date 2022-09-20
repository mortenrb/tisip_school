"""
Introduksjon til programmering med Python
Modul 4 - Løkker - Øving 4
Oppgave 4
"""

"""
Oppgavetekst:
I leksjon 4 i kapittel 7, figur 6, ser du kode som har to bugs i seg.
Finn ut hva feilene er og rett opp i koden. 

(anntar at oppgaven mener figur 7)
"""

forste = start = int(input("Hva er første tall?\n"))
andre = int(input("Hva er andre tall?\n"))

print()
print("Vi starter...")
while forste <= andre:
    print(forste)
    forste = forste + 1
print("Det var alle tallene mellom", start, "og", andre)
