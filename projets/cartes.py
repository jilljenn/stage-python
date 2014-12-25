n = 5
cartes = [[] for _ in range(n)]
for i in range(1 << n):
    for b in range(n):
        if len(bin(i)) > b and bin(i)[-(b + 1)] == '1':
            cartes[b].append(i)
for carte in cartes:
    print(r'\begin{tabular}{cccc}')
    for i in range(4):
        print(' & '.join(map(str, carte[4 * i:4 * (i + 1)])) + r'\\')
    print(r'\end{tabular}')
    print(r'\newpage')
