def play(boites, scores, mi, left):
    s = list(scores)
    if left:
        s[int(mi)] += boites[0]
        return (boites[1:], tuple(s))
    else:
        s[int(mi)] += boites[-1]
        return (boites[:-1], tuple(s))

def minmax(boites, scores=(0, 0), mi=False):
    if boites == []:
        return scores, [], '_'

    r = [minmax(*play(boites, scores, mi, m), mi=not mi) for m in (True, False)]

    if r[0][0][0] >= r[1][0][0]:
        return r[int(mi)][:2] + ('G', )
    else:
        return r[int(not mi)][:2] + ('D', )

def ia(boites):
    return minmax(boites)[2]
