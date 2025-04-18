TOKEN_1 = "O"
TOKEN_2 = "X"
VIDE = "."

def get_token(player):
    if player == 1:
        return TOKEN_1
    return TOKEN_2


def display_grid(grid):
    for line in range(len(grid)):
        text = ""
        for col in range(len(grid[line])):
            text = text + " " + grid[line][col]
        print(str(line) + text)

    text = ""
    for last_line in range(len(grid[0])):
        text = text + f" {last_line}"
    print(f" {text}")

# # def reset_grid(grid):
#      #tableau = [
#     [".", ".", ".", ".", "."],
#     [".", ".", ".", ".", "."],
#     [".", ".", ".", ".", "."],
#     [".", ".", ".", ".", "."],
#     [".", ".", ".", ".", "."],
# ]



def check_vertical(tableau, line, column):
    if line >= 3:
        return False #or we could say if and then if with if line is 2 or smaller and if (nest the following verifs)
    if tableau[line][column]==tableau[line+1][column]and tableau[line][column]==tableau[line+2][column]:
        return True
    # ^  si les deux jetons en dessous sont == au jeton(line, column), on renvoie True
    #sinon renvoie Faux
    return False

def check_horizontal(tableau, line, column):
    #d'abord check to the right of your just dropped piece:
    if column <=2:
        if tableau[line][column]==tableau[line][column+1]and tableau[line][column]==tableau[line][column+2]:
            return True
    #then to the left:
    if column >=2:
        if tableau[line][column]==tableau[line][column-1]and tableau[line][column]==tableau[line][column-2]:
            return True
    #then check to each side of it:
    if column >=1 and column <=3:
        if tableau[line][column]==tableau[line][column-1]and tableau[line][column]==tableau[line][column+1]:
            return True
    return False


def check_diagonal(tableau, line, column):
    #first check for a line down to the right of the piece:
    if line <= 2 and column <= 2:
        if tableau[line][column]==tableau[line+1][column+1] and tableau[line][column]==tableau[line+2][column+2]:
            return True
    #now check for a line up and to the left of the piece:
    if line >= 2 and column >= 2:
        if tableau[line][column]==tableau[line-1][column-1] and tableau[line][column]==tableau[line-2][column-2]:
            return True
    #now check for a line up to the left AND down to the right of the last piece:
    if line >=1 and line <=3 and column >=1 and column <=3:
        if tableau[line][column]==tableau[line-1][column-1] and tableau[line][column]==tableau[line+1][column+1]:
            return True
    #now check for a line up and to the right of the piece:
    if line >=2 and column <=2:
        if tableau[line][column]==tableau[line-1][column+1] and tableau[line][column]==tableau[line-2][column+2]:
            return True
    #now check for a line down and to the left of the piece:
    if line <=2 and column >=2:
        if tableau[line][column]==tableau[line+1][column-1] and tableau[line][column]==tableau[line+2][column-2]:
            return True
    #now check for a line down to the left and up to the right of the piece:
    if line >=1 and line <=3 and column >=1 and column <=3:
        if tableau[line][column]==tableau[line+1][column-1] and tableau[line][column]==tableau[line-1][column+1]:
            return True
    return False


def check_winner(tableau, column, player):
    line = 0
    while tableau[line][column]==VIDE:
        line+=1 #ici on fait la verif from top to bottom
        #we are checking for vertical victory:
    if check_vertical(tableau, line, column):
        return True
    if check_horizontal(tableau, line, column):
        return True
    if check_diagonal(tableau, line, column):
        return True



    return False


# def play(tableau, column, player):
#     if tableau[4][column] == VIDE:
#         tableau[4][column] = get_token(player)
#     elif tableau[3][column] == VIDE:
#         tableau[3][column] = get_token(player)
#     elif tableau[2][column] == VIDE:
#         tableau[2][column] = get_token(player)
#     elif tableau[1][column] == VIDE:
#         tableau[1][column] = get_token(player)
#     elif tableau[0][column] == VIDE:
#         tableau[0][column] = get_token(player)
#     elif player == 1:
#             player = 2
#     else: player = 1 
#     #this is supposed to find for the given column the first available linespace in that column
#     # line = 4
#     # # #this is to start at the bottom and work your way up
#     # while tableau[line][column] != VIDE and line > -1:
#     #     line -= 1 #(or line = line -1)
#     # token = get_token(player)
#     #
#     # tableau[line][column] = token #placer lebon token dans la colonne a la ligne trouvee

#     return tableau

def play(tableau, column, player):
    
    # trouver pour la colonne passeée en paramètre la première ligne vide
    line = 4

    while tableau[line][column] != '.' and line > -1:
        line -= 1

    # placer le bon token dans la colonne à la ligne trouvée. 
    if line > -1:
        tableau[line][column] = get_token(player)

    return tableau

def stalemate(tableau):

    for i in range(5):
        if tableau[0][i] == VIDE:
            return False
    print("Personne a gagné, je vide le tableau et vous continuez")

    return True


# line1ind0 = [" _ ", " _ ", " _ ", " _ ", " _ "]
# line2ind1 = [" _ ", " _ ", " _ ", " _ ", " _ "]
# line3ind2 = [" _ ", " _ ", " _ ", " _ ", " _ "]
# line4ind3 = [" _ ", " _ ", " _ ", " _ ", " _ "]
# line5ind4 = [" _ ", " _ ", " _ ", " _ ", " _ "]

# tableau = [line1ind0, line2ind1, line3ind2, line4ind3, line5ind4,]
tableau = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
]

################ dont use these until they are fixed for display ################
# def showgamegrid(grid):#, qtylists, listlength):
#     for indexdeline in range(len(grid)):#len(tableau) = for each little list in a pile of lists = how many = colheight
#         txt ="" #vide le text à chaque tour de boucle
#         for chaquecol in range(len(grid[indexdeline])):#len(tableau[5]) = the length of the (5th) list of the tableau
#             txt = txt + grid[indexdeline][chaquecol]
#         print(txt + "\n")

#     text = ""
#     for last_line in range(len(grid[0])):
#         text = text + f" {last_line}"
#     print(f" {text}")

# showgamegrid(tableau)

# def display_grid2(grid):
#     i = 0
#     for line in grid:
#         text = ""
#         for element in line:
#             text = text + " " + element
#         print(str(i) + text)
#         i = i + 1

#     text = ""
#     i = 0
#     for last_line in grid[0]:
#         text = text + f" {i}"
#         i = i + 1
#     print(f" {text}")
###########################################################################
winner = None
player = 1

while winner == None:
    
    display_grid(tableau)
    column = input(f"joueur {player} ({get_token(player)}), où vas tu jouer? ")
    column = int(column)

    play(tableau, column, player)

    # On joue un tour
    if check_winner(tableau, column, player):
        winner = player
        display_grid(tableau)
        print(f"Félicitations joueur {winner} ({get_token(winner)}), vous avez gagné!")

    else:
        if stalemate(tableau):
            tableau = [
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],]
        if player == 1:
            player = 2
        else:
            player = 1
    

