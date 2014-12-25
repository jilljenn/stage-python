
================================
Mardi matin - Jeu des allumettes
================================

Règles du jeu
:::::::::::::

Le jeu des allumettes se joue à deux joueurs : à tour de rôle, chacun doit retirer un certain nombre d'allumettes (par exemple, entre 1 et 3). Celui qui prend la dernière a perdu.

Votre mission
:::::::::::::

Vous allez créer un programme qui joue à ce jeu (appelé *champion*), sous la forme d'une fonction qui prend en argument le nombre d'allumettes actuellement dans la partie (``nb_allumettes``) et renvoie le nombre d'allumettes à retirer.

Par exemple, voici une fonction correspondant à un champion qui prend toujours une seule allumette : ::

    def ia(nb_allumettes):
        return 1

Enregistrez votre fonction sous le nom ``nom.py`` (où « nom » est le nom que vous donnez à votre champion). Pour envoyer votre champion dans l'arène, ajoutez-le dans le dossier ``interfaces/interface_allumettes`` dans Réseau → Helios.

Lancer des matches
::::::::::::::::::

Ouvrez PuTTY et connectez-vous à ``jj@helios``, mot de passe « stage ». Vous pourrez ensuite lancer des matches.

La commande suivante permet de démarrer une partie de 15 allumettes entre les champions ``joueur1`` et ``joueur2`` : ::

    python allumettes.py 15 joueur1 joueur2

Si vous voulez affronter manuellement un champion, tapez : ::

    python allumettes.py 15 input joueur2

Pour aller plus loin
::::::::::::::::::::

Que se passe-t-il si le nombre d'allumettes que chaque joueur peut retirer :

- est compris entre 1 et ``max_allumettes`` ?
- est compris entre ``min_allumettes`` et ``max_allumettes`` ?

Liste des champions
:::::::::::::::::::

La liste des champions est `ici <_static/interfaces/interface_allumettes>`_.
