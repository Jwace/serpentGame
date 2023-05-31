from random import *
import msvcrt as m

plateau = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

case_bonus = [12,18,27,46]

case_malus = [3,8,14,22,43]

joueur1 = 0
joueur2 = 0


def wait():
    m.getch()

def affichePlateau():
    for i in range(len(plateau)):
        print (i)

while plateau[49] == 0:

    affichePlateau()

    print("Joueur 1 : Appuyer sur entrée pour lancer le dé")
    wait()
    num_de = randint(1, 6)
    print(num_de)
    joueur1 += num_de


    print("Joueur 2 : Appuyer sur entrée pour lancer le dé")
    wait()
    num_de = randint(1, 6)
    print(num_de)
    joueur2 += num_de



