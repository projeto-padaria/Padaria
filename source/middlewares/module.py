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
        debug.printSuccess("Conexão com o Banco de Dados Fechada!")

    def LoginAuthentication(self, login, senha):
        self.usuario = "cpf"
        self.senha = "senha"
        self.table = "funcionario"
        try:
            self.cursor.execute(
                f"""SELECT {self.usuario},{self.senha} from {self.schema}.{self.table} where {self.usuario} = '{login}' and {self.senha} = '{senha}'"""
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
        for indice, valor in enumerate(valores):
            if indice in (0, 1, 2, 3, 4, 5, 6) and valor == "":
                aux += 1
            else:
                if valor == "" or valor == "None":
                    valores.pop(indice)
                    valores.insert(indice, None)
        if aux == 0:
            self.cursor.execute(
                "INSERT INTO padaria.endereco VALUES (?,?,?,?,?,?)",
                (
                    valores[9],
                    valores[7],
                    valores[8],
                    valores[10],
                    valores[11],
                    valores[12],
                ),
            )
            self.cursor.execute(
                "INSERT INTO padaria.funcionario VALUES (?,?,?,?,?,?,?, NULL)",
                (
                    valores[0],
                    valores[1],
                    valores[2],
                    valores[3],
                    valores[4],
                    valores[5],
                    valores[6],
                ),
            )
            self.cursor.commit()
            debug.printSuccess("Funcionário cadastrado com sucesso!!")
        else:
            raise Exception("Prencha os campos Obrigatórios Adequadamente!!")
    
    def addProduct(self,id):
        parameters = [1,1,id,2]
        self.cursor.execute("INSERT INTO padaria.venda VALUES (?,?,?,?,convert(date, getdate(), 29))",parameters)
        self.cursor.commit()

    def deleteProduct(self):
        pass


    def search(self,table, where):
        try:
            if where:
                parameters = ['%' + where + '%', '%' + where + '%']
                self.cursor.execute('SELECT * FROM padaria.produto WHERE idProduto LIKE ? OR nome LIKE ?', parameters)
                dados_lidos = self.cursor.fetchall()

                try:
                    table.setRowCount(len(dados_lidos))
                    table.setColumnCount(8)
                    for i in range(0, len(dados_lidos)):
                        for j in range(0, 8):
                            table.setItem(i, j, QTableWidgetItem(str(dados_lidos[i][j])))
                except Exception as error:
                    debug.printError(error)

            elif where == "":
                self.showTable(table,True)
            
        except Exception as error:
            print(error)
            # message = QMessageBox(self)
            # message.setWindowTitle("Sistema de Apoio ao Ensino")
            # message.setText(error.args[0])
            # message.setIcon(QMessageBox.Critical)
            # message.exec()


    def showTable(self, tableWidget,sender = None):
        if sender == True:
            self.cursor.execute(
                "SELECT P.idProduto, P.nome, P.marca, P.preco, P.quantidade, P.datadeemissao, P.datadevalidade FROM padaria.produto P;"
            )
            dados_lidos = self.cursor.fetchall()
            table = tableWidget
            try:
                table.setRowCount(len(dados_lidos))
                table.setColumnCount(7)
                for i in range(0, len(dados_lidos)):
                    for j in range(0, 7):
                        table.setItem(i, j, QTableWidgetItem(str(dados_lidos[i][j])))
            except Exception as error:
                debug.printError(error)

        elif sender == False:
            self.cursor.execute(
                "SELECT F.cpf,F.nome,F.sobrenome,F.senha,F.cargo,F.salario,F.telefone,E.bairro,E.rua,E.numero,E.cidade,E.UF,E.cep FROM padaria.funcionario F,padaria.endereco E WHERE F.idEndereco = E.idEndereco;"
            )
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
        else:
            self.cursor.execute(
                """SELECT V.idVenda,Fu.nome,F.nome,C.nome,V.idProduto, P.nome, P.marca, P.preco, P.datadevalidade, V.data FROM
                padaria.funcionario Fu,
                padaria.venda V,
                padaria.fornecedor F,
                padaria.produto P,
                padaria.cliente C
                WHERE 
                V.idProduto = P.idProduto and P.idFornecedor = F.idFornecedor and V.idFuncionario = Fu.idFuncionario and V.idCliente = C.idCliente""")
            dados_lidos = self.cursor.fetchall()
            table = tableWidget
            try:
                table.setRowCount(len(dados_lidos))
                table.setColumnCount(10)
                for i in range(0, len(dados_lidos)):
                    for j in range(0, 10):
                        table.setItem(i, j, QTableWidgetItem(str(dados_lidos[i][j])))
            except Exception as error:
                debug.printError(error)


    def deleteFun(self, cpf):
        self.cursor.execute(f"DELETE FROM padaria.funcionario WHERE cpf = '{cpf}' ")
        self.cursor.commit()

    def updateTableFun(self, fullDataSet):
        for indice, valor in enumerate(fullDataSet):
            if valor == "None" or valor == "":
                fullDataSet.pop(indice)
                fullDataSet.insert(indice, None)
        self.cursor.execute(
            f"""
        UPDATE padaria.endereco 
        SET bairro = ?,rua = ?,numero = ?,cidade = ?,uf = ?,cep = ?
        FROM padaria.endereco AS E
        INNER JOIN padaria.funcionario AS F ON E.idEndereco = F.idEndereco
        WHERE F.cpf = ? """,
            (
                fullDataSet[7],
                fullDataSet[8],
                fullDataSet[9],
                fullDataSet[10],
                fullDataSet[11],
                fullDataSet[12],
                fullDataSet[0],
            ),
        )
        self.cursor.execute(
            f""" UPDATE padaria.funcionario SET cpf = ?, nome = ?, sobrenome = ?, senha = ?, cargo = ?, salario = ?,telefone = ? WHERE cpf = ?""",
            (
                fullDataSet[0],
                fullDataSet[1],
                fullDataSet[2],
                fullDataSet[3],
                fullDataSet[4],
                fullDataSet[5],
                fullDataSet[6],
                fullDataSet[0],
            ),
        )
        self.cursor.commit()


# if __name__ == "__main__":
#     a = Connect("BD23333", "BD23333")
#     a.Login()
