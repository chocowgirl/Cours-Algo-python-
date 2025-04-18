vowels_list = ["a", "e", "i", "o", "u", "y",]
nombre_voyelles = 0
mot = input("Donnez-moi un mot:")
#print(vowels_list[0])
#A PRIORI OK
#for letter in word
for i in range(0, len(vowels_list)):
    target = vowels_list[i]
    #print("targeted vowel is:" + target)
    appearances = mot.count(target)
    #print(appearances)
    nombre_voyelles = nombre_voyelles + appearances

print("Nombre de voyelles dans votre mot : " +str(nombre_voyelles))

"""
vowels = "aeiouy"
count = 0
word = input("mot:)
for letter in word:
    if letter in vowels:
        count +=1

print(f"Il y a {count} voyelles dans '{mot}'.")
"""