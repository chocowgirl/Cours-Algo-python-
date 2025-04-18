from random import randint

# grid = [["a", "b", "c", "d"], ["e", "f", "g", "h",], ["i", "j", "k", "l",]]

# for iline in range(3):
#     txt ="" #vide le text à chaque tour de boucle
#     for icol in range(4):
#         txt = txt + grid[iline][icol]
#     print(txt + "\n")

grid = [[1,2,3,4,], 
        [5,6,7,8,], 
        [9,10,11,12,]]

for iline in range(3):
    num = ""
    for icol in range(4):
        num = num + str(grid[iline][icol]/2) + " "  #num += f"{grid[iline][icol]/2} "
    print(num + "\n")

    """
# table = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]]
### OR #########################
line1 = [1,2,3,4],
line2 = [5,6,7,8],
line3 = [9,10,11,12]]
table = [line1, line2, line3]
#################################   
for line in range(len(table)):
        txt = ""
    for column in range(len(table[line])):
        txt += f"{table[line][column]/2}"
    print(txt)
#######################################
              ORRRRR...
########################################    

 table = [
     [1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]

for line in table:
    txt = ""
    for value in line:
        txt += f"{value/2} "
    print(txt)

    """


