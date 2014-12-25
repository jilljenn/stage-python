# Créé par Florian, le 23/12/2014 en Python 3.2

def ia(boites):
    if len(boites) < 2:
        return 'G'
    if boites[-2] <= boites[1]:
        return 'G'
    else:
        return 'D'
