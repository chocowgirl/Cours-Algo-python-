from random import randint
POSSIBLE_LETTERS = ["a", "b", "c", "d", "e", "f"]
print(POSSIBLE_LETTERS)
CODELENGTH = 4
code = []
guess = []
bonindex = []
malplacé = []
#ICI ON A L'ANCIEN CONSTRUCTION DU CODE 4 CHIFFRES, PUIS LE NOUVEAU
                                            # while len(code) < 4:
                                            #     hat_num = randint(0,5)
                                            #     code.append(possible_letters[hat_num])

for _ in range(CODELENGTH): #au lieu de i on met _ car nous n'utilisons pas le "i" dans le boucle
    hat_index = randint(0,len(POSSIBLE_LETTERS)-1)
    code.append(POSSIBLE_LETTERS[hat_index])
print(code)

while guess != code: #this is ok here because we have generated a code b4 so code and guess are no longer equal
    guess = []  #with these next three lines we reset the lists involved in guesses and right or right-ish answers
    bonindex = []
    malplacé = []
    while len(guess) != CODELENGTH:
        #print(code) this is here in case I need to double check functioning
        guess = input("Entrez une combinaison de 4 lettres venant de la liste au-dessus (en miniscule, sans espaces) :")
        #if len(guess) != CODELENGTH:  part of extra foufou feature to test at the end
        #   print("J'ai dit QUATRE lettres SANS espaces entre eux...")  this is an extra foufou feature to test at the end
    guess = list(guess)
    print("Votre réponse: " + str(guess))

    #to identify the cases of right letter, right place (and to store the indexes involved)    
    for i in range(CODELENGTH):
        if guess[i] == code[i]:
            bonindex.append(i)
            #print(bonindex) #this tracks the iterations of bonindex and shows the result for QA
    print("Cas des bonnes lettres à leurs bonnes places: " + str(len(bonindex)) + "...")

# if guess == code:
#     print("AMAZING! Vous avez mis toutes les lettres dans leurs bonnes places!")