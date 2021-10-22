import random
import numpy as np

global d
class Environnement:
    taille = 50
    env = np.zeros((taille,taille))

    def deplace(self, actual, agent, pos_agent, choix, pas):
        print("Je suis l'agent "+str(agent.id))
        deplacement = agent.perception_action(actual, pos_agent[choix])
        if deplacement == 0:
            pos_agent[choix][0] -= pas
        elif deplacement == 1:
            pos_agent[choix][0] -= pas
            pos_agent[choix][1] += pas
        elif deplacement == 2:
            pos_agent[choix][1] += pas
        elif deplacement == 3:
            pos_agent[choix][0] += pas
            pos_agent[choix][1] += pas
        elif deplacement == 4:
            pos_agent[choix][0] += pas
        elif deplacement == 5:
            pos_agent[choix][0] += pas
            pos_agent[choix][1] -= pas
        elif deplacement == 6:
            pos_agent[choix][1] -= pas
        elif deplacement == 7:
            pos_agent[choix][0] -= pas
            pos_agent[choix][1] -= pas
        depot = random.uniform(0,1)
        prise = random.uniform(0,1)
        if agent.tenir == 0:
            if prise < agent.pprise:
                agent.tenir = actual
                agent.change = 1
                #print("Je souhaite prendre")
        else:
            if depot < agent.pdepot:
                #print("Je souhaite déposer "+ str(agent.tenir))
                agent.change = 2

        return pos_agent, agent

