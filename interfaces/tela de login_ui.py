# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela de login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(792, 584)
        font = QFont()
        font.setPointSize(10)
        Login.setFont(font)
        Login.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(200, 110, 441, 421))
        self.frame.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.usuarioButton = QLineEdit(self.frame)
        self.usuarioButton.setObjectName(u"usuarioButton")
        self.usuarioButton.setGeometry(QRect(120, 170, 211, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.usuarioButton.setFont(font1)
        self.usuarioButton.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.usuarioButton.setAlignment(Qt.AlignCenter)
        self.senhaButton = QLineEdit(self.frame)
        self.senhaButton.setObjectName(u"senhaButton")
        self.senhaButton.setGeometry(QRect(120, 230, 211, 20))
        self.senhaButton.setFont(font)
        self.senhaButton.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.senhaButton.setEchoMode(QLineEdit.Password)
        self.senhaButton.setAlignment(Qt.AlignCenter)
        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(120, 300, 221, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.loginButton.setFont(font2)
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginButton.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0, 170, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"\n"
"}")
        self.userIMG = QLabel(self.frame)
        self.userIMG.setObjectName(u"userIMG")
        self.userIMG.setGeometry(QRect(170, 30, 121, 111))
        self.userIMG.setPixmap(QPixmap(u"usuario image.png"))
        self.userIMG.setScaledContents(True)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.usuarioButton.setPlaceholderText(QCoreApplication.translate("Login", u"Usuario", None))
        self.senhaButton.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.loginButton.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.userIMG.setText("")
    # retranslateUi

