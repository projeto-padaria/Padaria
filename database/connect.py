import pyodbc as bd
import os
from getpass import getpass

class Connect:
    def __init__(self) -> None:
        self.server = 'regulus.cotuca.unicamp.br'
        self.username = None
        self.password = None
        self.database = self.username

    def Login(self) -> None:
        self.username = str(input('Username: '))
        self.password = getpass('Password: ')

        bd.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}')


Connect().Login()
