# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_Principal.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1108, 643)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
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
        self.leftContainer.setMaximumSize(QSize(9, 16777215))
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
        self.toolBox.setMinimumSize(QSize(180, 0))
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
        self.page.setGeometry(QRect(0, 0, 180, 518))
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
        self.btnHome.setStyleSheet(u"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"}")

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
        self.btnVenda.setStyleSheet(u"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btnVenda)

        self.btnCadastrar = QPushButton(self.page)
        self.btnCadastrar.setObjectName(u"btnCadastrar")
        self.btnCadastrar.setMinimumSize(QSize(0, 30))
        self.btnCadastrar.setFont(font1)
        self.btnCadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCadastrar.setStyleSheet(u"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btnCadastrar)

        self.btnContatos = QPushButton(self.page)
        self.btnContatos.setObjectName(u"btnContatos")
        self.btnContatos.setMinimumSize(QSize(0, 30))
        self.btnContatos.setFont(font1)
        self.btnContatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnContatos.setStyleSheet(u"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btnContatos)

        self.btnSobre = QPushButton(self.page)
        self.btnSobre.setObjectName(u"btnSobre")
        self.btnSobre.setMinimumSize(QSize(0, 30))
        self.btnSobre.setFont(font1)
        self.btnSobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSobre.setStyleSheet(u"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btnSobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"MENU")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 137, 218))
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

        self.horizontalLayout_2.addWidget(self.btinToggle, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.topFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnSair = QPushButton(self.topFrame)
        self.btnSair.setObjectName(u"btnSair")
        self.btnSair.setMinimumSize(QSize(80, 15))
        self.btnSair.setMaximumSize(QSize(80, 30))
        self.btnSair.setFont(font1)
        self.btnSair.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSair.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(71,71,71);\n"
"border: solid black;\n"
"border-radius: 5px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(71,71,71);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnSair)


        self.verticalLayout.addWidget(self.topFrame)

        self.mainFrame = QFrame(self.mainContainer)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(71, 71, 71);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, -1)
        self.Pages = QStackedWidget(self.mainFrame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.Pages.setLineWidth(1)
        self.pgHome = QWidget()
        self.pgHome.setObjectName(u"pgHome")
        self.verticalLayout_6 = QVBoxLayout(self.pgHome)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lblLogo = QLabel(self.pgHome)
        self.lblLogo.setObjectName(u"lblLogo")

        self.verticalLayout_6.addWidget(self.lblLogo)

        self.Pages.addWidget(self.pgHome)
        self.pgVenda = QWidget()
        self.pgVenda.setObjectName(u"pgVenda")
        self.verticalLayout_16 = QVBoxLayout(self.pgVenda)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.tabWidget_2 = QTabWidget(self.pgVenda)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane { background-color: rgb(49, 49, 49) }\n"
"\n"
"QTabBar::tab { background-color: white; }\n"
"\n"
"QTabBar::tab:selected {background-color:rgb(49, 49, 49); color:white }\n"
"\n"
"QTabWidget{background-color: black; border: none}\n"
"\n"
"QLineEdit{\n"
"border-radius:15px}")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_main = QFrame(self.tab_3)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy1)
        self.frame_main.setMinimumSize(QSize(0, 400))
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_11.setSpacing(25)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_pesquisa = QFrame(self.frame_main)
        self.frame_pesquisa.setObjectName(u"frame_pesquisa")
        self.frame_pesquisa.setMinimumSize(QSize(550, 250))
        self.frame_pesquisa.setStyleSheet(u"\n"
"QFrame{\n"
"background-color:rgb(49, 49, 49);\n"
"border:None;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 4px;}")
        self.frame_pesquisa.setFrameShape(QFrame.StyledPanel)
        self.frame_pesquisa.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_pesquisa)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_edit_pesquisa = QFrame(self.frame_pesquisa)
        self.frame_edit_pesquisa.setObjectName(u"frame_edit_pesquisa")
        self.frame_edit_pesquisa.setMinimumSize(QSize(540, 30))
        self.frame_edit_pesquisa.setMaximumSize(QSize(16777215, 16777215))
        self.frame_edit_pesquisa.setFrameShape(QFrame.StyledPanel)
        self.frame_edit_pesquisa.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_edit_pesquisa)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_9 = QFrame(self.frame_edit_pesquisa)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(300, 10))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.txtPesquisa = QLineEdit(self.frame_9)
        self.txtPesquisa.setObjectName(u"txtPesquisa")
        sizePolicy1.setHeightForWidth(self.txtPesquisa.sizePolicy().hasHeightForWidth())
        self.txtPesquisa.setSizePolicy(sizePolicy1)
        self.txtPesquisa.setMinimumSize(QSize(300, 10))
        self.txtPesquisa.setMaximumSize(QSize(16777215, 16777215))
        self.txtPesquisa.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;")
        self.txtPesquisa.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.txtPesquisa)

        self.btn_Pesquisar = QPushButton(self.frame_9)
        self.btn_Pesquisar.setObjectName(u"btn_Pesquisar")
        sizePolicy1.setHeightForWidth(self.btn_Pesquisar.sizePolicy().hasHeightForWidth())
        self.btn_Pesquisar.setSizePolicy(sizePolicy1)
        self.btn_Pesquisar.setMinimumSize(QSize(30, 10))
        self.btn_Pesquisar.setMaximumSize(QSize(16777215, 16777215))
        self.btn_Pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Pesquisar.setStyleSheet(u"\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(213, 213, 213);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Pesquisar.setIcon(icon1)
        self.btn_Pesquisar.setIconSize(QSize(16, 16))

        self.horizontalLayout_10.addWidget(self.btn_Pesquisar)


        self.horizontalLayout_7.addWidget(self.frame_9)

        self.btn_AddProduto = QPushButton(self.frame_edit_pesquisa)
        self.btn_AddProduto.setObjectName(u"btn_AddProduto")
        sizePolicy1.setHeightForWidth(self.btn_AddProduto.sizePolicy().hasHeightForWidth())
        self.btn_AddProduto.setSizePolicy(sizePolicy1)
        self.btn_AddProduto.setMinimumSize(QSize(30, 10))
        self.btn_AddProduto.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.btn_AddProduto.setFont(font3)
        self.btn_AddProduto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_AddProduto.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(213, 213, 213);\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_AddProduto)


        self.gridLayout_2.addWidget(self.frame_edit_pesquisa, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_pesquisa)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 15))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(100, 500))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.pushButton.setFont(font4)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color:white;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(202, 0, 0);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setMaximumSize(QSize(100, 500))
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(0, 182, 42);\n"
"color:white;\n"
"border-radius: 4px;}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 200, 0);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_2)


        self.gridLayout_2.addWidget(self.frame_6, 2, 0, 1, 1)

        self.tableProduct = QTableWidget(self.frame_pesquisa)
        if (self.tableProduct.columnCount() < 7):
            self.tableProduct.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableProduct.setObjectName(u"tableProduct")
        self.tableProduct.setMinimumSize(QSize(0, 0))
        self.tableProduct.setStyleSheet(u"QTableWidget QHeaderView::section { \n"
"background-color: white; color: black; }\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(148,148,148);\n"
"color: black;\n"
"font: 10pt \"MS SHell Slg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(71, 71, 71);\n"
"color: white;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.tableProduct, 1, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_pesquisa)

        self.frame_carrinho = QFrame(self.frame_main)
        self.frame_carrinho.setObjectName(u"frame_carrinho")
        self.frame_carrinho.setMinimumSize(QSize(431, 250))
        font5 = QFont()
        font5.setPointSize(25)
        font5.setBold(True)
        self.frame_carrinho.setFont(font5)
        self.frame_carrinho.setStyleSheet(u"\n"
"QPushButton{\n"
"border-radius: 4px;}\n"
"QFrame{\n"
"background-color:rgb(49, 49, 49);\n"
"border:None;\n"
"}")
        self.frame_carrinho.setFrameShape(QFrame.StyledPanel)
        self.frame_carrinho.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_carrinho)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, -1, -1, -1)
        self.frame_10 = QFrame(self.frame_carrinho)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_carrinho = QLabel(self.frame_10)
        self.label_carrinho.setObjectName(u"label_carrinho")
        self.label_carrinho.setMinimumSize(QSize(0, 0))
        self.label_carrinho.setMaximumSize(QSize(16777215, 16777215))
        self.label_carrinho.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_carrinho)

        self.btn_ExcluirProduto = QPushButton(self.frame_10)
        self.btn_ExcluirProduto.setObjectName(u"btn_ExcluirProduto")
        sizePolicy1.setHeightForWidth(self.btn_ExcluirProduto.sizePolicy().hasHeightForWidth())
        self.btn_ExcluirProduto.setSizePolicy(sizePolicy1)
        self.btn_ExcluirProduto.setMinimumSize(QSize(20, 20))
        self.btn_ExcluirProduto.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(10)
        self.btn_ExcluirProduto.setFont(font6)
        self.btn_ExcluirProduto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ExcluirProduto.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(208, 0, 0);\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(213, 213, 213);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_ExcluirProduto)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.tableCarrinho = QTableWidget(self.frame_carrinho)
        if (self.tableCarrinho.columnCount() < 4):
            self.tableCarrinho.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableCarrinho.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableCarrinho.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableCarrinho.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableCarrinho.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.tableCarrinho.setObjectName(u"tableCarrinho")
        self.tableCarrinho.setMinimumSize(QSize(0, 0))
        self.tableCarrinho.setStyleSheet(u"QTableWidget QHeaderView::section { \n"
"background-color: white; color: black; }\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(148,148,148);\n"
"color: black;\n"
"font: 10pt \"MS SHell Slg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(71, 71, 71);\n"
"color: white;\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.tableCarrinho)

        self.frame_7 = QFrame(self.frame_carrinho)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setStyleSheet(u"padding: 0px 10px;\n"
"background-color: rgb(71, 71, 71);\n"
"border: solid rgb(71, 71, 71);\n"
"color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_9.addWidget(self.label_9)


        self.verticalLayout_14.addWidget(self.frame_7)


        self.horizontalLayout_11.addWidget(self.frame_carrinho)


        self.horizontalLayout_14.addWidget(self.frame_main)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_15 = QVBoxLayout(self.tab_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_11 = QFrame(self.tab_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"\n"
"QFrame{\n"
"background-color:rgb(49, 49, 49);\n"
"border:None;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 4px;}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_18.addWidget(self.label_14)


        self.verticalLayout_17.addWidget(self.frame_12)

        self.widget = QWidget(self.frame_11)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setStyleSheet(u"background-color:rgb(49, 49, 49)")
        self.verticalLayout_19 = QVBoxLayout(self.widget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_13 = QFrame(self.widget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit = QLineEdit(self.frame_13)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_13.addWidget(self.lineEdit)

        self.pushButton_3 = QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon1)

        self.horizontalLayout_13.addWidget(self.pushButton_3)


        self.verticalLayout_19.addWidget(self.frame_13)


        self.verticalLayout_17.addWidget(self.widget)

        self.tableVenda = QTableWidget(self.frame_11)
        if (self.tableVenda.columnCount() < 10):
            self.tableVenda.setColumnCount(10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        self.tableVenda.setObjectName(u"tableVenda")
        self.tableVenda.setStyleSheet(u"QTableWidget QHeaderView::section { \n"
"background-color: white; color: black; }\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(148,148,148);\n"
"color: black;\n"
"font: 10pt \"MS SHell Slg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(71, 71, 71);\n"
"color: white;\n"
"}\n"
"")

        self.verticalLayout_17.addWidget(self.tableVenda)


        self.verticalLayout_15.addWidget(self.frame_11)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_16.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pgVenda)
        self.pgCadastrar = QWidget()
        self.pgCadastrar.setObjectName(u"pgCadastrar")
        self.pgCadastrar.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.pgCadastrar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(self.pgCadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setMinimumSize(QSize(0, 40))
        font7 = QFont()
        font7.setKerning(True)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.tabWidget.setFont(font7)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { background-color: rgb(49, 49, 49) }\n"
"\n"
"QTabBar::tab { background-color: white; }\n"
"\n"
"QTabBar::tab:selected {background-color:rgb(49, 49, 49); color:white }\n"
"\n"
"QTabWidget{background-color: black; border: none}\n"
"\n"
"QLineEdit{\n"
"border-radius:15px}")
        self.tabWidget.setUsesScrollButtons(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
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
        self.txtNome.setMinimumSize(QSize(0, 40))
        self.txtNome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtNome, 1, 1, 1, 1)

        self.txtSobrenome = QLineEdit(self.frame_4)
        self.txtSobrenome.setObjectName(u"txtSobrenome")
        self.txtSobrenome.setMinimumSize(QSize(0, 40))
        self.txtSobrenome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtSobrenome, 1, 2, 1, 1)

        self.txtSenha = QLineEdit(self.frame_4)
        self.txtSenha.setObjectName(u"txtSenha")
        self.txtSenha.setMinimumSize(QSize(0, 40))
        self.txtSenha.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtSenha, 2, 0, 1, 1)

        self.lblCadastroFun = QLabel(self.frame_4)
        self.lblCadastroFun.setObjectName(u"lblCadastroFun")
        self.lblCadastroFun.setMinimumSize(QSize(0, 0))
        self.lblCadastroFun.setMaximumSize(QSize(16777215, 200))

        self.gridLayout.addWidget(self.lblCadastroFun, 0, 0, 1, 3)

        self.txtCPF = QLineEdit(self.frame_4)
        self.txtCPF.setObjectName(u"txtCPF")
        self.txtCPF.setMinimumSize(QSize(0, 40))
        self.txtCPF.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtCPF, 1, 0, 1, 1)

        self.txtNumero = QLineEdit(self.frame_4)
        self.txtNumero.setObjectName(u"txtNumero")
        self.txtNumero.setMinimumSize(QSize(0, 40))
        self.txtNumero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtNumero, 6, 0, 1, 1)

        self.txtLogradouro = QLineEdit(self.frame_4)
        self.txtLogradouro.setObjectName(u"txtLogradouro")
        self.txtLogradouro.setMinimumSize(QSize(0, 40))
        self.txtLogradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtLogradouro, 4, 1, 1, 2)

        self.txtCargo = QLineEdit(self.frame_4)
        self.txtCargo.setObjectName(u"txtCargo")
        self.txtCargo.setMinimumSize(QSize(0, 40))
        self.txtCargo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtCargo, 2, 1, 1, 1)

        self.txtSalario = QLineEdit(self.frame_4)
        self.txtSalario.setObjectName(u"txtSalario")
        self.txtSalario.setMinimumSize(QSize(0, 40))
        self.txtSalario.setAlignment(Qt.AlignCenter)
        self.txtSalario.setPlaceholderText(u"SAL\u00c1RIO*")

        self.gridLayout.addWidget(self.txtSalario, 2, 2, 1, 1)

        self.txtBairro = QLineEdit(self.frame_4)
        self.txtBairro.setObjectName(u"txtBairro")
        self.txtBairro.setMinimumSize(QSize(0, 40))
        self.txtBairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtBairro, 6, 1, 1, 1)

        self.txtMunicipio = QLineEdit(self.frame_4)
        self.txtMunicipio.setObjectName(u"txtMunicipio")
        self.txtMunicipio.setMinimumSize(QSize(0, 40))
        self.txtMunicipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtMunicipio, 6, 2, 1, 1)

        self.txtUF = QLineEdit(self.frame_4)
        self.txtUF.setObjectName(u"txtUF")
        self.txtUF.setMinimumSize(QSize(0, 40))
        self.txtUF.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtUF, 7, 0, 1, 1)

        self.txtTelefone = QLineEdit(self.frame_4)
        self.txtTelefone.setObjectName(u"txtTelefone")
        self.txtTelefone.setMinimumSize(QSize(0, 40))
        self.txtTelefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtTelefone, 4, 0, 1, 1)

        self.txtCEP = QLineEdit(self.frame_4)
        self.txtCEP.setObjectName(u"txtCEP")
        self.txtCEP.setMinimumSize(QSize(0, 40))
        self.txtCEP.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txtCEP, 7, 1, 1, 2)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.btnCadastrarFun = QPushButton(self.tab)
        self.btnCadastrarFun.setObjectName(u"btnCadastrarFun")
        self.btnCadastrarFun.setMinimumSize(QSize(160, 30))
        self.btnCadastrarFun.setFont(font6)
        self.btnCadastrarFun.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCadastrarFun.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(0, 129, 0);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"border-radius: 5px;	\n"
