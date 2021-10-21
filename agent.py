from environnement import Environnement
from random import randint

def update_memoire(actual, memoire):
    if len(memoire) > 10:
        del memoire[0]
    memoire.append(actual)
    return memoire



def nb_Agents (liste, agent):
    compt = 0
    for i in range (len(liste)):
        if liste[i] == agent:
            compt = compt + 1
        return compt

class Agent:
    def __init__(self, id):
        self.id = id
        self.tenir = 0
        self.memoire = []
        self.pprise = -1
        self.pdepot = -1
        self.change = 0 #Pris ou déposé

    def prob(self, actual, memoire, tenir):
        pprise = -1
        pdepot = -1
        if actual == 1:
            if tenir == 0:
                f1 = nb_Agents(memoire, 1)
                pprise = (0.1 / (0.1 + f1)) ** 2
                return pprise
            else:
                return pprise
        elif actual == 2:
            if tenir == 0:
                f2 = nb_Agents(memoire, 2)
                pprise = (0.1 / (0.1 + f2)) ** 2
                return pprise
            else:
                return pprise
        else:
            if tenir == 0:
                return pdepot
            elif tenir == 1:
                f1 = nb_Agents(memoire, 1)
                pdepot = (f1 / (0.3 + f1)) ** 2
                return pdepot
            else:
                f2 = nb_Agents(memoire, 2)
                pdepot = (f2 / (0.3 + f2)) ** 2
                return pdepot

    def perception_action(self, actual, pos):
        env = Environnement()
        #Si l'agent est sur la première ligne
        if pos[0] == 0:
            #Si l'agent est sur la première colonne (0;0)
            if pos[1] == 0:
                o = randint(2, 4)
                self.memoire = update_memoire(actual, self.memoire)
                if self.tenir == 0:
                    self.pprise = self.prob(actual, self.memoire, self.tenir)
                else:
                    self.pdepot = self.prob(actual, self.memoire, self.tenir)
                return o
            #Si l'agent est à la dernière colonne (0;49)
            elif pos[1] == env.taille - 1:
                o = randint(4, 6)
                self.memoire = update_memoire(actual, self.memoire)
                if self.tenir == 0:
                    self.pprise = self.prob(actual, self.memoire, self.tenir)
                else:
                    self.pdepot = self.prob(actual, self.memoire, self.tenir)
                return o
            #Sur le bord haut
            else:
                self.memoire = update_memoire(actual, self.memoire)
                if self.tenir == 0:
                    self.pprise = self.prob(actual, self.memoire, self.tenir)
                else:
                    self.pdepot = self.prob(actual, self.memoire, self.tenir)
                o = randint(0, 4)
                if o == 0:
                    #Il se déplace à gauche
                    return 6
                elif o == 1:
                    # Il se déplace à gauche et en bas
                    return 5
                elif o == 2:
                    #Il se déplace en bas
                    return 4
                elif o == 3:
                    #Il se déplace à droite et en bas
                    return 3
                else:
                    #Il se déplace à droite
                    return 2

        elif pos[0] == env.taille - 1: #Si l'agent est sur la dernière ligne
            if pos[1] == 0: #Si l'agent est sur la première colonne (49;0)
                o = randint(0, 2)
                self.memoire = update_memoire(actual, self.memoire)
                if self.tenir == 0:
                    self.pprise = self.prob(actual, self.memoire, self.tenir)
                else:
                    self.pdepot = self.prob(actual, self.memoire, self.tenir)
                return o
            elif pos[1] == env.taille - 1: #Si l'agent est à la dernière colonne (49;49)
                n = randint(0, 2)
                self.memoire = update_memoire(actual, self.memoire)
                if self.tenir == 0:
                    self.pprise = self.prob(actual, self.memoire, self.tenir)
                else:
                    self.pdepot = self.prob(actual, self.memoire, self.tenir)
                if n == 0: #Déplacement vers la gauche
                    return 6
                elif n == 1: #Déplacement à gauche et en haut
                    return 7
                elif n == 2: #Déplacement vers le haut
                    return 0
            else: #Sur le bord bas
                self.memoire = update_memoire(actual, self.memoire)
                if self.tenir == 0:
                    self.pprise = self.prob(actual, self.memoire, self.tenir)
                else:
                    self.pdepot = self.prob(actual, self.memoire, self.tenir)
                o = randint(0, 4)
                if o == 0:
                    # Il se déplace à gauche
                    return 6
                elif 0 == 1:
                    # Il se déplace à gauche et en haut
                    return 7
                elif o == 2:
                    # Il se déplace en haut
                    return 0
                elif o == 3:
                    # Il se déplace à droite et en haut
                    return 1
                else:
                    # Il se déplace à droite
                    return 2

        #Au bord gauche
        elif pos[1] == 0:
            self.memoire = update_memoire(actual, self.memoire)
            if self.tenir == 0:
                self.pprise = self.prob(actual, self.memoire, self.tenir)
            else:
                self.pdepot = self.prob(actual, self.memoire, self.tenir)
            o = randint(0, 4)
            return o

        #Au bord droit
        elif pos[1] == env.taille - 1:
            self.memoire = update_memoire(actual, self.memoire)
            if self.tenir == 0:
                self.pprise = self.prob(actual, self.memoire, self.tenir)
            else:
                self.pdepot = self.prob(actual, self.memoire, self.tenir)
            o = randint(0, 4)
            if o == 0:
                # Il se déplace en bas
                return 4
            elif o == 1:
                # Il se déplace à gauche et en bas
                return 5
            elif o == 2:
                # Il se déplace à gauche
                return 6
            elif o == 3:
                # Il se déplace à gauche et en haut
                return 7
            else:
                # Il se déplace en haut
                return 0
        #Dans les 8 cas
        else:
            self.memoire = update_memoire(actual, self.memoire)
            if self.tenir == 0:
                self.pprise = self.prob(actual, self.memoire, self.tenir)
            else:
                self.pdepot = self.prob(actual, self.memoire, self.tenir)
            o = randint(0, 7)
            return o
