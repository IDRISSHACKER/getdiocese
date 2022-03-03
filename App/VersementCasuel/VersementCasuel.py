import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.VersementCasuel import VersementApi
from App.Api.models.Structure import StructureApi
from App.Api.models.Casuel import CasuelApi
from utils.gui.msg import msg
from utils.gui.Month import Month


class VersementCasuel:
    def __init__(self, home):
        super(VersementCasuel, self).__init__()
        self.home = home
        self.addVersement = loadUi("ui/versementCasuel/versemetCasuel.ui")
        self.initializeTable()
        self.versementState = 1
        self.api = VersementApi()
        self.structApi = StructureApi()
        self.casuelApi = CasuelApi()
        self.key = ''

    def settup_connexion(self):
        self.setMoisInVersement()
        self.populateTable()
        self.home.versementCasuelTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.addVersementCasuel.clicked.connect(self.showaddVersementModal)
        self.addVersement.saveVersement.clicked.connect(self.saveElement)

    def showaddVersementModal(self):
        self.addVersement.setModal(True)
        self.addVersement.show()
        self.addVersement.setWindowTitle("Ajouter un element")

    def initializeTable(self):
        self.home.versementCasuelTable.setColumnCount(8)
        self.home.versementCasuelTable.setHorizontalHeaderLabels(("id", "Structure", "Casuel", "Montant" ,"Date", "Mois","Edition", "Supression"))
        self.home.versementCasuelTable.setColumnWidth(0, 0)
        self.home.versementCasuelTable.setColumnWidth(1, 200)
        self.home.versementCasuelTable.setColumnWidth(2, 200)
        self.home.versementCasuelTable.setColumnWidth(3, 200)

    def populateTable(self):
        rows = self.api.getVersements()
        size = 0
        for row in rows:
            size += 1

        self.home.versementCasuelTable.setRowCount(size)
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

            self.home.versementCasuelTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[0]}"))
            self.home.versementCasuelTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[1]}"))
            self.home.versementCasuelTable.setCellWidget(index, 2, PyQt5.QtWidgets.QLabel(f"{data[2]}"))
            self.home.versementCasuelTable.setCellWidget(index, 3, PyQt5.QtWidgets.QLabel(f"{data[3]}"))
            self.home.versementCasuelTable.setCellWidget(index, 4, PyQt5.QtWidgets.QLabel(f"{data[4]}"))
            self.home.versementCasuelTable.setCellWidget(index, 5, PyQt5.QtWidgets.QLabel(f"{data[5]}"))
            self.home.versementCasuelTable.setCellWidget(index, 6, editBtn)
            self.home.versementCasuelTable.setCellWidget(index, 7, deleteBtn)
            index += 1

    def edit(self, value):
        self.versementState = 0
        datas = self.api.getVersement(value)
        for row in datas:
            self.addVersement.setModal(True)
            self.addVersement.setWindowTitle(f"edition de {row[3]}")
            self.key = row[0]
            self.addVersement.montant.setText(f"{row[3]}")
            self.addVersement.show()

    def onSelectedChanged(self, selected, deselected):
        table = self.home.versementCasuelTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = int(table.cellWidget(row, 0).text())

            if index == 6:
                self.edit(value)

            elif index == 7:
                self.api.removeVersement(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def setMoisInVersement(self):
        mois = Month().getMonthsTab()
        counter = 0
        for moi in mois:
            self.addVersement.mois.addItem(moi, str(counter))
            counter += 1

        casuels = self.casuelApi.getCasuels()
        for casuel in casuels:
            self.addVersement.casuel.addItem(str(casuel[2]), casuel[0])
            self.addVersement.montant.setText(str(casuel[3]))

        structs = self.structApi.getStructures()
        for struct in structs:
            self.addVersement.structure.addItem(str(struct[4]), struct[0])


    def saveElement(self):
        structure = self.addVersement.structure.currentData()
        casuel = self.addVersement.casuel.currentData()
        montant = self.addVersement.montant.text()
        date = self.addVersement.calandar.selectedDate().toString("dd/MM/yyyy")
        mois = self.addVersement.mois.currentData()
        id = time.time_ns()
        print(date)
        if len(montant) > 0:
            if self.versementState == 1:
                if self.api.setVersement(id, structure, casuel, montant, date, mois):
                    self.addVersement.close()
                else:
                    print("Can't save the versement")
            else:
                self.api.updateVersement(self.key, structure, casuel, montant, date, mois)
                self.addVersement.close()
                self.versementState = 1
                msg.show(f"Modification prise en compte ! ")
        else:
            print("Vous devez entrer un montant")

        self.populateTable()
