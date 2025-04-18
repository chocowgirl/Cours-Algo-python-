number = 0
while number<1 or number>10:
    number = int(input("Entrez un nombre entre 1 et 10:"))

    if number<1 or number>10:
        print("Il faut entrez un nombre ENTRE 1 ET 10")
    else:
        print("Merci :)")