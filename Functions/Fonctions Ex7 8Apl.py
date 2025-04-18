# from random import randint

# def mot_5lettres():
#     letters = ["a","i","l","n","o","r","s","t",]
#     mot = ""
#     for i in range(5):
#         letterchoice = letters[randint(0,len(letters)-1)]
#         #print(letterchoice)
#         mot = mot + letterchoice  #or mot += letterchoice, or you can use the return from pop to also erase from letters.
#         #print(mot)
#         letters.remove(letterchoice)
#         #print(letters)
#     return mot


# print(mot_5lettres())


# ##############7bis below#################
# from random import randint


# def mot_xlettres(x):
#     letters = ["a","i","l","n","o","r","s","t",]
#     mot = ""
#     for i in range(x):
#         letterchoice = letters[randint(0,len(letters)-1)]
#         #print(letterchoice)
#         mot = mot + letterchoice
#         #print(mot)
#         letters.remove(letterchoice)
#         #print(letters)
#     return mot

# x=9
# while x >8:
#     x=int(input("Je vais vous faire un mot de ma liste de 8 lettres sans repeter une lettre... vous voulez un mot de combien des lettres: "))
#     if x > 8:
#         print("je peux faire un mot de 8 lettres max si je ne vais pas repeter des lettres... alors...") 

# print(mot_xlettres(x))


##############7tris below################
# from random import randint

# def mot_xlettres(x, listofletters):
#     letters = listofletters
#     mot = ""
#     for i in range(x):
#         letterchoice = letters[randint(0,len(letters)-1)]
#         #print(letterchoice)
#         mot = mot + letterchoice
#         #print(mot)
#         letters.remove(letterchoice)
#         #print(letters)
#     return mot


# x=1000000
# list = []
# ############# main program #############################################
# while x > len(list):
#     string = input("Avez-vous une liste de lettres différentes pour moi?  ")
#     for letter in string:
#         list.append(letter)
#         #print(list)
#     x=int(input("Je vais vous faire un mot de votre liste de lettres sans repeter une lettre... vous voulez un mot de combien des lettres? : "))
#     if x > len(list):
#         print(f"je peux faire un mot de {len(list)} lettres max si je ne vais pas repeter des lettres... alors... {mot_xlettres(len(list),list)}")
#         #print(mot_xlettres(len(list)), list)
#         break
#     else:
#         print(mot_xlettres(x, list))

# ###### add in a failsafe against duplicate characters given by the user