def binaire(n):
    S = ""
    while n > 0:
        if n % 2 == 0:
            S = "0" + S
            n = n // 2
        else:
            S = "1" + S
            n = n // 2
    return S

nb_cartes = 5
cartes = [[] for _ in range(nb_cartes)]
nb_max = 2 ** nb_cartes
for nombre in range(nb_max):
    encodage = binaire(nombre)
    for b in range(nb_cartes):
        if len(encodage) >= b + 1 and encodage[-(b + 1)] == '1':
            cartes[b].append(nombre)
for carte in cartes:
    print(carte)
