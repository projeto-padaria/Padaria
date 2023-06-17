# Importação de libs
import sys
sys.path.append("interfaces")

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Importação de Interfaces
from tela_Login_ui import Ui_MainWindowLogin
from main import MainWindow

# Importação da Classe de Conexão com o Banco de Dados
from module import Connect


class MainWindowLogin(QMainWindow, Ui_MainWindowLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Imperador dos Pães - Login")
        self.btnLogin.clicked.connect(self.mainWindow)
        self.btnSair.clicked.connect(self.closeLogin)
        
    def mainWindow(self):
        self.login = self.txtLogin.text()
        self.password = self.txtSenha.text()
        db = Connect("BD23333", "BD23333")  # TROCAR
        db.Login()
        auth = db.LoginAuthentication(self.login, self.password)
        if auth == True:
            login.close()
            window = MainWindow()
            window.show()
        else:
            QMessageBox.warning(login, "ALERTA", "Login ou Senha Incorretos")
    
    def closeLogin(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = MainWindowLogin()
    login.show()
    sys.exit(app.exec())
