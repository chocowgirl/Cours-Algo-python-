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

example_numbers = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
irregular_example = [[1,2,3],[4,5,6,7,8,9,10],[11,12,13,14,15]]
another_example = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
last_example = [[2,4,6,8],[10,12,14,16],[18,20,22,24]]
reject_tableau1 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
reject_tableau2 = [[1,2,3,4,5,6,7,8,9,10]]

screen_tableau(reject_tableau2)

"""
Un return dans la fonction sera un façon de stopper sans avoir besoin 

def tableau_valide(tableau, n): ### the n here allows for flexibility in defining what's ok
    if len(tableau) > n:
        return False 
    
    for line in tableau:
        if len(line) > 9:
            return False

    return True

Puis dans la fonction affiche:
au debut on met:

if tableau_valide(tableau): ### façon de dire "if tableau_valide(tableau) == True"
"""