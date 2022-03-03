import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.VersementMesse import VersementApi
from App.Api.models.Structure import StructureApi
from App.Api.models.Messe import MesseApi
from utils.gui.msg import msg
from utils.gui.Month import Month


class VersementMesse:
    def __init__(self, home):
        super(VersementMesse, self).__init__()
        self.home = home
        self.addVersement = loadUi("ui/versementMesse/versemetMesse.ui")
        self.initializeTable()
        self.versementState = 1
        self.api = VersementApi()
        self.structApi = StructureApi()
        self.messeApi = MesseApi()
        self.key = ''

    def settup_connexion(self):
        self.setMoisInVersement()
        self.populateTable()
        self.home.versementMesseTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.addNewMesse.clicked.connect(self.showaddVersementModal)
        self.addVersement.saveVersement.clicked.connect(self.saveElement)

    def showaddVersementModal(self):
        self.addVersement.setModal(True)
        self.addVersement.show()
        self.addVersement.setWindowTitle("Versement messe")

    def initializeTable(self):
        self.home.versementMesseTable.setColumnCount(7)
        self.home.versementMesseTable.setHorizontalHeaderLabels(("id", "Structure", "Messe", "Montant" ,"Date", "Edition", "Supression"))
        self.home.versementMesseTable.setColumnWidth(0, 0)
        self.home.versementMesseTable.setColumnWidth(1, 200)
        self.home.versementMesseTable.setColumnWidth(2, 200)
        self.home.versementMesseTable.setColumnWidth(3, 200)

    def populateTable(self):
        rows = self.api.getVersements()
        size = 0
        for row in rows:
            size += 1

        self.home.versementMesseTable.setRowCount(size)
        index = 0

        datas = self.api.getVersements()
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

            self.home.versementMesseTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[0]}"))
            self.home.versementMesseTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[1]}"))
            self.home.versementMesseTable.setCellWidget(index, 2, PyQt5.QtWidgets.QLabel(f"{data[2]}"))
            self.home.versementMesseTable.setCellWidget(index, 3, PyQt5.QtWidgets.QLabel(f"{data[3]}"))
            self.home.versementMesseTable.setCellWidget(index, 4, PyQt5.QtWidgets.QLabel(f"{data[4]}"))
            self.home.versementMesseTable.setCellWidget(index, 5, editBtn)
            self.home.versementMesseTable.setCellWidget(index, 6, deleteBtn)
            index += 1

    def edit(self, value):
        self.versementState = 0
        datas = self.api.getVersement(value)
        for row in datas:
            self.addVersement.setModal(True)
            self.addVersement.setWindowTitle(f"edition de {row[3]}")
            self.key = row[0]
            self.addVersement.montant.setValue(int(row[3]))
            self.addVersement.show()

    def onSelectedChanged(self, selected, deselected):
        table = self.home.versementMesseTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = int(table.cellWidget(row, 0).text())

            if index == 5:
                self.edit(value)

            elif index == 6:
                self.api.removeVersement(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def setMoisInVersement(self):
        mois = Month().getMonthsTab()
        counter = 0
        for moi in mois:
            self.addVersement.mois.addItem(moi, str(counter))
            counter += 1

        messes = self.messeApi.getMesses()
        for messe in messes:
            self.addVersement.casuel.addItem(str(messe[2]), messe[0])

        structs = self.structApi.getStructures()
        for struct in structs:
            self.addVersement.structure.addItem(str(struct[4]), struct[0])

    def saveElement(self):
        structure = self.addVersement.structure.currentData()
        casuel = self.addVersement.casuel.currentData()
        montant = str(self.addVersement.montant.value())
        date = self.addVersement.calandar.selectedDate().toString("dd/MM/yyyy")
        mois = self.addVersement.mois.currentData()
        id = time.time_ns()

        if len(montant) > 0:
            if self.versementState == 1:
                if self.api.setVersement(id, structure, casuel, montant, date, mois):
                    self.addVersement.close()
                    self.addVersement.montant.setValue(0)
                else:
                    print("Can't save the versement")
            else:
                self.api.updateVersement(self.key, structure, casuel, montant, date, mois)
                self.addVersement.close()
                self.addVersement.montant.setValue(0)
                self.versementState = 1
                msg.show(f"Modification prise en compte ! ")
        else:
            print("Vous devez entrer un montant")

        self.populateTable()
