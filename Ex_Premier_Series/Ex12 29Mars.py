entry0 = None
entry1 = None
sumlist = []
total = 0
# print("entry0" + str(entry0))
# print("entry1" + str(entry1))
# print(sumlist)
# print("total = " + str(total))

print("\nOn va voir si vous trouvez la bonne combinaison...")
entry0 = int(input("Donnez-moi une chiffre:"))
sumlist.append(entry0)
#print(sumlist)
total = total + entry0
#print("Total =" + str(total))
entry1 = int(input("...et maintenant une autre:"))
sumlist.append(entry1)
#print(sumlist)
total = total + entry1
#print("Total =" + str(total))

while sumlist[-1] != sumlist[-2]:
    entry0 = int(input("et une autre:"))
    sumlist.append(entry0)
    #print(sumlist)
    total = total + entry0
    #print("Total =" + str(total))


if sumlist[-1] == sumlist[-2]:
    print("Vous avez trouvé la combinaison!  La somme de tous les chiffres que vous avez entré est " + str(total))

""" PREFERABLE DE FAIRE SANS LISTE CAR PAS STOCKAGE D'INFOS INUTILEMENT
previous = None
number = int(input("Nombre:"))
sumnumber = number

while number != previous:
    previous = number
    number = int(input("nombre?:"))
    sumnumber = sumnumber + number
    
print("somme = " +str(sumnumber))"""