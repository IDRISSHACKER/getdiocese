import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import time
from App.Api.models.Element import *
from App.Api.models.Categorie import *


class Messe:
    def __init__(self, home):
        super(Messe, self).__init__()
        self.home = home
        self.addMesse = loadUi("ui/Messe/Messe.ui")
        self.elementState = 1
        self.key = 0

    def settup_connexion(self):
        self.home.addMesse.clicked.connect(self.showMesseModal)

    def showMesseModal(self):
        self.addMesse.setModal(True)
        self.addMesse.show()
        self.addMesse.setWindowTitle("Nouvelle messe")
