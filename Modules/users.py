from Modules import database, validator
import hashlib

class user:
    def __init__(self, user):
        self.__ID = user[0]
        self.__Name = user[1]
        self.__TYPE = user[2]
        
class new_user:
    def __init__(self, name, senha, type, email, celular, rg, cpf, cep, numero, complemento = ""):
        """Cadastramento de um novo usuario"""
        #hashiando senha
        self.senha = hashlib.sha256(senha).digest()
        self.name =  name
        self.email = email
        self.celular = celular
        self.rg = rg
        self.cpf = cpf
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.type = type
    
    def cadastrar(self):
        """Efetua o cadastro"""
        try:
            if self.validacao == True:
                data = [self.name, self.senha, self.type, self.email, self.celular, self.rg, self.cpf, self.cep, self.numero, self.complemento]
                return database.user().cadastrar_user(data)
            else:
                return False, "DADOS INVALIDOS"
        except AttributeError:
            return False, "DADOS NÃO FORAM VALIDADOS"
            
    def validar(self):
        """Valida os dados do Usuario"""
        self.validacao = True
        email = validator.email(self.email)
        if email[0] == False:
            self.validacao = False
            return email
        elif validator.cpf(self.cpf) == False:
            self.validacao = False
            return False, "CPF INVALIDO"
        elif validator.cep(self.cep)[0] == False:
            self.validacao = False
            return validator.cep(self.cep)
        
        else:
            self.email = email
            self.validacao = True
            return True
        
        
class get_user:
    def __init__(self, Name, Senha):
        """Obtem dados de um usuario"""
        self.Senha = Senha
        self.__USER = database.user().get_user(Name)
        
    def password_verify(self, password_db, password_user):
        """Verifica se a senha esta correta"""
        if hashlib.sha256(password_user).digest() == password_db:
            return True
            
    @property
    def USER(self):
        """Retorna o usuario se a senha estiver correta se não retorna False"""
        if self.__USER != False and self.password_verify(self.__USER[1][2], self.Senha):
            user = self.__USER[1][0:2]
            user += self.__USER[1][3:]
            return user
        else:
            return False, "USUARIO OU SENHA INVALIDO"