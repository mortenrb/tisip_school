priser = list(map(int, input("Skriv inn priser\n").split()))


print(priser)
dyrest = priser[0]

for x in priser:
    if x > dyrest:
        dyrest = x

billigst = priser[0]
for y in priser:
    if y < billigst:
        billigst = y
        
print("L: {} H: {}".format(billigst, dyrest))