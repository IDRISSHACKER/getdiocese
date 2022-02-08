import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import time
from App.Api.models.Element import *
from App.Api.models.Categorie import *

class Partcipation:
    def __init__(self, home):
        super(Partcipation, self).__init__()
        self.home = home
        self.addParticipation = loadUi("ui/Participation/participation.ui")
        self.elementState = 1
        self.key = 0

    def settup_connexion(self):
        self.home.addParticipation.clicked.connect(self.showParticipationModal)

    def showParticipationModal(self):
        self.addParticipation.setModal(True)
        self.addParticipation.show()
        self.addParticipation.setWindowTitle("Nouvelle participation")
