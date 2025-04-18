liste = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1,]
print(liste)
input = int(input("SVP donnez-moi un numéro (un qui se trouve dans ma liste juste au-dessus-là): "))
liste.remove(input)
print("je l'ai envlevé, voyez?")
print(liste)
