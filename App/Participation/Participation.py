import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import time
from App.Api.models.Element import *
from App.Api.models.Categorie import *
from App.Api.models.Participation import ParticipationApi
from utils.gui.msg import msg

class Partcipation:
    def __init__(self, home):
        super(Partcipation, self).__init__()
        self.api = ParticipationApi()
        self.home = home
        self.addParticipation = loadUi("ui/Participation/participation.ui")
        self.participationState = 1
        self.key = 0

    def settup_connexion(self):
        self.initializeTable()
        self.populateTable()
        self.home.participationTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.addParticipation.clicked.connect(self.showParticipationModal)
        self.addParticipation.saveParticipation.clicked.connect(self.saveParticipation)

    def showParticipationModal(self):
        self.addParticipation.setModal(True)
        self.addParticipation.show()
        self.addParticipation.setWindowTitle("Nouvelle participation")

    def saveParticipation(self):
        id = time.time_ns()
        intitule = self.addParticipation.intitule.text()
        taux = self.addParticipation.taux.value()

        if len(intitule) > 0 and len(str(taux)) > 0:
            if self.participationState == 1:
                if self.api.setParticipation(id, intitule, taux):
                    self.addParticipation.close()
                    self.addParticipation.intitule.setText("")
                    self.addParticipation.taux.setValue(0)
                    msg.show(f"Sauvegarde reusis ! ")

                else:
                    print("Can't save the participation")
            else:
                self.api.updateParticipation(self.key, intitule, taux)
                self.addParticipation.close()
                self.addParticipation.intitule.setText("")
                self.addParticipation.taux.setValue(0)
                msg.show(f"Modification prise en compte ! ")
                self.participationState = 1
        else:
            print("Vous devez entrer un intitulé & un taux")

        self.populateTable()

    def initializeTable(self):
        self.home.participationTable.setColumnCount(4)
        self.home.participationTable.setHorizontalHeaderLabels(("Intitulé de la partipation", "taux", "Edition", "Supression"))
        self.home.participationTable.setColumnWidth(0, 200)
        self.home.participationTable.setColumnWidth(1, 200)
        self.home.participationTable.setColumnWidth(2, 200)
        self.home.participationTable.setColumnWidth(3, 200)

    def populateTable(self):
        rows = self.api.getParticipations()
        size = 0
        for row in rows:
            size += 1

        self.home.participationTable.setRowCount(size)
        index = 0

        datas = self.api.getParticipations()
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

            self.home.participationTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[1]}"))
            self.home.participationTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[2]} %"))
            self.home.participationTable.setCellWidget(index, 2, editBtn)
            self.home.participationTable.setCellWidget(index, 3, deleteBtn)
            index += 1

    def onSelectedChanged(self, selected, deselected):
        table = self.home.participationTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 2:
                print("edit ???")
                self.edit(value)

            elif index == 3:
                print(value)
                self.api.removeParticipation(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def edit(self, value):
        self.participationState = 2
        datas = self.api.getParticipation(value)
        for row in datas:
            self.addParticipation.setModal(True)
            self.addParticipation.setWindowTitle(f"edition de {row[1]}")
            self.key = row[0]
            self.addParticipation.intitule.setText(str(row[1]))
            self.addParticipation.taux.setValue(int(row[2]))
            self.addParticipation.show()