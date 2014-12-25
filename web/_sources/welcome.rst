
===========================
Lundi matin - Prise en main
===========================

Voici quelques exemples de code pour bien démarrer.

Calcul
::::::

.. activecode:: exemple_calculs

    print("Coucou !")
    print(2 * 3)
    print((3 + 3) * 7)

Variables
:::::::::

Les variables contiennent des données qu'on peut utiliser dans les programmes.

.. activecode:: exemple_variables

    nbEtoiles = 5
    print("*" * nbEtoiles)
    print("Il y a", nbEtoiles, "etoiles")
    print("S'il y en avait deux fois plus, il y en aurait", nbEtoiles * 2)

Changez la valeur de ``nbEtoiles`` et relancez le code.

.. activecode:: maj_variables

    nbClients = 0
    nbClients += 10
    nbClients = nbClients * 2 + 10
    print(nbClients)

Voyons ce qu'il se passe à chaque étape :

.. codelens:: maj_variables_debug

    nbClients = 0
    nbClients += 10
    nbClients = nbClients * 2 + 10
    print(nbClients)

Répétitions
:::::::::::

On peut répéter des instructions à l'aide de la boucle ``for``. Voici un exemple avec 5 **itérations** de l'instruction ``print("Coucou !")`` :

.. activecode:: boucles

    for i in range(5):
        print("Coucou !")

À l'intérieur de la boucle, ``i`` contient le numéro de l'itération courante (attention : ce nombre commence à 0).

.. activecode:: index

    for i in range(5):
        print(i)

- Adaptez ce code pour afficher tous les nombres de 0 à 99, puis tous les nombres de 1 à 100.
- Écrivez un code qui affiche un rectangle de 3 × 5 symboles ``x``
- Écrivez un code qui affiche un triangle de 5 symboles ``o``

Si l'on reprend l'exemple du nombre de clients :

.. codelens:: maj_variables_iterees

    nbClients = 0
    for i in range(5):
        nbClients += 10
        nbClients = nbClients * 2 + 10
    print(nbClients)

Conditions
::::::::::

.. activecode:: condition

    jour = 25
    mois = "Decembre"
    if jour == 25 and mois == "Decembre":
        print("Joyeux Noel !")
        print("Toutes les instructions de ce cote-ci sont executees")
    else:
        print("Rien a signaler")
        print("Les instructions de ce cote-la ne sont pas executees")

.. activecode:: condition_allumettes

    nbAllumettes = 5
    if nbAllumettes < 1:
        print("Ce nombre est trop faible")
    elif nbAllumettes > 3:
        print("Ce nombre est trop grand")
    else:
        print("Ce nombre est correct")

Changez la valeur de ``nbAllumettes`` et relancez le code.

Tableaux
::::::::

.. activecode:: exemple_tableaux

    tableau = [1, 2, 3]
    print(tableau[0])
    print(tableau[2])
    print("Le tableau a", len(tableau), "elements")
    tableau[1] = 1000  # Remplacement d'un element du tableau
    print(tableau)

Vous pouvez donc afficher les différents éléments du tableau ainsi :

.. activecode:: iteration_tableaux

    agesSoeurs = [14, 17, 47]
    for idSoeur in range(len(agesSoeurs)):
        print("La soeur numero", idSoeur, "a", agesSoeurs[idSoeur], "ans")

Ou bien ainsi :

.. activecode:: iteration_tableaux_bis

    agesSoeurs = [14, 17, 47]
    for age in agesSoeurs:
        print(age)

Chaînes de caractères
:::::::::::::::::::::

Les chaînes de caractères ont un fonctionnement similaire aux tableaux.

.. activecode:: chaines

    chaine = "abracadabra"
    for i in range(len(chaine)):
        print('Le caractere', i, 'est', chaine[i])

.. activecode:: chaines_bis

    chaine = "abracadabra"
    for lettre in chaine:
        if lettre == 'a':
            print("Il y a un A !")

Changez la valeur de ``chaine`` et relancez le code.

Dictionnaires
:::::::::::::

.. activecode:: exemple_dictionnaires

    dico = {"prenom": "Joseph", "nom": "Marchand"}
    print("Le prenom est", dico["prenom"])
    print("Le nom est", dico["nom"])
    dico["prenom"] = "Josephine"  # Remplacement de cle
    dico["age"] = 18  # Ajout de cle
    print("En fait, le prenom est", dico["prenom"], "et l'age est", dico["age"], "ans")

.. activecode:: annuaire

    annuaire = [
        {"prenom": "Joseph", "nom": "Marchand", "tel": "0642424242"},
        {"prenom": "Barack", "nom": "Obama", "tel": "0144080190"},
        {"prenom": "Pere", "nom": "Noel", "tel": "0836656565"},
    ]
    for entree in annuaire:
        if entree["nom"] == "Obama":
            print("Le numero d'Obama est", entree["tel"])
