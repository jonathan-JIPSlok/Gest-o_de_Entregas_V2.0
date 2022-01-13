import re
from validate_docbr import CPF
import requests
import json

def cpf(cpf):
    return CPF().validate(cpf)

def cep(cep):
    try:
        requisicao = requests.get(f"http://viacep.com.br/ws/{cep}/json/unicode")
    except requests.exceptions.ConnectionError:
        return False, "FALHA AO CONECTAR A INTERNET"
    try:
        if json.loads(requisicao.text)['erro'] == True:
            return False, "CEP INVALIDO"
    except:
        pass
    try:
        return True, json.loads(requisicao.text)
    except json.decoder.JSONDecodeError:
        return False, "CEP INVALIDO"
    
    
def email(email):
    verificador = re.compile("\w*@\w*.com")
    try:
        return verificador.search(email).group()
    except AttributeError:
        return False, "E-MAIL INVALIDO"