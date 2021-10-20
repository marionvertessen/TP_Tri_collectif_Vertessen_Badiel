from random import randint
import numpy as np
import sys
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
print("Je suis un objet 1 à la position "+ str(array[0][3]))
print(compte(1, env))
print(compte(2, env))

#Creation agent
listeAgent=[]
for i in range(20):
    x = alea()
    y = alea()
    agent = Agent(i, x, y)
    listeAgent.append(agent)

#Afficher la liste des agents
affichageAgent(listeAgent)

#Déplacement de l'agent
a = 1
m = 0
n = 0
for b in range (20):
            choix = randint(0, 19)
            i = listeAgent[choix].posx
            j = listeAgent[choix].posy
            upx = i - a
            upy = j
            up_rightx = i - a
            up_righty = j + a
            rightx = i
            righty = j + a
            down_rightx = i + a
            down_righty = j + a
            downx = i + a
            downy = j
            down_leftx = i + a
            down_lefty = j - a
            leftx = i
            lefty = j - a
            up_leftx = i - a
            up_lefty = j - a
            listeAgent, m, n, d= env.deplace(env.env[i][j], listeAgent, a, choix, env.env[upx][upy], env.env[up_rightx][up_righty], env.env[rightx][righty], env.env[down_rightx][down_righty], env.env[downx][downy], env.env[down_leftx][down_lefty], env.env[leftx][lefty], env.env[up_leftx][up_lefty])
            if d == 1:
                array[i][j] = 0
            elif d == 2:
                array[m][n] = listeAgent[choix].tenir
            print(array)
            affichageAgent(listeAgent)
