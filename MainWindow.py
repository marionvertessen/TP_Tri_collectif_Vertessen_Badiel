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
        h_screen = int(screen.height() - 2 * screen.height() / 10.)
        self.move(QPoint(screen.width() / 2 - w_screen / 2, screen.height() / 2 - h_screen / 2))

        w = QWidget()
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        w.setLayout(mainLayout)

        grid = QGridLayout()
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        mainLayout.addLayout(grid)
        self.setCentralWidget(w)
        self.array = np.empty([len(self.world), len(self.world)], dtype=QLabel)

        for i in range(len(self.world)):
            for j in range(len(self.world)):
                self.array[i, j] = QLabel()
                if world[i][j] == 0:
                    self.array[i, j].setStyleSheet("QLabel { background-color : black}")
                if world[i][j] == 1:
                    self.array[i, j].setStyleSheet("QLabel { background-color : blue}")
                if world[i][j] == 2:
                    self.array[i, j].setStyleSheet("QLabel { background-color : red}")

                self.array[i, j].setFixedSize(QSize(w_screen / len(self.world), h_screen / len(self.world)))
                self.array[i, j].setAlignment(Qt.AlignCenter)
                self.label_size = min(w_screen / len(self.world), h_screen / len(self.world))
                grid.addWidget(self.array[i, j], i, j)
