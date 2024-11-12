import datetime

import requests
from infra.DataBase.Connection import ConnectionDB
class Logs:
    def __init__(self, recognation_id: str = '', user_id: str = "", access_time: datetime.datetime = "", status:str = "") -> None:
        self.recognation_id = recognation_id
        self.user_id = user_id
        self.access_time = access_time
        self.status = status 
        self.connection = ConnectionDB()
        

    def register(self):
        print(str(self.recognation_id))
        print(self.user_id)
        print(self.access_time)
        print(self.status)
        url = "http://httpbin.org/delay/3"
        self.connection.open()
        result = self.connection.query(
            "SELECT * FROM recognation_logs WHERE user_id = ? AND DATE(access_time) = DATE('now') LIMIT 1", (self.user_id,))
        if(result):
            self.connection.close()
            raise Exception("Log ja registrado")
        try:
            print("Enviando requisição de log com timeout...")
            self.connection.query(
        "INSERT INTO recognation_logs (recognation_id, user_id, access_time, status) VALUES (?, ?, ?, ?)",
        (str(self.recognation_id), self.user_id, datetime.datetime.now(), self.status))
            self.connection.close()
            response = requests.post(url, timeout=3)  # Timeout configurado para 3 segundos
            if response.status_code == 200:
                print("Requisição enviada com sucesso!")
                return True  # Retorna True se o log for enviado com sucesso
            else:
                print(f"Erro ao enviar a requisição: {response.status_code}")
                return False  # Retorna False se houver erro
        except requests.exceptions.Timeout:
            print("Erro de Timeout: A requisição demorou mais que o esperado!")
            return False  # Retorna False em caso de timeout
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return False
