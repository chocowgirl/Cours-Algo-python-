from random import randint

def madeupword(length):
    lettres = "ahkonst" # or: lettres = ["a","h","k","o","n","s","t"]
    result = ""
    for i in range(length):
        indexinlettres = randint(0, len(lettres)-1)
        result = result + lettres[indexinlettres]
    #print(result)
    return result


x = int(input("Donnez-moi un numéro et je te ferais un mot qui contient autant des lettres : "))
print(madeupword(x))


"""
Pour cette Ex: pas necessaire d'appeler la variable qui sera utilisé
comme paramètre dehors la fonction la même que l'appelation de la variable
qui est utilisé comme argument pendant la construction de la fonction...
mais si tu veux tu peux... ce sera p-e plus importante dans le cas où,
par exemple nous demandons d'abord a plusieurs utilisateurs différents
leur longueur souhaité pour le mot... car comme ça on appelerais la fonction
comme:
print(madeupword(x))
print(madeupword(y))
print(madeupword(z))
"""