import threading
import datetime
import uuid
from models.Logs import Logs  # Suponha que a classe Logs esteja em logs.py

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
