import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.Versement import VersementApi
from utils.gui.msg import msg
from utils.gui.Month import Month
from App.Api.models.Compte import CompteApi


class Versement:
    def __init__(self, home):
        super(Versement, self).__init__()
        self.home = home
        self.addVersement = loadUi("ui/Versement/newVersement.ui")
        self.initializeTable()
        self.versementState = 1
        self.api = VersementApi()
        self.comptes = CompteApi()
        self.key = ''

    def settup_connexion(self):
        self.setCompteInVersement()
        self.setMoisInVersement()
        self.populateTable()
        self.home.versementTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.newVersement.clicked.connect(self.showaddVersementModal)
        self.addVersement.saveVersement.clicked.connect(self.saveElement)

    def showaddVersementModal(self):
        self.addVersement.setModal(True)
        self.addVersement.show()
        self.addVersement.setWindowTitle("Ajouter un element")

    def initializeTable(self):
        self.home.versementTable.setColumnCount(6)
        self.home.versementTable.setHorizontalHeaderLabels(("id", "Compte", "Montant" ,"Date", "Edition", "Supression"))
        self.home.versementTable.setColumnWidth(0, 0)
        self.home.versementTable.setColumnWidth(1, 200)
        self.home.versementTable.setColumnWidth(2, 200)
        self.home.versementTable.setColumnWidth(3, 200)

    def populateTable(self):
        rows = self.api.getVersements()
        size = 0
        for row in rows:
            size += 1

        self.home.versementTable.setRowCount(size)
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

            self.home.versementTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[0]}"))
            self.home.versementTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[1]}"))
            self.home.versementTable.setCellWidget(index, 2, PyQt5.QtWidgets.QLabel(f"{data[2]}"))
            self.home.versementTable.setCellWidget(index, 3, PyQt5.QtWidgets.QLabel(f"{data[3]}"))
            self.home.versementTable.setCellWidget(index, 4, editBtn)
            self.home.versementTable.setCellWidget(index, 5, deleteBtn)
            index += 1

    def edit(self, value):
        self.versementState = 0
        datas = self.api.getVersement(value)
        for row in datas:
            self.addVersement.setModal(True)
            self.addVersement.setWindowTitle(f"edition de {row[4]}")
            self.key = row[0]
            self.addVersement.montant.setValue(int(row[2]))
            self.addVersement.show()

    def onSelectedChanged(self, selected, deselected):
        table = self.home.versementTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = int(table.cellWidget(row, 0).text())

            if index == 4:
                self.edit(value)

            elif index == 5:
                self.api.removeVersement(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def setMoisInVersement(self):
        mois = Month().getMonthsTab()
        counter = 0
        for moi in mois:
            self.addVersement.mois.addItem(moi, str(counter))
            counter += 1
    
    def setCompteInVersement(self):
        comptes = self.comptes.getComptes()

        for compte in comptes:
            self.addVersement.numeroCompte.addItem(compte[1], compte[0])

    def saveElement(self):
        #compte = self.addVersement.numeroCompte.text()
        compte = str(self.addVersement.numeroCompte.currentData())
        montant = str(self.addVersement.montant.value())
        date = self.addVersement.calandar.selectedDate().toString("dd/MM/yyyy")
        mois = self.addVersement.mois.currentData()
        id = time.time_ns()

        if len(compte) > 0 and len(montant) > 0:
            if self.versementState == 1:
                if self.api.setVersement(id, compte, montant, date, mois):
                    self.addVersement.close()
                    self.addVersement.montant.setValue(0)
                else:
                    print("Can't save the versement")
            else:
                self.api.updateVersement(self.key, compte, montant, date, mois)
                self.addVersement.close()
                self.addVersement.montant.setValue(0)
                self.versementState = 1
                msg.show(f"Modification prise en compte ! ")
        else:
            print("Vous devez entrer un intitulé")

        self.populateTable()
