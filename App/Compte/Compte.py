import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import time
from App.Api.models.Compte import CompteApi
from App.Api.models.Structure import StructureApi
from utils.gui.msg import msg

class Compte:
    def __init__(self, home):
        super(Compte, self).__init__()
        self.api = CompteApi()
        self.structApi = StructureApi()
        self.home = home
        self.addCompte = loadUi("ui/Compte/Compte.ui")
        self.key = 0
        self.casuelState = 1

    def settup_connexion(self):
        self.initializeTable()
        self.populateTable()
        self.home.compteTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.addCompte.saveCompte.clicked.connect(self.saveCompte)
        self.home.addCompte.clicked.connect(self.showCompteModal)

    def showCompteModal(self):
        self.setElementInCasuel()
        self.addCompte.setModal(True)
        self.addCompte.show()
        self.addCompte.setWindowTitle("Nouveau compte")

    def saveCompte(self):
        id = time.time_ns()
        montant = self.addCompte.montant.value()
        structure = self.addCompte.structure.currentData()

        if len(str(montant)) > 0:
            if self.casuelState == 1:
                if self.api.setCompte(id, structure, montant):
                    self.addCompte.close()
                    self.addCompte.montant.setValue(0)
                    msg.show(f"Sauvegarde reusis ! ")
                    self.addCompte.close()

                else:
                    print("Can't save the casuel")
            else:
                self.api.updateCompte(self.key, structure, montant)
                self.addCompte.close()
                self.addCompte.montant.setValue(0)
                msg.show(f"Modification prise en compte ! ")
                self.casuelState = 1
        else:
            print("Vous devez entrer un montant")

        self.populateTable()

    def initializeTable(self):
        self.home.compteTable.setColumnCount(5)
        self.home.compteTable.setHorizontalHeaderLabels(
            ("numero de compte", "Structure", "Montant", "Edition", "Supression"))
        self.home.compteTable.setColumnWidth(0, 200)
        self.home.compteTable.setColumnWidth(1, 200)
        self.home.compteTable.setColumnWidth(2, 200)
        self.home.compteTable.setColumnWidth(3, 200)
        self.home.compteTable.setColumnWidth(4, 200)

    def populateTable(self):
        rows = self.api.getComptes()
        size = 0
        for row in rows:
            size += 1

        self.home.compteTable.setRowCount(size)
        index = 0

        datas = self.api.getComptes()
        for data in datas:
            objetNameEdit = f"{data[0]}-E"
            objetNameDelete = f"{data[0]}-D"

            editBtn = QtWidgets.QPushButton("Editer")
            editBtn.setObjectName(objetNameEdit)
            editBtn.setStyleSheet("""padding: 10px;
            border-radius: 4px;
            font-size: 10px;
            border: none;
            width: 200px;
            height: auto;
            text-align: center;""")

            deleteBtn = QtWidgets.QPushButton("Suprimer")
            deleteBtn.setObjectName(objetNameDelete)
            deleteBtn.setStyleSheet("""padding: 10px;
            border-radius: 4px;
            font-size: 10px;
            border: none;
            color: #ab0a0a;
            background-color: rgb(249, 122, 122, 0.1);
            width: 200px;
            height: auto;
            text-align: center;""")

            editBtn.setIcon(PyQt5.QtGui.QIcon("static/asset/icons/blue/edit.svg"))
            deleteBtn.setIcon(PyQt5.QtGui.QIcon("static/asset/icons/blue/delete.svg"))

            self.home.compteTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[0]}"))
            self.home.compteTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[1]}"))
            self.home.compteTable.setCellWidget(index, 2, PyQt5.QtWidgets.QLabel(f"{data[2]}"))
            self.home.compteTable.setCellWidget(index, 3, editBtn)
            self.home.compteTable.setCellWidget(index, 4, deleteBtn)
            index += 1

    def onSelectedChanged(self, selected, deselected):
        table = self.home.compteTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 3:
                print("edit ???")
                self.edit(value)

            elif index == 4:
                print(value)
                self.api.removeCompte(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def edit(self, value):
        self.casuelState = 2
        datas = self.api.getCompte(value)
        for row in datas:
            self.addCompte.setModal(True)
            self.addCompte.setWindowTitle(f"edition de {row[1]}")
            self.key = row[0]
            self.addCompte.montant.setValue(int(row[2]))
            self.addCompte.show()

    def setElementInCasuel(self):
        elems = self.structApi.getStructures()
        for row in elems:
            self.addCompte.structure.addItem(row[4], row[0])