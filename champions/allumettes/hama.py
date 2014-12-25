def ia(nb_allumettes):
    if (nb_allumettes % 2 != 0):
        return 2
    elif (nb_allumettes % 4 == 0):
        return 3
    else:
        return 1
