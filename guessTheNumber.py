from random import randint
number = randint(1, 10)
#print(number)
guess = None
guess_count = 0

while guess != number and guess_count<3:
    guess = int(input("Donnez-moi un nombre entre 1 et 10:"))
    guess_count = guess_count + 1
    
    if guess < number:
        print("votre nombre est trop petit.")
    elif guess > number:
        print("votre nombre est trop grand.")
    else:
        print("Vous l'avez trouvé! Félicitations!")
        
if guess != number:
    print("3 essais sans succes.  Le bon nombre était " + str(number))