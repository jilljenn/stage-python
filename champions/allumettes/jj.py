import random

def ia(nb_allumettes):
    if nb_allumettes % 4 == 1:
        return random.randint(1, 3)
    else:
        return (nb_allumettes % 4 + 4 - 1) % 4
