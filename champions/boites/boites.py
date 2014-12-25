#!/usr/bin/python3
import sys, importlib, random

VAL_MIN = 1
VAL_MAX = 100

NB_BOXES = 10

def usage():
    print("Usage: ./boites ia1 ia2")
    exit(1)

def parse_args(ac, av):
    if (ac != 3):
        usage()
    ia1 = importlib.import_module(av[1])
    ia2 = importlib.import_module(av[2])
    return (ia1, ia2)

def gen_list():
    lst = [random.randint(VAL_MIN, VAL_MAX) for box in range(NB_BOXES)]
    if (sum(lst) % 2 == 0):
        lst[random.randint(0, NB_BOXES - 1)] += 1
    return lst

def one_turn(boxes_list, ia_player, score, turn):
    print("liste des valeurs des boites à ce tour : ")
    print(" ".join(map(str, boxes_list)))
    answer = ia_player.ia(boxes_list)
    if (answer not in 'GD' or len(answer) != 1):
        print("Le joueur %d a répondu '%s', ce qui est contraire au règles." % ((turn % 2 + 1), answer))
        print("Il a donc perdu")
        exit(1)
    if (answer == 'G'):
        value = boxes_list.pop(0)
        complete_answer = "gauche"
    else:
        value = boxes_list.pop()
        complete_answer = "droite"
    print("Le joueur %d a pris la boite de %s (%d€)" % ((turn % 2 + 1), complete_answer, value))
    score[turn % 2] += value
    print("%d (J1) - (J2) %d" % (score[0], score[1]))


def main(ac, av):
    ia_list = parse_args(ac, av)
    turn = 0
    ia_player = ia_list[0]
    score = [0, 0]
    boxes_list = gen_list()
    while (len(boxes_list) > 0):
        one_turn(boxes_list, ia_player, score, turn)
        turn += 1
        ia_player = ia_list[turn % 2]
    if (score[0] > score[1]):
        print("Le joueur 1 a gagné !!")
    else:
        print("Le joueur 2 a gagné !!")
        
    print("%d (J1) - (J2) %d" % (score[0], score[1]))

if (__name__ == "__main__"):
    main(len(sys.argv), sys.argv)
