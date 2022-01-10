import database

class user:
    def __init__(self, data, type, entregas):
        self.ID = data[0]
        self.Name = data[1]
        self.TYPE = type
        self.ENTREGAS = entregas
        
class new_user:
    def __init__(self, name, email, number, rg, cpf, cep, type):
        self.DATA = [name, type, email, number, rg, cpf, cep]
    
    def cadastar(self):
        database.user().cadastrar_user(self.DATA)
        