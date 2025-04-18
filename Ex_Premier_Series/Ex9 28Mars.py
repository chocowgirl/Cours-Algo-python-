from random import randint
num1= 1
num2= 2
num3= 3
#print(num1, num2, num3)

while not (num1 == num2 and num2 == num3): 
    num1 = randint(1,6)
    num2 = randint(1,6)
    num3 = randint(1,6)
    print(num1, num2, num3)
    if num1 == num2 and num2 == num3:
        print(":D")
