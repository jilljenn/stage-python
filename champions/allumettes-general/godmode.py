# Créé par Florian, le 23/12/2014 en Python 3.2
def ia(nb_allumettes, mina, maxa):
    if 1 <= nb_allumettes % (mina + maxa) <= mina:
        return random.randint(mina, maxa)
    elif nb_allumettes % (mina + maxa) == 0:
        return maxa
    else:
        return max(mina, (nb_allumettes % (mina + maxa)) - mina)
