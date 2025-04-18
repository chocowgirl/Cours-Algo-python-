
scores = {"MokoSempai":16, "Grungi":30, "Elocin03":56}

nom = input("Donnez-moi votre nom / pseudonom : ")
score = int(input("Donnez-moi votre score : "))

scores[nom]=score #refresh on this taxonomy


for pseudo, score in scores.items():
    print(f"{pseudo} : {score}")     

# for item in scores.items():
#     print(f"{item[0]} : {item[1]}")


"""
ma-list = [1,2,3]
a,b,c = ma_list
print (a + b)
"""

"""
a= 3
b=5
a,b = b,a #on peut affecter plusieurs variables à la fois tant qu'on traite de chaque côté la même qté
print(a,b)
"""

"""
table = [[1,2,3],[4,5,6],[7,8,9]]

for x, y, z in table:
    print(x, y, z)
"""