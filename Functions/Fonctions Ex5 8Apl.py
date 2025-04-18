
def howmanyintheword(word, letter):
    total = 0
    # print(word)
    # print(letter)
    for i in range(len(word)):  #or for i in word:
        if word[i] == letter:
            total = total +1   # or total +=1

    return total



word = input("Mot: ")
letter = input("lettre: ")

print(howmanyintheword(word, letter))
#count = howmanyintheword(word, letter)
#print(f"There are {total} letter {letter}s in the word {word}.")