"background-color:rgb(49, 49, 49)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(49, 49, 49);\n"
"}")

        self.verticalLayout_9.addWidget(self.btnCadastrarFun, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setStyleSheet(u"border:None;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 9, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 13):
            self.tableWidget.setColumnCount(13)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem33)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"\n"
"QTableWidget QHeaderView::section { \n"
"background-color: white; color: black; }\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(148,148,148);\n"
"color: black;\n"
"font: 10pt \"MS SHell Slg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(49, 49, 49);\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

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
        self.btnAtualizar = QPushButton(self.frame_8)
        self.btnAtualizar.setObjectName(u"btnAtualizar")
        self.btnAtualizar.setMinimumSize(QSize(120, 30))
        self.btnAtualizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAtualizar.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(49, 49, 49)}")

        self.verticalLayout_7.addWidget(self.btnAtualizar)

        self.btnAlterar = QPushButton(self.frame_8)
        self.btnAlterar.setObjectName(u"btnAlterar")
        self.btnAlterar.setMinimumSize(QSize(120, 30))
        self.btnAlterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAlterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(206, 137, 0)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(49, 49, 49)}")

        self.verticalLayout_7.addWidget(self.btnAlterar)

        self.btnExcluir = QPushButton(self.frame_8)
        self.btnExcluir.setObjectName(u"btnExcluir")
        self.btnExcluir.setMinimumSize(QSize(120, 30))
        self.btnExcluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExcluir.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(182, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(49, 49, 49)}")

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
        self.label_7.setMinimumSize(QSize(0, 100))
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
        self.label_11.setMinimumSize(QSize(0, 200))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet(u"padding: 20px;")
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
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Imperador dos P\u00e3es </span></p></body></html>", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnVenda.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.btnCadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Funcion\u00e1rio", None))
        self.btnContatos.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.btnSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Usu\u00e1rio:  </span>Funcion\u00e1rio</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Sistema:  </span>Gest\u00e3o Padaria</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Status:</span>  Ativo </p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Vencimento:</span> 18/80/5260</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"SISTEMA", None))
        self.btinToggle.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sistema De Gest\u00e3o</span><br /></p></body></html>", None))
        self.btnSair.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.lblLogo.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/IMPERADOR DOS P\u00c2ES.png\" /></p></body></html>", None))
        self.txtPesquisa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquise aqui...", None))
