def ia(boites):
    if boites[0]== boites[-1]:
        return('G')
    if boites[0] >boites[1]:
        return('G')
    if boites[-1] >boites[-2]:
        return('D')
    if boites[0] >boites[-1]:
        return('G')
    if boites[-1] >boites[0]: 
        return('D')
    else:
        return('G')
    print(boites)