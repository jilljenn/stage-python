def ia(boites):
    n = len(boites)
    Sgauche = sum((boites[:n // 2]))
    Sdroite=(sum(boites[n // 2:]))
    if n == 10:
        if Sgauche> Sdroite:
            return "D"
        else:
            return "G"
    else:
        if boites[0] > boites[-1]:
            return "G"
        else:
            return "D"