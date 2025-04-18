from random import randint
lettres = ["a", "b", "c", "d", "e", "f"]

#select1 = randint(0,5)
#select1 = randint(0, len(lettres)-1) #this way if the list length changes later, it still works
select1 = int(input("Donnez-moi un numero entre 0 et 5:"))

while select1 < 0 or select1 > len(lettres)-1:
    select1 = int(input("Donnez-moi un numero entre 0 et 5:"))
#print(select1)
print(lettres)

print(lettres[0:select1])
print(lettres[select1:])


