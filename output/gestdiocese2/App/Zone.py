# -*- coding: utf-8 -*-
import random
import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from App.Api.models.Zone import *
from utils.gui.msg import msg

class Zone:
    def __init__(self, home):
        super(Zone, self).__init__()
        self.home = home
        self.addZone = loadUi("ui/Zone/newZone.ui")
        self.initializeTable()
        self.api = ZoneApi()
        self.zoneState = 1
        self.key = 0

    def settup_connexion(self):
        self.populateTable()
        self.home.zoneTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.addZone.clicked.connect(self.showAddZoneModal)
        self.addZone.saveZone.clicked.connect(self.saveZone)

    def showAddZoneModal(self):
        self.zoneState = 1
        self.addZone.setModal(True)
        self.addZone.setWindowTitle("Nouvelle zone")
        self.addZone.zone.setText("")
        self.addZone.show()

    def initializeTable(self):
        self.home.zoneTable.setColumnCount(3)
        self.home.zoneTable.setHorizontalHeaderLabels(("Nom de la zone", "Edition", "Supression"))
        self.home.zoneTable.setColumnWidth(0, 400)
        self.home.zoneTable.setColumnWidth(1, 200)
        self.home.zoneTable.setColumnWidth(2, 200)

    def populateTable(self):
        rows = self.api.getZones()
        size = 0
        for row in rows:
            size += 1

        self.home.zoneTable.setRowCount(size)
        index = 0

        datas = self.api.getZones()
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

            self.home.zoneTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(data[1]))
            self.home.zoneTable.setCellWidget(index, 1, editBtn)
            self.home.zoneTable.setCellWidget(index, 2, deleteBtn)
            index += 1

    def edit(self, value):
        self.zoneState = 0
        datas = self.api.getZone(value)
        for row in datas:
            self.addZone.setModal(True)
            self.addZone.setWindowTitle(f"edition de {row[1]}")
            self.key = row[0]
            self.addZone.zone.setText(row[1])
            self.addZone.show()

    def onSelectedChanged(self, selected, deselected):
        table = self.home.zoneTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 1:
                self.edit(value)

            elif index == 2:
                self.api.removeZone(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def test(self):
        table = self.home.zoneTable
        v = table.cellWidget(1, 0).text()
        print(v)

    def saveZone(self):
        zone = self.addZone.zone.text()
        secret = f"{time.time_ns()}"

        if len(zone) > 0:
            if self.zoneState == 1:
                if self.api.setZone(secret, zone):
                    self.addZone.close()
                    self.addZone.zone.setText("")
                    msg.show(f"la nouvelle zone à été ajoutée avèc success")
                else:
                    print(f"erreur l'ors de l'ajout de {secret} à la base de donnée")
            else:
                self.api.updateZone(self.key, zone)
                self.addZone.close()
                msg.show(f"Modification prise en compte ! ")
        else:
            print("Vous devez entrer un intitulé")

        self.populateTable()

