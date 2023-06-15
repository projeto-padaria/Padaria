# Importações da pasta 'interfaces'
import sys
sys.path.append('interfaces')
# Importações de bibliotecas do PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QPushButton
from login_ui import Ui_principalLogin

class FormPrincipal(QMainWindow, Ui_principalLogin):
    def __init__(self):
        super().__init__() 
        self.setupUi(self) 
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar) 
        self.show()
        self.setWindowTitle("Sistema de Vendas")

if __name__ == "__main__":
    aplicacao = QApplication(sys.argv) 
    janela = FormPrincipal() 
    aplicacao.exec()