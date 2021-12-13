class LayoutConfig:
    def __init__(self, home):
        super(LayoutConfig, self).__init__()
        self.home = home
        self.home.setWindowTitle("Gestion Eglise")
        self.active = 1

    def setup_connexion(self):
        self.home.menuBtn.clicked.connect(self.toggleMenu)
        self.home.dashboardBtn.clicked.connect(self.goToDashboard)
        self.home.structureBtn.clicked.connect(self.goToStructure)
        self.setActive(self.home.dashboardBtn)

    def goToDashboard(self):
        self.home.pages.setCurrentWidget(self.home.dashboard)
        self.setActive(self.home.dashboardBtn)

    def goToStructure(self):
        self.home.pages.setCurrentWidget(self.home.structure)
        self.setActive(self.home.structureBtn, "Structure")

    def removeActive(self):
        self.home.dashboardBtn.setStyleSheet("")
        self.home.structureBtn.setStyleSheet("")

    def setActive(self, btn, title="Dashboard"):
        self.removeActive()
        self.home.menuLabel.setText(title)
        return btn.setStyleSheet("background: rgba(255, 255, 255, 0.3)")

    def toggleMenu(self):
        menuStatus = self.home.leftMenu.isVisible()
        if (menuStatus):
            self.home.leftMenu.setVisible(False)
        else:
            self.home.leftMenu.setVisible(True)
