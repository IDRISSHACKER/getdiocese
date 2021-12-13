# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from Custom_Widgets.Widgets import *
from App.LayoutConfig import LayoutConfig
from App.Structure.Structure import Structure
from App.Login.Login import Login
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

count = 0


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__()
        self.home = loadUi("ui/main.ui")
        self.splash = loadUi("ui/Splash.ui")
        self.login = Login(self.home)
        self.conf = LayoutConfig(self.home)
        self.struct = Structure(self.home)
        self.loading()
        self.setup_connexion()
        self.login.setup_connexion()

    def setup_connexion(self):
        self.conf.setup_connexion()
        self.struct.settup_connexion()

    def progress(self):
        global count
        self.splash.progressBar.setValue(count)
        if count > 100:
            self.timer.stop()
            self.splash.close()
            self.login.login.show()
        count += 1

    def startProcess(self):
        global count

    def loading(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.timer.singleShot(0, lambda : self.splash.loadLabel.setText("Bienvenue"))
        self.timer.singleShot(500, lambda : self.splash.loadLabel.setText("Demarage des services..."))
        self.timer.singleShot(1000, lambda : self.splash.loadLabel.setText("Chargement de la base de donnée..."))
        self.timer.singleShot(1001, self.startProcess)
        self.timer.singleShot(8000, lambda : self.splash.loadLabel.setText("Initialisation..."))
        self.splash.setWindowFlag(Qt.FramelessWindowHint)
        self.splash.setAttribute(Qt.WA_TranslucentBackground)
        self.splash.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()

    sys.exit(app.exec_())
