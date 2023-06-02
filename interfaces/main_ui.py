# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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

class Ui_window_login(object):
    def setupUi(self, window_login):
        if not window_login.objectName():
            window_login.setObjectName(u"window_login")
        window_login.resize(350, 350)
        window_login.setMinimumSize(QSize(350, 350))
        window_login.setMaximumSize(QSize(350, 350))
        font = QFont()
        font.setFamilies([u"Consolas"])
        window_login.setFont(font)
        self.centralwidget = QWidget(window_login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_login = QFrame(self.centralwidget)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMaximumSize(QSize(350, 350))
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_login)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.l_login = QLabel(self.frame_login)
        self.l_login.setObjectName(u"l_login")
        self.l_login.setMinimumSize(QSize(0, 25))
        self.l_login.setMaximumSize(QSize(750, 15))
        self.l_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.l_login)

        self.le_login = QLineEdit(self.frame_login)
        self.le_login.setObjectName(u"le_login")
        self.le_login.setStyleSheet(u"QLineEdit {\n"
"	padding: 3px;\n"
"	border-radius: 3px;\n"
"}")

        self.verticalLayout_4.addWidget(self.le_login, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_login, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_frame = QFrame(self.centralwidget)
        self.frame_frame.setObjectName(u"frame_frame")
        self.frame_frame.setMaximumSize(QSize(350, 350))
        self.frame_frame.setFrameShape(QFrame.StyledPanel)
        self.frame_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_senha = QLabel(self.frame_frame)
        self.l_senha.setObjectName(u"l_senha")
        self.l_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.l_senha, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.le_Senha = QLineEdit(self.frame_frame)
        self.le_Senha.setObjectName(u"le_Senha")
        self.le_Senha.setMaximumSize(QSize(300, 25))
        self.le_Senha.setStyleSheet(u"QLineEdit {\n"
"	padding: 3px;\n"
"	border-radius: 3px;\n"
"}")
        self.le_Senha.setEchoMode(QLineEdit.Password)
        self.le_Senha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.le_Senha, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_frame)

        self.frame_btn = QFrame(self.centralwidget)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMaximumSize(QSize(350, 350))
        self.frame_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_btn)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cadastrar = QPushButton(self.frame_btn)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMaximumSize(QSize(300, 35))
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"	padding: 8px;\n"
"	border-radius: 3px;\n"
"	background-color: rgb(42, 99, 255);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	cursor: pointer;\n"
"}")
        self.btn_cadastrar.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_cancelar = QPushButton(self.frame_btn)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMaximumSize(QSize(300, 35))
        self.btn_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet(u"QPushButton {\n"
"	padding: 8px;\n"
"	border-radius: 3px;\n"
"	background-color: rgb(42, 99, 255);\n"
"	color: white;\n"
"}")
        self.btn_cancelar.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_cancelar)

        self.btn_entrar = QPushButton(self.frame_btn)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setMaximumSize(QSize(300, 35))
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"QPushButton {\n"
"	padding: 8px;\n"
"	border-radius: 3px;\n"
"	background-color: rgb(97, 200, 255);\n"
"	color: white;\n"
"}")
        self.btn_entrar.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_entrar)

        self.btn_cancelar.raise_()
        self.btn_entrar.raise_()
        self.btn_cadastrar.raise_()

        self.verticalLayout_3.addWidget(self.frame_btn)

        window_login.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(window_login)
        self.statusbar.setObjectName(u"statusbar")
        window_login.setStatusBar(self.statusbar)

        self.retranslateUi(window_login)

        QMetaObject.connectSlotsByName(window_login)
    # setupUi

    def retranslateUi(self, window_login):
        window_login.setWindowTitle(QCoreApplication.translate("window_login", u"MainWindow", None))
        self.l_login.setText(QCoreApplication.translate("window_login", u"Login", None))
        self.l_senha.setText(QCoreApplication.translate("window_login", u"Senha", None))
        self.le_Senha.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("window_login", u"Cadastrar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("window_login", u"Cancelar", None))
        self.btn_entrar.setText(QCoreApplication.translate("window_login", u"Entrar", None))
    # retranslateUi

