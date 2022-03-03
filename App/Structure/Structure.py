import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.Structure import StructureApi
from App.Api.models.Zone import ZoneApi
from App.Api.models.Service import ServiceApi
from App.Api.models.CategorieStruct import CategorieApi
from utils.gui.msg import msg
from utils.gui.dbJson import dbJson


class Structure:
    def __init__(self, home):
        super(Structure, self).__init__()
        self.home = home
        self.dbJson = dbJson("users.json")
        self.addStructure = loadUi("ui/Structure/addStructure.ui")
        self.structureState = 1
        self.key = 0
        self.api = StructureApi()
        self.zoneApi = ZoneApi()
        self.serviceApi = ServiceApi()
        self.ctgApi = CategorieApi()
        self.userData = self.dbJson.getJson()
        self.addStructure.boxCtg.setVisible(False)

        self.initializeTable()
        self.populateTable()

    def settup_connexion(self):
        self.initializeTable()
        self.populateTable()
        self.home.structTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.addStruct.clicked.connect(self.showAddStructModal)
        self.addStructure.addStruct.clicked.connect(self.saveStructure)

    def showAddStructModal(self):
        self.populateSelect()
        self.addStructure.setModal(True)
        self.addStructure.show()
        self.addStructure.setWindowTitle("Ajouter une structure")

    def populateSelect(self):
        zones = self.zoneApi.getZones()

        for row in zones:
            self.addStructure.zone.addItem(row[1], row[0])

        services = self.serviceApi.getServices()
        for row in services:
            self.addStructure.service.addItem(row[1], row[0])
        
        ctgStructures = self.ctgApi.getCategories()
        for row in ctgStructures:
            self.addStructure.ctgStruct.addItem(row[1], row[0])

    def initializeTable(self):
        self.home.structTable.setColumnCount(4)
        self.home.structTable.setHorizontalHeaderLabels(
            ("Nom de la structure", "Chef de la struture", "Edition", "Supression"))
        self.home.structTable.setColumnWidth(0, 200)
        self.home.structTable.setColumnWidth(1, 200)
        self.home.structTable.setColumnWidth(2, 200)
        self.home.structTable.setColumnWidth(3, 200)

    def populateTable(self):
        rows = self.api.getStructures()
        size = 0
        for row in rows:
            size += 1

        self.home.structTable.setRowCount(size)
        index = 0

        datas = self.api.getStructures()
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

            self.home.structTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[4]}"))
            self.home.structTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[5]}"))
            self.home.structTable.setCellWidget(index, 2, editBtn)
            self.home.structTable.setCellWidget(index, 3, deleteBtn)
            index += 1

    def saveStructure(self):
        secret = f"{time.time_ns()}"
        nameStructure = self.addStructure.structure.text()
        chefStructure = self.addStructure.chef.text()
        zone = self.addStructure.zone.currentData()
        service = self.addStructure.service.currentData()
        #ctgStructure = self.addStructure.ctgStruct.currentData()
        ctgStructure = self.dbJson.getJson("users.json").get("ctgStruct")
        print(f"CtgStruct {ctgStructure}")
        print(self.userData)

        if len(nameStructure) > 0 and len(chefStructure) > 0:
            if self.structureState == 1:
                self.api.setStructure(secret, ctgStructure, zone, service, nameStructure, chefStructure)

                self.addStructure.structure.setText("")
                self.addStructure.chef.setText("")
            else:
                self.api.updateStructure(self.key, ctgStructure, zone, service, nameStructure, chefStructure)
                self.addStructure.close()
                self.addStructure.chef.setText("")
                self.addStructure.structure.setText("")
                msg.show(f"Modification prise en compte ! ")
                self.structureState = 1
        else:
            print("Veillez remplir tous les champs")

        self.addStructure.close()
        self.populateTable()

    def onSelectedChanged(self, selected, deselected):
        table = self.home.structTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 2:
                self.populateSelect()
                self.edit(value)

            elif index == 3:
                self.api.removeStructure(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def edit(self, value):
        self.structureState = 0
        datas = self.api.getStructure(value)
        for row in datas:
            self.addStructure.setModal(True)
            self.addStructure.setWindowTitle(f"edition de {row[4]}")
            self.key = row[0]
            self.addStructure.structure.setText(f"{row[4]}")
            self.addStructure.chef.setText(f"{row[5]}")

        self.addStructure.show()
