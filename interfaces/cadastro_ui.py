# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QToolButton, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import icons__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1019, 613)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setStyleSheet(u"*{\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"color:White;\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.leftContainer = QFrame(self.centralwidget)
        self.leftContainer.setObjectName(u"leftContainer")
        self.leftContainer.setMaximumSize(QSize(200, 16777215))
        self.leftContainer.setFrameShape(QFrame.StyledPanel)
        self.leftContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.leftContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 9)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"QToolBox{\n"
"text-align: left;\n"
"color: white;\n"
"}\n"
"\n"
"QToolBox:tab{\n"
"border-radius: 5px;\n"
"background-color:rgb(49, 49, 49);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 0, -1)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        font = QFont()
        font.setBold(True)
        self.toolBox.setFont(font)
        self.toolBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBox.setStyleSheet(u"QPushButton{\n"
"color:White;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(71, 71, 71);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 182, 500))
        self.page.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnHome = QPushButton(self.page)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.btnHome.setFont(font1)
        self.btnHome.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnHome)

        self.btnVenda = QPushButton(self.page)
        self.btnVenda.setObjectName(u"btnVenda")
        self.btnVenda.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.btnVenda.setFont(font2)
        self.btnVenda.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnVenda)

        self.btnCadastrar = QPushButton(self.page)
        self.btnCadastrar.setObjectName(u"btnCadastrar")
        self.btnCadastrar.setMinimumSize(QSize(0, 30))
        self.btnCadastrar.setFont(font1)
        self.btnCadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnCadastrar)

        self.btnContatos = QPushButton(self.page)
        self.btnContatos.setObjectName(u"btnContatos")
        self.btnContatos.setMinimumSize(QSize(0, 30))
        self.btnContatos.setFont(font1)
        self.btnContatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnContatos)

        self.btnSobre = QPushButton(self.page)
        self.btnSobre.setObjectName(u"btnSobre")
        self.btnSobre.setMinimumSize(QSize(0, 30))
        self.btnSobre.setFont(font1)
        self.btnSobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnSobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"MENU")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 182, 500))
        self.page_2.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_13 = QVBoxLayout(self.page_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(85, 50))
        self.label_4.setMaximumSize(QSize(170, 100))

        self.verticalLayout_13.addWidget(self.label_4)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(85, 50))
        self.label_5.setMaximumSize(QSize(170, 100))

        self.verticalLayout_13.addWidget(self.label_5)

        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 50))
        self.label_12.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_13.addWidget(self.label_12)

        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 50))
        self.label_13.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_13.addWidget(self.label_13)

        self.toolBox.addItem(self.page_2, u"SISTEMA")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.leftContainer)

        self.mainContainer = QFrame(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setFrameShape(QFrame.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.topFrame = QFrame(self.mainContainer)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btinToggle = QPushButton(self.topFrame)
        self.btinToggle.setObjectName(u"btinToggle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btinToggle.setIcon(icon)
        self.btinToggle.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btinToggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.topFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.topFrame)

        self.mainFrame = QFrame(self.mainContainer)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setStyleSheet(u"background-color: rgb(71, 71, 71);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, -1)
        self.Pages = QStackedWidget(self.mainFrame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"")
        self.Pages.setLineWidth(1)
        self.pgHome = QWidget()
        self.pgHome.setObjectName(u"pgHome")
        self.verticalLayout_6 = QVBoxLayout(self.pgHome)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lblLogo = QLabel(self.pgHome)
        self.lblLogo.setObjectName(u"lblLogo")

        self.verticalLayout_6.addWidget(self.lblLogo)

        self.Pages.addWidget(self.pgHome)
        self.pgBanco = QWidget()
        self.pgBanco.setObjectName(u"pgBanco")
        self.horizontalLayout_11 = QHBoxLayout(self.pgBanco)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_9 = QFrame(self.pgBanco)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(330, 300))
        self.frame_9.setMaximumSize(QSize(330, 300))
        self.frame_9.setStyleSheet(u"background-color:rgb(49, 49, 49)")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(215, 100))
        self.frame_10.setMaximumSize(QSize(315, 100))
        self.frame_10.setStyleSheet(u"QLabel{\n"
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
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.lbl_Usuario = QLabel(self.frame_10)
        self.lbl_Usuario.setObjectName(u"lbl_Usuario")
        self.lbl_Usuario.setMinimumSize(QSize(280, 25))
        self.lbl_Usuario.setMaximumSize(QSize(300, 25))
        font3 = QFont()
        font3.setPointSize(10)
        self.lbl_Usuario.setFont(font3)
        self.lbl_Usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.lbl_Usuario, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.txtLoginDB = QLineEdit(self.frame_10)
        self.txtLoginDB.setObjectName(u"txtLoginDB")
        self.txtLoginDB.setMinimumSize(QSize(280, 25))
        self.txtLoginDB.setMaximumSize(QSize(300, 25))
        font4 = QFont()
        font4.setFamilies([u"MS SHel Dlg 2"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.txtLoginDB.setFont(font4)
        self.txtLoginDB.setStyleSheet(u"")
        self.txtLoginDB.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.txtLoginDB)


        self.verticalLayout_18.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(215, 100))
        self.frame_11.setMaximumSize(QSize(315, 100))
        self.frame_11.setStyleSheet(u"QLabel{\n"
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
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.lbl_Senha = QLabel(self.frame_11)
        self.lbl_Senha.setObjectName(u"lbl_Senha")
        self.lbl_Senha.setMinimumSize(QSize(280, 25))
        self.lbl_Senha.setMaximumSize(QSize(300, 25))
        self.lbl_Senha.setFont(font3)

        self.verticalLayout_20.addWidget(self.lbl_Senha)

        self.txtSenhaDB = QLineEdit(self.frame_11)
        self.txtSenhaDB.setObjectName(u"txtSenhaDB")
        self.txtSenhaDB.setMinimumSize(QSize(280, 25))
        self.txtSenhaDB.setMaximumSize(QSize(300, 25))
        self.txtSenhaDB.setFont(font4)
        self.txtSenhaDB.setStyleSheet(u"")
        self.txtSenhaDB.setEchoMode(QLineEdit.Password)
        self.txtSenhaDB.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.txtSenhaDB)


        self.verticalLayout_18.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(215, 50))
        self.frame_12.setMaximumSize(QSize(315, 100))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnLoginBD = QPushButton(self.frame_12)
        self.btnLoginBD.setObjectName(u"btnLoginBD")
        self.btnLoginBD.setMaximumSize(QSize(200, 100))
        font5 = QFont()
        font5.setPointSize(12)
        self.btnLoginBD.setFont(font5)
        self.btnLoginBD.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLoginBD.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_7.addWidget(self.btnLoginBD)


        self.verticalLayout_18.addWidget(self.frame_12, 0, Qt.AlignHCenter)

        self.lblAviso = QLabel(self.frame_9)
        self.lblAviso.setObjectName(u"lblAviso")
        self.lblAviso.setMinimumSize(QSize(215, 10))
        self.lblAviso.setMaximumSize(QSize(315, 100))
        self.lblAviso.setStyleSheet(u"text-align: center;\n"
"")

        self.verticalLayout_18.addWidget(self.lblAviso, 0, Qt.AlignHCenter)


        self.horizontalLayout_11.addWidget(self.frame_9)

        self.Pages.addWidget(self.pgBanco)
        self.pgVenda = QWidget()
        self.pgVenda.setObjectName(u"pgVenda")
        self.verticalLayout_16 = QVBoxLayout(self.pgVenda)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_pesquisa = QFrame(self.pgVenda)
        self.frame_pesquisa.setObjectName(u"frame_pesquisa")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_pesquisa.sizePolicy().hasHeightForWidth())
        self.frame_pesquisa.setSizePolicy(sizePolicy2)
        self.frame_pesquisa.setMinimumSize(QSize(0, 0))
        self.frame_pesquisa.setMaximumSize(QSize(800, 800))
        self.frame_pesquisa.setFrameShape(QFrame.StyledPanel)
        self.frame_pesquisa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_pesquisa)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_6 = QFrame(self.frame_pesquisa)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.l_F3Key = QLabel(self.frame_6)
        self.l_F3Key.setObjectName(u"l_F3Key")
        font6 = QFont()
        font6.setPointSize(8)
        self.l_F3Key.setFont(font6)

        self.horizontalLayout_8.addWidget(self.l_F3Key)

        self.l_F2Key = QLabel(self.frame_6)
        self.l_F2Key.setObjectName(u"l_F2Key")
        self.l_F2Key.setFont(font6)

        self.horizontalLayout_8.addWidget(self.l_F2Key)


        self.verticalLayout_15.addWidget(self.frame_6)

        self.gb_pesquisa = QGroupBox(self.frame_pesquisa)
        self.gb_pesquisa.setObjectName(u"gb_pesquisa")
        sizePolicy2.setHeightForWidth(self.gb_pesquisa.sizePolicy().hasHeightForWidth())
        self.gb_pesquisa.setSizePolicy(sizePolicy2)
        self.gb_pesquisa.setMaximumSize(QSize(800, 600))
        self.horizontalLayout_9 = QHBoxLayout(self.gb_pesquisa)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_7 = QFrame(self.gb_pesquisa)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.l_title = QLabel(self.frame_7)
        self.l_title.setObjectName(u"l_title")
        self.l_title.setMinimumSize(QSize(66, 22))
        self.l_title.setMaximumSize(QSize(66, 22))
        font7 = QFont()
        font7.setPointSize(13)
        self.l_title.setFont(font7)

        self.horizontalLayout_10.addWidget(self.l_title)

        self.le_produto = QLineEdit(self.frame_7)
        self.le_produto.setObjectName(u"le_produto")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.le_produto.sizePolicy().hasHeightForWidth())
        self.le_produto.setSizePolicy(sizePolicy3)
        self.le_produto.setMinimumSize(QSize(350, 22))
        self.le_produto.setMaximumSize(QSize(350, 22))

        self.horizontalLayout_10.addWidget(self.le_produto)


        self.horizontalLayout_9.addWidget(self.frame_7)

        self.toolButton = QToolButton(self.gb_pesquisa)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy2.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy2)
        self.toolButton.setMinimumSize(QSize(50, 22))
        self.toolButton.setMaximumSize(QSize(22, 22))
        self.toolButton.setPopupMode(QToolButton.InstantPopup)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(False)

        self.horizontalLayout_9.addWidget(self.toolButton)


        self.verticalLayout_15.addWidget(self.gb_pesquisa)


        self.verticalLayout_16.addWidget(self.frame_pesquisa)

        self.line = QFrame(self.pgVenda)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line)

        self.frame_carinhoCompra = QFrame(self.pgVenda)
        self.frame_carinhoCompra.setObjectName(u"frame_carinhoCompra")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_carinhoCompra.sizePolicy().hasHeightForWidth())
        self.frame_carinhoCompra.setSizePolicy(sizePolicy4)
        self.frame_carinhoCompra.setFrameShape(QFrame.StyledPanel)
        self.frame_carinhoCompra.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_carinhoCompra)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gb_carrinhoCompra = QGroupBox(self.frame_carinhoCompra)
        self.gb_carrinhoCompra.setObjectName(u"gb_carrinhoCompra")
        self.gb_carrinhoCompra.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_17 = QVBoxLayout(self.gb_carrinhoCompra)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")

        self.verticalLayout_14.addWidget(self.gb_carrinhoCompra)

        self.treeWidget = QTreeWidget(self.frame_carinhoCompra)
        self.treeWidget.headerItem().setText(7, "")
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(0, 300))
        self.treeWidget.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_14.addWidget(self.treeWidget)


        self.verticalLayout_16.addWidget(self.frame_carinhoCompra)

        self.Pages.addWidget(self.pgVenda)
        self.pgCadastrar = QWidget()
        self.pgCadastrar.setObjectName(u"pgCadastrar")
        self.pgCadastrar.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.pgCadastrar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(self.pgCadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy5)
        font8 = QFont()
        font8.setKerning(True)
        font8.setStyleStrategy(QFont.PreferDefault)
        self.tabWidget.setFont(font8)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setUsesScrollButtons(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"color: white;\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS SHel Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:rgb(49, 49, 49);\n"
"border:None;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txtNome = QLineEdit(self.frame_4)
        self.txtNome.setObjectName(u"txtNome")
        self.txtNome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtNome, 1, 1, 1, 1)

        self.lblCadastroFun = QLabel(self.frame_4)
        self.lblCadastroFun.setObjectName(u"lblCadastroFun")

        self.gridLayout.addWidget(self.lblCadastroFun, 0, 0, 1, 3)

        self.txtSobrenome = QLineEdit(self.frame_4)
        self.txtSobrenome.setObjectName(u"txtSobrenome")
        self.txtSobrenome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtSobrenome, 1, 2, 1, 1)

        self.txtCPF = QLineEdit(self.frame_4)
        self.txtCPF.setObjectName(u"txtCPF")
        self.txtCPF.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtCPF, 1, 0, 1, 1)

        self.txtCargo = QLineEdit(self.frame_4)
        self.txtCargo.setObjectName(u"txtCargo")
        self.txtCargo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtCargo, 2, 1, 1, 1)

        self.txtSenha = QLineEdit(self.frame_4)
        self.txtSenha.setObjectName(u"txtSenha")
        self.txtSenha.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtSenha, 2, 0, 1, 1)

        self.txtSalario = QLineEdit(self.frame_4)
        self.txtSalario.setObjectName(u"txtSalario")
        self.txtSalario.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtSalario, 2, 2, 1, 1)

        self.txtTelefone = QLineEdit(self.frame_4)
        self.txtTelefone.setObjectName(u"txtTelefone")
        self.txtTelefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtTelefone, 4, 0, 1, 1)

        self.txtMunicipio = QLineEdit(self.frame_4)
        self.txtMunicipio.setObjectName(u"txtMunicipio")
        self.txtMunicipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtMunicipio, 4, 2, 1, 1)

        self.txtBairro = QLineEdit(self.frame_4)
        self.txtBairro.setObjectName(u"txtBairro")
        self.txtBairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtBairro, 4, 1, 1, 1)

        self.txtLogradouro = QLineEdit(self.frame_4)
        self.txtLogradouro.setObjectName(u"txtLogradouro")
        self.txtLogradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtLogradouro, 5, 0, 1, 2)

        self.txtUF = QLineEdit(self.frame_4)
        self.txtUF.setObjectName(u"txtUF")
        self.txtUF.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtUF, 6, 0, 1, 1)

        self.txtCEP = QLineEdit(self.frame_4)
        self.txtCEP.setObjectName(u"txtCEP")
        self.txtCEP.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtCEP, 6, 1, 1, 1)

        self.txtNumero = QLineEdit(self.frame_4)
        self.txtNumero.setObjectName(u"txtNumero")
        self.txtNumero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtNumero, 5, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.btnCadastrarFun = QPushButton(self.tab)
        self.btnCadastrarFun.setObjectName(u"btnCadastrarFun")
        self.btnCadastrarFun.setMinimumSize(QSize(160, 20))
        self.btnCadastrarFun.setFont(font3)
        self.btnCadastrarFun.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCadastrarFun.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(0, 129, 0);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"border-radius: 5px;	\n"
