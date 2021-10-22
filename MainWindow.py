import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, world):
        super(MainWindow, self).__init__()
        self.world = world
        self.setWindowTitle("SMA")
        self.setWindowTitle("Début")
        screen = QApplication.primaryScreen().size()
        w_screen = int(screen.width() - 2 * screen.width() / 10.)
        h_screen = int(screen.height() - 2 * screen.height() / 9.)
        self.move(QPoint(screen.width() / 2 - w_screen / 2, screen.height() / 2 - h_screen / 1.8))

        w = QWidget()
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        w.setLayout(mainLayout)

        grid = QGridLayout()
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        mainLayout.addLayout(grid)
        self.setCentralWidget(w)
        self.array = np.empty([self.world.taille, self.world.taille], dtype=QLabel)

        for i in range(self.world.taille):
            for j in range(self.world.taille):
                self.array[i, j] = QLabel()
                if world.env[i][j] == 0:
                    self.array[i, j].setStyleSheet("QLabel { background-color : black}")
                if world.env[i][j] == 1:
                    self.array[i, j].setStyleSheet("QLabel { background-color : blue}")
                if world.env[i][j] == 2:
                    self.array[i, j].setStyleSheet("QLabel { background-color : red}")

                self.array[i, j].setFixedSize(QSize(w_screen / self.world.taille, h_screen / self.world.taille))
                self.array[i, j].setAlignment(Qt.AlignCenter)
                self.label_size = min(w_screen / self.world.taille, h_screen / self.world.taille)
                self.image = QPixmap('560938.png').scaled(self.label_size, self.label_size)
                #self.array[i, j].setPixmap(self.image)
                grid.addWidget(self.array[i, j], i, j)
