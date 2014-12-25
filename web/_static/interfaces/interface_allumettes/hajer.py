def ia(nb_allumettes):
    if nb_allumettes % 2 != 0:
        return 3
    else:
        if nb_allumettes >= 6:
            return 2
        else:
            return 1
