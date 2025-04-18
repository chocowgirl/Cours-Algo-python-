def screen_tableau(grid):
    numlists=len(grid) #measures and stores how many lists are in the tableau
    #print(f"number of lists = {numlists}")
    if numlists>9:
        print("Tableau trop grand. (Plus que 9 lignes)")
        quit() #rejects tableau and ends program if there are more than 9 lists
    
    for i in range(numlists): #for each list in the pile of lists:
        numcol = len(grid[i]) #defines and stores how many elements are in the list currently being measured
        #print(f"number of elements in line {i} = {numcol}")
        if numcol>9:
            print("Tableau trop grand. (Plus que 9 colonnes)")
            quit() #if a list contains more than 9 elements the tableau is rejected and the program ends
    #print(f"numlists = {numlists}, numcol = {numcol}")
    #return numlists, numcol #returns correct tableau dimensions (so long as tableau isn't irregular)



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



def renvoie_tableau_escargot(num_lines, num_cols):
    result = []
    for i in range(num_lines):
        line = []
        for j in range(0, num_cols):
            line.append(0)
        result.append(line)

    elem = 1
    start_line = 0  #+1
    end_line = num_lines -1 #-1
    startcol = 0 #+1
    endcol = num_cols -1 #-1

    while startcol <= endcol and start_line <= end_line:
        
        for c in range(startcol, endcol + 1):
            result[start_line][c] = elem
            elem += 1
        if elem > num_lines*num_cols:
            break

        for L in range(start_line +1, end_line +1):
            result[L][endcol] = elem
            elem += 1
        if elem > num_lines*num_cols:
            break

        for c in range(endcol-1, startcol-1, -1): #range of endcol-1 to startcol -1 inlcuded by steps of -1
            result[end_line][c] = elem
            elem += 1
        if elem > num_lines*num_cols:
            break

        for L in range(end_line-1, start_line, -1): # le 0 car on veut s'arreter sur index de line 1, le -1 car on va par pas de -1 dans les indexes
            result[L][startcol] = elem
            elem += 1
        if elem > num_lines*num_cols:
            break

        start_line += 1
        end_line -= 1
        startcol += 1
        endcol -= 1

    return result



affiche_tableau(renvoie_tableau_escargot(8,7))