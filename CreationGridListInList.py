from random import randint

grid = [["a", "b", "c", "d"], ["e", "f", "g", "h",], ["i", "j", "k", "l",]]

for line in range(len(grid)):
    txt ="" #vide le text à chaque tour de boucle
    for icol in range(len(grid[line])):
        txt = txt + grid[line][icol]
    print(txt + "\n")

