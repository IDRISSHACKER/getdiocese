# -*- coding: utf-8 -*-
import bdb
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from App.Login.Login import Login
from App.LayoutConfig import LayoutConfig
from App.Structure.Structure import Structure
from App.Service.Service import Service
from App.Versement.Versement import Versement
from App.Zone import Zone
from App.Budget.Budget import Budget
from App.Categorie.Categorie import Categorie
from App.Compte.Compte import Compte
from App.Element.Element import Element
from App.Casuel.Casuel import Casuel
from App.Messe.Messe import Messe
from App.Participation.Participation import Partcipation
from App.Taux.Taux import Taux
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from App.Api.models.bdd.Connexion import bdd

count = 0


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__()

        self.home = loadUi("ui/main.ui")
        self.main = loadUi("ui/home.ui")
        self.splash = loadUi("ui/Splash.ui")
        self.notDb = loadUi("ui/ErrBdd.ui")
        self.bdd = bdd()
        self.login = Login(self.home, self.main)
        self.conf = LayoutConfig(self.home, self.main)

        self.loading()
        # self.setup_connexion()
        self.bdd.worker.finished.connect(self.endWorker)

    def setup_connexion(self):
        self.struct = Structure(self.home)
        self.service = Service(self.home)
        self.versement = Versement(self.home)
        self.zone = Zone(self.home)
        self.budget = Budget(self.home)
        self.categorie = Categorie(self.home)
        self.compte = Compte(self.home)
        self.element = Element(self.home)
        self.casuel = Casuel(self.home)
        self.messe = Messe(self.home)
        self.participation = Partcipation(self.home)
        # self.taux = Taux(self.main)

        self.login.setup_connexion()
        self.conf.setup_connexion()
        self.struct.settup_connexion()
        self.service.settup_connexion()
        self.versement.settup_connexion()
        self.zone.settup_connexion()
        self.budget.settup_connexion()
        self.categorie.settup_connexion()
        self.element.settup_connexion()
        # self.taux.settup_connexion()
        self.casuel.settup_connexion()
        self.messe.settup_connexion()
        self.participation.settup_connexion()

    def endWorker(self):
        self.setup_connexion()
        self.login.login.show()
        self.splash.close()
        #self.bdd.thread.quit()

    def progress(self):
        global count
        self.splash.progressBar.setValue(count)
        if self.bdd.connect:
            self.timer.stop()
        count += 1

    def startProcess(self):
        global count

    def loading(self):
        # self.bd = bdd()
        # if not self.bd.test():
        #   self.notDb.err.setText(self.bd.errMsg())
        #   self.notDb.show()
        # else:
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.timer.singleShot(0, lambda: self.splash.loadLabel.setText("Bienvenue"))
        self.timer.singleShot(500, lambda: self.splash.loadLabel.setText("Demarage des services..."))
        self.timer.singleShot(1000,
                              lambda: self.splash.loadLabel.setText("Initialisation de votre Interface en cour..."))
        self.timer.singleShot(3000, lambda: self.splash.loadLabel.setText("Vous'y êtes presque..."))
        self.timer.singleShot(4000, self.startProcess)

        self.splash.setWindowFlag(Qt.FramelessWindowHint)
        self.splash.setAttribute(Qt.WA_TranslucentBackground)
        self.splash.show()


app = QApplication(sys.argv)
window = Main()

try:
    sys.exit(app.exec_())
except:
    print("exiting...")