"background-color:rgb(49, 49, 49);\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.btnCadastrarFun, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setStyleSheet(u"border:None;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 9, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"background-color: rgb(148,148,148);\n"
"color: white;\n"
"font: 10pt \"MS SHell Slg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(49, 49, 49);\n"
"}")

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border-radius: 5px;	\n"
"background-color:rgb(49, 49, 49);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"\n"
"QFrame{\n"
"background-color:rgb(49, 49, 49);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_excel = QPushButton(self.frame_8)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 141, 0);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_excel)

        self.btnAlterar = QPushButton(self.frame_8)
        self.btnAlterar.setObjectName(u"btnAlterar")
        self.btnAlterar.setMinimumSize(QSize(120, 30))
        self.btnAlterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAlterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(206, 137, 0)\n"
"}")

        self.verticalLayout_7.addWidget(self.btnAlterar)

        self.btnExcluir = QPushButton(self.frame_8)
        self.btnExcluir.setObjectName(u"btnExcluir")
        self.btnExcluir.setMinimumSize(QSize(120, 30))
        self.btnExcluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExcluir.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(182, 0, 0);\n"
"}")

        self.verticalLayout_7.addWidget(self.btnExcluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_8)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pgCadastrar)
        self.pgContatos = QWidget()
        self.pgContatos.setObjectName(u"pgContatos")
        self.verticalLayout_10 = QVBoxLayout(self.pgContatos)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.pgContatos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_10.addWidget(self.label_7)

        self.frame_5 = QFrame(self.pgContatos)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_12.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_12.addWidget(self.label_9)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.Pages.addWidget(self.pgContatos)
        self.pgSobre = QWidget()
        self.pgSobre.setObjectName(u"pgSobre")
        self.verticalLayout_11 = QVBoxLayout(self.pgSobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.pgSobre)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_11 = QLabel(self.pgSobre)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_11)

        self.Pages.addWidget(self.pgSobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.mainFrame)

        self.footerFrame = QFrame(self.mainContainer)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footerFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footerFrame)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Imperador dos P\u00e3es </span></p></body></html>", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnVenda.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.btnCadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btnContatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btnSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Usu\u00e1rio: </span>Funcion\u00e1rio</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Sistema:</span> Cadastro Funcion\u00e1rio</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Status:</span> Ativo </p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Vencimento:</span> 18/80/5260</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"SISTEMA", None))
        self.btinToggle.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">Sistema Gest\u00e3o</span><br/></p></body></html>", None))
        self.lblLogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/padaria.png\"/></p></body></html>", None))
        self.lbl_Usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Banco de Dados</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.txtLoginDB.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.lbl_Senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Senha</span></p></body></html>", None))
        self.txtSenhaDB.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.btnLoginBD.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.lblAviso.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.l_F3Key.setText(QCoreApplication.translate("MainWindow", u" F3 - Quantidade", None))
        self.l_F2Key.setText(QCoreApplication.translate("MainWindow", u" F2 - Pesquisa Produto", None))
        self.gb_pesquisa.setTitle(QCoreApplication.translate("MainWindow", u"Pesquisa de Produto", None))
        self.l_title.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gb_carrinhoCompra.setTitle(QCoreApplication.translate("MainWindow", u"Carrinho de compra", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Data de Validade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Data de Emiss\u00e3o", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Marca do Produto", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Nome do Produto", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"idVenda", None));
        self.txtNome.setText("")
        self.txtNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME ", None))
        self.lblCadastroFun.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CADASTRO</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">FUNCION\u00c1RIO</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.txtSobrenome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SOBRENOME", None))
        self.txtCPF.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txtCargo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CARGO", None))
        self.txtSenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SENHA", None))
        self.txtSalario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SAL\u00c1RIO", None))
        self.txtTelefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txtMunicipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None))
        self.txtBairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.txtLogradouro.setText("")
        self.txtLogradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.txtUF.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txtCEP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txtNumero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.btnCadastrarFun.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Funcion\u00e1rio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Realizar Cadastro ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"SOBRENOME", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SENHA", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CARGO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"SAL\u00c1RIO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btnAlterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Funcion\u00e1rios Cadastrados", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CONTATOS</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/whatsApp.png\" />   <span style=\" font-size:18pt; vertical-align:super;\">(xx)9xxxx-xxxx</span><span style=\" font-size:11pt;\"><br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/email.png\" />    <span style=\" font-size:18pt; vertical-align:super;\">@gmail.com</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/Youtube.png\" />   <span style=\" font-size:18pt; vertical-align:super;\">YouTube</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TEXTAO</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">\u00a9Imperador dos P\u00e3es 2023</span></p></body></html>", None))
    # retranslateUi

