def ia(boites):
    n = len(boites)
    scores = [[0] * n for _ in range(n)]
    for k in range(n):
        for l in range(n - k):
            if k == 0:
                scores[l][l] = boites[l] if n % 2 == 1 else -boites[l]
            elif (n - 1 - k) % 2 == 0:
                scores[l][l + k] = max(scores[l][l + k - 1] + boites[l + k], scores[l + 1][l + k] + boites[l])
            else:
                scores[l][l + k] = min(scores[l][l + k - 1] - boites[l + k], scores[l + 1][l + k] - boites[l])
    if n == 1:
        return 'G'
    else:
        return 'D' if scores[0][-2] + boites[-1] == scores[0][-1] else 'G'
