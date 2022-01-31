import PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class Versement:
    def __init__(self, home):
        super(Versement, self).__init__()
        self.home = home
        self.addVersement = loadUi("ui/Versement/newVersement.ui")
        self.initializeTable()

    def settup_connexion(self):
        self.populateTable()
        self.home.newVersement.clicked.connect(self.showAddVersement)
        self.addVersement.saveVersement.clicked.connect(self.saveVersement)

    def showAddVersement(self):
        self.addVersement.setModal(True)
        self.addVersement.show()
        self.addVersement.setWindowTitle("Nouveau versement")

    def initializeTable(self):
        self.home.versementTable.setColumnCount(4)
        self.home.versementTable.setHorizontalHeaderLabels(("Montant", "Date", "Editer le versement", "Supprimer"))
        self.home.versementTable.setColumnWidth(0, 200)
        self.home.versementTable.setColumnWidth(1, 200)
        self.home.versementTable.setColumnWidth(2, 200)
        self.home.versementTable.setColumnWidth(3, 200)

    def populateTable(self):
        editBtn = QtWidgets.QPushButton("Editer")
        deleteBtn = QtWidgets.QPushButton("Suprimer")
        editBtn.setIcon(PyQt5.QtGui.QIcon("static/asset/icons/blue/edit.svg"))
        deleteBtn.setIcon(PyQt5.QtGui.QIcon("static/asset/icons/blue/delete.svg"))

        self.home.versementTable.setRowCount(1)
        self.home.versementTable.setCellWidget(0, 0, PyQt5.QtWidgets.QLabel("Montant"))
        self.home.versementTable.setCellWidget(0, 1, PyQt5.QtWidgets.QLabel("Date"))
        self.home.versementTable.setCellWidget(0, 2, editBtn)
        self.home.versementTable.setCellWidget(0, 3, deleteBtn)

    def saveVersement(self):
        montant = self.addVersement.montant.text()
        numeroDeCompte = self.addVersement.numeroCompte.text()

        print(f"{montant} {numeroDeCompte}")

        self.addVersement.close()