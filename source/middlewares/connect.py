import pyodbc as bd
from os import system as clearTerminal
from time import sleep as wait
from getpass import getpass

class Connect:
    def __init__(self) -> None:
        self.server = 'regulus.cotuca.unicamp.br'
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.username = None
        self.password = None
        self.database = None
        self.schema = 'padaria'
        self.table = None
        self.query = None
        self.RED   = '\033[1;31m'  
        self.BLUE  = '\033[1;34m'
        self.CYAN  = '\033[1;36m'
        self.GREEN = '\033[0;32m'
        self.RESET = '\033[0;0m'
        self.BOLD    = '\033[;1m'
        self.REVERSE = '\033[;7m'
        self.YELLOW  = '\033[33m'

    # debug functions

    def printError(self, error) -> None:
        return print(f'{self.BOLD}{self.RED}ERROR: {self.RESET}{error}')
    
    def printSuccess(self, success) -> None:
        return print(f'{self.BOLD}{self.GREEN}SUCCESS: {self.RESET}{success}')
    
    def printWarning(self, warning) -> None:
        return print(f'{self.BOLD}{self.YELLOW}WARNING: {self.RESET}{warning}')
    
    def printInfo(self, info) -> None:
        return print(f'{self.BOLD}{self.CYAN}INFO: {self.RESET}{info}')
    
    def printTitle(self, title) -> None:
        menubar = '—' * len(title)
        return print(f'{self.BOLD}{menubar} {title} {menubar} {self.RESET}')
    
    # funções de execução

    def tryAgain(self,function) -> None:
        user_choice = input('Você quer tentar novamente? [S/N] ').lower()
        if user_choice == 's' or user_choice == 'sim':
            wait(5)
            return function()
        elif user_choice == 'n' or user_choice == 'não' or user_choice == 'nao':
            print('Finalizando...')
            return wait(5)
        else:
            self.printError('Opção inválida')
            return self.tryAgain(function)

    def Login(self) -> None:
        clearTerminal('cls')
        self.printTitle('Login')
        self.username = input('Usuário: ')
        self.database = self.username
        self.password = getpass('Senha: ')
        try:
            cursor = bd.connect(
                f'DRIVER={self.driver};SERVER={self.server};UID={self.username};PWD={self.password};DATABASE={self.database}').cursor()
            self.printSuccess('Login feito com sucesso!')
            wait(2)
            self.menu(cursor)
        except Exception as error:
            print('Login falha\n')
            self.printError(error)
            self.tryAgain(lambda: self.Login())

    def menu(self, cursor) -> None:
        clearTerminal('cls')
        self.printTitle('Menu')
        print('1 - Executar consulta')
        print('0 - Sair')
        user_choice = input('O que você quer fazer? ')
        match user_choice:
            case '1':
                return self.selectTable(cursor)
            case '0':
                print('Finalizando...')
                wait(5)
            case _:
                self.printError('Opção inválida')
                self.tryAgain(lambda: self.menu(cursor))

    def selectTable(self, cursor) -> None:
        clearTerminal('cls')
        try:
            self.printTitle('Tabelas disponíveis')
            for table in cursor.tables():
                if table.table_schem == self.schema:
                    print(table.table_name)
            self.table = input('Qual tabela você quer acessar? ').lower()
            self.printSuccess('Tabela selecionada com sucesso!')
            self.selectQuery(cursor)
           
        except Exception as error:
            self.printError(error)
            self.tryAgain(lambda: self.menu(cursor))

    def selectQuery(self, cursor) -> None:
        clearTerminal('cls')
        try:
            self.printTitle('Colunas disponíveis')
            for query in cursor.columns(table=self.table):
                print(query.column_name)
            self.query = input('Qual coluna você quer acessar? ').lower()
            self.printSuccess('Coluna selecionada com sucesso!')
            self.execute(cursor)
        except Exception as error:
            self.printError(error)
            self.tryAgain(lambda: self.menu(cursor))


    def execute(self, cursor) -> None:
        clearTerminal('cls')
        wait(2)
        try:
            self.printTitle('Resultado')
            for row in cursor.execute(f'SELECT {self.query} FROM {self.schema}.{self.table}'):
                print(row)
            self.printSuccess('Consulta feita com sucesso!')
            self.tryAgain(lambda: self.menu(cursor))
        except Exception as error:
            self.printError(error)
            self.tryAgain(lambda: self.menu(cursor))

if __name__ == '__main__':
    Connect().Login()