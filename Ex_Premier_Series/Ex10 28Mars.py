entry = None
list = []

while entry !=0:
    entry = int(input("Entrez un nombre:"))
    #print(entry)
    #if entry !=0:
    if list == []:
        list.append(entry)
    elif entry < list[0]:
        list.insert(0, entry)
    elif entry > list[-1]:
        list.append(entry)

    
#print(list)
print("Le numéro le plus bas que vous avez donné: " + str(list[0]) + "\n Le numéro le plus haut que vous avez donné:" + str(list[-1]))

""" CORRECTION PROF: LA LISTE VA BOUFFER BCP DE DONNE.  UNE LISTE SERA MOINS EFFICACE. UTILISER UNE VARIABLE.
number = int(input("nombre:"))
greater = number
lower = number

while number !=0:
    number = int(input("nombre:"))
    
    if number < lower:
        lower = number
    elif number > greater
        greater = number

print("plus grand:" + str(greater))
print("plus petit:" + str(lower))"""