import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import time
from App.Api.models.Element import *
from App.Api.models.Categorie import *


class Casuel:
    def __init__(self, home):
        super(Casuel, self).__init__()
        self.home = home
        self.addCasuel = loadUi("ui/Casuels/addCasuel.ui")
        self.elementState = 1
        self.key = 0

    def settup_connexion(self):
        self.home.newCasuel.clicked.connect(self.showCasuelModal)

    def showCasuelModal(self):
        self.addCasuel.setModal(True)
        self.addCasuel.show()
        self.addCasuel.setWindowTitle("Nouveau casuel")
