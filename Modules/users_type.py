import json
from os import sep

class types:
    def __init__(self):
        self.localfile = "Dados" + sep + "Configuracoes.json"
        
    def get_users_types(self):
        with open(self.localfile, "r") as arq:
            data = json.load(arq)
            data = data["Users_Types"]
            
        return True, data.keys()
        
    def get_users_permissions(self, user_type):
        with open(self.localfile, "r") as arq:
            data = json.load(arq)
            data = data["Users_Types"]
        try:
            return True, data[user_type]
        except KeyError:
            return False, "TIPO DE USUARIO NÃO EXISTENTE"
        
    def create_frisht_types(self):
        with open(self.localfile, "a+") as arq:
            try:
                self.get_users_types()
            except: # json.decoder.JSONDecodeError:
                frisht_data = {"Users_Types": {"Dono":{"Receber_Entregas":False,
                                                       "Entregas": True,
                                                       "Entregas_Realizadas": True,
                                                       "Entregas_Ausente": True,
                                                       "Entregas_Pendentes": True,
                                                       "Relatorio_Das_Entregas": True,
                                                       "Suas_Entregas": False,
                                                       "Suas_Entregas_Realizadas": False,
                                                       "Suas_Entregas_Ausente": False,
                                                       "Suas_Entregas_Pendentes": False,
                                                       "Relatorio_Das_Suas_Entregas": False,
                                                       "Cadastrar_Usuario": {"Typo": ["all"]},
                                                       "Cadastrar_Usuario_Secundary": {"New_User_Type": ["all"], "User_Type": ["all"]},
                                                       "Usuarios": True,
                                                       "Usuarios_Secundary": True,
                                                       "Seus_Usuarios": True,
                                                       "Tipos_de_Usuarios": True,
                                                       "Modificar_Tipo_de_Usuario": True,
                                                       "Modificar_Seu_Tipo_de_Usuario": True},
                                          "Adm":{"Receber_Entregas":False,
                                                       "Entregas": True,
                                                       "Entregas_Realizadas": True,
                                                       "Entregas_Ausente": True,
                                                       "Entregas_Pendentes": True,
                                                       "Relatorio_Das_Entregas": True,
                                                       "Suas_Entregas": False,
                                                       "Suas_Entregas_Realizadas": False,
                                                       "Suas_Entregas_Ausente": False,
                                                       "Suas_Entregas_Pendentes": False,
                                                       "Relatorio_Das_Suas_Entregas": False,
                                                       "Cadastrar_Usuario": {"Typo": ["Entregador", "Supervisor"]},
                                                       "Cadastrar_Usuario_Secundary": {"New_User_Type": ["Entregador"], "User_Type": ["Supervisor"]},
                                                       "Usuarios": True,
                                                       "Usuarios_Secundary": True,
                                                       "Seus_Usuarios": True,
                                                       "Tipos_de_Usuarios": True,
                                                       "Modificar_Tipo_de_Usuario": False,
                                                       "Modificar_Seu_Tipo_de_Usuario": False},
                                          "Entregador":{"Receber_Entregas":True,
                                                       "Entregas": False,
                                                       "Entregas_Realizadas": False,
                                                       "Entregas_Ausente": False,
                                                       "Entregas_Pendentes": False,
                                                       "Relatorio_Das_Entregas": False,
                                                       "Suas_Entregas": True,
                                                       "Suas_Entregas_Realizadas": True,
                                                       "Suas_Entregas_Ausente": True,
                                                       "Suas_Entregas_Pendentes": True,
                                                       "Relatorio_Das_Suas_Entregas": True,
                                                       "Cadastrar_Usuario": {"Typo": [None]},
                                                       "Cadastrar_Usuario_Secundary": {"New_User_Type": [None], "User_Type": [None]},
                                                       "Usuarios": None,
                                                       "Usuarios_Secundary": None,
                                                       "Seus_Usuarios": None,
                                                       "Tipos_de_Usuarios": None,
                                                       "Modificar_Tipo_de_Usuario": None,
                                                       "Modificar_Seu_Tipo_de_Usuario": None},
                                          "Supervisor":{"Receber_Entregas":False,
                                                       "Entregas": True,
                                                       "Entregas_Realizadas": True,
                                                       "Entregas_Ausente": True,
                                                       "Entregas_Pendentes": True,
                                                       "Relatorio_Das_Entregas": True,
                                                       "Suas_Entregas": False,
                                                       "Suas_Entregas_Realizadas": False,
                                                       "Suas_Entregas_Ausente": False,
                                                       "Suas_Entregas_Pendentes": False,
                                                       "Relatorio_Das_Suas_Entregas": False,
                                                       "Cadastrar_Usuario": {"Typo": ["Entregador"]},
                                                       "Cadastrar_Usuario_Secundary": {"New_User_Type": ["Entregador"], "User_Type": ["Supervisor"]},
                                                       "Usuarios": True,
                                                       "Usuarios_Secundary": True,
                                                       "Seus_Usuarios": True,
                                                       "Tipos_de_Usuarios": True,
                                                       "Modificar_Tipo_de_Usuario": False,
                                                       "Modificar_Seu_Tipo_de_Usuario": False}}}
                arq.write(json.dumps(frisht_data))