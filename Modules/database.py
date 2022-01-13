from os import sep
import sqlite3
from random import randint

class user:
    def __init__(self):
        self.LOCAL = "Dados" + sep + "Users.db" #, Local do arquivo
        self.connect() #Cria a conexão
        self.create_tables() #Cria as tabelas se elas não existirem
        
    def connect(self):
        """Cria uma conexão com o banco de dados e cria o cursor"""
        self.CONECTOR = sqlite3.connect(self.LOCAL)
        self.CURSOR = self.CONECTOR.cursor()
        
    def create_tables(self):
        """Cria as tabelas caso elas não existão"""
        self.CURSOR.execute("""CREATE TABLE IF NOT EXISTS Usuarios(ID INTERGER PRIMARY KEY, 
        Nome TEXT NOT NULL UNIQUE, 
        Senha TEXT NOT NULL, 
        Tipo TEXT NOT NULL, 
        Email TEXT NOT NULL, 
        Celular TEXT NOT NULL, 
        RG TEXT NOT NULL, 
        CPF TEXT NOT NULL, 
        CEP TEXT NOT NULL,
        Numero INTERGER NOT NULL,
        Complemento TEXT)""")
        
    def cadastrar_user(self, data):
        """Realiza o cadastro de um usuario
        data -> deve conter uma lista com todos os dados do usuario"""
        
        #Realiza o cadastro
        try:
            self.CURSOR.execute("INSERT INTO Usuarios(ID, Nome, Senha, Tipo, Email, Celular, RG, CPF, CEP, Numero, Complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (randint(100000000, 999999999), data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
        
        except sqlite3.IntegrityError as erro:
            print(str(erro) + "\nModulo: Database  \nFunção: cadastrar_user")
            return False, "NOME DE USUÁRIO JÁ CADASTRADO OU DADOS FALTANDO"
        
        #salva o cadastro
        self.CONECTOR.commit()
        
        #finaliza a conexão
        self.CONECTOR.close()
        
        return True, "CADASTRO REALIZADO COM SUCESSO"
        
    def get_user(self, name):
        """Pega um usuario
        name -> deve conter o nome do usuario"""
        resultado = self.CURSOR.execute("SELECT * FROM Usuarios  WHERE Nome = ?", (name, )).fetchall()
        self.CONECTOR.close()
        
        if len(resultado) != 0:
            return True, resultado[0]
        else:
            return False, "USUARIO NÃO ENCONTRADO"