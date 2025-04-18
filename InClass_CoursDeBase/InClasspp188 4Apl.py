from random import randint
greetlist = ["Bonjour", "Hello", "Ola", "Ciao"]

def random_greet():
    greet = randint(0,3)# or greet = randint(0,len(greetlist)-1)
    #print(greet)
    print(greetlist[greet])

for i in range(100):
    random_greet()

"""
from random import randint

def random_greet():
    possibilities = ["Bonjour", "Hello", "Ola", "Ciao"]
    greet = randint(0,3)# or greet = randint(0,len(possibilities)-1)
    #print(greet)
    print(possibilites[greet])

for _ in range(100):
    random_greet()
"""