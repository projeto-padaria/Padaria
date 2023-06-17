# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import icons__rc

class Ui_MainWindowLogin(object):
    def setupUi(self, MainWindowLogin):
        if not MainWindowLogin.objectName():
            MainWindowLogin.setObjectName(u"MainWindowLogin")
        MainWindowLogin.resize(360, 360)
        MainWindowLogin.setMinimumSize(QSize(360, 360))
        MainWindowLogin.setMaximumSize(QSize(360, 360))
        MainWindowLogin.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindowLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(350, 360))
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, 9, 9)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(330, 300))
        self.frame.setMaximumSize(QSize(330, 300))
        self.frame.setStyleSheet(u"background-color:rgb(49, 49, 49);\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(215, 100))
        self.frame_2.setMaximumSize(QSize(315, 100))
        self.frame_2.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: white;\n"
"border: None;\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS SHel Dlg 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:rgb(49, 49, 49)\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_Usuario = QLabel(self.frame_2)
        self.lbl_Usuario.setObjectName(u"lbl_Usuario")
        self.lbl_Usuario.setMinimumSize(QSize(280, 10))
        self.lbl_Usuario.setMaximumSize(QSize(300, 100))
        font = QFont()
        font.setPointSize(10)
        self.lbl_Usuario.setFont(font)
        self.lbl_Usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_Usuario, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.txtLogin = QLineEdit(self.frame_2)
        self.txtLogin.setObjectName(u"txtLogin")
        self.txtLogin.setMinimumSize(QSize(280, 25))
        self.txtLogin.setMaximumSize(QSize(300, 25))
        font1 = QFont()
        font1.setFamilies([u"MS SHel Dlg 2"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.txtLogin.setFont(font1)
        self.txtLogin.setStyleSheet(u"")
        self.txtLogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.txtLogin)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(215, 100))
        self.frame_3.setMaximumSize(QSize(315, 100))
        self.frame_3.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: white;\n"
"border: None;\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS SHel Dlg 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:rgb(49, 49, 49)\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_Senha = QLabel(self.frame_3)
        self.lbl_Senha.setObjectName(u"lbl_Senha")
        self.lbl_Senha.setMinimumSize(QSize(280, 25))
        self.lbl_Senha.setMaximumSize(QSize(300, 25))
        self.lbl_Senha.setFont(font)

        self.verticalLayout_3.addWidget(self.lbl_Senha)

        self.txtSenha = QLineEdit(self.frame_3)
        self.txtSenha.setObjectName(u"txtSenha")
        self.txtSenha.setMinimumSize(QSize(280, 25))
        self.txtSenha.setMaximumSize(QSize(300, 25))
        self.txtSenha.setFont(font1)
        self.txtSenha.setStyleSheet(u"")
        self.txtSenha.setEchoMode(QLineEdit.Password)
        self.txtSenha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txtSenha)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(215, 50))
        self.frame_4.setMaximumSize(QSize(315, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnLogin = QPushButton(self.frame_4)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMaximumSize(QSize(200, 100))
        font2 = QFont()
        font2.setPointSize(12)
        self.btnLogin.setFont(font2)
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:black;\n"
"background-color: rgb(203, 135, 0);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.btnLogin)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindowLogin.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowLogin)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowLogin.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowLogin)

        QMetaObject.connectSlotsByName(MainWindowLogin)
    # setupUi

    def retranslateUi(self, MainWindowLogin):
        MainWindowLogin.setWindowTitle(QCoreApplication.translate("MainWindowLogin", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindowLogin", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/login.png\"/></p></body></html>", None))
        self.lbl_Usuario.setText(QCoreApplication.translate("MainWindowLogin", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Usu\u00e1rio</span></p></body></html>", None))
        self.txtLogin.setPlaceholderText(QCoreApplication.translate("MainWindowLogin", u"CPF", None))
        self.lbl_Senha.setText(QCoreApplication.translate("MainWindowLogin", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Senha</span></p></body></html>", None))
        self.txtSenha.setPlaceholderText(QCoreApplication.translate("MainWindowLogin", u"Senha", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindowLogin", u"LOGIN", None))
    # retranslateUi

