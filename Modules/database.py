from os import sep
import sqlite3
from random import randint

class user:
    def __init__(self):
        self.LOCAL = "Dados" + sep + "Users.db"
        
    def connect(self):
        self.CONECTOR = sqlite3.connect(self.LOCAL)
        self.CURSOR = self.CONECTOR.cursor()
        self.create_tables()
        
    def create_tables(self):
        self.CURSOR.execute("CREATE TABLE IF NOT EXISTS Usuarios(ID interger primary key, Nome text, Tipo text, Email text, Numero text, RG text, CPF text, CEP text)")
        
    def cadastrar_user(self, data):
        self.CURSOR.execute("INSERT INTO Usuarios(ID, Nome, Tipo, Email, Numero, RG, CPF, CEP) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (randint(100000000, 999999999), data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        self.CONECTOR.close()
        