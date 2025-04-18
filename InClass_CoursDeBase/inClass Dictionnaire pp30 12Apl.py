ranks = {"Marie":1, "Bernard":4, "François":2, "Thomas":12, "Hila":15}
# removed = {}
# for prenom, rang in info_joueurs.copy():
#     if info_joueurs[rang] >= 10:
#         del info_joueurs[prenom]

# print(info_joueurs)

#         total += rang
#         moyen_niveau = total / len(info_joueurs) 
# print(f"Le niveau (rang) moyen des membres du club est : {moyen_niveau}")

####### correction below ########
toremove = []
#supprimer the needed elements
for name, rank in ranks.items():
    if rank >=10:
        toremove.append(name)

for name in toremove:
    ranks.pop(name)

avg=sum(ranks.values())
avg = avg / len(ranks)
print(avg)

###### OR #######
clone = {}
clone.update(ranks) ##### we will browse the copy and edit the original as consequence

for name, rank in clone.items():
    if rank >= 10:
        ranks.pop(name)

avg=sum(ranks.values())
avg = avg / len(ranks)
print(avg)

######## orrrr Debbies ######
for name, rank in list(ranks.items()): #we create an internal var which is a list version of the dictionary
    if rank >= 10:                      #this is a good option because the list disappears after the loop
        ranks.pop(name)

avg=sum(ranks.values())
avg = avg / len(ranks)
print(avg)

#############################
## ici nous voyons a dictionary comprehension ##
ranks = {name:rank for name, rank in ranks.items() if rank < 10}

avg=sum(ranks.values())
avg = avg / len(ranks)
print(avg)

#############################