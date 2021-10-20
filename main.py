from random import randint
import numpy as np
import sys
from agent import Agent
from environnement import Environnement

##Creation environnement
def alea():
    x = randint(0, env.taille - 1)
    return x


def compte(nb, env):
    compt = 0
    for i in range(env.taille):
        for j in range(env.taille):
            if env.env[i][j] == nb:
                compt = compt + 1
    return compt

def affichageAgent (liste):
    for i in range (len(liste)):
        print("L'id est "+ str(liste[i].id) +" ("+ str(liste[i].posx)+","+str(liste[i].posy)+")")


env = Environnement()
array = env.env
np.set_printoptions(threshold=sys.maxsize)

##Creation Objet A
for i in range(200):
    vide = False
    x = alea()
    y = alea()
    while vide == False:
        x = alea()
        y = alea()
        if array[x][y] == 0:
            vide = True
    array[x][y] = 1

##Creation Objet B
for i in range(200):
    vide = False
    x = alea()
    y = alea()
    while vide == False:
        x = alea()
        y = alea()
        if array[x][y] == 0:
            vide = True
    array[x][y] = 2

print(array)
print(compte(1, env))
print(compte(2, env))

#Creation agent
listeAgent=[]
for i in range(20):
    x = alea()
    y = alea()
    agent = Agent(i, x, y)
    listeAgent.append(agent)

print(listeAgent)
affichageAgent(listeAgent)

#Déplacement de l'agent
a = 1
for i in range (4):
    listeAgent = env.deplace(listeAgent, a)
    affichageAgent(listeAgent)


# importations à faire pour la réalisation d'une interface graphique
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Première étape : création d'une application Qt avec QApplication
#    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
#    on vérifie s'il existe déjà une instance de QApplication
app = QApplication.instance()
if not app: # sinon on crée une instance de QApplication
    app = QApplication(sys.argv)

# création d'une fenêtre avec QWidget dont on place la référence dans fen
fen = QWidget()

# la fenêtre est rendue visible
fen.show()

# exécution de l'application, l'exécution permet de gérer les événements
app.exec_()

