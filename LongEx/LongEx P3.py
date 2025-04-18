def renvoie_snake_tableau(lines, columns):
    tableau = []
    inline = []
    insert = 1
    for line in range(lines):
        inline = [] #vide la liste à chaque tour de boucle
        for icol in range(columns):
            inline.append(insert)
            insert = insert+1
        if (line+1)%2 == 0:   #or if line % 2 == 1
            inline.reverse()
            # if len(inline)==columns:
            #     tableau.append(inline)
        tableau.append(inline)
    print(tableau)
    return tableau

#print(renvoie_snake_tableau(7,3))

"""
#### ici on utilise .insert pour mettre la num dans la sequence au début.

def renvoie_tableau_serpent(numlines, numcols):
    result = []
    elem = 1
    en_arrière = False
    for i in range(numlines):
        line = []
        for j in range(numcols):
            if en_arrière:
                line.insert(0, elem)
            else:
                line.append(elem)
            elem += 1
        result.append(line)
        if en_arrière:
            en_arrière = False
        else:
            en_arrière =True   ######## we can do this whole 4 line flip-flop like: ########
                                            en_arrière = not en arrière  <-- we treat the two possible states of this var like a switch.
    return result

"""