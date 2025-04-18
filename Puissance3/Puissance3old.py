from random import randint

line1ind0 = [" _ ", " _ ", " _ ", " _ ", " _ "]
line2ind1 = [" _ ", " _ ", " _ ", " _ ", " _ "]
line3ind2 = [" _ ", " _ ", " _ ", " _ ", " _ "]
line4ind3 = [" _ ", " _ ", " _ ", " _ ", " _ "]
line5ind4 = [" _ ", " _ ", " _ ", " _ ", " _ "]

tableau = [line1ind0, line2ind1, line3ind2, line4ind3, line5ind4,]

def showgamegrid(grid):#, qtylists, listlength):
    for indexdeline in range(len(tableau)):#len(tableau) = how many little lists in a pile of lists? = colheight
        txt ="" #vide le text à chaque tour de boucle
        for chaquecol in range(len(tableau[indexdeline])): #facon de délcarer columns avec len()? #range(6)?
            txt = txt + tableau[indexdeline][chaquecol]
        print(txt + "\n")

showgamegrid(tableau)



###########jusque là on est bon.##############
# winner = None
# joueur = 2
# tour = 0
# cointoss = randint(1,2)

# def whos_turn(player): #to be placed after a turn is taken
#     if player == 1:
#         player = player + 1
#     else:
#         player = 1
#     print("Maintenant c'est le tour de joueur " +str(player))
#     return player

####TO HAVE AN ALTERNATING INFINTE BOUCLE OF TURNS:######

# #while winner == None:
#     joueur = whos_turn(joueur)
