from environnement import Environnement
from random import randint

class Agent:
    def __init__(self, id, posx, posy,):
        self.id = id
        self.posx = posx
        self.posy = posy
        self.tenir = 0

    def perception_action(self, i):
        env = Environnement()
        ##Si l'agent est sur la première ligne
        if self.posx == 0:
            n = randint(0, 2)
            #Si l'agent est sur la première colonne (0;0)
            if self.posy == 0:
                if n == 0: # Il se déplace à droite
                    return 2
                elif n == 1: # Il se déplace en bas
                    return 4
                else: # Il se déplace en bas et à droite
                    return 3
            #Si l'agent est à la dernière colonne (0;49)
            elif self.posy == env.taille - 1:
                if n == 0: #Il se déplace à gauche
                    return 6
                elif n == 1: #Il se déplace en bas
                    return 4
                else: #Il se déplace en bas et à gauche
                    return 5
            else:
                o = randint(0, 4)
                if o == 0:
                    #Il se déplace à gauche
                    return 6
                elif 0 == 1:
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

        ##Si l'agent est sur la dernière ligne
        elif self.posx == env.taille - 1:
            n = randint(0, 2)
            # Si l'agent est sur la première colonne (49;0)
            if self.posy == 0:
                if n == 0: # Déplacement vers la droite
                    return 2
                elif n == 1: # Déplacement à droite et en haut
                    return 1
                elif n == 2: #Déplacement vers le haut
                    return 0
            # Si l'agent est à la dernière colonne (49;49)
            elif self.posy == env.taille - 1:
                if n == 0: # Déplacement vers la gauche
                    return 6
                elif n == 1: # Déplacement à gauche et en haut
                    return 7
                elif n == 2: #Déplacement vers le haut
                    return 0
            else:
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

        ##Au bord gauche
        elif self.posy == 0:
            o = randint(0, 4)
            if o == 0:
                # Il se déplace en haut
                return 0
            elif 0 == 1:
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

        ##Au bord droit
        elif self.posy == env.taille - 1:
            o = randint(0, 4)
            if o == 0:
                # Il se déplace en bas
                return 4
            elif 0 == 1:
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
        ##Dans les 8 cas
        else:
            o = randint(0, 7)
            if o == 0:
                # Il se déplace en haut
                return 0
            elif 0 == 1:
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