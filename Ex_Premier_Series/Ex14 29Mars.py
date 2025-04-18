counter = 0
mot = None

while mot != "end":
    mot = input("Donnez-moi un mot:")
    counter = counter + 1
    if mot[0] == "t":
        print(mot + "!!!")

print("Vous avez entré " + str(counter) + " mots pour arriver au 'end'!")

"""
while word != "end":
    word = input("entrez un mot (end pour finir): ")
    if len(word) > 0 and word[0]=="t":
        print(word + "!!!")
        counter = counter + 1
print(counter)
"""