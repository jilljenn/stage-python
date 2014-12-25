import random

def ia(nb_allumettes, min_allumettes, max_allumettes):
    module = nb_allumettes % (min_allumettes + max_allumettes)
    if (1 <= module <= min_allumettes):
        return min_allumettes
    elif (module == 0):
        return max_allumettes
    else:
        return random.choice([(module - x) for x in range(1, min_allumettes + 1) if min_allumettes <= (module - x) <= max_allumettes])
