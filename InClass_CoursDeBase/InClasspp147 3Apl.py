from random import randint
POSSIBLE_LETTERS = ["a", "b", "c", "d", "e", "f"]
CODELENGTH = 4
#print(POSSIBLE_LETTERS)
code = []

#ICI ON A L'ANCIEN CONSTRUCTION DU CODE 4 CHIFFRES, PUIS LE NOUVEAU
                                            # while len(code) < 4:
                                            #     hat_num = randint(0,5)
                                            #     code.append(possible_letters[hat_num])
for _ in range(CODELENGTH): #BONNE PRATIQUE SI ON NE VA PAS UTILISER LE i POUR GUIDER AUTRE CHOSE DANS LE BOUCLE
    hat_index = randint(0,len(POSSIBLE_LETTERS)-1)
    code.append(POSSIBLE_LETTERS[hat_index])
print(code)