#!/usr/bin/python3
import sys, importlib

NB_MIN = 1
NB_MAX = 3

def usage():
    print("Usage: ./allumettes.py nb_allumettes IA1 IA2", file=sys.stderr)
    exit(1)

def atoi(string):
    try:
        return (int(string))
    except ValueError:
        usage()

def parse_args(ac, av):
    if (ac != 4):
        usage()
    nb_allumettes = atoi(av[1])
    ia1 = importlib.__import__(av[2])
    ia2 = importlib.__import__(av[3])
    return (nb_allumettes, [ia1, ia2])

def one_turn(nb_allumettes, num_player, ia_player):
    nb_to_take = ia_player.ia(nb_allumettes)
    if not (NB_MIN <= nb_to_take <= NB_MAX):
        print("Le joueur %d a renvoyé %d, ce qui est contraire aux règles." % (num_player, nb_to_take))
        print("Il a donc perdu.")
        exit(0)
    return (nb_to_take)


def main(ac, av):
    nb_allumettes, ia_list = parse_args(ac, av)
    num_player = 1
    ia_player = ia_list[0]
    turn = 0
    while (nb_allumettes > 0):
        print("|" * nb_allumettes)
        nb_to_take = one_turn(nb_allumettes, num_player, ia_player)
        nb_allumettes -= nb_to_take
        print("tour %d: le joueur %d a pris %d allumettes, il en reste %d" % (turn + 1, num_player, nb_to_take, nb_allumettes))
        turn += 1
        num_player = turn % 2 + 1
        ia_player = ia_list[turn % 2]
    print("Le vainqueur est le joueur %d" % num_player)
    exit(0)

if (__name__ == '__main__'):
    main(len(sys.argv), sys.argv)
