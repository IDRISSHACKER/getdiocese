import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.Structure import *
from App.Api.models.Element import *


class Taux:
    def __init__(self, home):
        super(Taux, self).__init__()
        self.home = home
        self.struct = StructureApi()
        self.elem   = ElementApi()
        self.addTaux = loadUi("ui/Taux/Taux.ui")
        self.initializeTable()
        self.populateTable()
        self.populateGroupBox()

    def settup_connexion(self):
        self.home.btnAdd.clicked.connect(self.showAdd)

    def showAdd(self):
        self.addTaux.setModal(True)
        self.addTaux.show()
        self.addTaux.setWindowTitle("Nouveau taux")


    def initializeTable(self):
        self.home.tauxTable.setColumnCount(4)
        self.home.tauxTable.setHorizontalHeaderLabels(("Cat", "PP", "FP", "FD", "FD", "structure", "PFP"))
        self.home.tauxTable.setColumnWidth(0, 200)
        self.home.tauxTable.setColumnWidth(1, 200)
        self.home.tauxTable.setColumnWidth(2, 200)
        self.home.tauxTable.setColumnWidth(3, 200)
        self.home.tauxTable.setColumnWidth(4, 200)
        self.home.tauxTable.setColumnWidth(5, 200)

    def populateTable(self):
        pass

    def saveTaux(self):
        pass

    def populateGroupBox(self):
        structures = self.struct.getStructures()
        for row in structures:
            self.addTaux.structure.addItem(row[4], row[0])

        elements = self.elem.getElements()
        for row in elements:
            self.addTaux.element.addItem(row[3], row[0])
