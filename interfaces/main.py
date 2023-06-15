from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from cadastro_ui import Ui_MainWindow
from tela_login_New_ui import Ui_MainWindowLogin
from PySide6 import QtCore
from connect import Connect
import sys


class MainWindowLogin(QMainWindow, Ui_MainWindowLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Padaria - Sistema de Gestão")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        self.btnLogin.clicked.connect(self.TelaPrincipal)

    def TelaPrincipal(self):
        self.login = self.txtLogin.text()
        self.senha = self.txtSenha.text()
        bd = Connect(self.login,self.senha).Login()
        if bd == False:
            login.close()
            window = MainWindow()
            window.show()
        else:
            print("N foi pae")
            login.close()

        # sys.exit(app.exec())

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Padaria - Sistema de Gestão")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        ##################################################################################
        #TOGGLE BUTTON
        self.btinToggle.clicked.connect(self.left_Container)
        ##################################################################################
        #Paginas do Sistema
        self.btnHome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgHome))
        self.btnVenda.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgVenda))
        self.btnCadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgCadastrar))
        self.btnSobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgSobre))
        self.btnContatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgContatos))
        ##################################################################################
        
        
    def left_Container(self):
        width = self.leftContainer.width() # tamanho do container

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9
        
        self.animation = QtCore.QPropertyAnimation(self.leftContainer, b"maximumWidth")
        self.animation.setDuration(500) #Duração da animação
        self.animation.setStartValue(width) #Incio da animacao
        self.animation.setEndValue(newWidth) #Término da animação
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart) #Tipo de animação
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = MainWindowLogin()
    login.show()
    sys.exit(app.exec())
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec())