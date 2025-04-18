signes = ["de piques", "de trèfles", "de carreaux", "de coeurs" ]
rangs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]

print("voici toutes les cartes...")

for irang in range(len(rangs)):
    rang = rangs[irang]
    for isigne in range(len(signes)):
        signe = signes[isigne]
        print(rang + " " + signe)

#affectations en plus à éviter pour programmes lourdes (ça bouffe memoire)

"""
VALUES =["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
SYMBOLES["de piques", "de trèfles", "de carreaux", "de coeurs"]

for value in VALUES:
    for symbol in SYMBOLES:
        print(f"{value} of {symbol}")
"""