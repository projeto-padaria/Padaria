import pyodbc as bd
from os import system as clearTerminal
from time import sleep as wait
from getpass import getpass

global cursor

class Connect:
    def __init__(self) -> None:
        self.server = 'regulus.cotuca.unicamp.br'
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.username = None
        self.password = None
        self.database = None
        self.cursor = None
        self.table = None
        self.query = None
        self.schema = 'padaria'

    def Login(self, option) -> None:
        clearTerminal('cls')
        match option:
            case 1:
                self.username = input('Usuário: ')
                self.database = self.username
                self.password = getpass('Senha: ')
            case _:
                self.username = 'BD23333'
                self.database = self.username
                self.password = 'BD23333'
        try:
            self.cursor = bd.connect(
                f'DRIVER={self.driver};SERVER={self.server};UID={self.username};PWD={self.password};DATABASE={self.database}').cursor()
            return self.cursor # type: ignore
        except Exception:
            print('Login falha\n')

class Login():
    def __init__(self) -> None:
        self.cursor = Connect().Login(0)
        self.usuario = 'cpf'
        self.senha = 'senha'
        self.schema = 'padaria'
        self.table = 'funcionario'

    def Table_function(self) -> None:
        for row in self.cursor.execute(f'SELECT * FROM {self.schema}.{self.table}'): # type: ignore
            print(row)

    def AuthUser(self, CPF, senha) -> bool:
        try:
            if self.cursor.execute(f'SELECT {self.usuario} FROM {self.schema}.{self.table} WHERE {self.usuario} = {CPF} and {self.senha} = {senha}'): # type: ignore
                print('Usuário existe')
                return True
            else:
                print('Senha incorreta ou usuário não existe')
                return False
        except Exception as error:
            print('Login falhou', error)
            return False