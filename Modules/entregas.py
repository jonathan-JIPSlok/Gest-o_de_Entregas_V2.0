from os import sep
import json
from Modules import validator
from random import randint

class new_entrega:
     def __init__(self, user_id, destinatario, celular, rg, cpf, cep, numero, complemento = ""):
         self.datajson = {"Destinatario":destinatario, "RG":rg, "CPF": None,"Celular":celular}
         self.user_id = user_id
         self.cpf = cpf
         self.cep = cep
         self.numero = numero
         self.complemento = complemento
         self.status = (False, "Nada")
         
     def validar(self):
         """Valida os dados da entrega, cpf do cliente e cep"""
         endereco = validator.cep(self.cep)
         if validator.cpf(self.cpf) == False:
             self.status = (False, "CPF INVALIDO")
         elif endereco[0] == False:
             self.status = (False, "CEP INVALIDO")
         else:
             self.status = (True, "DADOS VALIDOS")
             self.create_dict(endereco)
             
     def create_dict(self, endereco):
         """Adiciona o endereco é os dados que faltam ao dicionario que sera criado o JSON"""
         self.datajson["CPF"] = self.cpf
         for k,  v in endereco[1].items():
             if k != "ibge" and k != "ddd" and k != "gia" and k != "siafi":
                 self.datajson[k.title()] = v
             
         self.datajson["Numero"] = self.numero
         self.datajson["Complemento"] = self.complemento
         self.status = (True, "DICIONARIO CRIADO" )
         
     def write_json(self):
             """Escreve os dados no JSON"""
             data = {"Entregas": [{self.user_id: self.datajson}]}
             try:
                 with open("Dados" + sep + "Entregas.json", "r") as arq_leitura:
                     leitura = json.load(arq_leitura)
                     [data["Entregas"].append(item) for item in leitura["Entregas"]]
             except FileNotFoundError:
                 pass
             except TypeError:
                 pass
                 
             with open('Dados' + sep + 'Entregas.json', 'w') as arq:
                 arq.write(json.dumps(data))
             self.status = (True, "ENTREGA SALVA NO ARQUIVO JSON")
             
     def __str__(self):
         return str(self.status)
         
         
class get_entrega:
    """Retorna as entregas de um usuario"""
    def __init__(self, id):
        self.id = id
        self.local_file = "Dados" + sep + "Entregas.json"
        
    def open_file(self):
        """Abre o arquivo e retorna as entregas"""
        try:
            with open(self.local_file, "r") as arq:
                dados = json.load(arq)
        except FileNotFoundError as error:
            print(f"Modulo entregas \nclass get_entrega \ndef open_file \n{error}")
            return False, "NENHUMA ENTREGA ENCONTRADA"
        entregas = []
        for entrega in dados["Entregas"]:
            if list(entrega.keys())[0] == self.id:
                entregas.append(entrega)
        return True, entregas