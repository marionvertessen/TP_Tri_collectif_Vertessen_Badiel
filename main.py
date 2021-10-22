from random import randint
import numpy as np
import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow
from agent import Agent
from environnement import Environnement

##Creation environnement
def alea():
    x = randint(0, env.taille - 1)
    return x

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
#print(compte(1, env))
#print(compte(2, env))

#Creation agent
listeAgent=[]
listePosAgent=[]
for i in range(20):
    x = alea()
    y = alea()
    agent = Agent(i)
    listeAgent.append(agent)
    listePosAgent.append([x,y])

#Afficher la liste des agents
affichageAgent(listeAgent, listePosAgent)

app = QApplication.instance()
if not app: # sinon on crée une instance de QApplication
    app = QApplication(sys.argv)

# création d'une fenêtre avec QWidget dont on place la référence dans fen
fen = MainWindow(env)

# la fenêtre est rendue visible
fen.show()

# exécution de l'application, l'exécution permet de gérer les événements
app.exec_()
#Déplacement de l'agent
pas = 1
cmpt = 0
while cmpt<800000:
    choix = randint(0, 19)
    i = listePosAgent[choix][0]
    j = listePosAgent[choix][1]
    listePosAgent, agent = env.deplace(array[i][j], listeAgent[choix], listePosAgent, choix, pas)
    if agent.change == 1:
        #print("Je change en 0")
        array[i][j] = 0
        agent.change = 0
    elif agent.change == 2:
        array[listePosAgent[choix][0]][listePosAgent[choix][1]] = agent.tenir
        agent.tenir = 0
        agent.change = 0
    #print(array)
    #affichageAgent(listeAgent, listePosAgent)
    print(cmpt)
    cmpt+=1

app2 = QApplication.instance()
if not app2: # sinon on crée une instance de QApplication
    app2 = QApplication(sys.argv)

# création d'une fenêtre avec QWidget dont on place la référence dans fen
fen2 = MainWindow(env)

# la fenêtre est rendue visible
fen2.show()

# exécution de l'application, l'exécution permet de gérer les événements
app2.exec_()