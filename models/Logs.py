import datetime
import time
import requests
class Logs:
    def __init__(self, recognation_id: int, user_id: str, access_time: datetime.datetime, status:str) -> None:
        self.recognation_id = recognation_id
        self.user_id = user_id
        self.access_time = access_time
        self.status = status 
        

    def register(self):
        url = "http://exemplo.com/api/reconhecimento"
        dados = {
            "nome": "",
            "curso": "",
            "codigo_matricula": "",
        }
        try:
            response = requests.post(url, json=dados)
            if response.status_code == 200:
                print("Requisição enviada com sucesso")
            else:
                print(f"Erro ao enviar a requisição: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
