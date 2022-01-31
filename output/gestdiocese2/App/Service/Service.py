import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.Service import *

from utils.gui.msg import msg


class Service:
    def __init__(self, home):
        super(Service, self).__init__()
        self.home = home
        self.addService = loadUi("ui/Service/addService.ui")
        self.api = ServiceApi()
        self.initializeTable()
        self.serviceState = 1
        self.key = 0

    def settup_connexion(self):
        self.populateTable()
        self.home.serviceTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.addService.clicked.connect(self.showAddServiceModal)
        self.addService.addService.clicked.connect(self.saveService)

    def showAddServiceModal(self):
        self.serviceState = 1
        self.addZone.setModal(True)
        self.addZone.setWindowTitle("Nouvelle zone")
        self.addZone.zone.setText("")
        self.addZone.show()

    def showAddServiceModal(self):
        self.addService.setModal(True)
        self.addService.show()
        self.addService.setWindowTitle("Ajouter un service")

    def initializeTable(self):
        self.home.serviceTable.setColumnCount(3)
        self.home.serviceTable.setHorizontalHeaderLabels(("Nom du service", "Edition", "Supression"))
        self.home.serviceTable.setColumnWidth(0, 200)
        self.home.serviceTable.setColumnWidth(1, 200)
        self.home.serviceTable.setColumnWidth(2, 200)

    def onSelectedChanged(self, selected, deselected):
        table = self.home.serviceTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 1:
                self.edit(value)

            elif index == 2:
                self.api.removeService(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def edit(self, value):
        self.serviceState = 0
        datas = self.api.getService(value)
        for row in datas:
            self.addService.setModal(True)
            self.addService.setWindowTitle(f"edition de {row[1]}")
            self.key = row[0]
            self.addService.serviceInput.setText(row[1])
            self.addService.show()

    def populateTable(self):
        rows = self.api.getServices()
        size = 0
        for row in rows:
            size += 1

        self.home.serviceTable.setRowCount(size)
        index = 0

        datas = self.api.getServices()
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

            self.home.serviceTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(data[1]))
            self.home.serviceTable.setCellWidget(index, 1, editBtn)
            self.home.serviceTable.setCellWidget(index, 2, deleteBtn)
            index += 1

    def saveService(self):
        service = self.addService.serviceInput.text()
        secret = f"{time.time_ns()}"

        if len(service) > 0:
            if self.serviceState == 1:
                if self.api.setService(secret, service):
                    self.addService.close()
                    self.addService.serviceInput.setText("")
                else:
                    print("Can't save the service")
            else:
                self.api.updateService(self.key, service)
                self.addService.close()
                self.addService.serviceInput.setText("")
                msg.show(f"Modification prise en compte ! ")
        else:
            print("Vous devez entrer un intitulé")

        self.populateTable()