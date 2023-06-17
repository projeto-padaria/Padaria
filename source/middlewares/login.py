import sys
sys.path.append("interfaces")

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from tela_login_New_ui import Ui_MainWindowLogin
from module import Connect
from main import MainWindow

class MainWindowLogin(QMainWindow, Ui_MainWindowLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Padaria - Sistema de Gestão")
        self.btnLogin.clicked.connect(self.TelaPrincipal)

    def TelaPrincipal(self):
        self.login = self.txtLogin.text()
        self.senha = self.txtSenha.text()
        db = Connect('BD23333','BD23333')  # TROCAR
        db.Login()
        auth = db.LoginAuthentication(self.login, self.senha)
        if auth == True:
            login.close()
            window = MainWindow()
            window.show()
        else:
            QMessageBox.warning(login,"ALERTA","Login ou Senha Incorretos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = MainWindowLogin()
    login.show()
    sys.exit(app.exec())