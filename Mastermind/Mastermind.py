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

while len(guess) != CODELENGTH:
    guess = input("Entrez une combinaison de 4 lettres venant de la liste au-dessus (en miniscule, sans espaces) :")
    #if len(guess) != CODELENGTH:
     #   print("J'ai dit QUATRE lettres SANS espaces entre eux...")
guess = list(guess)
print("Votre réponse: " + str(guess))

    
for i in range(CODELENGTH):
    if guess[i] == code[i]:
        bonindex.append(i)
        print(bonindex)
print("Cas des bonnes lettres à leurs bonnes places: " + str(len(bonindex)) + "...")

if guess == code:
    print("YES! Vous avez trouvé le code!!!")

#REGARDER EN CLASS153 CAR NOUS AVONS DEJA AJOUTE pp155BOUCLE JE PENSE LA...


# #CHECK FUNCTIONING
# for i in range(CODELENGTH):
#     #while not (guess == code):
#         if guess[i] == code[i]:
#             bonindex = bonindex+1
#         elif guess[i] == code[1] or guess[i] == code[2] or guess[i] == code[3]:
#             malplacé = malplacé+1
#         print("bon lettre, bon endroit: " + str(bonindex))
#         print("bon lettre(s), mais malplacé: " + str(malplacé))



