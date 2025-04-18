liste = [1, 2, 3, 4, 5,]
print(liste)
last_removed = None

while len(liste)>0:
    last_removed = liste.pop(0)
    print(last_removed)
    print(liste)

print("all done")
