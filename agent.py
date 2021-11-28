from random import randint

def update_memoire(actual, memoire):
    if len(memoire) > 10:
        del memoire[0]
    if actual != 0.9 or actual != 0.8 or actual != 0.7:
        memoire.append(actual)
    return memoire



def prop_Agents (liste, objet):
    f = 0
    f_c = 0
    if objet == 1:
        for i in range (len(liste)):
            if liste[i] == objet:
                f = f + 1
            if liste[i] == 2:
                f_c = f_c + 1
            if liste[i] == 3:
                f_c = f_c + 1
    elif objet == 2:
        for i in range(len(liste)):
            if liste[i] == objet:
                f = f + 1
            if liste[i] == 1:
                f_c = f_c + 1
            if liste[i] == 3:
                f_c = f_c + 1
    elif objet == 3:
        for i in range(len(liste)):
            if liste[i] == objet:
                f = f + 1
            if liste[i] == 1:
                f_c = f_c + 1
            if liste[i] == 2:
                f_c = f_c + 1
    f = (f + f_c*0.1) / len(liste)
    return f

class Agent:
    def __init__(self, id):
        self.id = id
        self.tenir = 0
        self.memoire = []
        self.pprise = -1
        self.pdepot = -1
        self.change = 0 #Pris ou déposé
        self.pas = 1
        self.signal = -1

    def prob(self, actual, memoire, tenir):
        pprise = -1
        pdepot = -1

        if actual == 1:
            if tenir == 0:
                f1 = prop_Agents(memoire, 1)
                pprise = (0.1 / (0.1 + f1)) ** 2
                return pprise
            else:
                return pprise
        elif actual == 2:
            if tenir == 0:
                f2 = prop_Agents(memoire, 2)
                pprise = (0.1 / (0.1 + f2)) ** 2
                return pprise
            else:
                return pprise
        elif actual == 3:
            if tenir == 0:
                signal = 2
            else:
                return pprise
        else:
            if tenir == 0:
                return pdepot
            elif tenir == 1:
                f1 = prop_Agents(memoire, 1)
                pdepot = (f1 / (0.3 + f1)) ** 2
                return pdepot
            elif tenir == 2:
                f2 = prop_Agents(memoire, 2)
                pdepot = (f2 / (0.3 + f2)) ** 2
                return pdepot
            elif tenir == 3:
                f3 = prop_Agents(memoire, 3)
                pdepot = (f3 / (0.3 + f3)) ** 2
                return pdepot
            else:
                return pdepot

    def perception_action(self, actual, pos, taille_grille):
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
            elif pos[1] == taille_grille - 1:
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
                o = randint(2, 6)
                return o

        elif pos[0] == taille_grille - 1: #Si l'agent est sur la dernière ligne
            if pos[1] == 0: #Si l'agent est sur la première colonne (49;0)
                o = randint(0, 2)
                self.memoire = update_memoire(actual, self.memoire)
                if self.tenir == 0:
                    self.pprise = self.prob(actual, self.memoire, self.tenir)
                else:
                    self.pdepot = self.prob(actual, self.memoire, self.tenir)
                return o
            elif pos[1] == taille_grille - 1: #Si l'agent est à la dernière colonne (49;49)
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
                if o == 3:
                    return 6
                elif o == 4:
                    return 7
                else:
                    return o

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
        elif pos[1] == taille_grille - 1:
            self.memoire = update_memoire(actual, self.memoire)
            if self.tenir == 0:
                self.pprise = self.prob(actual, self.memoire, self.tenir)
            else:
                self.pdepot = self.prob(actual, self.memoire, self.tenir)
            o = randint(4, 8)
            if o == 8:
                # Il se déplace en bas
                return 0
            else:
                return o
        #Dans les 8 cas
        else:
            self.memoire = update_memoire(actual, self.memoire)
            if self.tenir == 0:
                self.pprise = self.prob(actual, self.memoire, self.tenir)
            else:
                self.pdepot = self.prob(actual, self.memoire, self.tenir)
            o = randint(0, 7)
            return o
