import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class Compte:
    def __init__(self, home):
        super(Compte, self).__init__()
        self.home = home
        self.initializeTable()

    def initializeTable(self):
        self.populateTable()
        self.home.compteTable.setColumnCount(2)
        self.home.compteTable.setHorizontalHeaderLabels(("Nom de la structure", "Solde"))
        self.home.compteTable.setColumnWidth(0, 300)
        self.home.compteTable.setColumnWidth(1, 300)

    def populateTable(self):
        self.home.compteTable.setRowCount(1)
        self.home.compteTable.setCellWidget(0, 0, PyQt5.QtWidgets.QLabel("Eglise struct"))
        self.home.compteTable.setCellWidget(0, 1, PyQt5.QtWidgets.QLabel("400 000 FCFA"))