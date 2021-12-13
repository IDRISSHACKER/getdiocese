# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 635)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    color: rgb(10, 114, 189);\n"
"    color: #000;\n"
"    border: none\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: #f0f3f5\n"
"}\n"
"\n"
"#leftMenu{\n"
"    background-color: #0a72bd;\n"
"    max-width: 250px\n"
"}\n"
"\n"
"#search{\n"
"    background: transparent;\n"
"}\n"
"\n"
"#searchFrame{\n"
"    border-radius: 8px;\n"
"    border: 2px solid #0a72bd;\n"
"}\n"
"\n"
"#menuLabel{\n"
"    color: #0a72bd\n"
"}\n"
"\n"
"#card1_3, #card2_3, #card3_3, #card4_3{\n"
"    background: #fff;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#headerFrame{\n"
"    background: #fff;\n"
"}\n"
"\n"
"#dashboardBtn, #structureBtn, #serviceBtn, #versementBtn, #compteBtn, #zoneBtn, #budgetBtn, #categorieBtn, #settingsBtn{\n"
"    color: #fff;\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"    border-radius: 6px;\n"
"    width: 200px\n"
"}\n"
"\n"
"#dashboardBtn:hover, #structureBtn:hover, #serviceBtn:hover, #versementBtn:hover, #compteBtn:hover, #zoneBtn:hover, #budgetBtn:hover, #categorieBtn:hover,#settingsBtn:hover{\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    transition: all linear 0.3s;\n"
"}\n"
"#dashboardBtn{\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    transition: all linear 0.3s;\n"
"}\n"
"\n"
"#profileCont{\n"
"    background: #fff;\n"
"    border-radius: 8px\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenu.sizePolicy().hasHeightForWidth())
        self.leftMenu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.leftMenu.setFont(font)
        self.leftMenu.setStyleSheet("")
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_10.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_9 = QtWidgets.QFrame(self.leftMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(30)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_23 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_16.addWidget(self.label_23, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_11.addWidget(self.frame_10, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.dashboardBtn = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboardBtn.sizePolicy().hasHeightForWidth())
        self.dashboardBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.dashboardBtn.setFont(font)
        self.dashboardBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dashboardBtn.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../static/asset/icons/white/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboardBtn.setIcon(icon)
        self.dashboardBtn.setIconSize(QtCore.QSize(25, 25))
        self.dashboardBtn.setObjectName("dashboardBtn")
        self.verticalLayout_9.addWidget(self.dashboardBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.structureBtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.structureBtn.setFont(font)
        self.structureBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.structureBtn.setAutoFillBackground(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../static/asset/icons/white/box.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.structureBtn.setIcon(icon1)
        self.structureBtn.setIconSize(QtCore.QSize(25, 25))
        self.structureBtn.setObjectName("structureBtn")
        self.verticalLayout_9.addWidget(self.structureBtn, 0, QtCore.Qt.AlignLeft)
        self.serviceBtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.serviceBtn.setFont(font)
        self.serviceBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../static/asset/icons/white/server.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.serviceBtn.setIcon(icon2)
        self.serviceBtn.setIconSize(QtCore.QSize(25, 25))
        self.serviceBtn.setObjectName("serviceBtn")
        self.verticalLayout_9.addWidget(self.serviceBtn, 0, QtCore.Qt.AlignLeft)
        self.versementBtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.versementBtn.setFont(font)
        self.versementBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../static/asset/icons/white/credit-card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.versementBtn.setIcon(icon3)
        self.versementBtn.setIconSize(QtCore.QSize(25, 25))
        self.versementBtn.setObjectName("versementBtn")
        self.verticalLayout_9.addWidget(self.versementBtn, 0, QtCore.Qt.AlignLeft)
        self.zoneBtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.zoneBtn.setFont(font)
        self.zoneBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../static/asset/icons/white/trello.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoneBtn.setIcon(icon4)
        self.zoneBtn.setIconSize(QtCore.QSize(25, 25))
        self.zoneBtn.setObjectName("zoneBtn")
        self.verticalLayout_9.addWidget(self.zoneBtn)
        self.budgetBtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.budgetBtn.setFont(font)
        self.budgetBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../static/asset/icons/white/trending-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.budgetBtn.setIcon(icon5)
        self.budgetBtn.setIconSize(QtCore.QSize(25, 25))
        self.budgetBtn.setObjectName("budgetBtn")
        self.verticalLayout_9.addWidget(self.budgetBtn)
        self.categorieBtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.categorieBtn.setFont(font)
        self.categorieBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../static/asset/icons/white/inbox.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.categorieBtn.setIcon(icon6)
        self.categorieBtn.setIconSize(QtCore.QSize(25, 25))
        self.categorieBtn.setObjectName("categorieBtn")
        self.verticalLayout_9.addWidget(self.categorieBtn)
        self.compteBtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.compteBtn.setFont(font)
        self.compteBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../static/asset/icons/white/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.compteBtn.setIcon(icon7)
        self.compteBtn.setIconSize(QtCore.QSize(25, 25))
        self.compteBtn.setObjectName("compteBtn")
        self.verticalLayout_9.addWidget(self.compteBtn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_11.addWidget(self.frame_8, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_9, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_11 = QtWidgets.QFrame(self.leftMenu)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.settingsBtn = QtWidgets.QPushButton(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.settingsBtn.setFont(font)
        self.settingsBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../static/asset/icons/white/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon8)
        self.settingsBtn.setIconSize(QtCore.QSize(25, 25))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_12.addWidget(self.settingsBtn)
        self.verticalLayout_10.addWidget(self.frame_11, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.leftMenu)
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu = QtWidgets.QWidget(self.headerFrame)
        self.menu.setObjectName("menu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.menu)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuBtn = QtWidgets.QPushButton(self.menu)
        self.menuBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../static/asset/icons/blue/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon9)
        self.menuBtn.setIconSize(QtCore.QSize(32, 32))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_3.addWidget(self.menuBtn)
        self.menuLabel = QtWidgets.QLabel(self.menu)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.menuLabel.setFont(font)
        self.menuLabel.setObjectName("menuLabel")
        self.horizontalLayout_3.addWidget(self.menuLabel)
        self.horizontalLayout_2.addWidget(self.menu, 0, QtCore.Qt.AlignLeft)
        self.widget_3 = QtWidgets.QWidget(self.headerFrame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.searchFrame = QtWidgets.QFrame(self.widget_3)
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.searchFrame)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../static/asset/icons/blue/search.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.search = QtWidgets.QLineEdit(self.searchFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.horizontalLayout_4.addWidget(self.search)
        self.horizontalLayout_5.addWidget(self.searchFrame)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.account = QtWidgets.QWidget(self.headerFrame)
        self.account.setStyleSheet("border-left:solid 1px #ddd")
        self.account.setObjectName("account")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.account)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.accountBtn = QtWidgets.QPushButton(self.account)
        self.accountBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../static/asset/icons/blue/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountBtn.setIcon(icon10)
        self.accountBtn.setIconSize(QtCore.QSize(34, 34))
        self.accountBtn.setObjectName("accountBtn")
        self.horizontalLayout_6.addWidget(self.accountBtn)
        self.horizontalLayout_2.addWidget(self.account, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignTop)
        self.pages = QtWidgets.QStackedWidget(self.mainBody)
        self.pages.setObjectName("pages")
        self.dashboard = QtWidgets.QWidget()
        self.dashboard.setObjectName("dashboard")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dashboard)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.framePages = QtWidgets.QFrame(self.dashboard)
        self.framePages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePages.setObjectName("framePages")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.framePages)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.cardsFrame_3 = QtWidgets.QWidget(self.framePages)
        self.cardsFrame_3.setObjectName("cardsFrame_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.cardsFrame_3)
        self.horizontalLayout_11.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.card1_3 = QtWidgets.QFrame(self.cardsFrame_3)
        self.card1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1_3.setObjectName("card1_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.card1_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.card1_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_22.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMaximumSize(QtCore.QSize(40, 40))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../static/asset/icons/blue/package.svg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_22.addWidget(self.label_9)
        self.verticalLayout_4.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.label_10 = QtWidgets.QLabel(self.card1_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_11.addWidget(self.card1_3, 0, QtCore.Qt.AlignTop)
        self.card2_3 = QtWidgets.QFrame(self.cardsFrame_3)
        self.card2_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2_3.setObjectName("card2_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.card2_3)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_15 = QtWidgets.QFrame(self.card2_3)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_33 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_23.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.frame_15)
        self.label_34.setMaximumSize(QtCore.QSize(40, 40))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("../static/asset/icons/blue/credit-card.svg"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_23.addWidget(self.label_34, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_17.addWidget(self.frame_15)
        self.label_35 = QtWidgets.QLabel(self.card2_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_17.addWidget(self.label_35)
        self.horizontalLayout_11.addWidget(self.card2_3)
        self.card3_3 = QtWidgets.QFrame(self.cardsFrame_3)
        self.card3_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card3_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card3_3.setObjectName("card3_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.card3_3)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_16 = QtWidgets.QFrame(self.card3_3)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_36 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_24.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.frame_16)
        self.label_37.setMaximumSize(QtCore.QSize(40, 40))
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap("../static/asset/icons/blue/sliders.svg"))
        self.label_37.setScaledContents(True)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_24.addWidget(self.label_37, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_18.addWidget(self.frame_16)
        self.label_38 = QtWidgets.QLabel(self.card3_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_18.addWidget(self.label_38)
        self.horizontalLayout_11.addWidget(self.card3_3)
        self.card4_3 = QtWidgets.QFrame(self.cardsFrame_3)
        self.card4_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card4_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card4_3.setObjectName("card4_3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.card4_3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_17 = QtWidgets.QFrame(self.card4_3)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_39 = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_25.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.frame_17)
        self.label_40.setMaximumSize(QtCore.QSize(40, 40))
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap("../static/asset/icons/blue/users.svg"))
        self.label_40.setScaledContents(True)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_25.addWidget(self.label_40, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_19.addWidget(self.frame_17)
        self.label_41 = QtWidgets.QLabel(self.card4_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_19.addWidget(self.label_41)
        self.horizontalLayout_11.addWidget(self.card4_3)
        self.verticalLayout_20.addWidget(self.cardsFrame_3)
        self.mainFraime_3 = QtWidgets.QWidget(self.framePages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFraime_3.sizePolicy().hasHeightForWidth())
        self.mainFraime_3.setSizePolicy(sizePolicy)
        self.mainFraime_3.setObjectName("mainFraime_3")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.mainFraime_3)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.widget_6 = QtWidgets.QWidget(self.mainFraime_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_21.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.mainFraime_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_21.addWidget(self.widget_7)
        self.verticalLayout_20.addWidget(self.mainFraime_3)
        self.verticalLayout_5.addWidget(self.framePages)
        self.pages.addWidget(self.dashboard)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pages.addWidget(self.page_3)
        self.structure = QtWidgets.QWidget()
        self.structure.setStyleSheet("#tableData{\n"
"    background: white;\n"
"    borde-radius: 4px\n"
"}\n"
"\n"
"#actions{\n"
"    background: white;\n"
"    borde-radius: 4px\n"
"}")
        self.structure.setObjectName("structure")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.structure)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.tableData = QtWidgets.QWidget(self.structure)
        self.tableData.setObjectName("tableData")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.tableData)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.structTable = QtWidgets.QTableWidget(self.tableData)
        self.structTable.setObjectName("structTable")
        self.structTable.setColumnCount(0)
        self.structTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.structTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.structTable.setVerticalHeaderItem(1, item)
        self.horizontalLayout_27.addWidget(self.structTable)
        self.horizontalLayout_26.addWidget(self.tableData)
        self.actions = QtWidgets.QWidget(self.structure)
        self.actions.setObjectName("actions")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.actions)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_11 = QtWidgets.QLabel(self.actions)
        self.label_11.setMaximumSize(QtCore.QSize(300, 230))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../static/asset/svg/undraw_ordinary_day_re_v5hy.svg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_21.addWidget(self.label_11)
        self.addStruct = QtWidgets.QPushButton(self.actions)
        font = QtGui.QFont()
        font.setFamily("GeForce")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addStruct.setFont(font)
        self.addStruct.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addStruct.setStyleSheet("#addStruct{\n"
"    background: rgb(10, 114, 189, 0.02);\n"
"    color: rgb(10, 114, 189);\n"
"    border-radius:4px;\n"
"    padding: 15px\n"
"}\n"
"\n"
"#addStruct:hover{\n"
"    background: rgb(10, 114, 189, 0.3);\n"
"    color: rgb(10, 114, 189);\n"
"    border-radius:4px\n"
"}\n"
"")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../static/asset/icons/blue/copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addStruct.setIcon(icon11)
        self.addStruct.setIconSize(QtCore.QSize(25, 25))
        self.addStruct.setObjectName("addStruct")
        self.verticalLayout_21.addWidget(self.addStruct)
        self.horizontalLayout_26.addWidget(self.actions)
        self.pages.addWidget(self.structure)
        self.verticalLayout.addWidget(self.pages)
        self.horizontalLayout.addWidget(self.mainBody)
        self.profileCont = QtWidgets.QWidget(self.centralwidget)
        self.profileCont.setObjectName("profileCont")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.profileCont)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout.addWidget(self.profileCont, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_23.setText(_translate("MainWindow", "EgliseGestion"))
        self.dashboardBtn.setText(_translate("MainWindow", "Dashboard"))
        self.structureBtn.setText(_translate("MainWindow", "Structure"))
        self.serviceBtn.setText(_translate("MainWindow", "Service"))
        self.versementBtn.setText(_translate("MainWindow", "Versement"))
        self.zoneBtn.setText(_translate("MainWindow", "Zone"))
        self.budgetBtn.setText(_translate("MainWindow", "Budget"))
        self.categorieBtn.setText(_translate("MainWindow", "Categorie"))
        self.compteBtn.setText(_translate("MainWindow", "Compte"))
        self.settingsBtn.setText(_translate("MainWindow", "Parametre"))
        self.menuLabel.setText(_translate("MainWindow", "Dashboard"))
        self.search.setPlaceholderText(_translate("MainWindow", "Effectuer une recherche"))
        self.label_8.setText(_translate("MainWindow", "12"))
        self.label_10.setText(_translate("MainWindow", "Structure"))
        self.label_33.setText(_translate("MainWindow", "200.000 FCFA"))
        self.label_35.setText(_translate("MainWindow", "Compte"))
        self.label_36.setText(_translate("MainWindow", "57"))
        self.label_38.setText(_translate("MainWindow", "Services"))
        self.label_39.setText(_translate("MainWindow", "89"))
        self.label_41.setText(_translate("MainWindow", "utilisateurs"))
        self.addStruct.setText(_translate("MainWindow", "Ajouter une structure"))
import ressources_rc
