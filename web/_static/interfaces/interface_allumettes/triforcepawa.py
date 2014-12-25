# Créé par Florian, le 23/12/2014 en Python 3.2
from random import choice
def ia(nb_allumettes):
    if nb_allumettes % 4 == 0: #Là je gagne#
        return 3
    if nb_allumettes % 4 == 1:
        return choice([1, 3])
    if nb_allumettes % 4 == 2: #là aussi#
        return 1
    if nb_allumettes % 4 == 3: #Et là encore B)))#
        return 2
