from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from App.Api.models.Users import Users

count = 0


class Login:
    def __init__(self, home, main=""):
        super(Login, self).__init__()
        self.home = home
        self.main = main
        self.status = 0
        self.login = loadUi("ui/Login/Login.ui")
        self.login.err.setVisible(False)
        self.modify_layout()
        self.user = Users()

    def setup_connexion(self):
        self.login.connect.clicked.connect(self.connexion)

    def modify_layout(self):
        self.login.setWindowTitle("Connexion")
        self.login.connect.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=2, yOffset=2, color=QtGui.QColor(0, 0, 0, 10)))
        self.login.widget_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=2, color=QtGui.QColor(0, 0, 0, 10)))

    def connexion(self):
        name = self.login.lineEdit.text()
        password = self.login.lineEdit_2.text()

        if name == "diocese" or password == "1234":
            self.login.close()
            self.main.show()
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
