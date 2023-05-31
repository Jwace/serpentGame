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
    compt = 0
    ligne = []
    ligne2 = []
    for i in range(len(plateau) - 1, -1, -1):
        
        if compt % 10 == 0 and compt !=0:
            
            if compt == 20 or compt == 40:
                ligne.reverse()
                print(ligne)
            else:
                print(ligne)
            ligne =[]
            ligne2 = []
        #print (i)
        plateau2 = plateau
        if joueur1 == joueur2:
            plateau2[joueur1] = 3
        else:
            plateau2[joueur1] = 1
            plateau2[joueur2] = 2
        ligne.append(plateau2[i])
        plateau2[joueur1] = 0
        plateau2[joueur2] = 0

        
        compt += 1

        if compt == 50:
            
            print(ligne)
            ligne =[]
            ligne2 = []


affichePlateau()  

while plateau[49] == 0:

  

    print("Joueur 1 : Appuyer sur entrée pour lancer le dé")
    wait()
    num_de = randint(1, 6)
    print(num_de)
    joueur1 += num_de

    affichePlateau()


    print("Joueur 2 : Appuyer sur entrée pour lancer le dé")
    wait()
    num_de = randint(1, 6)
    print(num_de)
    joueur2 += num_de

    affichePlateau()
    
