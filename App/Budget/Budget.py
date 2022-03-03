import datetime
import random
import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.Budget import *
from App.Api.models.Structure import StructureApi
from utils.gui.msg import msg

class Budget:
    def __init__(self, home):
        super(Budget, self).__init__()
        self.home = home
        self.addBudget = loadUi("ui/Budget/newBudget.ui")
        self.budgetState = 1
        self.key = 0
        self.api = BudgetApi()
        self.structApi = StructureApi()

    def settup_connexion(self):
        self.initializeTable()
        self.populateTable()
        self.home.budgetTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.addBudget.clicked.connect(self.showBudgetModal)
        self.addBudget.saveBudget.clicked.connect(self.saveBudget)

    def showBudgetModal(self):
        for row in self.structApi.getStructures():
            self.addBudget.structure.addItem(row[4], row[0])

        self.addBudget.setModal(True)
        self.addBudget.show()
        self.addBudget.setWindowTitle("Nouveau budget")

    def initializeTable(self):
        self.home.budgetTable.setColumnCount(6)
        self.home.budgetTable.setHorizontalHeaderLabels(("id", "Structure", "Montant du budget", "Année du budget", "Edition", "Supression"))
        self.home.budgetTable.setColumnWidth(0, 0)
        self.home.budgetTable.setColumnWidth(1, 200)
        self.home.budgetTable.setColumnWidth(2, 200)
        self.home.budgetTable.setColumnWidth(3, 200)

    def populateTable(self):
        rows = self.api.getBudgets()
        size = 0
        for row in rows:
            size += 1

        self.home.budgetTable.setRowCount(size)
        index = 0

        datas = self.api.getBudgets()
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

            self.home.budgetTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[0]}"))
            self.home.budgetTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[1]}"))
            self.home.budgetTable.setCellWidget(index, 2, PyQt5.QtWidgets.QLabel(f"{data[3]} FCFA"))
            self.home.budgetTable.setCellWidget(index, 3, PyQt5.QtWidgets.QLabel(data[2]))
            self.home.budgetTable.setCellWidget(index, 4, editBtn)
            self.home.budgetTable.setCellWidget(index, 5, deleteBtn)
            index += 1

    def onSelectedChanged(self, selected, deselected):
        table = self.home.budgetTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 3:
                pass
                #self.edit(value)

            elif index == 4:
                self.api.updateStructure(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def saveBudget(self):
        secret = random.randint(45, 890)
        structure = self.addBudget.structure.currentData()
        montant = self.addBudget.montant.value()
        year = time.localtime().tm_year

        print(year)

        if len(structure and str(montant)) > 0:
            if self.budgetState == 1:
                if self.api.setBudget(secret, structure, year, montant):
                    self.addBudget.close()
                    self.addBudget.montant.setValue(0)
                    msg.show(f"le nouveau budget à été ajoutée avèc success")
                else:
                    print(f"erreur l'ors de l'ajout de {secret} à la base de donnée")
            else:
                self.api.updateStructure(self.key, structure)
                self.addBudget.close()
                msg.show(f"Modification prise en compte ! ")
        else:
            print("Vous devez entrer un intitulé")

        self.populateTable()