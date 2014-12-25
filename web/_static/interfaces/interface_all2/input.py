def ia(nb_allumettes, min_all, max_all):
    print("Vous pouvez prendre entre %d et %d allumettes" % (min_all, max_all))
    print("il reste %d allumettes" % nb_allumettes)
    return (int(input("Combien d'allumettes voulez-vous retirer ? ")))
