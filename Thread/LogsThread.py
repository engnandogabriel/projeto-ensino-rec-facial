import threading
from models.Logs import Logs 

class LogThread(threading.Thread):
    def __init__(self, logs: Logs):
        super().__init__()
        self.logs = logs

    def run(self):
        try:
            self.logs.register()
            print("Log registrado com sucesso.")
        except Exception as e:
            print(f"Erro ao registrar log: {e}")
