# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'venda.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(628, 600)
        MainWindow.setMinimumSize(QSize(628, 600))
        MainWindow.setMaximumSize(QSize(628, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 4)

        self.frame_pesquisa = QFrame(self.centralwidget)
        self.frame_pesquisa.setObjectName(u"frame_pesquisa")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_pesquisa.sizePolicy().hasHeightForWidth())
        self.frame_pesquisa.setSizePolicy(sizePolicy)
        self.frame_pesquisa.setMinimumSize(QSize(0, 0))
        self.frame_pesquisa.setMaximumSize(QSize(800, 800))
        self.frame_pesquisa.setFrameShape(QFrame.StyledPanel)
        self.frame_pesquisa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_pesquisa)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.line = QFrame(self.frame_pesquisa)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.frame_2 = QFrame(self.frame_pesquisa)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_F3Key = QLabel(self.frame_2)
        self.l_F3Key.setObjectName(u"l_F3Key")
        font = QFont()
        font.setPointSize(8)
        self.l_F3Key.setFont(font)

        self.horizontalLayout.addWidget(self.l_F3Key)

        self.l_F2Key = QLabel(self.frame_2)
        self.l_F2Key.setObjectName(u"l_F2Key")
        self.l_F2Key.setFont(font)

        self.horizontalLayout.addWidget(self.l_F2Key)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.gb_pesquisa = QGroupBox(self.frame_pesquisa)
        self.gb_pesquisa.setObjectName(u"gb_pesquisa")
        sizePolicy.setHeightForWidth(self.gb_pesquisa.sizePolicy().hasHeightForWidth())
        self.gb_pesquisa.setSizePolicy(sizePolicy)
        self.gb_pesquisa.setMaximumSize(QSize(800, 600))
        self.horizontalLayout_3 = QHBoxLayout(self.gb_pesquisa)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_3 = QFrame(self.gb_pesquisa)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.l_title = QLabel(self.frame_3)
        self.l_title.setObjectName(u"l_title")
        self.l_title.setMinimumSize(QSize(66, 22))
        self.l_title.setMaximumSize(QSize(66, 22))
        font1 = QFont()
        font1.setPointSize(13)
        self.l_title.setFont(font1)

        self.horizontalLayout_2.addWidget(self.l_title)

        self.le_produto = QLineEdit(self.frame_3)
        self.le_produto.setObjectName(u"le_produto")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_produto.sizePolicy().hasHeightForWidth())
        self.le_produto.setSizePolicy(sizePolicy1)
        self.le_produto.setMinimumSize(QSize(350, 22))
        self.le_produto.setMaximumSize(QSize(350, 22))

        self.horizontalLayout_2.addWidget(self.le_produto)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.toolButton = QToolButton(self.gb_pesquisa)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QSize(50, 22))
        self.toolButton.setMaximumSize(QSize(22, 22))
        self.toolButton.setPopupMode(QToolButton.InstantPopup)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(False)

        self.horizontalLayout_3.addWidget(self.toolButton)


        self.verticalLayout_6.addWidget(self.gb_pesquisa)


        self.gridLayout.addWidget(self.frame_pesquisa, 1, 0, 1, 4, Qt.AlignVCenter)

        self.frame_operacao = QFrame(self.centralwidget)
        self.frame_operacao.setObjectName(u"frame_operacao")
        sizePolicy.setHeightForWidth(self.frame_operacao.sizePolicy().hasHeightForWidth())
        self.frame_operacao.setSizePolicy(sizePolicy)
        self.frame_operacao.setMinimumSize(QSize(204, 110))
        self.frame_operacao.setMaximumSize(QSize(204, 110))
        self.frame_operacao.setFrameShape(QFrame.StyledPanel)
        self.frame_operacao.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_operacao)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_operacao = QGroupBox(self.frame_operacao)
        self.gb_operacao.setObjectName(u"gb_operacao")
        self.gb_operacao.setMinimumSize(QSize(178, 90))
        self.gb_operacao.setMaximumSize(QSize(178, 90))
        self.gridLayout_2 = QGridLayout(self.gb_operacao)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_caixaRapido_2 = QPushButton(self.gb_operacao)
        self.btn_caixaRapido_2.setObjectName(u"btn_caixaRapido_2")

        self.gridLayout_2.addWidget(self.btn_caixaRapido_2, 0, 0, 1, 1)

        self.btn_reservas = QPushButton(self.gb_operacao)
        self.btn_reservas.setObjectName(u"btn_reservas")

        self.gridLayout_2.addWidget(self.btn_reservas, 1, 1, 1, 1)

        self.btn_Devoluo = QPushButton(self.gb_operacao)
        self.btn_Devoluo.setObjectName(u"btn_Devoluo")

        self.gridLayout_2.addWidget(self.btn_Devoluo, 0, 1, 1, 1)

        self.btn_orcamento = QPushButton(self.gb_operacao)
        self.btn_orcamento.setObjectName(u"btn_orcamento")

        self.gridLayout_2.addWidget(self.btn_orcamento, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.gb_operacao)


        self.gridLayout.addWidget(self.frame_operacao, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.frame_especial = QFrame(self.centralwidget)
        self.frame_especial.setObjectName(u"frame_especial")
        sizePolicy.setHeightForWidth(self.frame_especial.sizePolicy().hasHeightForWidth())
        self.frame_especial.setSizePolicy(sizePolicy)
        self.frame_especial.setMinimumSize(QSize(250, 80))
        self.frame_especial.setMaximumSize(QSize(250, 80))
        self.frame_especial.setFrameShape(QFrame.StyledPanel)
        self.frame_especial.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_especial)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gb_especial = QGroupBox(self.frame_especial)
        self.gb_especial.setObjectName(u"gb_especial")
        self.gb_especial.setMinimumSize(QSize(200, 60))
        self.gb_especial.setMaximumSize(QSize(200, 60))
        self.formLayout = QFormLayout(self.gb_especial)
        self.formLayout.setObjectName(u"formLayout")
        self.btn_pagamentEspecial = QPushButton(self.gb_especial)
        self.btn_pagamentEspecial.setObjectName(u"btn_pagamentEspecial")
        self.btn_pagamentEspecial.setMaximumSize(QSize(350, 16777215))

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btn_pagamentEspecial)


        self.verticalLayout_2.addWidget(self.gb_especial)


        self.gridLayout.addWidget(self.frame_especial, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.frame_carinhoCompra = QFrame(self.centralwidget)
        self.frame_carinhoCompra.setObjectName(u"frame_carinhoCompra")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_carinhoCompra.sizePolicy().hasHeightForWidth())
        self.frame_carinhoCompra.setSizePolicy(sizePolicy2)
        self.frame_carinhoCompra.setFrameShape(QFrame.StyledPanel)
        self.frame_carinhoCompra.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_carinhoCompra)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gb_carrinhoCompra = QGroupBox(self.frame_carinhoCompra)
        self.gb_carrinhoCompra.setObjectName(u"gb_carrinhoCompra")
        self.horizontalLayout_4 = QHBoxLayout(self.gb_carrinhoCompra)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.treeWidget = QTreeWidget(self.gb_carrinhoCompra)
        self.treeWidget.headerItem().setText(7, "")
        self.treeWidget.setObjectName(u"treeWidget")

        self.horizontalLayout_4.addWidget(self.treeWidget)


        self.verticalLayout_5.addWidget(self.gb_carrinhoCompra)


        self.gridLayout.addWidget(self.frame_carinhoCompra, 3, 0, 1, 4)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(115, 140))
        self.frame.setMaximumSize(QSize(115, 140))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gb_pagamento = QGroupBox(self.frame)
        self.gb_pagamento.setObjectName(u"gb_pagamento")
        self.verticalLayout_4 = QVBoxLayout(self.gb_pagamento)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_pagamento = QPushButton(self.gb_pagamento)
        self.btn_pagamento.setObjectName(u"btn_pagamento")

        self.verticalLayout_4.addWidget(self.btn_pagamento)

        self.btn_TEF = QPushButton(self.gb_pagamento)
        self.btn_TEF.setObjectName(u"btn_TEF")

        self.verticalLayout_4.addWidget(self.btn_TEF)

        self.btn_cancelar = QPushButton(self.gb_pagamento)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.verticalLayout_4.addWidget(self.btn_cancelar)


        self.verticalLayout_3.addWidget(self.gb_pagamento)


        self.gridLayout.addWidget(self.frame, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_F3Key.setText(QCoreApplication.translate("MainWindow", u" F3 - Quantidade", None))
        self.l_F2Key.setText(QCoreApplication.translate("MainWindow", u" F2 - Pesquisa Produto", None))
        self.gb_pesquisa.setTitle(QCoreApplication.translate("MainWindow", u"Pesquisa de Produto", None))
        self.l_title.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gb_operacao.setTitle(QCoreApplication.translate("MainWindow", u"Opera\u00e7\u00f5es", None))
        self.btn_caixaRapido_2.setText(QCoreApplication.translate("MainWindow", u"Caixa R\u00e1pido", None))
        self.btn_reservas.setText(QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.btn_Devoluo.setText(QCoreApplication.translate("MainWindow", u"Devolu\u00e7\u00e3o", None))
        self.btn_orcamento.setText(QCoreApplication.translate("MainWindow", u"Or\u00e7amento", None))
        self.gb_especial.setTitle(QCoreApplication.translate("MainWindow", u"Especial", None))
        self.btn_pagamentEspecial.setText(QCoreApplication.translate("MainWindow", u"Pagamento Especial", None))
        self.gb_carrinhoCompra.setTitle(QCoreApplication.translate("MainWindow", u"Carrinho de compra", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Data de Validade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Data de Emiss\u00e3o", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Marca do Produto", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Nome do Produto", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"idVenda", None));
        self.gb_pagamento.setTitle(QCoreApplication.translate("MainWindow", u"Pagamento", None))
        self.btn_pagamento.setText(QCoreApplication.translate("MainWindow", u"Pagamento", None))
        self.btn_TEF.setText(QCoreApplication.translate("MainWindow", u"TEF", None))
        self.btn_cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

