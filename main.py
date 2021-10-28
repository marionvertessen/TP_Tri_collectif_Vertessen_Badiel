from random import randint
import numpy as np
import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow
from environnement import Environnement

##Compte du nombre d'agents
def compte(nb, env):
    compt = 0
    for i in range(env.taille):
        for j in range(env.taille):
            if env.env[i][j] == nb:
                compt = compt + 1
    return compt

##Liste des Agents
def affichageAgent (liste_Agent, liste_Pos_Agent):
    for i in range (len(liste_Pos_Agent)):
        print("L'id est "+ str(liste_Agent[i].id) +" ("+ str(liste_Pos_Agent[i][0])+","+str(liste_Pos_Agent[i][1])+")")


env = Environnement()
np.set_printoptions(threshold=sys.maxsize)

env.init_env()
env.deplace(20000000)


