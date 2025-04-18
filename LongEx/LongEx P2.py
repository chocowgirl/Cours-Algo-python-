
def renvoie_tableau(lines, columns):
    tableau = []
    inline = []
    insert = 1
    for line in range(lines):
        inline = [] #vide la liste à chaque tour de boucle
        for icol in range(columns):
            inline.append(insert)
            insert = insert+1
            # if len(inline)==columns:
            #     tableau.append(inline)
        tableau.append(inline)
    return tableau

#print(renvoie_tableau(5,5))

"""
def renvoie_tableau(numlines, numcols):
    result = []
    elem = 1
    for i in range(num_lines):
        line = []
        for j in range(num_cols):
            line.append(elem)
            elem += 1
        result.append(line)
    return result

###### ORRRR ####### POUR NE PLUS AVOIR BESOIN D'UN COMPTEUR #########

def renvoie_tableau(numlines, numcols):
    result = []
    for i in range(num_lines):
        line = []
        for j in range(num_cols):
            line.append(i * num_cols + j + 1)
            elem += 1
        result.append(line)
    return result

################################################
    
or on peut utiliser n (numlines * numcols) to count using for i in range(n)
"""