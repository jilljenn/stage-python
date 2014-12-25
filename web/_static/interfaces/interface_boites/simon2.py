def iaAlpha(B):
    N = len(B)
    if N >= 2:
        if B[-1]-B[-2] > B[0] - B[1]:
            return('D')
        elif B[-1] - B[-2] < B[0] - B[1]:
            return('D')
        else:
        egalite(B)

def egalite(B):
    N = len(B)
    for i in range(N//2):
        if B[i+1] - B[i+2] > B[-i-2] - B[-i-3]:
            if i%2 == 0:
                return('D')
            else:
                return('G')
        elif B[i+1]
