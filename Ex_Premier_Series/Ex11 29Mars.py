from random import randint
num1 = randint(0,100)
num2 = randint(0,100)
somme = num1 + num2
# print(num1)
# print(num2)
# print(somme)
user_guess = -1 #int(input("Calculez la somme de " + str(num1) + " et " + str(num2) +":"))
number_tries = 0


while user_guess != somme:
    user_guess = int(input("Calculez la somme de " + str(num1) + " et " + str(num2) +":"))
    number_tries = number_tries +1
    #print("essais:" +str(number_tries))

if user_guess == somme:
    print("YES!  Bravo!  Erreurs commises avant d'avoir trouvé la bonne solution: " + str(number_tries -1))
