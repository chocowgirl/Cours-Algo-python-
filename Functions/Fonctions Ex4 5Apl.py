from random import randint

def number_spitter_range1_6(length):
    list = []
    for i in range(length):
        rando_num = (randint(1,6))
        list.append(rando_num)
        #print(list)
    return(list)

print(number_spitter_range1_6(18))