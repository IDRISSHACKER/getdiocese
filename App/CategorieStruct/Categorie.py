import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

from App.Api.models.CategorieStruct import *
from utils.gui.msg import msg


class Categorie:
    def __init__(self, home):
        super(Categorie, self).__init__()
        self.home = home
        self.addCtg = loadUi("ui/CategorieStruct/newCategorieStruct.ui")
        self.api = CategorieApi()
        self.initializeTable()
        self.key = 0

    def settup_connexion(self):
        self.populateTable()
        self.home.tableCtgStruct.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.categorieState = 1
        self.home.addCtgStruct.clicked.connect(self.showAddCtgModal)
        self.addCtg.saveCtg.clicked.connect(self.saveCtg)

    def showAddCtgModal(self):
        self.addCtg.setModal(True)
        self.addCtg.setWindowTitle("Ajouter une categorie")
        self.addCtg.ctg.setText("")
        self.addCtg.show()

    def initializeTable(self):
        self.home.tableCtgStruct.setColumnCount(3)
        self.home.tableCtgStruct.setHorizontalHeaderLabels(("Nom de la categorie", "Edition", "Supression"))
        self.home.tableCtgStruct.setColumnWidth(0, 200)
        self.home.tableCtgStruct.setColumnWidth(1, 200)
        self.home.tableCtgStruct.setColumnWidth(2, 200)

    def populateTable(self):
        rows = self.api.getCategories()
        size = 0
        for row in rows:
            size += 1

        self.home.tableCtgStruct.setRowCount(size)
        index = 0

        datas = self.api.getCategories()
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

            self.home.tableCtgStruct.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(data[1]))
            self.home.tableCtgStruct.setCellWidget(index, 1, editBtn)
            self.home.tableCtgStruct.setCellWidget(index, 2, deleteBtn)
            index += 1

    def onSelectedChanged(self, selected, deselected):
        table = self.home.tableCtgStruct
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 1:
                self.edit(value)

            elif index == 2:
                self.api.removeCategorie(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def edit(self, value):
        self.categorieState = 0
        datas = self.api.getCategorie(value)
        for row in datas:
            self.addCtg.setModal(True)
            self.addCtg.setWindowTitle(f"edition de {row[1]}")
            self.key = row[0]
            self.addCtg.ctg.setText(row[1])
            self.addCtg.show()

    def saveCtg(self):
        ctg = self.addCtg.ctg.text()

        secret = f"{time.time_ns()}"

        if len(ctg) > 0:
            if self.categorieState == 1:
                if self.api.setCategorie(secret, ctg):
                    self.addCtg.close()
                    self.addCtg.ctg.setText("")
                    msg.show(f"la nouvelle categorie à été ajoutée avèc success")
                else:
                    print(f"erreur l'ors de l'ajout de {ctg} à la base de donnée")
            else:
                self.api.updateCategorie(self.key, ctg)
                self.addCtg.close()
                msg.show(f"Modification prise en compte ! ")
                self.categorieState = 1
        else:
            print("Vous devez entrer un intitulé")

        self.populateTable()