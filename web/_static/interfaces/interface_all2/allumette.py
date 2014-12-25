#!/usr/bin/python3
import sys, importlib

def usage():
    print("Usage: ./allumettes.py IA1 IA2 nb_allumettes min max", file=sys.stderr)
    exit(1)

def atoi(string):
    try:
        return (int(string))
    except ValueError:
        usage()

def parse_args(ac, av):
    if (ac != 6):
        usage()
    ia1 = importlib.__import__(av[1])
    ia2 = importlib.__import__(av[2])
    nb_allumettes = atoi(av[3])
    min_all = atoi(av[4])
    max_all = atoi(av[5])
    return (nb_allumettes, min_all, max_all, [ia1, ia2])

def one_turn(nb_allumettes, min_all, max_all, num_player, ia_player):
    nb_to_take = ia_player.ia(nb_allumettes, min_all, max_all)
    if not (min_all <= nb_to_take <= max_all):
        print("Le joueur %d a renvoyé %d, ce qui est contraire aux règles." % (num_player, nb_to_take))
        print("Il a donc perdu.")
        exit(0)
    return (nb_to_take)


def main(ac, av):
    nb_allumettes, min_all, max_all, ia_list = parse_args(ac, av)
    num_player = 1
    ia_player = ia_list[0]
    turn = 0
    while (nb_allumettes > 0):
        print("|" * nb_allumettes)
        nb_to_take = one_turn(nb_allumettes, min_all, max_all, num_player, ia_player)
        nb_allumettes -= nb_to_take
        print("tour %d: le joueur %d a pris %d allumettes, il en reste %d" % (turn + 1, num_player, nb_to_take, nb_allumettes))
        turn += 1
        num_player = turn % 2 + 1
        ia_player = ia_list[turn % 2]
    print("Le vainqueur est le joueur %d" % num_player)
    exit(0)

if (__name__ == '__main__'):
    main(len(sys.argv), sys.argv)
