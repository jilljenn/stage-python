def ia(boites):
    sp = sum(boites[::2])
    si = sum(boites[1::2])
    if sp > si:
        return 'G'
    else:
        return 'D'
