entries = []
entry = input("Il me faut un mot... pourriez-vous me donner un? : ")


while entry != "stop":
    placement= int(input("a quel index dois-je placer ce mot? :"))
    entries.insert(placement, entry)
    #print(entries)
    entry = input("J'ai besoin d'un mot... tâpez un mot pour moi: ")

print("your list:")
print(entries)



"""DOMMAGE DE COMPARER LE != STOP DEUX FOIS
entries []
entry = input("word?:")

while entry != "stop":
    entries.append(entry)
    entry = input("word?:")
    
    

print(entries)"""