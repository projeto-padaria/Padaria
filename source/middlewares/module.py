# Importação de libs
import pyodbc as bd
from PySide6.QtWidgets import QTableWidgetItem
from os import system as clearTerminal

# Importação da Classe debug
from debug import libDebug
debug = libDebug()


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

    # funções de execução

    def Login(self) -> None:
        clearTerminal("cls")
        debug.printTitle("Login")
        self.database = self.username
        self.cursor = bd.connect(
            f"DRIVER={self.driver};SERVER={self.server};UID={self.username};PWD={self.password};DATABASE={self.database}"
        ).cursor()
        debug.printSuccess("Conexão com o Banco de Dados Estabelecida!")

    def closeConnection(self):
        self.cursor.close()

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
                raise Exception("Usuário ou Senha Inválidos!")
            else:
                debug.printSuccess("Usuário encontrado!!")
                self.cursor.close()
                return True
        except Exception as error:
            debug.printError(error)
            return False

    def insertTableFun(self, valores) -> None:
        aux = 0
        for indice,valor in enumerate(valores):
            if indice in (0,1,2,3,4,5,6) and valor == '':
                aux += 1
            else:
                if valor == '':
                    valores.pop(indice)
                    valores.insert(indice,None)
        if aux == 0:
            self.cursor.execute(
                "INSERT INTO padaria.endereco VALUES (?,?,?,?,?,?)",(valores[9],valores[7],valores[8],valores[10],valores[11],valores[12])
            )
            self.cursor.execute(
                "INSERT INTO padaria.funcionario VALUES (?,?,?,?,?,?,?, NULL)",(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
            )
            self.cursor.commit()
            debug.printSuccess("Funcionário cadastrado com sucesso!!")
        else:
            raise Exception("Prencha os campos Obrigatórios Adequadamente!!")
        

    def showTableFun(self, tableWidget):
        comando_SQL = "SELECT F.cpf,F.nome,F.sobrenome,F.senha,F.cargo,F.salario,F.telefone,E.bairro,E.rua,E.numero,E.cidade,E.UF,E.cep FROM padaria.funcionario F,padaria.endereco E WHERE F.idEndereco = E.idEndereco;"
        self.cursor.execute(comando_SQL)
        dados_lidos = self.cursor.fetchall()
        table = tableWidget
        try:
            table.setRowCount(len(dados_lidos))
            table.setColumnCount(13)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 13):
                    table.setItem(i, j, QTableWidgetItem(str(dados_lidos[i][j])))
        except Exception as error:
            debug.printError(error)

    def deleteFun(self, cpf):
        self.cursor.execute(f"DELETE FROM padaria.funcionario WHERE cpf = '{cpf}' ")
        self.cursor.commit()
        return "Cadastro de Funcionário excluido com sucesso!"
        
    def updateTable(self,fullDataSet):
        self.cursor.execute(f"""
        UPDATE padaria.endereco 
        SET
            bairro = '{fullDataSet[7]}',
            rua = '{fullDataSet[8]}',
            numero = {fullDataSet[9]},
            cidade = '{fullDataSet[10]}',
            uf ='{fullDataSet[11]}',
            cep = '{fullDataSet[12]}'
        FROM padaria.endereco AS E
        INNER JOIN padaria.funcionario AS F ON E.idEndereco = F.idEndereco
        WHERE F.cpf = '{fullDataSet[0]}'""")
        self.cursor.execute(f""" UPDATE padaria.funcionario SET

            cpf = '{fullDataSet[0]}',
            nome = '{fullDataSet[1]}',
            sobrenome = '{fullDataSet[2]}',
            senha = '{fullDataSet[3]}',
            cargo = '{fullDataSet[4]}',
            salario = {fullDataSet[5]},
            telefone = {fullDataSet[6]}
            WHERE cpf = '{fullDataSet[0]}'""")
        self.cursor.commit()

# if __name__ == "__main__":
#     a = Connect("BD23333", "BD23333")
#     a.Login()
