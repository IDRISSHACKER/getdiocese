import time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from App.Api.models.Users import Users
from utils.gui.dbJson import dbJson
from App.Api.models.CategorieStruct import CategorieApi

count = 0
count2 = 0


class Login:
    def __init__(self, home, main="", versementPage=""):
        super(Login, self).__init__()
        self.home = home
        self.main = main
        self.versementPage = versementPage
        self.status = 0
        self.ctgStruct = CategorieApi()
        self.login = loadUi("ui/Login/Login.ui")
        self.login.err.setVisible(False)
        self.modify_layout()
        self.user = Users()
        self.json = dbJson("users.json")
        self.timer2 = QtCore.QTimer()
        #self.login.err.setVisible(True)
        self.timer2.timeout.connect(self.closeApp)
    
    def setup_connexion(self):
        self.setCtgStructInLogin()
        self.login.connect.clicked.connect(self.connexion)
        self.timer2.start(40)


    def modify_layout(self):
        self.login.setWindowTitle("Connexion")
        self.login.connect.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=2, yOffset=2, color=QtGui.QColor(0, 0, 0, 10)))
        self.login.widget_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=2, color=QtGui.QColor(0, 0, 0, 10)))

    def connexion(self):
        jour = f"{time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year} {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}"
        name = self.login.lineEdit.text()
        ctgStruct = self.login.ctgStruct.currentData()
        ctgStructName = self.login.ctgStruct.currentText()
        password = self.login.lineEdit_2.text()
        self.setStructType(ctgStructName)

        if name == "diocese" and password == "1234":
            self.json.createJson({
                "login": name, 
                "password":"**********:)",
                "privilege": "admin",
                "ctgStruct": ctgStruct,
                "ctgStructName": ctgStructName,
                "lastLogin": jour
                },
                True
            )
            self.login.lineEdit.setText("")
            self.login.lineEdit_2.setText("")

            self.main.userName.setText(name)
            self.main.lastLogin.setText(jour)
            self.login.close()
            self.main.show()
            self.settingsVisibility()
        else:
            self.timer = QtCore.QTimer()
            self.login.err.setVisible(True)
            self.timer.timeout.connect(self.closeErr)
            self.timer.start(40)

    def closeErr(self):
        global count
        if count > 50:
            self.timer.stop()
            self.login.err.setVisible(False)
            count = 0
        count += 1

    def closeApp(self):
        global count2
        if count > 50:
            self.timer2.stop()
            self.login.close()
            count2 = 0
        count2 += 1
    
    def setCtgStructInLogin(self):
        allCtgStruct = self.ctgStruct.getCategories()
        for struct in allCtgStruct:
            self.login.ctgStruct.addItem(struct[1], struct[0])
    
    def setStructType(self, typeStruct=""):
        self.main.structType.setText(typeStruct)
    
    def settingsVisibility(self):
        structType = self.json.getJson("users.json").get("ctgStruct")
        if not int(structType) == 1:
            self.versementPage.versementCasuelBtn.setVisible(False)
        else:
            self.versementPage.versementCasuelBtn.setVisible(True)