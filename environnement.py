import numpy as np
from random import *

class Environnement:
    taille = 50
    env = np.zeros((taille,taille))

    def deplace(self, listeAgent, a):
        choix = randint(0, 19)
        print("Je suis l'agent "+str(listeAgent[choix].id))
        deplacement = listeAgent[choix].perception_action(a)
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
            listeAgent[choix].posy = listeAgent[choix].posy - a
            listeAgent[choix].posy = listeAgent[choix].posy - a
        return listeAgent

