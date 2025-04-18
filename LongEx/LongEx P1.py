def screen_tableau(grid):
    numlists=len(grid) #measures and stores how many lists are in the tableau
    print(f"number of lists = {numlists}")
    if numlists>9:
        print("Tableau trop grand. (Plus que 9 listes)")
        quit() #rejects tableau and ends program if there are more than 9 lists
    
    for i in range(numlists): #for each list in the pile of lists:
        numcol = len(grid[i]) #defines and stores how many elements are in the list currently being measured
        print(f"number of elements in line {i} = {numcol}")
        if numcol>9:
            print("Tableau trop grand. (Plus que 9 elements dans une liste)")
            quit() #if a list contains more than 9 elements the tableau is rejected and the program ends
    print(f"numlists = {numlists}, numcol = {numcol}")
    return numlists, numcol #returns correct tableau dimensions (so long as tableau isn't irregular)


def affiche_tableau(grid):
    screen_tableau(grid)
    for line in range(len(grid)):
        txt = "" #vide le text à chaque tour de boucle
        for icol in range(len(grid[line])):
            if grid[line][icol] > 9:
                txt = txt + f"{grid[line][icol]} "
            else:
                txt = txt + f"{grid[line][icol]}  "
        print(txt)


example_numbers = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
another_example = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
irregular_example = [[1,2,3],[4,5,6,7,8,9,10],[11,12,13,14,15]]
last_example = [[2,4,6,8],[10,12,14,16],[18,20,22,24]]
reject_tableau1 = [[1,2,3,4,5,6,7,8,9,10]]
reject_tableau2 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

affiche_tableau(example_numbers)