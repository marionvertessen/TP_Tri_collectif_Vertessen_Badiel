import random
import numpy as np

global d
class Environnement:
    taille = 50
    env = np.zeros((taille,taille))

    def deplace(self, actual, listeAgent, a, choix, up, up_right, right, down_right, down, down_left, left, up_left):
        print("Je suis l'agent "+str(listeAgent[choix].id))
        deplacement = listeAgent[choix].perception_action(actual, up, up_right, right, down_right, down, down_left, left, up_left)
        if deplacement == 0:
            listeAgent[choix].posx = listeAgent[choix].posx - a
        elif deplacement == 1:
            listeAgent[choix].posx = listeAgent[choix].posx - a
            listeAgent[choix].posy = listeAgent[choix].posy + a
        elif deplacement == 2:
            listeAgent[choix].posy = listeAgent[choix].posy + a
        elif deplacement == 3:
            listeAgent[choix].posx = listeAgent[choix].posx + a
            listeAgent[choix].posy = listeAgent[choix].posy + a
        elif deplacement == 4:
            listeAgent[choix].posx = listeAgent[choix].posx + a
        elif deplacement == 5:
            listeAgent[choix].posx = listeAgent[choix].posx + a
            listeAgent[choix].posy = listeAgent[choix].posy - a
        elif deplacement == 6:
            listeAgent[choix].posy = listeAgent[choix].posy - a
        elif deplacement == 7:
            listeAgent[choix].posx = listeAgent[choix].posx - a
            listeAgent[choix].posy = listeAgent[choix].posy - a
        depot = random.uniform(0,1)
        prise = random.uniform(0,1)
        if prise < listeAgent[choix].pprise:
            listeAgent[choix].tenir = actual
            listeAgent[choix].d = 1
        if depot < listeAgent[choix].pdepot:
            listeAgent[choix].tenir = 0
            listeAgent[choix].d = 2
        for i in range(len(listeAgent[choix].memoire)):
            print("La valeur de la mémoire est " + str(listeAgent[choix].memoire[i]))
        print("#######################Mon tenir est " + str(listeAgent[choix].tenir))
        return listeAgent, listeAgent[choix].posx, listeAgent[choix].posy, listeAgent[choix].d

