import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import time
from App.Api.models.Casuel import CasuelApi
from App.Api.models.Element import ElementApi
from App.Api.models.Categorie import *
from utils.gui.msg import msg

class Casuel:
    def __init__(self, home):
        super(Casuel, self).__init__()
        self.api = CasuelApi()
        self.elem = ElementApi()
        self.home = home
        self.addCasuel = loadUi("ui/Casuels/addCasuel.ui")
        self.key = 0
        self.casuelState = 1

    def settup_connexion(self):
        self.initializeTable()
        self.populateTable()
        self.home.casuelTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.addCasuel.saveCasuel.clicked.connect(self.saveCasuel)
        self.home.newCasuel.clicked.connect(self.showCasuelModal)

    def showCasuelModal(self):
        self.setElementInCasuel()
        self.addCasuel.setModal(True)
        self.addCasuel.show()
        self.addCasuel.setWindowTitle("Nouveau casuel")

    def saveCasuel(self):
        id = time.time_ns()
        intitule = self.addCasuel.intitule.text()
        montant = self.addCasuel.montant.text()
        cpt_el = self.addCasuel.element.currentData()

        if len(intitule) > 0:
            if self.casuelState == 1:
                if self.api.setCasuel(id, cpt_el, intitule, montant):
                    self.addCasuel.close()
                    self.addCasuel.intitule.setText("")
                    self.addCasuel.montant.setValue(0)
                    msg.show(f"Sauvegarde reusis ! ")
                    self.addCasuel.close()

                else:
                    print("Can't save the casuel")
            else:
                self.api.updateCasuel(self.key, cpt_el, intitule, montant)
                self.addCasuel.close()
                self.addCasuel.intitule.setText("")
                self.addCasuel.montant.setValue(0)
                msg.show(f"Modification prise en compte ! ")
                self.casuelState = 1
        else:
            print("Vous devez entrer un intitulé & un montant")

        self.populateTable()

    def initializeTable(self):
        self.home.casuelTable.setColumnCount(5)
        self.home.casuelTable.setHorizontalHeaderLabels(
            ("Intitulé du casuel", "Element", "Montant", "Edition", "Supression"))
        self.home.casuelTable.setColumnWidth(0, 200)
        self.home.casuelTable.setColumnWidth(1, 200)
        self.home.casuelTable.setColumnWidth(2, 200)
        self.home.casuelTable.setColumnWidth(3, 200)
        self.home.casuelTable.setColumnWidth(4, 200)

    def populateTable(self):
        rows = self.api.getCasuels()
        size = 0
        for row in rows:
            size += 1

        self.home.casuelTable.setRowCount(size)
        index = 0

        datas = self.api.getCasuels()
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

            self.home.casuelTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[2]}"))
            self.home.casuelTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[1]}"))
            self.home.casuelTable.setCellWidget(index, 2, PyQt5.QtWidgets.QLabel(f"{data[3]}"))
            self.home.casuelTable.setCellWidget(index, 3, editBtn)
            self.home.casuelTable.setCellWidget(index, 4, deleteBtn)
            index += 1

    def onSelectedChanged(self, selected, deselected):
        table = self.home.casuelTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 3:
                print("edit ???")
                self.edit(value)

            elif index == 4:
                print(value)
                self.api.removeCasuel(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def edit(self, value):
        self.casuelState = 2
        datas = self.api.getCasuel(value)
        for row in datas:
            self.addCasuel.setModal(True)
            self.addCasuel.setWindowTitle(f"edition de {row[1]}")
            self.key = row[0]
            self.addCasuel.intitule.setText(str(row[2]))
            self.addCasuel.montant.setValue(int(row[3]))
            self.addCasuel.show()

    def setElementInCasuel(self):
        elems = self.elem.getElements()
        for row in elems:
            self.addCasuel.element.addItem(row[3], row[0])