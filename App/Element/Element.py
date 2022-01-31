import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import time
from App.Api.models.Element import *
from App.Api.models.Categorie import *
from utils.gui.msg import msg


class Element:
    def __init__(self, home):
        super(Element, self).__init__()
        self.home = home
        self.addElement = loadUi("ui/Element/newElement.ui")
        self.api = ElementApi()
        self.ctgE = CategorieApi()
        self.elementState = 1
        self.key = 0
        self.initializeTable()

    def settup_connexion(self):
        self.populateTable()
        self.setCategoriesInElement()
        self.home.elementTable.selectionModel().selectionChanged.connect(self.onSelectedChanged)
        self.home.addElement.clicked.connect(self.showAddElementModal)
        self.addElement.saveElement.clicked.connect(self.saveElement)

    def showAddElementModal(self):
        self.addElement.setModal(True)
        self.addElement.show()
        self.addElement.setWindowTitle("Ajouter un element")

    def initializeTable(self):
        self.home.elementTable.setColumnCount(5)
        self.home.elementTable.setHorizontalHeaderLabels(("Titre de l'element", "Montant", "Categorie", "Edition", "Supression"))
        self.home.elementTable.setColumnWidth(0, 200)
        self.home.elementTable.setColumnWidth(1, 200)
        self.home.elementTable.setColumnWidth(2, 200)
        self.home.elementTable.setColumnWidth(4, 200)
        self.home.elementTable.setColumnWidth(5, 200)

    def populateTable(self):
        rows = self.api.getElements()
        size = 0
        for row in rows:
            size += 1

        self.home.elementTable.setRowCount(size)
        index = 0

        datas = self.api.getElements()
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

            self.home.elementTable.setCellWidget(index, 0, PyQt5.QtWidgets.QLabel(f"{data[3]}"))
            self.home.elementTable.setCellWidget(index, 1, PyQt5.QtWidgets.QLabel(f"{data[4]}"))
            self.home.elementTable.setCellWidget(index, 2, PyQt5.QtWidgets.QLabel(f"{data[2]}"))
            self.home.elementTable.setCellWidget(index, 3, editBtn)
            self.home.elementTable.setCellWidget(index, 4, deleteBtn)
            index += 1

    def edit(self, value):
        self.elementState = 0
        datas = self.api.getElement(value)
        for row in datas:
            self.addElement.setModal(True)
            self.addElement.setWindowTitle(f"edition de {row[3]}")
            self.key = row[0]
            self.addElement.titre.setText(f"{row[3]}")
            self.addElement.montant.setText(f"{row[4]}")
            self.addElement.show()

    def onSelectedChanged(self, selected, deselected):
        table = self.home.elementTable
        for ix in selected.indexes():
            row = ix.row()
            index = ix.column()
            value = table.cellWidget(row, 0).text()

            if index == 3:
                self.edit(value)

            elif index == 4:
                self.api.removeElement(value)
                self.populateTable()
                msg.show(f"Supression de {value} resuis ")

    def setCategoriesInElement(self):
        ctgs = self.ctgE.getCategories()
        for row in ctgs:
            self.addElement.ctg.addItem(row[1], row[0])



    def saveElement(self):
        title = self.addElement.titre.text()
        montant = self.addElement.montant.text()
        ctg = self.addElement.ctg.currentData()
        secret = f"{time.time_ns()}"

        if len(title) > 0 and len(montant) > 0 and len(ctg):
            if self.elementState == 1:
                if self.api.setElement(secret, 2, ctg, title, montant):
                    self.addElement.close()
                    self.addElement.titre.setText("")
                    self.addElement.montant.setText("")
                else:
                    print("Can't save the Element")
            else:
                self.api.updateElement(self.key, title, montant, ctg)
                self.addElement.close()
                self.addElement.titre.setText("")
                self.addElement.montant.setText("")
                msg.show(f"Modification prise en compte ! ")
        else:
            print("Vous devez entrer un intitulé")

        self.populateTable()
