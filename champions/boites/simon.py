def ia(boites):
    N = len(boites)
    if (N >= 2):
        if (boites[-1]-boites[-2] > boites[0]-boites[1]):
            return ("D")
        else:
            return ("G")
    else:
        return ("G")
