info_joueurs = {"Marie":1, "Bernard":4, "François":2, "Thomas":12, "Hila":15}
joueurs_classés = []
total = 0

for prenom, rang in info_joueurs.items():
    #print(rang)
    total += rang
    moyen_niveau = total / len(info_joueurs) 
print(f"Le niveau (rang) moyen des membres du club est : {moyen_niveau}")

"""
avg = sum(ranks.values())
avg/= len(ranks)
print(f"moyenne des rangs du club: {avg}")
"""
"""
for rank in ranks.values():
    sum_rank+=rank
avg=sum_rank/len(ranks)
"""
#######  bonus --> trouver le median #######
rank_values = list(ranks.values())
rank_values.sort()
print(rank_values)

if len(rank_values)%2==0:
    n = len(rank_values) //2
    median = rank_values[(n-1):(n+1)]
else:
    n=len(rank_values)//2 
    median = rank_values[n]
print(f"notre median est de: {median}")
    #// is whole number division

#si le result = impair, prend l'index qui est 0.5 moins que le resultat? CHECK
#si pair, can take the indexes on either side of the number (so the index that is the result and it-1) ? CHECK

"""
# for prenom, rang in info_joueurs.items():
#     joueurs_classés.append(rang)
# median_classe = (median(joueurs_classés))
# # joueurs_classés.sort()
# # median_classe = pop(median(joueurs_classés))
# # print(joueurs_classés)
# print(median_classe)"""