#if QT_CONFIG(tooltip)
        self.btn_Pesquisar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_Pesquisar.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_Pesquisar.setText("")
        self.btn_AddProduto.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        ___qtablewidgetitem = self.tableProduct.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"idProduto", None));
        ___qtablewidgetitem1 = self.tableProduct.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableProduct.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Marca", None));
        ___qtablewidgetitem3 = self.tableProduct.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem4 = self.tableProduct.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem5 = self.tableProduct.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data de Emiss\u00e3o", None));
        ___qtablewidgetitem6 = self.tableProduct.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Data de Validade", None));
        self.label_carrinho.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Carrinho de Compras</span></p></body></html>", None))
        self.btn_ExcluirProduto.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        ___qtablewidgetitem7 = self.tableCarrinho.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"idProduto", None));
        ___qtablewidgetitem8 = self.tableCarrinho.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem9 = self.tableCarrinho.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem10 = self.tableCarrinho.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">TOTAL:</span></p></body></html>", None))
        self.label_9.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Realizar Venda", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">VENDAS REALIZADAS</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquise aqui por ID...", None))
        self.pushButton_3.setText("")
        ___qtablewidgetitem11 = self.tableVenda.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"idVenda", None));
        ___qtablewidgetitem12 = self.tableVenda.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None));
        ___qtablewidgetitem13 = self.tableVenda.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Forncedor", None));
        ___qtablewidgetitem14 = self.tableVenda.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem15 = self.tableVenda.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"idProduto", None));
        ___qtablewidgetitem16 = self.tableVenda.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem17 = self.tableVenda.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Marca", None));
        ___qtablewidgetitem18 = self.tableVenda.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem19 = self.tableVenda.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Data Validade", None));
        ___qtablewidgetitem20 = self.tableVenda.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Data de Venda", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Vendas", None))
        self.txtNome.setText("")
        self.txtNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME*", None))
        self.txtSobrenome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SOBRENOME*", None))
        self.txtSenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SENHA*", None))
        self.lblCadastroFun.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/Funcionario.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; vertical-align:super;\">CADASTRAR FUNCION\u00c1RIO</span><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; marg"
                        "in-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.txtCPF.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF*", None))
        self.txtNumero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.txtLogradouro.setText("")
        self.txtLogradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.txtCargo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CARGO*", None))
        self.txtBairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.txtMunicipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None))
        self.txtUF.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txtTelefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE*", None))
        self.txtCEP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.btnCadastrarFun.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Funcion\u00e1rio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Realizar Cadastro ", None))
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"SOBRENOME", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"SENHA", None));
        ___qtablewidgetitem25 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"CARGO", None));
        ___qtablewidgetitem26 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"SAL\u00c1RIO", None));
        ___qtablewidgetitem27 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem28 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem29 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem30 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem31 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem32 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem33 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        self.btnAtualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btnAlterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Funcion\u00e1rios Cadastrados", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/Contato.png\" />  <span style=\" font-size:18pt; font-weight:600;\">DESENVOLVEDORES</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/whatsApp.png\" />   <span style=\" font-size:18pt; vertical-align:super;\">(19)98458-6252 - (19)98102-2857 - (19)991575980 - (19)99648-2234 </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; vertical-align:super;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img "
                        "src=\":/icons/icons/grupo.png\" /><span style=\" font-size:11pt;\"><br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/Sobre.png\" />   <span style=\" font-size:18pt; font-weight:600;\">SOBRE O SISTEMA</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Este \u00e9 um Sistema de Cadastro de Funcion\u00e1rios e Controle de Vendas de uma Padaria Fict\u00edcia, desenvolvido por alunos do Col\u00e9gio T\u00e9cnico de Campinas - COTUCA, com o objetivo de cumprir com os instrumentos avaliativos da m\u00e1teria de Pr\u00e1tica Profissional I. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">O Sistema foi constru\u00eddo a "
                        "partir da utiliza\u00e7\u00e3o conjunta da Lingaguem de Programa\u00e7\u00e3o Python, suas bibliotecas e do ambiente de desenvolvimento integrado de plataforma cruzada, QtDesigner.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/python.png\" />                                                        <img src=\":/icons/icons/QtDesigner.png\" /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">\u00a9Imperador dos P\u00e3es 2023</span></p></body></html>", None))
    # retranslateUi

