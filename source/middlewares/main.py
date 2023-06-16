import sys

sys.path.append("interfaces")
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from cadastro_ui import Ui_MainWindow
from tela_login_New_ui import Ui_MainWindowLogin
from PySide6 import QtCore
from connect import Connect


class MainWindowLogin(QMainWindow, Ui_MainWindowLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Imperador dos Pães - Login")
        appIcon = QIcon("")
        self.setWindowIcon(appIcon)
        self.btnLogin.clicked.connect(self.TelaPrincipal)

    def TelaPrincipal(self):
        self.login = self.txtLogin.text()
        self.senha = self.txtSenha.text()
        db = Connect('BD23333','BD23333')  
        db.Login()
        auth = db.LoginAuthentication(self.login, self.senha)
        if auth == True:
            login.close()
            window = MainWindow()
            window.show()
        else:
            QMessageBox.warning(login,"ALERTA","Login ou Senha Incorretos")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Imperador dos Pães - Sistema de Gestão")
        appIcon = QIcon("")
        self.setWindowIcon(appIcon)

        ######################################################################
        # TOGGLE BUTTON
        self.btinToggle.clicked.connect(self.left_Container)
        #####################################################################
        # Paginas do Sistema
        self.btnHome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgHome))
        self.btnVenda.clicked.connect(self.pgBancoDeDados)
        self.btnCadastrar.clicked.connect(self.pgBancoDeDados)
        self.btnSobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgSobre))
        self.btnContatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgContatos))
        self.btnCadastrarFun.clicked.connect(self.cadastroFuncionario)
        self.btnAtualizar.clicked.connect(self.refreshTable)
        self.btnLoginBD.clicked.connect(self.ConnectDatabase)
        ######################################################################

    def printError(self, error) -> None:
        return print(f"ERROR: {error}")

    def left_Container(self):
        width = self.leftContainer.width()  # tamanho do container

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.leftContainer, b"maximumWidth")
        self.animation.setDuration(500)  # Duração da animação
        self.animation.setStartValue(width)  # Incio da animacao
        self.animation.setEndValue(newWidth)  # Término da animação
        self.animation.setEasingCurve(
            QtCore.QEasingCurve.InOutQuart
        )  # Tipo de animação
        self.animation.start()

    def pgBancoDeDados(self):
        self.sender1 = self.sender()
        self.Pages.setCurrentWidget(self.pgBanco)

    def connectDatabase(self):
        self.login = self.txtLoginDB.text()
        self.password = self.txtSenhaDB.text()
        try:
            self.db = Connect(self.login, self.password)
            self.db.Login()
            if self.sender1 == self.btnVenda:
                self.txtLoginDB.setText("")
                self.txtSenhaDB.setText("")
                self.Pages.setCurrentWidget(self.pgVenda)
            elif self.sender1 == self.btnCadastrar:
                self.txtLoginDB.setText("")
                self.txtSenhaDB.setText("")
                self.db.showTableFun(self.tableWidget)
                self.Pages.setCurrentWidget(self.pgCadastrar)
        except Exception as error:
            QMessageBox.warning(login,"ALERTA","Login ou Senha Incorretos")
            self.printError(error)
            self.txtLoginDB.setText("")
            self.txtSenhaDB.setText("")

    def cadastroFuncionario(self):
        self.cpf = self.txtCPF.text()
        self.nome = self.txtNome.text()
        self.sobrenome = self.txtSobrenome.text()
        self.senha = self.txtSenha.text()
        self.cargo = self.txtCargo.text()
        self.salario = self.txtSalario.text()
        self.telefone = self.txtTelefone.text()
        self.rua = self.txtLogradouro.text()
        self.numero = self.txtNumero.text()
        self.bairro = self.txtBairro.text()
        self.cidade = self.txtMunicipio.text()
        self.uf = self.txtUF.text()
        self.cep = self.txtCEP.text()
        try:
            self.db.Login()
            self.db.insertTableFun(
                self.cpf,
                self.nome,
                self.sobrenome,
                self.senha,
                self.cargo,
                self.salario,
                self.telefone,
                self.rua,
                self.numero,
                self.bairro,
                self.cidade,
                self.uf,
                self.cep,
            )
            self.cpf = self.txtCPF.setText("")
            self.nome = self.txtNome.setText("")
            self.sobrenome = self.txtSobrenome.setText("")
            self.senha = self.txtSenha.setText("")
            self.cargo = self.txtCargo.setText("")
            self.salario = self.txtSalario.setText("")
            self.telefone = self.txtTelefone.setText("")
            self.rua = self.txtLogradouro.setText("")
            self.numero = self.txtNumero.setText("")
            self.bairro = self.txtBairro.setText("")
            self.cidade = self.txtMunicipio.setText("")
            self.uf = self.txtUF.setText("")
            self.cep = self.txtCEP.setText("")
        except Exception as error:
            self.printError(error)
            QMessageBox.warning(login,"ALERTA","Preencha os Campos Obrigatórios Adequadamente!")

    def refreshTable(self):
        self.db.showTableFun(self.tableWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = MainWindowLogin()
    login.show()
    sys.exit(app.exec())

