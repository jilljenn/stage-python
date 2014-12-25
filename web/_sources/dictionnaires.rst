
==========================================
Lundi après-midi - Langue française & IMDb
==========================================

Dictionnaires
:::::::::::::

Voici un compteur qui contient initialement deux clés : 5 et 1, associées respectivement aux valeurs 2000 et 4000.

.. activecode:: dictionnaire

    compteur = {5: 2000, 1: 4000}
    print(5 in compteur)
    print(3 in compteur)
    compteur[3] = 5000
    print(3 in compteur)
    print("Le compteur contient", compteur[3], "pour la cle", 3)
    for cle in compteur:
        print("Pour la cle", cle, "le compteur contient", compteur[cle])
    compteur[3] += 200000
    print("J'augmente la cle 3 de 200000 (gros bonus)")
    for cle in compteur:
        print("Pour la cle", cle, "le compteur contient", compteur[cle])

Langue française
::::::::::::::::

Pour charger le `dictionnaire de la langue française <../_static/dico.txt>`_ (336 531 mots), faites ceci :

.. code-block:: python

    dico = open('dico.txt').read().splitlines()

Quelques pistes
---------------

- Combien de mots de la langue française commencent par « c » ?
- Combien de mots font 17 lettres ?
- Combien de mots finissent par « k » ?

IMDb
::::

Pour charger le `top 250 IMDb <../_static/top250.json>`_ (Internet Movie Database), faites ceci :

.. code-block:: python

    import json
    top = json.load(open('top250.json'))

Quelques pistes
---------------

- Afficher le top 10 d'IMDb, sous la forme suivante : ::
 
    1 Les évadés
    2 ...
    ...
    10 ...

- Quel est le classement du film Lego ? Utiliser ``if "Lego" in top[i]["title"]``
- Quels sont les films sortis en 1994 ?
- Quels sont les acteurs de Inception ?
- Quels sont les films de Christopher Nolan ?
- Quels sont les films avec Natalie Portman ?
- Quelles sont les dix années où sont sortis le plus de films dans le top 250 ?
- Quelles sont les dix réalisateurs les plus présents dans le top 250 ?
- Quels sont les dix acteurs les plus présents dans le top 250 ?
- Quels sont les couplages réalisateur-acteur les plus fréquents dans le top 250 ?
