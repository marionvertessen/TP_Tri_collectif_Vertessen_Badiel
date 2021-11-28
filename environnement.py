import random
import sys

import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow
from agent import Agent

from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import KMeans


class Environnement:
    taille = 50
    env = np.zeros((taille, taille))
    listeAgent = []
    listePosAgent = []
    liste_cluster = []
    liste_nb_ite = []

    def alea(self):
        x = random.randint(0, self.taille - 1)
        return x

    def init_env(self):
        ##Creation Objet A
        for i in range(200):
            vide = False
            x = self.alea()
            y = self.alea()
            while vide == False:
                x = self.alea()
                y = self.alea()
                if self.env[x][y] == 0:
                    vide = True
            self.env[x][y] = 1

        ##Creation Objet B
        for i in range(200):
            vide = False
            x = self.alea()
            y = self.alea()
            while vide == False:
                x = self.alea()
                y = self.alea()
                if self.env[x][y] == 0:
                    vide = True
            self.env[x][y] = 2

        ##Creation Objet C
        for i in range(200):
            vide = False
            x = self.alea()
            y = self.alea()
            while vide == False:
                x = self.alea()
                y = self.alea()
                if self.env[x][y] == 0:
                    vide = True
            self.env[x][y] = 3

        # Creation agent

        for i in range(20):
            x = self.alea()
            y = self.alea()
            agent = Agent(i)
            self.listeAgent.append(agent)
            self.listePosAgent.append([x, y])

    def liste_coord(self, p):
        liste = []
        for i in range(self.taille):
            for j in range(self.taille):
                if self.env[i][j] == p:
                    liste.append([j, self.taille - i, self.env[i][j]])
        return liste

    def selecting_nb_cluster(self, X):
        range_n_clusters = [k for k in range(2, 20)]
        avg_init = 0
        nb_cluster = 0
        liste_sil = []
        for n_clusters in range_n_clusters:
            clusterer = KMeans(n_clusters=n_clusters, random_state=10)
            cluster_labels = clusterer.fit_predict(X)
            silhouette_avg = silhouette_score(X, cluster_labels)
            liste_sil.append(silhouette_avg)
            if avg_init <= silhouette_avg:
                nb_cluster = n_clusters
                avg_init = silhouette_avg
            """print(
                "For n_clusters =",
                n_clusters,
                "The average silhouette_score is :",
                silhouette_avg)"""
            # filter rows of original data
        #print("Le nombre de cluster : " + str(nb_cluster))
        """Y = np.array(liste_sil)
        X = np.array(range_n_clusters)
        plt.plot(X, Y)
        plt.title("Evolution silhouette")
        plt.xlabel("valeur de k")
        plt.ylabel("Silhouette")
        plt.show()"""
        return nb_cluster

    def deplace(self, nb_iteration):
        cmpt = 0
        while cmpt <= nb_iteration:
            # on choisit l'agent auquel on donne la parole
            choix = random.randint(0, 19)
            i = self.listePosAgent[choix][0]
            i_au = self.listePosAgent[choix][0]
            j = self.listePosAgent[choix][1]
            j_au = self.listePosAgent[choix][1]
            agent = self.listeAgent[choix]
            deplacement = agent.perception_action(self.env[i][j], self.listePosAgent[choix], self.taille)
            no_agent = 1
            if agent.tenir == 3:
                for agentc in listeAgent:
                    if agent.tenir == 3:
                        agent+no_agent == agentc
                        no_agent+=1
                depot = random.uniform(0, 1)
                if depot < agent.pdepot and self.env[i][j] == 0:
                    # print("Je souhaite déposer "+ str(agent.tenir))
                    self.env[i][j] = agent.tenir
                    agent1.tenir = 0
                    agant2.tenir = 0
            else:
                #i, i_au = self.listePosAgent[choix][0]
                #j, j_au = self.listePosAgent[choix][1]
                deplacement = agent.perception_action(self.env[i][j], self.listePosAgent[choix], self.taille)
                depot = random.uniform(0, 1)
                prise = random.uniform(0, 1)
                if self.env[i][j] == 3:
                    if agent.tenir == 0:
                        no_var = 1
                        listePosAutour = []
                        trouve = False
                        while agent.signal>0:
                            if i_au!= self.taille and j_au!= self.taille and i_au!= 0 and i_au != 0:
                                listePosAutour+no_var.append([i_au-1, j_au], [i_au-1, j_au+1], [i_au, j_au+1], [i_au+1, j_au+1], [i_au+1, j_au], [i_au+1, j_au-1], [i_au, j_au-1], [i_au-1, j_au-1])
                                for pos in listePosAutour+no_var:
                                    for posAgent in listePosAgent[choix]:
                                        if pos[0] == posAgent[0] and pos[1] ==posAgent[1]:
                                            trouve = True
                                            pos_agent_trouve = posAgent
                                no_var+=1
                                agent.signal-=1
                                i_au+=1
                                j_au+=1
                        if trouve == True:
                            agent_contact = listeAgent[listePosAgent.index(pos_agent_trouve)]
                            if agent_contact.tenir == 0:
                                listePosAgent[listePosAgent.index(pos_agent_trouve)][0] = i
                                listePosAgent[listePosAgent.index(pos_agent_trouve)][1] = j
                                agent.tenir = 3
                                agent_contact.tenir = 3
                                self.env[i][j] = 0
                else:
                    if agent.tenir == 0:
                        if prise < agent.pprise and self.env[i][j] != 0:
                            agent.tenir = self.env[i][j]
                            self.env[i][j] = 0
                                # print("Je souhaite prendre")
                    else:
                        if depot < agent.pdepot and self.env[i][j] == 0:
                         # print("Je souhaite déposer "+ str(agent.tenir))
                            self.env[i][j] = agent.tenir
                            agent.tenir = 0

                    if deplacement == 0:
                        self.listePosAgent[choix][0] -= self.listeAgent[choix].pas
                    elif deplacement == 1:
                        self.listePosAgent[choix][0] -= self.listeAgent[choix].pas
                        self.listePosAgent[choix][1] += self.listeAgent[choix].pas
                    elif deplacement == 2:
                        self.listePosAgent[choix][1] += self.listeAgent[choix].pas
                    elif deplacement == 3:
                        self.listePosAgent[choix][0] += self.listeAgent[choix].pas
                        self.listePosAgent[choix][1] += self.listeAgent[choix].pas
                    elif deplacement == 4:
                        self.listePosAgent[choix][0] += self.listeAgent[choix].pas
                    elif deplacement == 5:
                        self.listePosAgent[choix][0] += self.listeAgent[choix].pas
                        self.listePosAgent[choix][1] -= self.listeAgent[choix].pas
                    elif deplacement == 6:
                        self.listePosAgent[choix][1] -= self.listeAgent[choix].pas
                    elif deplacement == 7:
                        self.listePosAgent[choix][0] -= self.listeAgent[choix].pas
                        self.listePosAgent[choix][1] -= self.listeAgent[choix].pas

            # print(array)
            # affichageAgent(listeAgent, listePosAgent)
            #print(cmpt)
            if cmpt %500000==0:

                nb_1 = self.selecting_nb_cluster(self.liste_coord(1))
                nb_2 = self.selecting_nb_cluster(self.liste_coord(2))
                self.liste_cluster.append(nb_2 + nb_1)
                self.liste_nb_ite.append(cmpt)
            if cmpt == 1000000 or cmpt == 2000000 or cmpt == 3000000 or cmpt % 5000000 == 0:

                app2 = QApplication.instance()
                print("Affichage de la grille pour "+ str(cmpt) + " itérations !")
                if not app2:  # sinon on crée une instance de QApplication
                    app2 = QApplication(sys.argv)

                # création d'une fenêtre avec QWidget dont on place la référence dans fen
                fen2 = MainWindow(self.env)

                # la fenêtre est rendue visible
                fen2.show()

                # exécution de l'application, l'exécution permet de gérer les événements
                app2.exec_()
                print("Calculs en cours ...")
            cmpt += 1
        Y = np.array(self.liste_cluster)
        X = np.array(self.liste_nb_ite)
        plt.plot(X,Y)
        plt.title("Evolution du nombre de clusters")
        plt.xlabel("Nombre d'itérations")
        plt.ylabel("Nombre de clusters")
        plt.show()

        app2 = QApplication.instance()
        if not app2:  # sinon on crée une instance de QApplication
            app2 = QApplication(sys.argv)

            # création d'une fenêtre avec QWidget dont on place la référence dans fen
        fen2 = MainWindow(self.env)

        # la fenêtre est rendue visible
        fen2.show()

        # exécution de l'application, l'exécution permet de gérer les événements
        app2.exec_()
