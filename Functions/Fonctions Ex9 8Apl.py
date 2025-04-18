# def ajoute_tva(prix):
#     total = prix * 1.21
#     print(f"Prix TVA inclus: {total}")
#     return total

# ajoute_tva(100)
           
############# 9bis #############

def ajoute_tva(prix):
    total = prix * 1.21
    #print(f"Prix TVA inclus: {total}")
    return total

def somme_liste_plus_tva(liste):
    total = 0
    for i in range(0,len(liste)):
        total = total + liste[i]
        #print(total)
    total_avec_tva = ajoute_tva(total)
    print(total_avec_tva)
    return total_avec_tva

liste1000 = [100, 200, 300, 400,]

somme_liste_plus_tva(liste1000)