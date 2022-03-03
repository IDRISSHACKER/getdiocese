import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import time
from App.Api.models.Element import *
from App.Api.models.Categorie import *
from App.Api.models.Messe import MesseApi
from App.Api.models.Element import ElementApi
from utils.gui.msg import msg

class Messe:
    def __init__(self, home):
        super(Messe, self).__init__()
        self.api = MesseApi()
        self.elem = ElementApi()
        self.home = home
        self.addMesse = loadUi("ui/Messe/Messe.ui")
        self.messeState = 1
        self.key = 0

    def settup_connexion(self):
        self.initializeTable()
        self.populateTable()
        self.setElementInMesse()
        self.home.messeTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.addMesse.saveMesse.clicked.connect(self.saveMesse)
        self.home.addMesse.clicked.connect(self.showMesseModal)

    def showMesseModal(self):
        self.setElementInMesse()
        self.addMesse.setModal(True)
        self.addMesse.show()
        self.addMesse.setWindowTitle("Nouvelle messe")

    def saveMesse(self):
        id = time.time_ns()
        intitule = self.addMesse.intitule.text()
        cpt_el = self.addMesse.compte.currentData()

        if len(intitule) > 0:
            if self.messeState == 1:
                if self.api.setMesse(id, cpt_el, intitule):
                    self.addMesse.close()
                    self.addMesse.intitule.setText("")
                    msg.show(f"Sauvegarde reusis ! ")
                    self.addMesse.close()

                else:
                    print("Can't save the messe")
            else:
                self.api.updateMesse(self.key, cpt_el, intitule)
                self.addMesse.close()
                self.addMesse.intitule.setText("")
                msg.show(f"Modification prise en compte ! ")
                self.messeState = 1
        else:
            print("Vous devez entrer un intitulé & un taux")

        self.populateTable()

    def initializeTable(self):
        self.home.messeTable.setColumnCount(4)
        self.home.messeTable.setHorizontalHeaderLabels(
            ("Intitulé de la messe", "Element", "Edition", "Supression"))
        self.home.messeTable.setColumnWidth(0, 200)
        self.home.messeTable.setColumnWidth(1, 200)
        self.home.messeTable.setColumnWidth(2, 200)
        self.home.messeTable.setColumnWidth(3, 200)

    def populateTable(self):
        rows = self.api.getMesses()
        size = 0
        for row in rows:
            size += 1

        self.home.messeTable.setRowCount(size)
        index = 0

        datas = self.api.getMesses()
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

            self.home.messeTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[2]}"))
            self.home.messeTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[1]}"))
            self.home.messeTable.setCellWidget(index, 2, editBtn)
            self.home.messeTable.setCellWidget(index, 3, deleteBtn)
            index += 1

    def onSelectedChanged(self, selected, deselected):
        table = self.home.messeTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 2:
                print("edit ???")
                self.edit(value)

            elif index == 3:
                print(value)
                self.api.removeMesse(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def edit(self, value):
        self.messeState = 2
        datas = self.api.getMesse(value)
        for row in datas:
            self.addMesse.setModal(True)
            self.addMesse.setWindowTitle(f"edition de {row[1]}")
            self.key = row[0]
            self.addMesse.intitule.setText(str(row[2]))
            self.addMesse.show()

    def setElementInMesse(self):
        elems = self.elem.getElements()
        for row in elems:
            self.addMesse.compte.addItem(row[3], row[0])