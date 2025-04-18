given = 0
oneunder = None
total = None

while given > 100 or given < 1:
    given = int(input("Donnez-moi une chiffre entière entre 1 et 100:"))
    oneunder = given - 1
    total = given

while oneunder != 0:
    total = total + oneunder
    oneunder = oneunder - 1
    #print(total)

print("grand total = " + str(total))


""" V1
FOR GOING THE ADDITION ROUTE IN SECOND BOUCLE (number + 1, + number+2 ....)
somme = 0
i = 1

while i <= number:
    somme = somme + i
    i = i + i

print(somme)
"""

""" V2
(pas réelement besoin de utiliser oneunder unless you want to keep the given)
somme = 0
while number > 0:
    somme = somme + number
    somme = number - 1
"""

""" V3
somme = 0

for i in range(1, number+1):
    somme = somme + i

print(somme)
"""