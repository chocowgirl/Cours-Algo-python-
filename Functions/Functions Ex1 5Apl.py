user_word = input("Donnez-moi un mot et je vais l'invertir: ")

def reverse_it(the_thing):
    word_length = len(the_thing)
    reversed_word = ""
    for i in range(word_length):
        reversed_word = reversed_word + the_thing[word_length-1]
        word_length -= 1
        #print(reversed_word)
    return reversed_word

print(reverse_it(user_word))


"""
def invert_word():
    result = ""
    for i in range(-1, -len(word)-1, -1):
        result = result + word[i]

    return result

user_word = input("Entrez un mot: ")
print(invert_word(user_word))
"""

"""
def invert_word():
    result = ""
    i = -1
    for letter in word:
        pick = word[i]
        result = result + pick
        i = i - 1
"""

"""
POUR FAIRE SANS UTILISER LES INDEXES:

result = ""
for letter in word:
    result = letter + result
return result

print(result)
"""
