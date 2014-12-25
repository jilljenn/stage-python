
=================================
Mardi après-midi - Jeu des boîtes
=================================

Le jeu des boîtes est tiré de l'article de Jean-Paul Delahaye dans `le numéro de 1024 d'octobre 2014 <../_static/jeu.pdf>`_.

Règles du jeu
:::::::::::::

Vous avez 20 boîtes devant vous, chacune contient une certaine somme d'argent. Vous connaissez le contenu de toutes les boîtes. À tour de rôle, chaque joueur peut prendre soit la boîte le plus à gauche, soit celle le plus à droite. Celui qui obtient le plus d'argent gagne la partie (on garantit que la somme totale est impaire, il n'y a donc jamais égalité entre les montants récoltés par les deux joueurs).

Votre mission
:::::::::::::

Vous allez créer un programme qui joue à ce jeu (appelé *champion*), sous la forme d'une fonction qui prend en argument une liste représentant le contenu des boîtes actuellement dans la partie (``boites``) et renvoie ``"G"`` si votre champion souhaite choisir la boîte de gauche, ``"D"`` sinon.

Par exemple, voici une fonction correspondant à un champion qui prend toujours la boîte de droite : ::

    def ia(boites):
        return "D"

Enregistrez votre fonction sous le nom ``nom.py`` (où « nom » est le nom que vous donnez à votre champion). Pour envoyer votre champion dans l'arène, ajoutez-le dans le dossier ``interfaces/interface_boites`` dans Réseau → Helios.

Lancer des matches
::::::::::::::::::

Ouvrez PuTTY et connectez-vous à ``jj@helios``, mot de passe « stage ». Vous pourrez ensuite lancer des matches.

La commande suivante permet de démarrer une partie entre les champions ``joueur1`` et ``joueur2`` : ::

    python boites.py joueur1 joueur2

Essayez de battre ``jj`` en tapant : ::

    python boites.py input jj

Liste des champions
:::::::::::::::::::

La liste des champions est `ici <_static/interfaces/interface_boites>`_.
