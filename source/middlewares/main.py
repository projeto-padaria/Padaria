import sys
sys.path.append("interfaces")

# Importação de libs
from PyQt5.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6 import QtCore

# Importação da Interface de Cadastro
from tela_Principal_ui import Ui_MainWindow

# Importação da Classe de Conexão com o Banco de Dados
from module import Connect

# Importação da Classe debug e Criação da Instância
from debug import libDebug
debug = libDebug()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Imperador dos Pães - Sistema de Gestão")

        # TOGGLE BUTTON
        self.btinToggle.clicked.connect(self.left_Container)
        # Paginas do Sistema
        self.btnHome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgHome))
        self.btnVenda.clicked.connect(self.pgBancoDeDados)
        self.btnCadastrar.clicked.connect(self.pgBancoDeDados)
        self.btnSobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgSobre))
        self.btnContatos.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pgContatos)
        )
        self.btnCadastrarFun.clicked.connect(self.cadastroFuncionario)
        self.btnAtualizar.clicked.connect(self.refreshTable)
        self.btnLoginBD.clicked.connect(self.connectDatabase)
        self.btnAlterar.clicked.connect(self.updateTable)
        self.btnExcluir.clicked.connect(self.deletarFun)

    def left_Container(self):
        width = self.leftContainer.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.leftContainer, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
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
            QMessageBox.warning(self, "ALERTA", "Login ou Senha Incorretos")
            debug.printError(error)
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
            QMessageBox.about(None, "ALERTA", "Funcionário Cadastrado com Sucesso!")
        except Exception as error:
            debug.printError(error)
            QMessageBox.warning(
                None, "ALERTA", "Preencha os Campos Obrigatórios Adequadamente!"
            )

    def deletarFun(self):
        self.db.Login()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()
        if resp == QMessageBox.Yes:
            try:
                cpf = (
                    self.tableWidget.selectionModel()
                    .currentIndex()
                    .siblingAtColumn(0)
                    .data()
                )
                result = self.db.deleteFun(cpf)
                self.refreshTable()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Imperador dos Pães")
                msg.setText(result)
                msg.exec()
            except Exception as error:
                debug.printError(error)

    def updateTable(self):
        dados = []
        update_dados = []

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, column).text())
            update_dados.append(dados)
            dados = []

        try:
            self.db.Login()
            for dados in update_dados:
                self.db.updateTable(tuple(dados))
            QMessageBox.about(
                None, "Atualização de Dados", "Dados atualizados com sucesso!"
            )

            self.refreshTable()
        except Exception as error:
            debug.printError(error)

    def refreshTable(self):
        self.db.showTableFun(self.tableWidget)
