from environnement import Environnement
from random import randint

def pos(up, up_right, right, down_right, down, down_left, left, up_left):
    memoire = []
    if up == 1:
        memoire.append(1)
    elif up == 2:
        memoire.append(2)
    else:
        memoire.append(0)

    if up_right == 1:
        memoire.append(1)
    elif up_right == 2:
        memoire.append(2)
    else:
        memoire.append(0)

    if right == 1:
        memoire.append(1)
    elif right == 2:
        memoire.append(2)
    else:
        memoire.append(0)

    if down_right == 1:
        memoire.append(1)
    elif down_right == 2:
        memoire.append(2)
    else:
        memoire.append(0)

    if down == 1:
        memoire.append(1)
    elif down == 2:
        memoire.append(2)
    else:
        memoire.append(0)

    if down_left == 1:
        memoire.append(1)
    elif down_left == 2:
        memoire.append(2)
    else:
        memoire.append(0)

    if left == 1:
        memoire.append(1)
    elif left == 2:
        memoire.append(2)
    else:
        memoire.append(0)

    if up_left == 1:
        memoire.append(1)
    elif up_left == 2:
        memoire.append(2)
    else:
        memoire.append(0)

    return memoire

def prob(actual, memoire, tenir):
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
            pdepot = (f1/(0.3+f1)) ** 2
            return pdepot
        else:
            f2 = nb_Agents(memoire, 2)
            pdepot = (f2/(0.3+f2)) ** 2
            return pdepot

def nb_Agents (liste, agent):
    compt = 0
    for i in range (len(liste)):
        if liste[i] == agent:
            compt = compt + 1
        return compt

class Agent:
    def __init__(self, id, posx, posy):
        self.id = id
        self.posx = posx
        self.posy = posy
        self.tenir = 0
        self.memoire = [10]
        self.pprise = -1
        self.pdepot = -1
        self.d = 0

    def perception_action(self, actual, up, up_right, right, down_right, down, down_left, left, up_left):
        env = Environnement()
        #Si l'agent est sur la première ligne
        if self.posx == 0:
            n = randint(0, 2)
            #Si l'agent est sur la première colonne (0;0)
            if self.posy == 0:
                self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
                if self.tenir == 0:
                    self.pprise = prob(actual, self.memoire)
                else:
                    self.pdepot = prob(actual, self.memoire)
                if n == 0: # Il se déplace à droite
                    return 2
                elif n == 1: # Il se déplace en bas
                    return 4
                else: # Il se déplace en bas et à droite
                    return 3
            #Si l'agent est à la dernière colonne (0;49)
            elif self.posy == env.taille - 1:
                self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
                self.pprise = prob(actual, self.memoire, self.tenir)
                if n == 0: #Il se déplace à gauche
                    return 6
                elif n == 1: #Il se déplace en bas
                    return 4
                else: #Il se déplace en bas et à gauche
                    return 5
            #Sur le bord haut
            else:
                self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
                self.pprise = prob(actual, self.memoire, self.tenir)
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

        #Si l'agent est sur la dernière ligne
        elif self.posx == env.taille - 1:
            n = randint(0, 2)
            # Si l'agent est sur la première colonne (49;0)
            if self.posy == 0:
                self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
                self.pprise = prob(actual, self.memoire, self.tenir)
                if n == 0: # Déplacement vers la droite
                    return 2
                elif n == 1: # Déplacement à droite et en haut
                    return 1
                elif n == 2: #Déplacement vers le haut
                    return 0
            #Si l'agent est à la dernière colonne (49;49)
            elif self.posy == env.taille - 1:
                self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
                self.pprise = prob(actual, self.memoire, self.tenir)
                if n == 0: # Déplacement vers la gauche
                    return 6
                elif n == 1: # Déplacement à gauche et en haut
                    return 7
                elif n == 2: #Déplacement vers le haut
                    return 0
            #Sur le bord bas
            else:
                self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
                self.pprise = prob(actual, self.memoire, self.tenir)
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
        elif self.posy == 0:
            self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
            self.pprise = prob(actual, self.memoire, self.tenir)
            o = randint(0, 4)
            if o == 0:
                # Il se déplace en haut
                return 0
            elif o == 1:
                # Il se déplace à droite et en haut
                return 1
            elif o == 2:
                # Il se déplace à droite
                return 2
            elif o == 3:
                # Il se déplace en bas et à droite
                return 3
            else:
                # Il se déplace en bas
                return 4

        #Au bord droit
        elif self.posy == env.taille - 1:
            self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
            self.pprise = prob(actual, self.memoire, self.tenir)
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
            self.memoire = pos(up, up_right, right, down_right, down, down_left, left, up_left)
            self.pprise = prob(actual, self.memoire, self.tenir)
            o = randint(0, 7)
            if o == 0:
                # Il se déplace en haut
                return 0
            elif o == 1:
                # Il se déplace en haut et à droite
                return 1
            elif o == 2:
                # Il se déplace à droite
                return 2
            elif o == 3:
                # Il se déplace à droite et en bas
                return 3
            elif o == 4:
                # Il se déplace en bas
                return 4
            elif o == 5:
                # Il se déplace en bas et à gauche
                return 5
            elif o == 6:
                # Il se déplace à gauche
                return 6
            elif o == 5:
                # Il se déplace en haut et à gauche
                return 7
