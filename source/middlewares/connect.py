import pyodbc as bd
from PySide6.QtWidgets import QTableWidgetItem
from os import system as clearTerminal


class Connect:
    def __init__(self, login, senha) -> None:
        self.server = "regulus.cotuca.unicamp.br"
        self.driver = "SQL Server"
        self.username = login
        self.password = senha
        self.database = None
        self.cursor = None
        self.table = None
        self.query = None
        self.schema = "padaria"
        self.RED = "\033[1;31m"
        self.BLUE = "\033[1;34m"
        self.CYAN = "\033[1;36m"
        self.GREEN = "\033[0;32m"
        self.RESET = "\033[0;0m"
        self.BOLD = "\033[;1m"
        self.REVERSE = "\033[;7m"
        self.YELLOW = "\033[33m"

    # debug functions

    def printError(self, error) -> None:
        return print(f"{self.BOLD}{self.RED}ERROR: {self.RESET}{error}")

    def printSuccess(self, success) -> None:
        return print(f"{self.BOLD}{self.GREEN}SUCCESS: {self.RESET}{success}")

    def printTitle(self, title) -> None:
        menubar = "—" * len(title)
        return print(f"{self.BOLD}{menubar} {title} {menubar} {self.RESET}")

    # funções de execução

    def Login(self) -> None:
        clearTerminal("cls")
        self.printTitle("Login")
        self.database = self.username
        self.cursor = bd.connect(
            f"DRIVER={self.driver};SERVER={self.server};UID={self.username};PWD={self.password};DATABASE={self.database}"
        ).cursor()
        self.printSuccess("Login Feito!")

    def LoginAuthentication(self, login, senha):
        self.usuario = "cpf"
        self.senha = "senha"
        self.table = "funcionario"
        try:
            self.cursor.execute(
                f"""SELECT {self.usuario},{self.senha} from {self.schema}.{self.table} where {self.usuario} = {login} and {self.senha} = '{senha}'"""
            )
            conferir = self.cursor.fetchall()
            if conferir == []:
                exit()
            else:
                self.printSuccess("Usuário encontrado!!")
                return True
        except Exception as error:
            self.printError("Usuário Não Encontrado!")
            return False

    def insertTableFun(self, cpf, nome, sobrenome, senha, cargo, salario, telefone,rua, numero, bairro, cidade, uf, cep) -> None:

        valores = [cpf, nome, sobrenome, senha, cargo, salario, telefone, rua, numero, bairro, cidade, uf, cep]
        aux = 0
        for indice,valor in enumerate(valores):
            if indice in (0,1,2,3,4,5,6) and valor == '':
                aux += 1
            else:
                if valor == '':
                    valores.pop(indice)
                    valores.insert(indice,None)
        #  VER ORM
        if aux == 0:
            self.cursor.execute(
                "INSERT INTO padaria.endereco VALUES (?,?,?,?,?,?)",(valores[9],valores[7],valores[8],valores[10],valores[11],valores[12])
            )
            self.cursor.execute(
                "INSERT INTO padaria.funcionario VALUES (?,?,?,?,?,?,?, NULL)",(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
            )
            self.cursor.commit()
            print("Funcionário Cadastrado!!!!")
        else:
            raise Exception("Prencha os campos obrigatórios!!")
        

    def showTableFun(self, tableWidget):
        comando_SQL = "SELECT F.cpf,F.nome,F.sobrenome,F.senha,F.cargo,F.salario,F.telefone,E.bairro,E.rua,E.numero,E.cidade,E.UF,E.cep FROM padaria.funcionario F,padaria.endereco E WHERE F.idEndereco = E.idEndereco;"
        self.cursor.execute(comando_SQL)
        dados_lidos = self.cursor.fetchall()
        print(dados_lidos)
        table = tableWidget
        try:
            table.setRowCount(len(dados_lidos))
            table.setColumnCount(13)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 13):
                    table.setItem(i, j, QTableWidgetItem(str(dados_lidos[i][j])))
        except Exception as error:
            self.printError(error)


if __name__ == "__main__":
    a = Connect("BD23333", "BD23333")
    a.Login()
