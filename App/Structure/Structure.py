import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class Structure:
    def __init__(self, home):
        super(Structure, self).__init__()
        self.home = home
        self.addStructure = loadUi("ui/Structure/addStructure.ui")
        self.initializeTable()
        self.populateTable()

    def settup_connexion(self):
        self.home.addStruct.clicked.connect(self.showAddStructModal)
        self.addStructure.addStruct.clicked.connect(self.saveStructure)

    def showAddStructModal(self):
        self.addStructure.setModal(True)
        self.addStructure.show()
        self.addStructure.setWindowTitle("Ajouter une structure")

    def initializeTable(self):
        self.home.structTable.setColumnCount(4)
        self.home.structTable.setHorizontalHeaderLabels(("Nom de la structure", "Chef de la struture", "Edition", "Supression"))
        self.home.structTable.setColumnWidth(0, 200)
        self.home.structTable.setColumnWidth(1, 200)
        self.home.structTable.setColumnWidth(2, 200)
        self.home.structTable.setColumnWidth(3, 200)

    def populateTable(self):
        editBtn = QtWidgets.QPushButton("Editer")
        deleteBtn = QtWidgets.QPushButton("Suprimer")
        editBtn.setIcon(PyQt5.QtGui.QIcon("static/asset/icons/blue/edit.svg"))
        deleteBtn.setIcon(PyQt5.QtGui.QIcon("static/asset/icons/blue/delete.svg"))

        self.home.structTable.setRowCount(1)
        self.home.structTable.setCellWidget(0, 0, PyQt5.QtWidgets.QLabel("Eglise catholique de bafang"))
        self.home.structTable.setCellWidget(0, 1, PyQt5.QtWidgets.QLabel("JOHN SMITH"))
        self.home.structTable.setCellWidget(0, 2, editBtn)
        self.home.structTable.setCellWidget(0, 3, deleteBtn)

    def saveStructure(self):
        nameStructure = self.addStructure.lineEdit.text()
        chefStructure = self.addStructure.lineEdit_2.text()

        print(f"{nameStructure}<=====>{chefStructure}")

        #self.addStructure.lineEdit.setText()
        #self.addStructure.lineEdit_2.setText()
        self.addStructure.close()