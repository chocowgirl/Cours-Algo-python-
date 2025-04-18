from random import randint
code = "" # or: code = []

def randletter():
    letters = ["a","b","c","d","e"] #or : letters = "abcde"
    indexinletters = randint(0, len(letters)-1)
    letter = letters[indexinletters]
    return letter

#line below was used for QA of above function
#print(randletter())

for _ in range(5):
    code = code + randletter() #or if code s/b in list-form: code.append(randletter())
    #ou code += randletter()
print("code = " + code)