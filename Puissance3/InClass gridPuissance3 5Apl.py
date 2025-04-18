from random import randint

line1ind0 = [" _ ", " _ ", " _ ", " _ ", " _ "]
line2ind1 = [" _ ", " _ ", " _ ", " _ ", " _ "]
line3ind2 = [" _ ", " _ ", " _ ", " _ ", " _ "]
line4ind3 = [" _ ", " _ ", " _ ", " _ ", " _ "]
line5ind4 = [" _ ", " _ ", " _ ", " _ ", " _ "]

tableau = [line1ind0, line2ind1, line3ind2, line4ind3, line5ind4,]

def showgamegrid(grid):#, qtylists, listlength):
    for indexdeline in range(len(tableau)):#len(tableau) = for each little list in a pile of lists = how many = colheight
        txt ="" #vide le text à chaque tour de boucle
        for chaquecol in range(len(tableau[indexdeline])):#len(tableau[5]) = the length of the (5th) list of the tableau
            txt = txt + tableau[indexdeline][chaquecol]
        print(txt + "\n")

showgamegrid(tableau)
"""

def display_grid(grid):
    for line in range(len(grid)):
        text = ""

        for col in range(len(grid[line])):
            text = text + grid[line][col]
        print(str(line) + text)
    
    text = ""
    for last_line in range(len(grid[line])): #or (len(grid[0]))
        text = text + f" {last_line}"
    print(f" {text}")

#########
def check_winner(grid, current_player):
    return current_player == 2:
#### above is the same as:
    if current_player == 2:
        return True
    else:
        return False

   
winner = None
player = 1

while winner == None:
    display_grid(tableau)

#on jour un tour

    if check_winner(tableau, player): #si check winner fontion return un True,
        winner = player
    else:
        

##########
"""
# def display_grid2(grid):
#     i = 0
#     for line in grid:
#         text = ""

#         for element in line:
#             text = text + " " + element
#         print(str(i) + text)
#         i = i + i
#     text = ""
#     for last_line in grid[0]:
#     ###########faut remedier ce partie ici il a passé aux autres choses#########
#         text = text + f" {last_line}"
#     print(f" {text}")


# display_grid(tableau)
# """
###########jusque là on est bon.##############
# winner = None
# joueur = 2
# tour = 0
# cointoss = randint(1,2)

# def whos_turn(player): #to be placed after a turn is taken
#     if player == 1:
#         player = 2
#     else:
#         player = 1
#     print("Maintenant c'est le tour de joueur " +str(player))
#     return player

####TO HAVE AN ALTERNATING INFINTE BOUCLE OF TURNS:######

# #while winner == None:
#     joueur = whos_turn(joueur)
