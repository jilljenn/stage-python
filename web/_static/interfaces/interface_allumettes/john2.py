from random import randint, choice
def ia(allumettes):
    if allumettes == 2:
        return(1)
    if allumettes == 3:
        return (2)
    if allumettes == 4:
        return (3)
    if allumettes == 6:
        return (1)
    if allumettes == 7:
        return (2)
    if allumettes == 8:
        return (3)
    if allumettes == 11:
        return (2)
    if allumettes == 12:
        return (3)
    if allumettes == 13:
        return (3)
    if allumettes == 14:
        return (1)
    if allumettes == 10:
        return(1)
    if allumettes % 2 == 1:
        return (2)
    else:
        return choice([1, 3])
    print(allumettes)