wrong_pw = 0
password = None

while password != "Pyth0n" and wrong_pw<3:
    #print(wrong_pw)
    password = input("Entrez un mot de passe:")

    if password != "Pyth0n":
        print("Code erroné. Essayez à nouveau.")
        wrong_pw = wrong_pw + 1
    else:
        print("Mot de passe valide.")      
        
if wrong_pw == 3:
    print("Mot de passe incorrect. GAME OVER.")