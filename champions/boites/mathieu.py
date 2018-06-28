def ia(boites):
    if len(boites) == 1:
        return "D"
    if boites[0]-max(boites[1],boites[-1])>boites[-1]-max(boites[0],boites[-2]) :
        return "G"
    else :
        return "D"
