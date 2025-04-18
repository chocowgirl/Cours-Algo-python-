def remove_vowels(word):
    vowels = "aeiouy"
    answer = ""
    for i in range(len(word)):
        if word[i] not in vowels:
             answer = answer + word[i]
            #  print(answer)
    return answer

print(remove_vowels("cumulonimbus"))
#word = input("Word: ")
#print(remove_vowels(word))

""" IL Y A AUTRE CHOSE Q'ON PEUT FAIRE AVEC UN TRUC:
replace()
This function is used to replace characters in a string
So we can replace the vowel using replace and putting "" in place of the vowel (thus erasing it from the word)
"""