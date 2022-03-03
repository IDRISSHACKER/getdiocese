# -*- coding: utf-8 -*-
from PyQt5.uic import loadUi
from utils.gui.dbJson import dbJson

class LayoutConfig:
    def __init__(self, home, versementPage, main="", loginPage=""):
        super(LayoutConfig, self).__init__()
        self.home = home
        self.versementPage = versementPage
        self.loginPage = loginPage
        self.main = main
        self.json = dbJson("users.json")
        self.home.setWindowTitle("Parametres")
        self.main.setWindowTitle("Gestion Eglise")
        self.active = 1

    def setup_connexion(self):
        self.home.menuBtn.clicked.connect(self.toggleMenu)
        # self.home.dashboardBtn.clicked.connect(self.goToDashboard)
        self.home.structureBtn.clicked.connect(self.goToStructure)
        self.home.serviceBtn.clicked.connect(self.goToService)
        self.versementPage.versementBtn.clicked.connect(self.goToVersement)
        self.home.zoneBtn.clicked.connect(self.goToZone)
        self.home.budgetBtn.clicked.connect(self.goToBudget)
        self.home.categorieBtn.clicked.connect(self.goToCategorie)
        self.home.compteBtn.clicked.connect(self.goToCompte)
        self.home.elementBtn.clicked.connect(self.goToElement)
        self.home.casuelBtn.clicked.connect(self.goToCasuel)
        self.home.messeBtn.clicked.connect(self.goToMesse)
        self.home.participationBtn.clicked.connect(self.goToParticipation)
        self.home.categorieStruct.clicked.connect(self.goToCategorieStruct)
        self.home.tauxBtn.clicked.connect(self.goToTaux)
        self.main.btnCog.clicked.connect(self.showMain)
        self.main.btnVersement.clicked.connect(self.showVersement)
        self.main.btnAdd.clicked.connect(self.showVersement)
        self.versementPage.versementCasuelBtn.clicked.connect(self.goToVersementCasuel)
        self.versementPage.versementMesseBtn.clicked.connect(self.goToVersementMesse)
        self.main.deconnect.clicked.connect(self.logOut)
        

    def showMain(self):
        # self.home.setModal(True)
        self.setActive(self.home.structureBtn)
        self.home.show()

    def showVersement(self):
        self.setActive(self.versementPage.versementBtn)
        self.versementPage.show()

    def goToDashboard(self):
        self.home.pages.setCurrentWidget(self.home.dashboard)
        self.setActive(self.home.dashboardBtn)

    def goToStructure(self):
        self.home.pages.setCurrentWidget(self.home.structure)
        self.setActive(self.home.structureBtn, "Structure")

    def goToService(self):
        self.home.pages.setCurrentWidget(self.home.service)
        self.setActive(self.home.serviceBtn, "Services")

    def goToVersement(self):
        self.versementPage.pages.setCurrentWidget(self.versementPage.versement)
        self.setActive(self.versementPage.versementBtn, "Versement")

    def goToZone(self):
        self.home.pages.setCurrentWidget(self.home.zone)
        self.setActive(self.home.zoneBtn, "Gestion des Zones")

    def goToBudget(self):
        self.home.pages.setCurrentWidget(self.home.budget)
        self.setActive(self.home.budgetBtn, "Budget")

    def goToCategorie(self):
        self.home.pages.setCurrentWidget(self.home.categorie)
        self.setActive(self.home.categorieBtn, "Categorie d'element")

    def goToCategorieStruct(self):
        self.home.pages.setCurrentWidget(self.home.categorieStructure)
        self.setActive(self.home.categorieStruct, "Categorie de structure")

    def goToCompte(self):
        self.home.pages.setCurrentWidget(self.home.compte)
        self.setActive(self.home.compteBtn, "Compte")

    def goToElement(self):
        self.home.pages.setCurrentWidget(self.home.element)
        self.setActive(self.home.elementBtn, "Elements")

    def goToCasuel(self):
        self.home.pages.setCurrentWidget(self.home.casuels)
        self.setActive(self.home.casuelBtn, "Casuel")

    def goToParticipation(self):
        self.home.pages.setCurrentWidget(self.home.participation)
        self.setActive(self.home.participationBtn, "Participation")

    def goToVersementCasuel(self):
        self.versementPage.pages.setCurrentWidget(self.versementPage.versementCasuel)
        self.setActive(self.versementPage.versementCasuelBtn, "Versement casuel")

    def goToMesse(self):
        self.home.pages.setCurrentWidget(self.home.messe)
        self.setActive(self.home.messeBtn, "Messe")

    def goToVersementMesse(self):
        self.versementPage.pages.setCurrentWidget(self.versementPage.versementMesse)
        self.setActive(self.versementPage.versementMesseBtn, "Versement Messe")

    def goToElement(self):
        self.home.pages.setCurrentWidget(self.home.element)
        self.setActive(self.home.elementBtn, "Elements")
    
    def goToTaux(self):
        self.home.pages.setCurrentWidget(self.home.taux)
        self.setActive(self.home.tauxBtn, "Taux")
    
    def logOut(self):
        print("logOut")
        self.main.close()
        self.loginPage.login.show()

    def removeActive(self):
        # self.home.dashboardBtn.setStyleSheet("")
        self.home.structureBtn.setStyleSheet("")
        self.home.serviceBtn.setStyleSheet("")
        # self.home.versementBtn.setStyleSheet("")
        self.home.zoneBtn.setStyleSheet("")
        self.home.budgetBtn.setStyleSheet("")
        self.home.categorieBtn.setStyleSheet("")
        self.home.categorieStruct.setStyleSheet("")
        self.home.compteBtn.setStyleSheet("")
        self.home.elementBtn.setStyleSheet("")
        self.home.casuelBtn.setStyleSheet("")
        self.home.menuBtn.setStyleSheet("")
        self.home.messeBtn.setStyleSheet("")
        self.home.participationBtn.setStyleSheet("")
        self.home.tauxBtn.setStyleSheet("")

        self.versementPage.versementBtn.setStyleSheet("")
        self.versementPage.versementCasuelBtn.setStyleSheet("")
        self.versementPage.versementMesseBtn.setStyleSheet("")

    def setActive(self, btn, title="Dashboard"):
        self.removeActive()
        self.home.menuLabel.setText(title)
        self.versementPage.menuLabel.setText(title)
        return btn.setStyleSheet("background: rgba(255, 255, 255, 0.3)")

    def toggleMenu(self):
        menuStatus = self.home.leftMenu.isVisible()
        if (menuStatus):
            self.home.leftMenu.setVisible(False)
        else:
            self.home.leftMenu.setVisible(True)
    

