#tableau = [[1,2,3,], [4,5,6,], [7,8,9,]]
#tableau = [[-10, -11, -12, -13,], [-20, -21, -22, -23,], [-30, -31, -32, -33,], [-40, -41, -42, -43,]]

def add_total_tableau(grid):
    num = 0
    for indexdeline in range(len(grid)):#len(tableau) = how many little lists in a pile of lists? = colheight
        for chaquecol in range(len(grid[indexdeline])): #len(tableau[5]) = the length of the line of the tableau
            num = num + grid[indexdeline][chaquecol]
    print(num)
    #print(addition)


add_total_tableau(tableau)


# lineind0 = [" _ ", " _ ", " _ ", " _ ", " _ "]
# lineind1 = [" _ ", " _ ", " _ ", " _ ", " _ "]
# lineind2 = [" _ ", " _ ", " _ ", " _ ", " _ "]
# lineind3 = [" _ ", " _ ", " _ ", " _ ", " _ "]
# lineind4 = [" _ ", " _ ", " _ ", " _ ", " _ "]

# tableau = [lineind0, lineind1, lineind2, lineind3, lineind4,]

# def showgamegrid(grid):#, qtylists, listlength):
#     for indexdeline in range(len(grid)):#len(tableau) = how many little lists in a pile of lists? = colheight
#         txt ="" #vide le text à chaque tour de boucle
#         for chaquecol in range(len(grid[indexdeline])):#len(tableau[5]) = the length of the 5th of the tableau
#             txt = txt + grid[indexdeline][chaquecol]
#         print(txt + "\n")

# showgamegrid(tableau)

"""For this exercise, if we are adding or multiplying no subtotal is necessary in the place where in constructing a table
we have emptied the line text.  However, (supposedly) if we had to do subtraction operations or division it might be otherwise


def sumlist(table):
    sum_numbers = 0
    for line in table:
        for value in line:
            sum_numbers += value
            
    print sum_numbers
        
sumlist(tableau)

Here because we just want to go through the table without worrying too much about positions, we don't 
need to really use indexes in our function if we don't want to.

def sumlist(table):
    sum_numbers = 0
    for line in table:
        sum_numbers += sum(line)  <---This function, sum(), is not something we'd learned yet but we could use too.
            
    print sum_numbers
        
sumlist(tableau)

"""