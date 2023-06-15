# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_principalLogin(object):
    def setupUi(self, principalLogin):
        if not principalLogin.objectName():
            principalLogin.setObjectName(u"principalLogin")
        principalLogin.resize(320, 368)
        principalLogin.setMinimumSize(QSize(320, 368))
        principalLogin.setMaximumSize(QSize(320, 368))
        self.centralwidget = QWidget(principalLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_login = QFrame(self.centralwidget)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_login = QLabel(self.frame_login)
        self.l_login.setObjectName(u"l_login")

        self.verticalLayout.addWidget(self.l_login)

        self.le_login = QLineEdit(self.frame_login)
        self.le_login.setObjectName(u"le_login")

        self.verticalLayout.addWidget(self.le_login)


        self.verticalLayout_3.addWidget(self.frame_login)

        self.frame_senha = QFrame(self.centralwidget)
        self.frame_senha.setObjectName(u"frame_senha")
        self.frame_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_senha.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_senha)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.l_senha = QLabel(self.frame_senha)
        self.l_senha.setObjectName(u"l_senha")

        self.verticalLayout_2.addWidget(self.l_senha)

        self.le_senha = QLineEdit(self.frame_senha)
        self.le_senha.setObjectName(u"le_senha")

        self.verticalLayout_2.addWidget(self.le_senha)


        self.verticalLayout_3.addWidget(self.frame_senha)

        self.frame_entrar = QFrame(self.centralwidget)
        self.frame_entrar.setObjectName(u"frame_entrar")
        self.frame_entrar.setFrameShape(QFrame.StyledPanel)
        self.frame_entrar.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_entrar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_entrar = QPushButton(self.frame_entrar)
        self.btn_entrar.setObjectName(u"btn_entrar")

        self.gridLayout.addWidget(self.btn_entrar, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_entrar)

        principalLogin.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(principalLogin)
        self.statusbar.setObjectName(u"statusbar")
        principalLogin.setStatusBar(self.statusbar)

        self.retranslateUi(principalLogin)

        QMetaObject.connectSlotsByName(principalLogin)
    # setupUi

    def retranslateUi(self, principalLogin):
        principalLogin.setWindowTitle(QCoreApplication.translate("principalLogin", u"MainWindow", None))
        self.l_login.setText(QCoreApplication.translate("principalLogin", u"Login", None))
        self.l_senha.setText(QCoreApplication.translate("principalLogin", u"Senha", None))
        self.btn_entrar.setText(QCoreApplication.translate("principalLogin", u"Entrar", None))
    # retranslateUi

