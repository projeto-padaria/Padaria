# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela de cadastro.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_TelaDeCadastro(object):
    def setupUi(self, TelaDeCadastro):
        if not TelaDeCadastro.objectName():
            TelaDeCadastro.setObjectName(u"TelaDeCadastro")
        TelaDeCadastro.resize(770, 605)
        self.label = QLabel(TelaDeCadastro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 150, 511, 441))
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(TelaDeCadastro)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 480, 91, 51))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 0);\n"
"\n"
"}")

        self.retranslateUi(TelaDeCadastro)

        QMetaObject.connectSlotsByName(TelaDeCadastro)
    # setupUi

    def retranslateUi(self, TelaDeCadastro):
        TelaDeCadastro.setWindowTitle(QCoreApplication.translate("TelaDeCadastro", u"Dialog", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("TelaDeCadastro", u"cadastrar", None))
    # retranslateUi

