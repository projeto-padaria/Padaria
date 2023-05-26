import pyodbc as bd
import os
import getpass as gp

class Connect:
    def __init__(self) -> None:
        self.server = 'regulus.cotuca.unicamp.br'
        self.username = None
        self.password = None
        self.database = self.username

    def Login(self) -> None:
        self.username = str(input('Username: '))
        self.password = str(input('Senha: '))
