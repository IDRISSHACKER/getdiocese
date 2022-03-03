import time
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.Participation import ParticipationApi
from App.Api.models.Casuel import CasuelApi
from App.Api.models.Taux import TauxApi
from utils.gui.msg import msg


class Taux:
    def __init__(self, home):
        super(Taux, self).__init__()
        self.home = home
        self.api = TauxApi()
        self.casuels = CasuelApi()
        self.participations   = ParticipationApi()
        self.addTaux = loadUi("ui/Taux/Taux.ui")
        #self.initializeTable()
        #self.populateTable()
        #self.populateGroupBox()

    def settup_connexion(self):
        self.initializeTable()
        self.populateTable()
        self.populateGroupBox()
        self.home.tauxTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.addTaux.saveTaux.clicked.connect(self.saveTaux)
        self.home.addTaux.clicked.connect(self.showAdd)

    def showAdd(self):
        self.addTaux.setModal(True)
        self.addTaux.show()
        self.addTaux.setWindowTitle("Nouveau taux")

    def initializeTable(self):
        self.home.tauxTable.setColumnCount(5)
        self.home.tauxTable.setHorizontalHeaderLabels(("id", "participation", "casuel", "valeur du taux", "supression"))
        self.home.tauxTable.setColumnWidth(0, 0)
        self.home.tauxTable.setColumnWidth(1, 200)
        self.home.tauxTable.setColumnWidth(2, 200)
        self.home.tauxTable.setColumnWidth(3, 200)

    def populateTable(self):
        taux = self.api.getTaux()
        size = 0
        for row in taux:
            size += 1

        self.home.tauxTable.setRowCount(size)
        index = 0

        taux2 = self.api.getTaux()
        for data in taux2:
            objetNameDelete = f"{data[0]}-D"
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
            deleteBtn.setIcon(PyQt5.QtGui.QIcon("static/asset/icons/blue/delete.svg"))

            self.home.tauxTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(str(data[0])))
            self.home.tauxTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(str(data[1])))
            self.home.tauxTable.setCellWidget(index, 2, PyQt5.QtWidgets.QLabel(str(data[2])))
            self.home.tauxTable.setCellWidget(index, 3, PyQt5.QtWidgets.QLabel(str(data[3])))
            self.home.tauxTable.setCellWidget(index, 4, deleteBtn)
            index += 1

    def saveTaux(self):
        id = time.time_ns()
        id_part = self.addTaux.participation.currentData()
        id_c = self.addTaux.casuel.currentData()
        valeur = self.addTaux.valeur.value()

        if self.api.setTaux(id, id_part, id_c, valeur):
            self.addTaux.close()
            self.addTaux.valeur.setValue(0)
            self.populateTable()

    def populateGroupBox(self):
        participations = self.participations.getParticipations()
        for row in participations:
            self.addTaux.participation.addItem(row[1], row[0])

        casuels = self.casuels.getCasuels()
        for row in casuels:
            self.addTaux.casuel.addItem(row[2], row[0])

    def onSelectedChanged(self, selected, deselected):
        table = self.home.tauxTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 4:
                print(value)
                self.api.removeTaux(value)
                self.populateTable()
                msg.show(f"Supression reussis")