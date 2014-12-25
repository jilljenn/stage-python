taille = 0

def inverse(chemin):
    chemin_inverse = ""
    for i in range (len(chemin)):
        if chemin[i] == "g":
            chemin_inverse += "d"
        elif chemin[i] == "d":
            chemin_inverse += "g"
    return chemin_inverse[::-1]

def suivant(chemin):
    chemin_suivant = ""
    chemin_suivant = chemin + "d" + inverse(chemin)
    return chemin_suivant

def dragon(numero):
    global taille
    taille = 75 // numero
    chemin = ""
    for i in range(numero):
        chemin = suivant(chemin)
    return chemin

import turtle
tortue = turtle.Turtle()
tortue.speed(0)

def debut():
    gauche()

def gauche():
    tortue.left(90)
    tortue.forward(taille)
    
def droite():
    tortue.right(90)
    tortue.forward(taille)

def dessin(chemin):
    debut()
    for direction in chemin:
        if direction == "d":
            droite()
        else:
            gauche()

dessin(dragon(10))
input()